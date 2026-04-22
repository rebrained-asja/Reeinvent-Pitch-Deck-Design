# Design System - Reeinvent (Decks)

> **Purpose of this document.** This system is tuned for **slide decks** - PowerPoint (.pptx), PDF, and Google Slides. All measurements are given in **points (pt)** and **inches (in)** for slide canvas, with pixel equivalents where useful. The canonical slide canvas is **16:9 widescreen: 13.333 in × 7.5 in** (960 pt × 540 pt, or 1920 × 1080 px exported at 144 DPI). Google Slides' default 10 in × 5.625 in works with the same proportions - scale all values by 0.75.

## 1. Visual Theme & Atmosphere

Reeinvent's brand is a story told in two colors. It begins in **blue** - the color of clarity, structure, and the developer spirit that built the company - and evolves into **violet**, the color of imagination, intelligence, and AI. Every slide is a frame in that story. The brand's single most important visual gesture is the **blue-to-violet gradient at 30°**, a rising diagonal that isn't horizontal (too flat) and isn't vertical (too stiff) - it rises, like progress.

In a deck, this plays out at three scales: **full-bleed gradient backgrounds** on title and closing slides, **gradient highlights** on key words inside headlines, and **gradient accents** (strips, underlines, arrows) quietly sitting beside otherwise-neutral content slides.

The brand's signature mark is **The Arrow** - a stylized, diagonal up-right arrow with a notched, asymmetric tail derived from the three stripes inside the "REE" lettermark. It is the single strongest recognition device in the system. It appears on title slides as a watermark, on section dividers as a hero element, on content slides as a small accent, and on closing slides at display scale.

Typographically, decks use **Roboto** exclusively (700 for headlines, 400 for body). No secondary typeface. Energy comes from gradient treatments applied to Roboto, not from the letterforms.

Chromatically, decks are bi-modal. Alternate between **Ink dark slides** (`#0A1220` / `#1B2848` gradient) and **Off-white light slides** (`#F5F5F5`) for rhythm. A 15-slide deck might open dark, body light, section dividers dark, closing gradient - creating chapters without a word of explanation.

**Key characteristics for decks:**
- One typeface - Roboto, 700 and 400 only
- One gradient - blue→violet at **30°** (never horizontal, never vertical)
- One signature mark - the Arrow (up-right)
- Two canvas modes - Ink dark and Off-white light, alternated for rhythm
- Generous whitespace, large type, one idea per slide
- The Arrow anchors title slides, opens section dividers, closes the deck

## 2. Color Palette & Roles

### Neutrals
| Name | Hex | RGB | Use on slides |
|------|-----|-----|---------------|
| **Ink** | `#0A1220` | 10, 18, 32 | Primary dark background, section divider fill, body text on light slides |
| **Deep Navy** | `#1B2848` | 27, 40, 72 | Secondary dark background, top stop of dark gradient |
| **Off-White** | `#F5F5F5` | 245, 245, 245 | Primary light background, body text on dark slides, arrow fill |
| **White** | `#FFFFFF` | 255, 255, 255 | Headline text on dark slides, card fills when needed |

### Blue - Developer Roots
| Name | Hex | RGB | Use on slides |
|------|-----|-----|---------------|
| **Core Blue** | `#2665E2` | 38, 101, 226 | Primary accent, solid CTA fills, link color, 50% stop of Signature Gradient |
| **Mid Blue** | `#3C74E2` | 60, 116, 226 | Secondary accent, chart series 2 |
| **Sky Blue** | `#6C94E5` | 108, 148, 229 | Tints, faint fills, chart series 3, caption text on dark |

### Violet - AI Future
| Name | Hex | RGB | Use on slides |
|------|-----|-----|---------------|
| **Core Violet** | `#A942EF` | 169, 66, 239 | Saturated accent; endpoint of vivid gradient variant |
| **Mid Violet** | `#C26DE6` | 194, 109, 230 | 50% stop of Signature Gradient; highlight/badge fills |
| **Soft Violet** | `#D79BEC` | 215, 155, 236 | Tints, delicate highlights, chart series 4 |

### Gradients
- **Signature Gradient** - **30°, `#2665E2` 0% → `#C26DE6` 100%.** The brand. Use on title slide backgrounds, gradient text, underlines, CTA pill fills.
- **Vivid Gradient** - **30°, `#2665E2` 0% → `#A942EF` 100%.** A more saturated variant for hero moments (closing slide, big statement).
- **Dark Gradient** - **30°, `#1B2848` 0% → `#0A1220` 100%.** Tonal navy gradient for depth on dark slides without visual noise. Used when the blue/violet gradient would overpower.

### Chart palette (recommended order)
1. Core Blue `#2665E2`
2. Mid Violet `#C26DE6`
3. Mid Blue `#3C74E2`
4. Soft Violet `#D79BEC`
5. Sky Blue `#6C94E5`
6. Ink `#0A1220` (for neutral baselines/targets)

Avoid using more than 5 colored series on one chart. Prefer highlighting one series in Core Blue and greying the rest at 40% opacity.

### Text contrast by surface (strict)

This is the rule that determines which text color is legible on which background. Violating it produces the "blue on dark blue" failure where text visually disappears.

1. **On dark surfaces** (Ink `#0A1220`, Deep Navy `#1B2848`, Signature Gradient, Dark Gradient, Vivid Gradient):
   - Default text is **White** (`#FFFFFF`).
   - Secondary / supporting text is White at 70–85% opacity.
   - **Solid blue fills** (Core Blue, Mid Blue, Sky Blue) as text color are **prohibited** - blue letters on dark-navy background fail WCAG contrast.
   - **Gradient text** is permitted only for **headline-scale display text** (typically ≥ 40 pt), where the violet end of the gradient provides the contrast. Below 40 pt - eyebrows, labels, captions, body - text is always **White**. **Gradient text must follow the Gradient Text Safety Contract (§8).**
2. **On light surfaces** (Off-White `#F5F5F5`, White card fills):
   - Default text is **Ink**.
   - Secondary / supporting text is Ink at 55–75% opacity.
   - **Gradient text** is permitted for single-word emphasis and display-scale text (stat numbers, key headline words). **Gradient text must follow the Gradient Text Safety Contract (§8).**
