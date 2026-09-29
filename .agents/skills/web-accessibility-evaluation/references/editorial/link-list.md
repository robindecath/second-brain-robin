# Vitamin Play accessibility guidance — link-list (web)

Source: vitamin-play-documentation/src/content/components-accessibility/link-list.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Link List component provides these built-in accessibility features out-of-the-box.

          - **Correct semantics**: Each list item has proper `role` assignment (link or button) based on whether `href` or `onClick` is provided
          - **Keyboard support**: Activation via Enter/Space with proper focus management for each item
          - **Disabled states**: Default `disabled` and `aria-disabled` attributes when list items are unavailable

## What you need to do

          **Design / Content**
          - **Link text clarity:** Use clear, descriptive text for each list item that makes sense out of context; avoid generic text like "click here".
          - **Consistent ordering:** Organize list items in a logical order that matches user expectations and task flow.
          - **Content accessibility:** Ensure sufficient contrast (tokens), meaningful text, and logical reading order.

          **Development**
          - **Accessible names:** Ensure each list item has an accessible name, either from visible text content or via `aria-label`/`aria-labelledby`. The accessible name must contain the visible text.
          - **Descriptions:** Connect descriptions using `aria-describedby` when additional context is needed for a list item's function.
          - **Disabled behavior:** Prefer `aria-disabled="true"` over removing focus when a list item must remain visible; consider `isFocusable = true` to maintain keyboard access.
          - **Override caution:** If you add `aria-*` attributes or change behavior, validate against this doc and re-test with keyboard and screen readers.

## Accessibility attributes

        Each Link List Item is polymorphic and can semantically function as either an HTML link (``) or button (``), depending on whether an `href` or `onClick` is provided.

        Each list item element has:
        - `role="link"` when it semantically represents an HTML link (with `href`)
        - `role="button"` when it semantically represents an HTML button (with `onClick`)
        - An accessible name computed from text content, or provided via `aria-labelledby` or `aria-label`
        - `aria-describedby` set to the ID of the element containing the description, if a description is present
        - `disabled` or `aria-disabled="true"` when the action is unavailable

        **Important:** The accessible name must always contain the text that is presented visually to comply with [WCAG 2.5.3 Label in Name](https://www.w3.org/TR/WCAG22/#label-in-name).

## Accessible label

        Each list item must have an accessible label that describes its purpose or destination. By default, the accessible name is computed from the text content inside the list item element.

        However, it can also be provided with `aria-labelledby` (referencing another element's ID) or `aria-label` (providing the label directly).

        **Important:** The accessible name must always contain the text that is presented visually to comply with [WCAG 2.5.3 Label in Name](https://www.w3.org/TR/WCAG22/#label-in-name). This ensures users of speech recognition software can activate items by speaking the visible text.

        ```tsx
        // Default: accessible name from text content

          Home
          Products

        // With aria-label for additional context

            Cart

        // With custom icon and text

          }
          >
            Settings

        ```

## Connect descriptions

        If a list item has associated descriptive text that provides additional context about its function or destination, connect it using the `aria-describedby` attribute.

        This attribute should be set to the ID of the element containing the description. Screen readers will announce the description after the list item's accessible name.

        **Note:** Use descriptions sparingly and only when additional context truly enhances understanding of the item's purpose.

        ```tsx
        // List item with associated description

            My Account

          Last login: 2 hours ago

        // List with contextual information

            Orders

          3 pending orders

        ```

## Keyboard behaviour

        | Key | Action |
        | --- | ------ |
        | `Enter` or `Space` | When focus is on a list item, `Enter` or `Space` activates it, either navigating to the destination (for items with `href`) or triggering the click handler (for items with `onClick`). |
        | `Tab` | Moves focus to the next focusable element; all list items are included in the page `Tab` sequence. |
        | `Shift + Tab` | Moves focus to the previous focusable element. |
        | `Shift + F10` (Optional) | Opens a context menu for the list item (browser-dependent). |

## Design system guarantees

    ### Keyboard Interaction

    | **RGAA criterion** | **Requirement**                                                                           | **Responsibilities** |
    | ------------------ | ----------------------------------------------------------------------------------------- | :------------------: |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When the focus is set on the List Item Link, `Enter` or `Space` activate it. | ✅ |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | (Optional) `Shift + F10`: Opens a context menu for the List Item Link. | ➖ |

    ### ARIA & Accessibility Attributes

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                                                          | **Responsibilities** |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
| [6.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#6.1) |Is each link explicit (except in specific cases)? | 👥 |
| [6.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#6.2) |Does each link have a title on every web page? (No empty links) | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If the List Item Link is semantically an HTML link, the element containing the link text or graphic has `role` of `link`. If it is semantically an HTML button, it has `role` of `button`.                                                                                              | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The List Item Link has an accessible label. By default, the accessible name is computed from any text content inside the link element. However, it can also be provided with `aria-labelledby` or `aria-label`. Note that the accessible name should always be containing the text that is presented visually. | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If a description of the List Item Link's function is present, the link element has `aria-describedby` set to the ID of the element containing the description.                                                                                                                          | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When the action associated with a List Item Link is unavailable, it has `disabled` set to `true` or `aria-disabled` set to `true`.                                                                                                                                                      | ✅ |

  Using Decathlon Vitamin's design tokens ensures:
  - **Sufficient contrast** between link text and background for users with low vision or color vision deficiencies  
  - **Visible focus styles** making it clear which list item is currently focused for keyboard navigation users
  - **Appropriate touch target sizes** for users with mobility impairments or limited dexterity

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**    | **React** | **Svelte** |
| ------------------ | :-------: | :--------: |
| Firefox + NVDA     |           |            |
| IE + JAWS          |           |            |
| Safari + VoiceOver | ✅        | ✅         |
| Android + TalkBack |           |            |
| iOS + VoiceOver    |           |            |

## Testing and compliance

The component is tested through:
- [Deque Systems' Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core/tree/master) for compliance with [WCAG Level A & AA rules & accessibility best practices](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
- [ARIA Authoring Practices Guide (APG): Link Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/link/)
- [ARIA Authoring Practices Guide (APG): Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
