"""
YAML renderer for nf-docs.

Outputs pipeline documentation as structured YAML data.
"""

from pathlib import Path

import yaml

from nf_docs.models import Pipeline
from nf_docs.renderers.base import BaseRenderer


class YAMLRenderer(BaseRenderer):
    """
    Render pipeline documentation as YAML.

    This format is human-readable and suitable for:
    - Configuration files
    - Manual editing
    - Integration with YAML-based tools
    """

    def __init__(self, title: str | None = None, default_flow_style: bool = False):
        """
        Initialize the YAML renderer.

        Args:
            title: Optional custom title (included in output)
            default_flow_style: Use flow style for sequences/mappings
        """
        super().__init__(title)
        self.default_flow_style = default_flow_style

    def render(self, pipeline: Pipeline) -> str:
        """
        Render the pipeline to YAML.

        Args:
            pipeline: The Pipeline model to render

        Returns:
            YAML string
        """
        data = pipeline.to_dict()

        # Add custom title if provided
        if self.title:
            data["pipeline"]["name"] = self.title

        return yaml.dump(
            data,
            default_flow_style=self.default_flow_style,
            allow_unicode=True,
            sort_keys=False,
            width=100,
        )

    def render_to_directory(self, pipeline: Pipeline, output_dir: str | Path) -> list[Path]:
        """
        Render the pipeline to a directory.

        For YAML, this creates a single file.

        Args:
            pipeline: The Pipeline model to render
            output_dir: Output directory path

        Returns:
            List containing the single output file path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Determine filename from pipeline name
        name = pipeline.metadata.name or "pipeline"
        # Clean name for filename
        clean_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in name)
        filename = output_path / f"{clean_name}-api.yaml"

        self.render_to_file(pipeline, filename)
        return [filename]
