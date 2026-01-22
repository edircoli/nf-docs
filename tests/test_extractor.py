"""Tests for the pipeline extractor."""

from pathlib import Path
from unittest.mock import patch

from nf_docs.extractor import PipelineExtractor


class TestPipelineExtractor:
    def test_extract_schema_inputs(self, sample_pipeline: Path):
        """Test that schema inputs are extracted."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=sample_pipeline)
            pipeline = extractor.extract()

            # Check inputs from schema
            input_names = {inp.name for inp in pipeline.inputs}
            assert "input" in input_names
            assert "outdir" in input_names
            assert "genome" in input_names

    def test_extract_metadata_from_schema(self, sample_pipeline: Path):
        """Test that metadata is extracted from schema."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=sample_pipeline)
            pipeline = extractor.extract()

            # Schema title takes priority
            assert pipeline.metadata.name == "Test Pipeline"

    def test_extract_readme_description(self, sample_pipeline: Path):
        """Test that README description is extracted when schema has none."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=sample_pipeline)
            pipeline = extractor.extract()

            # Schema description takes priority
            assert pipeline.metadata.description is not None


class TestReadmeExtraction:
    def test_extract_simple_readme(self, tmp_path: Path):
        """Test extraction from a simple README."""
        readme = tmp_path / "README.md"
        readme.write_text("# My Pipeline\n\nThis is a test pipeline.\n")

        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=tmp_path)
            pipeline = extractor.extract()

            assert "test pipeline" in pipeline.metadata.description.lower()

    def test_extract_readme_with_badges(self, tmp_path: Path):
        """Test extraction skips badge lines."""
        readme = tmp_path / "README.md"
        readme.write_text(
            "# My Pipeline\n\n"
            "[![Build Status](https://example.com/badge.svg)](https://example.com)\n"
            "![Coverage](https://example.com/coverage.svg)\n\n"
            "This is the actual description.\n"
        )

        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=tmp_path)
            pipeline = extractor.extract()

            assert "actual description" in pipeline.metadata.description.lower()
            assert "badge" not in pipeline.metadata.description.lower()

    def test_no_readme(self, tmp_path: Path):
        """Test extraction when no README exists."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=tmp_path)
            pipeline = extractor.extract()

            # Should use directory name as fallback
            assert pipeline.metadata.name == tmp_path.name


class TestMetadataMerging:
    def test_schema_takes_priority(self, sample_pipeline: Path):
        """Test that schema metadata takes priority over config."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=sample_pipeline)
            pipeline = extractor.extract()

            # Schema has "Test Pipeline" as title
            assert pipeline.metadata.name == "Test Pipeline"


class TestInputGroups:
    def test_inputs_grouped_correctly(self, sample_pipeline: Path):
        """Test that inputs are grouped by their schema group."""
        with patch.object(PipelineExtractor, "_extract_from_lsp"):
            extractor = PipelineExtractor(workspace_path=sample_pipeline)
            pipeline = extractor.extract()

            groups = pipeline.get_input_groups()
            assert "Input/output options" in groups
            assert "Reference genome options" in groups


class TestSymbolNameParsing:
    """Test parsing of Nextflow LSP symbol names."""

    def test_parse_process_name(self, tmp_path: Path):
        """Test parsing process symbol names."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("process FASTQC")
        assert symbol_type == "process"
        assert name == "FASTQC"

    def test_parse_workflow_name(self, tmp_path: Path):
        """Test parsing workflow symbol names."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("workflow PIPELINE")
        assert symbol_type == "workflow"
        assert name == "PIPELINE"

    def test_parse_entry_workflow(self, tmp_path: Path):
        """Test parsing entry workflow symbol name."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("workflow <entry>")
        assert symbol_type == "workflow"
        assert name == ""

    def test_parse_function_name(self, tmp_path: Path):
        """Test parsing function symbol names."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("function myHelper")
        assert symbol_type == "function"
        assert name == "myHelper"

    def test_parse_enum_name(self, tmp_path: Path):
        """Test parsing enum symbol names."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("enum MyEnum")
        assert symbol_type == "enum"
        assert name == "MyEnum"

    def test_parse_unknown_name(self, tmp_path: Path):
        """Test parsing names without known prefix."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("something_else")
        assert symbol_type == "unknown"
        assert name == "something_else"

    def test_parse_empty_name(self, tmp_path: Path):
        """Test parsing empty name."""
        extractor = PipelineExtractor(workspace_path=tmp_path)

        symbol_type, name = extractor._parse_symbol_name("")
        assert symbol_type == "unknown"
        assert name == ""
