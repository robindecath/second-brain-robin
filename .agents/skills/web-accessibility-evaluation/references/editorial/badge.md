# Vitamin Play accessibility guidance — badge (web)

Source: vitamin-play-documentation/src/content/components-accessibility/badge.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Badge component provides these built-in accessibility features out-of-the-box.

          - **Status role:** Badge uses `role="status"` to announce content updates as polite live regions.
          - **Live region behavior:** Content changes are announced to screen readers with `aria-live="polite"` by default.
          - **Axe Core compliance:** Component tested with Deque Systems' accessibility testing engine.
          - **Design token guarantees:** Sufficient contrast and appropriate sizing through design tokens.

## What you need to do

          **Design / Content**
          - **Alternative text:** Provide meaningful alternative text when badge content is not self-explanatory (e.g., unitless numbers).
          - **Context clarity:** Ensure badge meaning is clear through surrounding context or explicit labels.
          - **Empty badges:** Provide alternative text for empty badges that convey status visually.

          **Development**
          - **Accessible labels:** Use `aria-label` or non-visible content when badge displays unitless values.
          - **Parent context:** Ensure parent elements (buttons, icons) have descriptive labels that include badge information.
          - **Live region customization:** Override `aria-live` only when necessary (use `assertive` for critical updates, `off` to disable).
          - **Override caution:** Test thoroughly if overriding default ARIA attributes.

## Accessibility Attributes

        The Badge component uses ARIA attributes to communicate status updates to assistive technologies:

        **Badge Element:**
        - `role="status"`: Identifies the element as a status indicator (implicit `aria-live="polite"`)
        - `aria-live="polite"`: Default behavior - announces updates without interrupting user
        - `aria-live="assertive"`: Optional - for critical updates requiring immediate attention
        - `aria-live="off"`: Optional - disables live region announcements
        - `aria-label` or text content: Provides meaningful context when badge shows unitless values

        **Parent Element Context:**
        When badge is associated with interactive elements (buttons, icons), the parent element should include badge information in its accessible name via `aria-label`.

## Accessible label

Badge content is often unitless (just numbers) or purely visual (empty dot). In these cases, you must provide meaningful context through accessible labels on parent elements or the badge itself.

## Badge with unitless number

        Provide context in the parent element's `aria-label`:

        ````tsx

          99+

        ````

## Empty badge (visual indicator)

        Provide context even when badge has no text content:

        ````tsx

        ````

## Badge with meaningful text

        When badge contains self-explanatory text, minimal additional context may be needed:

        ````tsx

          Shopping cart
          3 items

        ````

## Customizing live region behavior

        Override `aria-live` for specific use cases:

        ````tsx
        {/* Critical updates requiring immediate attention */}
        Alert

        {/* Disable announcements for decorative badges */}
        New
        ````

## Design system guarantees

The Vitamin Play design system ensures several accessibility requirements are met through design tokens and component architecture. These guarantees apply across all platforms and relieve implementers from managing these concerns manually.

### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                  | **Responsibilities** |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------: |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)     | The badge has `role="status"` to identify it as a status indicator                                                                                                                                                                              | ✅          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)     | The badge has implicit `aria-live="polite"` from the status role                                                                                                                                                                                | ✅          |
| [1.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#1.1)     | When content is unitless or purely visual, alternative text is provided via `aria-label`, non-visible content, or parent element context                                                                                                        | 👥          |
| [10.13](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.13)    | Information is not conveyed solely through shape, size, or position without an accessible alternative                                                                                                                                           | 👥          |

### Visual accessibility

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                  | **Responsibilities** |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------: |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2)     | Badge and background have sufficient color contrast (4.5:1 minimum) for users with low vision                                                                                                                                                   | ✅          |
| [10.9](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.9)    | Badge is appropriately sized for readability                                                                                                                                                                                                    | ✅          |
| [3.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.1)     | Status is not conveyed by color alone (shape and text are also indicators)                                                                                                                                                                      | ✅          |

  Using Vitamin Play design tokens ensures:
  - **Sufficient contrast** between badge and background for users with low vision or color deficiencies
  - **Appropriate sizing** of badges for readability across all platforms
  - **Consistent spacing** that meets accessibility requirements

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**          | **Tested** | **Notes**                                                                                     |
| ------------------------ | ---------- | --------------------------------------------------------------------------------------------- |
| Safari + VoiceOver       |            |                                                                                               |
| Firefox + NVDA           |            |                                                                                               |
| Chrome + JAWS            |            |                                                                                               |
| Edge + Narrator          |            |                                                                                               |

## Expected implementation details

- Most badge contents are unitless and give information only understandable through shape and/or context. Provide alternative text via non-visible content, `aria-label`, or parent element's accessible label
- When badge is empty (visual indicator only), provide alternative text that describes the status
- Badge defaults to `role="status"` with implicit `aria-live="polite"` for announcing content updates
- Override `aria-live` only when necessary: use `assertive` for critical updates, `off` to disable announcements
- When overriding accessibility features, ensure compliance with accessibility expectations in this documentation

## Implementation notes

The Badge component uses `role="status"` which is a type of live region defined by WAI-ARIA. This role provides:

- **Implicit `aria-live="polite"`**: Updates are announced to screen readers without interrupting the user's current activity
- **Advisory information**: Badge content is considered advisory information for the user, not critical enough to justify an alert
- **Automatic announcements**: When badge content changes (e.g., notification count updates), screen readers automatically announce the new value

This behavior makes Badge ideal for displaying dynamic content like notification counts, cart item quantities, or status indicators that update over time.

## Testing and compliance

    The Vitamin Play Badge component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [ARIA Authoring Practices Guide (APG): Status Role](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

    - [ARIA: status role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/status_role)
