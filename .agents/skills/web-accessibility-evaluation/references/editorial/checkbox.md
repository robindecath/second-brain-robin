# Vitamin Play accessibility guidance — checkbox (web)

Source: vitamin-play-documentation/src/content/components-accessibility/checkbox.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Checkbox component provides these built-in accessibility features out-of-the-box.

          - **Semantic structure:** Checkbox uses proper `role="checkbox"` with state management.
          - **Keyboard navigation:** Full keyboard support with Space key to toggle checked state.
          - **State management:** Checked, unchecked, and mixed states properly communicated via `aria-checked`.
          - **Touch accessibility:** Native input elements remain accessible for touch-based navigation.
          - **Axe Core compliance:** Component tested with Deque Systems' accessibility testing engine.
          - **Design token guarantees:** Sufficient contrast and appropriate sizing through design tokens.

## What you need to do

          **Design / Content**
          - **Label clarity:** Provide clear, descriptive labels for each checkbox and group.
          - **Group labeling:** Ensure checkbox groups have visible labels or legends.
          - **Required indicator:** Use explicit text like "(required)" instead of asterisk symbols.
          - **Helper text:** Provide helper text to guide users on what to select.
          - **Error messages:** Write clear, specific error messages when validation fails.

          **Development**
          - **Accessible labels:** Each checkbox must have an accessible label via content, `aria-labelledby`, or `aria-label`.
          - **Group labeling:** Checkbox groups must have a label via `role="group"` with `aria-labelledby` or use ``.
          - **Additional descriptions:** Use `aria-describedby` for helper text and error messages.
          - **FormControl integration:** Use with VpFormControl for complete form accessibility.
          - **Override caution:** Test thoroughly if overriding default ARIA attributes.

## Accessibility attributes

        The Checkbox component uses ARIA attributes to communicate its role, state, and properties to assistive technologies. The component implements the [ARIA Checkbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/) to ensure compatibility with screen readers and other assistive technologies.

        **Checkbox Element:**
        - `role="checkbox"`: Identifies the element as a checkbox
        - `aria-checked`: Indicates the checked state (true/false/mixed)
        - `aria-labelledby`, `aria-label`, or text content: Provides an accessible name
        - `aria-describedby`: References helper text or error messages (optional)

        **Checkbox Group:**
        - `role="group"`: Identifies a container for related checkboxes
        - `aria-labelledby` or `aria-label`: Provides an accessible name for the group
        - Alternative: Use `` with `` for native HTML grouping

## Accessible label

Every checkbox must have an accessible label that clearly describes its purpose. The label must be programmatically associated with the checkbox so assistive technologies can announce it properly.

## Visible label with text content

The recommended approach is to provide visible text content within the checkbox component. This ensures the label is visible to all users and programmatically associated with the checkbox.

```tsx
Enable notifications
```

## Label referenced by aria-labelledby

When the label exists elsewhere in the DOM, use `aria-labelledby` to reference it by ID.

```tsx
Enable notifications

```

## Checkbox group label

For groups of checkboxes, provide a group label using `role="group"` or a `` with ``.

```tsx

  Notification Settings
  Email notifications
  Push notifications
  SMS notifications

```

Or with fieldset:

```tsx

  Notification Settings
  Email notifications
  Push notifications
  SMS notifications

```

## Keyboard behaviour

The Checkbox component supports full keyboard interaction, allowing users to navigate to and toggle checkboxes without using a mouse. Keyboard support is essential for users with motor impairments and power users who prefer keyboard navigation.

| **Key**       | **Action**                                                                                           | **RGAA** |
| ------------- | ---------------------------------------------------------------------------------------------------- | -------- |
| `Space`       | When the checkbox has focus, pressing `Space` toggles the checkbox between checked and unchecked states | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)     |
| `Tab`         | Moves focus to the next focusable element                                                            | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)     |
| `Shift + Tab` | Moves focus to the previous focusable element                                                        | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)     |

## Design System guarantees

The Vitamin Play design system ensures several accessibility requirements are met through design tokens and component architecture. These guarantees apply across all platforms and relieve implementers from managing these concerns manually.

### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                  | **Responsibilities** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------: |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | The checkbox has `role="checkbox"`                                                                                                                                                                                                               | ✅          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | The checkbox has an accessible label provided by visible text content, `aria-labelledby`, or `aria-label`                                                                                                                                       | 👥          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | When checked, the checkbox has state `aria-checked="true"`                                                                                                                                                                                       | ✅          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | When unchecked, the checkbox has state `aria-checked="false"`                                                                                                                                                                                    | ✅          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | When partially checked, the checkbox has state `aria-checked="mixed"`                                                                                                                                                                            | ✅          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | If checkboxes are presented as a logical group with a visible label, they are included in an element with `role="group"` that has `aria-labelledby` set to the label's ID                                                                       | 👥          |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)           | If additional descriptive text is relevant to a checkbox or group, the checkbox or group has `aria-describedby` set to the description's ID                                                                                                      | 👥          |

