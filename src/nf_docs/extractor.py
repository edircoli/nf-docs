"""
Data extraction and merging for Nextflow pipeline documentation.

This module coordinates extraction from all data sources:
- Language Server (processes, workflows, functions)
- nextflow_schema.json (typed input parameters)
- nextflow.config (config parameters)
- README.md (pipeline description)

And merges them into a unified Pipeline model.
"""

import logging
import re
from pathlib import Path
from typing import Any

from nf_docs.config_parser import parse_config
from nf_docs.lsp_client import LSPClient, LSPError, SymbolKind, parse_hover_content
from nf_docs.models import (
    ConfigParam,
    Function,
    FunctionParam,
    Pipeline,
    PipelineInput,
    PipelineMetadata,
    Process,
    ProcessInput,
    ProcessOutput,
    Workflow,
    WorkflowInput,
    WorkflowOutput,
)
from nf_docs.schema_parser import find_schema_file, parse_schema

logger = logging.getLogger(__name__)


class ExtractionError(Exception):
    """Exception raised when data extraction fails."""

    pass


class PipelineExtractor:
    """
    Extracts documentation from a Nextflow pipeline.

    Coordinates extraction from multiple sources and merges them
    into a unified Pipeline model.
    """

    def __init__(
        self,
        workspace_path: str | Path,
        language_server_jar: str | Path | None = None,
        nextflow_path: str = "nextflow",
        use_lsp: bool = True,
        auto_download_lsp: bool = True,
    ):
        """
        Initialize the extractor.

        Args:
            workspace_path: Path to the Nextflow pipeline workspace
            language_server_jar: Path to the language server JAR (optional)
            nextflow_path: Path to the Nextflow executable
            use_lsp: Whether to use the Language Server for extraction
            auto_download_lsp: Whether to auto-download the language server
        """
        self.workspace_path = Path(workspace_path).resolve()
        self.language_server_jar = language_server_jar
        self.nextflow_path = nextflow_path
        self.use_lsp = use_lsp
        self.auto_download_lsp = auto_download_lsp

    def extract(self) -> Pipeline:
        """
        Extract all documentation from the pipeline.

        Returns:
            Complete Pipeline model with all extracted information
        """
        logger.info(f"Extracting documentation from: {self.workspace_path}")

        pipeline = Pipeline()

        # Extract from schema (has highest priority for inputs and metadata)
        schema_file = find_schema_file(self.workspace_path)
        if schema_file:
            logger.info(f"Found schema file: {schema_file}")
            try:
                schema_metadata, schema_inputs = parse_schema(schema_file)
                pipeline.metadata = schema_metadata
                pipeline.inputs = schema_inputs
            except Exception as e:
                logger.warning(f"Failed to parse schema: {e}")

        # Extract from config
        try:
            config_metadata, config_params = parse_config(
                self.workspace_path, self.nextflow_path
            )
            # Merge metadata (schema takes priority)
            pipeline.metadata = self._merge_metadata(pipeline.metadata, config_metadata)
            # Filter config params to exclude those already in inputs
            input_names = {inp.name for inp in pipeline.inputs}
            pipeline.config_params = [p for p in config_params if p.name not in input_names]
        except Exception as e:
            logger.warning(f"Failed to parse config: {e}")

        # Extract from README
        readme_description = self._extract_readme_description()
        if readme_description and not pipeline.metadata.description:
            pipeline.metadata.description = readme_description

        # Extract from Language Server
        if self.use_lsp:
            try:
                self._extract_from_lsp(pipeline)
            except LSPError as e:
                logger.warning(f"LSP extraction failed: {e}")
                logger.info("Falling back to regex-based extraction")
                self._extract_from_files(pipeline)
        else:
            self._extract_from_files(pipeline)

        # Infer pipeline name from directory if not set
        if not pipeline.metadata.name:
            pipeline.metadata.name = self.workspace_path.name

        logger.info(
            f"Extraction complete: {len(pipeline.workflows)} workflows, "
            f"{len(pipeline.processes)} processes, {len(pipeline.functions)} functions"
        )

        return pipeline

    def _merge_metadata(
        self, primary: PipelineMetadata, secondary: PipelineMetadata
    ) -> PipelineMetadata:
        """Merge metadata, with primary taking precedence."""
        return PipelineMetadata(
            name=primary.name or secondary.name,
            description=primary.description or secondary.description,
            version=primary.version or secondary.version,
            homepage=primary.homepage or secondary.homepage,
            repository=primary.repository or secondary.repository,
            authors=primary.authors or secondary.authors,
            license=primary.license or secondary.license,
        )

    def _extract_readme_description(self) -> str:
        """Extract description from README.md."""
        readme_candidates = [
            self.workspace_path / "README.md",
            self.workspace_path / "readme.md",
            self.workspace_path / "README.rst",
        ]

        for readme_path in readme_candidates:
            if readme_path.exists():
                try:
                    content = readme_path.read_text(encoding="utf-8")
                    # Extract first paragraph after title
                    return self._parse_readme_description(content)
                except Exception as e:
                    logger.debug(f"Failed to read README: {e}")

        return ""

    def _parse_readme_description(self, content: str) -> str:
        """Parse description from README content."""
        lines = content.split("\n")
        description_lines: list[str] = []
        in_description = False
        skip_badges = True

        for line in lines:
            stripped = line.strip()

            # Skip empty lines at start
            if not stripped and not in_description:
                continue

            # Skip title line
            if stripped.startswith("#") and not in_description:
                in_description = True
                continue

            # Skip badge lines (usually contain images/links at the start)
            if skip_badges and (
                stripped.startswith("[![")
                or stripped.startswith("![")
                or stripped.startswith("[!")
                or "badge" in stripped.lower()
            ):
                continue

            skip_badges = False

            # Stop at next heading or horizontal rule
            if stripped.startswith("#") or stripped.startswith("---"):
                break

            # Collect description lines
            if in_description:
                if stripped:
                    description_lines.append(stripped)
                elif description_lines:
                    # Stop at empty line after content
                    break

        return " ".join(description_lines)

    def _extract_from_lsp(self, pipeline: Pipeline) -> None:
        """Extract processes, workflows, and functions using the Language Server."""
        # Find all Nextflow files
        nf_files = list(self.workspace_path.rglob("*.nf"))
        if not nf_files:
            logger.warning("No .nf files found in workspace")
            return

        logger.info(f"Found {len(nf_files)} Nextflow files")

        try:
            with LSPClient(
                self.workspace_path,
                server_jar=self.language_server_jar,
                auto_download=self.auto_download_lsp,
            ) as client:
                for nf_file in nf_files:
                    try:
                        self._extract_file_symbols(client, nf_file, pipeline)
                    except Exception as e:
                        logger.warning(f"Failed to extract from {nf_file}: {e}")
        except LSPError as e:
            raise LSPError(f"Failed to start language server: {e}") from e

    def _extract_file_symbols(
        self, client: LSPClient, file_path: Path, pipeline: Pipeline
    ) -> None:
        """Extract symbols from a single file using LSP."""
        relative_path = file_path.relative_to(self.workspace_path)
        logger.debug(f"Processing: {relative_path}")

        # Open the document
        client.open_document(file_path)

        try:
            # Get document symbols
            symbols = client.get_document_symbols(file_path)

            for symbol in symbols:
                self._process_symbol(client, file_path, symbol, pipeline)

        finally:
            client.close_document(file_path)

    def _process_symbol(
        self,
        client: LSPClient,
        file_path: Path,
        symbol: dict[str, Any],
        pipeline: Pipeline,
    ) -> None:
        """Process a document symbol and add to pipeline."""
        name = symbol.get("name", "")
        kind = symbol.get("kind", 0)
        range_info = symbol.get("range", {})
        selection_range = symbol.get("selectionRange", range_info)

        # Get the line and character for hover
        start = selection_range.get("start", {})
        line = start.get("line", 0)
        character = start.get("character", 0)

        relative_path = str(file_path.relative_to(self.workspace_path))

        # Get hover information for docstring
        hover = client.get_hover(file_path, line, character)
        docstring, param_docs = parse_hover_content(hover)

        # Determine what kind of symbol this is
        if kind == SymbolKind.METHOD or "process" in name.lower():
            # This might be a process
            process = self._create_process_from_symbol(
                name, docstring, param_docs, relative_path, line + 1, symbol
            )
            if process and not any(p.name == process.name for p in pipeline.processes):
                pipeline.processes.append(process)

        elif kind == SymbolKind.CLASS:
            # This might be a workflow
            workflow = self._create_workflow_from_symbol(
                name, docstring, param_docs, relative_path, line + 1, symbol
            )
            if workflow and not any(w.name == workflow.name for w in pipeline.workflows):
                # Check if this is the entry workflow
                if name.lower() in ("main", "entry", ""):
                    workflow.is_entry = True
                pipeline.workflows.append(workflow)

        elif kind == SymbolKind.FUNCTION:
            # This is a function
            function = self._create_function_from_symbol(
                name, docstring, param_docs, relative_path, line + 1, symbol
            )
            if function and not any(f.name == function.name for f in pipeline.functions):
                pipeline.functions.append(function)

        # Process child symbols
        for child in symbol.get("children", []):
            self._process_symbol(client, file_path, child, pipeline)

    def _create_process_from_symbol(
        self,
        name: str,
        docstring: str,
        param_docs: dict[str, str],
        file_path: str,
        line: int,
        symbol: dict[str, Any],
    ) -> Process | None:
        """Create a Process from an LSP symbol."""
        process = Process(
            name=name,
            docstring=docstring,
            file=file_path,
            line=line,
        )

        # Extract inputs and outputs from children
        for child in symbol.get("children", []):
            child_name = child.get("name", "")
            child_kind = child.get("kind", 0)

            if "input" in child_name.lower() or child_kind == SymbolKind.PROPERTY:
                # Parse input declaration
                inp = ProcessInput(
                    name=child_name,
                    type="val",  # Will be refined by parsing
                    description=param_docs.get(child_name, ""),
                )
                process.inputs.append(inp)
            elif "output" in child_name.lower():
                # Parse output declaration
                out = ProcessOutput(
                    name=child_name,
                    type="path",  # Will be refined by parsing
                    description=param_docs.get(child_name, ""),
                )
                process.outputs.append(out)

        return process

    def _create_workflow_from_symbol(
        self,
        name: str,
        docstring: str,
        param_docs: dict[str, str],
        file_path: str,
        line: int,
        symbol: dict[str, Any],
    ) -> Workflow | None:
        """Create a Workflow from an LSP symbol."""
        workflow = Workflow(
            name=name,
            docstring=docstring,
            file=file_path,
            line=line,
        )

        # Extract take/emit and calls from children
        for child in symbol.get("children", []):
            child_name = child.get("name", "")

            if "take" in child_name.lower():
                inp = WorkflowInput(
                    name=child_name,
                    description=param_docs.get(child_name, ""),
                )
                workflow.inputs.append(inp)
            elif "emit" in child_name.lower():
                out = WorkflowOutput(
                    name=child_name,
                    description=param_docs.get(child_name, ""),
                )
                workflow.outputs.append(out)

        return workflow

    def _create_function_from_symbol(
        self,
        name: str,
        docstring: str,
        param_docs: dict[str, str],
        file_path: str,
        line: int,
        symbol: dict[str, Any],
    ) -> Function | None:
        """Create a Function from an LSP symbol."""
        function = Function(
            name=name,
            docstring=docstring,
            file=file_path,
            line=line,
            return_description=param_docs.get("_return", ""),
        )

        # Extract parameters from children
        for child in symbol.get("children", []):
            child_name = child.get("name", "")
            param = FunctionParam(
                name=child_name,
                description=param_docs.get(child_name, ""),
            )
            function.params.append(param)

        return function

    def _extract_from_files(self, pipeline: Pipeline) -> None:
        """Fallback: Extract processes, workflows, and functions using regex."""
        nf_files = list(self.workspace_path.rglob("*.nf"))

        for nf_file in nf_files:
            try:
                content = nf_file.read_text(encoding="utf-8")
                relative_path = str(nf_file.relative_to(self.workspace_path))

                # Extract processes
                processes = self._extract_processes_regex(content, relative_path)
                for process in processes:
                    if not any(p.name == process.name for p in pipeline.processes):
                        pipeline.processes.append(process)

                # Extract workflows
                workflows = self._extract_workflows_regex(content, relative_path)
                for workflow in workflows:
                    if not any(w.name == workflow.name for w in pipeline.workflows):
                        pipeline.workflows.append(workflow)

                # Extract functions
                functions = self._extract_functions_regex(content, relative_path)
                for function in functions:
                    if not any(f.name == function.name for f in pipeline.functions):
                        pipeline.functions.append(function)

            except Exception as e:
                logger.warning(f"Failed to parse {nf_file}: {e}")

    def _extract_processes_regex(self, content: str, file_path: str) -> list[Process]:
        """Extract processes using regex patterns."""
        processes: list[Process] = []

        # Pattern to match process definitions with optional docstring
        process_pattern = re.compile(
            r"(?:/\*\*\s*(.*?)\s*\*/\s*)?"  # Optional Javadoc comment
            r"process\s+(\w+)\s*\{",  # Process declaration
            re.DOTALL,
        )

        for match in process_pattern.finditer(content):
            docstring = match.group(1) or ""
            name = match.group(2)
            line = content[: match.start()].count("\n") + 1

            # Clean up docstring
            docstring = self._clean_docstring(docstring)
            param_docs = self._parse_javadoc_params(match.group(1) or "")

            process = Process(
                name=name,
                docstring=docstring,
                file=file_path,
                line=line,
            )

            # Extract inputs and outputs from process body
            process_end = self._find_block_end(content, match.end() - 1)
            if process_end:
                process_body = content[match.end() : process_end]
                process.inputs = self._extract_process_inputs(process_body, param_docs)
                process.outputs = self._extract_process_outputs(process_body, param_docs)
                process.directives = self._extract_process_directives(process_body)

            processes.append(process)

        return processes

    def _extract_workflows_regex(self, content: str, file_path: str) -> list[Workflow]:
        """Extract workflows using regex patterns."""
        workflows: list[Workflow] = []

        # Pattern to match workflow definitions
        workflow_pattern = re.compile(
            r"(?:/\*\*\s*(.*?)\s*\*/\s*)?"  # Optional Javadoc comment
            r"workflow\s+(\w*)\s*\{",  # Workflow declaration (name optional for entry)
            re.DOTALL,
        )

        for match in workflow_pattern.finditer(content):
            docstring = match.group(1) or ""
            name = match.group(2) or ""  # Empty name = entry workflow
            line = content[: match.start()].count("\n") + 1

            docstring = self._clean_docstring(docstring)

            workflow = Workflow(
                name=name,
                docstring=docstring,
                file=file_path,
                line=line,
                is_entry=not name,  # Entry workflow has no name
            )

            # Extract workflow body
            workflow_end = self._find_block_end(content, match.end() - 1)
            if workflow_end:
                workflow_body = content[match.end() : workflow_end]
                workflow.inputs = self._extract_workflow_inputs(workflow_body)
                workflow.outputs = self._extract_workflow_outputs(workflow_body)
                workflow.calls = self._extract_workflow_calls(workflow_body)

            workflows.append(workflow)

        return workflows

    def _extract_functions_regex(self, content: str, file_path: str) -> list[Function]:
        """Extract functions using regex patterns."""
        functions: list[Function] = []

        # Pattern to match function definitions
        function_pattern = re.compile(
            r"(?:/\*\*\s*(.*?)\s*\*/\s*)?"  # Optional Javadoc comment
            r"def\s+(\w+)\s*\((.*?)\)\s*\{",  # Function declaration
            re.DOTALL,
        )

        for match in function_pattern.finditer(content):
            docstring = match.group(1) or ""
            name = match.group(2)
            params_str = match.group(3)
            line = content[: match.start()].count("\n") + 1

            docstring = self._clean_docstring(docstring)
            param_docs = self._parse_javadoc_params(match.group(1) or "")

            function = Function(
                name=name,
                docstring=docstring,
                file=file_path,
                line=line,
                return_description=param_docs.get("_return", ""),
            )

            # Parse parameters
            if params_str.strip():
                for param in params_str.split(","):
                    param = param.strip()
                    if param:
                        # Handle default values
                        if "=" in param:
                            param_name, default = param.split("=", 1)
                            param_name = param_name.strip()
                            default = default.strip()
                        else:
                            param_name = param
                            default = None

                        function.params.append(
                            FunctionParam(
                                name=param_name,
                                description=param_docs.get(param_name, ""),
                                default=default,
                            )
                        )

            functions.append(function)

        return functions

    def _find_block_end(self, content: str, start: int) -> int | None:
        """Find the end of a block starting at the given brace position."""
        depth = 0
        i = start

        while i < len(content):
            if content[i] == "{":
                depth += 1
            elif content[i] == "}":
                depth -= 1
                if depth == 0:
                    return i
            i += 1

        return None

    def _clean_docstring(self, docstring: str) -> str:
        """Clean up a Javadoc-style docstring."""
        if not docstring:
            return ""

        # Remove * from start of lines
        lines = docstring.split("\n")
        cleaned_lines: list[str] = []

        for line in lines:
            line = line.strip()
            if line.startswith("*"):
                line = line[1:].strip()
            # Stop at @param or @return
            if line.startswith("@"):
                break
            if line:
                cleaned_lines.append(line)

        return " ".join(cleaned_lines)

    def _parse_javadoc_params(self, docstring: str) -> dict[str, str]:
        """Parse @param and @return tags from a Javadoc comment."""
        params: dict[str, str] = {}

        if not docstring:
            return params

        # Find @param tags
        param_pattern = re.compile(r"@param\s+(\w+)\s+(.+?)(?=@\w|$)", re.DOTALL)
        for match in param_pattern.finditer(docstring):
            name = match.group(1)
            desc = match.group(2).replace("*", "").strip()
            desc = " ".join(desc.split())  # Normalize whitespace
            params[name] = desc

        # Find @return tag
        return_pattern = re.compile(r"@returns?\s+(.+?)(?=@\w|$)", re.DOTALL)
        match = return_pattern.search(docstring)
        if match:
            desc = match.group(1).replace("*", "").strip()
            desc = " ".join(desc.split())
            params["_return"] = desc

        return params

    def _extract_process_inputs(
        self, body: str, param_docs: dict[str, str]
    ) -> list[ProcessInput]:
        """Extract input declarations from a process body."""
        inputs: list[ProcessInput] = []

        # Find input block
        input_match = re.search(r"input:\s*(.*?)(?=output:|script:|shell:|exec:|$)", body, re.DOTALL)
        if not input_match:
            return inputs

        input_block = input_match.group(1)

        # Parse input declarations
        # Patterns: val x, path x, tuple val(x), path(y), etc.
        input_patterns = [
            (r"tuple\s+(.+)", "tuple"),
            (r"val\s*\(?(\w+)\)?", "val"),
            (r"path\s*\(?(['\"]?[\w.*]+['\"]?)\)?", "path"),
            (r"env\s+(\w+)", "env"),
            (r"stdin", "stdin"),
        ]

        for pattern, input_type in input_patterns:
            for match in re.finditer(pattern, input_block):
                if input_type == "stdin":
                    name = "stdin"
                else:
                    name = match.group(1).strip("'\"")

                inputs.append(
                    ProcessInput(
                        name=name,
                        type=input_type,
                        description=param_docs.get(name, ""),
                    )
                )

        return inputs

    def _extract_process_outputs(
        self, body: str, param_docs: dict[str, str]
    ) -> list[ProcessOutput]:
        """Extract output declarations from a process body."""
        outputs: list[ProcessOutput] = []

        # Find output block
        output_match = re.search(
            r"output:\s*(.*?)(?=script:|shell:|exec:|when:|$)", body, re.DOTALL
        )
        if not output_match:
            return outputs

        output_block = output_match.group(1)

        # Parse output declarations with emit
        # Pattern: path "*.txt", emit: name
        output_pattern = re.compile(
            r"(tuple|val|path|env|stdout)\s*\(?([^,\n]+)\)?"
            r"(?:,\s*emit:\s*(\w+))?",
            re.MULTILINE,
        )

        for match in output_pattern.finditer(output_block):
            output_type = match.group(1)
            name = match.group(2).strip().strip("'\"")
            emit = match.group(3) or ""

            outputs.append(
                ProcessOutput(
                    name=name,
                    type=output_type,
                    description=param_docs.get(emit or name, ""),
                    emit=emit,
                )
            )

        return outputs

    def _extract_process_directives(self, body: str) -> dict[str, Any]:
        """Extract directives from a process body."""
        directives: dict[str, Any] = {}

        # Common directives
        directive_patterns = [
            (r"container\s+['\"]([^'\"]+)['\"]", "container"),
            (r"cpus\s+(\d+)", "cpus"),
            (r"memory\s+['\"]?([^'\"\n]+)['\"]?", "memory"),
            (r"time\s+['\"]?([^'\"\n]+)['\"]?", "time"),
            (r"label\s+['\"]?(\w+)['\"]?", "label"),
            (r"tag\s+['\"]?([^'\"\n]+)['\"]?", "tag"),
            (r"publishDir\s+['\"]([^'\"]+)['\"]", "publishDir"),
            (r"conda\s+['\"]([^'\"]+)['\"]", "conda"),
        ]

        for pattern, directive_name in directive_patterns:
            match = re.search(pattern, body)
            if match:
                value = match.group(1)
                # Try to convert to number
                try:
                    value = int(value)
                except ValueError:
                    pass
                directives[directive_name] = value

        return directives

    def _extract_workflow_inputs(self, body: str) -> list[WorkflowInput]:
        """Extract take declarations from a workflow body."""
        inputs: list[WorkflowInput] = []

        # Find take block
        take_match = re.search(r"take:\s*(.*?)(?=main:|emit:|$)", body, re.DOTALL)
        if not take_match:
            return inputs

        take_block = take_match.group(1)

        # Each line in take block is an input
        for line in take_block.strip().split("\n"):
            line = line.strip()
            if line and not line.startswith("//"):
                inputs.append(WorkflowInput(name=line))

        return inputs

    def _extract_workflow_outputs(self, body: str) -> list[WorkflowOutput]:
        """Extract emit declarations from a workflow body."""
        outputs: list[WorkflowOutput] = []

        # Find emit block
        emit_match = re.search(r"emit:\s*(.*?)$", body, re.DOTALL)
        if not emit_match:
            return outputs

        emit_block = emit_match.group(1)

        # Parse emit declarations
        # Pattern: name = channel or just channel
        for line in emit_block.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            if "=" in line:
                name = line.split("=")[0].strip()
            else:
                name = line

            outputs.append(WorkflowOutput(name=name))

        return outputs

    def _extract_workflow_calls(self, body: str) -> list[str]:
        """Extract process/workflow calls from a workflow body."""
        calls: list[str] = []

        # Find main block
        main_match = re.search(r"main:\s*(.*?)(?=emit:|$)", body, re.DOTALL)
        if main_match:
            main_body = main_match.group(1)
        else:
            # No explicit main block, use everything after take
            take_match = re.search(r"take:.*?(?=\n\s*\n|\n\s*[a-zA-Z])", body, re.DOTALL)
            if take_match:
                main_body = body[take_match.end() :]
            else:
                main_body = body

        # Find process/workflow calls: NAME(args) or NAME { }
        call_pattern = re.compile(r"\b([A-Z][A-Z0-9_]*)\s*[\(\{]")
        for match in call_pattern.finditer(main_body):
            name = match.group(1)
            if name not in calls:
                calls.append(name)

        return calls
