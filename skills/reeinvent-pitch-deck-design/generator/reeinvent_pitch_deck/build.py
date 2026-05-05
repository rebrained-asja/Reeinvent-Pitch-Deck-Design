"""Top-level build pipeline. Spec + master + per-archetype dispatch + embed."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation

from reeinvent_pitch_deck.embed import embed_fonts
from reeinvent_pitch_deck.master import (
    add_blank_slide,
    finalize_branded_presentation,
    new_branded_presentation,
)
from reeinvent_pitch_deck.spec import DeckSpec, SlideSpec

from reeinvent_pitch_deck.builders import (
    cover,
    divider,
    content as content_builder,
    two_column,
    stat,
    three_up,
    quote,
    closing,
    agenda,
    intro_split,
    service_detail,
    success_story,
)


DISPATCH = {
    "cover": cover.build,
    "section_divider": divider.build,
    "intro_split": intro_split.build,
    "content": content_builder.build,
    "two_column": two_column.build,
    "stat": stat.build,
    "three_up": three_up.build,
    "quote": quote.build,
    "closing": closing.build,
    "agenda": agenda.build,
    "service_detail": service_detail.build,
    "success_story": success_story.build,
}


def build_deck(deck: DeckSpec, output_path: Path, *, skip_font_embed: bool = False) -> Path:
    """Build a deck from a validated DeckSpec, save, embed Roboto, return path."""
    prs = new_branded_presentation()
    # Set core properties.
    prs.core_properties.title = deck.title
    prs.core_properties.author = deck.author
    if deck.date:
        # core_properties.created accepts a datetime; the JSON spec gives a
        # YYYY-MM-DD string. Skip if the format does not parse cleanly.
        try:
            from datetime import datetime
            prs.core_properties.created = datetime.fromisoformat(deck.date)
        except Exception:
            pass

    for slide_spec in deck.slides:
        slide = add_blank_slide(prs)
        builder = DISPATCH[slide_spec.archetype]
        builder(slide, slide_spec)
        notes_text = slide_spec.get("notes")
        if notes_text:
            slide.notes_slide.notes_text_frame.text = notes_text

    # Patch every theme part (slide master, notes master, handout master if
    # present) AFTER all slides built so lazily-created notes themes get
    # the brand color scheme.
    finalize_branded_presentation(prs)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output))

    if not skip_font_embed:
        embed_fonts(output)

    return output
