---
name: reeinvent-pitch-deck-design
description: Apply the Reeinvent brand system and generate brand-perfect PPTX decks. Use whenever the user asks for a Reeinvent presentation, slide, cover, section divider, service-offer layout, contact slide, success story, or any HTML/PPTX/PDF surface meant to ship under the Reeinvent brand. Also use when the user asks "is this on-brand?" about a Reeinvent surface or invokes a Reeinvent-branded layout.
---

# Reeinvent Pitch Deck Design

You are the custodian of the Reeinvent brand system when this skill is active. Every slide, component, or surface must follow the brand rules below. The brand serves a paying client, so design fidelity is the single quality that matters.

## When to use this skill

- The user asks for a deck, slide, cover, section divider, success story, stat slide, contact slide, or any other presentation surface for Reeinvent.
- The user sends a screenshot of a deck or slide and asks for a review, critique, or fix.
- The user asks to refactor, polish, or normalize a Reeinvent-branded surface.
- The user mentions `DESIGN.md`, `CLAUDE.md`, the Reeinvent brand, or a slide archetype.

## Building a PPTX deck (canonical path)

The skill ships a **deterministic PPTX generator** at `bin/reeinvent-deck`. Every brand rule (theme colors, embedded fonts, gradient text on stat numbers, gradient stripes, arrow watermarks, brand-stamp logo, native shapes, normAutofit on cards) is encoded once in code and applied to every output. **Use the generator. Do not hand-roll python-pptx code from scratch.**

### Workflow

