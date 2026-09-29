# Vitamin Play accessibility guidance — navigation-header (web)

Source: vitamin-play-documentation/src/content/components-accessibility/navigation-header.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Navigation Header component provides these built-in accessibility features out-of-the-box.

        - **Banner landmark:** Component is wrapped in a `` element with implicit `banner` role for easy navigation
        - **Semantic structure:** Proper HTML5 semantic elements for header organization
        - **Interactive elements:** All navigation items, search bar, and action buttons are keyboard accessible
        - **Design tokens:** Sufficient contrast and appropriate sizing for users with low vision

## What you need to do

        **Design / Content**
        - **Skip link:** Implement a "Skip to main content" link as the first focusable element on the page
        - **Descriptive labels:** Ensure navigation menu items have clear, descriptive text
        - **Logo alt text:** Provide appropriate alt text for the Decathlon logo
        - **Search placeholder:** Use clear placeholder text for the search input

        **Development**
        - **Landmark differentiation:** If your page has multiple banner elements, differentiate them using `aria-label`
        - **Navigation landmark:** Include a `` landmark with `aria-label` for the main navigation menu
        - **Focus management:** Ensure proper focus order from left to right, top to bottom
        - **Dropdown behavior:** Implement proper keyboard navigation for sub-navigation menus (Space/Enter to open, Escape to close)
        - **Testing:** Verify keyboard navigation works for all interactive elements
        - **Override caution:** If overriding accessibility features with custom `aria-*` attributes, ensure WCAG compliance is maintained

## Skip to main content

      The "Skip to main content" link is a critical accessibility feature designed to enhance navigation for users relying on keyboard-only interaction or screen readers. When activated, it immediately moves the user's focus past the navigation header and directly to the main content area of the page. This serves to bypass repetitive content—such as the global navigation menu, logo, and search bar—that appears on every page. Without this mechanism, keyboard and screen reader users would be forced to tab through these recurring elements repeatedly to reach the unique content of the current page.

      **WCAG 2.4.1** Bypass Blocks • **RGAA 12.1** Bypass repetitive content

> 
        Note: While not yet available as a pre-built component, Vitamin Play plans to offer the Skip main content link as a standard component for direct integration into user interfaces in a future release. Until the dedicated component is released, it is recommended that teams implement the "Skip to main content" link using the existing Link component and adhere to the guidelines and best practices for placement and behavior.

## Accessibility attributes

  The Navigation Header component uses a `` element which has an implicit `banner` role. This landmark helps users quickly identify the top-level navigation area of the page.

  If your page includes multiple banner elements (which should be rare), you must differentiate them by providing unique accessible names using `aria-label`. For example: `` and ``.

  The component can contain other landmarks:
  - A `` landmark with `aria-label` for the main navigation menu (e.g., ``)
  - Additional `` landmarks may be used for utility navigation or sub-navigation areas

## Accessible label

The Navigation Header should include properly labeled landmarks:

  - **Banner landmark:** The `` element provides implicit `banner` role; add `aria-label` only if multiple banners exist on the page
  - **Navigation landmark:** Include `aria-label` on the `` element to describe the navigation purpose
  - **Search:** Label the search input with a visible label or `aria-label`
  - **Icons:** Ensure icon buttons have accessible names via `aria-label`

  Each interactive element should have descriptive text that clearly identifies its purpose.

## Keyboard behaviour

All navigation header elements must be fully accessible via keyboard. The tab order follows the visual arrangement from left to right and top to bottom.
**WCAG 2.1.1** Keyboard • **2.1.2** No Keyboard Trap • **RGAA 7.1** Keyboard navigation

      | **Key** | **Action** |
      | --- | --- |
      | `Tab` | Moves focus to the next focusable element (skip link, logo, navigation items, search, action buttons) |
      | `Shift + Tab` | Moves focus to the previous focusable element |
      | `Enter` or `Space` | Activates the focused link or button |
      | `Escape` | Closes open sub-navigation menus and returns focus to the main navigation item |

      **Tab order:**
      - Skip to main content link
      - Logo (if it's a link)
      - Search input
      - Action buttons (left to right)
      - Main navigation items (left to right)

      **Sub-Navigation (Dropdown Menu) behavior:**
      - Focus immediately shifts to the first interactive item in the sub-navigation
      - Use `Tab` to navigate through all sub-navigation items
      - `Tab` from the last item moves focus to the next main navigation item

## Design system guarantees

  ### ARIA and accessibility attributes

  | **RGAA criterion** | **Requirement** | **Responsibilities** |
  | ------------------ | --------------- | :------------------: |
  | [12.6](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#12.6) | The component is created to be used as `banner` element on pages. If your page includes several elements with this role, please differentiate them with a different accessible name (`aria-label`, for example). | ✅ / 👥 |

Using Vitamin Play design tokens ensures sufficient contrast between navigation elements and their background, appropriate sizing for touch targets, and consistent spacing across the header.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

    | **Environment** | **React** | **Svelte** | **Vue** |
    | --------------- | :-------: | :--------: | :-----: |
    | Firefox + NVDA | | | |
    | IE + JAWS | | | |
    | Safari + VoiceOver | ✅ | | |
    | Android + TalkBack | | | |
    | iOS + VoiceOver | | | |

## Expected implementation details

  - If overriding accessibility features (by adding `aria-*` attributes) or modifying component behavior, ensure WCAG compliance is maintained

## Testing and compliance

  The component is tested through:
  - [Deque Systems' Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core/tree/master) for compliance with [WCAG Level A & AA rules & accessibility best practices](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
  - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
  - [MDN Web Docs: WAI-ARIA banner role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/banner_role)

## Additional resources

  - [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
  - [MDN Web Docs: navigation role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/navigation_role)
