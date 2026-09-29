# Vitamin Play accessibility guidance — sticker (web)

Source: vitamin-play-documentation/src/content/components-accessibility/sticker.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Sticker component provides these built-in accessibility features out-of-the-box.

          - **Design tokens:** Ensures sufficient contrast between text and background for readability.

## What you need to do

          **Design / Content**
          - **Alternative text:** Provide an accessible alternative (aria-label, title, or visible text) when the sticker conveys information through shape, size, or position alone.

          **Development**
          - **Override caution:** If you override accessibility features (e.g., adding aria-\* attributes), ensure compliance with the accessibility expectations described in this document.

## Accessibility attributes

    The Sticker component is a visual indicator that contains text and does not have a specific ARIA role. It is typically rendered as a simple HTML element (such as a `` or ``) with semantic content.

    **Key considerations:**

    - **No specific role:** The sticker does not require an ARIA role as it is purely informational.
    - **Text content:** The text within the sticker should be meaningful and accessible to screen readers.
    - **Alternative text:** If the sticker conveys information through visual styling (color, size, position), provide an alternative using `aria-label`, a `title` attribute, or ensure the information is available through visible text.

## Accessible label

        ```tsx
        {/* Default: Text content is the accessible label */}
        New

        {/* With aria-label for additional context */}
        {/* IMPORTANT: Must contain visible text "-20%" (WCAG 2.5.3) */}

          -20%

        {/* With title attribute */}

          24/7

        ```

      The Sticker component uses its text content as the accessible label by default. When the sticker's meaning is clear from its visible text, no additional label is needed.

      **When to provide an alternative:**
      - When the context is not clear from the text alone
    Example: If the context is already clear from the surrounding page (like a "Holiday Sale" banner nearby), you might not need the aria-label at all.
      - When the sticker uses color, shape, or position to convey meaning beyond the text
      - When the visible text is abbreviated and needs clarification

## Design system guarantees

  ### Visual accessibility

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | --- | --- | :------------------: |
    | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | In each web page, does the contrast between the color of the text and the color of its background meet the contrast requirements? | ✅ |
    | [10.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.2) | In each web page, is information not given solely through shape, size or position still available when stylesheets are disabled? | 👥 |

  Using Vitamin Play design tokens ensures sufficient contrast between the sticker text and its background, appropriate sizing for readability, and consistent spacing throughout your application.

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

    - When the sticker conveys information solely through color, shape, size, or position, provide an accessible alternative such as `aria-label`, a `title` attribute, or visible text.
    - Ensure the sticker's text content is meaningful and provides sufficient context for users relying on screen readers.

## Testing and compliance

    The Vitamin Play Sticker component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources
