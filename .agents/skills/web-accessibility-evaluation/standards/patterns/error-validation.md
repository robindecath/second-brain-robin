# Error Validation

## Overview

Forms must help users understand when something has gone wrong and how to fix it. WCAG 3.3.x criteria cover four progressive levels of error support: identification, description, suggestion, and prevention.

## The Four WCAG Error Criteria

| Criterion                    | Requirement                                                                                                         | Level |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----- |
| 3.3.1 Error Identification   | If an error is detected, the item in error is **identified** and the error is **described to the user in text**     | A     |
| 3.3.2 Labels or Instructions | Labels or instructions are provided when content requires user input                                                | A     |
| 3.3.3 Error Suggestion       | If an error is detected and suggestions are known, the suggestion is provided (unless it would jeopardize security) | AA    |
| 3.3.4 Error Prevention       | For legal/financial/data transactions: reversible, checked, or confirmable                                          | AA    |

## Key Principles

**1. Errors must be in text** — color alone, icons alone, or border changes alone do not satisfy 3.3.1.

**2. Errors must be associated with their field** — not just displayed elsewhere on the page. Use `aria-describedby`, `accessibilityHint`, or a direct visual/programmatic association.

**3. Error summary for multi-field forms** — when multiple fields fail simultaneously, provide a summary at the top of the form AND individual field messages. Move focus to the summary.

**4. Inline validation timing** — validate on blur (when leaving a field), not on each keystroke, to avoid announcing errors before the user has finished typing.

**5. Never clear valid input on error** — preserve what the user entered.

## Error Message Content

A good error message answers: "What went wrong?" and "How do I fix it?"

- ❌ "Invalid value"
- ❌ "Error in field 3"
- ✅ "Email address must contain @. Example: name@domain.com"
- ✅ "Password must be at least 8 characters. You entered 5."

## Platform Implementation

See your platform skill for implementation details:

- **Web**: `../../references/references/forms.md` — `aria-describedby`, `aria-invalid`, error summary pattern
- **iOS**: `../../references/references/error-validation.md` — `@AccessibilityFocusState` + `accessibilityHint`
- **Android**: `../../references/references/forms.md` — `TextInputLayout.setError()`, `OutlinedTextField(isError, supportingText)`

## Resources

- WCAG 3.3.1 Error Identification: <https://www.w3.org/WAI/WCAG22/Understanding/error-identification>
- WCAG 3.3.2 Labels or Instructions: <https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions>
- WCAG 3.3.3 Error Suggestion: <https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion>
- WCAG 3.3.4 Error Prevention: <https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data>
