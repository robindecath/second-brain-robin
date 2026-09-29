# Status Messages

## Overview

When content updates dynamically without a focus change (success banners, loading states, live counts, error toasts), assistive technologies must still announce the new content. Platforms expose "live region" APIs for this purpose. (WCAG 4.1.3 AA)

## The Problem

A sighted user sees a success banner appear after form submission. A screen reader user hears nothing because focus hasn't moved. WCAG 4.1.3 requires that status messages be programmatically determinable so AT can announce them without focus.

## Two Announcement Modes

| Mode | When to use | Platform APIs |
|---|---|---|
| **Polite** | Non-urgent updates — announce after current speech finishes | `aria-live="polite"` / `ACCESSIBILITY_LIVE_REGION_POLITE` / `AccessibilityNotification.Announcement` |
| **Assertive** | Urgent updates that interrupt — use sparingly | `aria-live="assertive"` / `ACCESSIBILITY_LIVE_REGION_ASSERTIVE` |

**Default to polite.** Assertive interrupts the user mid-sentence and should be reserved for critical errors or irreversible actions.

## Common Use Cases

| Scenario | Mode | Example message |
|---|---|---|
| Form submitted successfully | Polite | "Your order has been placed." |
| Item added to cart | Polite | "Product added. 3 items in cart." |
| Search results updated | Polite | "12 results found." |
| Session about to expire | Assertive | "Your session expires in 2 minutes." |
| Critical error | Assertive | "Payment failed. Please check your card details." |

## What NOT to Announce

- Don't announce every keystroke or character typed
- Don't re-announce content the user just interacted with (button labels, link text)
- Don't announce tooltip content on hover — tooltips should be discoverable, not auto-announced

## Platform Implementation

See your platform skill for implementation details:
- **Web**: `../../references/references/semantic.md` — `aria-live`, `role="status"`, `role="alert"`
- **iOS**: `../../references/references/accessibility-notifications.md` — `AccessibilityNotification.Announcement()`
- **Android**: `../../references/references/live-regions.md` — `ViewCompat.setAccessibilityLiveRegion()`

## Resources

- WCAG 4.1.3 Status Messages: <https://www.w3.org/WAI/WCAG22/Understanding/status-messages>
- ARIA Live Regions: <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions>
