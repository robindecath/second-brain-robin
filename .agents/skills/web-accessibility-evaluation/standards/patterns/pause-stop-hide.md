# Pause, Stop, Hide (Auto-Playing Content)

## Overview

Content that moves, blinks, scrolls, or auto-updates can distract users — particularly those with attention disorders, cognitive disabilities, or vestibular conditions. WCAG 2.2.2 requires that such content can be paused, stopped, or hidden. (WCAG 2.2.2 AA)

> **Distinct from `motion-animation.md`** which covers transition animations triggered by user interactions. This pattern covers content that moves **on its own** without user initiation.

## What Requires Pause/Stop/Hide Controls

Any content that:
- **Moves or scrolls** automatically for more than 5 seconds (marquees, tickers, animated banners)
- **Blinks** for more than 5 seconds (loading indicators, notification badges)
- **Auto-updates** (live feeds, real-time dashboards, rotating carousels)

**Exception**: If the movement is essential to the functionality (e.g., a real-time stock chart), no pause control is needed — but consider providing a "freeze" view option.

## Implementation Requirements

Provide at least one of:
1. **Pause/Resume button** — stops motion, resumes on demand
2. **Stop button** — halts motion permanently until user re-initiates
3. **Hide button** — removes the moving content from view

The control must be **keyboard accessible** and visible before the user interacts with the moving content (not hidden in a menu after the carousel has started).

## Auto-Playing Carousels

Carousels are the most common violation of this criterion:

- ❌ Auto-advancing without pause control
- ❌ Pause button that only pauses while hovered (not keyboard/touch accessible)
- ✅ Pause/play button always visible and keyboard reachable
- ✅ Manual-only navigation (no auto-advance at all — simplest conformant solution)

## Platform Implementation

See your platform skill for implementation details:
- **Web**: `../../references/references/advanced-patterns.md` — carousel patterns
- **iOS**: `../../references/references/carousels.md`
- **Android**: `../../references/references/` — ScrollView + button patterns

## Resources

- WCAG 2.2.2 Pause, Stop, Hide: <https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide>
