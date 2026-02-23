"""
Concise table renderer for nf-docs.

Outputs pipeline documentation as compact Markdown tables inspired by
terraform-docs.  Each section is a ``## Heading`` followed by one or more
dense Markdown tables — no prose, no per-item sub-sections, just scannable
reference data.  Supports marker-based injection into existing README files.
"""

from pathlib import Path

from nf_docs.generation_info import get_markdown_footer
from nf_docs.models import Pipeline, PipelineInput, Process, Workflow
from nf_docs.renderers.base import BaseRenderer

BEGIN_MARKER = "<!-- BEGIN_NF_DOCS -->"
END_MARKER = "<!-- END_NF_DOCS -->"


def inject_into_content(existing: str, new_content: str) -> str | None:
    """
    Replace text between ``BEGIN_NF_DOCS`` and ``END_NF_DOCS`` markers.

    Args:
        existing: The full text of the file that may contain markers.
        new_content: The rendered documentation to inject.

    Returns:
        The updated text with *new_content* between the markers, or ``None``
        if the markers were not found.
    """
    begin_idx = existing.find(BEGIN_MARKER)
    end_idx = existing.find(END_MARKER)
    if begin_idx == -1 or end_idx == -1 or end_idx <= begin_idx:
        return None

    before = existing[: begin_idx + len(BEGIN_MARKER)]
    after = existing[end_idx:]
    return f"{before}\n{new_content}\n{after}"


