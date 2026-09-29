# Vitamin Play accessibility guidance — tabs (web)

Source: vitamin-play-documentation/src/content/components-accessibility/tabs.mdx

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

        The Tabs component provides these built-in accessibility features
        out-of-the-box.

        - **Tab role:** Each tab element has `role="tab"` for proper screen reader identification.
        - **Tablist role:** The container for tabs has `role="tablist"` for proper structure.
        - **Tabpanel role:** Each content panel has `role="tabpanel"`.
        - **ARIA controls:** Each tab has `aria-controls` linking it to its associated panel.
        - **ARIA selected:** The active tab has `aria-selected="true"` while others have `aria-selected="false"`.
        - **ARIA labelledby:** Each tabpanel has `aria-labelledby` referring to its associated tab.
        - **Keyboard navigation:** Full keyboard support with arrow keys, Tab, Space, Enter, Home, and End keys.
        - **Focus management:** Focus moves correctly between tabs and into tab panels.

## What you need to do

        **Design/Content**

        - **Tab labels:** Provide clear, concise labels for each tab that describe the content in the associated panel.
        - **Content organization:** Structure tab panel content with proper heading hierarchy and semantic HTML.
        - **Icon accessibility:** If using icon-only tabs, ensure icons have clear meaning and provide accessible labels.

        **Development**

        - **Tablist labeling:** If the tab list has a visible label, set `aria-labelledby` on the tablist to reference it. Otherwise, provide an `aria-label`.
        - **Content structure:** Ensure tab panel content uses proper semantic HTML (headings, paragraphs, lists).
        - **Loading states:** Include appropriate `tabindex="0"` on tabpanels that don't contain focusable elements.
        - **Override caution:** If overriding accessibility features (e.g., adding custom `aria-*` attributes) or modifying behavior that could affect accessibility, ensure compliance with the expectations in this documentation.

## Accessibility attributes

      The Tabs component uses several ARIA attributes to ensure proper accessibility:

      - **`role="tablist"`**: Applied to the container element that holds all tabs.
      - **`role="tab"`**: Applied to each individual tab element within the tablist.
      - **`role="tabpanel"`**: Applied to each content panel associated with a tab.
      - **`aria-controls`**: Each tab element has this property referring to the ID of its associated tabpanel.
      - **`aria-selected`**: Set to `true` on the active tab and `false` on all other tabs.
      - **`aria-labelledby`**: Each tabpanel has this property referring to the ID of its associated tab element.

      **Screen reader announcement:**

      Screen readers announce the tab as "Tab, [label], [position] of [total]" and indicate whether it's selected. For example: "Tab 1, Selected, Tab, 1 of 3".

## Accessible label

  The tablist should have an accessible name provided through either `aria-labelledby` or `aria-label`.

      **Using `aria-labelledby` (recommended):**

      Reference the ID of a visible heading or label that describes the purpose of the tabs.

      ```tsx

        Discover all our product categories

          Women
          Men
          {/* ... */}

        {/* ... */}
        {/* ... */}

      ```

      **Icon-only tabs:**

      When using icon-only tabs, provide accessible text labels even when no visible text is present.

      **Important:** According to WCAG 2.5.3 Label in Name, the `aria-label` should match or contain any visible text if present.

## Keyboard behaviour

      The Tabs component supports the following keyboard interactions:

      | Key              | Action                                                                                               |
      | ---------------- | ---------------------------------------------------------------------------------------------------- |
      | `Tab`            | When focus moves into the tablist, places focus on the active tab. When the tablist contains focus, moves focus to the next element in the page (typically the tabpanel). |
      | `Left Arrow`     | Moves focus to the previous tab. If focus is on the first tab, moves focus to the last tab. Optionally activates the newly focused tab. |
      | `Right Arrow`    | Moves focus to the next tab. If focus is on the last tab, moves focus to the first tab. Optionally activates the newly focused tab. |
      | `Space` or `Enter` | Activates the focused tab if it was not activated automatically on focus. |
      | `Home`           | Moves focus to the first tab. Optionally activates the newly focused tab. |
      | `End`            | Moves focus to the last tab. Optionally activates the newly focused tab. |

