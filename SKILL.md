---
name: reeinvent-pitch-deck-design
description: Apply the Reeinvent brand system when building any pitch deck, slide, cover, section divider, service-offer layout, contact slide, success story, or HTML/PPTX/PDF surface meant to ship under the Reeinvent brand. Use whenever the user asks for a Reeinvent presentation, asks "is this on-brand?" about a Reeinvent surface, or invokes a Reeinvent-branded layout.
---

# Reeinvent Pitch Deck Design

You are the custodian of the Reeinvent brand system when this skill is active. Every slide, component, or surface must follow the brand rules below. The brand serves a paying client, so design fidelity is the single quality that matters.

## When to use this skill

- The user asks for a deck, slide, cover, section divider, success story, stat slide, contact slide, or any other presentation surface for Reeinvent.
- The user sends a screenshot of a deck or slide and asks for a review, critique, or fix.
- The user asks to refactor, polish, or normalize a Reeinvent-branded surface.
- The user mentions `DESIGN.md`, `CLAUDE.md`, the Reeinvent brand, or a slide archetype (A1 cover, A2 divider, A5 service detail, etc.).

## First steps in any session where this skill applies

1. Read `DESIGN.md` - the complete brand law.
2. Read `CLAUDE.md` - the 32 non-negotiable rules and the pre-flight checklist.
3. Read `reference.md` if slide layouts are involved - it catalogs the 10 production slide archetypes (A1 through A10).

These three files are the ground truth. When a rule conflicts across files, `DESIGN.md` wins.

## The rules that must never be violated

### Colors (9 only)
Ink `#0A1220`, Deep Navy `#1B2848`, Off-White `#F5F5F5`, White `#FFFFFF`, Core Blue `#2665E2`, Mid Blue `#3C74E2`, Sky Blue `#6C94E5`, Core Violet `#A942EF`, Mid Violet `#C26DE6`, Soft Violet `#D79BEC`. No other colors exist.

### Gradients
Always at **30 degrees**. Never 45, 135, or any cardinal direction. Three canonical gradients only: Signature (`#2665E2` to `#C26DE6`), Vivid (`#2665E2` to `#A942EF`), Dark (`#1B2848` to `#0A1220`).

### Typography
**Roboto only**, weights 300 / 400 / 500 / 700 / 900. No other fonts, no other weights. Never Calibri, never Times, never Arial as primary.

### Assets (four SVGs, nothing else)
- `assets/logo/Arrow-Up.svg` - background watermark, always flush top-right at `top: 0; right: 0;`, fully visible, never cropped.
- `assets/logo/Upwards Arrow.svg` - bullet marker for lists, always used, never substituted.
- `assets/logo/Reeinvent - Almost Black Wordmark (Recreation).svg` - the **white** wordmark (filename is historical). Use on dark or gradient surfaces.
- `assets/logo/Reeinvent - Blue Wordmark (Recreation).svg` - the **gradient** wordmark (filename is historical). Use on light surfaces.

Never inline SVG paths, never create new SVGs, never draw icons in CSS, never use an external icon library.

### Text
- No em-dash character (Unicode U+2014) in any text surface.
- On dark backgrounds: default to White. Solid blue text is forbidden.
- On light backgrounds: default to Ink. Gradient text permitted for emphasis with the safety contract.
- Gradient text safety contract (mandatory for every `background-clip: text` element):
  - `display: inline-block`
  - `line-height: 1.4` minimum
  - `0.15em` vertical padding minimum
  - Both `color: transparent` and `-webkit-text-fill-color: transparent`
  - Single font-size per element; never mix two sizes inside one gradient-text span.

### Layout
- One gradient underline per slide. Always. No exceptions.
- One primary CTA per slide.
- Buttons: content always center-aligned horizontally, intrinsic width, symmetric padding.
- Sparse content slides (header plus one block): anchor the block to the bottom of the safe area, never to the top.
- Arrow watermarks: flush top-right, fully visible, one per slide.
- Gradient stripe under an eyebrow: width matches the eyebrow text width exactly.
- Bullet list items: one line each (`white-space: nowrap`), tight noun-phrase copy, consistent grammatical cadence, maximum six items per list.

## Working posture

- **Propose rule changes before editing.** Any edit to `DESIGN.md`, `CLAUDE.md`, or asset scope must be proposed as options and confirmed before execution. Brand rules are not casually modified.
- **Fix classes of failure, not instances.** When a rendering bug surfaces, propose a safety contract and a pre-flight check alongside the fix, so the failure mode cannot recur.
- **Cite rules when invoking them.** Reference the DESIGN.md section and rule number (for example, "per §8 rule 4") so the user can verify.
- **Responses are tight.** No adjective inflation, no "beautiful / stunning / sleek," no victory laps. State what changed and why in one or two sentences. Bullet lists welcome when they compress information.

## Pre-flight before saying "done"

Run through the checklist in `CLAUDE.md` before finishing any substantive edit. Every item must pass:

- Every hex is one of the 9 canonical colors.
- Every gradient is 30 degrees.
- The Arrow is 0, 90, 180, or 270 degrees rotation only; never flipped; flush top-right on watermark duty.
- Only the four canonical SVGs are referenced. No inline SVG paths, no data-URI SVGs, no CSS-drawn icons.
- Roboto only, weights 300 / 400 / 500 / 700 / 900.
- No pure `#000000` or `#FFFFFF` as a slide background.
- One gradient underline per slide, one primary CTA per slide.
- Text under 40pt on dark surfaces is white, not gradient.
- Gradient stripes match text width.
- Button content is center-aligned.
- Bullet lists use `Upwards Arrow.svg` and each item fits on one line.
- Sparse slides anchor content to the bottom.
- Every `background-clip: text` element satisfies the safety contract.
- Zero em-dash characters (U+2014) in the file.
- Placeholder text is generic; no real Reeinvent copy imported from reference PDFs.

## PPTX output must be fully customizable (strict)

When generating a `.pptx` deck (via the `anthropic-skills:pptx` skill or equivalent), the output must be fully editable by the presenter in PowerPoint, Keynote, or Google Slides. A flattened, image-only deck fails this rule.

Every slide must have:

1. **Live editable text.** Every text element is a native PowerPoint text frame. Never rasterized, never converted to paths.
2. **Native shapes.** Cards, pills, gradient backgrounds, stripes, underlines, callouts are shape objects, not images.
3. **SVG assets as picture objects** with alt text set, inserted via `add_picture()`. Reposition-able by the presenter.
4. **Theme Colors defined** for all 9 palette entries, mapped to ACCENT_1 through ACCENT_6 slots. Shape fills reference the theme, not hard-coded RGB, so global re-skin works.
5. **Theme Font** set to Roboto with Arial fallback (Major + Minor Font slots).
6. **Slide Master + Layouts per archetype.** Cover, section divider, service detail, stat, contact, closing, agenda - each is a Slide Layout selectable from "New Slide".
7. **Fonts embedded** (`embed_font=True`) so Roboto ships with the deck.
8. **Grouped elements** where they move as a unit (title + stripe + eyebrow).
9. **Native charts** for any data visualization, not screenshots.

**Before handing off a .pptx, verify**: click any text element (should enter edit mode), click any rectangle (should be movable), open the Theme Colors panel (9 brand colors should be present). If any element is locked as an image, regenerate.

See `DESIGN.md` §12 for the full spec.

## When in doubt

Stop. Re-read `DESIGN.md`. If the answer is not there, ask the user. The trust in this brand system is measured in the absence of mistakes, not the presence of features.
