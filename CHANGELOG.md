# Changelog

All notable changes to the Reeinvent Pitch Deck Design System are documented in this file. Versions follow [semver](https://semver.org/) - **major** for breaking brand-rule changes, **minor** for additive rules / new components, **patch** for wording or infrastructure fixes that don't affect brand output.

The version your install runs is in [VERSION](VERSION). Claude reports it on session start.

---

## v2.3.1 - 2026-05-05

**Production-ready hardening.** Infrastructure-only patch. No brand-rule changes; decks built on v2.3.0 are bit-identical on v2.3.1.

- Rewrote the manual-install section in `README.md` to use the correct `~/.claude/skills/` copy step. The previous instruction (`cd skills/... && claude`) only auto-loaded `CLAUDE.md` from the cwd; it did not register the skill, so triggers fired only inside that one folder. The new instruction registers the skill globally, matching the plugin install.
- Softened the README session-start update-check claim to match reality. The check runs at skill activation, not at session start, so a session that never invokes a Reeinvent surface will not trigger it.
- Added a Recommended companion skills note to `README.md` calling out `anthropic-skills:pptx` and `anthropic-skills:pdf`. The brand system references these skills for `.pptx` / `.pdf` work; they are not bundled here.
- Added `.github/workflows/ci.yml`. Two jobs run on push and PR: a smoke test that generates a `.pptx`, runs `embed-fonts.py`, and verifies six `fntdata` parts plus reopen plus idempotency; and a lint job that asserts zero em-dash characters anywhere, every SVG hex on the 9-color palette, version sync across `VERSION` / `plugin.json` / `marketplace.json`, every required brand asset present, and plugin manifest names agreeing.
- Removed dead code from `scripts/embed-fonts.py` (a discarded first-pass zip rewrite that was immediately superseded). Behavior unchanged.
- Added italic 400 to the Roboto weight allowlist in `SKILL.md` for parity with `CLAUDE.md`. Italic was already permitted (pull quotes only) in `CLAUDE.md` rule 6 and in the pre-flight checklist; the allowlist is now consistent across all three sources of truth.
- Added Apache 2.0 attribution for the bundled Roboto fonts to `README.md` under a Credits section. License text continues to ship at `assets/fonts/Roboto/LICENSE.txt`.

## v2.3.0 - 2026-05-05

**Plugin-installable for real.** v2.2.2 advertised plugin install but Claude Desktop returned "Failed to install plugin" on the install handshake - the package was missing `.claude-plugin/plugin.json` (the plugin manifest), and the skill content was at the repo root rather than under `skills/<name>/`. v2.3.0 fixes both.

- Added `.claude-plugin/plugin.json` so Claude Code / Desktop / Cowork accept the install.
- Moved the skill content (SKILL.md, CLAUDE.md, DESIGN.md, reference.md, assets, scripts) to `skills/reeinvent-pitch-deck-design/` so the skill auto-discovers after install.
- Updated README and CLAUDE.md directory maps to reflect the new layout. Manual / fallback installs now `cd` into `skills/reeinvent-pitch-deck-design/` instead of the repo root.

**No brand-rule changes.** Decks built on v2.2.x are bit-identical on v2.3.0.

## v2.2.2 - 2026-05-05

**Client launch cut (broken install path).** Added CHANGELOG and tightened `.gitignore`. Plugin install was advertised but did not work - see v2.3.0 for the fix. **Do not install v2.2.2.**

- Added this CHANGELOG so installs can see release history at a glance.
- Tightened `.gitignore` to exclude generated decks, slide rasters, `*.bak`, and Python caches.

## v2.2.1 - 2026-05-05

**Repo rename + URL sync.** Repointed everything to the canonical `rebrained-de/Reeinvent-Pitch-Deck-Designer` repo. No brand-rule changes - decks built on v2.2.0 are bit-identical on v2.2.1.

- Repointed README install commands and the session-start version-check URL in CLAUDE.md / SKILL.md to the new org.
- Synced `marketplace.json` plugin version to match `VERSION` (was drifting since v2.2.0 shipped).
- Cleaned `<repo-root>/` placeholder out of CLAUDE.md's directory map; same for the absolute path in reference.md sources.

## v2.2.0 - 2026-04-25

**PPTX autofit + gradient stat-number rules.**

- Added rule: PPTX text frames inside fixed-geometry cards must use `normAutofit`, never `spAutoFit` (cards hold their geometry; text shrinks).
- Added rule: PPTX stat numbers and headline-scale text (>= 40 pt) carry Signature Gradient text fill, not solid Core Blue. PPTX gradient text is reliable, unlike HTML.
- Added preflight verification commands to CLAUDE.md.

## v2.1.0 - 2026-04-23

**Roboto bundled and auto-embedded.**

- Shipped six Roboto TTFs at `assets/fonts/Roboto/` (Apache 2.0): Light 300, Regular 400, Italic 400, Medium 500, Bold 700, Black 900.
- Added `scripts/embed-fonts.py` to inject the TTFs into any generated `.pptx`. Decks now render with correct weights on client machines that don't have Roboto installed.
- Five-weight scale (300 / 400 / 500 / 700 / 900) is the canonical Roboto allowlist across DESIGN.md, CLAUDE.md, and SKILL.md.

## v2.0.0 - 2026-04-22

**Plugin-installable release.**

- Renamed assets to canonical names; added PNG @2x variants alongside SVGs so PPTX can embed PNG (reliable) while HTML uses SVG.
- Added `.claude-plugin/marketplace.json` so the repo installs as a Claude Code / Desktop / Cowork plugin.
- Added `SKILL.md` so the repo also installs as a standalone skill.
- Required all PPTX output to be fully customizable: native shapes, live editable text, theme colors, theme fonts, slide masters per archetype. No rasterization.

## v1.x - internal

Pre-distribution drafts. Not shipped to clients.
