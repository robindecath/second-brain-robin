# Vitamin Play accessibility guidance — accordion (web)

Source: vitamin-play-documentation/src/content/components-accessibility/accordion.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Accordion component provides these built-in accessibility features out-of-the-box.

          - **Correct semantics**: Header button inside a heading wrapper with managed `aria-expanded` / `aria-controls` pairs
          - **Keyboard support**: Focus management and toggling via Enter/Space with proper tab order integration
          - **Disabled states**: Default `disabled` and `aria-disabled` attributes when collapse is locked

        {/*  */}

## What you need to do

          **Design / Content**
          - **Heading levels:** Choose heading levels that match the page's content hierarchy; keep labels concise and unique per panel.
          - **Content accessibility:** Use clear headings, readable text, meaningful image descriptions, sufficient contrast (tokens), and a coherent reading order.

          **Development**
          - **Header structure:** Wrap each header in an HTML heading or `role="heading" aria-level`; keep only the button inside the heading container.
          - **Relationships:** Use unique `aria-controls` per panel; add `role="region"` + `aria-labelledby` only for complex panels (avoid region overload).
          - **Focus order:** Maintain logical reading order; verify keyboard and screen reader focus across panels.
          - **Disabled behavior:** Prefer `aria-disabled="true"` over removing focus when a panel must remain open; for composite widgets, consider `isFocusable = true` per ADR while keeping tab order logical.
          - **Override caution:** If you add `aria-*` attributes or change behavior, validate against this doc and re-test with keyboard and screen readers.

        {/*  */}

## Accessibility attributes

        The title of each accordion header is contained in an element with `role="button"`. Each accordion header button is wrapped in an element with `role="heading"` that has a value set for `aria-level` that is appropriate for the information architecture of the page.

        **Important:** The button element is the only element inside the heading element. If there are other visually persistent elements, they are not included inside the heading element.

        The accordion header button element has:
        - `aria-expanded` set to `true` when the panel is visible, `false` when not visible
        - `aria-controls` set to the ID of the element containing the accordion panel content
        - `disabled` or `aria-disabled="true"` when the panel is visible and cannot be collapsed

{/* 

*/}

      {/*  */}

## Accessible label

            Each accordion header must have an accessible label that describes the panel content. By default, the accessible name is computed from the text content inside the header button element.

            Optionally, each element that serves as a container for panel content has `role="region"` and `aria-labelledby` with a value that refers to the button that controls display of the panel.

            **Note:** Avoid using the region role in circumstances that create landmark region proliferation, e.g., in an accordion that contains more than approximately 6 panels that can be expanded at the same time. Role region is especially helpful to the perception of structure by screen reader users when panels contain heading elements or a nested accordion.

            ```tsx
            // Default: accessible name from text content

              Personal Information

                {/* Panel content */}

            // With region role for complex content

                  Personal Information

                {/* Panel with headings or nested accordion */}

            ```

      {/*  */}

## Keyboard behaviour

      {/*  */}

        | Key | Action |
        | --- | ------ |
        | `Enter` or `Space` | When focus is on the accordion header for a collapsed panel, `Enter` or `Space` expands the associated panel. Note: if the implementation allows only one panel to be expanded, and if another panel is expanded, collapses that panel. |
        | `Tab` | Moves focus to the next focusable element; all focusable elements in the accordion are included in the page `Tab` sequence. |
        | `Shift + Tab` | Moves focus to the previous focusable element; all focusable elements in the accordion are included in the page `Tab` sequence. |
        | `Down Arrow` (Optional) | If focus is on an accordion header, moves focus to the next accordion header. If focus is on the last accordion header, either does nothing or moves focus to the first accordion header. |
        | `Up Arrow` (Optional) | If focus is on an accordion header, moves focus to the previous accordion header. If focus is on the first accordion header, either does nothing or moves focus to the last accordion header. |
        | `Home` (Optional) | When focus is on an accordion header, moves focus to the first accordion header. |
        | `End` (Optional) | When focus is on an accordion header, moves focus to the last accordion header. |

      {/*  */}

