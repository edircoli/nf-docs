# Contributing to nf-docs

Thank you for your interest in contributing to nf-docs! This document covers everything you need to
know to get started with development.

## Development Setup

### Prerequisites

- Python 3.10+
- Java 11+ (for the Nextflow Language Server)
- Node.js 18+ (for building Tailwind CSS, only needed when modifying HTML templates)

### Installation

```bash
# Clone the repository
git clone https://github.com/ewels/nf-docs.git
cd nf-docs

# Install in development mode with all dev dependencies
pip install -e ".[dev]"

# Or with uv (recommended)
uv pip install -e ".[dev]"
```

### Pre-commit Hooks

This project uses [prek](https://prek.j178.dev/) to run checks before each commit:

```bash
# Install prek (macOS/Linux)
curl -fsSL https://prek.j178.dev/install.sh | sh

# Set up pre-commit hooks
prek install
```

The hooks run:

- **ruff** - Linting and formatting for Python
- **ty** - Type checking
- **prettier** - Formatting for Markdown and YAML

To run all checks manually:

```bash
prek run --all-files
```

## Running Tests

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

## Linting & Formatting

The project uses ruff for linting/formatting and ty for type checking:

```bash
# Check for lint errors
ruff check src/ tests/

# Auto-fix lint errors
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/

# Type checking
ty check src/
```

## Running the CLI

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

## Project Structure

```
src/nf_docs/
├── __init__.py      # Package version (from importlib.metadata)
├── cli.py           # CLI entry point (rich-click)
├── cache.py         # Caching logic with version invalidation
├── config.py        # User configuration (~/.config/nf-docs/config.yaml)
├── extractor.py     # Main extraction orchestration
├── lsp_client.py    # Nextflow LSP communication
├── git_utils.py     # Git repository utilities
├── models.py        # Data models (dataclasses)
├── nf_parser.py     # Nextflow DSL parsing
├── renderers/       # Output format renderers
│   ├── __init__.py
│   ├── base.py
│   ├── html.py
│   ├── json_renderer.py
│   ├── markdown.py
│   └── yaml_renderer.py
└── templates/       # Jinja2 templates
    ├── html.html
    └── tailwind.css # Pre-built Tailwind CSS
```

## Code Style Guidelines

### General Principles

- **Line length**: 100 characters max (enforced by ruff)
- **Python version**: 3.10+ (native union types like `X | None` are supported)
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

## Building Tailwind CSS

The HTML output uses pre-built Tailwind CSS. If you modify the HTML template
(`src/nf_docs/templates/html.html`) or the input CSS (`build-assets/input.css`), you need to rebuild
the CSS.

**The pre-commit hook will automatically rebuild the CSS** when you commit changes to the template
or input CSS files. The CI will also verify the CSS is up to date.

To manually rebuild:

```bash
cd build-assets

# Install dependencies (first time only)
npm install

# Build the CSS
npm run build

# Or watch for changes during development
npm run watch
```

Alternatively, use the shell script:

```bash
./build-assets/build-tailwind.sh
```

The generated CSS is committed to the repository (`src/nf_docs/templates/tailwind.css`) so that end
users don't need Node.js installed.

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

### Configuration

User configuration is loaded from `~/.config/nf-docs/config.yaml` (or `$XDG_CONFIG_HOME`). See
`nf-docs config --show-example` for available options.

### HTML Output

The HTML renderer uses a single Jinja2 template with:

- Pre-built Tailwind CSS (no runtime processing)
- Inline JavaScript for search functionality
- Three-column responsive layout
- Full-text search across all documentation
- Dark mode support

## Test Pipelines

For testing, try these pipelines:

- [nextflow-io/rnaseq-nf](https://github.com/nextflow-io/rnaseq-nf) - Simple, good for initial
  testing
- [nf-core/fetchngs](https://github.com/nf-core/fetchngs) - Small but real
- [nf-core/rnaseq](https://github.com/nf-core/rnaseq) - Complex, good stress test

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Run linting (`prek run --all-files`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Questions?

Feel free to open an issue for questions or discussion.
