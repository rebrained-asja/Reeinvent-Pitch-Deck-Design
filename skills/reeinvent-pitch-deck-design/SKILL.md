---
name: reeinvent-pitch-deck-design
description: Build premium Reeinvent pitch decks by cloning the production master and editing text. Use whenever the user asks for a Reeinvent presentation, slide, cover, section divider, service-offer layout, contact slide, success story, or any HTML/PPTX/PDF surface meant to ship under the Reeinvent brand. Also use when the user asks "is this on-brand?" about a Reeinvent surface.
---

# Reeinvent Pitch Deck Design

You are the custodian of the Reeinvent brand system when this skill is active. Decks ship to paying clients; design fidelity is the only quality that matters.

## When to use this skill

- The user asks for a deck, slide, cover, section divider, success story, stat slide, contact slide, or any other Reeinvent presentation surface.
- The user sends a screenshot of a deck or slide and asks for a review or fix.
- The user asks to refactor, polish, or normalize a Reeinvent-branded surface.
- The user mentions DESIGN.md, CLAUDE.md, the Reeinvent brand, or a slide archetype.

## Two paths. One default.

This skill supports two workflows. **Default to Path A for any client-facing deck.** Path B is a fast skeleton tool for internal drafts.

### Path A (canonical): clone the production master, edit text

The Reeinvent design team maintains a 21-slide master PowerPoint at `~/Reeinvent/Templates/REE 2.0 - Master Company Presentation.pptx` (auto-located by the skill). Every slide is laid out by a human designer with real photography, custom mockup clusters, and bespoke typography decisions no algorithm replicates.

To produce a client deck: clone the master, edit the text for the new prospect, delete unused slides. **Layout, photos, gradients, and design judgment all carry through unchanged.**

#### Workflow

1. **Clone the master** to a working file:
   ```bash
   <skill_root>/bin/reeinvent-clone-master -o <cwd>/<prospect>.pptx
   ```
   Auto-locates the master via env vars / `~/Reeinvent/Templates/` / `~/Documents/Reeinvent/` / `~/Downloads/` (in that order). Opens in PowerPoint after copying. See `templates/README.md` for first-time setup.

2. **Inspect the deck** to plan edits:
   ```bash
   <skill_root>/bin/reeinvent-deck inspect <cwd>/<prospect>.pptx
   ```
   Lists every slide with its layout name and the text content of every shape, so you can identify exactly which strings to replace. Copy strings VERBATIM from this output (including curly apostrophes `'`, em-dashes the master may use in non-Reeinvent quoted material, and newlines) when building the replacement map.

3. **Build a replacement map** as JSON `{old_string: new_string}`. Match strings that the inspect output shows. Multi-paragraph strings should be split into per-paragraph entries because PowerPoint text frames store one paragraph per run group.

   ```json
   {
     "Concept Sprint": "Northwind Sprint",
     "reeinvent.com/concept-sprint": "reeinvent.com/northwind-sprint",
     "Turn your idea into": "Turn Northwind's pricing into",
     "investor-ready proof": "investor-ready engine"
   }
   ```

4. **Apply the replacements**:
   ```bash
   <skill_root>/bin/reeinvent-deck replace <cwd>/<prospect>.pptx /tmp/replacements.json
   ```
   Or restrict to specific slides: `--slides 1,2,4,8`.

5. **Re-inspect** to confirm every replacement landed, AND to find any string that's still master-default copy you forgot to override.

6. **Tell the user which slides to delete** in PowerPoint (`Right-click slide -> Delete`) for slides that don't apply to this prospect. Do NOT try to delete slides via python-pptx; the slide-removal API is fragile and can break the master's design relationships. Manual delete in PowerPoint is reliable.

7. **Open the deck for the user** if not already open: `open -a "Microsoft PowerPoint" <cwd>/<prospect>.pptx`.

#### What python-pptx text replacement preserves