## Design system guarantees

    ### Keyboard Interaction

    | **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                                                                                     | **Responsibilities** |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | When focus is on the accordion header for a collapsed panel, `Enter` or `Space` expands the associated panel._Note: if the implementation allows only one panel to be expanded, and if another panel is expanded, collapses that panel._                                                                       | ✅                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | When focus is on the accordion header for an expanded panel, `Enter` or `Space` collapses the panel if the implementation supports collapsing._Note: some implementations require one panel to be expanded at all times and allow only one panel to be expanded; so, they do not support a collapse function._ | ✅                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | `Tab`: Moves focus to the next focusable element; all focusable elements in the accordion are included in the page Tab sequence                                                                                                                                                                                     | ✅                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | `Shift + Tab`: Moves focus to the previous focusable element; all focusable elements in the accordion are included in the page Tab sequence.                                                                                                                                                                        | ✅                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | (Optional) `Down Arrow`: If focus is on an accordion header, moves focus to the next accordion header. If focus is on the last accordion header, either does nothing or moves focus to the first accordion header.                                                                                                  | ➖                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | (Optional) `Up Arrow`: If focus is on an accordion header, moves focus to the previous accordion header. If focus is on the first accordion header, either does nothing or moves focus to the last accordion header.                                                                                                | ➖                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | (Optional) `Home`: When focus is on an accordion header, moves focus to the first accordion header.                                                                                                                                                                                                                 | ➖                   |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)          | (Optional) `End`: When focus is on an accordion header, moves focus to the last accordion header.                                                                                                                                                                                                                   | ➖                   |

    ### ARIA & Accessibility Attributes

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Responsibilities** |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | The title of each accordion header is contained in an element with `role button`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ✅                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | Each accordion header button is wrapped in an element with `role heading` that has a value set for `aria-level` that is appropriate for the information architecture of the page._Note: If the native host language has an element with an implicit heading and aria-level, such as an HTML heading tag, a native host language element may be used._                                                                                                                                                                                                      | 👥                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | The button element is the only element inside the heading element. That is, if there are other visually persistent elements, they are not included inside the heading element                                                                                                                                                                                                                                                                                                                                                                                    | ✅                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | If the accordion panel associated with an accordion header is visible, the header button element has `aria-expanded` set to `true`. If the panel is not visible, `aria-expanded` is set to `false`.                                                                                                                                                                                                                                                                                                                                                              | ✅                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | The accordion header button element has `aria-controls` set to the ID of the element containing the accordion panel content.                                                                                                                                                                                                                                                                                                                                                                                                                                     | ✅                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | If the accordion panel associated with an accordion header is visible, and if the accordion does not permit the panel to be collapsed, the header button element has `disabled` set to `true` or `aria-disabled` set to true.                                                                                                                                                                                                                                                                                                                                    | ✅                   |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)          | (Optional) Each element that serves as a container for panel content has `role region` and `aria-labelledby` with a value that refers to the button that controls display of the panel._Note: avoid using the region role in circumstances that create landmark region proliferation, e.g., in an accordion that contains more than approximately 6 panels that can be expanded at the same time.Role region is especially helpful to the perception of structure by screen reader users when panels contain heading elements or a nested accordion._ | ✅                   |

  {/*  */}

  Using Decathlon Vitamin's design tokens ensures:
  - **Sufficient contrast** between content and background for users with low vision or color vision deficiencies
  - **Appropriate size** for heading triggers, allowing users with mobility impairments or limited dexterity to easily interact with them

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**    | **React** | **Svelte** |
| ------------------ | :-------: | :--------: |
| Firefox + NVDA     |           |            |
| IE + JAWS          |           |            |
| Safari + VoiceOver | ✅        |            |
| Android + TalkBack |           |            |
| iOS + VoiceOver    |           |            |

{/*  */}

## Testing and compliance

The component is tested through:
- [Deque Systems' Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core/tree/master) for compliance with [WCAG Level A & AA rules & accessibility best practices](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
- [ARIA Authoring Practices Guide (APG): Accordion Pattern (Sections With Show/Hide Functionality)](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

**Additional test references:**
- [Inside GOV.UK: "How we made the GOV.UK accordion component more accessible"](https://insidegovuk.blog.gov.uk/2021/10/29/how-we-made-the-gov-uk-accordion-component-more-accessible/)

{/*  */}
