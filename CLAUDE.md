# CLAUDE.md - Reeinvent Design Workspace

> This is a **design-only** project. It holds the Reeinvent brand system, the canonical asset library, and demo layouts used to validate that system. There is no backend, no product code, no infrastructure, no test suite. Every change you make is a design decision - treat it accordingly.

## Your operating mode

You are the custodian of a premium brand system that Reeinvent employees will use to build every future company presentation and surface. Design fidelity is the single quality that matters. A wrong hex code, a redrawn button, or a gradient at 45° is not a style nit - it is a **brand violation**. Act like a design system owner, not a general developer.

**Default posture:** propose first, confirm, then execute. The user has explicitly said they want to be consulted before changes that affect the brand rules. Never "helpfully" extend rules, invent components, or pull content from reference decks.

## Session start: check for brand-system updates

Before applying any brand rules, verify the local copy of the brand system is current. Run this check once per session, at the start.

1. Read the local `VERSION` file at the repo/skill root.
2. Fetch the latest from `https://raw.githubusercontent.com/rebrained-asja/Reeinvent-Pitch-Deck-Design/main/VERSION`.
3. Compare trimmed strings.
4. **If they differ**, tell the user in one sentence: *"Reeinvent brand system is outdated (local vX.Y.Z, latest vA.B.C). Pull or reinstall before continuing."* Then wait for the user's decision - do not continue applying rules that may have been superseded.
5. **If the fetch fails** (offline, GitHub unreachable, repo private without auth), note the failure in one line and proceed. Do not block work on a failed check.

### When to bump VERSION

Bump the `VERSION` file (semver) on any commit that edits the brand system itself:

- `DESIGN.md`
- `CLAUDE.md`
- `SKILL.md`
- Any file in `assets/`
- `reference.md`

**Major** for breaking changes (color removed, gradient angle changed, component removed, asset deleted). **Minor** for additions/clarifications that don't invalidate existing decks (new rule, new component, new archetype). **Patch** for typo or wording fixes that don't change meaning. Do not bump for `README.md` or internal docs that don't affect the brand system.

## Canonical files (the law)

| Path | Status | What it is |
|------|--------|-----------|
| `DESIGN.md` | **law** | The abstract brand guideline. No content, no tagline copy - only rules. Every edit is a brand decision. |
| `reference.md` | pattern library | Catalog of how the brand has been applied in production decks. Supplements DESIGN.md; must never contradict it. |
| `assets/logo/*.svg` + `*.png` | immutable | The **four canonical brand marks**, each provided as SVG (for web/HTML) and PNG at 2x (for PPTX embedding). The only brand graphics permitted anywhere in this project. |

No demo/test decks ship with this repo. When a deck is built (for validation, for the client, for a new offer), it lives in the working directory and is not committed back to this repo. The repo itself is the brand system, not the examples.

## Directory map

```
/Users/rebrained/Documents/Projects/Reeinvent/
├── CLAUDE.md                 ← this file
├── DESIGN.md                 ← the brand law
├── README.md                 ← client-facing install and usage guide
├── SKILL.md                  ← skill manifest for Claude Code / Cowork installs
├── VERSION                   ← semver, bumped on any brand-system edit
├── reference.md              ← pattern library from production decks
├── scripts/
│   └── embed-fonts.py        ← OOXML post-processor, embeds Roboto TTFs into generated .pptx
└── assets/
    ├── logo/                 ← the four canonical brand marks - SVG + PNG pairs
    │   ├── Arrow-Up.svg            ← background watermark arrow (native fill #F5F5F5)
    │   ├── Arrow-Up@2x.png         ← PNG for PPTX embedding
    │   ├── Upwards-Arrow.svg       ← BULLET marker - Core Blue rounded square + white arrow
    │   ├── Upwards-Arrow@2x.png    ← PNG for PPTX embedding
    │   ├── White-Logo.svg          ← WHITE wordmark (fill: #fff) for dark / gradient surfaces
    │   ├── White-Logo@2x.png       ← PNG for PPTX embedding
    │   ├── Gradient-Logo.svg       ← GRADIENT wordmark (#2665E2 → #C26DE6) for light surfaces
    │   └── Gradient-Logo@2x.png    ← PNG for PPTX embedding
    └── fonts/
        └── Roboto/            ← Apache 2.0, shipped for PPTX font embedding
            ├── Roboto-Light.ttf     ← weight 300
            ├── Roboto-Regular.ttf   ← weight 400
            ├── Roboto-Italic.ttf    ← weight 400 italic (pull quotes)
            ├── Roboto-Medium.ttf    ← weight 500
            ├── Roboto-Bold.ttf      ← weight 700
            ├── Roboto-Black.ttf     ← weight 900
            └── LICENSE.txt          ← Apache 2.0
```

