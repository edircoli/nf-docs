<div align="center">

# nf-docs

**Generate beautiful API documentation for Nextflow pipelines**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

![nf-docs demo](docs/images/demo.gif)

Choose from 3 different output formats:

</div>

<table width="100%">
<tr>
<td width="33%">
<h3 align="center">HTML</h3>
<ul><li>Single-file output</li><li>Share anywhere, even offline</li><li>Full-text search built in</li></ul><hr>
</td>
<td width="33%">
<h3 align="center">Markdown</h3>
<ul><li>Multiple files by section</li><li>Perfect for static site generators</li></ul><hr>
</td>
<td width="33%">
<h3 align="center">JSON / YAML</h3>
<ul><li>Machine-readable output</li><li>Build custom integrations</li><li>CI/CD friendly</li></ul><hr>
</td>
</tr>
</table>

## What is nf-docs?

Information is pulled from multiple sources to construct the docs (each only if available):

- **README.md** - Pipeline overview and description
- **nextflow.config** - Runtime configuration defaults
- **nextflow_schema.json** - Typed input parameters with descriptions and validation rules
- **Language Server** - Processes, workflows, functions with their Groovydoc comments
- **meta.yml** - nf-core module metadata (tools, keywords, authors)

The documentation for workflows, processes and functions is relatively unique. `nf-docs` extracts
this from your Nextflow pipelines by querying the
[Nextflow Language Server](https://github.com/nextflow-io/language-server). It produces structured
API documentation similar to Sphinx for Python or Javadoc for Java.

> **See it in action:** Browse generated documentation for real pipelines in
> [`examples/html/`](examples/html/), including [nf-core/sarek](examples/html/sarek/index.html) and
> [nf-core/rnavar](examples/html/rnavar/index.html).

## Quick Start

With [`uv`](https://docs.astral.sh/uv/):

```bash
uvx nf-docs generate ./my_pipeline
```

With `pip`:

```bash
# Install
pip install nf-docs

# Generate HTML documentation
nf-docs generate ./my_pipeline
```

That's it! Open `docs/index.html` in your browser.

## Installation

```bash
# With pip
pip install nf-docs

# With uv (faster)
uv tool install nf-docs

# Development install
pip install -e ".[dev]"
```

**Requirements:**

- Python 3.10+
- Java 11+ (for the Nextflow Language Server)
- Nextflow (optional, for parsing `nextflow.config`)

## Usage

### Generate Documentation

```bash
nf-docs generate PIPELINE_PATH [OPTIONS]
```

| Option              | Description                                       |
| ------------------- | ------------------------------------------------- |
| `--format`, `-f`    | Output format: `html`, `markdown`, `json`, `yaml` |
| `--output`, `-o`    | Output file or directory                          |
| `--title`, `-t`     | Custom title for documentation                    |
| `--no-cache`        | Force fresh extraction (ignore cache)             |
| `--verbose`, `-v`   | Enable debug output                               |
| `--language-server` | Path to Language Server JAR                       |

**Examples:**

```bash
# HTML - single file, shareable, works offline
nf-docs generate . -f html -o site/

# Markdown - multiple files for static site generators
nf-docs generate . -f markdown -o docs/

# JSON - pipe to file or other tools
nf-docs generate . -f json > api.json
```

### Other Commands

```bash
# Quick inspection (summary only)
nf-docs inspect /path/to/pipeline

# Pre-download the Language Server
nf-docs download-lsp
```

## Output Formats

### HTML

A self-contained single HTML file with everything included:

- Three-column responsive layout
- Full-text search across all documentation
- Deep linking to every section and item
- Source code links (GitHub, GitLab, Bitbucket)
- nf-core module documentation links
- Dark mode support
- Mobile-friendly design

### Markdown

Generates a directory of Markdown files, perfect for integration with documentation platforms:

```
docs/
├── index.md        # Pipeline overview
├── inputs.md       # Input parameters from schema
├── config.md       # Config parameters
├── workflows.md    # Workflow documentation
├── processes.md    # Process documentation
└── functions.md    # Function documentation
```

### JSON / YAML

Structured data for programmatic use, CI/CD pipelines, or building custom tooling.

## Writing Documentation

`nf-docs` extracts Groovydoc-style comments from your Nextflow code:

```nextflow
/**
 * Align reads to a reference genome using BWA MEM.
 *
 * This process handles both single-end and paired-end reads,
 * automatically detecting the input format.
 *
 * @param reads Tuple of sample ID and FASTQ files
 * @param index BWA index files
 * @return Tuple of sample ID and aligned BAM file
 */
process BWA_MEM {
    input:
    tuple val(sample_id), path(reads)
    path index

    output:
    tuple val(sample_id), path("*.bam"), emit: bam

    script:
    // ...
}
```

For input parameters, use
[nf-schema](https://nextflow-io.github.io/nf-schema/latest/nextflow_schema/)'s
`nextflow_schema.json`:

```json
{
  "$defs": {
    "input_output_options": {
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "description": "Path to the sample sheet",
          "help_text": "The sample sheet should be a CSV file with columns..."
        }
      }
    }
  }
}
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and contribution guidelines.

## License

Apache 2.0 - see [LICENSE](LICENSE) for details.
