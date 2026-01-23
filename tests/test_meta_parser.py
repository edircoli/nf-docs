"""Tests for meta.yml parser."""

import tempfile
from pathlib import Path

import pytest

from nf_docs.meta_parser import (
    MetaInput,
    MetaOutput,
    ModuleMeta,
    SubworkflowMeta,
    ToolInfo,
    find_meta_yml,
    is_module_path,
    is_subworkflow_path,
    parse_meta_for_file,
    parse_module_meta,
    parse_subworkflow_meta,
)


class TestToolInfo:
    """Tests for ToolInfo dataclass."""

    def test_creation(self):
        tool = ToolInfo(name="fastqc", description="Quality control")
        assert tool.name == "fastqc"
        assert tool.description == "Quality control"

    def test_to_dict(self):
        tool = ToolInfo(
            name="fastqc",
            description="QC tool",
            homepage="https://example.com",
            licence=["GPL-2.0"],
            identifier="biotools:fastqc",
        )
        data = tool.to_dict()
        assert data["name"] == "fastqc"
        assert data["homepage"] == "https://example.com"
        assert data["licence"] == ["GPL-2.0"]
        assert data["identifier"] == "biotools:fastqc"


class TestMetaInput:
    """Tests for MetaInput dataclass."""

    def test_creation(self):
        inp = MetaInput(name="reads", type="file", description="Input FASTQ files")
        assert inp.name == "reads"
        assert inp.type == "file"
        assert inp.description == "Input FASTQ files"

    def test_to_dict(self):
        inp = MetaInput(
            name="reads",
            type="file",
            description="Input FASTQ files",
            pattern="*.fastq.gz",
        )
        data = inp.to_dict()
        assert data["name"] == "reads"
        assert data["pattern"] == "*.fastq.gz"


class TestMetaOutput:
    """Tests for MetaOutput dataclass."""

    def test_creation(self):
        out = MetaOutput(name="html", type="file", description="FastQC report")
        assert out.name == "html"
        assert out.type == "file"

    def test_to_dict(self):
        out = MetaOutput(
            name="html",
            type="file",
            description="FastQC report",
            pattern="*_fastqc.html",
        )
        data = out.to_dict()
        assert data["name"] == "html"
        assert data["pattern"] == "*_fastqc.html"


class TestModuleMeta:
    """Tests for ModuleMeta dataclass."""

    def test_creation(self):
        meta = ModuleMeta(
            name="fastqc",
            description="Run FastQC on sequenced reads",
            keywords=["quality control", "qc"],
        )
        assert meta.name == "fastqc"
        assert meta.description == "Run FastQC on sequenced reads"
        assert len(meta.keywords) == 2

    def test_to_dict(self):
        meta = ModuleMeta(
            name="fastqc",
            description="QC tool",
            keywords=["qc"],
            tools=[ToolInfo(name="fastqc", description="QC")],
            authors=["@user1"],
        )
        data = meta.to_dict()
        assert data["name"] == "fastqc"
        assert data["keywords"] == ["qc"]
        assert len(data["tools"]) == 1
        assert data["authors"] == ["@user1"]


class TestSubworkflowMeta:
    """Tests for SubworkflowMeta dataclass."""

    def test_creation(self):
        meta = SubworkflowMeta(
            name="bam_stats_samtools",
            description="Produces statistics from BAM files",
            components=["samtools/stats", "samtools/idxstats"],
        )
        assert meta.name == "bam_stats_samtools"
        assert len(meta.components) == 2

    def test_to_dict(self):
        meta = SubworkflowMeta(
            name="bam_stats",
            description="Stats",
            components=["samtools/stats"],
            authors=["@user1"],
        )
        data = meta.to_dict()
        assert data["name"] == "bam_stats"
        assert data["components"] == ["samtools/stats"]


