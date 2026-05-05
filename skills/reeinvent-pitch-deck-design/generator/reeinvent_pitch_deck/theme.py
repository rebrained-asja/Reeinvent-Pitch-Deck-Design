"""Reeinvent brand constants. Single source of truth for every builder.

Every value here is pinned to DESIGN.md. If a builder needs a color, gradient,
or type measurement, it imports from this module rather than typing a literal.
"""

from __future__ import annotations

from dataclasses import dataclass


# 9 canonical colors (DESIGN.md section 2). RGB hex only. No 11th color exists.
INK = "0A1220"
DEEP_NAVY = "1B2848"
OFF_WHITE = "F5F5F5"
WHITE = "FFFFFF"
CORE_BLUE = "2665E2"
MID_BLUE = "3C74E2"
SKY_BLUE = "6C94E5"
CORE_VIOLET = "A942EF"
MID_VIOLET = "C26DE6"
SOFT_VIOLET = "D79BEC"

PALETTE = {
    "ink": INK,
    "deep_navy": DEEP_NAVY,
    "off_white": OFF_WHITE,
    "white": WHITE,
    "core_blue": CORE_BLUE,
    "mid_blue": MID_BLUE,
    "sky_blue": SKY_BLUE,
    "core_violet": CORE_VIOLET,
    "mid_violet": MID_VIOLET,
    "soft_violet": SOFT_VIOLET,
}


# 3 canonical gradients (DESIGN.md section 2 + 8). All at 30 degrees, always.
@dataclass(frozen=True)
class Gradient:
    name: str
    stop_0: str
    stop_100: str
    angle_deg: int = 30


SIGNATURE_GRADIENT = Gradient("Signature", CORE_BLUE, MID_VIOLET)
VIVID_GRADIENT = Gradient("Vivid", CORE_BLUE, CORE_VIOLET)
DARK_GRADIENT = Gradient("Dark", DEEP_NAVY, INK)


# Slide canvas (DESIGN.md): 16:9, 13.333 in x 7.5 in. EMU is python-pptx's
# native unit for shape geometry; 914400 EMU = 1 inch.
EMU_PER_INCH = 914400
SLIDE_WIDTH_IN = 13.333
SLIDE_HEIGHT_IN = 7.5
SLIDE_WIDTH_EMU = int(SLIDE_WIDTH_IN * EMU_PER_INCH)
SLIDE_HEIGHT_EMU = int(SLIDE_HEIGHT_IN * EMU_PER_INCH)


# Type scale (DESIGN.md section 3). Sizes in pt; weight is the OOXML/CSS
# font-weight number.
@dataclass(frozen=True)
class TypeRole:
    size_pt: float
    weight: int
    line_height: float
    italic: bool = False


TYPE_SCALE = {
    "mega_title": TypeRole(80, 700, 1.05),
    "title": TypeRole(54, 700, 1.10),
    "section_divider": TypeRole(72, 700, 1.10),
    "sub_headline": TypeRole(32, 400, 1.30),
    "body": TypeRole(20, 400, 1.35),
    "secondary_body": TypeRole(16, 400, 1.40),
    "stat_number": TypeRole(120, 700, 1.00),
    "stat_label": TypeRole(16, 500, 1.20),
    "eyebrow": TypeRole(14, 500, 1.30),
    "footer": TypeRole(10, 400, 1.20),
    "quote": TypeRole(40, 400, 1.25, italic=True),
    "cta_label": TypeRole(20, 500, 1.00),
}


# Margins and rhythm (DESIGN.md section 9).
SAFE_AREA_IN = 0.5
STANDARD_MARGIN_IN = 0.6
TITLE_TOP_MARGIN_IN = 1.2
FOOTER_HEIGHT_IN = 0.85

HEADLINE_TO_BODY_GAP_PT = 32
PARAGRAPH_GAP_PT = 16
SECTION_GAP_PT = 48
EYEBROW_TO_TITLE_GAP_PT = 12


# Brand-stamp logo placement (reference.md global pattern).
LOGO_STAMP_HEIGHT_IN = 0.5
LOGO_STAMP_RIGHT_IN = 0.4
LOGO_STAMP_TOP_IN = 0.4

# Cover-slide logo placement (DESIGN.md section 6.1).
COVER_LOGO_HEIGHT_IN = 0.8

# Closing-slide logo placement (DESIGN.md section 6.8).
CLOSING_LOGO_HEIGHT_IN = 0.8


# Roboto typeface names matching the embedded-font typefaces in
# reeinvent_pitch_deck.embed.FONT_MAP. Slides reference these names directly.
FONT_REGULAR = "Roboto"
FONT_LIGHT = "Roboto Light"
FONT_MEDIUM = "Roboto Medium"
FONT_BLACK = "Roboto Black"


def weight_to_typeface(weight: int) -> str:
    """Map numeric weight to the typeface name PowerPoint should select.

    The embedded-font OOXML stores Light/Medium/Black as their own typefaces
    (see embed.FONT_MAP); 400 and 700 share the "Roboto" typeface and use the
    bold attribute on the run.
    """
    if weight == 300:
        return FONT_LIGHT
    if weight == 500:
        return FONT_MEDIUM
    if weight == 900:
        return FONT_BLACK
    return FONT_REGULAR


def is_bold_weight(weight: int) -> bool:
    """OOXML bold attribute. True only for 700 inside the 'Roboto' typeface."""
    return weight == 700
