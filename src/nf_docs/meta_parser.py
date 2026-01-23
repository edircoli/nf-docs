"""
Parser for nf-core module and subworkflow meta.yml files.

This module handles parsing of meta.yml files that provide rich documentation
for nf-core modules and subworkflows, including tool information, input/output
descriptions, authors, and more.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)


@dataclass
class ToolInfo:
    """Information about a tool used in a module."""

    name: str
    description: str = ""
    homepage: str = ""
    documentation: str = ""
    tool_dev_url: str = ""
    doi: str = ""
    licence: list[str] = field(default_factory=list)
    identifier: str = ""  # e.g., biotools:fastqc

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        result: dict[str, Any] = {"name": self.name}
        if self.description:
            result["description"] = self.description
        if self.homepage:
            result["homepage"] = self.homepage
        if self.documentation:
            result["documentation"] = self.documentation
        if self.tool_dev_url:
            result["tool_dev_url"] = self.tool_dev_url
        if self.doi:
            result["doi"] = self.doi
        if self.licence:
            result["licence"] = self.licence
        if self.identifier:
            result["identifier"] = self.identifier
        return result


@dataclass
class MetaInput:
    """Input definition from meta.yml."""

    name: str
    type: str = ""
    description: str = ""
    pattern: str = ""
    ontologies: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        result: dict[str, Any] = {"name": self.name}
        if self.type:
            result["type"] = self.type
        if self.description:
            result["description"] = self.description
        if self.pattern:
            result["pattern"] = self.pattern
        if self.ontologies:
            result["ontologies"] = self.ontologies
        return result


@dataclass
class MetaOutput:
    """Output definition from meta.yml."""

    name: str  # Channel name (e.g., 'html', 'zip', 'bam')
    type: str = ""
    description: str = ""
    pattern: str = ""
    ontologies: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        result: dict[str, Any] = {"name": self.name}
        if self.type:
            result["type"] = self.type
        if self.description:
            result["description"] = self.description
        if self.pattern:
            result["pattern"] = self.pattern
        if self.ontologies:
            result["ontologies"] = self.ontologies
        return result


@dataclass
class ModuleMeta:
    """Parsed meta.yml content for a module (process)."""

    name: str
    description: str = ""
    keywords: list[str] = field(default_factory=list)
    tools: list[ToolInfo] = field(default_factory=list)
    inputs: list[MetaInput] = field(default_factory=list)
    outputs: list[MetaOutput] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    maintainers: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        result: dict[str, Any] = {"name": self.name}
        if self.description:
            result["description"] = self.description
        if self.keywords:
            result["keywords"] = self.keywords
        if self.tools:
            result["tools"] = [t.to_dict() for t in self.tools]
        if self.inputs:
            result["inputs"] = [i.to_dict() for i in self.inputs]
        if self.outputs:
            result["outputs"] = [o.to_dict() for o in self.outputs]
        if self.authors:
            result["authors"] = self.authors
        if self.maintainers:
            result["maintainers"] = self.maintainers
        return result


@dataclass
class SubworkflowMeta:
    """Parsed meta.yml content for a subworkflow."""

    name: str
    description: str = ""
    keywords: list[str] = field(default_factory=list)
    components: list[str] = field(default_factory=list)  # modules/subworkflows used
    inputs: list[MetaInput] = field(default_factory=list)
    outputs: list[MetaOutput] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    maintainers: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        result: dict[str, Any] = {"name": self.name}
        if self.description:
            result["description"] = self.description
        if self.keywords:
            result["keywords"] = self.keywords
        if self.components:
            result["components"] = self.components
        if self.inputs:
            result["inputs"] = [i.to_dict() for i in self.inputs]
        if self.outputs:
            result["outputs"] = [o.to_dict() for o in self.outputs]
        if self.authors:
            result["authors"] = self.authors
        if self.maintainers:
            result["maintainers"] = self.maintainers
        return result


def find_meta_yml(nf_file: Path) -> Path | None:
    """
    Find the meta.yml file associated with a Nextflow file.

    For modules/subworkflows, the meta.yml is typically in the same directory
    as the main.nf file.

    Args:
        nf_file: Path to the .nf file

    Returns:
        Path to meta.yml if found, None otherwise
    """
    meta_path = nf_file.parent / "meta.yml"
    if meta_path.exists():
        return meta_path
    return None


def _parse_module_inputs(raw_inputs: list[Any]) -> list[MetaInput]:
    """
    Parse module input definitions from meta.yml.

    Module inputs are structured as nested lists representing tuples:
    input:
      - - meta:
            type: map
            description: ...
        - reads:
            type: file
            description: ...
    """
    inputs: list[MetaInput] = []

    for input_tuple in raw_inputs:
        if not isinstance(input_tuple, list):
            continue

        for element in input_tuple:
            if not isinstance(element, dict):
                continue

            for name, props in element.items():
                if not isinstance(props, dict):
                    continue

                # Extract ontologies if present
                ontologies = []
                raw_ontologies = props.get("ontologies", [])
                if isinstance(raw_ontologies, list):
                    for ont in raw_ontologies:
                        if isinstance(ont, dict) and "edam" in ont:
                            ontologies.append(ont["edam"])

                inputs.append(
                    MetaInput(
                        name=name,
                        type=props.get("type", ""),
                        description=props.get("description", "").strip(),
                        pattern=props.get("pattern", ""),
                        ontologies=ontologies,
                    )
                )

    return inputs


def _parse_module_outputs(raw_outputs: dict[str, Any]) -> list[MetaOutput]:
    """
    Parse module output definitions from meta.yml.

    Module outputs are structured as a dict with channel names:
    output:
      html:
        - - meta:
              type: map
          - "*.html":
              type: file
              description: ...
    """
    outputs: list[MetaOutput] = []

    for channel_name, channel_content in raw_outputs.items():
        # Skip version outputs (they have special structure)
        if channel_name.startswith("versions"):
            continue

        if not isinstance(channel_content, list):
            continue

        # Collect all descriptions for this channel
        descriptions: list[str] = []
        patterns: list[str] = []
        output_type = ""
        ontologies: list[str] = []

        for output_tuple in channel_content:
            if not isinstance(output_tuple, list):
                continue

            for element in output_tuple:
                if not isinstance(element, dict):
                    continue

                for name, props in element.items():
                    if not isinstance(props, dict):
                        continue

                    # Skip meta entries for description purposes
                    if name == "meta":
                        continue

                    desc = props.get("description", "").strip()
                    if desc:
                        descriptions.append(desc)

                    pattern = props.get("pattern", "")
                    if pattern:
                        patterns.append(pattern)

                    if not output_type:
                        output_type = props.get("type", "")

                    raw_ont = props.get("ontologies", [])
                    if isinstance(raw_ont, list):
                        for ont in raw_ont:
                            if isinstance(ont, dict) and "edam" in ont:
                                ontologies.append(ont["edam"])

        outputs.append(
            MetaOutput(
                name=channel_name,
                type=output_type,
                description="\n".join(descriptions),
                pattern=", ".join(patterns) if patterns else "",
                ontologies=ontologies,
            )
        )

    return outputs


def _parse_subworkflow_inputs(raw_inputs: list[Any]) -> list[MetaInput]:
    """
    Parse subworkflow input definitions from meta.yml.

    Subworkflow inputs are simpler - a flat list of channel objects:
    input:
      - ch_bam_bai:
          description: ...
      - ch_fasta:
          description: ...
    """
    inputs: list[MetaInput] = []

    for item in raw_inputs:
        if not isinstance(item, dict):
            continue

        for name, props in item.items():
            if not isinstance(props, dict):
                # Simple case: just a name
                inputs.append(MetaInput(name=name))
                continue

            inputs.append(
                MetaInput(
                    name=name,
                    type=props.get("type", ""),
                    description=props.get("description", "").strip(),
                    pattern=props.get("pattern", ""),
                )
            )

    return inputs


def _parse_subworkflow_outputs(raw_outputs: list[Any]) -> list[MetaOutput]:
    """
    Parse subworkflow output definitions from meta.yml.

    Subworkflow outputs are a flat list:
    output:
      - stats:
          description: ...
      - versions:
          description: ...
    """
    outputs: list[MetaOutput] = []

    for item in raw_outputs:
        if not isinstance(item, dict):
            continue

        for name, props in item.items():
            if not isinstance(props, dict):
                outputs.append(MetaOutput(name=name))
                continue

            outputs.append(
                MetaOutput(
                    name=name,
                    type=props.get("type", ""),
                    description=props.get("description", "").strip(),
                    pattern=props.get("pattern", ""),
                )
            )

    return outputs


def _parse_tools(raw_tools: list[Any]) -> list[ToolInfo]:
    """
    Parse tool information from meta.yml.

    tools:
      - fastqc:
          description: ...
          homepage: ...
          licence: [...]
    """
    tools: list[ToolInfo] = []

    for item in raw_tools:
        if not isinstance(item, dict):
            continue

        for name, props in item.items():
            if not isinstance(props, dict):
                tools.append(ToolInfo(name=name))
                continue

            licence = props.get("licence", [])
            if isinstance(licence, str):
                licence = [licence]

            tools.append(
                ToolInfo(
                    name=name,
                    description=props.get("description", "").strip(),
                    homepage=props.get("homepage", ""),
                    documentation=props.get("documentation", ""),
                    tool_dev_url=props.get("tool_dev_url", ""),
                    doi=props.get("doi", ""),
                    licence=licence,
                    identifier=props.get("identifier", ""),
                )
            )

    return tools


def parse_module_meta(meta_path: Path) -> ModuleMeta | None:
    """
    Parse a module's meta.yml file.

    Args:
        meta_path: Path to the meta.yml file

    Returns:
        ModuleMeta object if parsing succeeds, None otherwise
    """
    try:
        content = meta_path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)

        if not data or not isinstance(data, dict):
            return None

        name = data.get("name", "")
        if not name:
            return None

        # Parse tools
        tools = _parse_tools(data.get("tools", []))

        # Parse inputs (module format)
        inputs = _parse_module_inputs(data.get("input", []))

        # Parse outputs (module format - dict structure)
        raw_outputs = data.get("output", {})
        if isinstance(raw_outputs, dict):
            outputs = _parse_module_outputs(raw_outputs)
        else:
            outputs = []

        # Authors and maintainers
        authors = data.get("authors", [])
        maintainers = data.get("maintainers", [])

        return ModuleMeta(
            name=name,
            description=data.get("description", "").strip(),
            keywords=data.get("keywords", []),
            tools=tools,
            inputs=inputs,
            outputs=outputs,
            authors=authors if isinstance(authors, list) else [],
            maintainers=maintainers if isinstance(maintainers, list) else [],
        )

    except yaml.YAMLError as e:
        logger.warning(f"Failed to parse YAML in {meta_path}: {e}")
        return None
    except Exception as e:
        logger.warning(f"Failed to parse module meta.yml {meta_path}: {e}")
        return None


def parse_subworkflow_meta(meta_path: Path) -> SubworkflowMeta | None:
    """
    Parse a subworkflow's meta.yml file.

    Args:
        meta_path: Path to the meta.yml file

    Returns:
        SubworkflowMeta object if parsing succeeds, None otherwise
    """
    try:
        content = meta_path.read_text(encoding="utf-8")
        data = yaml.safe_load(content)

        if not data or not isinstance(data, dict):
            return None

        name = data.get("name", "")
        if not name:
            return None

        # Components (modules/subworkflows used)
        components = data.get("components", data.get("modules", []))

        # Parse inputs (subworkflow format)
        inputs = _parse_subworkflow_inputs(data.get("input", []))

        # Parse outputs (subworkflow format - list structure)
        raw_outputs = data.get("output", [])
        if isinstance(raw_outputs, list):
            outputs = _parse_subworkflow_outputs(raw_outputs)
        else:
            outputs = []

        # Authors and maintainers
        authors = data.get("authors", [])
        maintainers = data.get("maintainers", [])

        return SubworkflowMeta(
            name=name,
            description=data.get("description", "").strip(),
            keywords=data.get("keywords", []),
            components=components if isinstance(components, list) else [],
            inputs=inputs,
            outputs=outputs,
            authors=authors if isinstance(authors, list) else [],
            maintainers=maintainers if isinstance(maintainers, list) else [],
        )

    except yaml.YAMLError as e:
        logger.warning(f"Failed to parse YAML in {meta_path}: {e}")
        return None
    except Exception as e:
        logger.warning(f"Failed to parse subworkflow meta.yml {meta_path}: {e}")
        return None


def is_module_path(file_path: Path | str, workspace_path: Path | str) -> bool:
    """
    Check if a file path is within a modules directory.

    Args:
        file_path: Path to check
        workspace_path: Root workspace path

    Returns:
        True if the path is within modules/
    """
    rel_path = Path(file_path).relative_to(workspace_path)
    parts = rel_path.parts
    return "modules" in parts


def is_subworkflow_path(file_path: Path | str, workspace_path: Path | str) -> bool:
    """
    Check if a file path is within a subworkflows directory.

    Args:
        file_path: Path to check
        workspace_path: Root workspace path

    Returns:
        True if the path is within subworkflows/
    """
    rel_path = Path(file_path).relative_to(workspace_path)
    parts = rel_path.parts
    return "subworkflows" in parts


def parse_meta_for_file(nf_file: Path, workspace_path: Path) -> ModuleMeta | SubworkflowMeta | None:
    """
    Find and parse the appropriate meta.yml for a Nextflow file.

    Automatically detects whether it's a module or subworkflow based on path.

    Args:
        nf_file: Path to the .nf file
        workspace_path: Root workspace path

    Returns:
        ModuleMeta or SubworkflowMeta if found and parsed, None otherwise
    """
    meta_path = find_meta_yml(nf_file)
    if not meta_path:
        return None

    if is_subworkflow_path(nf_file, workspace_path):
        return parse_subworkflow_meta(meta_path)
    else:
        # Default to module parsing (covers modules/ and other paths)
        return parse_module_meta(meta_path)