class TestFindMetaYml:
    """Tests for find_meta_yml function."""

    def test_find_existing_meta_yml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            # Create a mock module structure
            module_dir = tmppath / "modules" / "nf-core" / "fastqc"
            module_dir.mkdir(parents=True)
            (module_dir / "main.nf").touch()
            (module_dir / "meta.yml").write_text("name: fastqc")

            result = find_meta_yml(module_dir / "main.nf")
            assert result is not None
            assert result.name == "meta.yml"

    def test_find_nonexistent_meta_yml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "main.nf").touch()

            result = find_meta_yml(tmppath / "main.nf")
            assert result is None


class TestPathHelpers:
    """Tests for is_module_path and is_subworkflow_path."""

    def test_is_module_path(self):
        workspace = Path("/pipeline")
        assert is_module_path(Path("/pipeline/modules/nf-core/fastqc/main.nf"), workspace)
        assert is_module_path(Path("/pipeline/modules/local/tool/main.nf"), workspace)
        assert not is_module_path(Path("/pipeline/workflows/main.nf"), workspace)

    def test_is_subworkflow_path(self):
        workspace = Path("/pipeline")
        assert is_subworkflow_path(
            Path("/pipeline/subworkflows/nf-core/bam_stats/main.nf"), workspace
        )
        assert is_subworkflow_path(Path("/pipeline/subworkflows/local/prep/main.nf"), workspace)
        assert not is_subworkflow_path(Path("/pipeline/modules/tool/main.nf"), workspace)