3. **Gradient decoration** (stripes, underlines, highlights, pill fills) is permitted **on all surfaces** - decorative bars carry enough visual weight to read on any background regardless of size.
4. **Accessibility floor**: all text - including gradient text - must meet WCAG AA (≥ 4.5:1 contrast for text under 18 pt, ≥ 3:1 for text ≥ 18 pt bold or 24 pt regular) against its actual rendered background. When in doubt, default to White on dark and Ink on light.

## 3. Typography for Slides

### Font Family
- **Roboto** for everything. Canonical weights: **300, 400, 500, 700, 900** plus **400 italic** (pull quotes only). Nothing else.
- TTFs ship with the skill at `assets/fonts/Roboto/` (Apache 2.0). Every generated PPTX embeds them automatically (see §12.1 rule 7) so client machines without Roboto installed still render the deck correctly.
  - PowerPoint / Keynote: the embedded fonts travel with the file.
  - Google Slides: Roboto is built in; embedding is irrelevant but harmless.
  - PDF export: embedded fonts render correctly regardless of source machine.
- Fallback to **Arial** is permitted only when the target platform strips embedded fonts (strict corporate templates). Never Calibri, never Times.

### Slide Type Scale (16:9, 13.333″ × 7.5″)

| Role | Size (pt) | Weight | Line height | Use |
|------|-----------|--------|-------------|-----|
| **Mega title** | 80 pt | 700 | 1.05 | Cover / closing slide single statement |
| **Title** | 54 pt | 700 | 1.10 | Content slide headline |
| **Section divider** | 72 pt | 700 | 1.10 | "Section 01 / Why now" slides |
| **Sub-headline** | 32 pt | 400 | 1.30 | Supporting line under a title |
| **Body** | 20 pt | 400 | 1.35 | Paragraphs and main bullets |
| **Secondary body** | 16 pt | 400 | 1.40 | Sub-bullets, captions inside cards |
| **Stat number** | 120 pt | 700 | 1.00 | Single-number slides |
| **Stat label** | 16 pt | 500 | 1.20 | Under-number caption (uppercase, +1.5 pt tracking) |
| **Eyebrow / Kicker** | 14 pt | 500 | 1.30 | Uppercase section label, +1.5 pt tracking |
| **Footer / Page #** | 10 pt | 400 | 1.20 | Slide-footer metadata |
| **Quote** | 40 pt | 400 italic | 1.25 | Pull quotes |
| **CTA button label** | 20 pt | 500 | 1.00 | "Get started" pill text |

### Principles
- **Large type, one idea per slide.** Never below 14 pt for on-screen copy. Under 20 pt should be rare and deliberate.
- **Two weights only**: Roboto **400** for body, **700** for headlines. Skip 300/500/600 - the scale carries hierarchy, not weight.
- **Italic is reserved for pull quotes** and the rare inline emphasis.
- **Letter-spacing**: slightly negative on headlines ≥ 40 pt (−0.3 pt). Positive and wide (+1.5 pt) on uppercase eyebrows only.
- **Left-align by default.** Center-align is only for cover, section dividers, closing, and single-number stat slides.
- **No all-caps in body copy.** Uppercase is reserved for eyebrows, labels, and stat captions.

### Gradient Text Treatments (three only)
All three work directly inside PowerPoint's text fill (Format Shape → Text Options → Text Fill → Gradient Fill) and inside Google Slides via the "Gradient text" effect on a masked shape.
1. **Gradient Highlight** - a filled rectangle (30° Signature Gradient) sitting behind one or two key words, white text on top. Best on dark slides.
2. **Gradient Text** - the letters themselves carry the 30° gradient. Apply to **one headline word** only, never a full line.
3. **Gradient Underline** - a 2.5 pt, 30° gradient bar sitting 6 pt below a word. Used inline or under an eyebrow.

## 4. The Arrow - Signature Mark

The Arrow is the single most distinctive graphic device in the deck system. It is the stylized up-right arrow, with the notched tail that cites the three stripes of the REE lettermark. Master file: `assets/logo/Arrow-Up.svg`.

### Anatomy
- Native viewBox: **47.27 × 46.43** (essentially 1:1). Treat it as a **square**.
- Native fill: **`#F5F5F5`** (Off-White). Change the fill to adapt the arrow to context - do not add strokes, do not re-draw.
- Direction: **up-right, always.** To point in other directions, rotate in 90° increments. **Do not horizontally flip** - the geometry is asymmetric (the tail is notched on one side) and a mirror reads as broken.

### Scale on a slide (13.333″ × 7.5″ canvas)
| Role | Size | Use |
|------|------|-----|
| **Inline accent** | 0.35 in (25 pt) | Bullet replacement, eyebrow suffix, inline link mark |
| **Small** | 0.6 in (43 pt) | Card corner mark, footer accent |
| **Medium** | 1.2 in (86 pt) | Title slide corner accent, stat slide side element |
| **Large** | 3.0 in (216 pt) | Section divider hero element |
| **Display** | 6.0 in (432 pt) | Closing slide centerpiece; cover slide watermark (reduce opacity) |

### Fill rules
| Background | Arrow fill | Rationale |
|------------|-----------|-----------|
| Ink / Deep Navy | `#F5F5F5` (native) | Maximum contrast, brand-canonical |
| Off-White | `#0A1220` (Ink) | Invert the fill - never leave as #F5F5F5 on off-white |
| Signature Gradient | `#FFFFFF` | Pure white for lift |
| Image / photo | `#FFFFFF` | Pure white only; add a 20% scrim behind the arrow if contrast is weak |
| **Hero moment** (closing, cover) | Signature Gradient (30°) | The arrow itself becomes the gradient - reserved for one arrow per deck |

### Rotation
- **0° (up-right)** - default, forward momentum. Default on 95% of slides.
- **90° CW (down-right)** - pointing at a chart detail or into content below.
- **180° (down-left)** - retrospective framing ("where we started"). Rare.
- **270° CW (up-left)** - pairing with up-right arrow for bidirectional concepts (before/after).

### Position (strict)

