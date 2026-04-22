# Reeinvent Pitch Deck Design System

Your AI-assisted brand kit for building Reeinvent-style presentations. Once installed, every slide Claude helps you build will automatically follow the Reeinvent brand rules: colors, typography, logo placement, gradient usage, and layout.

---

## What you need

- **Claude Code**, **Claude Desktop**, or **Cowork** - any version that supports plugins (v2.0+).
- A logged-in Anthropic account.

That's it. No additional tools, no git required for the simple install.

---

## Install (recommended)

How you install depends on which Claude surface you use. All three install the same plugin - the command surface is just different.

### Claude Code (terminal) and Cowork

In the terminal, paste:

```
/plugin marketplace add rebrained-asja/Reeinvent-Pitch-Deck-Design
```

Then install the plugin:

```
/plugin install reeinvent-pitch-deck-design@reeinvent-brand-system
```

### Claude Desktop (app)

The `/plugin` slash commands do **not** work in Desktop's chat input. Install via the GUI instead:

1. Open **Settings → Code → Plugins** in the Desktop app.
2. Add the marketplace: `rebrained-asja/Reeinvent-Pitch-Deck-Design`.
3. Install the `reeinvent-pitch-deck-design` plugin from the list.

### Verify the install

Ask Claude:

> "What brand system is active, and what version?"

Claude should confirm it's running the Reeinvent Pitch Deck Design plugin and report a version matching the current `VERSION` file on GitHub. If it says "outdated" or "not found," re-run the install.

---

## Install (fallback - manual download)

For offline installs or environments where the plugin marketplace is unavailable.

### Option A - Download the ZIP

1. Go to the [repository page](https://github.com/rebrained-asja/Reeinvent-Pitch-Deck-Design).
2. Click the green **Code** button on the top right, then **Download ZIP**.
3. Unzip the folder somewhere you'll remember, for example `~/Documents/Reeinvent-Brand`.

### Option B - Clone with Git

```bash
git clone https://github.com/rebrained-asja/Reeinvent-Pitch-Deck-Design.git
```

### Using the fallback install

1. Open your terminal (Mac: Terminal / Windows: PowerShell).
2. Go into the folder you just downloaded:
   ```bash
   cd ~/Documents/Reeinvent-Brand
   ```
3. Start Claude Code:
   ```bash
   claude
   ```
4. Claude will automatically load the brand system from this folder and follow every rule.

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

- **DESIGN.md** - The complete brand guideline. Every rule Claude follows.
- **CLAUDE.md** - The operating manual for Claude. Loaded automatically.
- **SKILL.md** - Skill manifest (invoked automatically when you work on a Reeinvent surface).
- **reference.md** - Slide archetypes distilled from real Reeinvent presentations.
- **VERSION** - Semver of the currently installed brand system.
- **assets/logo/** - The four brand marks, each as SVG (for HTML / web) and PNG at 2x (for PPTX / Slides embedding).

---

## Updating to a new version

### Plugin install

```
/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system
```

### Manual install

Re-download the ZIP, or `git pull` inside the cloned folder.

Claude will warn you at session start if your local copy is behind the GitHub version.

---

## Common questions

**Do I need to tell Claude about the brand every time?**
No. Once installed, the brand rules apply whenever Claude is working on a Reeinvent surface.

**Can I use this in any folder?**
With the plugin install - yes, the brand system activates anywhere Claude detects a Reeinvent surface. With the manual install - only when Claude is running from the folder you downloaded.

**What if something looks off in the output?**
Send the screenshot to your Rebrained contact. Every rendering edge case is considered a bug in the system, not a copy issue.

**Can I edit the brand rules?**
The files are yours to modify, but changing `DESIGN.md` or `CLAUDE.md` will change what Claude produces. Coordinate with your Rebrained contact before making rule changes.

---

## Support

Questions, bug reports, or requests for new slide patterns: contact your Rebrained account lead.
