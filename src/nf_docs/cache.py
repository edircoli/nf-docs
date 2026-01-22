"""
Caching system for nf-docs pipeline extraction.

Caches the extracted Pipeline model to speed up re-runs when pipeline
files haven't changed.
"""

import hashlib
import json
import logging
import os
from pathlib import Path
from typing import Any

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

logger = logging.getLogger(__name__)


def get_xdg_cache_home() -> Path:
    """Get the XDG cache directory."""
    xdg_cache = os.environ.get("XDG_CACHE_HOME")
    if xdg_cache:
        return Path(xdg_cache)
    return Path.home() / ".cache"


import nf_docs


class PipelineCache:
    """
    Cache for extracted Pipeline models.

    Uses content-based cache invalidation by hashing relevant pipeline files.
    Cache is stored in XDG_CACHE_HOME/nf-docs/ (default ~/.cache/nf-docs/).
    """

    # Files to include in cache key computation
    CACHE_FILES = [
        "*.nf",
        "nextflow_schema.json",
        "nextflow.config",
        "README.md",
    ]

    def __init__(self, cache_dir: Path | None = None):
        """
        Initialize the cache.

        Args:
            cache_dir: Custom cache directory (default: $XDG_CACHE_HOME/nf-docs)
        """
        if cache_dir:
            self.cache_dir = Path(cache_dir)
        else:
            self.cache_dir = get_xdg_cache_home() / "nf-docs"

    def _get_workspace_hash(self, workspace: Path) -> str:
        """Get a hash of the workspace path for namespacing."""
        workspace_str = str(workspace.resolve())
        return hashlib.sha256(workspace_str.encode()).hexdigest()[:16]

    def _get_content_hash(self, workspace: Path) -> str:
        """
        Compute a hash of all relevant files in the workspace.

        This hash changes when any pipeline file is modified.
        """
        hasher = hashlib.sha256()

        # Collect all files to hash
        files_to_hash: list[Path] = []

        for pattern in self.CACHE_FILES:
            if "*" in pattern:
                # Glob pattern - find all matching files
                files_to_hash.extend(sorted(workspace.rglob(pattern)))
            else:
                # Specific file
                file_path = workspace / pattern
                if file_path.exists():
                    files_to_hash.append(file_path)

        # Hash each file's content
        for file_path in sorted(files_to_hash):
            try:
                # Include relative path in hash to detect file renames
                rel_path = file_path.relative_to(workspace)
                hasher.update(str(rel_path).encode())

                # Include file content
                content = file_path.read_bytes()
                hasher.update(content)
            except Exception as e:
                logger.debug(f"Could not hash {file_path}: {e}")

        return hasher.hexdigest()[:32]

    def _get_cache_path(self, workspace: Path) -> Path:
        """Get the cache file path for a workspace."""
        workspace_hash = self._get_workspace_hash(workspace)
        content_hash = self._get_content_hash(workspace)
        # Include version in filename to invalidate old caches when nf-docs is updated
        return self.cache_dir / f"{nf_docs.__version__}_{workspace_hash}_{content_hash}.json"

    def get(self, workspace: Path) -> Pipeline | None:
        """
        Get cached Pipeline if valid.

        Args:
            workspace: Path to the pipeline workspace

        Returns:
            Cached Pipeline if valid, None if cache miss or stale
        """
        cache_path = self._get_cache_path(workspace)

        if not cache_path.exists():
            logger.debug("Cache miss: no cache file")
            return None

        try:
            data = json.loads(cache_path.read_text(encoding="utf-8"))
            pipeline = self._deserialize_pipeline(data)
            logger.debug(f"Cache hit: loaded from {cache_path.name}")
            logger.info("Using cached extraction results")
            return pipeline
        except Exception as e:
            logger.debug(f"Cache miss: failed to load cache: {e}")
            return None

    def set(self, workspace: Path, pipeline: Pipeline) -> None:
        """
        Store Pipeline in cache.

        Args:
            workspace: Path to the pipeline workspace
            pipeline: Pipeline model to cache
        """
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        cache_path = self._get_cache_path(workspace)

        # Clean up old cache files for this workspace
        self._cleanup_old_caches(workspace, exclude=cache_path)

        try:
            data = self._serialize_pipeline(pipeline)
            cache_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            logger.debug(f"Cached to {cache_path.name}")
        except Exception as e:
            logger.warning(f"Failed to cache pipeline: {e}")

    def _cleanup_old_caches(self, workspace: Path, exclude: Path | None = None) -> None:
        """Remove old cache files for a workspace."""
        workspace_hash = self._get_workspace_hash(workspace)

        if not self.cache_dir.exists():
            return

        # Clean up caches from any version for this workspace
        for cache_file in self.cache_dir.glob(f"*{workspace_hash}_*.json"):
            if exclude and cache_file == exclude:
                continue
            try:
                cache_file.unlink()
                logger.debug(f"Removed old cache: {cache_file.name}")
            except Exception as e:
                logger.debug(f"Could not remove old cache {cache_file}: {e}")

    def clear(self, workspace: Path | None = None) -> int:
        """
        Clear cache for a workspace or all caches.

        Args:
            workspace: Specific workspace to clear, or None for all

        Returns:
            Number of cache files removed
        """
        if not self.cache_dir.exists():
            return 0

        count = 0

        if workspace:
            # Clear only this workspace's cache (match any version)
            workspace_hash = self._get_workspace_hash(workspace)
            for cache_file in self.cache_dir.glob(f"*_{workspace_hash}_*.json"):
                try:
                    cache_file.unlink()
                    count += 1
                except Exception:
                    pass
        else:
            # Clear all caches
            for cache_file in self.cache_dir.glob("*.json"):
                try:
                    cache_file.unlink()
                    count += 1
                except Exception:
                    pass

        logger.info(f"Cleared {count} cache file(s)")
        return count

    def _serialize_pipeline(self, pipeline: Pipeline) -> dict[str, Any]:
        """Serialize a Pipeline to JSON-compatible dict."""
        return pipeline.to_dict()

    def _deserialize_pipeline(self, data: dict[str, Any]) -> Pipeline:
        """Deserialize a Pipeline from JSON dict."""
        # Reconstruct metadata
        pipeline_data = data.get("pipeline", {})
        metadata = PipelineMetadata(
            name=pipeline_data.get("name", ""),
            description=pipeline_data.get("description", ""),
            version=pipeline_data.get("version", ""),
            homepage=pipeline_data.get("homepage", ""),
            repository=pipeline_data.get("repository", ""),
            authors=pipeline_data.get("authors", []),
            license=pipeline_data.get("license", ""),
        )

        # Reconstruct inputs
        inputs = []
        for inp_data in data.get("inputs", []):
            inputs.append(
                PipelineInput(
                    name=inp_data.get("name", ""),
                    type=inp_data.get("type", "string"),
                    description=inp_data.get("description", ""),
                    help_text=inp_data.get("help_text", ""),
                    required=inp_data.get("required", False),
                    default=inp_data.get("default"),
                    format=inp_data.get("format", ""),
                    pattern=inp_data.get("pattern", ""),
                    enum=inp_data.get("enum", []),
                    group=inp_data.get("group", ""),
                    hidden=inp_data.get("hidden", False),
                    fa_icon=inp_data.get("fa_icon", ""),
                )
            )

        # Reconstruct config params
        config_params = []
        for param_data in data.get("config_params", []):
            config_params.append(
                ConfigParam(
                    name=param_data.get("name", ""),
                    type=param_data.get("type", "string"),
                    description=param_data.get("description", ""),
                    default=param_data.get("default"),
                    source=param_data.get("source", ""),
                )
            )

        # Reconstruct workflows
        workflows = []
        for wf_data in data.get("workflows", []):
            wf_inputs = [
                WorkflowInput(
                    name=i.get("name", ""),
                    type=i.get("type", ""),
                    description=i.get("description", ""),
                )
                for i in wf_data.get("inputs", [])
            ]
            wf_outputs = [
                WorkflowOutput(
                    name=o.get("name", ""),
                    type=o.get("type", ""),
                    description=o.get("description", ""),
                )
                for o in wf_data.get("outputs", [])
            ]
            workflows.append(
                Workflow(
                    name=wf_data.get("name", ""),
                    docstring=wf_data.get("docstring", ""),
                    file=wf_data.get("file", ""),
                    line=wf_data.get("line", 0),
                    end_line=wf_data.get("end_line", 0),
                    inputs=wf_inputs,
                    outputs=wf_outputs,
                    calls=wf_data.get("calls", []),
                    is_entry=wf_data.get("is_entry", False),
                    source_url=wf_data.get("source_url", ""),
                )
            )

        # Reconstruct processes
        processes = []
        for proc_data in data.get("processes", []):
            proc_inputs = [
                ProcessInput(
                    name=i.get("name", ""),
                    type=i.get("type", ""),
                    description=i.get("description", ""),
                    qualifier=i.get("qualifier", ""),
                )
                for i in proc_data.get("inputs", [])
            ]
            proc_outputs = [
                ProcessOutput(
                    name=o.get("name", ""),
                    type=o.get("type", ""),
                    description=o.get("description", ""),
                    emit=o.get("emit", ""),
                )
                for o in proc_data.get("outputs", [])
            ]
            processes.append(
                Process(
                    name=proc_data.get("name", ""),
                    docstring=proc_data.get("docstring", ""),
                    file=proc_data.get("file", ""),
                    line=proc_data.get("line", 0),
                    end_line=proc_data.get("end_line", 0),
                    inputs=proc_inputs,
                    outputs=proc_outputs,
                    directives=proc_data.get("directives", {}),
                    source_url=proc_data.get("source_url", ""),
                )
            )

        # Reconstruct functions
        functions = []
        for func_data in data.get("functions", []):
            func_params = [
                FunctionParam(
                    name=p.get("name", ""),
                    type=p.get("type", ""),
                    description=p.get("description", ""),
                    default=p.get("default"),
                )
                for p in func_data.get("params", [])
            ]
            functions.append(
                Function(
                    name=func_data.get("name", ""),
                    docstring=func_data.get("docstring", ""),
                    file=func_data.get("file", ""),
                    line=func_data.get("line", 0),
                    end_line=func_data.get("end_line", 0),
                    params=func_params,
                    return_type=func_data.get("return_type", ""),
                    return_description=func_data.get("return_description", ""),
                    source_url=func_data.get("source_url", ""),
                )
            )

        return Pipeline(
            metadata=metadata,
            inputs=inputs,
            config_params=config_params,
            workflows=workflows,
            processes=processes,
            functions=functions,
        )
