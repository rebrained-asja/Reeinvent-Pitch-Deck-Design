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

## Install

Each Claude surface has its own install path - they are not interchangeable. Pick the one matching your surface.

| Surface | Install path | Slash commands |
|---------|--------------|----------------|
| Claude Code (terminal) | Plugin marketplace **or** manual copy to `~/.claude/skills/` | `/plugin marketplace add`, `/plugin install` |
| Cowork / Claude Desktop | Upload the skill ZIP via the **Skills** panel | None - Cowork has no `/plugin` command |

### Claude Code (terminal)

In your terminal, paste:

```
/plugin marketplace add rebrained-de/Reeinvent-Pitch-Deck-Designer
```

Then install the plugin:

```
/plugin install reeinvent-pitch-deck-design@reeinvent-brand-system
```

The plugin marketplace is a Claude Code feature. After install, the skill is registered globally - it activates in any working directory.

### Cowork / Claude Desktop

Cowork does **not** support the `/plugin` slash commands, and there is **no** "Settings → Code → Plugins" menu in the Desktop app. The brand system is installed as a **skill ZIP** uploaded through Cowork's Skills panel.

**Step 1 - get the skill bundle.**

1. Download the repository ZIP from the [repository page](https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer) - click the green **Code** button, then **Download ZIP**.
2. Unzip the download. Open the folder that appears (e.g. `Reeinvent-Pitch-Deck-Designer-main`).
3. Inside, navigate to `skills/reeinvent-pitch-deck-design/`. **This subfolder** is the skill bundle.
4. Re-zip that single subfolder so the resulting ZIP has `SKILL.md` at its root (not nested inside another folder).
   - **Mac**: right-click the `reeinvent-pitch-deck-design` folder → Compress. The ZIP appears next to it.
   - **Windows**: right-click the folder → Send to → Compressed (zipped) folder.

**Step 2 - upload to Cowork.**

1. Open the Skills panel in your Claude surface:
   - **claude.ai (web)**: Settings → Capabilities → Skills.
   - **Claude Desktop**: open the Skills section from the app sidebar.
2. Click **Create / Upload skill** and select the ZIP from Step 1.
3. Wait for Cowork to process the upload. The skill should appear in your Skills list as `reeinvent-pitch-deck-design`, enabled by default.

Once uploaded, the skill is available in every Cowork session, globally. No per-project re-install.

**If you don't see a Skills panel:** your account or app version may not yet have Skills enabled. Contact your Rebrained account lead.

### Verify the install

In any Claude session (Code or Cowork), ask:

> "What brand system is active, and what version?"

Claude should confirm it's running `reeinvent-pitch-deck-design` and report a version matching the current `VERSION` file on GitHub. If it reports "not found" or a stale version, re-run the install for your surface.

---

## Install (fallback - manual copy, Claude Code only)

For offline installs of Claude Code, or environments where the plugin marketplace is unavailable. **This fallback does not work in Cowork** - Cowork does not read from `~/.claude/skills/`.

### Option A - Download the ZIP

1. Go to the [repository page](https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer).
2. Click the green **Code** button, then **Download ZIP**.
3. Unzip the folder somewhere you'll remember, for example `~/Documents/Reeinvent-Brand`.

### Option B - Clone with Git

```bash
git clone https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer.git ~/Documents/Reeinvent-Brand
```

### Copy the skill into the Claude Code user-skill directory

1. Open your terminal (Mac: Terminal / Windows: PowerShell).
2. Copy the skill folder into `~/.claude/skills/`:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R ~/Documents/Reeinvent-Brand/skills/reeinvent-pitch-deck-design ~/.claude/skills/
   ```
   (Adjust the source path to wherever you unzipped or cloned the repo.)
3. Start Claude Code from any working directory and ask:
   > "What brand system is active, and what version?"

   Claude should report `reeinvent-pitch-deck-design` and a version matching the `VERSION` file. If it does not, the copy did not land at `~/.claude/skills/reeinvent-pitch-deck-design/SKILL.md` - re-run step 2.

**Why the copy step matters:** Claude Code auto-discovers skills from `~/.claude/skills/<name>/` (user) or `<project>/.claude/skills/<name>/` (project). Running `claude` inside the cloned repo without copying loads `CLAUDE.md` from the cwd but does not register the skill, so triggers only fire inside that one folder.

**To update later:** re-run the `cp -R` (it overwrites the previous copy), or `git pull` in the source folder and copy again.

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

## Troubleshooting

**`/plugin marketplace add ...` returns "unknown skill" in my chat.**
You are in Cowork or Claude Desktop, not Claude Code. The `/plugin` slash commands only work in the Claude Code terminal. Follow the **Cowork / Claude Desktop** install path above.

**I copied the folder to `~/.claude/skills/` and Cowork still doesn't see the brand system.**
Expected. Cowork reads skills from its own internal directory, not from `~/.claude/skills/`. That fallback path is Claude Code only. Re-install via the **Skills panel upload** path above.

**Claude renders the Reeinvent name as styled text instead of loading the logo file.**
The skill is registered but its asset files are not reachable from your working directory. This happens most often in Cowork sandboxes. Run the SKILL.md Step 0 check by asking Claude:
> "Run the Reeinvent skill Step 0 - verify the brand assets are reachable, and if not, tell me how to fix it."
Claude will halt and tell you whether to re-upload the skill bundle or copy the asset folder into your working directory.

**The logo is sitting on top of the Arrow watermark.**
The logo and the Arrow watermark must never share a quadrant - logo bottom-left or bottom-center, Arrow flush top-right. If you see overlap, the skill is either not loaded or Claude grabbed the wrong asset (the Arrow watermark file is `Arrow-Up.svg`; the wordmark logo is `Gradient-Logo.svg` or `White-Logo.svg`). Re-install and ask Claude to redo the slide.

**Claude only applies the brand rules in one project, not others.**
Once installed via the plugin marketplace or the Cowork Skills panel, the skill is global - it activates on any session. If it only fires in one folder, your install is probably the manual `cd skills/... && claude` shortcut, which loads `CLAUDE.md` from the cwd but does not register the skill. Re-install using one of the supported paths above.

**Cowork needed a restart after I uploaded the skill.**
Cowork caches the skill manifest at process start. After uploading, restart the app once. You should not need to restart for subsequent sessions.

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
