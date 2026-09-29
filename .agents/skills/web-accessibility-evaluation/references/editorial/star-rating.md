# Vitamin Play accessibility guidance — star-rating (web)

Source: vitamin-play-documentation/src/content/components-accessibility/star-rating.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Star Rating component provides these built-in accessibility features out-of-the-box.

          - **Design tokens:** Ensures sufficient contrast between filled and unfilled states to clearly communicate the rating value.
          - **Semantic structure:** Provides proper HTML structure for conveying rating information.

## What you need to do

          **Design/Content**
          - **Alternative text:** Provide an accessible alternative (aria-label or title attribute) to convey the rating value, as star icons alone do not provide sufficient context for screen reader users.
          - **Content clarity:** Ensure the rating format and scale are understandable (e.g., "4.2/5").

          **Development**
          - **ARIA labels:** Always provide an `aria-label` that describes the rating value and scale (e.g., "The score is 4.2 out of 5 stars").
          - **Override caution:** If you override accessibility features (e.g., adding aria-\* attributes), ensure compliance with the accessibility expectations described in this document.

## Accessibility attributes

    The Star Rating component is a non-interactive visual indicator that displays a rating value using star icons. It does not have a specific ARIA role as it is purely informational.

    **Key considerations:**

    - **No specific role:** The star rating does not require an ARIA role as it is a read-only display component.
    - **Alternative text required:** Since the rating is conveyed through visual shape and position of stars, an alternative text representation is mandatory using `aria-label` or a `title` attribute.
    - **Semantic content:** The accessible label should clearly state both the rating value and the scale (e.g., "The score is 4.2 out of 5 stars").

## Accessible label

        ```tsx
        {/* REQUIRED: Always provide aria-label */}

        {/* With title attribute as fallback */}

        {/* Contextual example with product rating */}

        ```

      The Star Rating component requires an accessible label because the rating information is conveyed solely through visual representation (star shapes and fill positions).

      **When to provide context:**
      - Always include the numeric rating value
      - Always specify the scale (e.g., "out of 5 stars")
      - Add context when relevant (e.g., "Customer rating", "Average rating")
      - Include review count when meaningful (e.g., "based on 127 reviews")

      **Why this matters:**
      Screen reader users cannot perceive the visual representation of filled/unfilled stars. An explicit text description ensures the rating information is equally accessible to all users.

## Design system guarantees

  ### Visual accessibility

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | --- | --- | :------------------: |
    | [3.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.3) | In each web page, are the colors used in interface components or graphic elements conveying information sufficiently contrasting (except in specific cases)? | ✅ |
    | [10.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.2) | Information cannot be conveyed solely through shape, size, or position; an alternative that is present and relevant must be provided, such as a non-visible content, an `aria-label`, or a `title` attribute, for instance. | 👥 |

  Using Vitamin Play design tokens ensures sufficient contrast between the star icons and their background, appropriate sizing for readability, and consistent spacing throughout your application.

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

## Testing and compliance

    The Vitamin Play Star Rating component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
