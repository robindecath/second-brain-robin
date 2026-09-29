# Vitamin Play accessibility guidance — article-card (web)

Source: vitamin-play-documentation/src/content/components-accessibility/article-card.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Article Card component provides these built-in accessibility features out-of-the-box.

          - **Keyboard navigation**: When focus is set on the card, it passes to the main call-to-action inside
          - **Action accessibility**: The call-to-action follows VpButton or VpLink accessibility guidelines
          - **Decorative images**: Card illustration images have empty alt attributes
          - **Automatic labeling**: Unless customized, the card's call-to-action is labeled with the card's title using aria-labelledby
          - **Semantic structure**: Proper heading hierarchy when textual content is used

## What you need to do

        **Design / Content**

        - **List structure**: Wrap multiple cards in lists to provide navigation shortcuts and item enumeration for screen reader users
        - **Reading order**: Ensure title comes first semantically (even if visually the label appears above)
        - **Content accessibility**: Ensure content within cards uses proper headings, readable text, and meaningful image descriptions if necessary

          **Development**

          - **Custom actions**: If providing your own call-to-action, ensure it has an accessible name using aria-label, .sr-only content, or aria-labelledby linking to the card title
          - **Testing responsibility**: Test keyboards, screen readers, and automated tools if overriding accessibility features

## Accessibility attributes

          The Article Card uses semantic HTML and ARIA attributes to provide accessible navigation and interaction patterns.

          **Key attributes:**

          - The card's call-to-action uses a semantic `` element with `role="button"` (or `` with `role="link"`)
          - The card's decorative illustration image has an empty `alt=""` attribute
          - Unless the card has additional textual content, it does not include heading elements
          - The card's call-to-action is labeled with `aria-labelledby` pointing to the card's title (unless customized)
          - The action inherits all accessibility features from VpButton or VpLink components

## Sufficient contrast in all cases

        The Vitamin Play article card uses an unifrom overlay behind the text to ensure sufficient contrast regardless of the background image used.

        This design choice guarantees a minimum contrast ratio of 4.5:1 between text and background (even white photos), meeting WCAG AA standards for readability and accessibility.

        A gradient is placed above the overlay to enhance visual appeal, but the underlying uniform dark layer is what ensures consistent accessibility across all card instances, regardless of the background image's brightness or color.

## Keyboard behaviour

        The Article Card implements keyboard navigation to ensure users can interact with cards using only the keyboard.

        | Key | Action |
        | --- | ------ |
        | `Tab` | Moves focus to the card's call-to-action button |
        | `Enter` or `Space` | Activates the card (triggers the call-to-action) |

## Design System guarantees

The following tables detail the accessibility criteria guaranteed by the Article Card component. These are automatically handled by the component and do not require additional implementation.

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
|                    | When the focus is set on the card, the focus is passed to the main call-to-action (link or button) inside the card. | ✅ |
| [1.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#1.2) | The card's decorative illustration image has an empty `alt=""` attribute. | ✅ |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | The card's text has sufficient contrast no matter the photo used in background thanks to the uniform overlay | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Unless otherwise requested, the article card's call-to-action is labeled with (`aria-labelledby`) the card's visual title. | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The call-to-action (link or button) inside the card follows the accessibility implementation details of the VpButton or VpLink component. | ✅ |
| [9.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#9.1) | Unless the card exceptionally has textual content other than its label and title, the article card does not include any heading-type semantic elements. | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between card elements and their background, appropriate sizing for readability and touch targets, and consistent spacing throughout your application.

**Legend:**
- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

When using a screen reader, the Article Card provides clear and concise information:

- Screen reader users can navigate to the card's call-to-action using standard navigation commands
- The call-to-action is announced with the card's title as its accessible name
- Decorative images are skipped (empty alt attribute)
- Title and label text are announced - if necessary - in semantic order (title first, then label)
- When using lists, screen readers announce the total number of cards and current position

**Tested with:**

| **Environment**    | **React** | **Svelte** | **Vue** |
| ------------------ | :-------: | :--------: | :-----: |
| Firefox + NVDA     |           |            |         |
| IE + JAWS          |           |            |         |
| Safari + VoiceOver | ✅        | ✅         |         |
| Android + TalkBack |           |            |         |
| iOS + VoiceOver    |           |            |         |

## Expected implementation details

    - When displaying multiple cards, use lists (``, ``) to enhance assistive technology experience
    - Screen readers provide shortcuts to lists and enumerate items
    - The component is tested with Axe Core accessibility testing engine for WCAG Level A & AA compliance
    - Design tokens guarantee sufficient color contrast and appropriately-sized touch targets

## Additional resources

    - [Inclusive Components: Cards by Heydon Pickering](https://inclusive-components.design/cards/)
    - [Accessible cards by Kitty Giraudel](https://kittygiraudel.com/2022/04/02/accessible-cards/)
    - [WCAG 2.2 Label in Name (Success Criterion 2.5.3)](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
    - [VpArticleCard Web Technical Documentation](https://github.com/dktunited/vitamin-play-web/tree/main/packages/logic/src/components/VpArticleCard/ACCESSIBILITY.md)
    - [RGAA (French Accessibility Guidelines)](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
