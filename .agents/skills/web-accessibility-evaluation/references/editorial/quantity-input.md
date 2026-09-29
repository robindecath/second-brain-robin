# Vitamin Play accessibility guidance — quantity-input (web)

Source: vitamin-play-documentation/src/content/components-accessibility/quantity-input.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Quantity Input component provides these built-in accessibility features out-of-the-box.

          - **Correct semantics**: Input field with `role="spinbutton"` and managed `aria-valuenow`, `aria-valuemin`, `aria-valuemax` attributes
          - **Keyboard support**: Arrow keys to increment/decrement, Home/End for min/max values
          - **Button accessibility**: Increment/decrement buttons are hidden from assistive technologies (`aria-hidden="true"`, `tabindex="-1"`) to prevent keyboard traps
          - **Constraints**: Respects min/max value constraints and prevents increment/decrement when limits are reached
          - **Required fields**: Visually marked with asterisk in visible and accessible names

## What you need to do

          **Design / Content**
          - **Labels**: Provide clear, descriptive labels for each quantity input
          - **Constraints**: Define appropriate min/max values and communicate limits to users
          - **Helper text**: Use descriptive helper text to explain valid ranges
          - **Error messages**: Provide clear, actionable error messages when values are invalid

          **Development**
          - **Accessible labels**: Associate visible labels using `` with `for` attribute, or use `aria-labelledby`, `aria-label`, or `title` attribute
          - **Grouping**: For logical groups of quantity inputs, use `role="group"` with `aria-labelledby`
          - **Descriptions**: Use `aria-describedby` for additional descriptive text (helper text, constraints)
          - **Error states**: Set `aria-invalid="true"` when values are outside allowed range
          - **Form integration**: Use with FormControl component for proper error message association
          - **Value text**: If numeric value isn't user-friendly, provide `aria-valuetext` for meaningful description
          - **Override caution**: If you add `aria-*` attributes or modify behavior, validate against this doc and re-test with keyboard and screen readers

## Accessibility attributes

        The focusable element serving as the Quantity Input has `role="spinbutton"`. This is typically an input element that supports text input with `type="text"` and `inputmode="numeric"`.

        The Quantity Input element has:
        - `aria-valuenow` set to a decimal value representing the current value
        - `aria-valuemin` set to the minimum allowed value (if it has a known minimum)
        - `aria-valuemax` set to the maximum allowed value (if it has a known maximum)
        - `aria-valuetext` (optional) set to a user-friendly string when the numeric value isn't clear
        - `aria-invalid="true"` when the value is outside the allowed range

        The increment and decrement buttons have:
        - `aria-hidden="true"` to hide them from assistive technologies
        - `tabindex="-1"` to remove them from tab order
        - This prevents keyboard traps and ensures the input field handles all keyboard navigation

        **Note**: Using `` creates accessibility and usability issues. We use `type="text"` with `inputmode="numeric"` instead for better accessibility.

## Accessible label

            The Quantity Input should have an accessible label provided by one of the following methods:

            1. A visible label element using the `for` attribute that corresponds to the input's `id` attribute
            2. A visible label referenced by `aria-labelledby`
            3. An `aria-label` attribute
            4. At minimum, a `title` attribute

            For best accessibility, use the component with the FormControl component which provides proper label, helper text, and error message associations.

            ```tsx
            {/* 1. Using a visible label with 'for' attribute */}
            Product Quantity

            {/* 2. Using aria-labelledby */}
            Product Quantity

            {/* 3. Using aria-label */}

            {/* 4. Best practice: with FormControl */}

              Quantity

              Select between 1 and 10
              Please enter a valid quantity

            ```

            **Grouping related inputs**

            If a set of Quantity Inputs is presented as a logical group with a visible label, the inputs should be included in an element with `role="group"` that has `aria-labelledby` set to the ID of the label element.

            You can also use the `` and `` elements for this purpose.

            ```tsx
            {/* Using role="group" */}

              Order Quantities

                Shipping Quantity:

                Billing Quantity:

            {/* Using fieldset/legend */}

              Order Quantities

                Shipping Quantity:

                Billing Quantity:

            ```

            **Adding descriptions**

            If the presentation includes additional descriptive static text relevant to a Quantity Input or group, the input or group should have `aria-describedby` set to the ID of the element containing the description.

            ```tsx

              Order Quantities

                Enter quantities for shipping and billing.

                Shipping Quantity:

                Billing Quantity:

            ```

            **Custom value text**

            If the value of `aria-valuenow` is not user-friendly (e.g., representing days of the week with numbers), set `aria-valuetext` to a string that makes the value understandable.

            ```tsx
            }
            />
            ```

