# Reeinvent Pitch Deck Design System

Your AI-assisted brand kit for building Reeinvent-style presentations. Once installed, every slide Claude helps you build will automatically follow the Reeinvent brand rules: colors, typography, logo placement, gradient usage, and layout.

---

## What you need

- A Claude account with **Skills** enabled (Claude Desktop, Cowork, or claude.ai).
- The ZIP file your Rebrained contact sent you.

That's it.

### One-time extras (only if you'll make PowerPoint or PDF files)

If you want Claude to also build `.pptx` (PowerPoint) or `.pdf` files for you, install these two free Anthropic skills once. They come from Anthropic, not Rebrained, and you only need them once:

- **pptx** - lets Claude create and edit PowerPoint files.
- **pdf** - lets Claude read and create PDFs.

Without them, Claude can still build slides on screen (as web pages) and follow every brand rule. You only need pptx / pdf if you want a downloadable PowerPoint or PDF file at the end.

---

## Install

1. Get the ZIP from your Rebrained contact (e.g. `reeinvent-pitch-deck-design-2.4.1.zip`).
2. Open Claude. Go to **Settings → Capabilities → Skills**.
3. Click **Create skill** and upload the ZIP.
4. Quit Claude and reopen it once.

Done. The brand rules now apply in every chat, in any project. You only do this once.

### Check it worked

Open any chat and ask:

> "What brand system is active, and what version?"

Claude should reply `reeinvent-pitch-deck-design` and the version that matches your ZIP. If it doesn't, delete the entry in Skills and re-upload the ZIP.

---

## How to use it

Once installed, just talk to Claude. The brand rules load automatically when you ask for a Reeinvent slide or deck.

### Example prompts to try

> **"Build me a 10-slide pitch deck for [your topic]. Follow our brand system."**

> **"Create a cover slide for a deck titled '[your title]'."**

> **"Review this slide layout against our brand and tell me what's off."**

> **"Make a service-detail slide for our new offer called [offer name]."**

> **"Build a contact slide with our three office cities."**

> **"Show me the slide layouts I can use for a sales deck."**

Claude knows the full brand system automatically: the 9 Reeinvent colors, the 30-degree gradient, Roboto typography, the four brand marks (each provided in both web and PowerPoint formats), the slide layouts (cover, section divider, service detail, success story, stat, contact, closing), and every layout rule.

---

## Updating to a new version

When Rebrained releases an update, you'll get a new ZIP file (e.g. `reeinvent-pitch-deck-design-2.5.0.zip`).

1. Open Claude → **Settings → Capabilities → Skills**.
2. Delete the existing `reeinvent-pitch-deck-design` entry.
3. Upload the new ZIP.
4. Quit Claude and reopen it.

Two clicks plus a restart. Your conversations and projects are untouched.

---

## If something's not right

**Claude wrote "Reeinvent" as plain text instead of using the logo.**
The skill didn't install cleanly. Delete it from Skills and re-upload the ZIP.

**The logo is sitting on top of the watermark.**
Same fix: delete the skill, re-upload the ZIP, ask Claude to redo the slide.

**Claude doesn't seem to know the brand rules in a new chat.**
Quit Claude completely and reopen it. Skills load when the app starts. If it still doesn't work, re-upload the ZIP.

**There's no Skills section in my Settings.**
Your account doesn't have Skills turned on yet. Email your Rebrained contact and they'll help.

**Something else looks wrong on a slide.**
Take a screenshot and send it to your Rebrained contact. We treat every rendering issue as a bug in the system, not your problem to fix.

---

## Common questions

**Do I need to tell Claude about the brand every time?**
No. Once installed, the brand rules apply automatically whenever you ask Claude about a Reeinvent deck or slide.

**Can I use this in any project or folder?**
Yes. Once uploaded, the skill works in every chat, regardless of where you are or what project you're in.

**Can I edit the brand rules myself?**
The files inside the ZIP are technically editable, but changing them changes what Claude produces. Talk to your Rebrained contact first if you want a rule changed - we'll do it for you so the system stays consistent.

**Do I need to keep the ZIP file after uploading?**
No. Claude copies everything from the ZIP into its own storage. You can delete the ZIP from your computer once the upload finishes. Keep a copy somewhere safe in case you ever need to re-install.

---

## What's inside the ZIP (for the curious)

The folder Claude unpacks contains:

- **SKILL.md** - the file that tells Claude this is a skill and when to use it.
- **CLAUDE.md** - Claude's operating manual: the brand rules and the pre-flight checklist.
- **DESIGN.md** - the complete brand guideline. Every rule Claude follows.
- **reference.md** - slide layout examples distilled from real Reeinvent presentations.
- **assets/logo/** - the four Reeinvent brand marks (logo and arrow), each in web and PowerPoint formats.
- **assets/fonts/Roboto/** - the Roboto font files, auto-embedded into every PowerPoint Claude makes.
- **scripts/** - small helper scripts Claude uses when generating PowerPoint and PDF files.

You don't need to touch any of this. It's listed in case you're ever curious what's inside the ZIP.

---

## For developers (Rebrained internal)

If you're on the Rebrained team using Claude Code (the terminal tool), there's a faster install path that doesn't need a ZIP.

In your terminal:

```
/plugin marketplace add rebrained-de/Reeinvent-Pitch-Deck-Designer
/plugin install reeinvent-pitch-deck-design@reeinvent-brand-system
```

To update later:

```
/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system
```

If the marketplace isn't available (offline, restricted env), clone the repo and copy the skill folder into `~/.claude/skills/`:

```bash
git clone https://github.com/rebrained-de/Reeinvent-Pitch-Deck-Designer.git ~/Documents/Reeinvent-Brand
mkdir -p ~/.claude/skills
cp -R ~/Documents/Reeinvent-Brand/skills/reeinvent-pitch-deck-design ~/.claude/skills/
```

These paths are **Claude Code only**. They don't work in Cowork or Claude Desktop. Those use the Skills upload path described above.

---

## Support

Questions, bug reports, or requests for new slide patterns: contact your Rebrained account lead.

---

## Credits

Roboto fonts (`assets/fonts/Roboto/`) are bundled under the Apache License 2.0, copyright Google. See `assets/fonts/Roboto/LICENSE.txt` for the full license text.
