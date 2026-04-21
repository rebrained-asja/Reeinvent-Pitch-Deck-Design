# Reeinvent Deck - Pattern Reference

> **Purpose.** This document catalogs how Reeinvent's design system is **actually used** in production decks. It is a companion to [DESIGN.md](DESIGN.md) - where DESIGN.md states the rules, this document shows the slide archetypes those rules combine into. Source: *REE 2.0 – Master Company Presentation* (21 slides). Use this as a starting library when building new decks so the output matches the house style without reinventing the wheel.

## Global Patterns Observed Across the Deck

These patterns appear on most slides and should be treated as the deck's connective tissue.

### Brand stamp (top-right corner)
- **Every content slide** carries the Reeinvent wordmark in the **top-right corner**, at ~0.5 in height.
- On light strips: Blue Wordmark. On dark areas: white recolor.
- Position: anchored `~0.4 in from right, ~0.4 in from top`.
- Never moves to another corner. This is the silent signature on every page.

### The "AI-DRIVEN [WORD]" pattern
- Service and section headers follow the format: `AI-DRIVEN PROTOTYPING`, `AI-DRIVEN SOLUTIONS`.
- **Style**: the first part (`AI-DRIVEN`) is Ink/dark navy, **weight 300 (thin)**, uppercase.
- The second word (`PROTOTYPING`, `SOLUTIONS`) is **gradient text**, uppercase, **weight 700 (bold)**.
- Size: **72–80 pt**, left-aligned at the top of the slide.
- This two-word header is Reeinvent's signature slide-title device.

### Gradient underline on headline emphasis
- Long headlines (like "YOUR **AI-DRIVEN SOFTWARE** COMPANY") apply the **Gradient Underline** under the emphasized words, not gradient-highlight or gradient-text.
- Underline is ~3 pt thick, blue-to-violet gradient, sitting 4–6 pt below the baseline.
- Use for 1–3 consecutive words in a title - never the whole line.

### Bolding inside body copy
- Body paragraphs use Roboto 400 as the base, but **select key phrases are set to 700** inline.
- Example: *"We help companies **identify** where AI creates **real value** & **build the solutions** to deliver it."*
- Rule: bold 2–4 noun phrases per paragraph. The bolding is the scannable skeleton - the reader gets the meaning even without reading every word.

### Chat-bubble callouts (rounded-square card with a pointing tail)
- Small white rounded-rectangle card (8 pt radius), containing a single-line promise in gradient or dark text.
- Has a small pointed tail attached to one edge (triangle, 12–16 pt), indicating the element it's labeling.
- Used for: taglines next to service names, client descriptors above success-story content.
- Examples seen: *"Long-term agentic innovation platform"*, *"Concept refined into a testable prototype"*, *"Investor-ready demo assets that win confidence"*.

### Duration pills (outlined rounded pills)
- Small rounded-pill outlined in white (on gradient backgrounds), containing a duration.
- **Format**: `<1 week`, `1–3 weeks`, `3–5 weeks`, `2–4 weeks`, `6–16 weeks`, `8–16 weeks`, `10–20+ weeks`.
- Size: ~16 pt text, 24 pt tall, 12 pt horizontal padding.
- Sits at the top of the left sidebar on service slides, above the service name.

### Arrow icon as bullet replacement
- In "What's Included" lists, standard bullets are replaced with a **small gradient rounded-square containing the Arrow** (~18 pt tall).
- The rounded-square is filled with Core Blue or the Signature Gradient, arrow is white.
- This is Reeinvent's house bullet - it should be used in every feature list instead of circles or dashes.

### Laptop + screenshot mockup cluster (service detail slides)
- A signature visual device: a **rotated laptop (10–15° clockwise)** displaying a video still (often a founder/team member speaking), with **2–3 website screenshots floating behind it** at slight counter-angles.
- The cluster bleeds off the right edge of the slide.
- Behind the cluster: a dark-navy tinted-photo background (office/context scene) at ~30% opacity.
- This is how every service gets visualized - consistency across the deck.

