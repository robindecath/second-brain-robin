# Vitamin Play accessibility guidance — bottom-sheet (web)

Source: vitamin-play-documentation/src/content/components-accessibility/bottom-sheet.mdx

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

				The Bottom Sheet component provides these built-in accessibility
				features out-of-the-box.

				- **Dialog semantics:** The sheet container is exposed as a dialog for assistive technologies.
				- **Escape key support:** The sheet can be dismissed with the `Escape` key.
				- **Focus containment:** Keyboard focus stays within the sheet while it is open.
				- **Focus restoration:** When closed, focus returns to the element that opened the sheet.
                - **Backdrop click:** The bottom sheet closes when clicking outside of it (configurable).

## What you need to do

				**Design/Content**

				- **Bottom sheet naming:** Provide either `aria-labelledby` that references a visible title, or `aria-label`.
				- **Content structure:** Use headings, lists, and readable text to preserve semantic structure.
				- **Reading order:** Keep a logical sequence for screen readers and keyboard users.

				**Development**

				- **Contain bottom sheet controls:** All elements required to operate the bottom sheet must be descendants of the element that has role `dialog`.
				- **Label the bottom sheet:** The bottom sheet has either a value set for the `aria-labelledby` property that refers to a visible bottom sheet title, or a label specified by `aria-label`.
				- **Content accessibility:** Ensure content within the bottom sheet is accessible, including proper headings, readable text, and meaningful descriptions for images and interactive elements.
				- **Override caution:** If overriding accessibility (`aria-*`) or component behavior, verify compliance with expected accessibility behavior.

## Accessibility attributes

			Bottom Sheet uses dialog semantics and accessible naming to ensure proper
			screen reader support:

			- **`role="dialog"`**: The sheet is announced as a dialog.
			- **`aria-labelledby`** or **`aria-label`**: Required to provide an accessible name.
			- **Dialog control containment**: Action buttons and close controls are part of the dialog subtree.

			**Screen reader announcement:**

			Screen readers announce the bottom sheet as a dialog followed by its
			accessible name.

{/*

## Accessible label

	The bottom sheet must have an accessible name with either `aria-labelledby` or
	`aria-label`.

	**Using `aria-labelledby` (recommended):**

	Reference the visible heading in the sheet header so visual and accessible labels stay aligned.

			```tsx

				Choose size

						Choose size

						Select your preferred product size.

			```

	**Using `aria-label`:**

	Use this when no visible title exists.

	**Important:** According to WCAG 2.5.3 Label in Name, if visible text exists, the `aria-label` should include it.

			```tsx

				Open size options

						Select your preferred product size.

			```

*/}

## Keyboard behaviour

			The Bottom Sheet component supports the following keyboard interactions:

			| Key           | Action                                                                                                       |
			| ------------- | ------------------------------------------------------------------------------------------------------------ |
			| `Tab`         | Moves focus to the next focusable element in the bottom sheet. Focus wraps from the last to the first element. |
			| `Shift + Tab` | Moves focus to the previous focusable element in the bottom sheet. Focus wraps from the first to the last element. |
			| `Escape`      | Closes the bottom sheet and returns focus to the trigger element.                                            |

		**Focus management:**

			Bottom sheets contain their own tab sequence while open. Keyboard users do
			not move focus to background content until the sheet closes.

			- Focus remains trapped within the bottom sheet.
			- On close, focus returns to the control that opened it.
			- Place initial focus on the most relevant element for the task (for example, close button or primary action).

        When bottom sheet appears, the first item that gets focus depends on the type of dialog:
            - If it’s a text only bottom sheet without actions the close action button takes focus.
            - If it’s a bottom sheet which ask a user decision, the primary action takes the focus.

## Design System guarantees

	| RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
	| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
	| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Sufficient contrast between text and background.                                                                                               |       👥 / ✅        |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The element that serves as the dialog container has a role of `dialog`.                                                                        |        ✅        |
    | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The dialog container element has `aria-modal` set to `true`.                                                                                   |        ✅        |
	| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | All elements required to operate the dialog are descendants of the element that has role `dialog`.                                             |        👥        |
	| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | The dialog has either a value set for the `aria-labelledby` property that refers to a visible dialog title, or a label specified by `aria-label`. |        👥        |
	| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | The bottom sheet can be operated using keyboard only (`Tab`, `Shift + Tab`, `Escape`).                                                        |        👥 / ✅        |
	| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus is visible on all interactive elements within the bottom sheet.                                                                          |     👥 / ✅        |

	Using Vitamin Play design tokens ensures sufficient contrast between bottom sheet content and background, appropriate sizing for readability, and consistent spacing throughout your application.

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

	Bottom Sheet uses the same drawer dialog accessibility behavior on web. For
	implementation details, refer to [modal component accessibility documentation](/components/web/modal?tab=a11y).
