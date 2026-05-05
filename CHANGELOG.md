# Changelog

All notable changes to the Reeinvent Pitch Deck Design System are documented in this file. Versions follow [semver](https://semver.org/) - **major** for breaking brand-rule changes, **minor** for additive rules / new components, **patch** for wording or infrastructure fixes that don't affect brand output.

The version your install runs is in [VERSION](VERSION). Claude reports it on session start.

---

## v3.1.0 - 2026-05-05

**Path A (clone the master deck) is now the canonical workflow.** v3.0.0 shipped a code-driven generator as the way to produce client decks, then sales-deck testing in real PowerPoint exposed a fundamental mismatch: the production Reeinvent master deck has design moves a generator cannot replicate without a designer in the loop (mega-display "AI-DRIVEN" titles at 180+ pt with full-bleed gradient text, laptop+screenshot mockup clusters layered over tinted product photography, partner-brand alliance accents on the Trident slide, multiple gradient underlines per slide). v3.0.0's generator produced brand-correct skeletons but not Reeinvent-quality output. Path A inverts the model: clone the actual master deck (where every slide is already designer-perfect) and have Claude swap only the text per prospect.

**What's new**

- `bin/reeinvent-clone-master`: locates the production master via env-var / `~/Reeinvent/Templates/` / `~/Documents/Reeinvent/` / `~/Downloads/` (in priority order), copies it to a working file in cwd, opens in PowerPoint. Variants supported: `master`, `slim`, `two-pager`.
- `bin/reeinvent-deck inspect <deck.pptx>`: lists every slide with its layout name and the text content of every shape. Used to plan replacements before mutating.
- `bin/reeinvent-deck replace <deck.pptx> <replacements.json>`: applies `{old: new}` text substitutions across the deck while preserving every shape's geometry, fonts, gradients, photography, and run-level typography. Restrict to specific slides via `--slides 1,2,4`.
- `templates/README.md`: documents the master-deck install location and discovery order.

**SKILL.md / CLAUDE.md / README rewrites**

- SKILL.md frames the two-path workflow with Path A as default for client work and Path B (skeleton generator) gated behind explicit "draft" / "rough cut" requests.
- CLAUDE.md no longer instructs Claude to write JSON specs for client decks; it instructs Claude to clone the master, inspect, replace, re-inspect.
- README documents first-time master-deck install (`mkdir -p ~/Reeinvent/Templates && mv ...`) prominently.
- DESIGN.md left intact but with an explicit caveat in SKILL.md: the master deck is the source of truth; DESIGN.md prose is a simplified summary that does not capture every brand pattern. The master allows multiple gradient underlines per slide (DESIGN.md says one), partner-brand colors on alliance slides (DESIGN.md says nine canonical only), and a full button library (DESIGN.md says no button library exists).

**What's preserved from v3.0.0**

The Path B generator (`bin/reeinvent-deck build`), 12 archetype builders, theme XML patching, font embedding, post-build verification, 20 tests, and CI all stay. They keep working for skeleton-mode use. The v3.0.0 release notes' premium claims are superseded; the generator remains useful for fast internal first-drafts and any context where the master deck is unavailable.

**Migration**

Re-install: `/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system`. Then drop your master into `~/Reeinvent/Templates/` per the README. The v3.0.0 JSON spec workflow continues to work but should not be used for client decks.

## v3.0.0 - 2026-05-05

**Deterministic PPTX generator. End of hand-rolled python-pptx.** v2.x shipped the brand law, assets, and a font-embed post-processor, but every PPTX request asked Claude to write python-pptx code from scratch while remembering 32 brand rules. The result was non-deterministic output that drifted between sessions: theme colors sometimes missing, gradient text sometimes solid Core Blue, autofit sometimes wrong, embed sometimes skipped. v3.0.0 replaces that with a code-driven pipeline that encodes every rule once and outputs production-grade decks.

**Premium polish (caught during pre-release review)**

- Card components now carry the brand-correct Ink-tinted drop shadow (0pt x 4pt, 16pt blur, Ink at 8% alpha). v3.0.0-alpha cards rendered as flat rectangles which read as cheap; this is the single biggest visual lift.
- Chat-bubble callouts now have the canonical triangular tail (built-in isosceles triangle primitive, rotated to point at the labeled element). Used on service-detail and success-story slides per reference.md. Renders consistently across PowerPoint, Keynote, Slides, and LibreOffice.
- Two-column right card now hugs its content with symmetric padding instead of stretching full-height. No more wasted whitespace.
- Agenda right column row spacing scales with item count so titles plus descriptions never clip.
- Cover slide eyebrow is now solid white (gradient stripe sits below) per DESIGN.md rule 23 - solid blue or gradient text under 40 pt on dark surfaces is prohibited. Fixes a brand violation that v3.0.0-alpha shipped.
- Cover slide gradient underline placed under the title's first word, never the highlighted phrase, satisfying rule 11 (no stacking of gradient-text + underline on the same word).
- Closing slide mega message bumped to 72 pt with tighter pill spacing and a properly visible centered wordmark.
- Closing slide hero arrow re-rasterized at 8x source resolution from the SVG so PowerPoint scaling stops aliasing.
- Arrow watermark opacity raised to the spec ceiling (10% on dark, 6% on light) so the signature mark reads on small renders and dim projector rooms.
- Service detail tagline and URL repositioned within the safe area; no more clipping.
- Intro split title sizes bumped to reference.md A3 spec (72 pt thin over 120 pt black) for the dramatic two-line hero treatment.

**Spec additions for production decks**

- `image: "path/to/photo.jpg"` field on `intro_split`, `service_detail`, and `success_story`. The builder embeds the supplied image; absent, it draws a labeled placeholder so the slot is unmistakably "needs your screenshot here." This is the path to "ready for the CFO" decks: drop in real photography, every slot has known geometry.
- `notes: "..."` field on every archetype, written into the slide's notes pane for the presenter.

**What's new**

- `generator/` Python package (`reeinvent_pitch_deck`). Spec in, brand-perfect `.pptx` out.
  - 12 archetype builders covering DESIGN.md section 6 (cover, section_divider, content, two_column, stat, three_up, quote, closing, agenda) and reference.md A1-A6 (intro_split, service_detail, success_story).
  - `theme.py`: 9 colors, 3 gradients, full type scale, geometry constants. Single source of truth.
  - `master.py`: patches the slide master's `theme1.xml` so the 9 brand colors register as Theme Colors (dk1, lt1, dk2, lt2, accent1-6) and theme fonts are Roboto. Re-skinning the deck is one Theme Colors panel away.
  - `helpers.py`: native `<a:gradFill>` for shape and text runs (30 deg, both stops), arrow watermark with correct opacity, brand stamp, gradient stripes / pills / chat bubbles, arrow bullet markers, recolor effect for arrow-on-light-bg, normAutofit on cards.
  - `embed.py`: ports the v2.x font-embed logic into the package (the old `scripts/embed-fonts.py` still works).
  - `verify.py`: post-build pre-flight covering 6 Roboto fntdata entries, all 9 brand colors in theme XML, no em-dash anywhere, no spAutoFit, 16:9 widescreen canvas.
  - `cli.py`: `reeinvent-deck build | verify | embed`.
  - `spec.py`: strict JSON validator. Unknown fields raise. Em-dash anywhere in any text raises. Bullet lists capped at 6 (DESIGN.md bullet rule 5). Three-up exactly 3 cards. All bounds enforced before a single shape is drawn.
- `bin/reeinvent-deck` bash wrapper. Auto-creates a Python venv on first run, installs `python-pptx`, invokes the CLI. Idempotent (cached via `requirements.txt` hash). Works from any cwd. **No manual pip install required.**
- `generator/examples/reeinvent-full.json`: 12-slide reference deck exercising every archetype.
- 19 tests (`tests/test_spec.py`, `tests/test_build.py`) covering spec validation, end-to-end deck build, theme color presence, font embedding, gradient text on stat numbers, no spAutoFit, no em-dash, canvas size.
- CI rebuilt: pytest job runs all 19 tests and additionally builds the full example via the CLI, runs verify, asserts 6 fntdata entries, asserts no spAutoFit. Bootstrap-script idempotency covered as a separate step. Lint job adds a fourth file (`pyproject.toml`) to the version-sync check.

**SKILL.md / CLAUDE.md rewrites**

- Removed the v2.x delegation to `anthropic-skills:pptx`. Decks are now built via `bin/reeinvent-deck`. Hand-rolled python-pptx is explicitly forbidden.
- Removed mentions of nonexistent skills (`normalize`, `polish`, `critique`, `audit`) as Skill-tool invocations; kept the names as workflow phases. The skill's actual capability surface is the generator + the brand law files; that is now what the docs describe.
- Spec format documented inline in SKILL.md so Claude can produce correct JSON without reading source code.

**README rewrite**

- Updated install paths (unchanged commands) and added a "Generating a deck without Claude" section so the generator is usable from a script or CI without going through Claude.
- Added the 12-archetype table.
- Updated the directory map.

**Decks built on v2.x will keep working**, but they were authored by hand. v3.0.0 is the first version where the deck pipeline is deterministic. Future decks should go through the generator. The breaking change for **users** is zero (install command is the same, output is `.pptx`). The breaking change for **DESIGN.md** is also zero (no rule additions, no rule changes). The breaking change is internal: the skill no longer asks Claude to compose python-pptx code; it asks Claude to compose a JSON spec.

**Migration**: re-install the plugin (`/plugin update reeinvent-pitch-deck-design@reeinvent-brand-system`). The bootstrap will create the venv on the first deck request. No other action required.

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