---

## Slide Archetypes

Every slide in the master deck falls into one of these patterns. Reproduce these directly when building new decks.

### A1 - Cover Slide (Full-Bleed Gradient)
**Seen on**: slide 1 (opening).

**Layout**:
- Full-bleed **Signature Gradient** (30°, Core Blue → Mid Violet).
- **Large Arrow watermark** (~6 in) bleeding off the top-right corner, rotation 0°, fill white at **~12% opacity**.
- **REEINVENT wordmark** centered horizontally, anchored at vertical center (slight optical lift: center − 0.3 in). Height ~0.9 in. White recolor.
- No other content. No date, no speaker, no agenda - this slide is a poster.

**When to use**: every deck opening.

---

### A2 - Section Divider / Chapter Card
**Seen on**: slide 12 (*Success Stories*), slide 21 (*Thank You*).

**Layout**:
- Full-bleed **Signature Gradient** (same as cover).
- **Arrow watermark** top-right, ~12% opacity.
- **Title** centered, **Roboto 300 (thin)**, uppercase, letter-spacing +6 pt, ~60 pt, white.
  - Examples: `SUCCESS STORIES`, `THANK YOU`.
- **REEINVENT wordmark** centered horizontally, anchored at ~80% vertical (`6.0 in from top` on a 7.5 in canvas), height ~0.7 in, white recolor.
- No body copy.

**When to use**: chapter breaks; final slide.

---

### A3 - Intro Split ("Who We Are" pattern)
**Seen on**: slide 2 (*Who We Are - Your AI-Driven Software Company*), slide 17 (*AI-Native Approach*).

**Layout** (two-panel 50/50):
- **Left panel**:
  - **Top half**: photograph (team photo, or REE lettermark on white) filling the full top.
  - **Bottom half**: **Signature Gradient** block, containing a two-line display title.
    - Line 1: upper word in **Roboto 300 thin**, ~72 pt, white.
    - Line 2: final word in **Roboto 900 black/ultra-bold**, ~120 pt, white.
    - Examples: `WHO WE / ARE`, `AI / FIRST`.
- **Right panel** (Ink `#0A1220` fill, subtle arrow watermark at 6% opacity):
  - Top-right: REEINVENT wordmark (white recolor, 0.5 in).
  - **Headline** left-aligned, ~44 pt Roboto 700, white, with **gradient underline** on 1–3 emphasized words. Max 3 lines.
    - Example: `YOUR AI-DRIVEN SOFTWARE COMPANY` with underline under "AI-DRIVEN" and "SOFTWARE".
  - **Body** below headline, 24 pt Roboto 400, white at 95% opacity, with 2–4 inline bold phrases.
    - Example: *"We help companies **identify** where AI creates **real value** & **build the solutions** to deliver it."*

**When to use**: deck introduction slide (slide 2); philosophical "how we think" slides.

---

### A4 - AI-DRIVEN Two-Column Split ("Prototyping / Solutions")
**Seen on**: slide 3 (*AI-DRIVEN Prototyping + Solutions*).

**Layout**:
- **Top title**: `AI-DRIVEN` in Ink thin at left, then the word being split (e.g., `DRIVEN`) transitioning into gradient text. ~120 pt across top.
- **Below**: two side-by-side rounded-square cards (24 pt radius), each 50% width, ~4.5 in tall.
  - **Left card**: **Dark Gradient** fill (Deep Navy → Ink).
  - **Right card**: **Signature Gradient** fill.
- **Each card contains**:
  - Category label at top: **Roboto 900**, white, uppercase, ~60 pt (`PROTOTYPING`, `SOLUTIONS`).
  - Below label: a thin white underline bar, ~60% of the label's width.
  - Two paragraphs of body: 24 pt Roboto 400, white, with 2–3 bold key phrases.

