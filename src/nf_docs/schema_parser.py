"""
Parser for nextflow_schema.json files.

Nextflow pipelines can define their parameters in a JSON Schema file
(draft 2020-12) that describes types, descriptions, defaults, and
validation rules for pipeline inputs.

See: https://nextflow-io.github.io/nf-schema/latest/nextflow_schema/
"""

import json
import logging
from pathlib import Path
from typing import Any

from nf_docs.models import PipelineInput, PipelineMetadata

logger = logging.getLogger(__name__)


class SchemaParseError(Exception):
    """Exception raised when schema parsing fails."""

    pass


def parse_schema(schema_path: str | Path) -> tuple[PipelineMetadata, list[PipelineInput]]:
    """
    Parse a nextflow_schema.json file.

    Args:
        schema_path: Path to the nextflow_schema.json file

    Returns:
        Tuple of (PipelineMetadata, list of PipelineInput)
    """
    path = Path(schema_path)
    if not path.exists():
        raise SchemaParseError(f"Schema file not found: {path}")

    try:
        with open(path, encoding="utf-8") as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        raise SchemaParseError(f"Invalid JSON in schema file: {e}") from e

    metadata = _parse_metadata(schema)
    inputs = _parse_inputs(schema)

    logger.info(f"Parsed schema with {len(inputs)} input parameters")
    return metadata, inputs


def _parse_metadata(schema: dict[str, Any]) -> PipelineMetadata:
    """Extract pipeline metadata from schema."""
    metadata = PipelineMetadata()

    # Title is often the pipeline name
    if "title" in schema:
        metadata.name = schema["title"]

    # Description
    if "description" in schema:
        metadata.description = schema["description"]

    # Check for $defs or definitions for additional metadata
    # Some schemas include manifest information
    if "$defs" in schema:
        defs = schema["$defs"]
        if "manifest" in defs:
            manifest = defs["manifest"]
            if "properties" in manifest:
                props = manifest["properties"]
                if "name" in props and "default" in props["name"]:
                    metadata.name = props["name"]["default"]
                if "version" in props and "default" in props["version"]:
                    metadata.version = props["version"]["default"]
                if "homePage" in props and "default" in props["homePage"]:
                    metadata.homepage = props["homePage"]["default"]
                if "author" in props and "default" in props["author"]:
                    # Author can be a comma-separated list
                    author_str = props["author"]["default"]
                    if author_str:
                        metadata.authors = [a.strip() for a in author_str.split(",")]

    return metadata


def _parse_inputs(schema: dict[str, Any]) -> list[PipelineInput]:
    """Extract input parameters from schema."""
    inputs: list[PipelineInput] = []

    # Parameters can be directly in properties or organized in definitions
    # Check for top-level properties
    if "properties" in schema:
        inputs.extend(_parse_properties(schema["properties"], schema.get("required", [])))

    # Check for grouped definitions (common in nf-core schemas)
    # These are referenced via $ref and allOf
    defs = schema.get("$defs") or schema.get("definitions", {})

    for group_name, group_def in defs.items():
        if not isinstance(group_def, dict):
            continue

        # Skip non-parameter definitions like "manifest"
        if group_name in ("manifest",):
            continue

        # Get the group title (human-readable name)
        group_title = group_def.get("title", group_name)

        if "properties" in group_def:
            group_required = group_def.get("required", [])
            group_inputs = _parse_properties(
                group_def["properties"], group_required, group=group_title
            )
            inputs.extend(group_inputs)

    return inputs


def _parse_properties(
    properties: dict[str, Any],
    required: list[str],
    group: str = "",
) -> list[PipelineInput]:
    """Parse a properties object into PipelineInput objects."""
    inputs: list[PipelineInput] = []

    for param_name, param_def in properties.items():
        if not isinstance(param_def, dict):
            continue

        # Determine type
        param_type = param_def.get("type", "string")
        if isinstance(param_type, list):
            # Handle union types like ["string", "null"]
            param_type = [t for t in param_type if t != "null"][0] if param_type else "string"

        # Create input object
        inp = PipelineInput(
            name=param_name,
            type=param_type,
            description=param_def.get("description", ""),
            help_text=param_def.get("help_text", ""),
            required=param_name in required,
            default=param_def.get("default"),
            format=param_def.get("format", ""),
            pattern=param_def.get("pattern", ""),
            enum=param_def.get("enum", []),
            group=group,
            hidden=param_def.get("hidden", False),
            fa_icon=param_def.get("fa_icon", ""),
        )

        inputs.append(inp)

    return inputs


def find_schema_file(workspace_path: str | Path) -> Path | None:
    """
    Find the nextflow_schema.json file in a workspace.

    Args:
        workspace_path: Path to the Nextflow pipeline workspace

    Returns:
        Path to the schema file, or None if not found
    """
    workspace = Path(workspace_path)

    # Common locations for the schema file
    candidates = [
        workspace / "nextflow_schema.json",
        workspace / "schema" / "nextflow_schema.json",
        workspace / "assets" / "nextflow_schema.json",
    ]

    for candidate in candidates:
        if candidate.exists():
            logger.debug(f"Found schema file: {candidate}")
            return candidate

    return None


def validate_schema(schema: dict[str, Any]) -> list[str]:
    """
    Validate a nextflow schema for common issues.

    Args:
        schema: Parsed schema dictionary

    Returns:
        List of warning messages (empty if no issues)
    """
    warnings: list[str] = []

    # Check for $schema declaration
    if "$schema" not in schema:
        warnings.append("Schema is missing $schema declaration")

    # Check that all parameters have descriptions
    def check_properties(props: dict[str, Any], path: str = "") -> None:
        for name, defn in props.items():
            if not isinstance(defn, dict):
                continue
            param_path = f"{path}.{name}" if path else name
            if "description" not in defn:
                warnings.append(f"Parameter '{param_path}' is missing a description")
            if "type" not in defn:
                warnings.append(f"Parameter '{param_path}' is missing a type")

    if "properties" in schema:
        check_properties(schema["properties"])

    defs = schema.get("$defs") or schema.get("definitions", {})
    for group_name, group_def in defs.items():
        if isinstance(group_def, dict) and "properties" in group_def:
            check_properties(group_def["properties"], group_name)

    return warnings
