# Reeinvent Pitch Deck Design System

Your AI-assisted brand kit for building Reeinvent-style presentations. Every slide Claude helps you build will automatically follow the Reeinvent brand rules: colors, typography, logo placement, gradient usage, and layout.

---

## What you need

1. **Claude Code** installed on your computer. Download from [claude.ai/download](https://claude.ai/download) if you don't have it yet.
2. This folder (downloaded or cloned, see below).

That's it. No other tools required.

---

## How to install

### Option 1 - Download the ZIP (easiest, no tools needed)

1. Go to the [repository page](https://github.com/rebrained-asja/Reeinvent-Pitch-Deck-Design) on GitHub.
2. Click the green **Code** button on the top right.
3. Click **Download ZIP**.
4. Unzip the folder somewhere you'll remember, for example `~/Documents/Reeinvent-Brand`.

### Option 2 - Clone with Git (if you have Git installed)

```bash
git clone https://github.com/rebrained-asja/Reeinvent-Pitch-Deck-Design.git
```

---

## How to use it with Claude

1. Open your terminal (Mac: Terminal app / Windows: PowerShell).
2. Go into the folder you just downloaded:
   ```bash
   cd ~/Documents/Reeinvent-Brand
   ```
   (adjust the path to wherever you unzipped it)
3. Start Claude:
   ```bash
   claude
   ```
4. Ask Claude anything about your presentation. Claude will automatically load the brand system from this folder and follow every rule.

---

## Example prompts to try

Here are some things you can ask Claude once you're inside this folder:

> **"Build me a 10-slide pitch deck for [your topic]. Follow our brand system."**

> **"Create a cover slide for a deck titled '[your title]'."**

> **"Review this slide layout against DESIGN.md and tell me what's off."**

> **"Make a service-detail slide for our new offer called [offer name]. Use the A5 archetype from reference.md."**

> **"Build a contact slide with our three office cities."**

> **"Show me the four slide archetypes I can use for a sales deck."**

Claude knows the full brand system automatically: the 9 canonical colors, the 30-degree gradient, Roboto typography, the four logo assets, the slide archetypes (cover, section divider, service detail, success story, stat, contact, closing), and every layout rule.

---

## What's inside this folder

- **DESIGN.md** - The complete brand guideline. Every rule Claude follows. You can read it if you want to understand the system in detail, but you don't have to.
- **CLAUDE.md** - The operating manual for Claude. Automatically loaded when you open Claude from this folder. You don't need to read it.
- **reference.md** - Slide archetypes distilled from real Reeinvent presentations. Useful when you want Claude to copy a specific layout pattern.
- **signal-deck.html** - A complete example pitch deck. Open it in any browser to see the brand system in action.
- **assets/logo/** - The four brand graphics (two wordmark versions, two arrow variants). Claude uses these automatically.

---

## Common questions

**Do I need to tell Claude about the brand every time?**
No. As long as you start Claude from inside this folder, the brand rules load automatically.

**Can I use this in any folder?**
Only when Claude is running from this folder (or a project folder that copies these files in). Claude reads the rules from `CLAUDE.md` when it starts.

**What if something looks off in the output?**
Send the screenshot to your Rebrained contact. Every rendering edge case is considered a bug in the system, not a copy issue.

**Can I edit the brand rules?**
The files are yours to modify, but changing `DESIGN.md` or `CLAUDE.md` will change what Claude produces. Coordinate with your Rebrained contact before making rule changes.

---

## Support

Questions, bug reports, or requests for new slide patterns: contact your Rebrained account lead.
