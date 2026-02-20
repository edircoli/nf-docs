# Changelog

## [Version 0.1.0](https://github.com/ewels/nf-docs/releases/tag/v0.1.0) - 2026-02-20

Initial release of `nf-docs`.

### Added

- `nf-docs generate` command to extract and render pipeline documentation in HTML, JSON, YAML, and
  Markdown formats
- `nf-docs inspect` command for a dry-run summary of what nf-docs finds in a pipeline
- `nf-docs download-lsp` and `nf-docs clear-cache` utility commands
- Extraction of pipeline inputs from `nextflow_schema.json` and config parameters from
  `nextflow.config`
- Process, workflow, and function documentation via the Nextflow Language Server (LSP), including
  Groovydoc docstrings and typed I/O declarations
- nf-core `meta.yml` support for enriched module and subworkflow documentation
- Git-aware source code deep links for GitHub, GitLab, and Bitbucket
- XDG-compliant caching keyed by content hash and package version, with automatic invalidation
- User config file at `~/.config/nf-docs/config.yaml` for persistent defaults
