"""
Utility for creating an isolated Nextflow environment.

This module provides functions to run Nextflow and the Nextflow Language Server
in an isolated environment that doesn't pick up user configuration from ~/.nextflow.
"""

import os
import tempfile
from pathlib import Path

# Module-level temp directory that persists for the process lifetime
_nxf_home_temp_dir: tempfile.TemporaryDirectory | None = None


def get_isolated_nxf_home() -> Path:
    """
    Get a temporary directory to use as NXF_HOME.

    This ensures Nextflow doesn't pick up user configuration from ~/.nextflow/config.
    The directory is created once and reused for the lifetime of the process.

    Returns:
        Path to the temporary NXF_HOME directory
    """
    global _nxf_home_temp_dir
    if _nxf_home_temp_dir is None:
        _nxf_home_temp_dir = tempfile.TemporaryDirectory(prefix="nf-docs-nxf-home-")
    return Path(_nxf_home_temp_dir.name)


def get_isolated_env() -> dict[str, str]:
    """
    Get environment variables for running Nextflow in isolation.

    Returns a copy of the current environment with NXF_HOME set to a temporary
    directory, preventing Nextflow from reading user configuration.

    Returns:
        Dictionary of environment variables
    """
    env = os.environ.copy()
    env["NXF_HOME"] = str(get_isolated_nxf_home())
    return env