**When to use**: when you have a two-pillar offering that needs equal weight - the "we do X **and** Y" frame.

---

### A5 - Service Detail (The Offer Template)
**Seen on**: slides 4–11 (*Concept Sprint*, *Investor Demo*, *Rapid Prototype*, *AI-Readiness Study*, *UX Redesign*, *Process Automation*, *Custom Apps*, *Product Scaling*).

This is the deck's most-repeated slide. **It's the offer template - any new service fits this mold.**

**Layout**:
- **Top strip** (full-width, ~0.9 in tall, white fill):
  - Left: category header, e.g. `AI-DRIVEN PROTOTYPING` or `AI-DRIVEN SOLUTIONS` in the standard pattern (thin + gradient).
  - Right: REEINVENT wordmark in Blue (0.5 in height).
- **Left sidebar** (~25% width, full remaining height, **Signature Gradient** fill):
  - Arrow watermark behind at ~8% opacity.
  - At top: outlined **duration pill** (e.g., `<1 week`, `3–5 weeks`) - white outline, white text.
  - Below pill: **service name** in two lines:
    - Line 1: Roboto 300 thin, ~54 pt, white (e.g., `CONCEPT`, `RAPID`).
    - Line 2: Roboto 900, ~72 pt, white (e.g., `SPRINT`, `PROTOTYPE`).
  - Below service name: **chat-bubble callout** (white rounded card with triangular tail pointing up at the service name) - one-line promise in dark text.
    - Examples: *"Concept refined into a testable prototype"*, *"Proof of value you can test, demo or pitch"*.
  - At bottom: a short **italic-style tagline**, 20–24 pt white Roboto 400, 2–4 lines.
    - Examples: *"Turn ideas into testable AI concepts fast"*, *"Find where AI truly makes sense in your business"*.
- **Main area** (~75% width, Ink/Deep Navy fill with tinted photo at 30%):
  - **Laptop + screenshot mockup cluster** (see Global Pattern above) - rotated laptop with 2–3 website screens floating behind, bleeding off the right edge.
  - **"WHAT'S INCLUDED" white rounded card** (16 pt radius), center-bottom of main area, 60% width of the main area:
    - Label at top: `WHAT'S INCLUDED` in Roboto 700, 18 pt, Core Blue.
    - Bulleted list: 4–6 items, 20 pt Roboto 400 Ink, each bullet is the **gradient Arrow rounded-square** (~18 pt tall).
- **Bottom-right corner**: service URL, e.g. `reeinvent.com/concept-sprint`, 14 pt white. The slug (`/concept-sprint`) is in **Roboto 700** or gradient text for emphasis.

**When to use**: anytime a service/offering gets its own slide. This is the canonical "offer card" - copy the whole template.

---

### A6 - Success Story (Case Study Template)
**Seen on**: slides 13–15 (*Alva*, *Airpark*, *Easylazy*).

**Layout**:
- **Top strip** (white, full-width, ~0.9 in tall):
  - Left: **client logo** in a colored pill/badge matching the client's brand (e.g., Alva = blue, Airpark = green, Easylazy = sunburst orange+teal).
  - Center: `SUCCESS STORY` in Roboto 300 thin, ~44 pt, Ink, letter-spacing +4 pt.
  - Right: REEINVENT wordmark, Blue, 0.5 in.
- **Main area** (Ink/Deep Navy, tinted product/context photo at ~30% opacity right-half):
  - **Top-left chat bubble**: one-line descriptor of the client/project in gradient text, white rounded card, small tail pointing up at the client logo. Example: *"Long-term agentic innovation platform"*, *"Smart urban parking, reimagined"*, *"Digitizing the beach guest experience"*.
  - **Three-row content stack** at left (each row is ~0.9 in tall):
    1. **CHALLENGE** - gradient-filled pill label on left (violet/blue gradient, white Roboto 700 text, ~16 pt uppercase). White rounded card on right (20 pt Ink body). One sentence.
    2. **SOLUTIONS** - same structure. One sentence.
    3. **RESULTS** - same structure, but the white card contains a **bullet list** (4 items) using the gradient Arrow bullets. Each bullet is a metric: *`+20% faster knowledge access`*, *`10+ systems connected`*, etc.
  - **Right side**: product/UI screenshots floating on top of the photo background (phone mockups stacked for mobile-first products; dashboard mockups for B2B).

