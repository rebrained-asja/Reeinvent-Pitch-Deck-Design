"""Resolve paths to brand assets shipped with the skill.

The generator package lives at <skill_root>/generator/. Brand assets and
fonts live at <skill_root>/assets/. This module centralizes the path math.
"""

from __future__ import annotations

from pathlib import Path

# generator/reeinvent_pitch_deck/assets.py -> generator/reeinvent_pitch_deck
# parents[0] = reeinvent_pitch_deck, [1] = generator, [2] = skill_root
SKILL_ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = SKILL_ROOT / "assets"
LOGO_DIR = ASSETS_DIR / "logo"
FONTS_DIR = ASSETS_DIR / "fonts" / "Roboto"


def asset(name: str) -> Path:
    p = LOGO_DIR / name
    if not p.is_file():
        raise FileNotFoundError(f"brand asset missing: {p}")
    return p


# Brand-mark PNG paths (PPTX always uses PNG per DESIGN.md section 14).
ARROW_UP_PNG = lambda: asset("Arrow-Up@2x.png")
UPWARDS_ARROW_PNG = lambda: asset("Upwards-Arrow@2x.png")
WHITE_LOGO_PNG = lambda: asset("White-Logo@2x.png")
GRADIENT_LOGO_PNG = lambda: asset("Gradient-Logo@2x.png")


def font_file(filename: str) -> Path:
    p = FONTS_DIR / filename
    if not p.is_file():
        raise FileNotFoundError(f"font file missing: {p}")
    return p
