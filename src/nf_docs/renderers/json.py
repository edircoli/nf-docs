"""
JSON renderer for nf-docs.

Outputs pipeline documentation as structured JSON data.
"""

import json
from pathlib import Path

from nf_docs.models import Pipeline
from nf_docs.renderers.base import BaseRenderer


class JSONRenderer(BaseRenderer):
    """
    Render pipeline documentation as JSON.

    This format is machine-readable and suitable for:
    - Integration with other tools
    - Custom post-processing
    - API responses
    """

    def __init__(self, title: str | None = None, indent: int = 2):
        """
        Initialize the JSON renderer.

        Args:
            title: Optional custom title (included in output)
            indent: JSON indentation level (default: 2)
        """
        super().__init__(title)
        self.indent = indent

    def render(self, pipeline: Pipeline) -> str:
        """
        Render the pipeline to JSON.

        Args:
            pipeline: The Pipeline model to render

        Returns:
            JSON string
        """
        data = pipeline.to_dict()

        # Add custom title if provided
        if self.title:
            data["pipeline"]["name"] = self.title

        return json.dumps(data, indent=self.indent, ensure_ascii=False)

    def render_to_directory(self, pipeline: Pipeline, output_dir: str | Path) -> list[Path]:
        """
        Render the pipeline to a directory.

        For JSON, this creates a single file.

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
        filename = output_path / f"{clean_name}-api.json"

        self.render_to_file(pipeline, filename)
        return [filename]
