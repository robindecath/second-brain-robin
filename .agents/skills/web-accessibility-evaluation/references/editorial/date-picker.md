# Vitamin Play accessibility guidance — date-picker (web)

Source: vitamin-play-documentation/src/content/components-accessibility/date-picker.mdx

## Responsibilities at a glance

## What the design system guarantees

        The Date Picker shadcn component provides these built-in accessibility features out-of-the-box.

          - **Correct semantics**: Combined input pattern with proper `role="combobox"`, `role="dialog"`, and `role="grid"` for calendar
          - **Keyboard support**: Full keyboard navigation with Enter/Space for selection, Arrow keys for calendar navigation, Escape to close
          - **ARIA attributes**: Managed `aria-haspopup`, `aria-expanded` and `aria-controls` for input/dialog relationship

## What you need to do

          **Design / Content**
          - **Clear labels**: Provide descriptive labels for the date input field
          - **Format instructions**: Place format hints in the text input helper text (e.g., "Format: MM/DD/YYYY"), not in a placeholder, to ensure they stay visible while typing.
          - **Free text entry**: Never make the input read-only or force selection through the calendar — typing the date manually must always remain possible
          - **Error messages**: Use clear, actionable error messages for invalid dates or out-of-range selections
          - **Date constraints**: Clearly communicate date range restrictions (min/max dates)

          **Development**
          - **Input association**: Connect the input field with its label using proper `` element or `aria-labelledby`
          - **Format instructions**: Manually add `aria-describedby` to link the input with format instructions in helper text
          - **Calendar dialog**: Implement the calendar popup as a modal dialog with proper focus management
          - **Date announcements**: Ensure selected dates and navigation within the calendar are announced to screen readers
          - **Error handling**: Use `aria-invalid` and manually link error messages via `aria-describedby`
          - **Technical reference**: Follow the W3C ARIA Date Picker Combobox Pattern

## Accessibility attributes

      The date picker uses a combobox pattern where the text input controls a calendar popup:

      **1. Text Input**
      - The text input field has `role="combobox"` - this is the combobox element
      - `aria-haspopup="dialog"` indicates that activating the icon button opens a calendar dialog
      - `aria-expanded="false"` when closed, `"true"` when the calendar is open
      - `aria-controls` points to the ID of the calendar dialog element

      **2. Calendar Popup**
      - The calendar container has `role="dialog"` with `aria-modal="true"`
      - Inside the dialog, the date grid has `role="grid"`
      - Each date cell has `role="gridcell"` with appropriate `aria-selected` state
      - Navigation buttons have proper button semantics with descriptive labels

      **Important:** The text input IS the combobox. The combobox pattern ensures screen readers announce the relationship between the input field and the calendar popup, while the grid pattern provides efficient keyboard navigation through dates.

## Accessible label

      Each date picker input must have an accessible label that describes its purpose. The label should be associated with the input using a `` element or `aria-labelledby` attribute.

      Additionally, you must manually add `aria-describedby` to link:
      - **Format instructions**: Helper text describing the expected date format (e.g., "MM/DD/YYYY")
      - **Constraints**: Min/max date restrictions
      - **Error messages**: Validation feedback when input is invalid

      **Example:**
      ```tsx
      Departure Date

      Format: MM/DD/YYYY

        Select a date between {minDate} and {maxDate}

      {isInvalid && (

          Please enter a valid date

      )}
      ```

      **Important:** Always place format instructions in visible helper text (not placeholder) to ensure they remain visible while typing (RGAA 11.10.5). Use `aria-describedby` to link all relevant instructions and messages to the input.

## Keyboard behaviour

      **Input Field**

      | Key | Action |
      | --- | ------ |
      | `Enter` or `Space` on icon | Opens the calendar dialog and moves focus to the selected date (or today's date if none selected) |
      | `Tab` | Moves focus to the next focusable element |
      | `Shift + Tab` | Moves focus to the previous focusable element |

      **Calendar Dialog (Combobox)**

      | Key | Action |
      | --- | ------ |
      | `Enter` or `Space` | Selects the focused date, closes the calendar, and returns focus to the combobox input |
      | `Escape` | Closes the calendar without making a selection and returns focus to the combobox input |
      | `Right Arrow` | Moves focus to the next day |
      | `Left Arrow` | Moves focus to the previous day |
      | `Down Arrow` | Moves focus to the same day in the next week |
      | `Up Arrow` | Moves focus to the same day in the previous week |
      | `Home` | Moves focus to the first day of the current week |
      | `End` | Moves focus to the last day of the current week |
      | `Page Up` | Changes the calendar to the previous month and focuses the same day |
      | `Page Down` | Changes the calendar to the next month and focuses the same day |
      | `Shift + Page Up` | Changes the calendar to the previous year and focuses the same day |
      | `Shift + Page Down` | Changes the calendar to the next year and focuses the same day |
      | `Tab` | Moves focus to the next focusable element within the dialog (e.g., "Previous Month", "Next Month" buttons) |

      **Reference:** For complete implementation details, see the W3C ARIA Date Picker Pattern.

## Design system guarantees

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| ------------------ | --------------- | :------------------: |
| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Sufficient contrast between date picker input and background (4.5:1 minimum) | ✅ |
| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Complete ARIA implementation with `role="dialog"`, `role="grid"`, `aria-modal`, `aria-haspopup`, `aria-expanded`, `aria-controls`, and `aria-selected` attributes | ✅ |
| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | Full keyboard interaction support (Enter/Space, Escape, Tab, Arrow keys, Home/End, Page Up/Down) for opening calendar, navigating dates, and selecting values | ✅ |
| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus indicator is clearly visible with sufficient contrast | ✅ |
| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | The date input has an accessible label provided by: ``, `aria-labelledby`, `aria-label`, or `title` attribute | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | You must manually add `aria-describedby` to link date format instructions, constraints, and error messages to the input | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Date format instructions must be in visible helper text (not placeholder) to remain visible while typing | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Mandatory fields should be clearly marked with "(required)" or an asterisk in both visible and accessible labels | 👥 |
| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Error messages must be clear, actionable, include real examples (e.g., "Enter date as MM/DD/YYYY, for example 01/15/2024"), and be manually linked via `aria-describedby` | 👥 |
| | Appropriate sizing for date picker elements (minimum touch targets) for users with mobility impairments | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between date picker elements and their background, appropriate sizing for readability, and consistent spacing throughout your application.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

**Tested with:**

| **Environment**    | **React** |
| ------------------ | :-------: |
| Firefox + NVDA     |           |
| IE + JAWS          |           |
| Safari + VoiceOver |    ✅     |
| Android + TalkBack |           |
| iOS + VoiceOver    |           |

## Testing and compliance

The Vitamin Play Date Picker component is tested with:
- Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
- Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide (APG): Combobox with Date Picker Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-datepicker/)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
