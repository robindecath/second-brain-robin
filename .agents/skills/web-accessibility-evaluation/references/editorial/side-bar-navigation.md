# Vitamin Play accessibility guidance — side-bar-navigation (web)

Source: vitamin-play-documentation/src/content/components-accessibility/side-bar-navigation.mdx

## Responsibilities at a glance

## What the design system guarantees

				The Side Bar Navigation component provides these built-in accessibility features out-of-the-box.
				- **Navigation landmark:** Exposes the sidebar as a semantic `` landmark in page context
				- **Structured hierarchy:** Supports hierarchical parent and child navigation with semantic HTML (``, ``, links, buttons) to expose information architecture clearly
				- **Keyboard-operable interactions:** Expand/collapse actions and item activation can be fully operated with keyboard controls
				- **ARIA state sync:** Keeps `aria-expanded`, `aria-current`, and submenu relationships synchronized with visual state
				- **Visible states:** Active, hover, focus, and expanded/collapsed states are visually differentiated
				- **Focus management:** Preserves logical focus order and restores focus when closing submenus
				- **Design tokens:** Color, spacing, and typography tokens support readable, consistent navigation patterns

## What you need to do

				**Design / Content**
				- **Label clarity:** Use concise, descriptive labels for parent and child items
				- **Predictable organization:** Keep a clear and consistent structure for what content and submenus belong under each header
				- **Visible text alignment:** Ensure visible item labels match the spoken accessible names
				**Development**
				- **Landmark naming:** Provide an accessible name for the navigation region with `aria-label` or `aria-labelledby`
				- **Override caution:** Do not override built-in ARIA behavior and accessible names with unrelated custom attributes

## Accessibility attributes

			Side Bar Navigation provides a semantic navigation structure and predictable menu relationships out-of-the-box.

			- Uses a semantic `` region with list semantics (`` / ``) for navigation trees
			- Uses synchronized `aria-expanded`, `aria-controls`, and `aria-current="page"` states for expandable and active items
			- Supports APG-aligned keyboard interactions for nested navigation
			- In your implementation, provide a clear `aria-label` or `aria-labelledby` value so this navigation is distinguishable from other navigation landmarks

			Reference pattern: WAI-ARIA APG: Menubar Pattern

## Accessible label

					Use this section for naming only: apply accessible names to the navigation region and interactive items while keeping spoken names aligned with visible text.

					- **Navigation region name:** Add `aria-label="Main navigation"` (or `aria-labelledby`) on the sidebar ``
					- **Item naming consistency:** Keep visible labels and accessible names aligned for links and expandable triggers (WCAG 2.5.3 Label in Name)
					- **Avoid replacement labels:** Do not replace concise visible labels with unrelated custom accessible names

			```tsx

							Dashboard

							Catalog

								Products

								Stock

			```

## Keyboard behaviour

				| **Key** | **Action** |
				| --- | --- |
				| `Tab` | Moves focus into the sidebar navigation. From the last focusable item, moves focus out of the component. |
				| `Shift + Tab` | Moves focus to the previous focusable element, including leaving the sidebar backwards. |
				| `Down Arrow` | Moves focus to the next item in the same menu level. |
				| `Up Arrow` | Moves focus to the previous item in the same menu level. |
				| `Right Arrow` | Opens a submenu (when available) and moves focus to its first item. |
				| `Left Arrow` | Closes the current submenu and returns focus to its parent item. |
				| `Enter` or `Space` | Activates a link or toggles an expandable item. |
				| `Escape` | Closes the open submenu and returns focus to the controlling item. |
				| `Home` (Optional) | Moves focus to the first item in the current menu level. |
				| `End` (Optional) | Moves focus to the last item in the current menu level. |

## Design system guarantees

	| **RGAA criterion** | **Description** | **Responsibilities** |
	| --- | --- | :---: |
	| [3.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.1) [10.9](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.9)| Navigation state must not rely only on position, shape, or color; textual and semantic alternatives are required. | ✅ |
	| [3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#3.2) | Design tokens provide color combinations intended to maintain readable contrast for navigation content. | ✅ |
	| [7.1](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.1) | Navigation items support accessibility attributes such as `aria-expanded`, `aria-controls`, and `aria-current` when configured correctly. | ✅ / 👥 |
	| [7.3](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#7.3) | The component supports keyboard navigation patterns for item traversal, submenu open/close, and activation. | ✅ |
	| [9.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#9.2) | The sidebar must be exposed as a named navigation landmark so users can identify its purpose quickly. | ✅ |
	| [10.7](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/#10.7) | Focus visibility is ensured through design tokens and focus styles. | ✅ |

Using Vitamin Play design tokens ensures sufficient contrast between navigation elements and their background, appropriate sizing for readability, and consistent spacing throughout your application.

**Legend:**

- ✅ = Compliant (Design system guarantees)
- 👥 = User responsibility (Developer must implement)

## Screen readers restitution

	**Tested with:**

		| **Environment** | **React** | **Svelte** | **Vue** |
		| --- | :---: | :---: | :---: |
		| Firefox + NVDA |  |  |  |
		| IE + JAWS |  |  |  |
		| Safari + VoiceOver |  |  |  |
		| Android + TalkBack |  |  |  |
		| iOS + VoiceOver |  |  |  |

## Expected implementation details

	The Side Bar Navigation component already handles core accessibility mechanics such as focus flow, keyboard traversal, and ARIA state synchronization.

	- Add an accessible navigation name with `aria-label` or `aria-labelledby`
	- Keep content and submenu organization predictable under each header
	- Avoid overriding built-in ARIA behavior unless strictly necessary; if customized, re-validate WCAG A/AA conformance

## Testing and compliance

	The Vitamin Play Side Bar Navigation component is tested with:

	- Deque Systems' Axe Core accessibility testing engine
	- Compliance with WCAG Level A & AA rules
	- ARIA Authoring Practices Guide (APG): Menubar Pattern
	- RGAA - French Accessibility Guidelines