**Asset routing by output format:**
- **HTML / web surfaces** → use the `.svg` file. Browsers render SVG natively at any size.
- **PPTX / Google Slides** → use the `@2x.png` file. PPTX and Slides render SVG imports unreliably (missing fills, placeholder rectangles, gradient collapse). PNG embedded via `add_picture()` is universally reliable.
- **PDF via HTML print** → use the `.svg` file (browser handles it).
- **PDF via PPTX export** → use the `@2x.png` file (PPTX is the source).

**The two arrows are not interchangeable.** `Arrow-Up` is the background watermark (used at top-right of cover / divider / closing slides). `Upwards-Arrow` is the bullet marker (used only inside list items). Each has one job.

These four brand marks are the only brand graphics that exist in this project. There are no standalone buttons, icons, lettermarks, or alternate logo files. If a design needs a button, you build it from Roboto + one of the 9 brand colors + optionally the `Arrow-Up` mark next to the label. If a design needs an icon, use one of the arrows or go without.

**Do not inline SVG paths. Do not write CSS replicas. Do not reach for external icon libraries. Do not create new SVG files without explicit user approval. Do not substitute a PNG for an SVG or vice versa outside the routing rule above.**

## The 9 colors - the only colors you may use

| Name | Hex | Role |
|------|-----|------|
| Ink | `#0A1220` | Primary dark background, body text on light |
| Deep Navy | `#1B2848` | Secondary dark surface, top stop of dark gradient |
| Off-White | `#F5F5F5` | Primary light background, body text on dark |
| White | `#FFFFFF` | Headline text on dark, card fills |
| Core Blue | `#2665E2` | Primary accent, CTA fill, 50% stop of Signature Gradient |
| Mid Blue | `#3C74E2` | Secondary accent, chart series 2 |
| Sky Blue | `#6C94E5` | Tints, chart series 3 |
| Core Violet | `#A942EF` | Saturated accent, vivid-gradient endpoint |
| Mid Violet | `#C26DE6` | 50% stop of Signature Gradient, highlights |
| Soft Violet | `#D79BEC` | Delicate tints, chart series 4 |

If you find yourself typing a hex code that is not on this list, stop. There is no 11th color.

## The gradient - one angle, three flavors

| Name | CSS | Purpose |
|------|-----|---------|
| Signature | `linear-gradient(30deg, #2665E2 0%, #C26DE6 100%)` | The brand. Default. |
| Dark | `linear-gradient(30deg, #1B2848 0%, #0A1220 100%)` | Depth on dark sections |
| Vivid | `linear-gradient(30deg, #2665E2 0%, #A942EF 100%)` | Reserved for hero moments |

**All gradients are 30° exactly.** Not 45°, not 135°, not `to bottom right`. Always `30deg` or equivalent.

## Typography - one family, five weights

- Family: **Roboto** (Google Fonts, also built into Google Slides; TTFs shipped at `assets/fonts/Roboto/` for PPTX embedding).
- Weights: **300, 400, 500, 700, 900**, plus **400 italic** (pull quotes only). Nothing else.
- Fallback chain: `Roboto, Arial, sans-serif`. Never Calibri, never Times.

## The Arrow

