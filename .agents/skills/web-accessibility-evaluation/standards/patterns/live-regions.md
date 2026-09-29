# Live Regions

## Overview

Live regions announce dynamic content changes to screen reader users without requiring focus to move. Misuse creates noise that degrades the experience. This pattern provides urgency guidance, centralization rules, and anti-patterns.

**WCAG criteria**: 4.1.3 (Status Messages)

---

## Live Region Urgency Table

| Urgency | `aria-live` Value | Behavioral Impact | Example |
| ------- | ----------------- | ----------------- | ------- |
| **Critical** | `assertive` / `role="alert"` | Interrupts immediately, clears speech queue | Session timeout, API failure, data loss warning |
| **Standard** | `polite` | Announces at next graceful break | Search results count, "Saved", cart update |
| **Passive** | `off` | Only announced if user navigates to it | Character count, progress percentage |

---

## Rules

### 1. Use `assertive` ONLY for critical, time-sensitive updates

Updates that prevent safe continuation: data loss, session timeout, network drop, critical error requiring immediate action.

**Never** use `assertive` for: success messages, loading states, search results, form validation, cart updates.

### 2. Centralize live regions

One `polite` region and one `assertive` region per page. Update their text content — don't create new regions dynamically.

```html
<!-- In your layout, render once -->
<div id="polite-announcer" aria-live="polite" aria-atomic="true" class="visually-hidden"></div>
<div id="assertive-announcer" aria-live="assertive" aria-atomic="true" class="visually-hidden"></div>
```

### 3. Debounce frequently-changing regions

When content changes rapidly (combobox results as user types, real-time counters), debounce the live region update to avoid speech queue flooding.

```tsx
// Debounce search result count announcements
const [resultCount, setResultCount] = useState(0);
const announceRef = useRef<HTMLDivElement>(null);

useEffect(() => {
  const timeout = setTimeout(() => {
    if (announceRef.current) {
      announceRef.current.textContent = `${resultCount} results found`;
    }
  }, 500); // Wait for typing to settle
  return () => clearTimeout(timeout);
}, [resultCount]);
```

### 4. Do NOT use live regions for transient states

"Loading…" or "Updating…" interstitial states create noise. Only announce the **outcome** (success/failure), not the process.

### 5. Do NOT update live regions inside inert DOM

If a dialog just closed and its content contains a live region, updating that region may still fire announcements in some AT. Ensure live regions are only updated when their container is visible and active.

### 6. `role="alert"` vs `aria-live="assertive"`

`role="alert"` is equivalent to `aria-live="assertive" aria-atomic="true"`. Use `role="alert"` for error messages that must interrupt. Use `aria-live="assertive"` when you need more control (e.g., `aria-atomic="false"`).

### 7. `role="status"` vs `aria-live="polite"`

`role="status"` is equivalent to `aria-live="polite" aria-atomic="true"`. Use for status updates like "3 items in cart" or "Changes saved".

---

## Anti-Patterns

| Anti-pattern | Why it's wrong | Fix |
| ------------ | -------------- | --- |
| `aria-live="assertive"` on search results | Interrupts constantly while typing | Use `polite` + debounce |
| Live region on a loading spinner | Announces "Loading" repeatedly | Announce only the final result |
| New `aria-live` region injected dynamically | AT may not register it | Pre-render region, update content |
| `aria-live` on the entire page wrapper | Every DOM change announced | Scope to specific announcement div |
| `role="alert"` on form validation that fires on blur | Interrupts user mid-flow | Use `aria-live="polite"` for form errors |

---

## Platform Implementation

- **Web**: `aria-live="polite|assertive"`, `role="alert"`, `role="status"`
- **iOS**: `UIAccessibility.post(notification: .announcement, argument: "message")` — use `.layoutChanged` for focus, `.announcement` for passive updates
- **Android**: `View.announceForAccessibility("message")` or `ACCESSIBILITY_LIVE_REGION_POLITE` / `ACCESSIBILITY_LIVE_REGION_ASSERTIVE` on ViewGroups

---

## Resources

- WCAG 4.1.3 Status Messages: <https://www.w3.org/WAI/WCAG22/Understanding/status-messages>
- ARIA Live Regions: <https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#live_region>
- MDN aria-live: <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-live>
