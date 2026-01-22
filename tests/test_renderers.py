"""Tests for output renderers."""

import json
from pathlib import Path

import pytest
import yaml

from nf_docs.models import (
    Pipeline,
    PipelineInput,
    PipelineMetadata,
    Process,
    ProcessInput,
    ProcessOutput,
    Workflow,
)
from nf_docs.renderers import (
    HTMLRenderer,
    JSONRenderer,
    MarkdownRenderer,
    YAMLRenderer,
    get_renderer,
)


@pytest.fixture
def sample_pipeline() -> Pipeline:
    """Create a sample pipeline for testing renderers."""
    return Pipeline(
        metadata=PipelineMetadata(
            name="test-pipeline",
            description="A test pipeline",
            version="1.0.0",
            authors=["Test Author"],
        ),
        inputs=[
            PipelineInput(
                name="input",
                type="string",
                description="Input file path",
                required=True,
                group="Input/output",
            ),
            PipelineInput(
                name="outdir",
                type="string",
                description="Output directory",
                default="./results",
                group="Input/output",
            ),
        ],
        workflows=[
            Workflow(
                name="MAIN",
                docstring="Main workflow",
                file="main.nf",
                line=10,
                is_entry=True,
                calls=["PROCESS_A", "PROCESS_B"],
            ),
        ],
        processes=[
            Process(
                name="PROCESS_A",
                docstring="First process",
                file="main.nf",
                line=20,
                inputs=[ProcessInput(name="input_file", type="path")],
                outputs=[ProcessOutput(name="*.txt", type="path", emit="output")],
                directives={"cpus": 2, "memory": "4.GB"},
            ),
            Process(
                name="PROCESS_B",
                docstring="Second process",
                file="main.nf",
                line=40,
            ),
        ],
    )


class TestGetRenderer:
    def test_get_json_renderer(self):
        renderer_class = get_renderer("json")
        assert renderer_class == JSONRenderer

    def test_get_yaml_renderer(self):
        renderer_class = get_renderer("yaml")
        assert renderer_class == YAMLRenderer

    def test_get_markdown_renderer(self):
        renderer_class = get_renderer("markdown")
        assert renderer_class == MarkdownRenderer

    def test_get_md_renderer(self):
        renderer_class = get_renderer("md")
        assert renderer_class == MarkdownRenderer

    def test_get_html_renderer(self):
        renderer_class = get_renderer("html")
        assert renderer_class == HTMLRenderer

    def test_invalid_format(self):
        with pytest.raises(ValueError, match="Unsupported format"):
            get_renderer("invalid")


class TestJSONRenderer:
    def test_render(self, sample_pipeline: Pipeline):
        renderer = JSONRenderer()
        output = renderer.render(sample_pipeline)

        # Should be valid JSON
        data = json.loads(output)

        assert data["pipeline"]["name"] == "test-pipeline"
        assert len(data["inputs"]) == 2
        assert len(data["processes"]) == 2

    def test_render_with_custom_title(self, sample_pipeline: Pipeline):
        renderer = JSONRenderer(title="Custom Title")
        output = renderer.render(sample_pipeline)

        data = json.loads(output)
        assert data["pipeline"]["name"] == "Custom Title"

    def test_render_to_directory(self, sample_pipeline: Pipeline, tmp_path: Path):
        renderer = JSONRenderer()
        files = renderer.render_to_directory(sample_pipeline, tmp_path)

        assert len(files) == 1
        assert files[0].exists()
        assert files[0].suffix == ".json"

        # Verify content
        data = json.loads(files[0].read_text())
        assert data["pipeline"]["name"] == "test-pipeline"


class TestYAMLRenderer:
    def test_render(self, sample_pipeline: Pipeline):
        renderer = YAMLRenderer()
        output = renderer.render(sample_pipeline)

        # Should be valid YAML
        data = yaml.safe_load(output)

        assert data["pipeline"]["name"] == "test-pipeline"
        assert len(data["inputs"]) == 2

    def test_render_to_directory(self, sample_pipeline: Pipeline, tmp_path: Path):
        renderer = YAMLRenderer()
        files = renderer.render_to_directory(sample_pipeline, tmp_path)

        assert len(files) == 1
        assert files[0].suffix == ".yaml"


