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

from nf_docs.cache import PipelineCache
from nf_docs.config import get_config
from nf_docs.config_parser import parse_config
from nf_docs.git_utils import GitInfo, build_source_url, get_git_info
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
from nf_docs.nf_parser import parse_process_hover, parse_workflow_hover
from nf_docs.progress import (
    ExtractionPhase,
    ProgressCallbackType,
    ProgressUpdate,
    null_progress,
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
        force_refresh: bool = False,
        progress_callback: ProgressCallbackType | None = None,
    ):
        """
        Initialize the extractor.

        Args:
            workspace_path: Path to the Nextflow pipeline workspace
            language_server_jar: Path to the language server JAR (optional)
            nextflow_path: Path to the Nextflow executable
            use_cache: Whether to use caching for extraction results
            force_refresh: Force re-extraction even if cache exists (still updates cache)
            progress_callback: Optional callback for progress updates
        """
        self.workspace_path = Path(workspace_path).resolve()
        self.language_server_jar = language_server_jar
        self.nextflow_path = nextflow_path
        self.cache = PipelineCache() if use_cache else None
        self.force_refresh = force_refresh
        self._progress = progress_callback or null_progress

    def extract(self) -> Pipeline:
        """
        Extract all documentation from the pipeline.

        Returns:
            Complete Pipeline model with all extracted information
        """
        # Display path relative to home dir for cleaner output
        try:
            display_path = f"~/{self.workspace_path.relative_to(Path.home())}"
        except ValueError:
            display_path = str(self.workspace_path)
        logger.info(f"Extracting documentation from: {display_path}")

        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.STARTING,
                message="Starting extraction...",
            )
        )

        # Check cache first (unless force_refresh is set)
        if self.cache and not self.force_refresh:
            self._progress(
                ProgressUpdate(
                    phase=ExtractionPhase.CHECKING_CACHE,
                    message="Checking cache...",
                )
            )
            cached = self.cache.get(self.workspace_path)
            if cached:
                self._progress(
                    ProgressUpdate(
                        phase=ExtractionPhase.COMPLETE,
                        message="Loaded from cache",
                    )
                )
                return cached

        pipeline = Pipeline()

        # Extract from schema (has highest priority for inputs and metadata)
        schema_file = find_schema_file(self.workspace_path)
        if schema_file:
            self._progress(
                ProgressUpdate(
                    phase=ExtractionPhase.PARSING_SCHEMA,
                    message="Parsing schema...",
                    detail=str(schema_file.name),
                )
            )
            logger.debug(f"Found schema file: {schema_file}")
            try:
                schema_metadata, schema_inputs = parse_schema(schema_file)
                pipeline.metadata = schema_metadata
                pipeline.inputs = schema_inputs
            except Exception as e:
                logger.warning(f"Failed to parse schema: {e}")

        # Extract from config
        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.PARSING_CONFIG,
                message="Parsing config...",
            )
        )
        try:
            config_metadata, config_params = parse_config(self.workspace_path, self.nextflow_path)
            # Merge metadata (schema takes priority)
            pipeline.metadata = self._merge_metadata(pipeline.metadata, config_metadata)
            # Filter config params to exclude those already in inputs and ignored prefixes
            input_names = {inp.name for inp in pipeline.inputs}
            config = get_config()
            pipeline.config_params = [
                p
                for p in config_params
                if p.name not in input_names and not config.should_ignore_config_param(p.name)
            ]
        except Exception as e:
            logger.warning(f"Failed to parse config: {e}")

        # Extract from README (full content after first h1, with base64 images)
        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.PARSING_README,
                message="Parsing README...",
            )
        )
        readme_content = self._extract_readme_content()
        if readme_content:
            pipeline.metadata.readme_content = readme_content

        # Get git info for repository URL and source links
        git_info = get_git_info(self.workspace_path)
        if git_info and git_info.base_url and not pipeline.metadata.repository:
            pipeline.metadata.repository = git_info.base_url

        # Extract from Language Server (pass git_info for source URLs)
        self._extract_from_lsp(pipeline, git_info)

        # Infer pipeline name from directory if not set
        if not pipeline.metadata.name:
            pipeline.metadata.name = self.workspace_path.name

        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.FINALIZING,
                message="Finalizing...",
            )
        )

        logger.info(
            f"Extraction complete: {len(pipeline.workflows)} workflows, "
            f"{len(pipeline.processes)} processes, {len(pipeline.functions)} functions"
        )

        # Store in cache
        if self.cache:
            self.cache.set(self.workspace_path, pipeline)

        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.COMPLETE,
                message="Extraction complete",
                detail=f"{len(pipeline.workflows)} workflows, {len(pipeline.processes)} processes, {len(pipeline.functions)} functions",
            )
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

    def _extract_readme_content(self) -> str:
        """
        Extract full README content after the first h1 heading.

        Also converts local images to base64 data URIs for portability.
        """
        readme_candidates = [
            self.workspace_path / "README.md",
            self.workspace_path / "readme.md",
            self.workspace_path / "README.rst",
        ]

        for readme_path in readme_candidates:
            if readme_path.exists():
                try:
                    content = readme_path.read_text(encoding="utf-8")
                    parsed_content = self._parse_readme_content(content)
                    # Convert local images to base64
                    return self._convert_images_to_base64(parsed_content, readme_path.parent)
                except Exception as e:
                    logger.debug(f"Failed to read README: {e}")

        return ""

    def _parse_readme_content(self, content: str) -> str:
        """
        Parse README content, returning everything after the first h1 heading.

        Strips the title (markdown # or HTML <h1>) and any badge lines immediately following.
        """
        lines = content.split("\n")
        result_lines: list[str] = []
        found_title = False
        in_html_h1 = False
        skip_badges = True

        for line in lines:
            stripped = line.strip()
            stripped_lower = stripped.lower()

            # Skip everything before/inside the first h1
            if not found_title:
                # Markdown h1
                if stripped.startswith("# "):
                    found_title = True
                    continue
                # HTML <h1> opening tag
                if "<h1" in stripped_lower:
                    in_html_h1 = True
                    # Check if it closes on the same line
                    if "</h1>" in stripped_lower:
                        found_title = True
                        in_html_h1 = False
                    continue
                # Inside HTML h1, look for closing tag
                if in_html_h1:
                    if "</h1>" in stripped_lower:
                        found_title = True
                        in_html_h1 = False
                    continue
                # Still looking for title
                continue

            # Skip badge lines immediately after title
            if skip_badges:
                # Badge patterns: [![...], ![...], [!..., or lines containing "badge"
                if (
                    stripped.startswith("[![")
                    or stripped.startswith("![")
                    or stripped.startswith("[!")
                    or "badge" in stripped_lower
                    or not stripped  # Skip empty lines in badge section
                ):
                    continue
                # First non-badge, non-empty line - stop skipping
                skip_badges = False

            result_lines.append(line)

        return "\n".join(result_lines)

    def _convert_images_to_base64(self, content: str, base_path: Path) -> str:
        """
        Convert local image references to base64 data URIs.

        Handles both markdown image syntax: ![alt](path) and HTML img tags.
        """
        import base64
        import mimetypes

        def get_mime_type(path: str) -> str:
            """Get MIME type for an image file."""
            mime_type, _ = mimetypes.guess_type(path)
            return mime_type or "application/octet-stream"

        def encode_image(image_path: Path) -> str | None:
            """Encode an image file to base64 data URI."""
            if not image_path.exists():
                logger.debug(f"Image not found: {image_path}")
                return None
            try:
                with open(image_path, "rb") as f:
                    data = base64.b64encode(f.read()).decode("utf-8")
                mime_type = get_mime_type(str(image_path))
                return f"data:{mime_type};base64,{data}"
            except Exception as e:
                logger.debug(f"Failed to encode image {image_path}: {e}")
                return None

        def is_local_path(path: str) -> bool:
            """Check if a path is local (not a URL)."""
            return not path.startswith(("http://", "https://", "data:"))

        def resolve_path(path: str) -> Path:
            """Resolve a relative path against the base path."""
            # Handle paths that start with ./
            if path.startswith("./"):
                path = path[2:]
            return base_path / path

        # Replace markdown images: ![alt](path)
        def replace_md_image(match: re.Match) -> str:
            alt = match.group(1)
            path = match.group(2)
            if is_local_path(path):
                image_path = resolve_path(path)
                data_uri = encode_image(image_path)
                if data_uri:
                    return f"![{alt}]({data_uri})"
            return match.group(0)

        content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_md_image, content)

        # Replace HTML img tags: <img src="path" ...>
        def replace_html_image(match: re.Match) -> str:
            full_tag = match.group(0)
            src_match = re.search(r'src=["\']([^"\']+)["\']', full_tag)
            if src_match:
                path = src_match.group(1)
                if is_local_path(path):
                    image_path = resolve_path(path)
                    data_uri = encode_image(image_path)
                    if data_uri:
                        return full_tag.replace(path, data_uri)
            return full_tag

        content = re.sub(r"<img[^>]+>", replace_html_image, content, flags=re.IGNORECASE)

        return content

    def _extract_from_lsp(self, pipeline: Pipeline, git_info: GitInfo | None = None) -> None:
        """Extract processes, workflows, and functions using the Language Server."""
        # Find all Nextflow files
        self._progress(
            ProgressUpdate(
                phase=ExtractionPhase.LSP_SCANNING_FILES,
                message="Scanning for Nextflow files...",
            )
        )
        nf_files = list(self.workspace_path.rglob("*.nf"))
        if not nf_files:
            logger.warning("No .nf files found in workspace")
            return

        logger.info(f"Found {len(nf_files)} Nextflow files")
        # Don't show file count yet - LSP needs to start and index first

        if git_info and git_info.base_url:
            logger.debug(f"Git repository detected: {git_info.base_url}")
        else:
            logger.debug("No git repository detected or unable to build source URLs")

        with LSPClient(
            self.workspace_path,
            server_jar=self.language_server_jar,
            progress_callback=self._progress,
        ) as client:
            # Try workspace symbols first to see what the LSP knows about
            workspace_symbols = client.get_workspace_symbols("")
            logger.debug(f"Workspace symbols: {len(workspace_symbols)}")
            if workspace_symbols:
                logger.debug(f"First few: {workspace_symbols[:3]}")

            for i, nf_file in enumerate(nf_files):
                relative_path = nf_file.relative_to(self.workspace_path)
                self._progress(
                    ProgressUpdate(
                        phase=ExtractionPhase.LSP_EXTRACTING_SYMBOLS,
                        message="Extracting symbols...",
                        current=i + 1,
                        total=len(nf_files),
                        detail=str(relative_path),
                    )
                )
                try:
                    self._extract_file_symbols(client, nf_file, pipeline, git_info)
                except Exception as e:
                    logger.warning(f"Failed to extract from {nf_file}: {e}")

    def _extract_file_symbols(
        self,
        client: LSPClient,
        file_path: Path,
        pipeline: Pipeline,
        git_info: GitInfo | None = None,
    ) -> None:
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
                self._process_symbol(client, file_path, symbol, pipeline, git_info)

        finally:
            client.close_document(file_path)

    def _parse_symbol_name(self, raw_name: str) -> tuple[str, str]:
        """
        Parse a symbol name from the Nextflow LSP.

        The Nextflow LSP returns symbol names with type prefixes like:
        - "process FASTQC"
        - "workflow PIPELINE"
        - "workflow <entry>" (for entry workflow)
        - "function myFunc"
        - "enum MyEnum"

        Args:
            raw_name: The raw symbol name from the LSP

        Returns:
            Tuple of (symbol_type, clean_name) where symbol_type is one of
            "process", "workflow", "function", "enum", or "unknown"
        """
        # Known prefixes from the Nextflow LSP
        prefixes = ["process ", "workflow ", "function ", "enum "]

        for prefix in prefixes:
            if raw_name.startswith(prefix):
                symbol_type = prefix.strip()
                clean_name = raw_name[len(prefix) :]
                # Handle special entry workflow syntax: "workflow <entry>"
                if clean_name == "<entry>":
                    clean_name = ""
                return symbol_type, clean_name

        # No prefix found - return as unknown
        return "unknown", raw_name

    def _process_symbol(
        self,
        client: LSPClient,
        file_path: Path,
        symbol: dict[str, Any],
        pipeline: Pipeline,
        git_info: GitInfo | None = None,
    ) -> None:
        """Process a document symbol and add to pipeline."""
        raw_name = symbol.get("name", "")
        kind = symbol.get("kind")  # May be None for Nextflow symbols
        range_info = symbol.get("range", {})
        selection_range = symbol.get("selectionRange", range_info)

        # Parse the symbol name to extract type and clean name
        symbol_type, name = self._parse_symbol_name(raw_name)

        # Get the line and character for hover
        start = selection_range.get("start", {})
        end = range_info.get("end", {})
        line = start.get("line", 0)
        character = start.get("character", 0)
        end_line = end.get("line", line)

        relative_path = str(file_path.relative_to(self.workspace_path))

        # Build source URL if git info available
        source_url = ""
        if git_info:
            # LSP lines are 0-based, source URLs use 1-based
            source_url = build_source_url(git_info, relative_path, line + 1, end_line + 1) or ""

        # Get hover information - contains signature and documentation
        hover = client.get_hover(file_path, line, character)
        signature, docstring, param_docs = parse_hover_content(hover)

        # Determine what kind of symbol this is based on parsed type or LSP kind
        if symbol_type == "process" or kind == SymbolKind.METHOD:
            process = self._create_process_from_signature(
                name, signature, docstring, relative_path, line + 1, end_line + 1, source_url
            )
            if process and not any(p.name == process.name for p in pipeline.processes):
                pipeline.processes.append(process)

        elif symbol_type == "workflow" or kind == SymbolKind.CLASS:
            workflow = self._create_workflow_from_signature(
                name, signature, docstring, relative_path, line + 1, end_line + 1, source_url
            )
            if workflow and not any(w.name == workflow.name for w in pipeline.workflows):
                # Entry workflow has empty name (parsed from "<entry>")
                if name == "" or name.lower() in ("main", "entry"):
                    workflow.is_entry = True
                pipeline.workflows.append(workflow)

        elif symbol_type == "function" or kind == SymbolKind.FUNCTION:
            function = self._create_function_from_signature(
                name,
                signature,
                docstring,
                param_docs,
                relative_path,
                line + 1,
                end_line + 1,
                source_url,
            )
            if function and not any(f.name == function.name for f in pipeline.functions):
                pipeline.functions.append(function)

        # Process child symbols
        for child in symbol.get("children", []):
            self._process_symbol(client, file_path, child, pipeline, git_info)

    def _create_process_from_signature(
        self,
        name: str,
        signature: str,
        docstring: str,
        file_path: str,
        line: int,
        end_line: int = 0,
        source_url: str = "",
    ) -> Process | None:
        """Create a Process by parsing the LSP signature."""
        process = Process(
            name=name,
            docstring=docstring,  # Actual Groovydoc documentation
            file=file_path,
            line=line,
            end_line=end_line,
            source_url=source_url,
        )

        # Use the nf_parser to extract inputs/outputs from the signature
        # The signature is in the format:
        # process NAME {
        #   input:
        #   tuple val(meta), path(reads)
        #
        #   output:
        #   tuple val(meta), path("*.html"), emit: html
        # }
        parsed = parse_process_hover(f"```nextflow\n{signature}\n```")
        if parsed:
            for inp in parsed.inputs:
                process.inputs.append(
                    ProcessInput(name=inp.name, type=inp.type, qualifier=inp.qualifier)
                )
            for out in parsed.outputs:
                process.outputs.append(ProcessOutput(name=out.name, type=out.type, emit=out.emit))

        return process

    def _create_workflow_from_signature(
        self,
        name: str,
        signature: str,
        docstring: str,
        file_path: str,
        line: int,
        end_line: int = 0,
        source_url: str = "",
    ) -> Workflow | None:
        """Create a Workflow by parsing the LSP signature."""
        workflow = Workflow(
            name=name,
            docstring=docstring,  # Actual Groovydoc documentation
            file=file_path,
            line=line,
            end_line=end_line,
            source_url=source_url,
        )

        # Use the nf_parser to extract takes/emits from the signature
        parsed = parse_workflow_hover(f"```nextflow\n{signature}\n```")
        if parsed:
            for take_name in parsed.takes:
                # Parse "name: Type" format if present
                if ":" in take_name:
                    n, t = take_name.split(":", 1)
                    workflow.inputs.append(WorkflowInput(name=n.strip(), type=t.strip()))
                else:
                    workflow.inputs.append(WorkflowInput(name=take_name))
            for emit_name in parsed.emits:
                # Parse "name: Type" format if present
                if ":" in emit_name:
                    n, t = emit_name.split(":", 1)
                    workflow.outputs.append(WorkflowOutput(name=n.strip(), type=t.strip()))
                else:
                    workflow.outputs.append(WorkflowOutput(name=emit_name))

        return workflow

    def _create_function_from_signature(
        self,
        name: str,
        signature: str,
        docstring: str,
        param_docs: dict[str, str],
        file_path: str,
        line: int,
        end_line: int = 0,
        source_url: str = "",
    ) -> Function | None:
        """Create a Function by parsing the LSP signature."""
        function = Function(
            name=name,
            docstring=docstring,
            file=file_path,
            line=line,
            end_line=end_line,
            source_url=source_url,
            return_description=param_docs.get("_return", ""),
        )

        # Parse function signature: def name(param1: Type, param2: Type) -> ReturnType
        # or: def name(param1, param2)
        match = re.search(r"def\s+\w+\s*\(([^)]*)\)", signature)
        if match:
            params_str = match.group(1)
            if params_str.strip():
                for param_part in params_str.split(","):
                    param_part = param_part.strip()
                    if ":" in param_part:
                        n, type_str = param_part.split(":", 1)
                        n = n.strip()
                        function.params.append(
                            FunctionParam(
                                name=n,
                                type=type_str.strip(),
                                description=param_docs.get(n, ""),
                            )
                        )
                    else:
                        n = param_part.strip()
                        function.params.append(
                            FunctionParam(
                                name=n,
                                description=param_docs.get(n, ""),
                            )
                        )

        return function
