"""
Tailwind CSS utility for rendering Jinja templates with tree-shaken CSS.

This module provides functionality to:
1. Render Jinja templates to HTML
2. Process the HTML with Tailwind CSS CLI to generate tree-shaken CSS
3. Inject the minified CSS into the final HTML as a self-contained file
"""

import re
import subprocess
import tempfile
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, PackageLoader


def render_with_tailwind(
    template_path: str | Path,
    context: dict,
    output_path: str | Path | None = None,
    tailwind_config: str | Path | None = None,
    tailwind_input_css: str | Path | None = None,
    minify: bool = True,
) -> str:
    """
    Render a Jinja template and process it with Tailwind CSS.

    Args:
        template_path: Path to the Jinja template file
        context: Dictionary of context variables for the template
        output_path: Optional path to write the output HTML file
        tailwind_config: Optional path to tailwind.config.js
        tailwind_input_css: Optional path to input CSS file with @tailwind directives
        minify: Whether to minify the CSS output (default: True)

    Returns:
        The rendered HTML string with inlined Tailwind CSS
    """
    template_path = Path(template_path)

    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)

    # Render the template
    rendered_html = template.render(**context)

    # Process with Tailwind
    final_html = process_html_with_tailwind(
        html_content=rendered_html,
        tailwind_config=tailwind_config,
        tailwind_input_css=tailwind_input_css,
        minify=minify,
    )

    # Write output if path provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(final_html, encoding="utf-8")

    return final_html


def render_package_template_with_tailwind(
    package: str,
    template_name: str,
    context: dict,
    output_path: str | Path | None = None,
    tailwind_config: str | Path | None = None,
    tailwind_input_css: str | Path | None = None,
    minify: bool = True,
) -> str:
    """
    Render a Jinja template from a Python package and process with Tailwind CSS.

    Args:
        package: Python package name containing the templates
        template_name: Name of the template file
        context: Dictionary of context variables for the template
        output_path: Optional path to write the output HTML file
        tailwind_config: Optional path to tailwind.config.js
        tailwind_input_css: Optional path to input CSS file with @tailwind directives
        minify: Whether to minify the CSS output (default: True)

    Returns:
        The rendered HTML string with inlined Tailwind CSS
    """
    # Set up Jinja environment with package loader
    env = Environment(loader=PackageLoader(package, "templates"))
    template = env.get_template(template_name)

    # Render the template
    rendered_html = template.render(**context)

    # Process with Tailwind
    final_html = process_html_with_tailwind(
        html_content=rendered_html,
        tailwind_config=tailwind_config,
        tailwind_input_css=tailwind_input_css,
        minify=minify,
    )

    # Write output if path provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(final_html, encoding="utf-8")

    return final_html


def process_html_with_tailwind(
    html_content: str,
    tailwind_config: str | Path | None = None,
    tailwind_input_css: str | Path | None = None,
    minify: bool = True,
) -> str:
    """
    Process HTML content with Tailwind CSS to generate tree-shaken CSS.

    Args:
        html_content: The HTML content to process
        tailwind_config: Optional path to tailwind.config.js
        tailwind_input_css: Optional path to input CSS file
        minify: Whether to minify the CSS output

    Returns:
        HTML with Tailwind CSS inlined in a <style> tag
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Write HTML to temp file for Tailwind to scan
        html_file = tmpdir / "input.html"
        html_file.write_text(html_content, encoding="utf-8")

        # Create input CSS if not provided
        if tailwind_input_css:
            input_css = Path(tailwind_input_css).read_text(encoding="utf-8")
        else:
            input_css = "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n"

        input_css_file = tmpdir / "input.css"
        input_css_file.write_text(input_css, encoding="utf-8")

        # Create tailwind config if not provided
        if tailwind_config:
            config_content = Path(tailwind_config).read_text(encoding="utf-8")
        else:
            config_content = f"""/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  content: ["{html_file.as_posix()}"],
  theme: {{
    extend: {{}},
  }},
  plugins: [],
}}
"""
        config_file = tmpdir / "tailwind.config.js"
        config_file.write_text(config_content, encoding="utf-8")

        # Output CSS file
        output_css_file = tmpdir / "output.css"

        # Build Tailwind command
        cmd = [
            "tailwindcss",
            "-i",
            str(input_css_file),
            "-o",
            str(output_css_file),
            "-c",
            str(config_file),
        ]

        if minify:
            cmd.append("--minify")

        # Run Tailwind CLI
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=tmpdir,
        )

        if result.returncode != 0:
            raise RuntimeError(f"Tailwind CSS failed: {result.stderr}")

        # Read generated CSS
        css_content = output_css_file.read_text(encoding="utf-8")

    # Inject CSS into HTML
    return inject_css_into_html(html_content, css_content)


def inject_css_into_html(html_content: str, css_content: str) -> str:
    """
    Inject CSS content into an HTML document.

    Replaces any existing <style> tags or adds a new one in <head>.

    Args:
        html_content: The HTML content
        css_content: The CSS to inject

    Returns:
        HTML with CSS injected in a <style> tag
    """
    style_tag = f"<style>\n{css_content}\n</style>"

    # Check if there's already a <style> tag to replace
    if "<style>" in html_content:
        # Replace existing style tag(s)
        html_content = re.sub(
            r"<style>.*?</style>",
            style_tag,
            html_content,
            flags=re.DOTALL,
        )
    elif "</head>" in html_content:
        # Insert before </head>
        html_content = html_content.replace("</head>", f"{style_tag}\n</head>")
    else:
        # Prepend to document
        html_content = f"{style_tag}\n{html_content}"

    return html_content


def main() -> None:
    """CLI entry point for the Tailwind utility."""
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(
        description="Render Jinja templates with Tailwind CSS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Render a template with context from JSON file
  nf-docs-tailwind template.html -c context.json -o output.html

  # Render with inline context
  nf-docs-tailwind template.html --context '{"title": "My Page"}' -o output.html

  # Render without minification
  nf-docs-tailwind template.html -c context.json -o output.html --no-minify
        """,
    )

    parser.add_argument("template", type=Path, help="Path to the Jinja template file")
    parser.add_argument(
        "-c",
        "--context",
        type=str,
        help="Context data as JSON string or path to JSON file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output file path (defaults to stdout)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to tailwind.config.js",
    )
    parser.add_argument(
        "--input-css",
        type=Path,
        help="Path to input CSS file with @tailwind directives",
    )
    parser.add_argument(
        "--no-minify",
        action="store_true",
        help="Disable CSS minification",
    )

    args = parser.parse_args()

    # Parse context
    context = {}
    if args.context:
        if Path(args.context).exists():
            context = json.loads(Path(args.context).read_text())
        else:
            context = json.loads(args.context)

    # Render
    try:
        result = render_with_tailwind(
            template_path=args.template,
            context=context,
            output_path=args.output,
            tailwind_config=args.config,
            tailwind_input_css=args.input_css,
            minify=not args.no_minify,
        )

        if not args.output:
            print(result)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
