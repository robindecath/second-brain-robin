# Vitamin Play accessibility contracts (web)

Per-component **consumer-side** requirements (what VP handles vs what you must do).
When auditing/reviewing/remediating/testing code that USES a `Vp*` component, load the
matching contract file and verify every consumer requirement is satisfied (accessible
name, associated label, keyboard, required indication, grouping, etc.). A `Vp*` component
used WITHOUT fulfilling its contract is a finding even though the component itself is correct.

## Components with a documented contract
- [`accordion`](accordion.md)
- [`article-card`](article-card.md)
- [`badge`](badge.md)
- [`bottom-sheet`](bottom-sheet.md)
- [`breadcrumbs`](breadcrumbs.md)
- [`button`](button.md)
- [`checkbox`](checkbox.md)
- [`chip`](chip.md)
- [`combobox`](combobox.md)
- [`date-picker`](date-picker.md)
- [`divider`](divider.md)
- [`footer`](footer.md)
- [`icon-button`](icon-button.md)
- [`link`](link.md)
- [`link-list`](link-list.md)
- [`loader`](loader.md)
- [`modal`](modal.md)
- [`navigation-header`](navigation-header.md)
- [`price`](price.md)
- [`product-card`](product-card.md)
- [`progress-bar`](progress-bar.md)
- [`quantity-input`](quantity-input.md)
- [`radio`](radio.md)
- [`score-rating`](score-rating.md)
- [`search`](search.md)
- [`select`](select.md)
- [`side-bar-navigation`](side-bar-navigation.md)
- [`side-sheet`](side-sheet.md)
- [`skeleton`](skeleton.md)
- [`snackbar`](snackbar.md)
- [`star-rating`](star-rating.md)
- [`sticker`](sticker.md)
- [`table`](table.md)
- [`tabs`](tabs.md)
- [`text-input`](text-input.md)
- [`textarea`](textarea.md)
- [`toggle`](toggle.md)

See also `_foundations-accessibility.md` (design-system accessibility foundations).
