#!/usr/bin/env python3
"""Generate screenshots of nf-docs HTML output for the README.

This script uses Playwright to capture screenshots of different sections
of the generated HTML documentation, then combines them into an animated GIF.

Requirements:
    pip install playwright pillow
    playwright install chromium

Usage:
    python scripts/generate_readme_screenshots.py

    # Use a specific HTML file
    python scripts/generate_readme_screenshots.py --html examples/html/sarek/index.html

    # Custom output path
    python scripts/generate_readme_screenshots.py --output docs/demo.gif
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# Check for required dependencies
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: playwright is required. Install with: pip install playwright")
    print("Then run: playwright install chromium")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: pillow is required. Install with: pip install pillow")
    sys.exit(1)


def capture_screenshots(
    html_path: Path,
    output_dir: Path,
    width: int = 1280,
    height: int = 800,
) -> list[Path]:
    """Capture screenshots of different sections of the HTML documentation.

    Args:
        html_path: Path to the HTML file to screenshot
        output_dir: Directory to save screenshots
        width: Browser viewport width
        height: Browser viewport height

    Returns:
        List of paths to the captured screenshots
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    screenshots: list[Path] = []

    # Sections to capture - (section_id, filename, description)
    # section_id matches the data-section attribute on nav links
    sections = [
        ("overview", "01_overview.png", "Overview"),
        ("inputs", "02_inputs.png", "Inputs"),
        ("workflows", "03_workflows.png", "Workflows"),
        ("processes", "04_processes.png", "Processes"),
        ("functions", "05_functions.png", "Functions"),
    ]

    file_url = f"file://{html_path.absolute()}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})

        # Load the page once
        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        for section_id, filename, description in sections:
            print(f"  Capturing {description}...")

            # Click the navigation link to switch sections
            nav_link = page.locator(f'.nav-link[data-section="{section_id}"]')
            if nav_link.count() > 0:
                nav_link.click()
                # Wait for section to become visible
                time.sleep(0.3)

            # Scroll to top of content area
            page.evaluate("window.scrollTo({ top: 0 })")
            time.sleep(0.1)

            screenshot_path = output_dir / filename
            page.screenshot(path=str(screenshot_path))
            screenshots.append(screenshot_path)

        browser.close()

    return screenshots


def create_gif(
    screenshots: list[Path],
    output_path: Path,
    duration: int = 2000,
    loop: int = 0,
) -> None:
    """Create an animated GIF from screenshots.

    Args:
        screenshots: List of paths to screenshot images
        output_path: Path for the output GIF
        duration: Duration of each frame in milliseconds
        loop: Number of loops (0 = infinite)
    """
    if not screenshots:
        print("Error: No screenshots to combine")
        return

    images = [Image.open(path) for path in screenshots]

    # Save as animated GIF
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=loop,
        optimize=True,
    )

    # Calculate file size
    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"  Created GIF: {output_path} ({size_mb:.2f} MB)")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate README screenshots from nf-docs HTML output"
    )
    parser.add_argument(
        "--html",
        type=Path,
        default=Path("examples/html/sarek/index.html"),
        help="Path to the HTML file to screenshot (default: examples/html/sarek/index.html)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/images/demo.gif"),
        help="Output path for the GIF (default: docs/images/demo.gif)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1280,
        help="Browser viewport width (default: 1280)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=800,
        help="Browser viewport height (default: 800)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=2000,
        help="Duration of each frame in milliseconds (default: 2000)",
    )
    parser.add_argument(
        "--keep-screenshots",
        action="store_true",
        help="Keep individual screenshot files",
    )

    args = parser.parse_args()

    # Validate input file exists
    if not args.html.exists():
        print(f"Error: HTML file not found: {args.html}")
        print("\nGenerate it first with:")
        print(f"  nf-docs generate testing/sarek -f html -o {args.html.parent}/")
        sys.exit(1)

    print(f"Generating screenshots from: {args.html}")

    # Create temporary directory for screenshots
    screenshot_dir = args.output.parent / ".screenshots"

    # Capture screenshots
    print("Capturing screenshots...")
    screenshots = capture_screenshots(
        html_path=args.html,
        output_dir=screenshot_dir,
        width=args.width,
        height=args.height,
    )

    # Create GIF
    print("Creating animated GIF...")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    create_gif(screenshots, args.output, duration=args.duration)

    # Clean up screenshots unless --keep-screenshots
    if not args.keep_screenshots:
        for screenshot in screenshots:
            screenshot.unlink()
        screenshot_dir.rmdir()
        print("  Cleaned up temporary screenshots")

    print(f"\nDone! GIF saved to: {args.output}")
    print("\nTo use in README.md:")
    print(f"  ![nf-docs demo]({args.output})")


if __name__ == "__main__":
    main()
