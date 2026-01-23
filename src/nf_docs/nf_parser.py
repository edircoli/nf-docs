"""
Nextflow code parser for extracting structured information.

Parses Nextflow process/workflow definitions from LSP hover content
to extract inputs, outputs, and other metadata.
"""

import re
from dataclasses import dataclass, field


@dataclass
class ParsedInput:
    """A parsed input declaration."""

    name: str
    type: str  # val, path, tuple, env, stdin, file
    qualifier: str = ""  # Additional info like stageAs, arity


@dataclass
class ParsedOutput:
    """A parsed output declaration."""

    name: str
    type: str  # val, path, tuple, env, stdout, file
    emit: str = ""
    optional: bool = False


@dataclass
class ParsedProcess:
    """Parsed process information from code."""

    name: str
    inputs: list[ParsedInput] = field(default_factory=list)
    outputs: list[ParsedOutput] = field(default_factory=list)


@dataclass
class ParsedWorkflow:
    """Parsed workflow information from code."""

    name: str
    takes: list[str] = field(default_factory=list)  # Input channel names
    emits: list[str] = field(default_factory=list)  # Output channel names


def parse_process_hover(hover_text: str) -> ParsedProcess | None:
    """
    Parse a process definition from LSP hover content.

    The hover content looks like:
    ```nextflow
    process FASTQC {
      input:
      tuple val(meta), path(reads)

      output:
      tuple val(meta), path("*.html"), emit: html
      tuple val(meta), path("*.zip"), emit: zip
      path "versions.yml", emit: versions
    }
    ```

    Args:
        hover_text: The hover content from LSP

    Returns:
        ParsedProcess with extracted inputs/outputs, or None if parsing fails
    """
    # Extract code from markdown code block
    code_match = re.search(r"```(?:nextflow|groovy)?\s*\n?(.*?)```", hover_text, re.DOTALL)
    if code_match:
        code = code_match.group(1)
    else:
        code = hover_text

    # Extract process name
    name_match = re.search(r"process\s+(\w+)\s*\{", code)
    if not name_match:
        return None

    process = ParsedProcess(name=name_match.group(1))

    # Extract input section
    input_match = re.search(r"input:\s*(.*?)(?:output:|script:|shell:|exec:|\})", code, re.DOTALL)
    if input_match:
        input_block = input_match.group(1)
        process.inputs = _parse_input_declarations(input_block)

    # Extract output section
    output_match = re.search(r"output:\s*(.*?)(?:script:|shell:|exec:|when:|\})", code, re.DOTALL)
    if output_match:
        output_block = output_match.group(1)
        process.outputs = _parse_output_declarations(output_block)

    return process


def _parse_input_declarations(block: str) -> list[ParsedInput]:
    """Parse input declarations from an input block."""
    inputs = []

    # Split by lines and parse each declaration
    lines = block.strip().split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parsed = _parse_single_input(line)
        if parsed:
            inputs.append(parsed)

    return inputs


def _parse_single_input(line: str) -> ParsedInput | None:
    """Parse a single input declaration line."""
    line = line.strip()
    if not line:
        return None

    # Handle tuple inputs: tuple val(meta), path(reads)
    if line.startswith("tuple"):
        # Extract components
        components = re.findall(r"(val|path|file|env)\s*\(([^)]+)\)", line)
        if components:
            # Create a descriptive name from components
            parts = []
            for comp_type, comp_name in components:
                parts.append(f"{comp_type}({comp_name})")
            name = ", ".join(parts)
            return ParsedInput(name=name, type="tuple")

    # Handle simple inputs: val(x), path(x), file(x), env(x), stdin
    simple_match = re.match(r"(val|path|file|env)\s*\(([^)]+)\)", line)
    if simple_match:
        input_type = simple_match.group(1)
        name = simple_match.group(2).strip().strip("'\"")
        return ParsedInput(name=name, type=input_type)

    # Handle stdin
    if line == "stdin" or line.startswith("stdin "):
        return ParsedInput(name="stdin", type="stdin")

    # Handle path with pattern: path '*.txt'
    path_pattern = re.match(r"path\s+['\"]([^'\"]+)['\"]", line)
    if path_pattern:
        return ParsedInput(name=path_pattern.group(1), type="path")

    return None


