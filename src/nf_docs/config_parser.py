"""
Parser for Nextflow configuration files.

This module extracts configuration parameters by running `nextflow config -flat`
which outputs all resolved parameters in a flat key=value format.
"""

import logging
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from rich.text import Text

from nf_docs.models import ConfigParam, PipelineMetadata

logger = logging.getLogger(__name__)


class ConfigParseError(Exception):
    """Exception raised when config parsing fails."""

    pass


def parse_config(
    workspace_path: str | Path,
    nextflow_path: str = "nextflow",
) -> tuple[PipelineMetadata, list[ConfigParam]]:
    """
    Parse Nextflow configuration using `nextflow config -flat`.

    Args:
        workspace_path: Path to the Nextflow pipeline workspace
        nextflow_path: Path to the Nextflow executable

    Returns:
        Tuple of (PipelineMetadata from manifest, list of ConfigParam)
    """
    workspace = Path(workspace_path)

    # Check if nextflow is available
    if not shutil.which(nextflow_path):
        logger.warning(
            f"Nextflow not found at '{nextflow_path}'. "
            "Config parsing will be skipped. Install Nextflow or provide --nextflow-path."
        )
        return PipelineMetadata(), []

    # Check if there's a config file
    config_files = list(workspace.glob("*.config")) + list(workspace.glob("conf/*.config"))
    if not config_files and not (workspace / "nextflow.config").exists():
        logger.debug("No config files found in workspace")
        return PipelineMetadata(), []

    try:
        result = subprocess.run(
            [nextflow_path, "config", "-flat", str(workspace)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=str(workspace),
        )

        if result.returncode != 0:
            error_msg = result.stderr.strip() or result.stdout.strip() or "(no error output)"
            # Strip ANSI escape codes for cleaner logging
            error_msg = Text.from_ansi(error_msg).plain
            logger.warning(f"nextflow config failed: {error_msg}")
            # Try to parse what we can from direct file reading
            return _parse_config_file_directly(workspace)

        return _parse_flat_config(result.stdout)

    except subprocess.TimeoutExpired:
        logger.warning("nextflow config timed out")
        return _parse_config_file_directly(workspace)
    except FileNotFoundError:
        logger.warning(f"Nextflow executable not found: {nextflow_path}")
        return _parse_config_file_directly(workspace)


def _parse_flat_config(config_output: str) -> tuple[PipelineMetadata, list[ConfigParam]]:
    """
    Parse the output of `nextflow config -flat`.

    The output format is:
        key = value
        key = 'string value'
        key = [list, values]
    """
    metadata = PipelineMetadata()
    params: list[ConfigParam] = []

    # Track which params we've seen
    seen_params: set[str] = set()

    for line in config_output.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue

        # Parse key = value
        match = re.match(r"^([a-zA-Z0-9_.]+)\s*=\s*(.*)$", line)
        if not match:
            continue

        key = match.group(1)
        value_str = match.group(2).strip()

        # Parse the value
        value = _parse_value(value_str)
        value_type = _infer_type(value)

        # Handle manifest entries
        if key.startswith("manifest."):
            _update_metadata_from_manifest(metadata, key, value)
            continue

        # Handle params entries
        if key.startswith("params."):
            param_name = key[7:]  # Remove "params." prefix
            if param_name not in seen_params:
                seen_params.add(param_name)
                params.append(
                    ConfigParam(
                        name=param_name,
                        type=value_type,
                        default=value,
                    )
                )

    logger.info(f"Parsed config with {len(params)} parameters")
    return metadata, params


def _parse_value(value_str: str) -> Any:
    """Parse a value string into a Python object."""
    # Remove surrounding quotes
    if (value_str.startswith("'") and value_str.endswith("'")) or (
        value_str.startswith('"') and value_str.endswith('"')
    ):
        return value_str[1:-1]

    # Handle null
    if value_str.lower() == "null":
        return None

    # Handle booleans
    if value_str.lower() == "true":
        return True
    if value_str.lower() == "false":
        return False

    # Handle numbers
    try:
        if "." in value_str:
            return float(value_str)
        return int(value_str)
    except ValueError:
        pass

    # Handle lists
    if value_str.startswith("[") and value_str.endswith("]"):
        # Simple list parsing
        inner = value_str[1:-1].strip()
        if not inner:
            return []
        items = [_parse_value(item.strip()) for item in inner.split(",")]
        return items

    # Handle maps/closures (return as string)
    return value_str


def _infer_type(value: Any) -> str:
    """Infer the JSON Schema type from a Python value."""
    if value is None:
        return "string"  # Default to string for null
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "string"


def _update_metadata_from_manifest(metadata: PipelineMetadata, key: str, value: Any) -> None:
    """Update metadata from a manifest config entry."""
    field = key[9:]  # Remove "manifest." prefix

    if field == "name":
        metadata.name = str(value) if value else ""
    elif field == "version":
        metadata.version = str(value) if value else ""
    elif field == "description":
        metadata.description = str(value) if value else ""
    elif field == "homePage":
        metadata.homepage = str(value) if value else ""
    elif field == "author":
        if value:
            metadata.authors = [a.strip() for a in str(value).split(",")]


def _parse_config_file_directly(workspace: Path) -> tuple[PipelineMetadata, list[ConfigParam]]:
    """
    Fallback: Parse nextflow.config directly without Nextflow.

    This is a simplified parser that handles common patterns but won't
    resolve includes or closures.
    """
    config_file = workspace / "nextflow.config"
    if not config_file.exists():
        return PipelineMetadata(), []

    try:
        content = config_file.read_text(encoding="utf-8")
    except Exception as e:
        logger.warning(f"Failed to read config file: {e}")
        return PipelineMetadata(), []

    metadata = PipelineMetadata()
    params: list[ConfigParam] = []

    # Simple regex-based parsing for params block
    # This is a fallback and won't handle all cases
    params_match = re.search(r"params\s*\{([^}]*)\}", content, re.DOTALL)
    if params_match:
        params_block = params_match.group(1)
        for line in params_block.split("\n"):
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            match = re.match(r"^(\w+)\s*=\s*(.*)$", line)
            if match:
                param_name = match.group(1)
                value_str = match.group(2).strip()
                value = _parse_value(value_str)
                params.append(
                    ConfigParam(
                        name=param_name,
                        type=_infer_type(value),
                        default=value,
                    )
                )

    # Parse manifest block
    manifest_match = re.search(r"manifest\s*\{([^}]*)\}", content, re.DOTALL)
    if manifest_match:
        manifest_block = manifest_match.group(1)
        for line in manifest_block.split("\n"):
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            match = re.match(r"^(\w+)\s*=\s*(.*)$", line)
            if match:
                field = match.group(1)
                value_str = match.group(2).strip()
                value = _parse_value(value_str)
                _update_metadata_from_manifest(metadata, f"manifest.{field}", value)

    return metadata, params


def find_config_files(workspace_path: str | Path) -> list[Path]:
    """
    Find all Nextflow config files in a workspace.

    Args:
        workspace_path: Path to the Nextflow pipeline workspace

    Returns:
        List of paths to config files
    """
    workspace = Path(workspace_path)
    config_files: list[Path] = []

    # Main config file
    main_config = workspace / "nextflow.config"
    if main_config.exists():
        config_files.append(main_config)

    # Config directory
    conf_dir = workspace / "conf"
    if conf_dir.is_dir():
        config_files.extend(conf_dir.glob("*.config"))

    # Other config files in root
    for config in workspace.glob("*.config"):
        if config not in config_files:
            config_files.append(config)

    return config_files