The arrow watermark has **one canonical position**: **flush with the top edge and the right edge** of its container. Expressed in CSS: `top: 0; right: 0;`. In PowerPoint/Google Slides: the top-right corner of the arrow bounding box touches the top-right corner of the slide (or of the panel, when placed inside a sub-container like a side panel or a card).

- The arrow **must be fully visible** on the canvas - every pixel of its bounding box is inside the slide. It **never** bleeds off the top, right, left, or bottom edge.
- Do not crop the arrow with `overflow: hidden`, picture masks, or negative offsets. No part of the mark may be cut by the slide boundary.
- Do not drift the arrow inward from the corner. It is **flush** - touching both edges.
- Rotation stays at 0° (up-right). The arrow's head points at the top-right corner; the notched tail extends down-left into the canvas, leading the eye toward the content.
- Only **one arrow watermark per slide**. If a slide has multiple panels (e.g., a split-layout intro), only one panel carries the watermark.

### Size on a slide (proportional to the container)

Sized as a percentage of the container's width so the arrow reads at the same relative scale regardless of canvas size.

| Container | Arrow width (of container) | Example on 13.333″ canvas |
|-----------|---------------------------|---------------------------|
| Full-slide cover / section divider / closing | **32–35%** | ~4.3–4.7 in |
| Full-slide content (subtle accent) | **18–22%** | ~2.4–2.9 in |
| Half-slide or main panel of a split | **38–45%** | ~2.5–3.0 in |
| Narrow sidebar (service slides) | **35–45%** | proportional |
| Standalone card (inside a grid of cards) | **35–45%** | proportional |

Opacity stays within:
- **6–10%** on dark/gradient surfaces
- **4–6%** on light surfaces

### Do / Don't
- **Do** place the arrow flush at `top: 0; right: 0;` of its container.
- **Do** keep the arrow square - never stretch horizontally or vertically.
- **Do** rotate in 90° steps only.
- **Do** fill with a solid brand color or the gradient - never leave half-transparent with a stroke outline.
- **Don't** crop the arrow. No part of it may be cut off by the canvas edge.
- **Don't** bleed the arrow off-canvas with negative offsets. Flush, not overflowing.
- **Don't** drift inward from the corner. The top-right corner of the arrow box touches the top-right corner of the container.
- **Don't** flip the arrow horizontally. It's directional.
- **Don't** skew, shear, or apply perspective.
- **Don't** place two watermarks on the same slide - one arrow per slide.

## 5. Logo Lockups on Slides

Only **two wordmark variants** exist. There is no lettermark, no app-icon mark, no monogram.

- **Gradient Wordmark** - `assets/logo/Gradient-Logo.svg` (HTML) / `assets/logo/Gradient-Logo@2x.png` (PPTX). Carries the Signature Gradient (30°, `#2665E2 → #C26DE6`). The default mark on all light surfaces (Off-White, white cards, white strips).
- **White Wordmark** - `assets/logo/White-Logo.svg` (HTML) / `assets/logo/White-Logo@2x.png` (PPTX). Solid `#ffffff`. The default mark on all dark / gradient surfaces (Ink, Deep Navy, Signature-Gradient backgrounds).

### Placement on slides
- **Cover slide (Signature Gradient bg)**: White Wordmark, centered horizontally, anchored at vertical center (slight optical lift of −0.3 in). Height ~0.9 in.
- **Content slides (top-right brand stamp)**: Choose the variant that contrasts with the local surface at the top-right. On white/Off-White top strips, use the Gradient Wordmark. On Ink/Deep Navy surfaces, use the White Wordmark. Height ~0.5 in. Anchored ~0.4 in from the top, ~0.4 in from the right.
- **Closing slide (Signature Gradient bg)**: White Wordmark, centered horizontally, anchored at ~80% vertical. Height ~0.7 in.

### Clearspace
Maintain clearspace equal to the **height of the "R" in the wordmark** on all four sides. Nothing - no text, no line, no other graphic - may enter that zone.

### Selection rule (strict)
If the background is light → Gradient Wordmark.
If the background is dark or uses the Signature Gradient → White Wordmark.
Never apply a CSS filter, recolor, or duotone effect to either file. If a surface needs a different mark, switch files; don't re-tint.

### Minimum sizes
- Wordmark: **0.6 in height** (deck footer minimum)
- Lettermark: **0.4 in height** (the REE symbol alone)
- Never scale below these - the stripes in REE lose legibility.

## 6. Slide Templates

All templates target **16:9, 13.333 in × 7.5 in**. Google Slides (10 in × 5.625 in) uses the same proportions - multiply margins by 0.75.

