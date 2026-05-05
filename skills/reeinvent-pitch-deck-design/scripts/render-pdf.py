#!/usr/bin/env python3
"""
render-pdf.py - Render a Reeinvent HTML deck to PDF with vector quality.

Why this exists
---------------
The PPTX -> PDF path (LibreOffice / PowerPoint export) downsamples and
JPEG-compresses every embedded PNG, so logos, gradients, and bullet
markers degrade visibly. The HTML deck uses SVGs - vectors that stay
infinite-resolution if the renderer preserves them. Headless Chrome
preserves them. This script wraps that:

  - Injects the slide-canvas page size (default 1280 x 720 px) so Chrome
    prints at the deck's aspect ratio instead of US Letter portrait.
  - Renders the HTML in place so relative SVG paths resolve.
  - Writes a vector PDF beside the input HTML.

Usage
-----
    python scripts/render-pdf.py INPUT.html [OUTPUT.pdf]
    python scripts/render-pdf.py INPUT.html --width 1280 --height 720

If OUTPUT.pdf is omitted, the output goes next to the input with the
same stem and a `.pdf` extension.

What it does NOT compress
-------------------------
SVG references in <img>, <object>, and CSS background-image stay vector.
CSS gradients stay vector. Roboto from Google Fonts stays embedded.
The only raster content in the output is whatever raster was already
in the HTML (e.g., photographs).

Requirements
------------
- Google Chrome installed at one of the standard macOS / Linux paths,
  or a Chromium binary on PATH.
- The HTML must use SVG brand marks (per DESIGN.md asset routing rule).
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
]


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if Path(path).is_file():
            return path
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    raise FileNotFoundError(
        "no Chrome / Chromium binary found. Install Chrome or pass a binary "
        "path via the CHROME env var."
    )


def inject_page_size(html_path: Path, width: int, height: int) -> Path:
    """Return a path to a sibling HTML file with @page size injected.

    The new file lives in the same directory as the input so relative
    asset paths (Reeinvent-Pitch-Deck-Designer/skills/.../*.svg) resolve
    correctly when Chrome loads it.
    """
    raw = html_path.read_text(encoding="utf-8")
    page_rule = f"@page {{ size: {width}px {height}px; margin: 0; }}\n"

    if "@page" in raw:
        # The HTML already declares an @page; trust the author and don't
        # double-inject. The user can still override via the --width and
        # --height args by editing their HTML.
        return html_path

    if "@media print" in raw:
        # Inject the @page rule just before the print block so it scopes
        # to print/PDF only.
        modified = raw.replace("@media print {", page_rule + "@media print {", 1)
    else:
        # No print stylesheet at all. Append a minimal one before </style>.
        snippet = (
            page_rule
            + "@media print {\n"
            + "  body { background: #fff; padding: 0; gap: 0; }\n"
            + "  .slide { page-break-after: always; box-shadow: none; "
            + "border-radius: 0; margin: 0; }\n"
            + "}\n"
        )
        modified = re.sub(r"</style>", snippet + "</style>", raw, count=1)
        if modified == raw:
            # No <style> block found; wrap one in <head>.
            modified = re.sub(
                r"</head>",
                f"<style>\n{snippet}</style>\n</head>",
                raw,
                count=1,
            )

    prepared = html_path.with_name("." + html_path.stem + ".prepared.html")
    prepared.write_text(modified, encoding="utf-8")
    return prepared


def render(input_html: Path, output_pdf: Path, width: int, height: int) -> None:
    chrome = os.environ.get("CHROME") or find_chrome()
    prepared = inject_page_size(input_html, width, height)
    cleanup = prepared != input_html

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={output_pdf}",
        f"file://{prepared.resolve()}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise RuntimeError(
                f"Chrome failed (exit {result.returncode}): {result.stderr.strip()}"
            )
    finally:
        if cleanup and prepared.exists():
            prepared.unlink()

    if not output_pdf.is_file() or output_pdf.stat().st_size == 0:
        raise RuntimeError(f"output PDF was not produced: {output_pdf}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Render a Reeinvent HTML deck to a vector PDF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", type=Path, help="path to the HTML deck")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="output PDF path (default: same stem as input, .pdf)",
    )
    parser.add_argument(
        "--width", type=int, default=1280,
        help="slide width in CSS pixels (default 1280)",
    )
    parser.add_argument(
        "--height", type=int, default=720,
        help="slide height in CSS pixels (default 720)",
    )
    args = parser.parse_args(argv[1:])

    if not args.input.is_file():
        print(f"render-pdf: input not found: {args.input}", file=sys.stderr)
        return 1

    output = args.output or args.input.with_suffix(".pdf")
    try:
        render(args.input, output, args.width, args.height)
    except Exception as exc:
        print(f"render-pdf: {exc}", file=sys.stderr)
        return 1

    size_kb = output.stat().st_size // 1024
    print(f"render-pdf: wrote {output} ({size_kb} KB, vector-preserving)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