## Keyboard behaviour

        | **Key** | **Action** |
        | --- | --- |
        | `Tab` | Moves focus to the input field |
        | `Shift + Tab` | Moves focus to the previous focusable element |
        | `Up Arrow` | Increases the value by the step amount |
        | `Down Arrow` | Decreases the value by the step amount |
        | `Home` | Sets the value to the minimum (if `min` is defined) |
        | `End` | Sets the value to the maximum (if `max` is defined) |
        | `Enter` | Submits the form (if in a form context) |

        **Note**: The increment and decrement buttons are not focusable via Tab navigation. This prevents keyboard traps and ensures all keyboard interactions happen through the input field.

## Design system guarantees

    **ARIA and accessibility attributes**

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | --- | --- | :---: |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity uses appropriate HTML input type `text` with the `inputmode=number` attribute value to optimize the user experience and allow browsers to offer relevant input features. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity has an accessible label provided by one of the following: a visible and close label element using the `for` attribute on the label that corresponds to the input's `id` attribute ; a visible label referenced by the value of `aria-labelledby`; an `aria-label` or at least a `title` attribute | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If a set of Input Quantity is presented as a logical group with a visible label, the inputs are included in an element with `role group` that has the property `aria-labelledby` set to the ID of the element containing the label. | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If the presentation includes additional descriptive static text relevant to an Input Quantity or group, the Input Quantity or group has the property `aria-describedby` set to the ID of the element containing the description. | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Mandatory fields should be clearly marked, either with general text placed prominently before the form or by employing an asterisk in both the visible name and its accessible counterpart. If the form is short and has only one required field, it may only show hints for optional fields. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The increment and decrement buttons are not focusable using tab navigation to prevent keyboard trap and confusion. The input field itself receives focus and handles keyboard navigation. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The increment and decrement buttons have `aria-hidden="true"` and `tabindex="-1"` to hide them from assistive technologies while maintaining visual functionality. For cases where buttons need to be focusable but not actionable, set `isFocusable: true` in component props. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The component respects min and max value constraints and prevents increment/decrement when limits are reached. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The focusable element serving as the Input Quantity has role `spinbutton`. This is typically an element that supports text input. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity element has the `aria-valuenow` property set to a decimal value representing the current value of the Input Quantity. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity element has the `aria-valuemin` property set to a decimal value representing the minimum allowed value of the Input Quantity if it has a known minimum value. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity element has the `aria-valuemax` property set to a decimal value representing the maximum allowed value of the Input Quantity if it has a known maximum value. | ✅ |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If the value of `aria-valuenow` is not user-friendly, e.g., the day of the week is represented by a number, the `aria-valuetext` property is set on the Input Quantity element to a string that makes the Input Quantity value understandable. | 👥 |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Input Quantity element has `aria-invalid` set to `true` if the value is outside the allowed range. Note that most implementations prevent input of invalid values, but in some scenarios, blocking all invalid input may not be practical. | 👥 |

    **Visual accessibility**

    | **RGAA criterion** | **Requirement** | **Responsibilities** |
    | --- | --- | :---: |
    | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Design tokens guarantee sufficient contrast between the input field and its background for users with low vision or color vision deficiencies. | ✅ |
    | [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | The input field has a visible focus indicator that meets contrast requirements. | ✅ |
    |  | The increment/decrement buttons meet touch target size requirements (minimum 44x44px) even though they are not focusable, ensuring they can be easily activated by users with mobility impairments. | ✅ |

  Using Vitamin Play design tokens ensures sufficient contrast between the input field, buttons, and their background, appropriate sizing for readability and interaction, and consistent spacing throughout your application.

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

    **Tested with:**

    | **Environment**    | **React** | **Svelte** | **Vue** |
    | ------------------ | :-------: | :--------: | :-----: |
    | Firefox + NVDA     |           |            |         |
    | IE + JAWS          |           |            |         |
    | Safari + VoiceOver |           |            |         |
    | Android + TalkBack |           |            |         |
    | iOS + VoiceOver    |           |            |         |

## Implementation notes

    **Out of range values**

    The Input Quantity element has `aria-invalid` set to `true` if the value is outside the allowed range. Note that in our implementation, we prevent input of invalid values, but in some scenarios, blocking all invalid input may not be practical.

    **Button labels**

    The increment and decrement buttons have descriptive `aria-label` attributes to ensure screen reader users understand their function ("Decrease/increase value"). You can customize these labels by rendering your own buttons via the `startSlot` and `endSlot` props.

    **Focusable and disabled**

    VpInputQuantity can be focusable even when disabled by setting both `isFocusable` and `isDisabled` properties to `true`. The component remains visible for screen reader and keyboard navigation users. This is recommended when the component's presence provides important context, such as knowing all possible options in a menu.

## Testing and compliance

    The Vitamin Play Quantity Input component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [ARIA Authoring Practices Guide (APG): Spinbutton Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
