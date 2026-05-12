# Changelog

All notable changes to the Reeinvent Pitch Deck Design System are documented in this file. Versions follow [semver](https://semver.org/) - **major** for breaking brand-rule changes, **minor** for additive rules / new components, **patch** for wording or infrastructure fixes that don't affect brand output.

The version your install runs is in [VERSION](VERSION). Claude reports it on session start.

---

## v2.4.2 - 2026-05-12

**Cowork skill upload fix.** Cowork's Skills uploader rejects ZIPs whose
contained paths include the `@` character, with the error "Zip file
contains path with invalid characters." The brand PNGs shipped at
`Arrow-Up@2x.png`, `Upwards-Arrow@2x.png`, `White-Logo@2x.png`, and
`Gradient-Logo@2x.png` (the `@2x` is an iOS/web naming convention for
2x-resolution assets). Renamed all four files to `-2x.png` so the ZIP
uploads cleanly. Updated every reference in SKILL.md, CLAUDE.md,
DESIGN.md, and the CI workflow.

**No brand-rule changes.** The PNGs are bit-identical; only the filenames
changed. Decks built on v2.4.1 rebuild bit-identical on v2.4.2 once the
filename references update.

If you used the old `@2x.png` filenames in your own documents or
templates, do a find-and-replace: `@2x.png` -> `-2x.png`.

## v2.4.1 - 2026-05-12

**Cowork install fix + brand-asset safety net.** A first client install of v2.4.0 surfaced three documentation bugs and one silent runtime failure. None of the brand rules change; v2.4.0 decks rebuild bit-identical on v2.4.1.

### Documentation - install paths corrected

The README presented three install paths as if equivalent. Two were wrong for Cowork:

- `/plugin marketplace add ...` does not work in Cowork chat. It is a Claude Code-only slash command. The README now scopes it to Claude Code.
- "Settings → Code → Plugins" does not exist in Claude Desktop / Cowork. The README's instruction to install there is removed.
- `~/.claude/skills/` is not read by Cowork. The manual-copy fallback is now labeled Claude-Code-only.

Replaced with a verified Cowork path: download the repo ZIP, extract `skills/reeinvent-pitch-deck-design/` as the skill bundle, re-zip that subfolder, upload via Cowork's Skills panel (claude.ai → Settings → Capabilities → Skills, or the Desktop Skills sidebar). The README now opens with a surface-to-path matrix so the right path is picked before any commands run.

Added a Troubleshooting section covering the five symptoms most likely to surface in a fresh client install: the "unknown skill" error in Cowork chat, the silent `~/.claude/skills/` no-op in Cowork, logo-rendered-as-text, logo-on-top-of-watermark, and the missing cross-project trigger.

### Skill runtime - Step 0 asset verification

Added a "Step 0: verify the skill's assets are reachable" gate at the top of SKILL.md, before the existing version check. It runs the first time a session asks for a Reeinvent surface:

1. Read `assets/logo/Gradient-Logo.svg` to confirm the install location is intact.
2. Decide an asset-reach strategy for the output (copy `assets/` into the working directory, or inline SVGs for HTML when filesystem access is restricted).
3. Verify the strategy worked before generating any deck.

If step 1 fails, the skill halts and reports the install problem in one sentence. It does not fall back to text or CSS-drawn marks. This converts the most common failure mode (the v2.4.0 client install hit this when Cowork registered the skill manifest without bundling the assets) from silent to loud.

### Brand rules - logo lockup section

Added three rules (33-35) in CLAUDE.md covering logo behavior that v2.4.0 left implicit and Claude got wrong:

- **Rule 33**: Never render the wordmark as styled text. The wordmark loads from the asset file or the skill halts per Step 0. No `<div>Reeinvent</div>` fallback.
- **Rule 34**: The logo and the Arrow watermark never share a quadrant. Logo bottom-left / bottom-center; Arrow flush top-right. Overlap means the wrong asset was selected.
- **Rule 35**: Wordmark routing by surface is not optional - `Gradient-Logo` on light, `White-Logo` on dark or gradient.

The same content lands in SKILL.md's "Assets" section so both ground-truth files agree. Added traps 11-13 (logo-as-text, logo-on-watermark, skipping Step 0) so the failure modes are documented twice - by rule and by anti-pattern.

Pre-flight checklist updated: the `<img src>` line now explicitly forbids text substitutes; new lines verify logo / watermark quadrant separation and light / dark wordmark routing.

### Skill description - broader trigger phrases

SKILL.md description front-matter now includes `agenda`, `stat slide`, `closing slide`, `make slides`, `build a deck`, and `A1 through A10` so the skill fires reliably when users phrase a request without saying "Reeinvent presentation" verbatim. The v2.4.0 description triggered cleanly on the formal phrasing but missed casual ones like "draft me a client pitch deck."

## v2.4.0 - 2026-05-05

**Vector PDF export for client distribution.** Adds `scripts/render-pdf.py` so HTML decks can render directly to PDF via headless Chrome - SVGs and gradients stay vector all the way to the deliverable. The previous default path (HTML -> PPTX -> LibreOffice PDF) downsampled and JPEG-recompressed every embedded image; logos and gradient bands degraded visibly at any zoom. The new path is the canonical client-distribution flow.

- Added `skills/reeinvent-pitch-deck-design/scripts/render-pdf.py`. Auto-detects Chrome on macOS / Linux, injects an `@page` size rule for slide-shaped PDFs, renders in place so relative SVG paths resolve.
- Updated CLAUDE.md "Export / convert to PPTX or PDF" with a decision table mapping goal -> source format -> tool, plus the rule "never route HTML -> PPTX -> PDF for a client deliverable."
- Updated CLAUDE.md asset routing for `PDF via HTML print` to point at `scripts/render-pdf.py`.

No brand-rule changes. PPTX builds and PDF builds from existing HTML are bit-identical to v2.3.2; v2.4.0 only adds a new export path.

## v2.3.2 - 2026-05-05

**Claude Desktop install fix.** v2.3.1 installed cleanly via Claude Code CLI but failed in Claude Desktop. Root cause: the marketplace manifest used a shape that CLI tolerates and Desktop rejects. No brand-rule changes; decks built on v2.3.1 are bit-identical on v2.3.2.

- Aligned `.claude-plugin/marketplace.json` with the canonical shape used by `anthropics/skills` (the only known-working public marketplace reference). Three concrete deltas:
  - Added an explicit `skills` array on the plugin entry: `["./skills/reeinvent-pitch-deck-design"]`. Without this, Desktop's stricter validator rejects the plugin because it cannot deterministically locate the skill content. CLI auto-discovers and was masking the gap.
  - Added `"strict": false` on the plugin entry. Matches the reference; relaxes Desktop's schema validation to the same level CLI uses.
  - Added a top-level `metadata` block with `description` and `version`. Brings the marketplace manifest to schema parity with the reference.
  - Changed `"source": "."` to `"source": "./"` for trailing-slash parity with the reference.
- Bumped `VERSION` and `plugin.json` to `2.3.2`. Marketplace `metadata.version` and `plugins[0].version` likewise.

**No brand-rule changes.** This is purely a manifest-shape fix.

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
