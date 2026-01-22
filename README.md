# nf-docs

Generate API documentation for Nextflow pipelines by querying the Nextflow Language Server.

`nf-docs` extracts docstrings and type information from Nextflow pipelines, producing structured documentation similar to Sphinx for Python or Javadoc. It combines information from multiple sources:

- **Language Server**: Processes, workflows, functions with their docstrings
- **nextflow_schema.json**: Typed input parameters with descriptions
- **nextflow.config**: Runtime configuration defaults
- **README.md**: Pipeline overview

## Installation

```bash
# Install from source
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

### Requirements

- Python 3.9+
- Java 11+ (for the Language Server)
- Nextflow (optional, for config parsing)

## Quick Start

```bash
# Generate Markdown documentation
nf-docs generate /path/to/pipeline --format markdown --output docs/

# Generate JSON output to stdout
nf-docs generate . --format json

# Generate a self-contained HTML site
nf-docs generate . --format html --output site/

# Inspect a pipeline without generating docs
nf-docs inspect /path/to/pipeline
```

## Usage

### Generate Command

```bash
nf-docs generate PIPELINE_PATH [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--format`, `-f` | Output format: `json`, `yaml`, `markdown`, `html` (default: markdown) |
| `--output`, `-o` | Output file or directory |
| `--title`, `-t` | Custom title for documentation |
| `--language-server` | Path to the Language Server JAR |
| `--nextflow-path` | Path to Nextflow executable (default: nextflow) |
| `--verbose`, `-v` | Enable verbose output |

**Examples:**

```bash
# Generate Markdown docs in ./docs/
nf-docs generate . --format markdown --output docs/

# Generate JSON API spec
nf-docs generate . --format json > pipeline-api.json

# Generate YAML with custom title
nf-docs generate . --format yaml --title "My Pipeline" > api.yaml

# Generate HTML site
nf-docs generate ./my-pipeline --format html -o site/

# Use specific language server JAR
nf-docs generate . --language-server /path/to/language-server-all.jar
```

### Inspect Command

Quick inspection without full documentation generation:

```bash
nf-docs inspect PIPELINE_PATH [--verbose]
```

### Download Language Server

Pre-download the Nextflow Language Server:

```bash
nf-docs download-lsp [--force]
```

## Output Formats

### JSON

Machine-readable structured data:

```json
{
  "pipeline": {
    "name": "nf-core/rnaseq",
    "version": "3.14.0",
    "description": "RNA-seq analysis pipeline"
  },
  "inputs": [
    {
      "name": "input",
      "type": "string",
      "format": "file-path",
      "description": "Path to samplesheet",
      "required": true
    }
  ],
  "workflows": [...],
  "processes": [...],
  "functions": [...]
}
```

### YAML

Human-friendly structured data (same schema as JSON).

### Markdown

Creates a documentation directory:

```
docs/
├── index.md          # Pipeline overview
├── inputs.md         # Input parameters
├── config.md         # Config parameters (if any)
├── workflows.md      # Workflow documentation
├── processes.md      # Process documentation
└── functions.md      # Functions (if any)
```

### HTML

Self-contained static site with navigation.

## Docstring Format

`nf-docs` supports Javadoc-style comments (same as the Nextflow Language Server):

```nextflow
/**
 * Align reads to a reference genome using BWA MEM.
 *
 * @param reads Tuple of sample ID and fastq files
 * @param index BWA index files
 * @return Tuple of sample ID and BAM file
 */
process BWA_MEM {
    input:
    tuple val(sample_id), path(reads)
    path index

    output:
    tuple val(sample_id), path("*.bam"), emit: bam

    script:
    ...
}
```

## Schema Support

`nf-docs` parses `nextflow_schema.json` files following the [nf-schema specification](https://nextflow-io.github.io/nf-schema/latest/nextflow_schema/):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "input_output_options": {
      "title": "Input/output options",
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "description": "Path to samplesheet",
          "help_text": "The samplesheet should contain..."
        }
      },
      "required": ["input"]
    }
  }
}
```

## Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Language Server │────▶│ Internal Schema  │────▶│ Output Renderer │
│ (symbols/hover) │     │ (unified model)  │     │ (md/html/json)  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        ▲                        ▲
        │                        │
┌───────┴───────┐       ┌───────┴────────┐
│ .nf files     │       │ nextflow_schema│
│ nextflow.config│       │ README.md      │
└───────────────┘       └────────────────┘
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=nf_docs

# Format code
black src/ tests/

# Lint
ruff check src/ tests/

# Type check
mypy src/
```

## Test Pipelines

For testing, try these pipelines:

- [nextflow-io/rnaseq-nf](https://github.com/nextflow-io/rnaseq-nf) - Simple, good for initial testing
- [nf-core/fetchngs](https://github.com/nf-core/fetchngs) - Small but real
- [nf-core/rnaseq](https://github.com/nf-core/rnaseq) - Complex, good stress test

## License

MIT License - see [LICENSE](LICENSE) for details.