class TestMarkdownRenderer:
    def test_render_index(self, sample_pipeline: Pipeline):
        renderer = MarkdownRenderer()
        output = renderer.render(sample_pipeline)

        # Check for key sections
        assert "# test-pipeline" in output
        assert "Version:" in output
        assert "A test pipeline" in output

    def test_render_inputs(self, sample_pipeline: Pipeline):
        renderer = MarkdownRenderer()
        output = renderer.render(sample_pipeline)

        # Check inputs are documented
        assert "--input" in output
        assert "--outdir" in output
        assert "Required" in output

    def test_render_processes(self, sample_pipeline: Pipeline):
        renderer = MarkdownRenderer()
        output = renderer.render(sample_pipeline)

        # Check processes are documented
        assert "PROCESS_A" in output
        assert "PROCESS_B" in output
        assert "First process" in output

    def test_render_to_directory(self, sample_pipeline: Pipeline, tmp_path: Path):
        renderer = MarkdownRenderer()
        files = renderer.render_to_directory(sample_pipeline, tmp_path)

        # Should create multiple files
        assert len(files) >= 3  # At least index, inputs, processes

        # Check expected files exist
        file_names = {f.name for f in files}
        assert "index.md" in file_names
        assert "inputs.md" in file_names
        assert "processes.md" in file_names

    def test_render_workflows_with_calls(self, sample_pipeline: Pipeline):
        renderer = MarkdownRenderer()
        output = renderer.render(sample_pipeline)

        # Check workflow calls are linked
        assert "PROCESS_A" in output
        assert "processes.md#" in output  # Link to process

    def test_custom_title(self, sample_pipeline: Pipeline):
        renderer = MarkdownRenderer(title="My Custom Title")
        output = renderer.render(sample_pipeline)

        assert "# My Custom Title" in output


class TestHTMLRenderer:
    def test_render(self, sample_pipeline: Pipeline):
        renderer = HTMLRenderer(use_tailwind=False)
        output = renderer.render(sample_pipeline)

        # Should be valid HTML (lowercase doctype is valid HTML5)
        assert "<!doctype html>" in output.lower()
        assert "<html" in output
        assert "</html>" in output

    def test_render_contains_content(self, sample_pipeline: Pipeline):
        renderer = HTMLRenderer(use_tailwind=False)
        output = renderer.render(sample_pipeline)

        # Check content is present
        assert "test-pipeline" in output
        assert "PROCESS_A" in output
        assert "PROCESS_B" in output
        assert "--input" in output

    def test_render_contains_navigation(self, sample_pipeline: Pipeline):
        renderer = HTMLRenderer(use_tailwind=False)
        output = renderer.render(sample_pipeline)

        # Check navigation elements (using Tailwind classes now)
        assert "<aside" in output
        assert "<nav" in output
        assert "Overview" in output
        assert "Inputs" in output
        assert "Processes" in output

    def test_render_self_contained(self, sample_pipeline: Pipeline):
        renderer = HTMLRenderer(use_tailwind=False)
        output = renderer.render(sample_pipeline)

        # Should include inline CSS and JS
        assert "<style>" in output
        assert "</style>" in output
        assert "<script>" in output
        assert "</script>" in output

    def test_render_to_directory(self, sample_pipeline: Pipeline, tmp_path: Path):
        renderer = HTMLRenderer(use_tailwind=False)
        files = renderer.render_to_directory(sample_pipeline, tmp_path)

        # Should create single HTML file
        assert len(files) == 1
        assert files[0].name == "index.html"
        assert files[0].exists()


class TestRendererWithEmptyPipeline:
    def test_json_empty(self):
        pipeline = Pipeline()
        renderer = JSONRenderer()
        output = renderer.render(pipeline)

        data = json.loads(output)
        assert data["inputs"] == []
        assert data["processes"] == []

    def test_markdown_empty(self):
        pipeline = Pipeline()
        renderer = MarkdownRenderer()
        output = renderer.render(pipeline)

        # Should still produce valid markdown
        assert "#" in output

    def test_html_empty(self):
        pipeline = Pipeline()
        renderer = HTMLRenderer(use_tailwind=False)
        output = renderer.render(pipeline)

        # Should still produce valid HTML (lowercase doctype is valid HTML5)
        assert "<!doctype html>" in output.lower()
