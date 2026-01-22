"""
HTML renderer for nf-docs.

Outputs pipeline documentation as a self-contained static HTML site.
"""

from pathlib import Path

import markdown
from jinja2 import Environment, PackageLoader
from markupsafe import Markup

from nf_docs.models import Pipeline
from nf_docs.renderers.base import BaseRenderer


def md_to_html(text: str | None) -> Markup:
    """Convert markdown text to HTML, safe for Jinja templates."""
    if not text:
        return Markup("")
    # Convert markdown to HTML, stripping the outer <p> tags for inline use
    html = markdown.markdown(text, extensions=["tables", "fenced_code"])
    return Markup(html)


class HTMLRenderer(BaseRenderer):
    """
    Render pipeline documentation as a self-contained HTML page.

    This creates a single-page application with navigation that works
    without any server or build step. Optionally processes with Tailwind
    CSS for tree-shaken, minified styling.
    """

    def __init__(self, title: str | None = None, use_tailwind: bool = True):
        """
        Initialize the HTML renderer.

        Args:
            title: Optional custom title for the documentation
            use_tailwind: Whether to process with Tailwind CSS (default: True)
        """
        super().__init__(title)
        self.use_tailwind = use_tailwind
        self.env = Environment(loader=PackageLoader("nf_docs", "templates"))
        # Register markdown filter
        self.env.filters["markdown"] = md_to_html
        self.template = self.env.get_template("html.html")

    def render(self, pipeline: Pipeline) -> str:
        """
        Render the pipeline to HTML.

        Args:
            pipeline: The Pipeline model to render

        Returns:
            HTML string
        """
        title = self.get_title(pipeline)
        input_groups = pipeline.get_input_groups()

        html_content = self.template.render(
            title=title,
            pipeline=pipeline,
            input_groups=input_groups,
        )

        # Process with Tailwind if enabled
        if self.use_tailwind:
            try:
                from nf_docs.tailwind import process_html_with_tailwind

                html_content = process_html_with_tailwind(html_content)
            except Exception:
                # If Tailwind fails (not installed, etc.), fall back to CDN
                html_content = self._inject_tailwind_cdn(html_content)

        return html_content

    def _inject_tailwind_cdn(self, html_content: str) -> str:
        """Inject Tailwind CSS CDN as fallback."""
        cdn_script = """<script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              primary: {
                DEFAULT: "#0DC09D",
                light: "#E6F9F5",
                dark: "#0A9A7D",
              },
            },
          },
        },
      };
    </script>"""
        return html_content.replace("</head>", f"{cdn_script}\n</head>")

    def render_to_directory(self, pipeline: Pipeline, output_dir: str | Path) -> list[Path]:
        """
        Render the pipeline to a directory.

        For HTML, this creates a single index.html file.

        Args:
            pipeline: The Pipeline model to render
            output_dir: Output directory path

        Returns:
            List containing the single output file path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        filename = output_path / "index.html"
        self.render_to_file(pipeline, filename)
        return [filename]
