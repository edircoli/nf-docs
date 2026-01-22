"""Tests for the caching system."""

import json
from pathlib import Path

import pytest

from nf_docs.cache import PipelineCache, get_xdg_cache_home
from nf_docs.models import (
    Pipeline,
    PipelineInput,
    PipelineMetadata,
    Process,
    ProcessInput,
    Workflow,
)


class TestGetXdgCacheHome:
    """Tests for get_xdg_cache_home function."""

    def test_default_cache_home(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test default cache home when XDG_CACHE_HOME is not set."""
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)
        result = get_xdg_cache_home()
        assert result == Path.home() / ".cache"

    def test_custom_cache_home(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        """Test custom cache home from XDG_CACHE_HOME."""
        custom_cache = tmp_path / "custom_cache"
        monkeypatch.setenv("XDG_CACHE_HOME", str(custom_cache))
        result = get_xdg_cache_home()
        assert result == custom_cache


class TestPipelineCache:
    """Tests for PipelineCache class."""

    @pytest.fixture
    def cache(self, tmp_path: Path) -> PipelineCache:
        """Create a cache with temporary directory."""
        cache_dir = tmp_path / "cache"
        return PipelineCache(cache_dir=cache_dir)

    @pytest.fixture
    def sample_pipeline_dir(self, tmp_path: Path) -> Path:
        """Create a sample pipeline directory."""
        pipeline_dir = tmp_path / "pipeline"
        pipeline_dir.mkdir()

        # Create some pipeline files
        (pipeline_dir / "main.nf").write_text("process FOO { script: 'echo hi' }")
        (pipeline_dir / "nextflow.config").write_text("params.input = null")
        (pipeline_dir / "nextflow_schema.json").write_text('{"$schema": "test"}')
        (pipeline_dir / "README.md").write_text("# Test Pipeline")

        return pipeline_dir

    @pytest.fixture
    def sample_pipeline(self) -> Pipeline:
        """Create a sample Pipeline model."""
        return Pipeline(
            metadata=PipelineMetadata(
                name="test-pipeline",
                description="A test pipeline",
                version="1.0.0",
            ),
            inputs=[
                PipelineInput(
                    name="input",
                    type="string",
                    description="Input file",
                    required=True,
                    group="Input/output options",
                ),
            ],
            processes=[
                Process(
                    name="FOO",
                    docstring="A test process",
                    file="main.nf",
                    line=1,
                    inputs=[ProcessInput(name="reads", type="path")],
                ),
            ],
            workflows=[
                Workflow(
                    name="main",
                    docstring="Main workflow",
                    is_entry=True,
                ),
            ],
        )

    def test_cache_miss_no_file(
        self, cache: PipelineCache, sample_pipeline_dir: Path
    ) -> None:
        """Test cache miss when no cache file exists."""
        result = cache.get(sample_pipeline_dir)
        assert result is None

    def test_cache_set_and_get(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test setting and getting from cache."""
        # Set the cache
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Get from cache
        result = cache.get(sample_pipeline_dir)
        assert result is not None
        assert result.metadata.name == "test-pipeline"
        assert result.metadata.version == "1.0.0"
        assert len(result.inputs) == 1
        assert result.inputs[0].name == "input"
        assert len(result.processes) == 1
        assert result.processes[0].name == "FOO"
        assert len(result.workflows) == 1
        assert result.workflows[0].name == "main"

    def test_cache_invalidation_on_file_change(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test cache invalidation when a file changes."""
        # Set the cache
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Verify cache hit
        result = cache.get(sample_pipeline_dir)
        assert result is not None

        # Modify a file
        (sample_pipeline_dir / "main.nf").write_text("process BAR { script: 'echo bye' }")

        # Cache should miss due to content change
        result = cache.get(sample_pipeline_dir)
        assert result is None

    def test_cache_invalidation_on_new_file(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test cache invalidation when a new .nf file is added."""
        # Set the cache
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Verify cache hit
        result = cache.get(sample_pipeline_dir)
        assert result is not None

        # Add a new .nf file
        (sample_pipeline_dir / "modules.nf").write_text("process NEW { script: 'echo new' }")

        # Cache should miss due to new file
        result = cache.get(sample_pipeline_dir)
        assert result is None

    def test_cache_clear_specific_workspace(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test clearing cache for a specific workspace."""
        # Set the cache
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Verify cache hit
        assert cache.get(sample_pipeline_dir) is not None

        # Clear the cache
        cleared = cache.clear(sample_pipeline_dir)
        assert cleared == 1

        # Cache should miss
        assert cache.get(sample_pipeline_dir) is None

    def test_cache_clear_all(
        self,
        cache: PipelineCache,
        tmp_path: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test clearing all caches."""
        # Create two pipeline directories
        pipeline1 = tmp_path / "pipeline1"
        pipeline1.mkdir()
        (pipeline1 / "main.nf").write_text("process A {}")

        pipeline2 = tmp_path / "pipeline2"
        pipeline2.mkdir()
        (pipeline2 / "main.nf").write_text("process B {}")

        # Cache both
        cache.set(pipeline1, sample_pipeline)
        cache.set(pipeline2, sample_pipeline)

        # Verify both cached
        assert cache.get(pipeline1) is not None
        assert cache.get(pipeline2) is not None

        # Clear all
        cleared = cache.clear()
        assert cleared == 2

        # Both should miss
        assert cache.get(pipeline1) is None
        assert cache.get(pipeline2) is None

    def test_old_cache_cleanup(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test that old cache files are cleaned up when a new one is created."""
        # Set the cache
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Count cache files
        cache_files = list(cache.cache_dir.glob("*.json"))
        assert len(cache_files) == 1

        # Modify a file and set cache again
        (sample_pipeline_dir / "main.nf").write_text("process CHANGED {}")
        cache.set(sample_pipeline_dir, sample_pipeline)

        # Should still have only one cache file (old one cleaned up)
        cache_files = list(cache.cache_dir.glob("*.json"))
        assert len(cache_files) == 1

    def test_deserialize_all_fields(self, cache: PipelineCache) -> None:
        """Test that all Pipeline fields are correctly serialized and deserialized."""
        pipeline = Pipeline(
            metadata=PipelineMetadata(
                name="test",
                description="desc",
                version="1.0",
                homepage="https://example.com",
                repository="https://github.com/test",
                authors=["Author 1", "Author 2"],
                license="MIT",
            ),
            inputs=[
                PipelineInput(
                    name="input",
                    type="string",
                    description="Input desc",
                    help_text="Help text",
                    required=True,
                    default="default.txt",
                    format="file-path",
                    pattern="*.txt",
                    enum=["a", "b"],
                    group="Input options",
                    hidden=False,
                    fa_icon="fas fa-file",
                ),
            ],
        )

        # Serialize and deserialize
        data = cache._serialize_pipeline(pipeline)
        result = cache._deserialize_pipeline(data)

        assert result.metadata.name == "test"
        assert result.metadata.authors == ["Author 1", "Author 2"]
        assert result.inputs[0].help_text == "Help text"
        assert result.inputs[0].enum == ["a", "b"]
        assert result.inputs[0].fa_icon == "fas fa-file"

    def test_cache_file_format(
        self,
        cache: PipelineCache,
        sample_pipeline_dir: Path,
        sample_pipeline: Pipeline,
    ) -> None:
        """Test that cache files are valid JSON."""
        cache.set(sample_pipeline_dir, sample_pipeline)

        cache_files = list(cache.cache_dir.glob("*.json"))
        assert len(cache_files) == 1

        # Should be valid JSON
        content = cache_files[0].read_text()
        data = json.loads(content)
        assert "pipeline" in data
        assert data["pipeline"]["name"] == "test-pipeline"
