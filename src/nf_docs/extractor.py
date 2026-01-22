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
from pathlib import Path
from typing import Any

from nf_docs.cache import PipelineCache
from nf_docs.config_parser import parse_config
from nf_docs.lsp_client import LSPClient, SymbolKind, parse_hover_content
from nf_docs.models import (
    Function,
    FunctionParam,
    Pipeline,
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
        use_cache: bool = True,
    ):
        """
        Initialize the extractor.

        Args:
            workspace_path: Path to the Nextflow pipeline workspace
            language_server_jar: Path to the language server JAR (optional)
            nextflow_path: Path to the Nextflow executable
            use_cache: Whether to use caching for extraction results
        """
        self.workspace_path = Path(workspace_path).resolve()
        self.language_server_jar = language_server_jar
        self.nextflow_path = nextflow_path
        self.cache = PipelineCache() if use_cache else None

    def extract(self) -> Pipeline:
        """
        Extract all documentation from the pipeline.

        Returns:
            Complete Pipeline model with all extracted information
        """
        logger.info(f"Extracting documentation from: {self.workspace_path}")

        # Check cache first
        if self.cache:
            cached = self.cache.get(self.workspace_path)
            if cached:
                return cached

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
            config_metadata, config_params = parse_config(self.workspace_path, self.nextflow_path)
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
        self._extract_from_lsp(pipeline)

        # Infer pipeline name from directory if not set
        if not pipeline.metadata.name:
            pipeline.metadata.name = self.workspace_path.name

        logger.info(
            f"Extraction complete: {len(pipeline.workflows)} workflows, "
            f"{len(pipeline.processes)} processes, {len(pipeline.functions)} functions"
        )

        # Store in cache
        if self.cache:
            self.cache.set(self.workspace_path, pipeline)

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

            # Only stop skipping badges when we hit actual content
            if stripped:
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

        with LSPClient(
            self.workspace_path,
            server_jar=self.language_server_jar,
        ) as client:
            # Try workspace symbols first to see what the LSP knows about
            workspace_symbols = client.get_workspace_symbols("")
            logger.debug(f"Workspace symbols: {len(workspace_symbols)}")
            if workspace_symbols:
                logger.debug(f"First few: {workspace_symbols[:3]}")

            for nf_file in nf_files:
                try:
                    self._extract_file_symbols(client, nf_file, pipeline)
                except Exception as e:
                    logger.warning(f"Failed to extract from {nf_file}: {e}")

    def _extract_file_symbols(self, client: LSPClient, file_path: Path, pipeline: Pipeline) -> None:
        """Extract symbols from a single file using LSP."""
        relative_path = file_path.relative_to(self.workspace_path)
        logger.debug(f"Processing: {relative_path}")

        # Open the document
        client.open_document(file_path)

        try:
            # Get document symbols
            symbols = client.get_document_symbols(file_path)
            logger.debug(f"  Found {len(symbols)} symbols")

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
                inp = ProcessInput(
                    name=child_name,
                    type="val",
                    description=param_docs.get(child_name, ""),
                )
                process.inputs.append(inp)
            elif "output" in child_name.lower():
                out = ProcessOutput(
                    name=child_name,
                    type="path",
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
