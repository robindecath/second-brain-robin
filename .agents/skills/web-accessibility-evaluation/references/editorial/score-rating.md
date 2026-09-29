# Vitamin Play accessibility guidance — score-rating (web)

Source: vitamin-play-documentation/src/content/components-accessibility/score-rating.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Score Rating component provides these built-in accessibility features out-of-the-box.

          - **Design tokens:** Ensures sufficient contrast between the star icon, score text, and background for clear readability.
          - **Semantic structure:** Provides proper HTML structure for conveying rating information.
          - **Decorative icon handling:** The star icon is automatically hidden from screen readers using `aria-hidden="true"` to prevent redundant announcements.

## What you need to do

          **Design/Content**
          - **Alternative text:** Provide an accessible alternative (aria-label) to convey the complete rating value, as the visual combination of star icon and numeric text may not provide sufficient context for screen reader users.
          - **Content clarity:** Ensure the rating format and scale are understandable (e.g., "4.2/5").

          **Development**
          - **ARIA labels:** Always provide an `aria-label` that describes the rating value and scale (e.g., "Score rating: 4.2 out of 5 stars").
          - **Override caution:** If you override accessibility features (e.g., adding aria-\* attributes), ensure compliance with the accessibility expectations described in this document.

## Accessibility attributes

    The Score Rating component is a non-interactive visual indicator that displays a numeric rating value alongside a star icon. It does not have a specific ARIA role as it is purely informational.

    **Key considerations:**

    - **No specific role:** The score rating does not require an ARIA role as it is a read-only display component.
    - **Decorative icon:** The star icon is purely decorative and is hidden from assistive technologies by default (using `aria-hidden="true"`), ensuring screen readers don't announce redundant information.
    - **Alternative text required:** Since the rating is conveyed through a combination of visual icon and text, an alternative text representation is mandatory using `aria-label` to provide complete context for screen reader users.
    - **Semantic content:** The accessible label should clearly state both the rating value and the scale (e.g., "Score rating: 4.2 out of 5 stars").

## Accessible label

        ```tsx
        {/* REQUIRED: Always provide aria-label */}

        {/* Contextual example with product rating */}

        {/* With additional context */}

        {/* In product card context */}

        ```

      The Score Rating component requires an accessible label to provide complete context for screen reader users, even though the score is displayed as text.

      **When to provide context:**
      - Always include the numeric rating value
      - Always specify the scale (e.g., "out of 5 stars")
      - Add context when relevant (e.g., "Customer rating", "Average rating", "Overall rating")
      - Include review count when meaningful (e.g., "based on 89 reviews")

      **Why this matters:**
      Without proper context, screen reader users may only hear the numeric value without understanding it represents a rating on a specific scale. The accessible label ensures the rating information is complete and meaningful.

## Design system guarantees

  ### Visual accessibility

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | --- | --- | :------------------: |
    | [1.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#1.2) | Is every decorative image properly ignored by assistive technologies? | ✅ |
    | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | In each web page, is the contrast between the text color and its background color sufficiently high (except in special cases)? | ✅ |
    | [3.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.3) | In each web page, are the colors used in interface components or graphic elements conveying information sufficiently contrasting (except in specific cases)? | ✅ |
    | [10.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.2) | Information cannot be conveyed solely through shape, size, or position; an alternative that is present and relevant must be provided, such as a non-visible content, an `aria-label`, or a `title` attribute, for instance. | 👥 |

  Using Vitamin Play design tokens ensures sufficient contrast between the star icon and score text against their background, appropriate sizing for readability, and consistent spacing throughout your application.

  **Legend:**
  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Implementation examples

  ### Do's and Don'ts

### Do

          ```tsx
          {/* ✅ DO: Provide complete context */}

          {/* ✅ DO: Include additional context when helpful */}

          ```

### Don't

          ```tsx
          {/* ❌ DON'T: Omit the accessible label */}

          {/* ❌ DON'T: Provide incomplete information */}

          {/* ❌ DON'T: Use vague descriptions */}

          ```

## Testing and validation

  ### Screen reader testing

    | **Environment**    | **Status** | **Expected announcement** |
    | ------------------ | ---------- | ------------------------- |
    | Firefox + NVDA     | ✅         | "Score rating: 4.2 out of 5 stars" (or custom label) |
    | Chrome + JAWS      | ✅         | "Score rating: 4.2 out of 5 stars" (or custom label) |
    | Safari + VoiceOver | ✅         | "Score rating: 4.2 out of 5 stars" (or custom label) |
    | Mobile Safari + VoiceOver | ✅ | "Score rating: 4.2 out of 5 stars" (or custom label) |

  ### Manual testing checklist

    - Screen reader announces the complete rating value and scale
    - Visual contrast meets WCAG AA standards (4.5:1 for text, 3:1 for icons)
    - Component is readable in both light and dark modes
    - Rating information is understandable when isolated from surrounding context

## Additional notes

    - Using Vitamin Play's design tokens guarantees several essential requirements for accessibility, including sufficient contrast between the star icon, score text, and their background for users with low vision or color vision deficiencies.
    - If the Score Rating is used within a larger context (e.g., Product Card, Article Card), ensure the accessible label provides enough information to be meaningful on its own.
    - Consider announcing review counts when available to provide additional context (e.g., "4.7 out of 5 stars based on 234 reviews").

## Compliance and standards

  ### Standards compliance

    This component meets the following accessibility standards:

    - **WCAG 2.1 Level AA:** Contrast ratios, text alternatives
    - **RGAA (French accessibility framework):** Criteria 3.3 (contrast), 10.2 (information conveyed through shape)
    - **Section 508:** Information and user interface components

## Resources

  ### References

    - [RGAA - General Accessibility Improvement Framework (French)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
    - [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
    - [MDN Web Docs: ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
    - [Vitamin Play Web Repository](https://github.com/dktunited/vitamin-play-web)

  ### Contributing

  One of the Vitamin Play Design System goals is to provide guidelines & components to gain in consistency, efficiency & accessibility. The best way to achieve this is together! We would love contributions from the community _(bug reports, feature requests, suggestions, Pull Requests, whatever you want!)_.

    See the [contributing guidelines](https://github.com/dktunited/vitamin-play-web/blob/main/CONTRIBUTING.md) for details.
