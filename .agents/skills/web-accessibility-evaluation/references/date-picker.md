# Web Date Picker Accessibility

The latest Vitamin Play accessibility documentation describes the Date Picker as a combobox controlling a calendar dialog.

## Design-system guarantees

The component provides the structural pattern when used correctly:

- the input uses `role="combobox"`;
- the calendar popup uses `role="dialog"` and `aria-modal="true"`;
- the calendar uses `role="grid"` and date cells use `role="gridcell"`;
- `aria-haspopup`, `aria-expanded`, and `aria-controls` connect the input and dialog;
- Enter/Space opens or selects, arrow keys navigate, and Escape closes.

## Consumer responsibilities

- Provide a clear visible label associated with the input.
- Keep free-text date entry available; do not make the input calendar-only or read-only.
- Put format instructions in visible helper text, not only in a placeholder.
- Link format instructions, constraints, and errors with `aria-describedby`.
- Set `aria-invalid` and provide actionable validation messages for invalid or out-of-range dates.
- Ensure selected dates, month navigation, and dialog focus changes are announced.
- Ensure the input, calendar trigger, and navigation controls have usable keyboard access and touch targets.

```tsx
<label htmlFor="departure-date">Departure date</label>
<VpDatePicker
  id="departure-date"
  aria-describedby="departure-format departure-error"
/>
<span id="departure-format">Format: MM/DD/YYYY</span>
```

## Verification

Test the full combobox/dialog/grid interaction with keyboard and a screen reader. Confirm focus moves into the dialog when it opens and returns to the input when it closes. Check that the accessible name, expanded state, selected date, disabled dates, constraints, and errors are announced.

## References

- WAI-ARIA Authoring Practices: Combobox Date Picker Pattern
- WCAG 1.3.1, 3.3.1, 3.3.2, 4.1.2
