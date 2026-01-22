"""Tests for the pipeline extractor."""

from pathlib import Path

import pytest

from nf_docs.extractor import PipelineExtractor


class TestPipelineExtractor:
    def test_extract_from_sample_pipeline(self, sample_pipeline: Path):
        """Test extraction from a sample pipeline."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,  # Use regex-based extraction for tests
        )

        pipeline = extractor.extract()

        # Check metadata - schema title takes priority over config manifest name
        assert pipeline.metadata.name == "Test Pipeline"
        # Version comes from config since schema doesn't have it
        # (Nextflow not installed in test env, so version may not be available)

    def test_extract_inputs_from_schema(self, sample_pipeline: Path):
        """Test that schema inputs are extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # Check inputs from schema
        input_names = {inp.name for inp in pipeline.inputs}
        assert "input" in input_names
        assert "outdir" in input_names
        assert "genome" in input_names

    def test_extract_processes(self, sample_pipeline: Path):
        """Test that processes are extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # Check processes
        process_names = {p.name for p in pipeline.processes}
        assert "BWA_MEM" in process_names
        assert "FASTQC" in process_names

    def test_extract_process_docstring(self, sample_pipeline: Path):
        """Test that process docstrings are extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        bwa = pipeline.get_process_by_name("BWA_MEM")
        assert bwa is not None
        assert "Align reads" in bwa.docstring or "BWA MEM" in bwa.docstring

    def test_extract_workflows(self, sample_pipeline: Path):
        """Test that workflows are extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # Should have at least the ANALYSIS workflow and entry workflow
        workflow_names = {w.name for w in pipeline.workflows}
        assert "ANALYSIS" in workflow_names

    def test_extract_workflow_calls(self, sample_pipeline: Path):
        """Test that workflow calls are extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        analysis = pipeline.get_workflow_by_name("ANALYSIS")
        assert analysis is not None
        assert "FASTQC" in analysis.calls
        assert "BWA_MEM" in analysis.calls

    def test_extract_readme_description(self, sample_pipeline: Path):
        """Test that README description is extracted."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # Metadata description should come from schema, which takes priority
        # But if schema didn't have description, README would be used
        assert pipeline.metadata.description is not None

    def test_config_params_filtered(self, sample_pipeline: Path):
        """Test that config params not in schema are kept separate."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # max_cpus is in config but not in schema inputs
        config_param_names = {p.name for p in pipeline.config_params}
        input_names = {i.name for i in pipeline.inputs}

        # Config params should not duplicate schema inputs
        assert len(config_param_names & input_names) == 0


class TestProcessExtraction:
    def test_extract_process_inputs(self, sample_pipeline: Path):
        """Test extraction of process inputs."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        bwa = pipeline.get_process_by_name("BWA_MEM")
        assert bwa is not None

        # Should have inputs
        assert len(bwa.inputs) > 0

    def test_extract_process_outputs(self, sample_pipeline: Path):
        """Test extraction of process outputs."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        fastqc = pipeline.get_process_by_name("FASTQC")
        assert fastqc is not None

        # Should have outputs
        assert len(fastqc.outputs) > 0

    def test_extract_process_directives(self, sample_pipeline: Path):
        """Test extraction of process directives."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        bwa = pipeline.get_process_by_name("BWA_MEM")
        assert bwa is not None

        # Should have directives
        assert "container" in bwa.directives or "cpus" in bwa.directives


class TestWorkflowExtraction:
    def test_extract_workflow_inputs(self, sample_pipeline: Path):
        """Test extraction of workflow inputs (take)."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        analysis = pipeline.get_workflow_by_name("ANALYSIS")
        assert analysis is not None

        # Should have inputs from take block
        assert len(analysis.inputs) > 0

    def test_extract_workflow_outputs(self, sample_pipeline: Path):
        """Test extraction of workflow outputs (emit)."""
        extractor = PipelineExtractor(
            workspace_path=sample_pipeline,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        analysis = pipeline.get_workflow_by_name("ANALYSIS")
        assert analysis is not None

        # Should have outputs from emit block
        assert len(analysis.outputs) > 0


class TestEmptyPipeline:
    def test_empty_directory(self, tmp_path: Path):
        """Test extraction from an empty directory."""
        extractor = PipelineExtractor(
            workspace_path=tmp_path,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        # Should return empty pipeline with directory name
        assert pipeline.metadata.name == tmp_path.name
        assert len(pipeline.processes) == 0
        assert len(pipeline.workflows) == 0

    def test_minimal_pipeline(self, tmp_path: Path):
        """Test extraction from a minimal pipeline."""
        # Create just a main.nf
        main_nf = tmp_path / "main.nf"
        main_nf.write_text("""
process HELLO {
    output:
    stdout

    script:
    \"\"\"
    echo "Hello World"
    \"\"\"
}

workflow {
    HELLO()
}
""")

        extractor = PipelineExtractor(
            workspace_path=tmp_path,
            use_lsp=False,
        )

        pipeline = extractor.extract()

        assert len(pipeline.processes) == 1
        assert pipeline.processes[0].name == "HELLO"