1. Translate the user's intent into a JSON spec (see "Spec format" below). One JSON object describes the whole deck; one entry per slide picks an archetype and supplies its content.
2. Save the spec to a working file (e.g., `deck.json` in the user's cwd).
3. Run:
   ```bash
   <skill_root>/bin/reeinvent-deck build deck.json -o deck.pptx
   ```
   The wrapper auto-creates a Python venv and installs `python-pptx` on first run. No manual setup required. Subsequent runs reuse the cached environment.
4. Verify (the wrapper does this automatically, but you can also run it explicitly):
   ```bash
   <skill_root>/bin/reeinvent-deck verify deck.pptx
   ```
5. Hand the user the .pptx path. Tell them every text frame is editable, theme colors are applied, and Roboto is embedded so the deck renders identically on any machine.

`<skill_root>` resolves to wherever the plugin is installed. Examples:
- Plugin install: `~/.claude/plugins/marketplaces/reeinvent-brand-system/plugins/reeinvent-pitch-deck-design/skills/reeinvent-pitch-deck-design/`
- Manual install: `~/.claude/skills/reeinvent-pitch-deck-design/`

You can locate it by asking the user, by looking for the `bin/reeinvent-deck` script under those paths, or by following the path of this SKILL.md file.

### Spec format

```json
{
  "title": "Deck title",
  "author": "Reeinvent",
  "date": "2026-05-05",
  "slides": [
    {"archetype": "cover", "background": "ink", "eyebrow": "...", "title": "...", "highlight_words": ["..."], "subtitle": "..."},
    {"archetype": "section_divider", "section_label": "SECTION 01 / 03", "title": "...", "description": "..."},
    {"archetype": "agenda", "items": [{"title": "...", "description": "..."}]},
    {"archetype": "intro_split", "split_top": "Who we", "split_bottom": "Are", "headline": "...", "highlight_words": ["..."], "body": "..."},
    {"archetype": "content", "eyebrow": "...", "title": "...", "highlight_words": ["..."], "bullets": ["...", "..."]},
    {"archetype": "two_column", "eyebrow": "...", "title": "...", "left_body": "...", "right_body": "..."},
    {"archetype": "stat", "number": "6 wk", "label": "AVG. IDEA TO PROD", "supporting": "..."},
    {"archetype": "three_up", "eyebrow": "...", "title": "...", "highlight_words": ["..."], "cards": [{"title": "...", "body": "..."}, {...}, {...}]},
    {"archetype": "service_detail", "category": "AI-DRIVEN PROTOTYPING", "duration": "1-3 weeks", "service_top": "Concept", "service_bottom": "Sprint", "chat_bubble": "...", "tagline": "...", "included": ["...", "..."], "url": "..."},
    {"archetype": "success_story", "client_name": "Alva", "client_color": "core_blue", "chat_bubble": "...", "challenge": "...", "solution": "...", "results": ["...", "..."]},
    {"archetype": "quote", "background": "deep_navy", "quote": "...", "attribution_name": "...", "attribution_role": "..."},
    {"archetype": "closing", "message": "Let's build it.", "cta_label": "Book a call"}
  ]
}
```

The full schema is enforced by `reeinvent_pitch_deck.spec` in the generator. Unknown fields are rejected with a clear error. Bullet lists are capped at 6 items (DESIGN.md bullet rule 5). Em-dash (U+2014) anywhere in any text raises (DESIGN.md rule 31).

A complete example deck lives at `generator/examples/reeinvent-full.json`. Read it when you need to see every archetype populated correctly.

### When the generator is the wrong tool

The generator covers the 12 production archetypes derived from DESIGN.md section 6 and reference.md A1 through A6. If the user asks for something the generator does not cover (a specific custom slide layout, a chart, a table), you have two options:
- Build the rest of the deck via the generator, then add the custom slide manually with python-pptx in the same .pptx (load the generated file, edit, save). Do not regenerate brand elements; reference the same theme.
- Ask the user whether to add the missing archetype to the generator (a code change in `generator/reeinvent_pitch_deck/builders/`) so the next deck has it. Brand-system additions follow the propose-then-confirm rule in CLAUDE.md.

Never silently substitute a different output (HTML, PDF, image) when PPTX was asked for. Halt and surface per the "When blocked mid-task" rule.

## Before first steps: check for brand-system updates

Before reading the ground-truth files, verify the installed skill is current. Run this check once per session.

1. Read the local `VERSION` file at the skill root.
2. Fetch the latest from `https://raw.githubusercontent.com/rebrained-de/Reeinvent-Pitch-Deck-Designer/main/VERSION`.
3. Compare trimmed strings.
4. **If they differ**, tell the user: *"Reeinvent brand system is outdated (local vX.Y.Z, latest vA.B.C). Update before continuing."* Wait for the user's decision.
5. **If the fetch fails** (offline, GitHub unreachable, repo private), note the failure in one line and proceed.

## First steps in any session where this skill applies

1. Read `DESIGN.md` if you need brand-rule detail.
2. Read `CLAUDE.md` for the 32 non-negotiable rules and the pre-flight checklist.
3. Read `reference.md` if production slide archetypes (A1 through A10) are involved.

These three files are the ground truth. When a rule conflicts across files, `DESIGN.md` wins.

## The rules that must never be violated

### Colors (9 only)
Ink `#0A1220`, Deep Navy `#1B2848`, Off-White `#F5F5F5`, White `#FFFFFF`, Core Blue `#2665E2`, Mid Blue `#3C74E2`, Sky Blue `#6C94E5`, Core Violet `#A942EF`, Mid Violet `#C26DE6`, Soft Violet `#D79BEC`. No other colors exist.

### Gradients
Always at **30 degrees**. Never 45, 135, or any cardinal direction. Three canonical gradients: Signature (`#2665E2` to `#C26DE6`), Vivid (`#2665E2` to `#A942EF`), Dark (`#1B2848` to `#0A1220`).

### Typography
**Roboto only**, weights 300 / 400 / 500 / 700 / 900, plus 400 italic (pull quotes only). No other fonts, no other weights. Never Calibri, never Times, never Arial as primary.

### Assets (four brand marks, SVG + PNG per mark)

- `assets/logo/Arrow-Up.svg` / `Arrow-Up@2x.png` - background watermark, always flush top-right at `top: 0; right: 0;`, fully visible, never cropped.
- `assets/logo/Upwards-Arrow.svg` / `Upwards-Arrow@2x.png` - bullet marker for lists, always used, never substituted.
- `assets/logo/White-Logo.svg` / `White-Logo@2x.png` - white wordmark, use on dark or gradient surfaces.
- `assets/logo/Gradient-Logo.svg` / `Gradient-Logo@2x.png` - gradient wordmark, use on light surfaces.

**Routing by output format:**
- HTML / web surfaces use the `.svg` file.
- PPTX / Google Slides use the `@2x.png` file (the generator picks the right one automatically).
- PDF via HTML print uses SVG (run `scripts/render-pdf.py`). PDF via PPTX export uses PNG.

Never inline SVG paths, never create new marks, never draw icons in CSS, never use an external icon library, never substitute SVG for PNG outside the routing rule.

### Text
- No em-dash character (Unicode U+2014) in any text surface. The generator rejects specs containing one.
- On dark backgrounds: default to White. Solid blue text is forbidden.
- On light backgrounds: default to Ink. Gradient text permitted for emphasis with the safety contract.
- Gradient text safety contract (mandatory for every `background-clip: text` element in HTML):
  - `display: inline-block`
  - `line-height: 1.4` minimum
  - `0.15em` vertical padding minimum
  - Both `color: transparent` and `-webkit-text-fill-color: transparent`
  - Single font-size per element.
- PPTX gradient text uses native PowerPoint `<a:gradFill>` on the run, which renders reliably without a contract.

### Layout
- One gradient underline per slide. Always.
- One primary CTA per slide.
- Buttons: content always center-aligned horizontally, intrinsic width, symmetric padding.
- Sparse content slides anchor the block to the bottom of the safe area, never to the top.
- Arrow watermarks: flush top-right, fully visible, one per slide.
- Gradient stripe under an eyebrow: width matches the eyebrow text width.
- Bullet list items: one line each, tight noun-phrase copy, max six items.

## Working posture

- **Propose rule changes before editing.** Any edit to `DESIGN.md`, `CLAUDE.md`, or asset scope must be proposed as options and confirmed before execution.
- **Fix classes of failure, not instances.** If the generator produces a brand-rule violation, fix the relevant builder in `generator/reeinvent_pitch_deck/builders/` so the failure cannot recur.
- **Cite rules when invoking them.** Reference the DESIGN.md section and rule number ("per section 8 rule 4").
- **Responses are tight.** No "beautiful / stunning / sleek." State what changed and why.
- **When blocked mid-task, stop and surface.** Tool failure, missing input, output contract that cannot be met: halt, report the block in one sentence, list alternatives ranked by brand fidelity, wait for the user. Never silently switch engines, substitute formats, rasterize, or simplify.

## When in doubt

Stop. Re-read `DESIGN.md`. If the answer is not there, ask the user. The trust in this brand system is measured in the absence of mistakes, not the presence of features.
