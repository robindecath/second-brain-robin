# Vitamin Play accessibility guidance — product-card (web)

Source: vitamin-play-documentation/src/content/components-accessibility/product-card.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Product Card component provides these built-in accessibility features out-of-the-box.

          - **Keyboard navigation**: Focus management through interactive elements within the card
          - **Semantic structure**: Proper HTML structure with headings and links
          - **Image accessibility**: Decorative images are properly handled
          - **Link accessibility**: Product title link follows VpLink accessibility guidelines
          - **Action buttons**: Icon buttons follow VpIconButton accessibility guidelines with proper labeling

## What you need to do

        **Design/Content**

        - **Alternative text**: Provide meaningful alt text for product images (only if the image conveys important information that are not in the text, otherwise use empty alt for decorative images)
        - **Product titles**: Ensure titles are descriptive and meaningful (All caps usage is forbidden for accessibility reasons)
        - **Price information**: Include currency and pricing information clearly
        - **List structure**: Wrap multiple cards in lists to provide navigation shortcuts for screen reader users

          **Development**

          - **Image alt text**: Ensure product images have descriptive alt attributes if necessary, or empty alt if decorative
          - **Icon button labels**: Provide accessible labels (aria-label) for action buttons (like, add to cart, etc.)
          - **Testing responsibility**: Test keyboards, screen readers, and automated tools if overriding accessibility features

## Accessibility attributes

          The Product Card uses semantic HTML and ARIA attributes to provide accessible navigation and interaction patterns.

          **Key attributes:**

          - The product title link uses a semantic `` element with proper structure
          - Product image uses descriptive `alt` attribute for non-decorative images
          - Action buttons (like, wishlist) have `aria-label` attributes for screen readers
          - Star rating component has appropriate accessibility labels
          - Price information is wrapped in semantic elements for clarity

## Keyboard behaviour

        The Product Card implements keyboard navigation to ensure users can interact with all elements using only the keyboard.

        | Key | Action |
        | --- | ------ |
        | `Tab` | Moves focus through interactive elements (product link, action buttons) |
        | `Enter` | Activates the focused element (navigates to product, triggers action) |
        | `Space` | Activates focused buttons (like, wishlist actions) |

## Design System guarantees

The following tables detail the accessibility criteria guaranteed by the Product Card component. These are automatically handled by the component and do not require additional implementation.

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [1.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#1.1) | The card's decorative illustration image has an empty alt. | 👥 |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Action buttons (like, wishlist) must have accessible labels using aria-label. | 👥 |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When navigating with keyboard, focus moves through all interactive elements in logical order. | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | All interactive elements are keyboard accessible. | ✅ |
| [9.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#9.1) | While headings are necessary for structured content in complex product cards, we recommend avoiding them in product cards within list pages to maintain a clean heading hierarchy and improve screen reader navigation. | 👥 |
| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus is clearly visible on all interactive elements. | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between card elements and their background, appropriate sizing for readability and touch targets, and consistent spacing throughout your application.

**Legend:**
- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

When using a screen reader, the Product Card provides clear and concise information:

- Screen reader users can navigate through all interactive elements (product link, action buttons)
- Product title is announced as a link
- Product image alt text is announced (if provided)
- Star rating score and number of reviews are announced
- Price information is clearly stated
- Action buttons are announced with their accessible labels
- When using lists, screen readers announce the total number of cards and current position

**Tested with:**

| **Environment**    | **React** | **Svelte** | **Vue** |
| ------------------ | :-------: | :--------: | :-----: |
| Firefox + NVDA     |           |            |         |
| IE + JAWS          |           |            |         |
| Safari + VoiceOver |    ✅     |      ✅     |         |
| Android + TalkBack |           |            |         |
| iOS + VoiceOver    |           |            |         |

## Expected implementation details

    - When displaying multiple product cards, use lists (``, ``) to enhance assistive technology experience
    - Screen readers provide shortcuts to lists and enumerate items
    - Ensure product images have descriptive alt attributes that describe the product if necessary, or empty alt if they are purely decorative
    - Provide clear aria-label attributes for action buttons (e.g., "Add to wishlist", "Add to cart")
    - The component is tested with Axe Core accessibility testing engine for WCAG Level A & AA compliance
    - Design tokens guarantee sufficient color contrast and appropriately-sized touch targets

## Additional resources

    - [WCAG 2.2 Images of Text (Success Criterion 1.4.5)](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)
    - [WCAG 2.2 Label in Name (Success Criterion 2.5.3)](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
    - [Accessible Product Cards - Smashing Magazine](https://www.smashingmagazine.com/2020/02/accessible-ecommerce/)
    - [VpProductCard Web Technical Documentation](https://github.com/dktunited/vitamin-play-web/tree/main/packages/frameworks/vue/src/components/VpProductCard)
    - [RGAA (French Accessibility Guidelines)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
