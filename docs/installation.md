# Installation

## Requirements

- Python 3.10+
- Java 11+ (for the Nextflow Language Server)
- Nextflow (optional — needed for parsing `nextflow.config`)

## Install

=== ":simple-astral:{ .middle } &nbsp; uv"

    ```bash
    # Run as one-off
    uvx nf-docs ./my-pipeline
    ```

    ```bash
    # Install so "nf-docs" is available globally
    uv tool install nf-docs

    # Run
    nf-docs ./my_pipeline
    ```

=== ":simple-python:{ .middle } &nbsp; pip"

    ```bash
    # Install
    pip install nf-docs

    # Run
    nf-docs ./my_pipeline
    ```

=== ":simple-git:{ .middle } &nbsp; Development"

    ```bash
    # Clone the git repo locally
    git clone https://github.com/ewels/nf-docs

    # Install in 'editable' mode with dev dependencies
    pip install -e ".[dev]"

    # Run
    nf-docs ./my_pipeline
    ```