## Manual vs Automatic activation

      Tabs can be configured with two activation modes:

      **Automatic activation (recommended):**

      The tab activates automatically when it receives focus via arrow keys. This is the default and recommended behavior when tab panels load quickly.

      **Manual activation:**

      The tab receives focus but is not activated until the user presses `Space` or `Enter`. This is recommended when:
      - Tab panel content takes time to load
      - Switching tabs has side effects (e.g., network requests)
      - Users need to navigate quickly through many tabs

      It is recommended that tabs activate automatically when they receive focus as long as their associated tab panels are displayed without noticeable latency.

## Design System guarantees

  ### ARIA and accessibility attributes

  | RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
  | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The element that serves as the container for the set of tabs has role `tablist`.                                                               |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | Each element that serves as a tab has role `tab` and is contained within the element with role `tablist`.                                      |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | Each element that contains the content panel for a `tab` has role `tabpanel`.                                                                  |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | If the tab list has a visible label, the element with role `tablist` has `aria-labelledby` set to a value that refers to the labelling element. Otherwise, the `tablist` element has a label provided by `aria-label`. |        👥        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | Each element with role `tab` has the property `aria-controls` referring to its associated `tabpanel` element.                                  |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | The active `tab` element has the state `aria-selected` set to `true` and all other `tab` elements have it set to `false`.                      |        ✅        |
  | [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1)             | Each element with role `tabpanel` has the property `aria-labelledby` referring to its associated `tab` element.                                |        ✅        |

  ### Keyboard interaction

  | RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
  | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
  | [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3)             | The component is operable by keyboard.                                                                                                         |        ✅        |

  ### Visual accessibility

  | RGAA criterion | Requirement                                                                                                                                    | Responsibilities |
  | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
  | [3.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.1)             | The item status (selected/not selected) is not only conveyed by color.                                                                                 |        ✅        |
  | [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2)             | Sufficient contrast between text and background.                                                                                               |        ✅        |
  | [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7)            | Focus is visible on all interactive elements (tabs).                                                                                           |        ✅        |

  Using Vitamin Play design tokens ensures sufficient contrast between tab labels and their background, appropriate sizing for readability, and consistent spacing throughout your application.

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

## Expected implementation details

  - When the tabpanel does not contain any focusable elements or the first element with content is not focusable, the tabpanel should set `tabindex="0"` to include it in the tab sequence of the page.
  - When the component is disabled (`disabled` prop set to `true`), items are neither interactive nor focusable. However, disabled interactive elements can serve as visual and contextual indicators. For specific composite widget elements like Tabs, you can keep them focusable even when disabled by setting the `isFocusable` prop to `true`: the `disabled` native attribute would be set to `false`, but an `aria-disabled` attribute would be set to `true`.
  - It is recommended that tabs activate automatically when they receive focus as long as their associated tab panels are displayed without noticeable latency. This typically requires tab panel content to be preloaded. Otherwise, automatic activation slows focus movement, which significantly hampers users' ability to navigate efficiently across the tab list.

## Testing and compliance

  The Vitamin Play Tabs component is tested with:

  - Deque Systems' [Axe Core](https://github.com/dequelabs/axe-core) accessibility testing engine
  - Compliance with [WCAG Level A & AA rules](https://www.w3.org/WAI/WCAG21/quickref/)
  - [ARIA Authoring Practices Guide (APG): Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
  - [RGAA - French Accessibility Guidelines](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Additional resources

  - [MDN Web Docs: `tab` role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)
  - [MDN Web Docs: `tablist` role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)
  - [MDN Web Docs: `tabpanel` role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tabpanel_role)
