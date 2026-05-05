# Reeinvent Pitch Deck Designer

A Claude-installable plugin that builds **brand-perfect Reeinvent PPTX decks**. One command turns a JSON spec into an editable PowerPoint file with theme colors, embedded Roboto, native shapes, gradient text on stat numbers, and every brand rule from the Reeinvent design system already applied.

The same plugin also carries the brand law (DESIGN.md, CLAUDE.md, reference.md, four brand marks, six Roboto weights) so any HTML, slide, or surface Claude builds for Reeinvent stays on-brand without extra prompting.

---

## What you need

- **Claude Code**, **Claude Desktop**, or **Cowork** (any version that supports plugins, v2.0+).
- A logged-in Anthropic account.
- **Python 3.10+** on your machine. The generator's bootstrap creates its own virtualenv, so you don't need to install `python-pptx` yourself.

That's it. No manual `pip install`, no separate companion skills.

---

## Install

How you install depends on which Claude surface you use. All three install the same plugin.

### Claude Code (terminal) and Cowork

In the terminal, paste:

```
/plugin marketplace add rebrained-de/Reeinvent-Pitch-Deck-Designer
```

Then install the plugin:

```
/plugin install reeinvent-pitch-deck-design@reeinvent-brand-system
```

### Claude Desktop (app)

The `/plugin` slash commands do **not** work in Desktop's chat input. Install via the GUI:

1. Open **Settings -> Code -> Plugins** in the Desktop app.
2. Add the marketplace: `rebrained-de/Reeinvent-Pitch-Deck-Designer`.
3. Install the `reeinvent-pitch-deck-design` plugin from the list.

### Verify the install

Ask Claude:

> "What brand system is active, and what version?"

Claude should confirm it's running the Reeinvent Pitch Deck Design plugin and report a version matching the current `VERSION` file. If it says "outdated" or "not found," re-run the install.

---

## Usage

Once installed, the plugin loads automatically when you ask Claude to do anything Reeinvent-branded. Just talk to Claude.

### Example prompts

> **"Build me a 12-slide pitch deck for our AI-readiness offering. Use the brand system."**

Claude writes a JSON spec (one entry per slide, picking the right archetype), runs the generator, and hands you a `.pptx`. Open in PowerPoint, Keynote, or Google Slides; everything is editable.

> **"Create a cover slide titled 'From ideas to scalable AI in weeks' with 'in weeks' highlighted."**

> **"Make a stat slide: 6 weeks, label 'AVG. IDEA TO PROD'."**

> **"Build a contact slide with our three offices (Sarajevo, Vienna, Berlin)."**

> **"Review this deck against DESIGN.md and tell me what's off."**

> **"Show me the 12 archetypes I can use."**

### What the generator gives you

Every slide is built from one of 12 archetypes (DESIGN.md section 6 + reference.md A1-A6):

| Archetype | When to use |
|-----------|-------------|
| `cover` | Opening slide |
| `section_divider` | Chapter break |
| `intro_split` | Deck introduction (50/50 photo + Ink) |
| `agenda` | Table of contents |
| `content` | Single-column body or bullet list |
| `two_column` | 50/50 text + card |
| `stat` | Big-number slide (gradient text on the number) |
| `three_up` | Three white cards across the bottom |
| `service_detail` | Per-offer template (sidebar + included list + mockup placeholder) |
| `success_story` | Case study (CHALLENGE / SOLUTION / RESULTS) |
| `quote` | Pull quote |
| `closing` | Call-to-action / Thank You |

Every output `.pptx` includes:
- All 9 brand colors registered as Theme Colors (re-skin the whole deck from one panel).
- Roboto embedded as 6 weights (font travels with the file).
- Native shapes and live editable text (no rasterized slides).
- Gradient text fill on stat numbers and headlines >= 40 pt.
- `normAutofit` on cards (text shrinks within fixed geometry).
- Brand stamp, arrow watermarks, gradient stripes, gradient pills, chat bubbles, arrow bullet markers (all native).

---