### 6.1 Cover Slide
- **Background**: Ink (`#0A1220`) solid, or Dark Gradient (30°, #1B2848 → #0A1220).
- **Arrow**: Display size (6 in), top-right, bleeding off-canvas by 1.5 in. Fill: Off-White at **8% opacity**.
- **Eyebrow** (optional): 14 pt, Gradient Text, uppercase, top-left at margin `0.8 in from left, 0.8 in from top`.
- **Title**: Mega title, 80 pt, white, weight 700. Left-aligned, anchored at `0.8 in from left, vertical center − 0.5 in`. Max width **9 in**.
  - Use **one Gradient Highlight** on one or two key words.
- **Sub-headline**: 24 pt, Off-White at 78% opacity, directly under title with 32 pt gap. Max width **8 in**.
- **Logo**: White Wordmark at **0.8 in height**, bottom-left, **0.5 in from left, 0.5 in from bottom**.
- **Date/author**: 12 pt Off-White at 55% opacity, bottom-right, **0.5 in from right, 0.5 in from bottom**.

### 6.2 Section Divider
- **Background**: Signature Gradient full-bleed (30°, Core Blue → Mid Violet).
- **Arrow**: Large (3 in), right-center of slide, fill **White**.
- **Section number**: 14 pt eyebrow, white, uppercase, top-left (`0.8 in, 0.8 in`).
  - Format: `SECTION 02 / 05`.
- **Section title**: Section divider size, 72 pt, white, weight 700, left-aligned, vertically centered. Max width **7 in**.
- **One-line description**: 20 pt, white at 85% opacity, directly under title.

### 6.3 Content Slide - Single Column
- **Background**: Off-White.
- **Eyebrow**: 14 pt Gradient Text, top-left (`0.6 in, 0.6 in`), with a **2.5 pt, 120 pt-wide gradient stripe** directly below at `0.6 in, 0.9 in`.
- **Title**: 54 pt Ink, weight 700, left-aligned, starting at `0.6 in from left, 1.2 in from top`. Max width **11 in**.
- **Body**: 20 pt Ink, 1.35 line height. Starts 32 pt below title. Max width **9 in**.
- **Small arrow accent** (optional): 0.35 in inline arrow in Core Blue, replacing bullet markers.
- **Footer**: Gradient Wordmark 0.3 in height bottom-left; page number bottom-right.

### 6.4 Content Slide - Two Column (50/50 split)
- **Background**: Off-White.
- **Left column**: text block, starts at `0.6 in from left`, width **5.5 in**.
  - Eyebrow + gradient stripe
  - Title (40 pt)
  - Body (20 pt)
- **Right column**: image, card, or diagram, starts at `7.0 in from left`, width **5.7 in**.
  - **Right-column card**: 16 pt corner radius, `#FFFFFF` fill, subtle shadow (0 pt × 4 pt Y, 16 pt blur, Ink at 8% alpha).
- **Footer** as standard.

### 6.5 Stat Slide (Big Number)
- **Background**: Ink or Off-White.
- **Stat number**: 120 pt, weight 700, Signature Gradient fill (text gradient), center-aligned, vertically at `1/3 from top`.
- **Stat label**: 16 pt uppercase, +1.5 pt tracking, weight 500, directly under number with 24 pt gap. Max width **6 in**.
- **Supporting sentence**: 20 pt, 400, center-aligned, 40 pt below label. Max width **8 in**.
- **Small arrow accent**: 0.6 in, below supporting sentence with 40 pt gap, fill Core Blue or gradient.

### 6.6 Three-up Card Row
- **Background**: Off-White.
- **Standard eyebrow + title row** at top (see 6.3).
- **Three cards**: evenly distributed across `0.6 in → 12.7 in` (usable width 12.1 in, card width ~3.8 in, gap 0.25 in).
- **Card anatomy**:
  - Fill: white.
  - Radius: 16 pt.
  - Padding: 24 pt.
  - Shadow: 0 pt × 4 pt, 16 pt blur, Ink at 6% alpha.
  - Icon: 32 pt tall line-style icon, Core Blue stroke, top of card.
  - Card title: 20 pt, 700, Ink, 16 pt below icon.
  - Card body: 14 pt, 400, Ink at 72% opacity, 8 pt below title.
  - Optional "Arrow mark": Small arrow (0.5 in), Core Blue, bottom-right corner of card.

### 6.7 Quote Slide
- **Background**: Deep Navy (`#1B2848`) or Off-White.
- **Opening mark**: 140 pt gradient-text `"` glyph, top-left at margin.
- **Quote**: 40 pt italic, weight 400, centered between opening mark and attribution. Max width **10 in**, center-aligned.
- **Attribution**: 16 pt, weight 500, eyebrow-style (uppercase, +1.5 pt tracking). Gradient text for the name, neutral color for role/company. Below quote, 40 pt gap.

### 6.8 Closing Slide
- **Background**: Signature Gradient, full-bleed, 30°.
- **Display arrow**: 6.0 in, centered at `2.5 in from top`, fill White.
- **Mega message**: 64 pt, white, 700, centered, under arrow.
- **CTA**: rounded-pill button (see §7), solid white fill with Ink text, 40 pt gap below message.
- **Logo**: White Wordmark at 0.8 in height, bottom-center, 0.5 in from bottom.

### 6.9 Agenda / Table of Contents
- **Background**: Off-White.
- **Layout**: Two columns.
  - Left: "AGENDA" eyebrow + gradient stripe, then "Today's agenda" 54 pt title.
  - Right: numbered list (1 / 2 / 3…), each row with:
    - Large number (40 pt gradient text, weight 700, 0.8 in column width)
    - Section label (24 pt Ink, 700)
    - Short description (14 pt Ink at 65% opacity)
    - Row separator: 0.5 pt Ink at 12% alpha, 16 pt below row.

## 7. Components

### Button / CTA

There is **no SVG button library**. When a CTA is required, build it from brand primitives - a pill drawn from fill, Roboto label, and optionally the Arrow-Up.svg next to the label. Decks rarely need interactive buttons; most "book a call" or "learn more" moments are handled by the speaker, not by the slide.

**Canonical pill specification** (when a CTA is needed):
- **Shape**: pill, radius **29 pt** (half the 58 pt button height).
- **Height**: 58 pt. **Padding**: 16 pt top, 28 pt sides, 18 pt bottom.
- **Label**: Roboto 500, 20 pt, sentence case - never all-caps.
- **Fill options** (pick one):
  - **Primary**: Core Blue (`#2665E2`) solid, white label. Subtle Core-Blue-tinted shadow (0 pt × 4 pt, 12 pt blur, Core Blue at 25%).
  - **Gradient**: Signature Gradient (30°, `#2665E2 → #C26DE6`), white label. Reserved for cover and closing CTAs only.
  - **White-on-gradient**: white fill, Ink label. Reserved for closing slides where the full-bleed gradient is the background.
- **Optional Arrow-Up.svg**: placed 12 pt to the right of the label, 22 pt tall, fill-matched to the label color (white on colored pills, Ink on white pills). Rotation 0°.

#### CTA usage rules (strict)

1. **Build CTAs from primitives only.** Pill shape, color fill, Roboto label, and optionally Arrow-Up.svg. Do not inline SVG paths. Do not create or import icon or button SVGs. Do not draw decorative shapes with CSS `clip-path` or `border-radius` hacks.
2. **One primary CTA per slide.** If a slide presents two actions, only one may carry the primary fill; a secondary action must be a plain underlined text link in Core Blue (no pill).
3. **Reserved for cover, closing, and service-detail slides.** CTAs do not appear on content, stat, quote, section-divider, or data slides.
4. **No hover or motion states in static decks.** Hover styling is an HTML-demo affordance only. Exported PPTX/PDF slides render one fixed state.
5. **No custom colors.** CTAs use one of the three documented fills. Do not introduce orange, green, or any non-brand hue.
6. **The bullet marker (`Upwards-Arrow`) is decoration, not a button.** See Bullet List component. Bullets are never clickable, never links, never carry hover states.
7. **Button content is always center-aligned horizontally within the button.** Label and optional Arrow form a single content block, centered. Button width is intrinsic - it hugs the content plus symmetric padding. The label is never pinned left with the arrow pushed right, and there is never asymmetric padding on either side.

### Bullet List

Bulleted lists use a single canonical marker and obey a strict set of rules. Sloppy bullets - wrapped text, inconsistent cadence, substitute markers - are a brand violation.

**Marker**: always `assets/logo/Upwards-Arrow.svg` (HTML) / `assets/logo/Upwards-Arrow@2x.png` (PPTX). A Core Blue rounded square containing the up-right arrow. No dots, no dashes, no checkmarks, no CSS-drawn rounded-squares, no pseudo-elements.

**Size**: marker height ≈ **1.6 × the label's cap-height** (so the bullet reads a hair larger than the text and visually anchors the row).

**Layout**: bullet + label on one row. Vertical alignment: center. Horizontal gap between bullet and label: ≈ half the label's cap-height.

**Row spacing**: 8–12 pt between consecutive bullet rows.

#### Bullet list rules (strict)

1. **One marker, always.** `Upwards-Arrow` is the only bullet permitted in the Reeinvent system. No other marker - ever.
2. **One line per item - always.** No bullet text may wrap to a second line. Enforce with `white-space: nowrap` in HTML/CSS, or by keeping copy short in PPTX.
3. **Copy as tight as possible.** Bullets are scan-ready summaries, not sentences. If an item genuinely needs two lines, split it into two bullets or move the content out of the list into body copy.
4. **Consistent grammatical cadence.** Every item in a given list follows the same shape - all noun phrases ("24/7 drift monitoring"), or all verb phrases ("Monitor drift"), or all adjective-led phrases ("Fast · Robust · Scalable"). Never mix shapes inside one list.
5. **No more than 6 items per list.** Past six, the reader stops scanning and starts skipping. Split into two lists or choose a different layout (e.g., a card row).
6. **Bullet marker is decoration, not a link.** The arrow-in-circle is never clickable, never hover-styled, never linked.

### Card
- **Fill**: White on light slides, Deep Navy on dark slides.
- **Radius**: 16 pt (standard), 24 pt (hero cards).
- **Padding**: 24 pt (compact), 32 pt (standard).
- **Shadow**: 0 pt × 4 pt, 16 pt blur, Ink at 6–10% alpha. **Never use black shadows** - always Ink-tinted.
- **Badge** (optional top-right): pill shape, 24 pt tall, 12 pt horizontal padding, Signature Gradient fill, white 10 pt uppercase label with +1 pt tracking.

### Stat Block
- Large gradient-text number (80–120 pt).
- Under-label in 14 pt uppercase, +1.5 pt tracking, Ink at 60% opacity.
- Optional small Arrow (0.35 in) to the right of the number, Core Blue, for "growth" context.

### Callout / Pull Quote Block
- Full-width block within a content slide.
- Left border: 3 pt gradient vertical stripe (30° gradient, rotated to vertical, 100% height of block).
- Content: 24 pt italic Ink, left-aligned, 32 pt left padding from stripe.
- Max height ~2.5 in on a content slide.

### Chart
- **Axis labels**: 12 pt, Ink at 65% opacity.
- **Gridlines**: 0.5 pt, Ink at 8% alpha.
- **Bars/Lines**: use Chart palette order from §2.
- **Highlighted series**: Core Blue at 100%, all other series at 40% opacity (greyed).
- **Title above chart**: treated as Card title (20 pt, 700).
- **Data labels**: only on the one series you want the audience to read - avoid label clutter.

### Iconography on Slides
- **Style**: line, 2 pt stroke, rounded caps and joins.
- **Grid**: 32 pt icon on cards, 48 pt on hero slides.
- **Color**: Core Blue on light slides, Off-White on dark slides.
- **Theme family**: exploration and flight - **rockets, hot-air balloons, space shuttles, launchpads, orbits**. Reeinvent's brand metaphor is velocity and lift, not generic tech.
- **The Arrow is not an icon.** It is a standalone mark. Don't place it in the icon row.

## 8. Gradient Usage on Slides

Three treatments, applied deliberately.

1. **Full-bleed background** - Signature or Dark Gradient fills the entire slide. Reserved for Cover, Section Dividers, and Closing slides. Never for dense content slides.
2. **Gradient Highlight** (behind text) - a filled rectangle (4 pt corner radius) behind one or two words in a headline. On dark slides. One per slide maximum.
3. **Gradient Text** - the letters themselves carry the gradient. One word per headline. Works on both dark and light.
4. **Gradient Stripe** - a 2.5 pt horizontal bar sitting under an eyebrow or section label. **Width matches the text width above it exactly**, aligned left with that text (extending from the text's left edge to its right edge). The stripe is never a fixed width; it always traces the label it belongs to. Use freely - this is the repeating brand detail.
5. **Gradient Underline** - a 2.5 pt gradient bar beneath a word or link, 6 pt below baseline.

### Gradient Underline Rules (strict)

1. **One line only.** A gradient underline may never span more than one line of text. If the emphasized phrase would wrap, split it into per-word underlines (each fitting on its own line) or switch to Gradient Highlight.
2. **Short phrases only.** 1–3 words maximum per underline. Longer emphasis reads as decoration, not intent.
3. **Headlines only.** Never underline body copy, captions, bullets, or eyebrow labels. Eyebrows carry the Gradient Stripe instead; body copy uses inline **bold** for emphasis.
4. **One underline per slide - always.** No exceptions. Applies equally to cover, intro, section-title, content, stat, quote, and closing slides. Two stacked underlines on the same slide visually compete and read as decoration rather than intent.
5. **Position & thickness**: 2.5 pt thick (≈ 0.18em at headline sizes), sits 6 pt below the baseline (≈ 0.15em offset at headline sizes). Width matches the text width exactly - no horizontal padding or bleed.
6. **Don't stack treatments on the same word.** If a word carries Gradient Text, it does not also carry a Gradient Underline. Pick one treatment per word. Gradient Highlight likewise - never combined with an underline on the same word.

### Gradient Text Safety Contract (strict - prevents render clipping)

`background-clip: text` is the CSS technique used to fill letter shapes with the gradient. It has known failure modes at display scale where glyph outlines extend beyond the element's paint box and get clipped (the "`98%` with the bottom of the `%` cut off" failure). This contract is mandatory for every gradient-text element in HTML, web exports, and interactive PDFs. PPTX/Keynote/Google Slides use native gradient-fill text features and render correctly without the contract.

Every gradient-text element must satisfy ALL of the following:

1. **`display: inline-block`.** Shrinks the paint box to the content, producing clean glyph boundaries. Never use `background-clip: text` on a block-level `<div>` that fills its parent.
2. **`line-height: 1.4` minimum.** Roboto's natural metrics at display scale need this much vertical room or glyph curves (`%`, `8`, `6`, `9`, descenders, antialiasing halos) fall outside the paint box. Never set line-height below 1.4 on gradient text.
3. **Vertical padding: `0.15em` top and bottom minimum.** Buffer inside the paint box so even the outermost antialiasing pixels paint correctly.
4. **Both `color: transparent` AND `-webkit-text-fill-color: transparent`.** The `-webkit` property is the actual WebKit/Blink rendering instruction; `color: transparent` is the Firefox/standards fallback. Always set both.
5. **One font-size per gradient-text element.** Never mix two font sizes inside a single `background-clip: text` element (no `<div class="grad-text">98<span style="smaller">%</span></div>`). If a display group has two sizes (like `98` + `%`), **split them into two independent gradient-text elements**, each sized and styled on its own. The gradient paints cleanly per element.

**Fallback when the contract can't be satisfied**: use solid Core Blue (`#2665E2`) instead of gradient text. Solid color has zero rendering risk.

### Angle
Always **30°** in PPTX. In PowerPoint's gradient editor, set the angle to 30° explicitly - don't use "Diagonal Top Left to Bottom Right" which is 135°.

## 9. Spacing & Grid

### Slide margins (16:9, 13.333″ × 7.5″)
- **Safe area**: 0.5 in on all sides (no content outside this).
- **Standard text margin**: 0.6 in from left/right, 0.6 in from top for content slides.
- **Title block top margin**: 0.6 in from top, 1.2 in from top to headline baseline.
- **Footer area**: bottom 0.85 in reserved for logo + page number.

### Horizontal grid
Use a **12-column grid**:
- Gutter: 0.2 in
- Column width: ~1.0 in each
- Usable width: 12.1 in

Common column spans:
- Full-width block: **12 cols (12.1 in)**
- Two-column 50/50: **6 cols each** with 0.4 in gutter → 5.85 in per column
- Three-column cards: **4 cols each** with 0.25 in gutter → 3.85 in per card
- 60/40 split: **7/5 cols** → 7.05 in / 5.05 in

### Vertical rhythm
- Headline → body gap: **32 pt**
- Body paragraph gap: **16 pt**
- Section gap (within a slide): **48 pt**
- Eyebrow → title gap: **12 pt**

### Vertical anchoring for sparse content (strict)

Content must never be top-anchored with empty space below. Sparse slides read as "cut off" when the block sits at the top with half the canvas unused.

1. **Header + one content block** (eyebrow + title at top, then a card row / image / quote / bullet list): the content block is anchored to the **bottom of the safe area**, just above the bottom padding. The header sits at the top. The space between breathes.
2. **Only a content block, no header** (e.g., three cards alone): the block sits in the **lower two-thirds** of the slide. Never the upper half.
3. **Centered vertical alignment** is acceptable when the content block is visually heavy and the resulting top-and-bottom whitespace would look balanced.
4. **Top-anchored content** is correct only when a footer element (page number, URL, continuation cue) grounds the bottom of the slide.
5. Equivalently in CSS: on flex/grid slides with `auto 1fr` row templates, use `align-items: end` on the content block, not `start`.

## 10. Animation & Transitions (for .pptx / Google Slides)

Decks look better when they don't animate - but when motion is used, it must be restrained.

- **Slide transition**: **Fade**, 0.3 s. Use nothing else. No push, no dissolve, no fancy 3D.
- **On-slide build**: **Appear** or **Fade In**, 0.15 s. Never "Fly In from left".
- **Arrow entrance** (section divider): Fade + scale 0.95 → 1.0, 0.4 s, ease-out. One arrow animation per deck - on the cover or section 01 - not repeated.
- **Charts**: Fade each series in, 0.15 s, stagger 0.1 s. Never use category-by-category reveals - they slow presenters down.

## 11. Do's and Don'ts (Deck-Specific)

### Do
- Use Roboto 700 for titles, 400 for body - nothing else.
- Keep headlines under **10 words**.
- Put **one idea per slide**.
- Keep body text at **20 pt or larger**.
- Apply Gradient Highlight to only **one or two words per headline**.
- Use the Arrow at the documented scales - don't invent new sizes.
- Alternate dark and light slides to create rhythm.
- Set gradients to **30°** explicitly.
- Export PDFs with Roboto embedded.
- Use 16:9 (13.333 × 7.5 in). Don't use 4:3.

### Don't
- **Don't** use Calibri, Times, or the default PowerPoint fonts.
- **Don't** put more than ~40 words on a content slide.
- **Don't** use pure black (`#000`) - use Ink (`#0A1220`).
- **Don't** use pure white for page backgrounds - use Off-White (`#F5F5F5`).
- **Don't** flip the Arrow horizontally.
- **Don't** use clip-art, stock illustrations, or emoji in place of iconography.
- **Don't** mix the Signature Gradient with another accent color. Blue and violet belong together **only through the gradient**.
- **Don't** apply gradient text to body copy - it fails contrast.
- **Don't** use more than **one** full-bleed gradient background in three consecutive slides.
- **Don't** use fly-in or spin transitions. Fade only.
- **Don't use the em-dash character (Unicode U+2014) anywhere. Ever.** Not in headlines, body copy, captions, speaker notes, filenames, or any other text. Replace with a hyphen (`-`), colon (`:`), semicolon (`;`), or a full stop depending on the sentence. This applies to every Reeinvent text surface: decks, docs, layouts, and brand guidelines. The glyph itself does not appear anywhere in this document.

## 12. Export & Format Tips

### PowerPoint (.pptx) - customizability requirements (strict)

Every PPTX deck Claude generates must be **fully editable by the presenter in PowerPoint / Keynote / Google Slides.** A flattened, image-only deck fails this rule. The presenter must be able to change text, move shapes, re-skin colors, and add new slides from the existing layouts without recreating anything from scratch.

**Generation engine: python-pptx only.** Never use PowerPoint automation (AppleScript, osascript, the PowerPoint app's scripting interface), Keynote scripting, or macro-based generation. The Anthropic `pptx` skill (which wraps python-pptx) is the preferred path - invoke it via the Skill tool rather than writing raw python-pptx code from scratch. If python-pptx cannot produce the required output, apply rule 10 below (halt and report) instead of switching engines.

1. **Live editable text.** Every text element is a native PowerPoint text frame (`TextFrame` in python-pptx). Never rasterized, never converted to shapes or paths, never embedded as an image.
2. **Native shapes.** Cards, pills, cover backgrounds, gradient fills, stripe accents, underlines, callout bubbles are PowerPoint shape objects (`Slide.shapes.add_shape()`, `.add_textbox()`, etc.), not flattened images.
3. **Brand assets as picture objects - PNG, not SVG.** The four canonical brand marks go in via `Slide.shapes.add_picture()` using the `@2x.png` variant from `assets/logo/`, never the SVG. PPTX and Google Slides render SVG imports unreliably (gradient collapse, placeholder rectangles, missing fills); PNG is universally reliable. The presenter can still reposition or resize the picture object. Alt text is always set (`picture.alt_text = "Reeinvent arrow"` etc.) for accessibility and Selection Pane navigation. See §14 for the routing rule.
4. **Theme Colors defined.** The 9 canonical hex codes are registered as PPTX Theme Colors in the `theme1.xml` of the .pptx package. Shape fills reference Theme Color slots (for example `MSO_THEME_COLOR.ACCENT_1` mapped to Core Blue) rather than hard-coding RGB on every shape. This lets a global palette change propagate.
5. **Theme Font set to Roboto** with Arial as fallback. Set via the theme's Major Font + Minor Font definitions.
6. **Slide Master + Layouts per archetype.** The Slide Master defines the wordmark stamp, footer page number, and default typography. One Slide Layout exists per production archetype (cover, section divider, service detail, stat, contact, closing, agenda, etc. per `reference.md`). When the presenter adds a new slide from the "New Slide" menu, each layout is available as a brand-correct starting point.
7. **Fonts embedded via post-processing.** python-pptx itself does not write embedded-font parts - you must run `python scripts/embed-fonts.py OUTPUT.pptx` after python-pptx saves. The script injects the six TTFs from `assets/fonts/Roboto/` as OOXML `ppt/fonts/*.fntdata` parts and registers the `<p:embeddedFontLst>`, so the deck renders correctly on any machine without Roboto installed. **Not optional.** A .pptx without embedded Roboto falls back to Arial on client machines and is a brand violation.
8. **Group related elements.** When a title, its gradient stripe, and its eyebrow should move as a unit, group them (`Slide.shapes.add_group_shape()`). The presenter moves one block, not three pieces.
9. **Charts as native charts, not screenshots.** Any stat visualization, bar chart, line chart is a native PPTX chart object the presenter can edit. Not a flattened image.
10. **If any brand element cannot be rendered natively, stop - do not substitute.**
    - **Native rendering** = live text frames, native shape objects, native charts, SVG assets inserted via `Slide.shapes.add_picture()`. Everything in rules 1–9 above.
    - **Prohibited fallbacks** (without explicit user approval): rasterizing text or shapes to PNG/JPG, embedding flattened images of otherwise-native elements, removing the element, simplifying the styling (e.g., replacing gradient text with solid color "because it's close enough"), or switching to a different generation engine.
    - **Required action on failure:** halt generation. Report to the user - (a) which element failed, (b) why native rendering failed, (c) available alternatives ranked by brand fidelity. Wait for a decision before continuing.

**Check before handing off:** open the generated .pptx in PowerPoint, click on any text element, and verify it enters edit mode. Click on any background rectangle and verify it can be moved. If any element is locked as an image, the deck violates this rule and must be regenerated.

### PowerPoint (.pptx) - presenter setup (for context)
- **File → Options → Save → Embed fonts** → check "Embed fonts in the file" and "Embed all characters". Ensures Roboto travels with the deck.
- Slide size: **Design → Slide Size → Widescreen (16:9)** - then **Custom → 13.333 in × 7.5 in** if needed.
- Gradients: Format Shape → Fill → Gradient Fill → Type: **Linear**, Angle: **30°**, two stops at 0% `#2665E2` and 100% `#C26DE6`.

### Google Slides
- Open from `.pptx` import - Google preserves Roboto (built-in), colors, and gradients.
- Slide size: **File → Page setup → Custom** → **13.333 × 7.5 in** (or keep Google's 10 × 5.625 at 16:9 and scale values by 0.75).
- Gradients: use the color picker's "+ Custom" → add gradient via **Shape fill → Gradient**. Google Slides supports 30° angles.
- For Gradient Text, use a filled shape as a mask behind a text outline, or export the headline as an SVG and insert.

### PDF export
- PowerPoint: **File → Save As → PDF** with "High quality" selected.
- Google Slides: **File → Download → PDF**.
- Always test the PDF on a non-author machine - it's the fastest way to catch font embedding failures.
- **Vector assets stay vector** (logo SVG, Arrow SVG, gradients). Raster images (photos) should be 144 DPI minimum for a 1920-wide canvas.

### Accessibility
- Minimum contrast: body text ≥ 4.5:1 against background. Ink on Off-White = 17:1, Core Blue on Off-White = 4.6:1, White on Ink = 17:1 - all pass.
- **Don't rely on color alone** - charts that distinguish series by color must also distinguish by marker shape or line style.
- Add **alt text** to the Arrow ("Reeinvent arrow - indicates direction/progress") and logo ("Reeinvent logo").
- Slide reading order: PowerPoint → Home → Arrange → Selection Pane → reorder so screen readers hit title → body → footer.

## 13. Agent Prompt Guide

When asking an AI agent to generate a slide, include:

**Canvas**: `16:9, 13.333 in × 7.5 in, Off-White background (#F5F5F5)`
**Fonts**: `Roboto 700 for title, Roboto 400 for body`
**Palette**: `Ink #0A1220, Core Blue #2665E2, Mid Violet #C26DE6, 30° gradient`
**Arrow**: `use Arrow-Up mark (SVG for HTML, @2x.png for PPTX) at [size] in, fill [color], rotation [deg]`
**Logo**: `Gradient Wordmark at 0.3 in height, bottom-left (0.5, 7.15 in)`
**Margins**: `content starts 0.6 in from left/top, safe area 0.5 in`

### Example prompts

> "Build a **cover slide** on Ink background. Arrow at 6 in in top-right bleeding off-canvas, fill Off-White at 8% opacity, rotation 0°. Eyebrow 'AI-FIRST ENGINEERING PARTNER' at (0.8, 0.8), 14 pt, Gradient Text, uppercase, +1.5 pt tracking. Title 'From ideas to scalable AI solutions - in weeks.' at 80 pt weight 700 white, anchored bottom-left at (0.8, 4.2 in), max width 9 in, with Gradient Highlight on 'in weeks'. White Wordmark at 0.8 in height, bottom-left (0.5, 0.5 in from bottom). Date '2026-04-21' at 12 pt, 55% white, bottom-right."

> "Build a **section divider** on full-bleed Signature Gradient. 'SECTION 02 / 05' eyebrow top-left, 14 pt white uppercase. 'How we ship in weeks' title 72 pt weight 700 white, left-aligned, vertically centered, max width 7 in. Large Arrow at 3 in, right-center of slide, fill white, rotation 0°."

> "Build a **stat slide** on Off-White. Centered number '6 wk' at 120 pt, Signature Gradient text fill. Label 'AVG. IDEA TO PROD' at 16 pt uppercase +1.5 pt tracking, 24 pt below number. Supporting line 'From first conversation to a system your users can touch.' at 20 pt, 40 pt below label, max width 8 in. Small Arrow at 0.6 in in Core Blue, 40 pt below supporting line."

> "Build a **three-card row** on Off-White. Eyebrow 'WHAT WE BUILD' at top-left with 120 pt gradient stripe below. Title 'Services that take you from idea to scale.' at 54 pt. Three cards at 3.85 in each, 16 pt radius, 24 pt padding. Each card: line-style rocket icon 32 pt Core Blue, title 20 pt 700, body 14 pt 72% Ink, Small Arrow bottom-right corner Core Blue."

### Iteration checklist
1. Is the gradient set to **30°**? (Not 45°, not 135°.)
2. Is the Arrow **not horizontally flipped**? (Only 0/90/180/270 rotations.)
3. Is every text size **≥ 14 pt**?
4. Is there **one idea, one title, one CTA** per slide?
5. Does the footer have the Gradient Wordmark + page number?
6. Is the slide using **Ink/Off-White**, not pure black/white?
7. Is the **Signature Gradient appearing at most twice** across any three consecutive slides?

## 14. Asset Index

The project ships **four brand marks** - each provided as an SVG (for HTML / web) and a PNG at 2x (for PPTX / Slides embedding). These are the only brand graphics permitted anywhere in any Reeinvent deck, layout, or surface. Do not create, import, inline, or redraw anything else.

| Mark | SVG (HTML) | PNG (PPTX) | Canonical use |
|------|------------|------------|---------------|
| The Arrow | `assets/logo/Arrow-Up.svg` | `assets/logo/Arrow-Up@2x.png` | The signature mark - background watermarks only. Section-divider decoration, cover / closing watermark. Square, native fill `#F5F5F5`. |
| Gradient Wordmark | `assets/logo/Gradient-Logo.svg` | `assets/logo/Gradient-Logo@2x.png` | The logo on all **light** surfaces. Carries the Signature Gradient. |
| White Wordmark | `assets/logo/White-Logo.svg` | `assets/logo/White-Logo@2x.png` | The logo on all **dark / gradient** surfaces. Solid `#ffffff`. |
| Bullet / Direction Mark | `assets/logo/Upwards-Arrow.svg` | `assets/logo/Upwards-Arrow@2x.png` | The bullet-list marker - **bullets only**. A Core Blue rounded square with a white up-right arrow inside. 56 × 56 native viewBox. Never used as a watermark, decoration, or link button. |

**Asset routing by output format (strict):**
- **HTML / web surfaces** → use the `.svg` file. Browsers render SVG natively at any size.
- **PPTX / Google Slides** → use the `@2x.png` file, embedded via `Slide.shapes.add_picture()`. SVG import is unreliable across PowerPoint versions and Slides imports (gradients collapse to placeholder rectangles, fills drop). PNG at 2x renders identically to the vector at every realistic slide size.
- **PDF via HTML print** → use the `.svg` file (browser handles rasterization at print time).
- **PDF via PPTX export** → use the `@2x.png` file (PPTX is the source).

Do not substitute one for the other outside this routing. Do not re-render PNGs from SVGs on the fly at runtime - the committed PNGs are the only PPTX source of truth.

**Role separation (strict):**
- `Arrow-Up` → watermarks / backgrounds / cover decorations. Never a bullet.
- `Upwards-Arrow` → bullet list markers. Never a watermark, never clickable, never decoration outside of lists.
- The two Arrow marks are **not interchangeable**. Each has one job.

**Not available, do not invent:**
- No lettermark (REE-only symbol)
- No app-icon-style mark
- No button or CTA SVG library
- No icon set (rockets, balloons, checkmarks, chevrons - none)
- No alternate color variants (orange, green, monochrome-black, etc.)

If a design appears to need something not in this table, the answer is either "use one of the four" or "ask the user before adding a new asset." Never add without approval.