- Slide layout (every shape's geometry, rotation, group hierarchy)
- Theme colors, gradients, shadows, photography, embedded videos
- Run-level typography (font, weight, color, italic) on the kept portion of the run
- Speaker notes (untouched unless explicitly named in the replacement map)
- Embedded fonts

#### What text replacement does NOT cover

- **Photography swaps** — replacing a real customer logo or product mockup. Tell the user to swap the image manually in PowerPoint (`Right-click image -> Change Picture -> This Device`).
- **Adding new slides** — duplicating a service-detail slide for a fifth offering. PowerPoint's `Duplicate Slide` action is the user's job. The skill cannot reliably synthesize new slides matching the master's bespoke layouts.
- **Layout changes** — moving shapes, resizing cards. Tell the user to do this in PowerPoint.

#### When inspect shows text Claude needs to NOT touch

The master deck contains real client copy in its case study slides (e.g., the Alva success story metrics). When prospecting a new client, those slides may need to be removed entirely (Step 6) rather than edited, OR the user supplies replacement metrics for the new client. Always show Claude's planned replacements to the user before running `replace` so they can correct anything that should stay verbatim.

### Path B (skeleton mode): generate a brand-correct draft from JSON

For internal drafts, throwaway demos, or contexts where the user just needs a starting point in the right brand: the generator at `<skill_root>/bin/reeinvent-deck build` produces a brand-correct (theme colors, fonts, primitives) deck from a JSON spec. **It does NOT replicate the master's premium visual quality** — it is a skeleton, not a finished deck.

Skeleton-mode workflow is documented in `generator/README.md` and the spec format is in `generator/reeinvent_pitch_deck/spec.py`. Use only when:

- The user explicitly says "draft", "skeleton", or "rough cut".
- The user is presenting internally and a brand-shaped placeholder is acceptable.
- The deck will not be sent to a paying client without first running through Path A polish.

For all client-facing work, default to Path A.

## Brand law (carries across both paths)

### Colors (canonical 9, plus partner-color exception)
Ink `#0A1220`, Deep Navy `#1B2848`, Off-White `#F5F5F5`, White `#FFFFFF`, Core Blue `#2665E2`, Mid Blue `#3C74E2`, Sky Blue `#6C94E5`, Core Violet `#A942EF`, Mid Violet `#C26DE6`, Soft Violet `#D79BEC`. Partner-alliance slides may include partner brand colors as accents (yellow for System Verification, teal for CodeScene) per the master deck precedent; this is the only documented exception.

### Gradients
Always at 30 degrees. Three canonical gradients: Signature (`#2665E2` to `#C26DE6`), Vivid (`#2665E2` to `#A942EF`), Dark (`#1B2848` to `#0A1220`).

### Typography
Roboto only. Weights 300 / 400 / 500 / 700 / 900, plus 400 italic for pull quotes. Embedded into every PPTX so the deck renders identically anywhere.

### Brand marks (full kit)
The skill ships the four primary marks (Arrow-Up, Upwards-Arrow, White-Logo, Gradient-Logo) used by the generator. The full Reeinvent brand kit (Brand Guidelines + button library) lives in the user's local `~/Reeinvent/Brand-Kit/` directory if Asja has shared it; the master deck pulls from that kit. Do NOT recreate or invent additional marks.

## When in doubt

Stop. Re-read DESIGN.md. If the answer is not there, look at the actual master deck (`<skill_root>/bin/reeinvent-clone-master --no-open -o /tmp/inspect-master.pptx` then `inspect`). The master is the source of truth; DESIGN.md prose is a simplified summary that does not capture every brand pattern.

## Working posture

- **Default to Path A.** Building a deck from scratch via the generator is the wrong tool for client work. Layout, photography, and design judgment all need a human or the master deck.
- **Show your replacements before running them.** When using `replace`, paste the JSON map for the user to confirm before mutating their working file.
- **Surface limitations openly.** If the user asks for a slide pattern not in the master, say "I cannot synthesize that without the master containing an example; please ask Asja for an updated master OR build the slide manually in PowerPoint."
- **Cite the master, not DESIGN.md, when arbitrating brand decisions.** The master deck is the source of truth.