## What's inside the plugin

```
skills/reeinvent-pitch-deck-design/
  SKILL.md           - skill manifest, auto-invoked on Reeinvent triggers
  CLAUDE.md          - 32 non-negotiable brand rules + pre-flight checklist
  DESIGN.md          - full brand law (colors, gradients, type, layout)
  reference.md       - 10 production slide archetypes from real decks
  bin/
    reeinvent-deck   - bash wrapper. Auto-bootstraps Python venv, runs generator.
  generator/
    reeinvent_pitch_deck/   - Python package: theme, master, builders, verify
    examples/               - reeinvent-full.json (12-slide reference deck)
    tests/                  - 19 tests covering spec validation + every brand rule
  scripts/
    embed-fonts.py   - thin wrapper around the generator's font embed (back-compat)
    render-pdf.py    - HTML deck -> vector PDF via headless Chrome
  assets/
    logo/            - 4 brand marks (SVG for HTML, PNG for PPTX)
    fonts/Roboto/    - 6 TTFs (Apache 2.0)
```

The `.venv` directory is created on first generator run inside the skill folder; ignored by git.

---

## Updating

### Plugin install

```
/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system
```

The bootstrap script automatically rebuilds the Python venv if `requirements.txt` changed; no manual step required.

### Manual install

`git pull` in the cloned folder, then re-copy:

```bash
cp -R ~/Documents/Reeinvent-Brand/skills/reeinvent-pitch-deck-design ~/.claude/skills/
```

Claude checks for updates the first time you ask for a Reeinvent surface in a session: if your local copy is behind GitHub, it will tell you in one line and wait.

---

## Manual fallback (offline / no plugin marketplace)

For air-gapped environments. Same end result, more steps.

```bash
git clone https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer.git
mkdir -p ~/.claude/skills
cp -R Reeinvent-Pitch-Deck-Designer/skills/reeinvent-pitch-deck-design ~/.claude/skills/
```

Then ask Claude as you normally would. The bootstrap script discovers itself relative to where you copied it.

---

## Generating a deck without Claude (advanced)

If you want to drive the generator from a script or CI, skip Claude entirely:

```bash
# Write a spec
cat > deck.json <<'EOF'
{
  "title": "My Deck",
  "slides": [
    {"archetype": "cover", "title": "From ideas to scalable AI", "highlight_words": ["scalable AI"]},
    {"archetype": "stat", "number": "6 wk", "label": "AVG. IDEA TO PROD"},
    {"archetype": "closing", "message": "Let's build it.", "cta_label": "Book a call"}
  ]
}
EOF

# Build (auto-bootstraps the venv on first call)
~/.claude/skills/reeinvent-pitch-deck-design/bin/reeinvent-deck build deck.json -o deck.pptx
```

The full spec schema lives in `generator/reeinvent_pitch_deck/spec.py`. Reference deck: `generator/examples/reeinvent-full.json`.

---

## Common questions

**Do I need to tell Claude about the brand every time?**
No. The plugin loads automatically whenever Claude touches a Reeinvent surface.

**Can I edit the generated deck?**
Yes. Every slide is fully editable in PowerPoint, Keynote, and Google Slides. Theme colors propagate via the master, so a global re-skin is one panel away.

**The generator doesn't have an archetype I need.**
Tell Claude what's missing. We add new archetypes by editing `generator/reeinvent_pitch_deck/builders/`. Brand-system additions follow propose-then-confirm.

**Can I use this without Claude?**
Yes - see "Generating a deck without Claude" above. The generator is a regular Python package.

**What if something looks off in the output?**
Send the screenshot to your Rebrained contact. Every rendering edge case is treated as a bug in the generator, not a content issue. The fix lives in code, not in your spec.

---

## Support

Questions, bug reports, or requests for new slide patterns: contact your Rebrained account lead.

---

## Credits

Roboto fonts (`assets/fonts/Roboto/`) are bundled under the Apache License 2.0, copyright Google. See `assets/fonts/Roboto/LICENSE.txt` for the full license text.