- Asset: `assets/logo/Arrow-Up.svg` (HTML) / `assets/logo/Arrow-Up@2x.png` (PPTX)
- ViewBox: `0 0 47.27 46.43` (treat as square)
- Native fill: `#F5F5F5`
- Rotations allowed: **0°, 90°, 180°, 270° only**
- **Never horizontally flip.** The notched tail is asymmetric; mirroring produces a broken mark.

## Non-negotiable rules (reject any edit that violates these)

### Color
1. Every hex in every file must be one of the 9 canonical colors.
2. Backgrounds never use `#000000` or `#FFFFFF` - use Ink and Off-White.
3. Blue and violet combine **only through the Signature Gradient**, never as adjacent solid fills.

### Gradient
4. All gradients are 30° exactly.
5. Full-bleed gradient backgrounds are reserved for cover, section divider, and closing slides.

### Type
6. Only Roboto, only weights 300/400/500/700/900 (plus 400 italic for pull quotes).
7. Headlines are 40 pt or larger; body is 18–20 pt; nothing on-screen below 14 pt.
8. Italic is reserved for pull quotes only.

### Underlines (DESIGN.md §8)
9. **One gradient underline per slide - always. No exceptions.**
10. An underline never spans more than one line of text.
11. Never stack gradient treatments (text + underline + highlight) on the same word.

### CTAs / Buttons (DESIGN.md §7)
12. **No SVG button library exists.** If a design needs a CTA, you build it from brand primitives - Roboto 500 label on a Core Blue or Signature Gradient pill, optionally paired with Arrow-Up.svg next to the label.
13. One primary CTA per slide.
14. Never invent a button component in DESIGN.md without user approval. CTAs are minimal by default - the decision to introduce a styled button is a brand decision.
15. Never recolor the Arrow-Up.svg outside documented rules (see Arrow section).
16. The `Upwards-Arrow` mark (Core Blue rounded square with white arrow) is decoration only - it signifies progress/direction, never user action. Never clickable, never a link, never used as a standalone button or CTA.
17. **Button content is always center-aligned horizontally.** Label and optional Arrow form one content block, centered. Button width is intrinsic; padding is symmetric left and right. Never left-pin the label with the arrow pushed right.

### The Arrow (DESIGN.md §4)
18. Rotate only in 90° steps. Never flip.
19. Never stretch or skew. Keep it square.
20. Arrow watermarks sit at 6–10% opacity on dark, 4–6% on light.
21. **Arrow watermarks are always flush with the top and right edges of their container - `top: 0; right: 0;`. Fully visible. Never cropped, never bled off the canvas, never drifted inward from the corner.** One arrow watermark per slide.

### Text contrast by surface (DESIGN.md §2.5)
22. **Default text on dark surfaces is White.** Solid blue (Core Blue, Mid Blue, Sky Blue) as a text fill on Ink, Deep Navy, or any gradient background is **prohibited** - "blue on dark blue" fails contrast.
23. **Gradient text on dark surfaces** is permitted **only for headline-scale text ≥ 40 pt**. Below 40 pt - eyebrows, labels, captions, body - always use White on dark. Gradient decoration (stripes, underlines, highlights) is permitted at any size on any surface.
24. **Default text on light surfaces is Ink.** Gradient text on light is permitted for single-word emphasis per §8 rules.

### Gradient stripe (DESIGN.md §8)
25. **Gradient stripe width = width of the text above it.** Stripes are never fixed-width; they always trace the label they belong to, aligned left with that text.

### Gradient text safety contract (DESIGN.md §8 - absolute)
Every gradient-text element in HTML/web/interactive-PDF surfaces MUST satisfy ALL five:
- `display: inline-block`
- `line-height: 1.4` minimum
- Vertical padding `0.15em` top AND bottom minimum
- Both `color: transparent` AND `-webkit-text-fill-color: transparent`
- **One font-size per element.** Never mix sizes inside a single `background-clip: text` element. Split into separate gradient-text spans, each at its own size.

If any of these cannot be satisfied for a given layout, **fall back to solid Core Blue `#2665E2`** instead of gradient text. Solid color has zero rendering risk.

### Bullet lists (DESIGN.md §7)
26. **Bullet marker is always `assets/logo/Upwards-Arrow.svg` (HTML) or `assets/logo/Upwards-Arrow@2x.png` (PPTX).** No dots, dashes, checkmarks, CSS-drawn rounded-squares, or pseudo-elements. One marker, period.
27. **One line per bullet item - always.** No wrapping to two lines, ever. Enforce with `white-space: nowrap`. If an item doesn't fit, rewrite it tighter or split into two bullets.
28. **Copy in bullets is scan-ready, not sentence-form.** Short noun phrases or verb phrases. Tight. Every item in one list shares the same grammatical shape.
29. **Max 6 items per bullet list.** Past six, the reader skips. Split into two lists or switch layout.

### Layout (DESIGN.md §9)
30. **Sparse content slides anchor content to the bottom.** When a slide has a header (eyebrow + title) plus one content block (card row / bullets / image), the content block sits at the bottom of the safe area, not the top. Top-anchored content with empty space below is a brand violation. In CSS: use `align-items: end` on `grid-template-rows: auto 1fr` layouts, not `start`.

### Text hygiene
31. **Never use the em-dash character (Unicode U+2014) in any text.** Not in docs, not in decks, not in HTML, not in filenames, not in commit messages, not in conversational responses. Replace with hyphen (`-`), colon (`:`), semicolon (`;`), or a full stop. This rule applies to every file and every piece of writing in this project, including the rule text itself - the glyph does not appear in CLAUDE.md or DESIGN.md.

### Content
32. This project's files contain **no Reeinvent copy**. All demo text is generic placeholder. Do not import taglines, case-study text, or service descriptions from the reference PDFs.

## Traps you will fall into if you aren't careful

Claude makes these mistakes by default. Pre-empt them.

1. **Guessing colors.** Never type a hex from memory. Refer to the 9-color table.
2. **Inventing SVG content.** Only four brand marks exist (each with SVG + PNG variant). Do not inline SVG `<path>` data, do not create icons, do not draw shapes as data-URIs. If a visual needs a mark, it is Arrow-Up, Upwards-Arrow, White-Logo, or Gradient-Logo - nothing else.
3. **Redrawing in CSS.** No CSS-drawn icons, no `clip-path` arrows, no pseudo-element chevrons. Typography + colors + the three SVGs only.
4. **Horizontal gradients.** The default CSS tutorial uses `to right`. Override that reflex. `30deg` always.
5. **Arrow flipping with `transform: scaleX(-1)`.** Never. Rotate only.
6. **Stacking text emphasis.** Underline + bold + gradient-text all at once looks "premium" but is a violation. Pick one.
7. **Extending rules unasked.** The user's last request said six things - don't add a seventh because it "feels consistent." Ask.
8. **Pulling copy from reference decks.** The reference PDFs are for layout only. Never extract taglines, headlines, or body text.
9. **Creating documentation or asset files.** No new `*.md` or `*.svg` files unless the user explicitly asks.
10. **Inventing a component.** New components must be proposed to the user, added to DESIGN.md §7, and only then used in demos.

## How to handle common requests

### "Create a test layout / deck / slide"
1. Identify the archetype from `reference.md` (A1–A10) or the DESIGN.md template (§6).
2. Use only the 9 colors, the 3 gradients, Roboto, and the SVG assets.
3. Populate with generic placeholders (`Headline`, `Service Name`, `Audience One`).
4. Invoke **`normalize`** to verify DESIGN.md compliance, then run the pre-flight checklist, before responding "done."

### "Add a new rule / change a rule"
1. Read the existing section in DESIGN.md.
2. Draft the new or modified rule in plain language and propose to the user.
3. Confirm.
4. Edit DESIGN.md.
5. Update the current working deck (whatever HTML / PPTX file is live in the working directory) to comply.

