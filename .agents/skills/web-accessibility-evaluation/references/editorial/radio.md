# Vitamin Play accessibility guidance — radio (web)

Source: vitamin-play-documentation/src/content/components-accessibility/radio.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Radio component provides these built-in accessibility features out-of-the-box.

          - **Semantic structure:** Radio buttons use proper `role="radio"` within a `role="radiogroup"`.
          - **Keyboard navigation:** Full keyboard support including arrow key navigation between radio options.
          - **State management:** Checked state is properly communicated via `checked` attribute.
          - **Focus management:** Focus moves to checked radio or first radio when entering the group.
          - **Touch accessibility:** Native input elements remain accessible for touch-based navigation.
          - **Axe Core compliance:** Component tested with Deque Systems' accessibility testing engine.
          - **Design token guarantees:** Sufficient contrast and appropriate sizing through design tokens.

## What you need to do

          **Design / Content**
          - **Label clarity:** Provide clear, descriptive labels for each radio option and the group.
          - **Group labeling:** Ensure the radio group has a visible label or legend.
          - **Required indicator:** Use explicit text like "(required)" instead of asterisk symbols.
          - **Helper text:** Provide helper text to guide users on what to select.
          - **Error messages:** Write clear, specific error messages when validation fails.

          **Development**
          - **Accessible labels:** Each radio must have an accessible label via content, `aria-labelledby`, or `aria-label`.
          - **Group labeling:** The radiogroup must have a label via `aria-labelledby` or `aria-label`.
          - **Additional descriptions:** Use `aria-describedby` for helper text and error messages.
          - **FormControl integration:** Use with VpFormControl for complete form accessibility.
          - **Override caution:** Test thoroughly if overriding default ARIA attributes.

## Accessibility attributes

        The Radio component uses ARIA roles and attributes to ensure proper screen reader support:

        **Radio Group Container:**
        - `role="radiogroup"`: Identifies the container as a radio group
        - `aria-labelledby` or `aria-label`: Provides an accessible name for the group
        - `aria-describedby`: References helper text or error messages (optional)

        **Radio Buttons:**
        - `role="radio"`: Identifies each option as a radio button
        - `checked`: Boolean indicating the checked state (true/false)
        - `aria-labelledby`, `aria-label`, or text content: Provides an accessible name
        - `aria-describedby`: References additional descriptive information (optional)

        **Focus Behavior:**
        - When focus enters the group, it moves to the checked radio or the first radio if none is checked
        - Arrow keys navigate between radios and automatically check the focused option
        - Tab/Shift+Tab move focus in and out of the entire group

## Accessible label

      Each radio button must have an accessible label. There are three ways to provide this:

## Using visible text content (recommended):

      The simplest approach is to place the label text as children of the VpRadioGroupItem.

      ````tsx

        Email

      ````

## Using `aria-labelledby`:

      Reference an external label element by its ID.

      ````tsx

      Phone
      ````

## Using `aria-label`:

      Provide a label directly as an attribute (use when no visible label exists).

      ````tsx

      ````

## Radio group label:

      The group itself also needs a label, typically provided through VpFormLabel when using VpFormControl, or via `aria-labelledby` or `aria-label` attributes.

      ````tsx
      {/* Radio Group with label using VpFormControl */}

          Preferred contact method:

          {/* radio items */}

      {/* Or using aria-label directly */}

        {/* radio items */}

      ````

## Keyboard behaviour

        The radio component follows standard keyboard navigation patterns:

        | Key | Action |
        |-----|--------|
        | `Tab`, `Shift + Tab` | Move focus into and out of the radio group. When entering, focus moves to the checked radio or first radio if none checked. |
        | `Space` | Checks the focused radio button if not already checked. |
        | `Right Arrow`, `Down Arrow` | Move to next radio, check it, and uncheck previous. Wraps to first from last. |
        | `Left Arrow`, `Up Arrow` | Move to previous radio, check it, and uncheck previous. Wraps to last from first. |

        **Note:** When radio groups are nested in a toolbar, arrow keys navigate without automatically changing the checked state.

## Design System guarantees

  This section clarifies which accessibility criteria are guaranteed by the component and which require user implementation.

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

  ### Keyboard interaction

  | **RGAA criterion** | **Requirement** | **Responsibilities** |
  |----------|-------------|:--------:|
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Tab and Shift+Tab move focus into/out of radio group. Focus moves to checked or first radio. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Space key checks the focused radio button. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Arrow keys navigate between radios, checking the focused one and unchecking others. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Arrow navigation wraps from last to first and vice versa. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | In toolbar context, arrow keys navigate without changing checked state. | ✅ |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Enter key support in toolbar context (optional). | ➖ |

  ### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement** | **Responsibilities** |
|----------|-------------|:--------:|
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Radio buttons contained in element with `role="radiogroup"`. | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Each radio button has `role="radio"`. | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Checked state communicated via `checked` attribute (true/false). | ✅ |
| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | Each radio element has accessible label via content, `aria-labelledby`, or `aria-label`. | 👥 |
| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | Radiogroup has accessible label via `aria-labelledby` or `aria-label`. | 👥 |
| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | Additional information referenced via `aria-describedby` on radiogroup or radios. | 👥 |
| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus visible on all interactive elements. | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Disabled radios are not focusable (unless `isFocusable` is set). | ✅ |

### Form integration

| **RGAA criterion** | **Requirement** | **Responsibilities** |
|----------|-------------|:--------:|
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Error messages are clear and understandable. | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Error messages are associated with the field via `aria-describedby`. | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Required fields are indicated clearly (recommended: explicit text vs. asterisk). | 👥 |
| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | Helper text provided to guide selection. | 👥 |

  Using Vitamin Play design tokens ensures:
  - **Sufficient contrast** between radio buttons and backgrounds for users with low vision or color deficiencies
  - **Appropriate sizing** of radio buttons and touch targets for users with mobility impairments or limited dexterity
  - **Consistent spacing** that meets accessibility requirements across all platforms

## Screen readers restitution

| **Environment**    | **React** | **Svelte** | **Vue** |
| ------------------ | :-------: | :--------: | :-----: |
| Firefox + NVDA     |           |            |         |
| IE + JAWS          |           |            |         |
| Safari + VoiceOver | ✅        |            |         |
| Android + TalkBack |           |            |         |
| iOS + VoiceOver    |           |            |         |

## Expected implementation details

    - Use with `VpFormControl` for clear error messages associated with the input
    - Each radio item requires an accessible label (text content, `aria-labelledby`, or `aria-label`)
    - Radio group requires a label (`aria-labelledby` or `aria-label`)
    - Use `aria-describedby` to reference additional information for the group or individual radios
    - Replace asterisk `*` with explicit "(required)" text for required fields
    - For composite widgets, consider `isFocusable={true}` to keep disabled items focusable with `aria-disabled="true"` (see [ADR](https://github.com/dktunited/vitamin-play-web/blob/main/ADR/008-disabling-for-accessibility.md))
    - When overriding accessibility features, ensure compliance with expectations in this documentation

## Implementation notes

    The Radio component uses a strategy that keeps native input elements within accessible bounds (not `display: none` or fully off-screen) to ensure:
    - Touch-based navigation works on mobile devices with screen readers
    - Users can explore content by dragging their finger across the screen
    - Proper focus and visual feedback on mobile devices

## Testing and compliance

    The Vitamin Play radio component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [ARIA Authoring Practices Guide (APG): Radio Group Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources
