# Reeinvent Pitch Deck Designer

A Claude-installable plugin that helps you build **premium Reeinvent pitch decks** from the production master deck. The skill clones the master, lets Claude swap text per prospect, and hands you a brand-perfect editable PPTX.

The plugin also carries the brand law (DESIGN.md, CLAUDE.md, reference.md, four brand marks, six Roboto weights) so any HTML, slide, or surface Claude builds for Reeinvent stays on-brand.

---

## Two paths

The skill supports two workflows. **Path A is canonical for any client-facing deck.** Path B is a fast skeleton tool for internal drafts.

| Path | What it does | When to use |
|------|--------------|-------------|
| **A: Clone the master** | Duplicate the production master deck, edit text via Claude, you delete unused slides in PowerPoint. Layout, photography, bespoke typography all preserved from the human-designed master. | Every client-facing deck. The default. |
| **B: Generate from JSON spec** | Code-driven generator builds a brand-correct skeleton from a JSON spec. Theme colors, fonts, gradients, native shapes - but no premium photography or bespoke layouts. | Internal drafts only. Throwaway demos. The user explicitly asks for a "skeleton" or "rough cut". |

If you ship Path B output to a paying client without running it through Path A polish, you will not be happy with the result. Don't.

---

## What you need

- **Claude Code**, **Claude Desktop**, or **Cowork** (any version that supports plugins, v2.0+).
- A logged-in Anthropic account.
- **Python 3.10+** for the optional Path B skeleton generator. The bootstrap creates its own venv on first use; no manual `pip install`.
- **One copy of the Reeinvent master deck** at a known location (see "First-time setup" below). Path A cannot work without it.

---

## Install

How you install depends on which Claude surface you use. All three install the same plugin.

### Claude Code (terminal) and Cowork

```
/plugin marketplace add rebrained-de/Reeinvent-Pitch-Deck-Designer
/plugin install reeinvent-pitch-deck-design@reeinvent-brand-system
```

### Claude Desktop (app)

The `/plugin` slash commands do not work in Desktop's chat input. Install via the GUI:

1. Open **Settings -> Code -> Plugins** in the Desktop app.
2. Add the marketplace: `rebrained-de/Reeinvent-Pitch-Deck-Designer`.
3. Install the `reeinvent-pitch-deck-design` plugin from the list.

### Verify the install

Ask Claude: *"What brand system is active, and what version?"* — it should report the Reeinvent Pitch Deck Design plugin and a version matching the current `VERSION` file.

---

## First-time setup (required for Path A)

Drop the master deck at a stable location so the skill auto-finds it:

```bash
mkdir -p ~/Reeinvent/Templates
mv ~/Downloads/"REE 2.0 – Master Company Presentation.pptx" ~/Reeinvent/Templates/
# Optionally also the slim variant:
mv ~/Downloads/"REE 2.0 – Slim Company Presentation.pptx" ~/Reeinvent/Templates/
```

The skill auto-detects the master via this priority order:
1. `REEINVENT_MASTER_DECK` env var (single file path)
2. `REEINVENT_TEMPLATES_DIR` env var (directory)
3. `~/Reeinvent/Templates/`
4. `~/Documents/Reeinvent/Templates/`
5. `~/Downloads/REE 2.0 *Master* Presentation.pptx` (fallback only)

If you do not have the master deck, ask Asja for the latest copy. The masters are not bundled with this repo (165 MB exceeds GitHub's per-file limit; they also contain client-confidential material).

---

## Usage

Once installed and the master is in place, just talk to Claude.

### Example prompts (Path A)

> **"Build me a 10-slide pitch deck for Northwind. Use slides 1-3 of the master, then service detail (Concept Sprint and Investor Demo) tailored to their pricing-engine use case, then the Alva success story but with placeholder metrics, plus contact and closing."**

Claude will:
1. Clone the master (`bin/reeinvent-clone-master`) into your cwd.
2. Inspect every slide to map current text -> proposed replacement.
3. Show you the replacement map for confirmation.
4. Apply replacements via `bin/reeinvent-deck replace`.
5. Re-inspect to verify.
6. Tell you which slides to delete in PowerPoint manually.
7. Open the result.

### Example prompts (Path B, skeleton)

> **"Give me a quick skeleton 4-slide deck for an internal review. Cover, two stats, closing."**

Claude switches to Path B, writes a JSON spec, runs the generator. Brand-correct skeleton. You polish manually if it ever becomes external-facing.

### Other things to ask Claude

> **"Review this slide against the Reeinvent master."** (paste a screenshot)

> **"Inspect the master deck and tell me every service-detail slide that exists."**

> **"What's the URL convention for service slides? Pull it from the master."**

---

## What's inside the plugin

```
skills/reeinvent-pitch-deck-design/
  SKILL.md                    skill manifest, two-path workflow
  CLAUDE.md                   brand rules and operating manual
  DESIGN.md                   brand guideline (simplified summary; master is ground truth)
  reference.md                production slide archetypes catalogued
  templates/README.md         where the master deck must live (first-time setup)
  bin/
    reeinvent-clone-master    clone the production master, open in PowerPoint
    reeinvent-deck            inspect / replace / build / verify / embed (CLI)
  generator/                  Path B skeleton generator (Python package + tests + examples)
  scripts/
    embed-fonts.py            standalone font embed (back-compat)
    render-pdf.py             HTML deck -> vector PDF via headless Chrome
  assets/
    logo/                     four primary brand marks (SVG + PNG @2x)
    fonts/Roboto/             six TTFs (Apache 2.0)
```

The full Reeinvent brand kit (Brand Guidelines PDF + button library) lives separately in your local `~/Reeinvent/Brand-Kit/` if Asja has shared it. The skill does not bundle it.

---

## Updating

```
/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system
```

The bootstrap rebuilds Python deps automatically when needed. The master deck is updated separately (drop a new copy into `~/Reeinvent/Templates/` overwriting the old one).

---

## Manual install (offline, no marketplace)

```bash
git clone https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer.git
mkdir -p ~/.claude/skills
cp -R Reeinvent-Pitch-Deck-Designer/skills/reeinvent-pitch-deck-design ~/.claude/skills/
```

Then drop the master deck into `~/Reeinvent/Templates/` per "First-time setup" above.

---

## CLI reference (for scripted use)

```bash
# Clone the production master deck (auto-locates)
bin/reeinvent-clone-master -o my-deck.pptx [--variant master|slim|two-pager] [--no-open]

# List every text shape on every slide of any deck
bin/reeinvent-deck inspect deck.pptx [--json]

# Apply text replacements from a {old: new} JSON map
bin/reeinvent-deck replace deck.pptx replacements.json [-o output.pptx] [--slides 1,2,4]

# Path B: build a skeleton deck from a JSON spec
bin/reeinvent-deck build spec.json -o deck.pptx

# Run brand pre-flight checks on any deck
bin/reeinvent-deck verify deck.pptx

# Inject Roboto font embedding into any existing deck
bin/reeinvent-deck embed deck.pptx
```

---

## Common questions

**Why isn't the generator the canonical workflow?**
The Reeinvent master deck is built by a human designer with bespoke layouts (mega-display "AI-DRIVEN" titles, laptop+screenshot mockup clusters, partner-brand alliance colors) that no algorithm replicates without significant custom photography and per-slide judgment. v3.0.0 attempted code generation as the canonical path; it produced brand-shaped output but not Reeinvent-quality output. Path A clones the actual master, which already has all the design judgment baked in.

**Can I edit the generated/cloned deck after Claude finishes?**
Yes. Every shape and text frame remains editable in PowerPoint, Keynote, and Google Slides.

**The master deck doesn't have a slide I need.**
Tell Asja. New slide patterns get added to the master, then they're available in every Path A clone.

**What if something looks off in the output?**
Send the screenshot. Path A output should look identical to the master except for swapped text; if it doesn't, the replacement broke a paragraph's run structure (rare but fixable).

---

## Support

Questions, bug reports, or new slide-pattern requests: contact your Rebrained account lead.

---

## Credits

Roboto fonts (`assets/fonts/Roboto/`) are bundled under the Apache License 2.0, copyright Google. See `assets/fonts/Roboto/LICENSE.txt`.
