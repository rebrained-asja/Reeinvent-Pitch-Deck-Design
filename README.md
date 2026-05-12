# Reeinvent Pitch Deck Design System

Your AI-assisted brand kit for building Reeinvent-style presentations. Once installed, every slide Claude helps you build will automatically follow the Reeinvent brand rules: colors, typography, logo placement, gradient usage, and layout.

---

## What you need

- A Claude account with **Skills** enabled (Claude Desktop, Cowork, or claude.ai).
- The ZIP file your Rebrained contact sent you.

That's it.

---

## Install

1. Get the ZIP from your Rebrained contact: `reeinvent-pitch-deck-design-X.Y.Z.zip`.
2. In Claude, open **Settings → Capabilities → Skills**.
3. Click **Create skill** and upload the ZIP.
4. Restart Claude once.

Done. The brand rules now apply in every chat, in any project.

**To update later:** you'll get a new ZIP. Delete the old `reeinvent-pitch-deck-design` entry in Skills, upload the new one. Two clicks.

**If you don't see a Skills panel:** your account doesn't have Skills enabled yet - tell your Rebrained contact.

### Verify it works

In any chat, ask:

> "What brand system is active, and what version?"

Claude should reply `reeinvent-pitch-deck-design` and the version on the ZIP. If it doesn't, re-upload.

---

## How to use it

Once installed, just talk to Claude. The brand rules load automatically.

### Example prompts to try

> **"Build me a 10-slide pitch deck for [your topic]. Follow our brand system."**

> **"Create a cover slide for a deck titled '[your title]'."**

> **"Review this slide layout against DESIGN.md and tell me what's off."**

> **"Make a service-detail slide for our new offer called [offer name]. Use the A5 archetype from reference.md."**

> **"Build a contact slide with our three office cities."**

> **"Show me the four slide archetypes I can use for a sales deck."**

Claude knows the full brand system automatically: the 9 canonical colors, the 30-degree gradient, Roboto typography, the four brand marks (each with SVG for HTML and PNG for PPTX), the slide archetypes (cover, section divider, service detail, success story, stat, contact, closing), and every layout rule.

---

## What's inside the plugin

The brand-system files live at `skills/reeinvent-pitch-deck-design/` inside the plugin:

- **SKILL.md** - Skill manifest. Claude invokes it automatically when you work on a Reeinvent surface.
- **CLAUDE.md** - The operating manual for Claude. The 32 non-negotiable rules and the pre-flight checklist.
- **DESIGN.md** - The complete brand guideline. Every rule Claude follows.
- **reference.md** - Slide archetypes distilled from real Reeinvent presentations.
- **assets/logo/** - The four brand marks, each as SVG (for HTML / web) and PNG at 2x (for PPTX / Slides embedding).
- **assets/fonts/Roboto/** - Roboto TTFs (Apache 2.0), auto-embedded into every generated `.pptx`.
- **scripts/embed-fonts.py** - PPTX post-processor that embeds Roboto into output decks.
- **scripts/render-pdf.py** - HTML deck → vector PDF via headless Chrome. Use for client-distributed PDFs so SVGs and gradients stay vector instead of getting downsampled by the PPTX → PDF route.

Distribution metadata at the repo root: `README.md`, `CHANGELOG.md`, `VERSION`, `.claude-plugin/`.

---

## If something's not right

- **Claude wrote "Reeinvent" as plain text instead of the logo** → re-upload the ZIP.
- **The logo sits on top of the watermark** → re-upload the ZIP.
- **No Skills panel in Settings** → tell your Rebrained contact, your account needs it enabled.
- **Something else looks off** → screenshot it and send to your Rebrained contact.

---

## Common questions

**Do I need to tell Claude about the brand every time?**
No. Once installed, the brand rules apply whenever Claude is working on a Reeinvent surface.

**Can I use this in any folder?**
Yes, with either install path. The plugin install registers the skill globally. The manual install does the same thing once you have copied `skills/reeinvent-pitch-deck-design/` into `~/.claude/skills/` (see "Using the fallback install" above). After that, the brand system activates anywhere Claude detects a Reeinvent surface.

**What if something looks off in the output?**
Send the screenshot to your Rebrained contact. Every rendering edge case is considered a bug in the system, not a copy issue.

**Can I edit the brand rules?**
The files are yours to modify, but changing `DESIGN.md` or `CLAUDE.md` will change what Claude produces. Coordinate with your Rebrained contact before making rule changes.

---

## Support

Questions, bug reports, or requests for new slide patterns: contact your Rebrained account lead.

---

## Credits

Roboto fonts (`assets/fonts/Roboto/`) are bundled under the Apache License 2.0, copyright Google. See `assets/fonts/Roboto/LICENSE.txt` for the full license text.
