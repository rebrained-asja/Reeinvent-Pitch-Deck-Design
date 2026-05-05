"""JSON spec parser + validator. Strict: unknown keys raise.

Spec shape (top level):
    {
      "title": "...",         # optional, used in PPTX core props
      "author": "...",         # optional
      "date": "YYYY-MM-DD",    # optional
      "slides": [ <slide-spec>, ... ]
    }

Slide-spec shape (one of the archetypes below). Every slide must declare
"archetype". Per-archetype required fields are documented in the ARCHETYPE
table; unknown fields are rejected so authors notice typos.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


VALID_BACKGROUNDS = {"ink", "off_white", "deep_navy", "gradient", "dark_gradient", "vivid_gradient"}


class SpecError(ValueError):
    pass


# Per-archetype field definitions: required, optional, default.
ARCHETYPES: dict[str, dict[str, Any]] = {
    "cover": {
        "required": {"title"},
        "optional": {"eyebrow", "highlight_words", "subtitle", "background", "date", "author", "notes"},
        "defaults": {"background": "ink"},
    },
    "section_divider": {
        "required": {"title"},
        "optional": {"section_label", "description", "notes"},
        "defaults": {},
    },
    "intro_split": {
        "required": {"split_top", "split_bottom", "headline", "body"},
        "optional": {"highlight_words", "image_note", "image", "notes"},
        "defaults": {},
    },
    "content": {
        "required": {"title"},
        "optional": {"eyebrow", "body", "bullets", "highlight_words", "background", "notes"},
        "defaults": {"background": "off_white"},
    },
    "two_column": {
        "required": {"title", "left_body", "right_body"},
        "optional": {"eyebrow", "highlight_words", "background", "notes"},
        "defaults": {"background": "off_white"},
    },
    "stat": {
        "required": {"number", "label"},
        "optional": {"supporting", "background", "notes"},
        "defaults": {"background": "off_white"},
    },
    "three_up": {
        "required": {"title", "cards"},  # cards is list of {title, body, optional eyebrow}
        "optional": {"eyebrow", "highlight_words", "background", "notes"},
        "defaults": {"background": "off_white"},
    },
    "quote": {
        "required": {"quote", "attribution_name"},
        "optional": {"attribution_role", "background", "notes"},
        "defaults": {"background": "deep_navy"},
    },
    "closing": {
        "required": {"message"},
        "optional": {"cta_label", "notes"},
        "defaults": {},
    },
    "agenda": {
        "required": {"items"},  # list of {title, description}
        "optional": {"eyebrow", "title", "notes"},
        "defaults": {"eyebrow": "AGENDA", "title": "Today's agenda"},
    },
    "service_detail": {
        "required": {"category", "service_top", "service_bottom", "duration", "tagline", "included"},
        "optional": {"chat_bubble", "url", "image", "notes"},
        "defaults": {},
    },
    "success_story": {
        "required": {"client_name", "challenge", "solution", "results"},
        "optional": {"chat_bubble", "client_color", "image", "notes"},
        "defaults": {"client_color": "core_blue"},
    },
}


@dataclass
class SlideSpec:
    archetype: str
    fields: dict[str, Any] = field(default_factory=dict)

    def get(self, key: str, default: Any = None) -> Any:
        return self.fields.get(key, default)


@dataclass
class DeckSpec:
    title: str = "Reeinvent Pitch Deck"
    author: str = "Reeinvent"
    date: str | None = None
    slides: list[SlideSpec] = field(default_factory=list)


def _check_em_dash(value: Any, path: str) -> None:
    """DESIGN.md rule 31: zero U+2014 anywhere in any output."""
    if isinstance(value, str):
        if "\u2014" in value:
            raise SpecError(
                f"em-dash (U+2014) found at {path}: {value!r}. "
                "Replace with hyphen, colon, semicolon, or period (DESIGN.md rule 31)."
            )
    elif isinstance(value, list):
        for i, v in enumerate(value):
            _check_em_dash(v, f"{path}[{i}]")
    elif isinstance(value, dict):
        for k, v in value.items():
            _check_em_dash(v, f"{path}.{k}")


def _validate_slide(idx: int, raw: dict[str, Any]) -> SlideSpec:
    if not isinstance(raw, dict):
        raise SpecError(f"slides[{idx}] must be an object")
    if "archetype" not in raw:
        raise SpecError(f"slides[{idx}] missing required 'archetype' field")
    archetype = raw["archetype"]
    if archetype not in ARCHETYPES:
        valid = ", ".join(sorted(ARCHETYPES.keys()))
        raise SpecError(
            f"slides[{idx}] unknown archetype {archetype!r}. Valid: {valid}"
        )
    schema = ARCHETYPES[archetype]
    fields = {k: v for k, v in raw.items() if k != "archetype"}
    # Reject unknown fields.
    allowed = set(schema["required"]) | set(schema["optional"])
    unknown = set(fields.keys()) - allowed
    if unknown:
        raise SpecError(
            f"slides[{idx}] ({archetype}) has unknown fields: {sorted(unknown)}. "
            f"Allowed: {sorted(allowed)}"
        )
    # Apply defaults.
    for k, v in schema["defaults"].items():
        fields.setdefault(k, v)
    # Required fields present?
    missing = set(schema["required"]) - set(fields.keys())
    if missing:
        raise SpecError(
            f"slides[{idx}] ({archetype}) missing required fields: {sorted(missing)}"
        )
    # Background validation.
    if "background" in fields and fields["background"] not in VALID_BACKGROUNDS:
        raise SpecError(
            f"slides[{idx}] background={fields['background']!r} not in {sorted(VALID_BACKGROUNDS)}"
        )
    # Bullets / cards / items / included are lists of strings or dicts; bound checks.
    if archetype == "content" and "bullets" in fields:
        if not isinstance(fields["bullets"], list) or not all(isinstance(x, str) for x in fields["bullets"]):
            raise SpecError(f"slides[{idx}] bullets must be a list of strings")
        if len(fields["bullets"]) > 6:
            raise SpecError(f"slides[{idx}] bullets exceed max 6 (DESIGN.md bullet rule 5)")
    if archetype == "three_up":
        cards = fields["cards"]
        if not isinstance(cards, list) or len(cards) != 3:
            raise SpecError(f"slides[{idx}] three_up.cards must be a list of exactly 3 entries")
        for ci, c in enumerate(cards):
            if not isinstance(c, dict) or "title" not in c or "body" not in c:
                raise SpecError(f"slides[{idx}] three_up.cards[{ci}] missing title or body")
    if archetype == "agenda":
        items = fields["items"]
        if not isinstance(items, list) or not items:
            raise SpecError(f"slides[{idx}] agenda.items must be a non-empty list")
        for ii, it in enumerate(items):
            if not isinstance(it, dict) or "title" not in it:
                raise SpecError(f"slides[{idx}] agenda.items[{ii}] missing title")
    if archetype == "service_detail":
        if not isinstance(fields["included"], list) or not all(isinstance(x, str) for x in fields["included"]):
            raise SpecError(f"slides[{idx}] service_detail.included must be a list of strings")
        if len(fields["included"]) > 6:
            raise SpecError(
                f"slides[{idx}] service_detail.included exceeds max 6 (DESIGN.md bullet rule 5)"
            )
    if archetype == "success_story":
        results = fields["results"]
        if not isinstance(results, list) or not all(isinstance(x, str) for x in results):
            raise SpecError(f"slides[{idx}] success_story.results must be a list of strings")
        if len(results) > 6:
            raise SpecError(
                f"slides[{idx}] success_story.results exceeds max 6 (DESIGN.md bullet rule 5)"
            )
    # Em-dash check on every text value.
    _check_em_dash(fields, f"slides[{idx}]")
    return SlideSpec(archetype=archetype, fields=fields)


def parse_spec(raw: dict[str, Any]) -> DeckSpec:
    if not isinstance(raw, dict):
        raise SpecError("top-level spec must be an object")
    allowed_top = {"title", "author", "date", "slides"}
    unknown = set(raw.keys()) - allowed_top
    if unknown:
        raise SpecError(f"unknown top-level keys: {sorted(unknown)}. Allowed: {sorted(allowed_top)}")
    if "slides" not in raw or not isinstance(raw["slides"], list) or not raw["slides"]:
        raise SpecError("spec must contain a non-empty 'slides' list")
    deck = DeckSpec(
        title=raw.get("title", "Reeinvent Pitch Deck"),
        author=raw.get("author", "Reeinvent"),
        date=raw.get("date"),
    )
    _check_em_dash(deck.title, "title")
    _check_em_dash(deck.author, "author")
    if deck.date:
        _check_em_dash(deck.date, "date")
    deck.slides = [_validate_slide(i, s) for i, s in enumerate(raw["slides"])]
    return deck


def load_spec(path: Path) -> DeckSpec:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return parse_spec(raw)
