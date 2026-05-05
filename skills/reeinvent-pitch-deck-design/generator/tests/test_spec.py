"""Spec validator: rejects malformed input, accepts the canonical examples."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from reeinvent_pitch_deck.spec import SpecError, parse_spec


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples"


def test_minimal_example_parses():
    raw = json.loads((EXAMPLES_DIR / "minimal.json").read_text())
    deck = parse_spec(raw)
    assert deck.slides
    assert deck.slides[0].archetype == "cover"


def test_full_example_parses():
    raw = json.loads((EXAMPLES_DIR / "reeinvent-full.json").read_text())
    deck = parse_spec(raw)
    archetypes = {s.archetype for s in deck.slides}
    expected = {
        "cover",
        "intro_split",
        "agenda",
        "section_divider",
        "stat",
        "three_up",
        "two_column",
        "service_detail",
        "success_story",
        "quote",
        "content",
        "closing",
    }
    assert archetypes == expected


def test_unknown_archetype_rejected():
    with pytest.raises(SpecError, match="unknown archetype"):
        parse_spec({"slides": [{"archetype": "fancy_pants", "title": "x"}]})


def test_unknown_field_rejected():
    with pytest.raises(SpecError, match="unknown fields"):
        parse_spec({"slides": [{"archetype": "cover", "title": "x", "wat": "y"}]})


def test_em_dash_rejected_in_title():
    with pytest.raises(SpecError, match="em-dash"):
        parse_spec({"slides": [{"archetype": "cover", "title": "Hello \u2014 world"}]})


def test_em_dash_rejected_in_bullets():
    with pytest.raises(SpecError, match="em-dash"):
        parse_spec(
            {
                "slides": [
                    {
                        "archetype": "content",
                        "title": "x",
                        "bullets": ["a", "b \u2014 c"],
                    }
                ]
            }
        )


def test_bullet_max_six_enforced():
    with pytest.raises(SpecError, match="bullets exceed max 6"):
        parse_spec(
            {
                "slides": [
                    {
                        "archetype": "content",
                        "title": "x",
                        "bullets": [str(i) for i in range(7)],
                    }
                ]
            }
        )


def test_three_up_requires_three_cards():
    with pytest.raises(SpecError, match="exactly 3"):
        parse_spec(
            {
                "slides": [
                    {
                        "archetype": "three_up",
                        "title": "x",
                        "cards": [{"title": "a", "body": "b"}],
                    }
                ]
            }
        )


def test_empty_slides_rejected():
    with pytest.raises(SpecError, match="non-empty"):
        parse_spec({"slides": []})


def test_top_level_unknown_key_rejected():
    with pytest.raises(SpecError, match="unknown top-level"):
        parse_spec({"slides": [{"archetype": "cover", "title": "x"}], "wat": 1})