class ConciseRenderer(BaseRenderer):
    """
    Render pipeline documentation as compact Markdown tables.

    Modelled on the ``terraform-docs markdown table`` output format:
    a single document with heading-per-section and a dense table underneath.
    """

    # ------------------------------------------------------------------
    # Public API (BaseRenderer contract)
    # ------------------------------------------------------------------

    def render(self, pipeline: Pipeline) -> str:
        """
        Render the full pipeline as a single concise Markdown string.

        Args:
            pipeline: The Pipeline model to render.

        Returns:
            Concise Markdown string with all sections.
        """
        sections: list[str] = []

        sections.append(self._render_header(pipeline))

        if pipeline.inputs:
            sections.append(self._render_inputs(pipeline))

        if pipeline.config_params:
            sections.append(self._render_config(pipeline))

        if pipeline.workflows:
            sections.append(self._render_workflows(pipeline))

        if pipeline.processes:
            sections.append(self._render_processes(pipeline))

        if pipeline.functions:
            sections.append(self._render_functions(pipeline))

        content = "\n\n".join(sections)
        content += "\n\n" + get_markdown_footer()
        return content

    def render_to_directory(self, pipeline: Pipeline, output_dir: str | Path) -> list[Path]:
        """Write concise documentation to a single file inside *output_dir*.

        If the README.md already exists and contains ``<!-- BEGIN_NF_DOCS -->`` /
        ``<!-- END_NF_DOCS -->`` markers, the generated content is injected between
        them, leaving the rest of the file untouched.  Otherwise a new file is
        created with the markers wrapping the content.

        Args:
            pipeline: The Pipeline model to render.
            output_dir: Target directory (created if absent).

        Returns:
            List containing the single created/updated file path.
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        out_file = output_path / "README.md"
        content = self.render(pipeline)
        if out_file.exists():
            existing = out_file.read_text(encoding="utf-8")
            injected = inject_into_content(existing, content)
            if injected is not None:
                out_file.write_text(injected, encoding="utf-8")
                return [out_file]
        # No existing file or no markers — write with markers
        wrapped = f"{BEGIN_MARKER}\n{content}\n{END_MARKER}\n"
        out_file.write_text(wrapped, encoding="utf-8")
        return [out_file]

    # ------------------------------------------------------------------
    # Header
    # ------------------------------------------------------------------

    def _render_header(self, pipeline: Pipeline) -> str:
        """Render the top-level title and one-line summary."""
        title = self.get_title(pipeline)
        lines: list[str] = [f"# {title}"]

        parts: list[str] = []
        if pipeline.metadata.version:
            parts.append(f"**Version:** {pipeline.metadata.version}")
        if pipeline.metadata.description:
            parts.append(pipeline.metadata.description)
        if parts:
            lines.append("")
            lines.append(" · ".join(parts))

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Inputs
    # ------------------------------------------------------------------

    def _render_inputs(self, pipeline: Pipeline) -> str:
        """Render pipeline inputs as grouped tables."""
        lines: list[str] = ["## Inputs"]

        groups = pipeline.get_input_groups()
        for group_name, inputs in groups.items():
            lines.append("")
            lines.append(f"### {group_name}")
            lines.append("")
            lines.append("| Name | Description | Type | Default | Required |")
            lines.append("|------|-------------|------|---------|:--------:|")
            for inp in inputs:
                lines.append(self._input_row(inp))

        return "\n".join(lines)

    def _input_row(self, inp: PipelineInput) -> str:
        """Format a single input parameter as a table row."""
        name = f"`--{inp.name}`"
        desc = self._cell(inp.description)
        type_ = f"`{inp.type}`" if inp.type else "n/a"
        default = f"`{inp.default}`" if inp.default is not None else "n/a"
        required = "yes" if inp.required else "no"
        return f"| {name} | {desc} | {type_} | {default} | {required} |"

    # ------------------------------------------------------------------
    # Config parameters
    # ------------------------------------------------------------------

    def _render_config(self, pipeline: Pipeline) -> str:
        """Render non-input configuration parameters."""
        lines: list[str] = [
            "## Configuration",
            "",
            "| Name | Type | Default | Description |",
            "|------|------|---------|-------------|",
        ]
        for param in pipeline.config_params:
            name = f"`{param.name}`"
            type_ = f"`{param.type}`" if param.type else "n/a"
            default = f"`{param.default}`" if param.default is not None else "n/a"
            desc = self._cell(param.description)
            lines.append(f"| {name} | {type_} | {default} | {desc} |")

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Workflows
    # ------------------------------------------------------------------

    def _render_workflows(self, pipeline: Pipeline) -> str:
        """Render workflows as a summary table plus per-workflow I/O tables."""
        lines: list[str] = [
            "## Workflows",
            "",
            "| Name | Description | Entry |",
            "|------|-------------|:-----:|",
        ]
        for wf in pipeline.workflows:
            lines.append(self._workflow_row(wf))

        # Per-workflow detail: inputs / outputs (only when present)
        for wf in pipeline.workflows:
            detail = self._workflow_detail(wf, pipeline)
            if detail:
                lines.append("")
                lines.append(detail)

        return "\n".join(lines)

    def _workflow_row(self, wf: Workflow) -> str:
        """Format a single workflow as a summary table row."""
        name = f"`{wf.name}`" if wf.name else "*(entry)*"
        desc = self._cell(wf.meta_description or wf.docstring)
        entry = "yes" if wf.is_entry else "no"
        return f"| {name} | {desc} | {entry} |"

    def _workflow_detail(self, wf: Workflow, pipeline: Pipeline) -> str:
        """Render per-workflow inputs, outputs, and calls if present."""
        name = wf.name or "entry"
        sections: list[str] = []

        # Inputs
        if wf.meta_inputs or wf.inputs:
            rows: list[str] = [
                f"### `{name}` Inputs",
                "",
                "| Name | Description |",
                "|------|-------------|",
            ]
            if wf.meta_inputs:
                for inp in wf.meta_inputs:
                    n = f"`{inp.get('name', '')}`"
                    d = self._cell(inp.get("description"))
                    rows.append(f"| {n} | {d} |")
            else:
                for inp in wf.inputs:
                    rows.append(f"| `{inp.name}` | {self._cell(inp.description)} |")
            sections.append("\n".join(rows))

        # Outputs
        if wf.meta_outputs or wf.outputs:
            rows = [
                f"### `{name}` Outputs",
                "",
                "| Name | Description |",
                "|------|-------------|",
            ]
            if wf.meta_outputs:
                for out in wf.meta_outputs:
                    n = f"`{out.get('name', '')}`"
                    d = self._cell(out.get("description"))
                    rows.append(f"| {n} | {d} |")
            else:
                for out in wf.outputs:
                    rows.append(f"| `{out.name}` | {self._cell(out.description)} |")
            sections.append("\n".join(rows))

        # Calls
        if wf.calls:
            call_names = ", ".join(f"`{c}`" for c in wf.calls)
            sections.append(f"**`{name}` calls:** {call_names}")

        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    # Processes
    # ------------------------------------------------------------------

    def _render_processes(self, pipeline: Pipeline) -> str:
        """Render processes as a summary table plus per-process I/O tables."""
        lines: list[str] = [
            "## Processes",
            "",
            "| Name | Description |",
            "|------|-------------|",
        ]
        for proc in pipeline.processes:
            lines.append(self._process_row(proc))

        # Per-process detail: inputs / outputs
        for proc in pipeline.processes:
            detail = self._process_detail(proc)
            if detail:
                lines.append("")
                lines.append(detail)

        return "\n".join(lines)

    def _process_row(self, proc: Process) -> str:
        """Format a single process as a summary table row."""
        name = f"`{proc.name}`"
        desc = self._cell(proc.meta_description or proc.docstring)
        return f"| {name} | {desc} |"

    def _process_detail(self, proc: Process) -> str:
        """Render per-process inputs and outputs if present."""
        sections: list[str] = []

        # Inputs
        if proc.meta_inputs or proc.inputs:
            rows: list[str] = [
                f"### `{proc.name}` Inputs",
                "",
                "| Name | Type | Description |",
                "|------|------|-------------|",
            ]
            if proc.meta_inputs:
                for inp in proc.meta_inputs:
                    n = f"`{inp.get('name', '')}`"
                    t = f"`{inp.get('type', '-')}`"
                    d = self._cell(inp.get("description"))
                    rows.append(f"| {n} | {t} | {d} |")
            else:
                for inp in proc.inputs:
                    rows.append(f"| `{inp.name}` | `{inp.type}` | {self._cell(inp.description)} |")
            sections.append("\n".join(rows))

        # Outputs
        if proc.meta_outputs or proc.outputs:
            if proc.meta_outputs:
                rows = [
                    f"### `{proc.name}` Outputs",
                    "",
                    "| Name | Type | Pattern | Description |",
                    "|------|------|---------|-------------|",
                ]
                for out in proc.meta_outputs:
                    n = f"`{out.get('name', '')}`"
                    t = f"`{out.get('type', '-')}`"
                    p = f"`{out.get('pattern', '-')}`" if out.get("pattern") else "n/a"
                    d = self._cell(out.get("description"))
                    rows.append(f"| {n} | {t} | {p} | {d} |")
            else:
                rows = [
                    f"### `{proc.name}` Outputs",
                    "",
                    "| Name | Type | Emit | Description |",
                    "|------|------|------|-------------|",
                ]
                for out in proc.outputs:
                    emit = f"`{out.emit}`" if out.emit else "n/a"
                    rows.append(
                        f"| `{out.name}` | `{out.type}` | {emit}"
                        f" | {self._cell(out.description)} |"
                    )
            sections.append("\n".join(rows))

        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    # Functions
    # ------------------------------------------------------------------

    def _render_functions(self, pipeline: Pipeline) -> str:
        """Render functions as a summary table."""
        lines: list[str] = [
            "## Functions",
            "",
            "| Name | Parameters | Returns | Description |",
            "|------|------------|---------|-------------|",
        ]
        for func in pipeline.functions:
            name = f"`{func.name}`"
            params = ", ".join(f"`{p.name}`" for p in func.params) if func.params else "n/a"
            returns = self._cell(func.return_description)
            desc = self._cell(func.docstring)
            lines.append(f"| {name} | {params} | {returns} | {desc} |")

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _cell(value: str | None) -> str:
        """Sanitise a value for use inside a Markdown table cell."""
        if not value:
            return "n/a"
        # Collapse newlines and pipes that would break the table
        return value.replace("\n", " ").replace("|", "\\|").strip()
