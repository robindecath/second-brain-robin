# Vitamin Play accessibility guidance — modal (web)

Source: vitamin-play-documentation/src/content/components-accessibility/modal.mdx

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

        The Modal component provides these built-in accessibility features
        out-of-the-box.

        - **Dialog role:** The modal container automatically has `role="dialog"` and `aria-modal="true"` attributes for proper screen reader announcement.
        - **Escape key:** The modal closes when the `Escape` key is pressed.
        - **Backdrop click:** The modal closes when clicking outside of it (configurable).
        - **Focus management:** Focus is trapped within the modal when open.

## What you need to do

        **Design/Content**

        - **Dialog labeling:** Provide either an `aria-labelledby` attribute referencing a visible title, or an `aria-label` attribute for the modal.
        - **Content accessibility:** Ensure content within the modal uses proper heading hierarchy, readable text, and meaningful descriptions for images and interactive elements.
        - **Reading order:** Maintain a logical reading order for screen readers by structuring content appropriately.

        **Development**

        - **Dialog structure:** Structure all interactive elements required to operate the modal as descendants of the modal container.
        - **ARIA labeling:** Implement either `aria-labelledby` pointing to a visible title element or `aria-label` on the dialog container.
        - **Content hierarchy:** Structure modal content with proper semantic HTML (headings, paragraphs, lists).
        - **Override caution:** If overriding accessibility features (e.g., adding custom `aria-*` attributes) or modifying behavior that could affect accessibility, ensure compliance with the expectations in this documentation.

## Accessibility attributes

      The Modal component uses several ARIA attributes to ensure proper accessibility:

      - **`role="dialog"`**: Applied to the modal container element to indicate it contains a dialog.
      - **`aria-modal="true"`**: Applied to the modal container to indicate that content outside the modal is inert when the modal is open.
      - **`aria-labelledby`** or **`aria-label`**: One of these attributes must be present on the dialog container to provide an accessible name (see Accessible label section below for implementation details).

      **Screen reader announcement:**

      Screen readers announce the modal as "Dialog" followed by the accessible name. When the modal opens, screen readers typically announce "Dialog [name]" or similar phrasing depending on the screen reader.

## Accessible label

  The modal must have an accessible name provided through either `aria-labelledby` or `aria-label`.

  **Using `aria-labelledby` (recommended):**

  Reference the ID of a visible title element within the modal. This is the preferred approach as it ensures visual and programmatic consistency.

      ```tsx

            Confirm Action

            Are you sure you want to proceed?

            Cancel
            Confirm

      ```

  **Using `aria-label`:**

  Provide a text description directly on the dialog element when there is no visible title.

  **Important:** According to WCAG 2.5.3 Label in Name, if you provide a custom `aria-label`, it should contain the visible title text if one is present.

      ```tsx

            Your changes have been saved successfully.

            Close

      ```

## Keyboard behaviour

      The Modal component supports the following keyboard interactions:

      | Key              | Action                                                                                               |
      | ---------------- | ---------------------------------------------------------------------------------------------------- |
      | `Tab`            | Moves focus to the next focusable element within the modal. Focus wraps from the last to the first element. |
      | `Shift + Tab`    | Moves focus to the previous focusable element within the modal. Focus wraps from the first to the last element. |
      | `Escape`         | Closes the modal and returns focus to the trigger element.                                           |

    **Focus management:**

      Modal dialogs contain their tab sequence. That is, `Tab` and `Shift + Tab` do not move focus outside the dialog. Unlike non-modal dialogs, modal dialogs do not provide means for moving keyboard focus outside the dialog window without closing the dialog.

      - Focus is trapped within the modal - keyboard navigation cannot reach elements outside the modal while it's open, preventing accidental interaction with background content.
      - When the modal closes, focus returns to the element that triggered the modal.

      When modal appears, the first item that gets focus depends on the type of dialog:

      - If it's a text only modal without bottom actions the close action button takes focus.
      - If it's a modal which ask a user decision/confirmation, the primary button takes the focus.
      - If it's a modal which ask for a destructive action, the "cancel" button takes the focus.

## Design System guarantees

  ### ARIA and accessibility attributes

  | RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
  | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The element that serves as the dialog container has a role of `dialog`.                                                                        |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The dialog container element has `aria-modal` set to `true`.                                                                                   |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | All elements required to operate the dialog are descendants of the element that has role `dialog`.                                             |        👥        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The dialog has either a value set for the `aria-labelledby` property that refers to a visible dialog title, or a label specified by `aria-label`. |        👥        |

  ### Visual accessibility

  | RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
  | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
  | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2)             | Sufficient contrast between text and background.                                                                                               |       👥 / ✅        |
  | [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7)            | Focus is visible on all interactive elements within the modal.                                                                                 |      👥 / ✅        |

  Using Vitamin Play design tokens ensures sufficient contrast between modal content and background, appropriate sizing for readability, and consistent spacing throughout your application.

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

The `alertdialog` role is a special-case dialog role designed specifically for dialogs that divert users' attention to a brief, important message. If your modal serves as an alert that requires immediate user attention or action, consider using the alert dialog pattern instead. For more information, see the [ARIA authoring practices guide: alert dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/).

## Testing and compliance

  The Vitamin Play Modal component is tested with:

  - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
  - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
  - [ARIA Authoring Practices Guide (APG): Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
  - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

  - [MDN Web Docs: Dialog element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
  - [W3C WAI-ARIA Practices: Modal Dialog Example](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/dialog/)