### "Add a new component"
1. Do not skip straight to code.
2. Propose the spec: shape, radius, colors, typography, use cases, do/don't.
3. Confirm with the user.
4. Add to DESIGN.md §7.
5. Then use it in demos.

### "Fix a demo"
1. If the user sent a screenshot, invoke **`critique`** first for a structured assessment.
2. Identify which DESIGN.md rule the current rendering violates.
3. Quote the rule.
4. Make the minimal edit that brings the demo into compliance.
5. Invoke **`normalize`** to verify the fix didn't introduce a new violation elsewhere.

### "Export / convert to PPTX or PDF"
- HTML decks should include `@media print` rules (flatten slides to full-page layout) so browser print-to-PDF produces a clean deck.
- For real `.pptx` output, invoke the **`anthropic-skills:pptx`** skill.
- For PDF reads/exports, invoke the **`anthropic-skills:pdf`** skill.
- DESIGN.md §12 documents the export settings presenters follow.

## Available skills

Six specialized skills are installed. When a request matches one of these triggers, **invoke the skill via the Skill tool first** instead of doing the work by hand. These are pre-built capabilities - they do the job faster and more reliably than ad-hoc effort.

### `anthropic-skills:pptx` - PowerPoint file handling
**Trigger**: any request involving a `.pptx` file - creating, reading, editing, extracting content, combining, or generating a deck from the rules in DESIGN.md.
**Invoke when the user says**: "make a .pptx", "convert this deck to PowerPoint", "open the master deck", "extract the slides from [file].pptx", "build a deck matching our system as a .pptx file".

### `anthropic-skills:pdf` - PDF file handling
**Trigger**: any request involving a `.pdf` - reading reference decks, extracting text / tables / images, merging exports, running OCR, exporting the pitch deck to PDF.
**Invoke when the user says**: "read the reference deck", "extract the brand guide's typography", "export the pitch deck to PDF", "merge these PDFs", "what does the 2-pager look like?".

### `normalize` - design-system compliance audit
**Trigger**: checking whether something complies with DESIGN.md. This is this project's core loop - use liberally.
**Invoke when the user says**: "is this on brand?", "does this follow the rules?", "clean this up to match the system", "audit against DESIGN.md", or when you finish a non-trivial demo edit and want to self-verify before responding "done".

### `polish` - pre-ship quality pass
**Trigger**: catching alignment, spacing, and micro-detail issues before a deck ships. Run after substantive edits, always run before the user takes the deck to a real audience.
**Invoke when the user says**: "polish this", "final pass", "getting ready to ship", "last tune-up", or when you're about to respond "done" on a deck that will be presented externally.

### `critique` - UX / visual design review
**Trigger**: structured design feedback. Use when the user sends a screenshot, says something looks "off," or asks "what's wrong here?".
**Invoke when the user says**: "review this slide", "this looks wrong", "what's off about this?", or sends a screenshot of a working deck asking for feedback. **Run `critique` before `polish`** when both could apply - critique identifies problems, polish fixes finish details.

### `audit` - technical quality check
**Trigger**: accessibility, responsive behavior, and anti-pattern checks before a deck is exported to PDF or sent externally.
**Invoke when the user says**: "is this accessible?", "run an audit", "WCAG check", "responsive test", or before any PDF export that will be distributed beyond internal review.

### Skill invocation notes
- Use the `Skill` tool with the exact skill name (including the `anthropic-skills:` prefix for `pptx` and `pdf`).
- When multiple skills could apply, pick the most specific first - e.g., a screenshot of a slide with spacing issues → `critique` first, then `polish`.
- When in doubt whether a skill applies, **run it**. Cost of invoking a skill is low; cost of hand-rolling work a skill would have done better is high.
- Never mention a skill name without invoking it.

## Pre-flight checklist (run before saying "done")

Use this against every demo edit, every new slide, every component addition:

