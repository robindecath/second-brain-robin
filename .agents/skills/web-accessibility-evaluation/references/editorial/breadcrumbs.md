# Vitamin Play accessibility guidance — breadcrumbs (web)

Source: vitamin-play-documentation/src/content/components-accessibility/breadcrumbs.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Breadcrumbs component provides these built-in accessibility features out-of-the-box.

        - **Navigation landmark:** Component is wrapped in a `` landmark region for easy navigation
        - **Semantic structure:** Breadcrumb trail is structured as an ordered list (``)
        - **Interactive elements:** All breadcrumb items that are links can be interacted with via keyboard
        - **Design tokens:** Sufficient contrast and appropriate sizing for users with low vision

## What you need to do

        **Design / Content**
        - **Clear labels:** Ensure breadcrumb labels are concise and descriptive (24 characters or less recommended)
        - **Valid hierarchy:** Every breadcrumb link must lead to a valid landing page (no abstract categories or dead links)
        - **Overflow handling:** Implement overflow controls when displaying 4+ breadcrumb items
        - **Current page:** Clearly distinguish the current page visually (e.g., bold text, different color).

        **Development**
        - **Landmark label:** Provide an accessible label for the `` landmark using `aria-label` or `aria-labelledby`
        - **Current page marker:** Mark the current page item with the `isCurrent` prop so `aria-current="page"` is set correctly
        - **Testing:** Verify keyboard navigation works for all breadcrumb links
        - **Override caution:** If overriding accessibility features with custom `aria-*` attributes, ensure WCAG compliance is maintained

## Accessibility attributes

      The Breadcrumbs component uses a `` landmark region to help users quickly locate the navigation trail. This landmark should be labeled with `aria-label` (e.g., "Breadcrumb navigation") or `aria-labelledby` to distinguish it from other navigation regions on the page.

      The breadcrumb trail is structured as an ordered list (``) to convey the hierarchical relationship between items to assistive technologies.

      The current page item is marked with `aria-current="page"` to indicate to screen readers which item represents the user's current location. If the current page is not a link, `aria-current` is optional but recommended.

## Accessible label

      **How to provide accessible labels:**

      The Breadcrumbs `` landmark must be labeled to distinguish it from other navigation regions:

      - **Preferred:** Use `aria-label` directly on the component with a descriptive label like "Breadcrumb navigation" or "Page hierarchy"
      - **Alternative:** Use `aria-labelledby` to reference a visible heading that describes the navigation
      - **Current page:** Mark the current page item with the `isCurrent` prop, which automatically adds `aria-current="page"`

      Each breadcrumb item should have concise, descriptive text that clearly identifies the page it links to.

```tsx
      {/* Best practice: aria-label on nav */}

        Home
        Sports
        Football
        Shoes

      {/* Alternative: aria-labelledby referencing heading */}
      Product navigation

        Home
        Current Page

      {/* With brand link */}

        Home
        Sports
        Shoes

      ```

## Keyboard behaviour

      | **Key** | **Action** |
      | --- | --- |
      | `Tab` | Moves focus to the next focusable breadcrumb link or brand link |
      | `Shift + Tab` | Moves focus to the previous focusable element |
      | `Enter` or `Space` | Activates the focused breadcrumb link |

## Design system guarantees

  ### Keyboard interaction

  | **RGAA Criterion** | **Description** | **Responsibilities** |
  | --- | --- | :---: |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When focus is on a Breadcrumbs item you can interact with it if it is a link. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | `Tab` allows you to navigate through link items and the brandLink (if present). | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | `Shift + Tab`: Moves focus to the previous focusable element. | ✅ |

  ### ARIA & Accessibility Attributes

  | **RGAA Criterion** | **Description** | **Responsibilities** |
  | --- | --- | :---: |
  | [12.6](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#12.6) | The Breadcrumbs trail is contained within a navigation landmark region. | ✅ |
  | [9.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#9.3) | The Breadcrumbs list is treated as a `` list. | ✅ |
  | [12.6](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#12.6) | The landmark region is labelled via `aria-label` or `aria-labelledby`. | 👥 |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The link to the current page has `aria-current` set to page. If the element representing the current page is not a link, `aria-current` is optional. | 👥 / ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between breadcrumb links and their background, appropriate sizing for readability and touch targets, and consistent spacing throughout the breadcrumb trail.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

    | **Environment** | **React** | **Svelte** |
    | --------------- | :-------: | :--------: |
    | Firefox + NVDA | | |
    | IE + JAWS | | |
    | Safari + VoiceOver | ✅ | ✅ |
    | Android + TalkBack | | |
    | iOS + VoiceOver | | |

## Expected implementation details

  - The Breadcrumbs root element is a navigation landmark region (``) that should be labelled via `aria-label` or `aria-labelledby`
  - The link to the current page has `aria-current` set to page - mark the current item with the `isCurrent` prop for automatic handling
  - If overriding accessibility features (by adding `aria-*` attributes) or modifying component behavior, ensure WCAG compliance is maintained

## Testing and compliance

  The component is tested through:
  - [Deque Systems' Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core/tree/master) for compliance with [WCAG Level A & AA rules & accessibility best practices](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
  - [ARIA Authoring Practices Guide: Breadcrumb Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/)
  - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

  - [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
