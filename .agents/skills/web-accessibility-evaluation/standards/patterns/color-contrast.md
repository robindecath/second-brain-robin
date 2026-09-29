# Color Contrast

## Overview

Color contrast ensures that text and UI elements are readable by people with low vision or color deficiency. WCAG defines minimum contrast ratios based on text size and component type.

## Thresholds

| Content type | Minimum ratio | WCAG criterion |
|---|---|---|
| Normal text (< 18pt / < 14pt bold) | **4.5:1** | 1.4.3 AA |
| Large text (≥ 18pt / ≥ 14pt bold) | **3:1** | 1.4.3 AA |
| UI components and graphics | **3:1** | 1.4.11 AA |
| Focus indicators | **3:1** | 2.4.11 AA |

> **AAA target**: 7:1 for normal text, 4.5:1 for large text (WCAG 1.4.6).

## Color-Independent Design

Never use color as the **sole** means of conveying information (WCAG 1.4.1). Always pair color with a second indicator:

- Error states → red border **+ error icon + text message**
- Required fields → asterisk **+ label text "Required"**
- Status badges → color **+ text label**
- Charts/graphs → color **+ pattern or label**

## How to Measure

Use a contrast ratio tool before shipping:
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/) (desktop app, picks screen colors)
- Browser DevTools → Accessibility panel → inspect any text element

## Platform Implementation

See your platform skill for implementation details:
- **Web**: `../../references/references/colors.md` — Vitamin Play semantic tokens
- **iOS**: `../../references/references/` — SwiftUI `Color` and Dynamic Colors
- **Android**: `../../references/references/` — Material color roles and `@color` resources

## Resources

- WCAG 1.4.1 Use of Color: <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color>
- WCAG 1.4.3 Contrast (Minimum): <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum>
- WCAG 1.4.11 Non-text Contrast: <https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast>
