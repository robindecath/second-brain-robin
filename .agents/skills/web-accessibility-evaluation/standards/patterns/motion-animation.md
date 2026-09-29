# Motion and Animation

## Overview

Excessive or unexpected animation can trigger vestibular disorders (dizziness, nausea) in susceptible users. All platforms expose a user preference to reduce motion that must be respected. (WCAG 2.3.3 AAA, but widely expected at AA level in practice)

> **Distinct from WCAG 2.3.1** (Three Flashes) which covers seizure-triggering flashes. See `pause-stop-hide.md` for auto-playing content.

## The Reduce Motion Preference

Users can enable "Reduce Motion" in their OS accessibility settings:
- **macOS/iOS**: Settings → Accessibility → Motion → Reduce Motion
- **Android**: Settings → Accessibility → Remove animations
- **Windows**: Settings → Ease of Access → Display → Show animations

When enabled, your application **must** replace or disable motion-heavy animations.

## Safe vs. Unsafe Animations

| Safe (keep even with reduce-motion) | Unsafe (disable or replace) |
|---|---|
| Opacity fade (no positional change) | Parallax scrolling |
| Instant state transitions | Zoom/scale transitions |
| Static color changes | Spinning loaders (replace with static) |
| Progress bar fill | Sliding panels (replace with crossfade) |

## Minimum Requirements

- **Essential animations**: If motion is necessary to convey information (e.g., a loading spinner communicating progress), provide a text alternative
- **Duration**: Keep transitions under 300ms where motion cannot be disabled
- **No infinite loops** of purely decorative motion

## Platform Implementation

See your platform skill for implementation details:
- **Web**: `@media (prefers-reduced-motion: reduce)` CSS media query
- **iOS**: `../../references/references/reduce-motion.md` — `@Environment(\.accessibilityReduceMotion)`
- **Android**: `../../references/` — `Settings.Global.ANIMATOR_DURATION_SCALE`

## Resources

- WCAG 2.3.3 Animation from Interactions: <https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions>
- MDN prefers-reduced-motion: <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion>
