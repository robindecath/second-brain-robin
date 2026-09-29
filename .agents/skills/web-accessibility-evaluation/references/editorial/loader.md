# Vitamin Play accessibility guidance — loader (web)

Source: vitamin-play-documentation/src/content/components-accessibility/loader.mdx

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

      The Loader component provides these built-in accessibility features out-of-the-box.

        - **Alternative text support:** The component accepts children that will be visually hidden but accessible to screen readers
        - **Status role:** The component automatically includes `role="status"` to indicate assistive technologies should announce updates
        - **Live region:** The component includes `aria-live="polite"` to ensure screen readers announce loading state changes
        - **Reduced motion:** All animations are reduced by default when the user has set a **Prefers reduce motion** parameter on their device
        - **Design tokens:** Using Vitamin Play design tokens ensures sufficient contrast between the loader and its background

## What you need to do

        **Design/Content:**

        - **Alternative text:** Ensure alternative text is provided for information that is only conveyed through shape, size, or position
        - **Loading completion:** If loading content isn't rendered in place of the spinner, ensure the completion of the loading state is conveyed

        **Development:**

        - **Parent wrapper:** Wrap the loader in a parent element with `role="status"` and `aria-live="polite"`. The live region must be present in the DOM before the loading indicator has rendered
        - **Alternative text:** Provide visually hidden text as children to describe the loading state
        - **Loading completion:** If some loading content isn't rendered in place of the spinner, convey the completion of the loading state through a non-visible status message such as "loading complete"
        - **Optional ARIA attributes:** Consider using `aria-busy`, `aria-atomic`, or `aria-relevant` attributes to enhance the loading experience
        - **Override caution:** If overriding accessibility features, ensure compliance with the accessibility expectations described in the technical documentation

## Accessibility attributes

      The Loader component uses the following ARIA attributes to ensure proper screen reader support:

      - **`role="status"`**: Indicates that the loader is a status indicator that should be announced by assistive technologies
      - **`aria-live="polite"`**: Ensures screen readers announce updates when the loading state changes, without interrupting the user
      - **Visually hidden text**: Children content is visually hidden but accessible to screen readers to provide context about what is loading

      The live region must be present in the DOM **before** the loading indicator has rendered to ensure proper announcement by screen readers.

## Accessible label

      The Loader component accepts children that will be visually hidden but accessible to screen readers. This allows you to provide context about what is loading.

      **Best practices:**

      - Provide descriptive text that explains what is being loaded
      - Ensure the visible loader label contains the same text as the accessible name (WCAG 2.5.3 Label in Name)
      - Keep the description concise and informative

      **Example:**

      ```tsx
      import "@vtmn-play/css";
      import { VpLoader } from "@vtmn-play/react";

      export default function Page() {
        return (

            {isLoading ? Loading products... : }

        );
      }
      ```

      **With aria-busy:**

      ```tsx
      import "@vtmn-play/css";
      import { VpLoader } from "@vtmn-play/react";

      export default function Page() {
        return (

            {isLoading ? Loading... : children}

        );
      }
      ```

      **Loading completion announcement:**

      If the loaded content doesn't replace the loader, announce completion explicitly:

      ```tsx
      import "@vtmn-play/css";
      import { VpLoader } from "@vtmn-play/react";

      export default function Page() {
        return (

            {isLoading ? (
              Loading products...
            ) : (
              Loading complete
            )}

        );
      }
      ```

      **Optional aria-atomic:**

      Use `aria-atomic="true"` to indicate the entire region should be announced:

      ```tsx

          The current score is 23/0 after 5 Overs

      ```

      **Optional aria-relevant:**

      Use `aria-relevant` to specify which changes should be announced:

      ```tsx

        {/* use JavaScript to add and remove users here */}

      ```

## Loading button behavior

    When a button enters a loading state, it automatically becomes disabled and non-focusable to prevent user interaction during the loading process. This ensures users cannot trigger duplicate actions while an operation is in progress.

    **Key behaviors:**

    - **Disabled state:** The button is automatically disabled when loading begins
    - **Focus management:** The button loses focus and cannot receive focus while loading
    - **Automatic re-enabling:** Once loading completes, the button becomes enabled and focusable again
    - **Focus restoration:** Focus is restored to the button after loading completes, allowing keyboard users to continue their workflow

    This behavior prevents accidental duplicate submissions and provides a clear indication that an action is in progress.

## Design system guarantees

### ARIA and accessibility attributes

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| --- | --- | :---: |
| [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | Add corresponding `role` and `aria-live` roles to element wrapping the loading spinner or indicator. The live region must be present in the DOM **before the loading indicator has rendered**. | 👥 |
| [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | If some loading content isn't rendered in place of the spinner, the completion of the loading state should still be conveyed to assistive technologies. A non-visible status message such as "loading complete" could be put in the `aria-live` section or exposed through a specific `role`. | 👥 |
| [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | (Optional) The `aria-busy` state attribute may be used to indicate an element is being modified and that assistive technologies may want to wait until the changes are complete before informing the user about the update. | 👥 |
| [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | (Optional) The `aria-atomic` state attribute may be used to indicate to screen readers if they need to present all or only parts of the changed region based on the `aria-relevant` attribute. | 👥 |
| [7.5](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.5) | (Optional) The `aria-relevant` attribute may be used to indicate what notifications the user agent will trigger when a live region is modified. | 👥 |

### Visual accessibility

| **RGAA criterion** | **Requirement** | **Responsibilities** |
| --- | --- | :---: |
| [10.9](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.9) | Information cannot be conveyed solely through shape, size, or position; an alternative that is present and relevant must be provided. | ✅ / 👥 |
| [3.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.3) | Using Vitamin Play design tokens ensures sufficient contrast between the loader and its background. | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between the loader and its background, appropriate sizing for readability, and consistent spacing throughout your application.

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

## Testing and compliance

The Vitamin Play Loader component is tested with:

- Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
- Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide (APG): Status Role](https://www.w3.org/WAI/ARIA/apg/patterns/alert/#wai-aria-roles-states-and-properties)
- [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)
