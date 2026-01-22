"""Tests for the CLI interface."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from nf_docs.cli import generate, inspect, main


@pytest.fixture
def runner():
    """Create a CLI runner."""
    return CliRunner()


class TestMainCommand:
    def test_help(self, runner: CliRunner):
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Generate API documentation" in result.output

    def test_version(self, runner: CliRunner):
        result = runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "nf-docs" in result.output


class TestGenerateCommand:
    def test_generate_help(self, runner: CliRunner):
        result = runner.invoke(generate, ["--help"])
        assert result.exit_code == 0
        assert "Generate documentation" in result.output

    def test_generate_json(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(generate, [str(sample_pipeline), "--format", "json", "--no-lsp"])
        assert result.exit_code == 0
        # Output should be JSON
        assert '"pipeline"' in result.output

    def test_generate_yaml(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(generate, [str(sample_pipeline), "--format", "yaml", "--no-lsp"])
        assert result.exit_code == 0
        # Output should be YAML
        assert "pipeline:" in result.output

    def test_generate_markdown_to_directory(self, runner: CliRunner, sample_pipeline: Path, tmp_path: Path):
        output_dir = tmp_path / "docs"
        result = runner.invoke(
            generate,
            [str(sample_pipeline), "--format", "markdown", "--output", str(output_dir), "--no-lsp"],
        )
        assert result.exit_code == 0
        assert output_dir.exists()
        assert (output_dir / "index.md").exists()

    def test_generate_html_to_directory(self, runner: CliRunner, sample_pipeline: Path, tmp_path: Path):
        output_dir = tmp_path / "site"
        result = runner.invoke(
            generate,
            [str(sample_pipeline), "--format", "html", "--output", str(output_dir), "--no-lsp"],
        )
        assert result.exit_code == 0
        assert output_dir.exists()
        assert (output_dir / "index.html").exists()

    def test_generate_with_custom_title(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(
            generate,
            [str(sample_pipeline), "--format", "json", "--title", "My Custom Title", "--no-lsp"],
        )
        assert result.exit_code == 0
        assert "My Custom Title" in result.output

    def test_generate_nonexistent_path(self, runner: CliRunner):
        result = runner.invoke(generate, ["/nonexistent/path", "--format", "json"])
        assert result.exit_code != 0

    def test_generate_verbose(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(
            generate,
            [str(sample_pipeline), "--format", "json", "--verbose", "--no-lsp"],
        )
        assert result.exit_code == 0


class TestInspectCommand:
    def test_inspect_help(self, runner: CliRunner):
        result = runner.invoke(inspect, ["--help"])
        assert result.exit_code == 0
        assert "Inspect" in result.output

    def test_inspect_pipeline(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(inspect, [str(sample_pipeline)])
        assert result.exit_code == 0
        # Should show summary
        assert "Pipeline:" in result.output
        assert "Processes:" in result.output or "processes" in result.output.lower()

    def test_inspect_empty_directory(self, runner: CliRunner, tmp_path: Path):
        result = runner.invoke(inspect, [str(tmp_path)])
        assert result.exit_code == 0

    def test_inspect_verbose(self, runner: CliRunner, sample_pipeline: Path):
        result = runner.invoke(inspect, [str(sample_pipeline), "--verbose"])
        assert result.exit_code == 0
