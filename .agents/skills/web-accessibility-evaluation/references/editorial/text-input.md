# Vitamin Play accessibility guidance — text-input (web)

Source: vitamin-play-documentation/src/content/components-accessibility/text-input.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Text Input component provides these built-in accessibility features out-of-the-box.

          - **Semantic HTML:** Uses native `` element with appropriate type attributes
          - **Required field:** The field is programmatically marked as required with required set to true directly on the input. An asterisk (*) is just there for visual highlighting and is hidden from screenreaders by default.
          - **Form integration:** Proper name and id attributes for form submission
          - **Design tokens:** Sufficient contrast and appropriate sizing for users with low vision or mobility impairments

## What you need to do

        **Design / Content**
        - **Label clarity:** Provide clear, descriptive labels for each input field
        - **Label positioning:** Place labels near the input field to which it is linked.
        - **Helper text:** Include helpful descriptions for complex or sensitive fields
        - **Error messages:** Ensure error messages are specific and actionable
        - **Required fields:** The best way to indicate a required field is to replace the asterisk (*) by "(required)" as asterisks may not be understood/seen well by all users.
        - **Input format:** Visibly indicate expected formats before submission

          **Development**
          - **Accessible labels:** Always provide an accessible label via ``, `aria-labelledby`, or `aria-label`
          - **Field grouping:** Use `role="group"` or `` for logical groups with `aria-labelledby` or ``
          - **Descriptions:** Associate helper text using `aria-describedby`
          - **Form control integration:** Use with FormControl component for automatic associations
          - **Input types:** Use appropriate input types (email, tel, number, etc.) with caution for type="number"
          - **Testing:** Verify keyboard navigation and screen reader announcements

## Accessibility attributes

        The Text Input uses a native `` element, which provides implicit `role="textbox"`. Screen readers announce the input with its role, label, state (required, disabled), and any associated descriptions.

        When using VpFormControl, the component automatically manages ARIA associations:
        - Label is connected via `for` attribute matching the input's `id`
        - Helper text is connected via `aria-describedby`
        - Error messages are connected via `aria-describedby` and `aria-invalid` when status is "error"
        - Required state is indicated via `aria-required="true"` or the `required` attribute

## Accessible label

        ```tsx
        {/* Best practice: Use VpFormControl for automatic associations */}

          Email address

          We'll never share your email.

        {/* Alternative: Explicit label with for attribute */}
        Shipping address

        {/* Using aria-labelledby for existing text */}
        Username

        {/* IMPORTANT: Must contain visible text "First name" */}

        First name
        ```

      **How to provide accessible labels:**

        The Text Input requires an accessible name from one of these methods (in order of preference):

        1. **VpFormControl + VpFormLabel** - Automatically creates proper associations
        2. **``** - Visible label using standard HTML
        3. **`aria-labelledby`** - Reference to existing text element
        4. **`aria-label`** - Programmatic label (use sparingly)
        5. **`title`** - Last resort fallback (avoid if possible)

        When using custom accessible labels, ensure the visible text is contained within the accessible label to meet WCAG 2.5.3 (Label in Name).

## Keyboard behaviour

          | Key | Action |
          |-----|--------|
          | `Tab` | Moves focus to the text input field |
          | `Shift + Tab` | Moves focus out of the field to the previous element |
          | `Left / Right Arrow` | Moves the cursor one character at a time |
          | `Ctrl / Cmd + Arrow` | Jumps the cursor to the beginning or end of a word |
          | `Shift + Arrow` | Selects text character by character |
          | `Enter` | Submits the input or triggers the associated action |
          | `Escape` | Clears the current input or dismisses the focus |
          | `Backspace / Delete` | Removes the character before or after the cursor |

## Design system guarantees

    ### ARIA and accessibility attributes

    | **RGAA criterion** | **Requirement** | **React Wrapper** | **Svelte Wrapper** |
    | ------------------ | --------------- | :---------------: | :----------------: |
    | [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | The Input has an accessible label provided by one of the following: a visible and close label element using the `for` attribute on the label that corresponds to the input's `id` attribute ; a visible label referenced by the value of `aria-labelledby`; an `aria-label` or at least a `title` attribute | 👥 | 👥 |
    | [11.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.5) | If the presentation includes additional descriptive static text relevant to an Input or Inputs group, the Input or Input group has the property `aria-describedby` set to the ID of the element containing the description. | 👥 | 👥 |
    | [11.8](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.8) | If a set of Input is presented as a logical group with a visible label, the Inputs are included in an element with `role group` that has the property `aria-labelledby` set to the ID of the element containing the label. | 👥 | 👥 |
    | [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Mandatory fields should be clearly marked, either with general text placed prominently before the form or by employing an asterisk in both the visible name and its accessible counterpart. If the form is short and has only one required field, it may only show hints for optional fields. | ✅ | ✅ |
    | [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | For all fields whose input format is controlled, the expected format is visibly indicated before submitting the form and, in the case of an error return, the error message mentions a real example of input. | 👥 | 👥 |
    | [11.13](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.13)| Utilize appropriate HTML input types (type attribute) such as `text`, `email`, `password`, `number`, etc., to optimize the user experience and allow browsers to offer relevant input features. | ➖ | ➖ |

  Using Decathlon Vitamin's design tokens guarantees several essential requirements for accessibility like sufficient contrast between the input field and its background for users with low vision or color vision deficiencies, and ensuring that input fields are of appropriate size, allowing users with mobility impairments or limited dexterity to easily interact with them.

## Screen readers restitution

      | Environment | React | Svelte |
      |-------------|:-----:|:------:|
      | Firefox + NVDA |  |  |
      | IE + JAWS |  |  |
      | Safari + VoiceOver | ✅ | ✅ |
      | Android + TalkBack |  |  |
      | iOS + VoiceOver |  |  |

Using Vitamin Play design tokens ensures sufficient contrast between input elements and their background, appropriate sizing for readability and touch targets, and consistent spacing across all platforms.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Expected implementation details

    - The Text Input component is designed to work with the `VpFormControl` component, which provides clear and understandable error messages when there are issues with the input's value or format
    - The input has an accessible label provided by a visible label element, `aria-labelledby`, `aria-label`, or at minimum a `title` attribute
    - For grouped inputs (e.g., shipping vs. billing address), use `role="group"` with `aria-labelledby`, or `` with ``
    - Additional descriptive text is associated via `aria-describedby`
    - Required fields are marked with an explicit "(required)" indicator rather than asterisk alone
    - For controlled-format fields, the expected format is visibly indicated before submission

## Implementation notes

    - The component uses a native `` element to leverage browser accessibility features
    - Be cautious with `type="number"` as it can create [accessibility and usability issues](https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/). Consider using `type="text"` with `inputmode="numeric"` and `pattern="[0-9]*"` instead
    - When disabled (`disabled` prop), the component is neither interactive nor focusable. For cases where disabled elements serve as contextual indicators, use the `isFocusable` prop to allow keyboard focus while maintaining `aria-disabled="true"`
    - Do not override accessibility features without ensuring WCAG compliance

## Testing and compliance

    - The component is tested through [Axe Core accessibility testing engine](https://github.com/dequelabs/axe-core) for WCAG Level A & AA compliance
    - Meets [RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/) (French accessibility) standards
    - Follows [ARIA 1.2 textbox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/textbox/) best practices

## Additional resources

    - [MDN Web Docs: Input](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