class TestParseModuleMeta:
    """Tests for parse_module_meta function."""

    def test_parse_simple_module(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write("""
name: fastqc
description: Run FastQC on sequenced reads
keywords:
  - quality control
  - qc
tools:
  - fastqc:
      description: QC tool
      homepage: https://example.com
      licence: ["GPL-2.0"]
input:
  - - meta:
        type: map
        description: Sample information
    - reads:
        type: file
        description: Input FASTQ files
output:
  html:
    - - meta:
          type: map
      - "*.html":
          type: file
          description: FastQC report
          pattern: "*_fastqc.html"
authors:
  - "@user1"
maintainers:
  - "@user2"
""")
            f.flush()
            result = parse_module_meta(Path(f.name))

        assert result is not None
        assert result.name == "fastqc"
        assert result.description == "Run FastQC on sequenced reads"
        assert "quality control" in result.keywords
        assert len(result.tools) == 1
        assert result.tools[0].name == "fastqc"
        assert result.tools[0].homepage == "https://example.com"
        assert len(result.inputs) == 2  # meta and reads
        assert len(result.outputs) == 1
        assert result.outputs[0].name == "html"
        assert result.authors == ["@user1"]
        assert result.maintainers == ["@user2"]

    def test_parse_invalid_yaml(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write("invalid: yaml: content: [")
            f.flush()
            result = parse_module_meta(Path(f.name))

        assert result is None

    def test_parse_missing_name(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write("description: No name field")
            f.flush()
            result = parse_module_meta(Path(f.name))

        assert result is None


class TestParseSubworkflowMeta:
    """Tests for parse_subworkflow_meta function."""

    def test_parse_simple_subworkflow(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write("""
name: bam_stats_samtools
description: Produces comprehensive statistics from BAM files
keywords:
  - statistics
  - bam
  - samtools
components:
  - samtools/stats
  - samtools/idxstats
  - samtools/flagstat
input:
  - ch_bam_bai:
      description: The input BAM and its index
  - ch_fasta:
      description: Reference genome fasta
output:
  - stats:
      description: Samtools stats output
  - flagstat:
      description: Samtools flagstat output
authors:
  - "@user1"
""")
            f.flush()
            result = parse_subworkflow_meta(Path(f.name))

        assert result is not None
        assert result.name == "bam_stats_samtools"
        assert "samtools/stats" in result.components
        assert len(result.inputs) == 2
        assert result.inputs[0].name == "ch_bam_bai"
        assert len(result.outputs) == 2
        assert result.outputs[0].name == "stats"

    def test_parse_with_modules_field(self):
        """Test parsing with 'modules' field instead of 'components'."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            f.write("""
name: test_subworkflow
description: Test subworkflow
keywords:
  - test
modules:
  - module1
  - module2
input:
  - ch_input:
      description: Input channel
output:
  - result:
      description: Output
authors:
  - "@user1"
""")
            f.flush()
            result = parse_subworkflow_meta(Path(f.name))

        assert result is not None
        assert result.components == ["module1", "module2"]


class TestParseMetaForFile:
    """Tests for parse_meta_for_file function."""

    def test_parse_module_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            module_dir = tmppath / "modules" / "nf-core" / "fastqc"
            module_dir.mkdir(parents=True)
            (module_dir / "main.nf").touch()
            (module_dir / "meta.yml").write_text("""
name: fastqc
description: QC tool
keywords:
  - qc
tools:
  - fastqc:
      description: FastQC
      licence: ["GPL-2.0"]
input: []
output: {}
authors:
  - "@user1"
""")

            result = parse_meta_for_file(module_dir / "main.nf", tmppath)
            assert result is not None
            assert isinstance(result, ModuleMeta)
            assert result.name == "fastqc"

    def test_parse_subworkflow_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            sw_dir = tmppath / "subworkflows" / "nf-core" / "bam_stats"
            sw_dir.mkdir(parents=True)
            (sw_dir / "main.nf").touch()
            (sw_dir / "meta.yml").write_text("""
name: bam_stats
description: Stats workflow
keywords:
  - stats
components:
  - samtools/stats
input:
  - ch_bam:
      description: Input
output:
  - stats:
      description: Output
authors:
  - "@user1"
""")

            result = parse_meta_for_file(sw_dir / "main.nf", tmppath)
            assert result is not None
            assert isinstance(result, SubworkflowMeta)
            assert result.name == "bam_stats"

    def test_no_meta_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            (tmppath / "main.nf").touch()

            result = parse_meta_for_file(tmppath / "main.nf", tmppath)
            assert result is None


class TestRealMetaFiles:
    """Tests using actual meta.yml files from the testing directory."""

    @pytest.fixture
    def testing_dir(self):
        """Get the testing directory path."""
        # Adjust path based on where tests are run from
        test_file = Path(__file__).parent.parent
        testing = test_file / "testing"
        if not testing.exists():
            pytest.skip("Testing directory not available")
        return testing

    def test_parse_rnavar_fastqc_meta(self, testing_dir):
        """Test parsing actual fastqc meta.yml from rnavar."""
        meta_path = testing_dir / "rnavar" / "modules" / "nf-core" / "fastqc" / "meta.yml"
        if not meta_path.exists():
            pytest.skip("FastQC meta.yml not found")

        result = parse_module_meta(meta_path)
        assert result is not None
        assert result.name == "fastqc"
        assert "quality control" in result.keywords or "qc" in result.keywords
        assert len(result.tools) >= 1
        assert result.tools[0].name == "fastqc"
        assert result.tools[0].homepage
        assert len(result.inputs) >= 1
        assert len(result.outputs) >= 1

    def test_parse_rnavar_bam_stats_meta(self, testing_dir):
        """Test parsing actual bam_stats_samtools meta.yml from rnavar."""
        meta_path = (
            testing_dir / "rnavar" / "subworkflows" / "nf-core" / "bam_stats_samtools" / "meta.yml"
        )
        if not meta_path.exists():
            pytest.skip("bam_stats_samtools meta.yml not found")

        result = parse_subworkflow_meta(meta_path)
        assert result is not None
        assert result.name == "bam_stats_samtools"
        assert len(result.components) >= 1
        assert any("samtools" in c for c in result.components)
        assert len(result.inputs) >= 1
        assert len(result.outputs) >= 1
