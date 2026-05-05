# Reeinvent Pitch Deck Design System

Your AI-assisted brand kit for building Reeinvent-style presentations. Once installed, every slide Claude helps you build will automatically follow the Reeinvent brand rules: colors, typography, logo placement, gradient usage, and layout.

---

## What you need

- **Claude Code**, **Claude Desktop**, or **Cowork** - any version that supports plugins (v2.0+).
- A logged-in Anthropic account.

That's it. No additional tools, no git required for the simple install.

### Recommended companion skills

Two Anthropic-published skills are referenced by the brand system for `.pptx` and `.pdf` work. They are not bundled here. Install them once if you plan to generate or read decks in those formats:

- `anthropic-skills:pptx` - PowerPoint generation and editing.
- `anthropic-skills:pdf` - PDF reading, extraction, and export.

The brand system still loads without them; rules apply to every HTML / web surface unconditionally. The companion skills are only required when Claude is asked to produce or read a `.pptx` / `.pdf` directly.

---

## Install (recommended)

How you install depends on which Claude surface you use. All three install the same plugin - the command surface is just different.

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

The `/plugin` slash commands do **not** work in Desktop's chat input. Install via the GUI instead:

1. Open **Settings → Code → Plugins** in the Desktop app.
2. Add the marketplace: `rebrained-de/Reeinvent-Pitch-Deck-Designer`.
3. Install the `reeinvent-pitch-deck-design` plugin from the list.

### Verify the install

Ask Claude:

> "What brand system is active, and what version?"

Claude should confirm it's running the Reeinvent Pitch Deck Design plugin and report a version matching the current `VERSION` file on GitHub. If it says "outdated" or "not found," re-run the install.

---

## Install (fallback - manual download)

For offline installs or environments where the plugin marketplace is unavailable.

### Option A - Download the ZIP

1. Go to the [repository page](https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer).
2. Click the green **Code** button on the top right, then **Download ZIP**.
3. Unzip the folder somewhere you'll remember, for example `~/Documents/Reeinvent-Brand`.

### Option B - Clone with Git

```bash
git clone https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer.git
```

### Using the fallback install

The plugin install above registers the brand system as a discoverable Claude skill. The manual install does the same thing by copying the skill folder into the user-skill directory Claude scans on startup.

1. Open your terminal (Mac: Terminal / Windows: PowerShell).
2. Make sure the user-skill directory exists, then copy the skill folder into it:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R ~/Documents/Reeinvent-Brand/skills/reeinvent-pitch-deck-design ~/.claude/skills/
   ```
   (Adjust the source path to wherever you unzipped or cloned the repo.)
3. Start Claude Code from any working directory:
   ```bash
   claude
   ```
4. Verify the skill is discovered. Ask Claude:
   > "What brand system is active, and what version?"

   Claude should report `reeinvent-pitch-deck-design` and a version matching the `VERSION` file. If it does not, the copy step did not land in `~/.claude/skills/reeinvent-pitch-deck-design/SKILL.md` - re-run step 2.

**Why the copy step matters:** Claude only auto-discovers skills from `~/.claude/skills/<name>/` (user) or `<project>/.claude/skills/<name>/` (project). Running `claude` inside the cloned repo without copying loads `CLAUDE.md` from the cwd but does not register the skill, so brand-rule triggers fire only when you stay inside that one folder.

**To update later:** re-run step 2 (the `cp -R` overwrites the previous copy), or `git pull` in the source folder and copy again.

---

## How to use it with Claude

Once installed (either path), just talk to Claude. The brand rules load automatically.

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

## Updating to a new version

### Plugin install

```
/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system
```

### Manual install

Re-download the ZIP (or `git pull` inside the cloned folder), then re-copy:

```bash
cp -R ~/Documents/Reeinvent-Brand/skills/reeinvent-pitch-deck-design ~/.claude/skills/
```

The brand system checks for updates the first time you ask Claude for a Reeinvent surface in a session - if your local copy is behind GitHub, Claude will tell you in one line and wait for you to update. The check runs at skill activation, not at session start, so a session that never asks for a Reeinvent surface will not trigger it.

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
