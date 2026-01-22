"""
LSP Client for communicating with the Nextflow Language Server.

This module handles:
- Spawning the language server JAR as a subprocess
- JSON-RPC communication over stdin/stdout
- LSP protocol initialization and shutdown
- Querying document symbols and hover information
"""

import json
import logging
import os
import re
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.request import urlretrieve

import httpx

logger = logging.getLogger(__name__)

# Language server download URL (GitHub releases)
LANGUAGE_SERVER_REPO = "nextflow-io/language-server"
LANGUAGE_SERVER_JAR = "language-server-all.jar"


class LSPError(Exception):
    """Exception raised for LSP-related errors."""

    pass


class LSPClient:
    """
    Client for the Nextflow Language Server.

    Communicates via JSON-RPC over stdin/stdout with the language server
    process to extract documentation information from Nextflow files.
    """

    def __init__(
        self,
        workspace_path: str | Path,
        server_jar: str | Path | None = None,
        java_path: str = "java",
        auto_download: bool = True,
    ):
        """
        Initialize the LSP client.

        Args:
            workspace_path: Path to the Nextflow pipeline workspace
            server_jar: Path to the language server JAR (optional, will auto-download)
            java_path: Path to Java executable
            auto_download: Whether to auto-download the language server if not found
        """
        self.workspace_path = Path(workspace_path).resolve()
        self.java_path = java_path
        self.auto_download = auto_download
        self._process: subprocess.Popen | None = None
        self._request_id = 0
        self._response_lock = threading.Lock()
        self._responses: dict[int, Any] = {}
        self._reader_thread: threading.Thread | None = None
        self._running = False

        # Find or download language server
        if server_jar:
            self.server_jar = Path(server_jar)
            if not self.server_jar.exists():
                raise LSPError(f"Language server JAR not found: {server_jar}")
        else:
            self.server_jar = self._find_or_download_server()

    def _find_or_download_server(self) -> Path:
        """Find or download the language server JAR."""
        # Check common locations
        search_paths = [
            Path.home() / ".nf-docs" / LANGUAGE_SERVER_JAR,
            Path.home() / ".local" / "share" / "nf-docs" / LANGUAGE_SERVER_JAR,
            Path("/usr/local/share/nf-docs") / LANGUAGE_SERVER_JAR,
        ]

        for path in search_paths:
            if path.exists():
                logger.info(f"Found language server at: {path}")
                return path

        if not self.auto_download:
            raise LSPError(
                "Language server JAR not found. Please provide --language-server path "
                "or enable auto-download."
            )

        # Download to user directory
        download_dir = Path.home() / ".nf-docs"
        download_dir.mkdir(parents=True, exist_ok=True)
        target_path = download_dir / LANGUAGE_SERVER_JAR

        logger.info("Downloading Nextflow Language Server...")
        self._download_language_server(target_path)
        return target_path

    def _download_language_server(self, target_path: Path) -> None:
        """Download the latest language server release from GitHub."""
        # Get latest release info
        api_url = f"https://api.github.com/repos/{LANGUAGE_SERVER_REPO}/releases/latest"

        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(api_url)
                response.raise_for_status()
                release_info = response.json()

            # Find the JAR asset
            jar_url = None
            for asset in release_info.get("assets", []):
                if asset["name"] == LANGUAGE_SERVER_JAR:
                    jar_url = asset["browser_download_url"]
                    break

            if not jar_url:
                raise LSPError(
                    f"Could not find {LANGUAGE_SERVER_JAR} in latest release. "
                    "Please download manually from "
                    f"https://github.com/{LANGUAGE_SERVER_REPO}/releases"
                )

            # Download the JAR
            logger.info(f"Downloading from: {jar_url}")
            urlretrieve(jar_url, target_path)
            logger.info(f"Downloaded language server to: {target_path}")

        except httpx.HTTPError as e:
            raise LSPError(f"Failed to download language server: {e}") from e

    def _get_workspace_uri(self) -> str:
        """Get the workspace path as a file URI."""
        path = str(self.workspace_path)
        if sys.platform == "win32":
            path = "/" + path.replace("\\", "/")
        return f"file://{quote(path, safe='/:')}"

    def _get_document_uri(self, file_path: str | Path) -> str:
        """Get a file path as a document URI."""
        path = Path(file_path).resolve()
        path_str = str(path)
        if sys.platform == "win32":
            path_str = "/" + path_str.replace("\\", "/")
        return f"file://{quote(path_str, safe='/:')}"

    def start(self) -> None:
        """Start the language server process."""
        if self._process is not None:
            return

        # Check Java is available
        try:
            subprocess.run(
                [self.java_path, "-version"],
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            raise LSPError(
                f"Java not found or not working. Please install Java 11+ and ensure "
                f"it's on your PATH. Error: {e}"
            ) from e

        logger.info(f"Starting language server: {self.server_jar}")

        self._process = subprocess.Popen(
            [self.java_path, "-jar", str(self.server_jar)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(self.workspace_path),
        )

        self._running = True
        self._reader_thread = threading.Thread(target=self._read_responses, daemon=True)
        self._reader_thread.start()

        # Initialize the server
        self._initialize()

    def _read_responses(self) -> None:
        """Background thread to read responses from the server."""
        assert self._process is not None
        assert self._process.stdout is not None

        while self._running:
            try:
                # Read headers
                headers = {}
                while True:
                    line = self._process.stdout.readline()
                    if not line:
                        self._running = False
                        return
                    line = line.decode("utf-8").strip()
                    if not line:
                        break
                    if ":" in line:
                        key, value = line.split(":", 1)
                        headers[key.strip().lower()] = value.strip()

                # Read content
                content_length = int(headers.get("content-length", 0))
                if content_length > 0:
                    content = self._process.stdout.read(content_length)
                    message = json.loads(content.decode("utf-8"))

                    # Handle response
                    if "id" in message:
                        with self._response_lock:
                            self._responses[message["id"]] = message

            except Exception as e:
                logger.debug(f"Error reading response: {e}")
                if not self._running:
                    break

    def _send_request(self, method: str, params: dict | None = None) -> Any:
        """Send a request to the language server and wait for response."""
        assert self._process is not None
        assert self._process.stdin is not None

        self._request_id += 1
        request_id = self._request_id

        message = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
        }
        if params is not None:
            message["params"] = params

        content = json.dumps(message)
        header = f"Content-Length: {len(content)}\r\n\r\n"

        self._process.stdin.write(header.encode("utf-8"))
        self._process.stdin.write(content.encode("utf-8"))
        self._process.stdin.flush()

        # Wait for response
        import time

        timeout = 30.0
        start = time.time()
        while time.time() - start < timeout:
            with self._response_lock:
                if request_id in self._responses:
                    response = self._responses.pop(request_id)
                    if "error" in response:
                        raise LSPError(
                            f"LSP error: {response['error'].get('message', 'Unknown error')}"
                        )
                    return response.get("result")
            time.sleep(0.01)

        raise LSPError(f"Timeout waiting for response to {method}")

    def _send_notification(self, method: str, params: dict | None = None) -> None:
        """Send a notification to the language server (no response expected)."""
        assert self._process is not None
        assert self._process.stdin is not None

        message = {
            "jsonrpc": "2.0",
            "method": method,
        }
        if params is not None:
            message["params"] = params

        content = json.dumps(message)
        header = f"Content-Length: {len(content)}\r\n\r\n"

        self._process.stdin.write(header.encode("utf-8"))
        self._process.stdin.write(content.encode("utf-8"))
        self._process.stdin.flush()

    def _initialize(self) -> None:
        """Initialize the language server with workspace information."""
        workspace_uri = self._get_workspace_uri()

        init_params = {
            "processId": os.getpid(),
            "rootUri": workspace_uri,
            "rootPath": str(self.workspace_path),
            "capabilities": {
                "textDocument": {
                    "hover": {
                        "contentFormat": ["markdown", "plaintext"],
                    },
                    "documentSymbol": {
                        "hierarchicalDocumentSymbolSupport": True,
                    },
                },
                "workspace": {
                    "symbol": {
                        "symbolKind": {
                            "valueSet": list(range(1, 27)),
                        },
                    },
                },
            },
            "workspaceFolders": [
                {
                    "uri": workspace_uri,
                    "name": self.workspace_path.name,
                }
            ],
        }

        result = self._send_request("initialize", init_params)
        logger.debug(f"Server capabilities: {result}")

        # Send initialized notification
        self._send_notification("initialized", {})
        logger.info("Language server initialized")

    def stop(self) -> None:
        """Stop the language server process."""
        if self._process is None:
            return

        self._running = False

        try:
            self._send_request("shutdown")
            self._send_notification("exit")
        except Exception:
            pass

        try:
            self._process.terminate()
            self._process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self._process.kill()
            self._process.wait()

        self._process = None
        logger.info("Language server stopped")

    def __enter__(self) -> "LSPClient":
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.stop()

    def open_document(self, file_path: str | Path) -> None:
        """
        Notify the server that a document is open.

        This must be done before querying symbols or hover for a document.
        """
        path = Path(file_path).resolve()
        content = path.read_text(encoding="utf-8")

        self._send_notification(
            "textDocument/didOpen",
            {
                "textDocument": {
                    "uri": self._get_document_uri(path),
                    "languageId": "nextflow",
                    "version": 1,
                    "text": content,
                }
            },
        )

    def close_document(self, file_path: str | Path) -> None:
        """Notify the server that a document is closed."""
        self._send_notification(
            "textDocument/didClose",
            {
                "textDocument": {
                    "uri": self._get_document_uri(file_path),
                }
            },
        )

    def get_document_symbols(self, file_path: str | Path) -> list[dict[str, Any]]:
        """
        Get all symbols in a document.

        Returns a list of DocumentSymbol objects containing:
        - name: Symbol name
        - kind: Symbol kind (6=Method, 12=Function, 5=Class, etc.)
        - range: Location in the document
        - selectionRange: Location of the symbol name
        - children: Nested symbols
        """
        result = self._send_request(
            "textDocument/documentSymbol",
            {
                "textDocument": {
                    "uri": self._get_document_uri(file_path),
                }
            },
        )
        return result or []

    def get_hover(
        self, file_path: str | Path, line: int, character: int
    ) -> dict[str, Any] | None:
        """
        Get hover information at a specific position.

        Args:
            file_path: Path to the document
            line: Zero-based line number
            character: Zero-based character position

        Returns:
            Hover information including docstring and type info, or None
        """
        result = self._send_request(
            "textDocument/hover",
            {
                "textDocument": {
                    "uri": self._get_document_uri(file_path),
                },
                "position": {
                    "line": line,
                    "character": character,
                },
            },
        )
        return result

    def get_workspace_symbols(self, query: str = "") -> list[dict[str, Any]]:
        """
        Search for symbols across the workspace.

        Args:
            query: Search query (empty string returns all symbols)

        Returns:
            List of SymbolInformation objects
        """
        result = self._send_request(
            "workspace/symbol",
            {
                "query": query,
            },
        )
        return result or []


# Symbol kind constants from LSP specification
class SymbolKind:
    """LSP Symbol Kind constants."""

    FILE = 1
    MODULE = 2
    NAMESPACE = 3
    PACKAGE = 4
    CLASS = 5
    METHOD = 6
    PROPERTY = 7
    FIELD = 8
    CONSTRUCTOR = 9
    ENUM = 10
    INTERFACE = 11
    FUNCTION = 12
    VARIABLE = 13
    CONSTANT = 14
    STRING = 15
    NUMBER = 16
    BOOLEAN = 17
    ARRAY = 18
    OBJECT = 19
    KEY = 20
    NULL = 21
    ENUM_MEMBER = 22
    STRUCT = 23
    EVENT = 24
    OPERATOR = 25
    TYPE_PARAMETER = 26


def parse_hover_content(hover: dict[str, Any] | None) -> tuple[str, dict[str, str]]:
    """
    Parse hover content to extract docstring and param descriptions.

    Args:
        hover: Hover response from LSP

    Returns:
        Tuple of (main_docstring, param_descriptions)
        where param_descriptions is a dict mapping param names to descriptions
    """
    if not hover or "contents" not in hover:
        return "", {}

    contents = hover["contents"]

    # Handle MarkupContent
    if isinstance(contents, dict):
        text = contents.get("value", "")
    elif isinstance(contents, str):
        text = contents
    elif isinstance(contents, list):
        # MarkedString[]
        text = "\n".join(
            item.get("value", item) if isinstance(item, dict) else str(item) for item in contents
        )
    else:
        return "", {}

    # Parse Javadoc-style comments
    docstring = ""
    params: dict[str, str] = {}

    lines = text.split("\n")
    current_section = "description"
    current_param = ""

    for line in lines:
        line = line.strip()

        # Skip code fence markers
        if line.startswith("```"):
            continue

        # Check for @param tag
        param_match = re.match(r"@param\s+(\w+)\s*(.*)", line)
        if param_match:
            current_section = "param"
            current_param = param_match.group(1)
            params[current_param] = param_match.group(2).strip()
            continue

        # Check for @return tag
        return_match = re.match(r"@returns?\s*(.*)", line)
        if return_match:
            current_section = "return"
            params["_return"] = return_match.group(1).strip()
            continue

        # Handle continuation lines
        if current_section == "description":
            if line and not line.startswith("@"):
                if docstring:
                    docstring += " " + line
                else:
                    docstring = line
        elif current_section == "param" and current_param:
            if line and not line.startswith("@"):
                params[current_param] += " " + line

    return docstring.strip(), params
