# Vitamin Play accessibility guidance — select (web)

Source: vitamin-play-documentation/src/content/components-accessibility/select.mdx

Do,
	Dont,
	ColumnLayout,
	Column,
	ContentBlock,
	Callout,
	FigmaImage,
	WebOnly,
	AndroidOnly,
	AppleOnly,
} from "@ui";

## Responsibilities at a glance

## What the design system guarantees

					The Select component provides these built-in accessibility features out-of-the-box.

					- **Native semantics:** It uses the native HTML `` element, which exposes the control and its options to assistive technologies.
					- **Keyboard support:** The browser provides standard keyboard operation for opening the option list, moving through options, selecting a value, and cancelling.
					- **Focus visibility:** Design tokens provide a visible focus state with sufficient contrast.
					- **Required-field indication:** Required fields are identified consistently in both the visible and accessible name.

## What you need to do

					**Design / Content**
					- **Label:** Provide a clear, concise label that describes the choice users must make.
					- **Placeholder:** Use the placeholder option to guide a selection, not as a replacement for the label.
					- **Required fields:** Identify clearly which selects are required. If you use asterisks, ensure a sentence explains their meaning before the form starts.
					- **Helper and error text:** Make instructions and errors specific, actionable, and visible.

					**Development**
					- **Accessible name:** Associate a visible `` with the Select, or provide `aria-labelledby`, `aria-label`, or, as a last resort, `title`.
					- **Descriptions:** Connect relevant helper text or instructions with `aria-describedby`.
					- **Validation:** Use `VpFormControl` so error messages are associated with the Select and announced by screen readers.
					- **Groups:** Use `` and ``, or `role="group"` with `aria-labelledby`, for related Select controls.
					- **Override caution:** When adding ARIA attributes or changing behavior, re-test with keyboard and screen readers.

## Accessibility attributes

				Select is a native form control. Its semantics, selected value, available options, disabled state, and required state are exposed by the browser. Screen readers commonly announce the control as a combo box.

				Do not replace the native element with a custom control when native Select behavior meets the need. For multi-select, editable input, filtering, or custom option content, use [Combobox](/components/web/combobox) and implement the full ARIA combobox pattern instead.

## Accessible label

				Give every Select an accessible label. A visible, nearby `` is the preferred method because it benefits all users. When a visible label cannot be used, reference visible text with `aria-labelledby`, use `aria-label`, or provide a `title` as a last resort.

				Use `VpFormControl` for labelled fields with helper text, validation, and required status. It keeps the information related to the Select programmatically associated.

				```tsx

					Delivery method

						Choose a delivery method
						Standard delivery
						Express delivery

					Choose the delivery speed that suits you.
					Choose a delivery method to continue.

				```

				**Grouping and descriptions**

				When several Select controls form one logical group, use native `` and `` elements. If native grouping is not possible, use `role="group"` and reference the group label with `aria-labelledby`. Associate additional static instructions with `aria-describedby`.

				```tsx

					Shipping preferences
					Country

						France

				```

## Keyboard behaviour

				Keyboard behavior is provided by the browser and may vary slightly by operating system.

				| Key | Action |
				| --- | --- |
				| `Tab` | Moves focus to the Select control. |
				| `Space`, `Arrow Up`, or `Arrow Down` | Opens the option list when the Select has focus. |
				| `Arrow Up` or `Arrow Down` | Moves through options while the list is open. |
				| `Space` or `Enter` | Selects the focused option. |
				| `Escape` | Closes the option list without changing the selected option. |

## Design system guarantees

		| RGAA criterion | Requirement | Responsibilities |
		| --- | --- | :---: |
		| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The Select uses a native HTML `` element, preserving its standard semantics and browser-provided keyboard behavior. | ✅ |
		| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | If a set of Select controls is presented as a logical group with a visible label, they are included in an element with `role="group"` and `aria-labelledby`, or in a native `` with ``. | 👥 |
		| [11.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.1) | The Select has an accessible label provided by a visible label associated with its `id`, `aria-labelledby`, `aria-label`, or at least a `title` attribute. | 👥 |
		| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | If additional descriptive static text is relevant to a Select or Select group, it is associated using `aria-describedby`. | 👥 |
		| [11.10](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.10) | Mandatory fields are clearly marked, either with general text placed prominently before the form or by employing an asterisk in both the visible name and its accessible counterpart. | ✅ / 👥 |
		| [11.11](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#11.11) | Error messages are clear, understandable, associated with the Select, and perceivable by screen reader users. | 👥 |

		Using Vitamin Play design tokens helps maintain sufficient contrast between the Select and its background, as well as an appropriate target size for people with low vision or limited dexterity.

		**Legend:**

		- ✅ = Compliant (design system guarantee)
		- 👥 = User responsibility

## Screen readers restitution

		| Environment | React Wrapper | Svelte Wrapper |
		| --- | :---: | :---: |
		| Firefox + NVDA |  |  |
		| IE + JAWS |  |  |
		| Safari + VoiceOver |  |  |
		| Android + TalkBack |  |  |
		| iOS + VoiceOver |  |  |

## Testing and compliance

			The Vitamin Play select component is tested with:

			- Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
			- Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
			- [MDN: ``](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
			- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
