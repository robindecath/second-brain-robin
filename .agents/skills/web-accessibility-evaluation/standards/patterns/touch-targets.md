# Touch Targets

Search terms: touch target size, minimum touch target, 44px, 48dp, interactive target.

## Overview

Touch targets must be large enough for users to activate reliably, including people with motor impairments or tremors. WCAG 2.2 introduced a minimum size requirement; platform Human Interface Guidelines recommend larger targets.

## Size Requirements

| Standard | Minimum size | Notes |
|---|---|---|
| WCAG 2.5.8 AA (2.2) | 24×24 CSS px | Applies to web; spacing exception allowed |
| WCAG 2.5.5 AAA | 44×44 CSS px | Recommended target for web |
| Apple HIG | 44×44 pt | Recommended for iOS/iPadOS |
| Material Design | 48×48 dp | Recommended for Android |

The **visual size** can be smaller than the interactive area. Use invisible padding or platform-specific hit area APIs to extend the touch target without changing the visual design.

## Exemptions (WCAG 2.5.8)

The minimum size requirement does **not** apply when:
- The target is inline within a sentence or block of text
- The target size is determined by the user agent and not modified by the author
- An equivalent, conforming target performs the same action nearby

## Spacing Exception

If a 24×24 target cannot be achieved, ensure the **offset spacing** (distance to the nearest adjacent target) totals at least 24px in each axis. Two adjacent 20px targets with 4px between them would both pass.

## Platform Implementation

See your platform skill for implementation details:
- **Web**: CSS `min-height: 44px; min-width: 44px` with `padding`
- **iOS**: `../../references/references/touch-target-size.md` — `.frame(minWidth: 44, minHeight: 44)`, `.contentShape()`
- **Android**: `../../references/references/touch-targets.md` — `minWidth/minHeight 48dp`, `TouchDelegate`

## Resources

- WCAG 2.5.5 Target Size (Enhanced): <https://www.w3.org/WAI/WCAG22/Understanding/target-size>
- WCAG 2.5.8 Target Size (Minimum): <https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum>
- Apple HIG — Layout: <https://developer.apple.com/design/human-interface-guidelines/layout>
- Material Design — Accessibility: <https://m3.material.io/foundations/accessible-design/accessibility-basics>
