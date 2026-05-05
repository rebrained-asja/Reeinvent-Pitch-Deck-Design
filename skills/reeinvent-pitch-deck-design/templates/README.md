# Reeinvent master decks

This directory tells the skill where to find the production master deck files. Master decks are NOT bundled with this repo (the full PPTX is 165 MB; GitHub blocks files over 100 MB). You install the master decks once, locally, and the skill auto-detects them.

## What you need

At least one of these files, anywhere on your machine:

- **Master Company Presentation** (full 21-slide deck) — the canonical Reeinvent pitch.
- **Slim Company Presentation** — shorter variant.
- **Two-Pager Company Presentation** — short briefing variant.
- **Sarajevo Slush'd / SDG Business Pioneers** — event-specific pitches.

These ship from your designer (Asja). If you do not have them, ask Asja to send the latest masters.

## Where to put them

The skill auto-detects masters in this priority order:

1. The path in the `REEINVENT_MASTER_DECK` environment variable (single file).
2. The directory in the `REEINVENT_TEMPLATES_DIR` environment variable.
3. `~/Reeinvent/Templates/` (the recommended location).
4. `~/Documents/Reeinvent/Templates/`.
5. `~/Downloads/` matching `REE 2.0*Master*Presentation*.pptx` and `REE 2.0*Slim*.pptx` (fallback for first-time use; not stable since Downloads gets cleaned).

**Recommended setup (one-time, 30 seconds):**

```bash
mkdir -p ~/Reeinvent/Templates
mv ~/Downloads/"REE 2.0 – Master Company Presentation.pptx" ~/Reeinvent/Templates/
mv ~/Downloads/"REE 2.0 – Slim Company Presentation.pptx" ~/Reeinvent/Templates/
```

After that, `bin/reeinvent-clone-master` and the skill find them automatically.

## Why no auto-update

Master decks change rarely (1-2 times per year when the brand evolves). They are large binary files unsuited to git distribution. Asja maintains the canonical master in a shared folder; you pull a fresh copy when she updates it. The skill does NOT try to download masters automatically because:

- They are confidential client material.
- They include real customer logos and case study screenshots that should not be in a public repo.
- Bandwidth: 165 MB per pull would be wasteful.

## Updating to a new master

Drop the new file into the same location, overwriting the old one. The skill picks up the new file on the next deck request. Keep a `Master.pptx.backup-YYYYMMDD` copy if you want history.