### Form integration

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                  | **Responsibilities** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------: |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10)           | When used with FormControl, error messages are clearly associated with the checkbox and announced by screen readers                                                                                                                             | ✅          |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10)           | Required checkboxes display a clear indicator (preferably "(required)" instead of "*")                                                                                                                                                           | 👥          |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10)           | Helper text is programmatically associated with the checkbox                                                                                                                                                                                     | ✅          |

### Visual accessibility

| **RGAA criterion** | **Requirement**                                                                                                                                                                                                                                  | **Responsibilities** |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------: |
| [3.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.1)           | State changes are not conveyed by color alone                                                                                                                                                                                                   | ✅          |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2)           | Checkbox and background have sufficient color contrast (4.5:1 minimum) for users with low vision                                                                                                                                                | ✅          |
| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7)           | Focus indicator is clearly visible with sufficient contrast                                                                                                                                                                                                      | ✅          |
|             | Checkbox is appropriately sized (minimum 24x24px touch target) for users with limited dexterity                                                                                                                                                 | ✅          |

  Using Vitamin Play design tokens ensures:
  - **Sufficient contrast** between checkbox and background for users with low vision or color deficiencies
  - **Appropriate sizing** of checkboxes and touch targets for users with mobility impairments or limited dexterity
  - **Consistent spacing** that meets accessibility requirements across all platforms

  **Legend:**

  - ✅ = Compliant (Design system guarantees)
  - 👥 = User responsibility (Developer must implement)

## Screen readers restitution

| **Environment**          | **Tested** | **Notes**                                                                                     |
| ------------------------ | ---------- | --------------------------------------------------------------------------------------------- |
| Safari + VoiceOver       | ✅          | Announces role, label, and checked/unchecked state correctly                                  |
| Firefox + NVDA           |            |                                                                                               |
| Chrome + JAWS            |            |                                                                                               |
| Edge + Narrator          |            |                                                                                               |

## Expected implementation details

The following implementation patterns ensure optimal accessibility when using the Checkbox component. While the component provides core accessibility features, implementers must ensure proper labeling, group structure, and form integration.

### Using with FormControl (Recommended)

The Checkbox component works best when integrated with the `FormControl` component, which provides error handling, helper text, and proper ARIA associations:

```tsx

  Enable email notifications

  We'll send you updates about your account
  {isInvalid && You must accept to continue}

```

### Accessible label strategies

Provide an accessible label using one of these three methods:

```tsx
{/* 1. Visible text content (Recommended) */}
I accept the terms and conditions

{/* 2. Using aria-labelledby to reference an existing label */}
I accept the terms and conditions

{/* 3. Using aria-label for programmatic labeling */}

```

### Grouping checkboxes

When presenting multiple related checkboxes, use `role="group"` or `` with proper labeling:

```tsx
{/* Using role="group" */}

  Notification Settings
  Email notifications
  Push notifications
  SMS notifications

{/* Using fieldset/legend */}

  Notification Settings
  Email notifications
  Push notifications
  SMS notifications

```

### Adding descriptions

Use `aria-describedby` to associate descriptive text with a checkbox or group:

```tsx

  Notification Settings

    Choose how you'd like to receive updates about your account.

  Email notifications
  Push notifications
  SMS notifications

```

### Required field indicators

Replace the default asterisk (*) with an explicit "(required)" label:

```tsx

  (required)}>
    I accept the terms and conditions

```

### Focusable disabled state

When a disabled checkbox needs to remain focusable for contextual awareness, use the `isFocusable` prop:

```tsx

  Premium feature (upgrade required)

```

This sets `aria-disabled="true"` instead of the native `disabled` attribute, allowing keyboard focus while preventing interaction.

## Implementation notes

Additional implementation considerations to ensure optimal accessibility and user experience across all platforms.

### Rendering strategy

The checkbox component customizes the native input rendering by visually hiding it while keeping it accessible:

- The native `` element remains in the DOM and is not completely hidden via `display: none`
- This approach ensures touch-based navigation works on mobile devices with screen readers
- Users navigating by touch can discover and interact with the checkbox
- The element remains focusable and receives proper visual feedback

## Testing and compliance

    The Vitamin Play checkbox component is tested with:

    - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
    - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
    - [ARIA Authoring Practices Guide (APG): Checkbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/)
    - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
