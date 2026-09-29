# Vitamin Play accessibility guidance — icon-button (web)

Source: vitamin-play-documentation/src/content/components-accessibility/icon-button.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Icon Button component provides these built-in accessibility features out-of-the-box.

          - **Semantic structure:** Icon button uses proper `role="button"` or `role="link"` (with href) automatically.
          - **Keyboard navigation:** Full keyboard support (Enter and Space for buttons, Enter for links).
          - **Focus management:** Focus moves appropriately after activation based on the action performed.
          - **State management:** Disabled and loading states properly communicated via `disabled`, `aria-disabled`, and `aria-busy`.
          - **Axe Core compliance:** Component tested with Deque Systems' accessibility testing engine.
          - **Design token guarantees:** Sufficient contrast, visible focus styles, and minimum touch target size.

## What you need to do

          **Design / Content**
          - **Icon clarity:** Use universally recognized icons that clearly indicate the action.
          - **Button vs link:** Use icon buttons for actions, icon links for navigation.
          - **Error messages:** Write clear feedback for loading states and errors.
          - **Context:** Icon buttons must have clear labels for screen reader users.

          **Development**
          - **Accessible labels:** Icon buttons MUST have an accessible label via `aria-label` or `aria-labelledby` since they have no visible text.
          - **Additional descriptions:** Use `aria-describedby` for supplementary information about the icon button's function.
          - **Loading states:** Provide appropriate loading messages via `loadingScreenReaderText` prop.
          - **Override caution:** If overriding ARIA attributes, maintain compliance with keyboard accessibility, focus management, and state communication expectations.

## Accessibility attributes

      The Vitamin Play icon button has a `role="button"` by default, which identifies it as a button to assistive technologies like screen readers. When the icon button receives an `href` property, it functions as a link and has `role="link"` instead.

      **As a button (`role="button"`):**
      - Screen readers announce the element as "button" to users
      - Users understand the element is interactive and can be activated
      - Keyboard navigation works properly (Space/Enter keys trigger the button)
      - The element is included in the accessibility tree with the correct semantics. This is particularly important when using elements other than `` tags that function as buttons, ensuring WCAG compliance and proper accessibility support.

      **As a link (`role="link"`):**
      - Screen readers announce the element as "link" to users
      - Users understand the element navigates to another page or resource
      - Keyboard navigation works properly (Enter key triggers the link)
      - The element is included in the accessibility tree with the correct semantics, ensuring WCAG compliance

## Accessible label

        **Icon buttons must always have an accessible label** since they don't contain visible text. The accessible name must be provided with `aria-label` or `aria-labelledby`.

        **Important:** The accessible label should clearly describe the action the icon button performs.

        ```tsx
        // Icon button with aria-label

        // Icon button with aria-labelledby

        Delete item
        ```

## Keyboard behaviour

      - **Keyboard activation:**
        - **As a button:** Both `Enter` and `Space` keys activate the icon button
        - **As a link (with `href`):** Only the `Enter` key activates the link
      - **Focus Management:** After activation, focus is set depending on the type of action performed:
        - If an icon button opens a dialog, focus moves inside the dialog
        - If used as a link, focus moves to the linked page
        - If the icon button does not dismiss the current context, focus remains on it after activation

## Description

    If a description of the icon button's function is present, use `aria-describedby` set to the ID of the element containing the description. This allows screen readers to announce additional context about the icon button's purpose beyond the accessible label.

    ```tsx
    // Icon button with description

      Your changes will be automatically saved to the server

    ```

## Disabled state

    When the action associated with an icon button is unavailable, set the icon button's `disabled` attribute to `true`. 

    **Note:** In some cases, disabled interactive elements serve as visual indicators. For example, a disabled icon button in a toolbar may signal that an action is not currently available. In such cases, you may set the `isFocusable` prop to `true` so the icon button remains focusable with `aria-disabled="true"`.

    ```tsx
// Disabled icon button

// Disabled but focusable

    ```

## Loading state

        When the icon button is in a loading state (`loading` prop set to `true`), it automatically has:
        - `aria-busy="true"`
        - `aria-live="polite"`
        - A loading state announcement to screen readers

        You should also provide a specific text description via the `loadingScreenReaderText` prop:

        ```tsx

        ```

        This text is visible in the DOM but hidden in the UI. If CSS is disabled, users will see this alternative.

## Touch target

        All icon buttons automatically provide a **minimum touch target size of 44x44px** to meet WCAG accessibility requirements.

        For small icon buttons where the visible button is smaller than 44x44px, an **invisible touch target area** is automatically added around the button to reach the minimum size. This ensures users with mobility impairments or limited dexterity can easily interact with icon buttons without increasing the visual size.

        **Important:** The component handles this automatically. You don't need to add extra padding or modify the component.

## Design system guarantees

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    |--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------:|
    | [7.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.2), [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When the element has `role="button"`, both `Enter` and `Space` activate it. When it has `role="link"` (with `href`), only `Enter` activates it. | ✅ |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Following activation, focus is set depending on the action performed. For example, if activating the icon button opens a dialog, focus moves inside the dialog. If used as a link, focus moves to the linked page. If activation does not dismiss the current context, focus typically remains on the element after activation. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If the icon button is semantically a link, the icon button has `role` of `link`. If it is semantically a button, the icon button has `role` of `button`. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The icon button has an accessible label. Since icon buttons have no visible text, the accessible name must be provided with `aria-label` or `aria-labelledby`. Note that [the accessible name should clearly describe the action](https://www.w3.org/TR/WCAG22/#label-in-name). | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If a description of the icon button's function is present, the icon button element has `aria-describedby` set to the ID of the element containing the description. | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | When the action associated with an icon button is unavailable, the icon button has `disabled` set to `true` or `aria-disabled` set to `true`. | ✅ |
    | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | When the icon button is on loading state (`loading` prop set to `true`), it has `aria-busy` set to `true`, an `aria-label` describing its state and an `aria-live` set to `polite` to inform users the state has changed. | ✅ / 👥 |

  Using Decathlon Vitamin's design tokens ensures:
  - **Sufficient contrast** between icon button content and background for users with low vision or color vision deficiencies
  - **Visible and consistent focus styles** making it clear which icon button is currently focused for keyboard navigation
  - **Minimum touch target size** automatically provided (see Touch target section above)

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**      | **React**   | **Svelte**  |
|----------------------|-------------------|-------------------|
| Firefox + NVDA       |                   |                   |
| IE + JAWS            |                   |                   |
| Safari + VoiceOver   |        ✅         |        ✅          |
| Android + TalkBack   |                   |                   |
| iOS + VoiceOver      |                   |                   |

## Implementation notes

    **Critical:** Icon buttons must always have an accessible label via `aria-label` or `aria-labelledby` since they have no visible text.

    If you override accessibility features by adding `aria-*` attributes or modifying the component's behavior, ensure that you maintain compliance with the accessibility expectations described in this document. For example:
    - Always provide a clear, descriptive `aria-label` that describes the action (not just the icon name)
    - Maintain keyboard accessibility (Space/Enter for buttons, Enter only for links with `href`)
    - Provide appropriate ARIA roles and states (`role="button"` or `role="link"`, `aria-disabled`, `aria-busy`, `aria-pressed`)
    - Keep the focus management behavior consistent with user expectations

## Testing and compliance

The Vitamin Play icon button component is tested with:
- [Deque Systems' Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
- Compliance with [WCAG Level A & AA rules](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)
- [ARIA Authoring Practices Guide (APG): Button Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/button/)
- [ARIA Authoring Practices Guide (APG): Link Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/link/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