**When to use**: every case study / customer story. Never reinvent this layout - copy and swap content.

---

### A7 - "We Work With" - Three-Column Audience
**Seen on**: slide 18 (*We Work With*).

**Layout**:
- **Top half**: photo of people working / team, fading via dark gradient into the bottom half.
- **Large white title** `WE WORK WITH` in Roboto 900 ultra-bold, ~140 pt, straddling the photo/column boundary (so the bottom of the title is over the columns).
- **Bottom half**: three full-height rounded-top columns:
  - Each column filled with the **Signature Gradient** (slight variation - darker/lighter to keep columns visually distinct).
  - Giant background numeral (`1`, `2`, `3`) in white at ~15% opacity, ~300 pt, weight 700, filling most of each column.
  - Audience label at bottom-center of each column: Roboto 700, ~32 pt, white, 2 lines.
    - Examples: `STARTUPS / & SCALEUPS`, `INNOVATION / TEAMS`, `ENTERPRISES / EXPLORING AI`.

**When to use**: segmentation / audience / tier slides. Great for "who is this for" framing.

---

### A8 - Partnership / Trident Alliance Slide
**Seen on**: slide 19 (*Trident*).

**Layout**:
- **Background**: Ink with a blurred audience/conference photo at ~25% opacity.
- **Top-left**: **circular "seal" badge** - round outlined ring with partner names running around the perimeter (`REEINVENT • CODESCENE • SYSTEM VERIFICATION`), trident symbol in the center. White stroke on dark.
- **Right of seal**: giant partnership name, Roboto 900, ~180 pt, white (`Trident`).
- **Body paragraph** below the seal/title, with a thin **multi-color vertical accent bar** on the left (blue / yellow / teal, 3 stacked segments, each matching one partner's brand).
- **Three partner logos** at the bottom, each with a 2 pt colored underline in that partner's brand color (Reeinvent = blue, System Verification = yellow, CodeScene = teal).
- **Right side**: **circular process infographic** - concentric ring divided into quadrants with partner roles (`Innovation / Quality Monitoring / Code Health / Analytics`) around a dark-navy core labeled `INSIGHTS / GROWTH / RESILIENCE`. Each ring segment uses the corresponding partner's color.

**When to use**: partnership / alliance / multi-brand positioning slides.

---

### A9 - Offices / Map Slide
**Seen on**: slide 20 (*Our Offices*).

**Layout**:
- **Top strip** (white, ~1.0 in):
  - Left: the Trident seal badge (small, ~0.7 in).
  - Center: `Our Offices` in Roboto 900, ~54 pt, Ink.
  - (No wordmark at top-right - the seal stands in for brand presence here.)
- **Main area** (Ink fill):
  - **Subtle outlined world/regional map** at ~25% opacity, white strokes only, centered.
  - **City labels** as white rounded-rectangle cards (8 pt radius, thin white outline, semi-transparent fill):
    - City in Roboto 700 uppercase, ~16 pt, white.
    - Country below in Roboto 400, ~11 pt, white at 70%.
  - Each city-card connected to its **dot on the map** by a thin white polyline (right-angle bends, not diagonal straight lines).
  - Cards arranged in columns on the left (Germany, US), top-center (Poland), bottom-center (Balkans), right (Sweden/Denmark/Norway).

**When to use**: global presence / office list slides. Layout gives geographic spread without needing a high-fidelity map.

---

### A10 - Mega-Title Contact Slide
**Seen on**: slide 20 (*Contact*).

**Layout**:
- **Full-width display title** `CONTACT` at the very top, Roboto 900 ultra-bold, Ink, **~220 pt**, bleeding to the left edge of the slide. No gradient - pure Ink.
- REEINVENT wordmark at top-right (standard stamp).
- **Three cards below** (evenly distributed, equal width):
  - **Top**: photo of the city, with the city name overlaid as large white **thin outlined ghost lettering** (Roboto 300, ~80 pt, letter-spacing +2 pt, white with low opacity or white stroke only).
  - **Below photo**: white card with alternating-band rows:
    - Band 1 (white row): `LOCATION` eyebrow in Core Blue uppercase, city name in Roboto 400 Ink below.
    - Band 2 (Ink row): `ADDRESS` eyebrow in gradient text uppercase, address in white Roboto 400.
    - Band 3 (white row): `EMAIL` eyebrow in Core Blue uppercase, address in Roboto 400 Ink.
  - (Pattern continues for PHONE, WEBSITE if present.)
- Card shape: 16 pt radius, overall card height ~4.5 in.

**When to use**: multi-office contact slide; multi-speaker credit slide.

---

## Recurring Micro-Patterns

### The gradient pill label
- Used for: `CHALLENGE`, `SOLUTIONS`, `RESULTS`, `WHAT'S INCLUDED`, `LOCATION`, `ADDRESS`, `EMAIL`.
- Shape: rounded pill (radius ≈ half the pill height).
- Fill: **Signature Gradient** (30°).
- Text: white or gradient-text, Roboto 700, uppercase, ~14–16 pt, +1 pt tracking.
- Use this for every row-label or section-marker on content slides.

### The chat-bubble callout
- Small white rounded-rectangle with a triangular tail.
- Radius: 10–12 pt. Tail: small triangle (~14 pt side) extending from the edge that points at the element being labeled.
- Contains one short phrase (3–7 words), 16 pt Roboto 400, dark text (or gradient text on taglines).
- Use for: client descriptors on success stories, tagline-under-service-name on service slides, inline pointer annotations.

### The duration pill
- White **outlined** pill (1.5 pt stroke) on gradient backgrounds - transparent fill, white stroke, white text.
- Format: `<1 week`, `1–3 weeks`, `3–5 weeks`, etc.
- Sits at the top of the left sidebar on service slides.

### The Arrow bullet
- Gradient rounded-square (6 pt radius) containing the Arrow Up SVG, ~18 pt tall.
- Fill: Signature Gradient; Arrow: white.
- Replaces circle bullets / checkmarks / dashes in every "what's included" or "results" list.

### The AI-DRIVEN / thin + bold header
- Pattern: `[WORD in Roboto 300 thin, ~72 pt] [WORD in Roboto 700 gradient-text, ~72 pt]`.
- Applied to service category headers, section intros, philosophy statements.
- This is the single strongest title-device in the deck - use it anywhere a slide needs a heavy top-of-slide title.

### The "split-half" slide
- 50/50 vertical split between a photo + gradient block (left) and Ink + body copy (right).
- Left is emotional (image, oversized thin+bold title); right is rational (headline + paragraph).
- Seen in Who We Are, AI-Native Approach - generalizable to "emotional framing + logical detail."

---

## Color Usage in Context

How the palette actually plays across a full deck:

| Slide type | Background | Dominant palette use |
|-----------|-----------|---------------------|
| Cover / Chapter / Thank You | Signature Gradient full-bleed | Gradient is the whole slide; white type only |
| Intro Split | Left: photo + gradient block. Right: Ink | Gradient as emotional anchor; Ink as content ground |
| Service Detail | Top: white strip. Left sidebar: gradient. Main: Ink + photo | Gradient frames the service name; Ink carries the product shots |
| Success Story | Top: white strip. Main: Ink + tinted photo | Gradient only on pill labels and chat bubbles |
| Audience Split | Top: photo. Bottom: gradient columns | Gradient repeats as columns; white type dominant |
| Contact / Offices | Top: white/Ink heading. Main: Ink | Mostly neutral; gradient only on eyebrow labels within cards |

**Cadence rule**: alternate gradient-heavy and Ink-heavy slides. A 21-slide deck typically opens Gradient → Split → Gradient → Ink-heavy content (slides 4–11) → Gradient divider → Ink content → closer Gradient. The gradient is a punctuation mark, not a constant state.

---

## Typographic Cadence

In production decks, Reeinvent uses **a wider weight range than DESIGN.md initially specifies**. Observed weights:
- **Roboto 300 (Light/Thin)** - used for cover titles (`SUCCESS STORIES`, `THANK YOU`), the upper half of split titles (`WHO WE`, `AI`, `CONCEPT`, `RAPID`, `AI-DRIVEN`), and outlined ghost lettering over photos.
- **Roboto 400 (Regular)** - body copy, default.
- **Roboto 700 (Bold)** - headlines, inline emphasis, eyebrow labels.
- **Roboto 900 (Black)** - mega titles (`CONTACT`, `WE WORK WITH`, `Trident`), and the bottom half of split titles (`ARE`, `FIRST`, `SPRINT`, `PROTOTYPE`, `DRIVEN`).

**Practical rule**: the hero "split title" pattern (thin-over-bold) only works when you have both **Roboto 300 and Roboto 900** installed. Embed both weights in the .pptx.

Update [DESIGN.md](DESIGN.md) §3 to permit the full 300/400/700/900 range when building cover and mega-title slides.

---

## Quick Slide Archetype Reference

| Archetype | ID | Use when... |
|-----------|----|-------------|
| Cover (full-bleed gradient) | A1 | Opening slide of every deck |
| Section divider | A2 | Chapter break, closing "Thank You" |
| Intro split (50/50 photo+gradient / Ink) | A3 | Deck introduction, philosophy statement |
| AI-DRIVEN two-column | A4 | Positioning a two-pillar offering |
| Service detail (with mockup cluster) | A5 | Each individual service offer |
| Success story (Challenge/Solution/Results) | A6 | Each customer case |
| We Work With three-column | A7 | Audience segmentation |
| Partnership seal slide | A8 | Multi-brand alliance |
| Offices map | A9 | Global presence |
| Mega-title contact | A10 | Final contact / credits |

---

## What's Missing from DESIGN.md That Shows Up in Production

After reviewing the master deck, the following refinements should be added to [DESIGN.md](DESIGN.md):

1. **Add Roboto 300 and Roboto 900** as permitted weights (currently only 400 and 700). The thin-over-bold split titles (`CONCEPT / SPRINT`) require both.
2. **Add the chat-bubble callout** as a component. It's everywhere in production and isn't currently specified.
3. **Add the gradient pill label** as a primary row-labeling device (CHALLENGE/SOLUTIONS/RESULTS pattern).
4. **Add the laptop + screenshots mockup cluster** as the canonical service visual. Without this pattern, service slides look like generic tech-vendor slides.
5. **Add the "AI-DRIVEN [WORD]" header pattern** as Reeinvent's signature slide-title device.
6. **Add the outlined duration pill** (`<1 week`) as a standard component on service slides.
7. **The Roboto 900 mega-title** (`CONTACT` at ~220 pt) is a stronger device than what DESIGN.md's 80 pt "Mega title" allows. Permit up to ~220 pt for one-word display titles.

---

## Sources

- `/Users/rebrained/Downloads/REE 2.0 – Master Company Presentation (Compressed).pdf` (21 slides) - the full master deck, covering cover, intro, AI-driven positioning, 8 service details, success stories chapter, 3 case studies, AI-native approach, audience segmentation, Trident partnership, offices map, contact, thank-you.
- *2-Pager Company Presentation* (116 MB, not inspectable within file-size limits) - deferred; expected to overlap with the master deck's service-detail and success-story archetypes.
