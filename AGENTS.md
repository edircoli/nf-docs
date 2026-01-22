# AGENTS.md

This file provides guidance for AI coding agents working on the nf-docs project.

## Project Overview

nf-docs is a CLI tool that generates documentation for Nextflow pipelines by querying the Nextflow
Language Server (LSP) and extracting information from `nextflow_schema.json`, `nextflow.config`, and
`README.md`.

## Build & Development

### Installation

```bash
# Install in development mode with all dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run all tests with verbose output
pytest -v

# Run a specific test file
pytest tests/test_models.py

# Run a specific test class
pytest tests/test_models.py::TestProcess

# Run a single test
pytest tests/test_models.py::TestProcess::test_creation -v

# Run tests with coverage
pytest --cov=nf_docs --cov-report=term-missing
```

### Linting & Formatting

The project uses ruff for linting/formatting and ty for type checking. Pre-commit hooks run these
automatically.

```bash
# Check for lint errors
ruff check src/ tests/

# Auto-fix lint errors
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/

# Type checking
ty check src/

# Run all pre-commit hooks manually
pre-commit run --all-files
```

### Running the CLI

```bash
# Generate docs for a pipeline (from the pipeline directory)
nf-docs generate . -f html -o ./nf-docs/

# Generate JSON output
nf-docs generate . -f json

# Skip cache (force fresh LSP extraction)
nf-docs generate . -f html --no-cache

# Enable debug logging
nf-docs generate . -f html -v
```

## Code Style Guidelines

### General Principles

- **Line length**: 100 characters max (enforced by ruff)
- **Python version**: 3.9+ (use `from __future__ import annotations` if needed)
- **Type hints**: Required for all function signatures
- **Docstrings**: Required for all public modules, classes, and functions

### Data Models

Use `@dataclass` for all data models. Follow the pattern in `models.py`:

```python
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Example:
    """Brief description of what this represents."""

    name: str
    description: str = ""
    items: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "name": self.name,
            "description": self.description,
            "items": self.items,
        }
```

### Type Hints

- Use built-in generic types: `list[str]`, `dict[str, Any]`, `tuple[int, str]`
- Use `X | None` instead of `Optional[X]`
- Import `Any` from `typing` when needed

### Imports

Imports are sorted by ruff (isort rules). Order:

1. Standard library
2. Third-party packages
3. Local imports

### Error Handling

- Use specific exception types where appropriate
- Log errors at appropriate levels (debug, info, warning, error)
- Provide context in error messages

```python
import logging

logger = logging.getLogger(__name__)

def example():
    try:
        result = some_operation()
    except SpecificError as e:
        logger.warning("Operation failed: %s", e)
        return None
```

### Logging

- Use `logging.getLogger(__name__)` at module level
- Debug: LSP communication, cache details, internal state
- Info: User-relevant progress (e.g., "Using cached results")
- Warning: Recoverable issues
- Error: Failures that affect output

### Testing

Tests use pytest with pytest-asyncio for async tests. Follow existing patterns:

```python
import pytest
from nf_docs.models import Process


class TestProcess:
    """Tests for Process model."""

    def test_creation(self):
        """Test basic process creation."""
        process = Process(name="FASTQC", docstring="QC tool")
        assert process.name == "FASTQC"
        assert process.docstring == "QC tool"

    def test_to_dict(self):
        """Test dictionary conversion."""
        process = Process(name="TEST")
        result = process.to_dict()
        assert result["name"] == "TEST"
```

For async tests:

```python
import pytest


@pytest.mark.asyncio
async def test_async_operation():
    """Test async functionality."""
    result = await some_async_function()
    assert result is not None
```

### File Organization

```
src/nf_docs/
├── __init__.py      # Package version (from importlib.metadata)
├── cli.py           # CLI entry point (rich-click)
├── cache.py         # Caching logic with version invalidation
├── extractor.py     # Main extraction orchestration
├── lsp_client.py    # Nextflow LSP communication
├── git_utils.py     # Git repository utilities
├── models.py        # Data models (dataclasses)
├── nf_parser.py     # Nextflow DSL parsing
├── renderers/       # Output format renderers
│   ├── __init__.py
│   ├── html.py
│   ├── json_renderer.py
│   └── markdown.py
└── templates/       # Jinja2 templates
    └── html.html
```

## Architecture Notes

### LSP Integration

The Nextflow Language Server provides symbols (processes, workflows, functions) via JSON-RPC over
stdio. Key quirks:

- Symbol names come prefixed: `"process FASTQC"`, `"workflow MAIN"`
- Hover results include signature code block followed by `---` then Groovydoc
- Workspace must be indexed via `didChangeConfiguration` before queries work

### Caching

Cache is stored in `~/.cache/nf-docs/` and keyed by:

- Pipeline path
- Package version (invalidates on upgrade)
- Content hash of Nextflow files

### HTML Output

The HTML renderer uses a single Jinja2 template with:

- Inline CSS (Tailwind-based)
- Inline JavaScript for search functionality
- Three-column responsive layout
- Full-text search across all documentation