- [ ] Every hex in the edit is one of the 9 canonical colors.
- [ ] Every gradient is `30deg`.
- [ ] The Arrow is 0°/90°/180°/270° rotation - not flipped.
- [ ] No inline SVG paths, no data-URI SVGs, no CSS-drawn icons anywhere in the file.
- [ ] Every `<img src>` points to one of the three files in `assets/logo/`.
- [ ] Arrow watermarks sit flush at `top: 0; right: 0;` - fully visible, never cropped, never bleeding off the canvas.
- [ ] Font family is Roboto with weights only from {300, 400, 500, 700, 900}, plus 400 italic for pull quotes.
- [ ] No `#000000` or `#FFFFFF` as a section/slide background.
- [ ] At most **one** gradient underline per slide.
- [ ] At most **one** primary CTA per slide.
- [ ] No gradient stacking on the same word.
- [ ] **Text under 40 pt on dark surfaces is White, never gradient, never solid blue.**
- [ ] **Gradient stripes under eyebrows match the text width exactly** - not fixed-width.
- [ ] **Button content is center-aligned horizontally.**
- [ ] **Bullet lists use `Upwards-Arrow.svg` (HTML) or `Upwards-Arrow@2x.png` (PPTX) as the marker** - no substitutes.
- [ ] **PPTX embeds PNG (`@2x.png`) brand assets, never SVG.** HTML surfaces use SVG.
- [ ] **Every generated `.pptx` has been run through `python scripts/embed-fonts.py`** and contains six `ppt/fonts/*.fntdata` entries (verify with `unzip -l FILE.pptx | grep fntdata`). No embedded fonts means the deck falls back to Arial on client machines - a brand violation.
- [ ] **Every bullet item fits on one line** (`white-space: nowrap` in HTML; tight copy in PPTX).
- [ ] **Sparse slides anchor content to the bottom**, not the top. No card row floats at the top with empty space below.
- [ ] **Zero em-dash characters (Unicode U+2014) anywhere in the file.** Verify with `grep -P '\x{2014}' FILE` returning empty.
- [ ] **Every `background-clip: text` element satisfies the safety contract**: `display: inline-block` + `line-height: 1.4` min + `0.15em` vertical padding min + both `color: transparent` and `-webkit-text-fill-color: transparent` + single font-size per element.
- [ ] Placeholder text is generic - no real Reeinvent copy.
- [ ] If DESIGN.md was edited, the demo still complies with the rest of DESIGN.md.

If any box is unchecked, fix before responding.

## Ask before you act

The user has said explicitly: consult them before changes that affect the brand rules. That means:

- **Ask** before adding a new rule to DESIGN.md.
- **Ask** before removing or relaxing an existing rule.
- **Ask** before introducing a new component.
- **Ask** before pulling any text from reference material.
- **Ask** before creating a new top-level file.

When the user's instruction is ambiguous (e.g., "fix it," "tighten the rule," "use all rules"), paraphrase your understanding in one or two sentences and confirm before editing.

## When blocked mid-task

If a chosen path fails mid-execution, stop and surface. This applies to:

- **Tool failure** - a command returns non-zero, a script throws, a library is missing.
- **Permission denied** at the OS level - automation, file access, network.
- **Required input missing** - the working deck isn't where you expected, a referenced asset doesn't exist.
- **Output contract can't be met** - a DESIGN.md rule can't be satisfied with the current approach.

**Required action:** halt. Report the block in one sentence. Lay out available alternatives ranked by brand fidelity. Wait for the user to pick.

**Prohibited:** silently switching engines, substituting a different output format, rasterizing, simplifying "because it's close enough," removing the blocked element, or continuing with a partial result. Switching strategy under a block is a decision - decisions are the user's.

## Tone when responding

- State what you changed and why, not what the change "feels like."
- When a rule is invoked, cite it (e.g., *"DESIGN.md §8 rule 9: one underline per slide"*).
- Keep end-of-turn summaries to one or two sentences.
- No victory laps. No adjectives like "beautiful," "stunning," "sleek." The work speaks.

## When in doubt

Stop. Re-read DESIGN.md. If the answer isn't there, ask. The user's trust in this brand system is measured in the absence of mistakes, not the presence of features.
