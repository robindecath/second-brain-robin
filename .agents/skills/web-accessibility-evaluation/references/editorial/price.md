# Vitamin Play accessibility guidance — price (web)

Source: vitamin-play-documentation/src/content/components-accessibility/price.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Price component provides these built-in accessibility features out-of-the-box.

          - **Visual accessibility**: Sufficient contrast between price text and background using design tokens
          - **Semantic structure**: Proper HTML markup for displaying price information

## What you need to do

          **Design / Content**
          - **Visual distinction**: Ensure price variants (regular, sale, barred) are distinguishable not only by visual styling but also through alternative text.
          - **Content accessibility**: Ensure price information is clear and unambiguous.

          **Development**
          - **Alternative text**: Provide descriptive `aria-label` or `title` attributes for price variants that convey meaning only through visual styling (e.g., barred prices, discounts).
          - **Semantic context**: Ensure price information is placed in appropriate context within the page structure.
          - **Override caution**: If you add `aria-*` attributes or modify behavior, validate against this doc and re-test with screen readers.

## Accessibility attributes

        The Price component is a display-only component that presents pricing information. It does not have interactive behavior or receive keyboard focus.

        For accessibility:
        - Price information must not rely solely on visual styling (color, strikethrough, size) to convey meaning
        - Alternative text must be provided for price variants (e.g., barred prices, sale prices, discounts) using `aria-label` or `title` attributes
        - The component itself does not have specific ARIA roles as it uses standard text markup

      {/* Placeholder for Figma diagram if available */}

## Providing alternative text

        Since price information can be conveyed through visual styling alone (strikethrough for barred prices, different colors for sale prices), you must provide alternative text that makes this information accessible to screen reader users.

        Use `aria-label` on price elements to explicitly describe the meaning of the visual styling. This ensures that users who cannot perceive visual differences can understand the complete pricing information.

        **Note:** Always include context like "Former price", "Sale price", or "Discount" in the accessible label when visual styling conveys this meaning.

        ```tsx
        // ❌ WRONG: Barred price without alternative text

                €30.00
                €40.00

            // ✅ CORRECT: Barred price + discount with aria-label

            3000€

                4000€

                25% off

        ```

## Design system guarantees

    ### ARIA & Accessibility Attributes

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                             | **Responsibilities** |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------: |
| [10.9](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.9) | Information cannot be conveyed solely through shape, size, or position; an alternative that is present and relevant must be provided, such as non-visible content, an `aria-label`, or a `title` attribute, for instance. | 👥 |

  Using Decathlon Vitamin's design tokens ensures:
  - **Sufficient contrast** between price text and background for users with low vision or color vision deficiencies
  - **Readable typography** with appropriate font sizes and weights for different price variants

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
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
