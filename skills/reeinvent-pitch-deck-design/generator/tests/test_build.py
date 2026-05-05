"""End-to-end: build the example decks, verify every brand contract."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

from reeinvent_pitch_deck.build import build_deck
from reeinvent_pitch_deck.spec import load_spec
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
from reeinvent_pitch_deck.verify import VerificationError, verify_deck


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"


@pytest.fixture
def minimal_pptx(tmp_path):
    deck = load_spec(EXAMPLES_DIR / "minimal.json")
    out = tmp_path / "minimal.pptx"
    build_deck(deck, out)
    return out


@pytest.fixture
def full_pptx(tmp_path):
    deck = load_spec(EXAMPLES_DIR / "reeinvent-full.json")
    out = tmp_path / "reeinvent-full.pptx"
    build_deck(deck, out)
    return out


def test_minimal_deck_verifies(minimal_pptx):
    verify_deck(minimal_pptx)


def test_full_deck_verifies(full_pptx):
    verify_deck(full_pptx)


def test_full_deck_has_twelve_slides(full_pptx):
    with zipfile.ZipFile(full_pptx) as z:
        slides = [n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")]
    assert len(slides) == 12


def test_six_fonts_embedded(minimal_pptx):
    with zipfile.ZipFile(minimal_pptx) as z:
        fnt = [n for n in z.namelist() if n.startswith("ppt/fonts/") and n.endswith(".fntdata")]
    assert len(fnt) == 6


def test_theme_carries_nine_brand_colors(minimal_pptx):
    with zipfile.ZipFile(minimal_pptx) as z:
        theme = z.read("ppt/theme/theme1.xml").decode("utf-8").upper()
    for hex_val in (
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
    ):
        assert hex_val.upper() in theme, f"theme missing brand color #{hex_val}"


def test_no_em_dash_anywhere(full_pptx):
    with zipfile.ZipFile(full_pptx) as z:
        for name in z.namelist():
            if name.endswith(".xml") or name.endswith(".rels"):
                body = z.read(name).decode("utf-8", errors="replace")
                assert "\u2014" not in body, f"em-dash found in {name}"


def test_no_sp_autofit_anywhere(full_pptx):
    with zipfile.ZipFile(full_pptx) as z:
        for name in z.namelist():
            if name.startswith("ppt/slides/") and name.endswith(".xml"):
                body = z.read(name).decode("utf-8")
                assert "<a:spAutoFit" not in body, (
                    f"{name} has spAutoFit; cards must use normAutofit (DESIGN.md 12.1 rule 11)"
                )


def test_stat_number_has_gradient_text_fill(full_pptx):
    """DESIGN.md section 12.1 rule 12: stat number carries Signature Gradient."""
    with zipfile.ZipFile(full_pptx) as z:
        # Find any slide containing "6 wk" - it is the stat slide.
        for name in z.namelist():
            if not (name.startswith("ppt/slides/slide") and name.endswith(".xml")):
                continue
            body = z.read(name).decode("utf-8")
            if "6 wk" in body:
                # Every run inside the stat number must have a:gradFill.
                # Check that gradFill appears with the brand stops.
                assert "<a:gradFill" in body, f"{name} stat number missing gradFill"
                assert "2665E2" in body.upper() and "C26DE6" in body.upper(), (
                    f"{name} gradFill missing brand stops"
                )
                return
    pytest.fail("stat slide ('6 wk') not found in deck")


def test_canvas_is_widescreen(minimal_pptx):
    with zipfile.ZipFile(minimal_pptx) as z:
        body = z.read("ppt/presentation.xml").decode("utf-8")
    assert 'cx="12192000"' in body
    assert 'cy="6858000"' in body


def test_speaker_notes_brand_theme(tmp_path):
    """Notes-master theme (theme2.xml) is created lazily when speaker notes
    are first added. The brand theme MUST propagate to it; otherwise the
    notes pane shows Office default colors and a re-skin breaks half the deck.
    Regression for the bug found during the v3.0.0 sales-deck test run.
    """
    from reeinvent_pitch_deck.build import build_deck
    from reeinvent_pitch_deck.spec import parse_spec

    deck = parse_spec({
        "title": "Notes regression",
        "slides": [
            {
                "archetype": "cover",
                "title": "With notes",
                "notes": "These notes force the notes-master theme to instantiate.",
            }
        ],
    })
    out = tmp_path / "notes.pptx"
    build_deck(deck, out)

    with zipfile.ZipFile(out) as z:
        theme_files = [n for n in z.namelist() if n.startswith("ppt/theme/") and n.endswith(".xml")]
        assert len(theme_files) >= 2, f"expected theme1 + theme2 (notes); got {theme_files}"
        for tf in theme_files:
            body = z.read(tf).decode("utf-8").upper()
            for hex_val in ("0A1220", "1B2848", "2665E2", "C26DE6", "D79BEC"):
                assert hex_val in body, f"{tf} missing brand color #{hex_val}"
