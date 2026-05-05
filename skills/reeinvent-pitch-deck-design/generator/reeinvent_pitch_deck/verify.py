"""Open a generated .pptx and run brand pre-flight checks. Each check raises
if it fails. Used by the CLI's `verify` command and by CI tests.
"""

from __future__ import annotations

import re
import zipfile
from pathlib import Path

from reeinvent_pitch_deck.theme import (
    CORE_BLUE,
    CORE_VIOLET,
    DEEP_NAVY,
    INK,
    MID_BLUE,
    MID_VIOLET,
    OFF_WHITE,
    SKY_BLUE,
    SOFT_VIOLET,
    WHITE,
)


CANONICAL_HEX = {
    INK,
    DEEP_NAVY,
    OFF_WHITE,
    WHITE,
    CORE_BLUE,
    MID_BLUE,
    SKY_BLUE,
    CORE_VIOLET,
    MID_VIOLET,
    SOFT_VIOLET,
}


class VerificationError(AssertionError):
    pass


def _read(z: zipfile.ZipFile, name: str) -> str:
    return z.read(name).decode("utf-8", errors="replace")


def check_fonts_embedded(z: zipfile.ZipFile) -> None:
    names = z.namelist()
    fnt = [n for n in names if n.startswith("ppt/fonts/") and n.endswith(".fntdata")]
    if len(fnt) != 6:
        raise VerificationError(
            f"expected 6 ppt/fonts/*.fntdata entries; found {len(fnt)}: {sorted(fnt)}"
        )
    pres = _read(z, "ppt/presentation.xml")
    if "embeddedFontLst" not in pres:
        raise VerificationError(
            "presentation.xml missing <p:embeddedFontLst>"
        )


def check_no_em_dash(z: zipfile.ZipFile) -> None:
    """U+2014 forbidden anywhere in the deck text."""
    for name in z.namelist():
        if not (name.endswith(".xml") or name.endswith(".rels")):
            continue
        body = _read(z, name)
        if "\u2014" in body:
            raise VerificationError(
                f"em-dash (U+2014) found in {name}. DESIGN.md rule 31."
            )


def check_theme_colors(z: zipfile.ZipFile) -> None:
    """Every theme1.xml must include the 9 brand colors among the color scheme."""
    theme_files = [n for n in z.namelist() if re.match(r"ppt/theme/theme\d+\.xml$", n)]
    if not theme_files:
        raise VerificationError("no ppt/theme/themeN.xml files found")
    for tf in theme_files:
        body = _read(z, tf)
        upper = body.upper()
        for hex_val in CANONICAL_HEX:
            if hex_val.upper() not in upper:
                raise VerificationError(
                    f"theme {tf} missing brand color #{hex_val}. "
                    "Theme color scheme is the source of truth for re-skinning."
                )


def check_no_sp_autofit(z: zipfile.ZipFile) -> None:
    """DESIGN.md section 12.1 rule 11: card text uses normAutofit, not spAutoFit."""
    for name in z.namelist():
        if not name.startswith("ppt/slides/") or not name.endswith(".xml"):
            continue
        body = _read(z, name)
        if "<a:spAutoFit" in body:
            raise VerificationError(
                f"{name} contains <a:spAutoFit/>. Use <a:normAutofit/> for card text."
            )


def check_canvas_size(z: zipfile.ZipFile) -> None:
    body = _read(z, "ppt/presentation.xml")
    # 16:9 widescreen at 13.333 in x 7.5 in = 12192000 x 6858000 EMU
    if 'cx="12192000"' not in body or 'cy="6858000"' not in body:
        raise VerificationError(
            "slide canvas is not 13.333 in x 7.5 in (16:9 widescreen). "
            "Expected cx=12192000 cy=6858000 in <p:sldSz>."
        )


def verify_deck(path: Path) -> None:
    """Run every pre-flight check. Raise VerificationError on first failure."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"deck not found: {path}")
    with zipfile.ZipFile(path, "r") as z:
        check_fonts_embedded(z)
        check_no_em_dash(z)
        check_theme_colors(z)
        check_no_sp_autofit(z)
        check_canvas_size(z)