def _parse_output_declarations(block: str) -> list[ParsedOutput]:
    """Parse output declarations from an output block."""
    outputs = []

    # Split by lines and parse each declaration
    lines = block.strip().split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parsed = _parse_single_output(line)
        if parsed:
            outputs.append(parsed)

    return outputs


def _parse_single_output(line: str) -> ParsedOutput | None:
    """Parse a single output declaration line."""
    line = line.strip()
    if not line:
        return None

    # Extract emit name if present
    emit_match = re.search(r"emit:\s*(\w+)", line)
    emit_name = emit_match.group(1) if emit_match else ""

    # Extract optional flag
    optional = "optional:" in line or "optional :" in line

    # Handle tuple outputs: tuple val(meta), path("*.html"), emit: html
    if line.startswith("tuple"):
        components = re.findall(r"(val|path|file|env)\s*\(([^)]+)\)", line)
        if components:
            parts = []
            for comp_type, comp_name in components:
                parts.append(f"{comp_type}({comp_name})")
            name = ", ".join(parts)
            return ParsedOutput(name=name, type="tuple", emit=emit_name, optional=optional)

    # Handle simple outputs: path "versions.yml", emit: versions
    simple_match = re.match(r"(val|path|file|env|stdout)\s*\(?([^),]*)\)?", line)
    if simple_match:
        output_type = simple_match.group(1)
        name = (
            simple_match.group(2).strip().strip("'\"()") if simple_match.group(2) else output_type
        )
        return ParsedOutput(name=name, type=output_type, emit=emit_name, optional=optional)

    return None


def parse_workflow_hover(hover_text: str) -> ParsedWorkflow | None:
    """
    Parse a workflow definition from LSP hover content.

    Args:
        hover_text: The hover content from LSP

    Returns:
        ParsedWorkflow with extracted takes/emits, or None if parsing fails
    """
    # Extract code from markdown code block
    code_match = re.search(r"```(?:nextflow|groovy)?\s*\n?(.*?)```", hover_text, re.DOTALL)
    if code_match:
        code = code_match.group(1)
    else:
        code = hover_text

    # Extract workflow name (may be empty for entry workflow)
    name_match = re.search(r"workflow\s+(\w+)?\s*\{", code)
    if not name_match:
        return None

    name = name_match.group(1) or ""
    workflow = ParsedWorkflow(name=name)

    # Extract take section
    take_match = re.search(r"take:\s*(.*?)(?:main:|emit:|\})", code, re.DOTALL)
    if take_match:
        take_block = take_match.group(1)
        for line in take_block.strip().split("\n"):
            line = line.strip()
            if line and not line.startswith("//"):
                workflow.takes.append(line)

    # Extract emit section
    emit_match = re.search(r"emit:\s*(.*?)(?:\}|$)", code, re.DOTALL)
    if emit_match:
        emit_block = emit_match.group(1)
        for line in emit_block.strip().split("\n"):
            line = line.strip()
            if line and not line.startswith("//"):
                # Handle "name = channel" or just "name"
                if "=" in line:
                    emit_name = line.split("=")[0].strip()
                else:
                    emit_name = line
                workflow.emits.append(emit_name)

    return workflow


def is_code_block(text: str) -> bool:
    """Check if text appears to be a code block rather than documentation."""
    # If it contains code fences, it's code
    if "```" in text:
        return True

    # If it starts with process/workflow/def keywords, it's code
    stripped = text.strip()
    if re.match(r"^(process|workflow|def)\s+\w+", stripped):
        return True

    # If it contains typical code patterns
    code_patterns = [
        r"\binput:\s*$",
        r"\boutput:\s*$",
        r"\bscript:\s*$",
        r"\btuple\s+val\(",
        r"\bpath\s*\(",
        r"\bval\s*\(",
    ]
    for pattern in code_patterns:
        if re.search(pattern, text, re.MULTILINE):
            return True

    return False
