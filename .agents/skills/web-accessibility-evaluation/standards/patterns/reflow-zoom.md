# Reflow and Zoom

## Overview

Users with low vision rely on zooming and text scaling to read content. Interfaces must remain usable when zoomed to 400% (reflow) or when the system font size is increased (text resize). (WCAG 1.4.4, 1.4.10, 1.4.12 AA)

## Three Related Criteria

### WCAG 1.4.4 — Resize Text

Text must be resizable up to **200%** without loss of content or functionality. This means no content should be cut off, overlapping, or become inaccessible when text size doubles.

**Applies to**: Web (browser zoom), iOS (Dynamic Type), Android (Font Scale)

### WCAG 1.4.10 — Reflow

Content must reflow into a single column when viewport width is equivalent to **320 CSS px** (400% zoom on a 1280px screen) **without horizontal scrolling** — except for content that requires two-dimensional layout (data tables, maps, complex diagrams).

This is a web-first criterion but the principle applies: at the largest platform text sizes, content must not overflow or require horizontal scrolling.

### WCAG 1.4.12 — Text Spacing

When users override text spacing (line height ≥ 1.5×, letter spacing ≥ 0.12em, word spacing ≥ 0.16em, no paragraph spacing), **no content or functionality is lost**. Text containers must expand to accommodate overrides.

## Common Violations

| Violation                                                     | Criterion     |
| ------------------------------------------------------------- | ------------- |
| Fixed `px` heights on text containers that clip text          | 1.4.4, 1.4.12 |
| `overflow: hidden` on containers without `min-height`         | 1.4.4, 1.4.12 |
| Horizontal scroll at 320px wide (except 2D content)           | 1.4.10        |
| Text in images (cannot be resized by user)                    | 1.4.5, 1.4.4  |
| Using `px` for font sizes (ignores browser base font setting) | 1.4.4         |

## Platform Rules

| Platform    | Rule                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| **Web**     | Use `rem`/`em` for font sizes, `min-height` instead of `height`, test at 400% browser zoom              |
| **iOS**     | Use Dynamic Type text styles (`Font.title`, `.body`), `ScaledMetric` for spacing, `ScrollView` wrappers |
| **Android** | Use `sp` for all text sizes, `wrap_content` for container heights, test at 200% Font Scale              |

## Platform Implementation

See your platform skill for implementation details:

- **Web**: `../../references/references/semantic.md` — `rem` units, responsive containers, layout patterns
- **iOS**: `../../references/references/dynamic-type.md` — `ScaledMetric`, `Font.title`, avoiding fixed heights
- **Android**: `../../references/references/text-scaling.md` — `sp` units, `wrap_content`, Font Scale testing

## Resources

- WCAG 1.4.4 Resize Text: <https://www.w3.org/WAI/WCAG22/Understanding/resize-text>
- WCAG 1.4.10 Reflow: <https://www.w3.org/WAI/WCAG22/Understanding/reflow>
- WCAG 1.4.12 Text Spacing: <https://www.w3.org/WAI/WCAG22/Understanding/text-spacing>
