---
name: google-workspace
description: >
  Read and write Google Workspace data (Drive, Docs, Sheets, Slides, Gmail, Calendar)
  through the gws CLI. Use whenever the user mentions a Google Drive file or folder, a
  Google Doc, Google Sheet, Google Slides deck, a Gmail message or thread, or a Google
  Calendar event — including when they only paste a docs.google.com, drive.google.com
  or calendar.google.com link. Never guess the content of a Google resource and never
  ask the user to copy/paste it — fetch it with gws.
license: Proprietary
metadata:
  audience: all
  domain: productivity
  api: cli
  mcp_required: false
  owner: Decathlon AI Augmented SDLC
  version: "2.0.0"
  last-updated: "2026-07-30"
---

# Google Workspace (`gws`)

`gws` is the single CLI for every Google Workspace API. It is the only supported
way to read or write Google Workspace data at Decathlon.

**Never invent the content of a Google resource, and never ask the user to
copy/paste it: fetch it.**

## When to use this skill

As soon as a request involves any of these — including when the user only pastes a link:

| Signal | Service |
|---|---|
| Drive file/folder, `drive.google.com/…` | Drive |
| Google Doc, `docs.google.com/document/…` | Docs |
| Google Sheet, `docs.google.com/spreadsheets/…` | Sheets |
| Google Slides, `docs.google.com/presentation/…` | Slides |
| Gmail message/thread/label, "my inbox" | Gmail |
| Calendar event, availability, "my agenda" | Calendar |
| Google Chat message, "post to the space", `chat.google.com/…` | Chat (write via `+send` only — see RECIPES.md) |
| To-do / task list, "add a task", "my tasks" | Tasks |
| Contact, address book, "look someone up in the directory" | People/Contacts |
| Google Form, survey, quiz, "form responses", `forms.google.com/…`, `docs.google.com/forms/…` | Forms |
| Meet space/link, meeting recording or transcript, `meet.google.com/…` | Meet |

## Preflight

```bash
scripts/gws-auth-hint.sh   # "gws: ready (you@decathlon.com)", or the exact fix
```

It wraps `gws auth status` and, when something is wrong, tells you *which*
thing — missing binary, missing OAuth client, or missing login — with the
command to fix it. The other scripts call it automatically on failure, so you
usually just relay their output.

- `gws: command not found` → not installed: `npm install -g @googleworkspace/cli`,
  then sign in below.
- `token_valid` is not `true`, or a call fails with `401` / "not authenticated"
  → not signed in. Sign in below.
- A `403` on one service only → the token predates a scope. The same login
  re-consents with the full set.

**Never run `gws auth login` yourself.** It prints a consent URL and then blocks
on its localhost listener until a human approves in a browser — it would hang
your turn. Instead, get the exact login command from the auth-hint script (it is
the single source of truth for the scope list) and give that to the user, then
stop:

```bash
scripts/gws-auth-hint.sh   # prints the full `gws auth login --scopes …` line to relay
```

Tell them what to expect, because the CLI **does not open a browser itself**:

> It prints a `https://accounts.google.com/…` URL and waits. Open that URL in
> your browser, sign in with your Decathlon account and approve the permissions
> — the command finishes on its own once you do.

Pass the scopes exactly as the script prints them: a bare `gws auth login` opens
an interactive scope picker and grants a narrower set, which then fails at call
time. Do **not** use `--readonly` (breaks writes) or `--full` (asks for far more
than we need).

It needs `client_secret.json` in the gws config directory (`~/.config/gws/`, or
`~/Library/Application Support/gws/` on older macOS setups). The platform
installer writes it; if it is missing, re-run the installer.

Once the user confirms they are signed in, re-run `gws auth status` and carry on.

Granted scopes: Drive, Sheets, Docs, Slides, `gmail.modify` +
`gmail.settings.basic`, Calendar, Tasks,
Contacts/People (+ directory), Chat (spaces, messages, reactions,
memberships), Forms (`forms.body` + responses read) and Meet
(`meetings.space.created` + readonly) — read
**and** write. (Google Keep is intentionally excluded — its restricted
`keep` scope is not registered on the OAuth consent screen and requesting
it blocks the whole sign-in.)

---

## Read documents with the scripts, not the raw API

This is the single most important rule in this skill. The document APIs return
the full structural tree of a file — every shape, every style run, every
element ID. On a real 47-slide deck, `slides presentations get` returns
**15.8 MB of JSON (~4 million tokens)**. The same deck exported as text is
**25 KB (~4.6k tokens)** — a **625×** difference for the same information.

### `scripts/gws-fetch.sh <url-or-id>` — any file as cheap text

Resolves the URL, picks the cheapest export format for that file type, writes it
to a file, and prints **only a summary** — never the content.

```bash
scripts/gws-fetch.sh "https://docs.google.com/document/d/<ID>/edit"
```
```
title:    Q3 Product Brief
kind:     document
modified: 2026-07-29T14:05:08.401Z
exported: text/markdown
path:     /var/folders/.../gws-fetch/<ID>.md
size:     18422 bytes · 402 lines · 2810 words (~3746 tokens)
```

Then **read the file selectively** — `grep` for what you need, or view a line
range. Do not `cat` a large file into context.

| File type | Exported as | Note |
|---|---|---|
| Google Doc | `text/markdown` | Headings, lists and tables preserved |
| Google Slides | `text/plain` | Whole-deck reading only — **no slide boundaries**, see below |
| Google Sheet | `text/csv` | **First sheet only** — see below for other tabs |
| Anything else | raw bytes | Download, then convert locally |

Options: `-o <path>` to choose the destination, `--mime <mime>` to force a
format, `--print` to also echo the content (small files only).

### `scripts/gws-slide-text.sh <url-or-id> <n>` — one slide's text

**The Drive text export of a deck has no slide delimiters at all**, so it can
never answer "what is on slide 6?". Use this script for anything slide-scoped.
It fetches a single page with a text-only field mask (~4 KB) and prints ~1 KB.

```bash
scripts/gws-slide-text.sh "https://docs.google.com/presentation/d/<ID>/edit" 6
scripts/gws-slide-text.sh <ID> --outline   # every slide: number, id, first line
```
```
slide:  6 of 47 (objectId g3c895a8aafd_3_0) — Organization Chart
---
Digital Organization - Macro view
Our Digital Organization is structured into four layers: …
```

`--outline` is one API call for the whole deck (~2 KB for 47 slides) — use it to
locate the right slide before reading it.

### `scripts/gws-slide-png.sh <url-or-id> <n>` — render a slide as an image

Text extraction loses diagrams, arrows and org charts. Render the slide and look
at the image.

```bash
scripts/gws-slide-png.sh "https://docs.google.com/presentation/d/<ID>/edit" 6
scripts/gws-slide-png.sh <ID> --list      # slide number → objectId
```
```
slide:    6 of 47 (objectId g3c895a8aafd_3_0)
path:     /var/folders/.../gws-fetch/<ID>-slide-06.png
size:     1600x900 px · 257980 bytes
```

Use `--size SMALL|MEDIUM|LARGE` (default `LARGE`, 1600 px). Prefer `MEDIUM` when
you only need the layout.

### Which one for a presentation?

| Question | Command |
|---|---|
| "Summarise this deck" | `gws-fetch.sh <url>` then grep the export |
| "What is on slide 6?" | `gws-slide-text.sh <url> 6` |
| "Where is X in this deck?" | `gws-slide-text.sh <url> --outline` |
| "Show me slide 6" / it's a diagram | `gws-slide-png.sh <url> 6` |

When the user asks *both* what a slide says and to see it, run the text and the
PNG script — together they cost ~2 KB plus one image.

---

## Token discipline for direct API calls

When you do call the API directly, four levers keep responses small:

1. **`fields` mask — always.** Google returns everything by default.
   ```bash
   # 15.8 MB  →  2.5 KB
   gws slides presentations get --params '{"presentationId":"<ID>","fields":"title,slides.objectId"}'
   gws drive files list --params '{"q":"...","pageSize":20,"fields":"files(id,name,mimeType,modifiedTime)"}'
   ```
2. **`--format csv` or `--format table`** instead of the default JSON envelope,
   especially for Sheets ranges and list results.
3. **Cap the page size.** `"pageSize"` / `"maxResults"` on every list call.
   Use `--page-all` only when the user explicitly asked for an exhaustive list,
   and always with `--page-limit`.
4. **Two-step reads.** List IDs first (cheap), then fetch only the items you
   need. For Gmail use `"format": "metadata"` for triage and `"full"` only on
   the messages that matter.

Redirect anything large to a file with `-o` and grep it, rather than letting it
land in the transcript. `gws` refuses `-o` paths outside the current working
directory — `cd` into the destination first (both bundled scripts already do).

## Sheets: reading a specific tab

`gws-fetch.sh` exports the first sheet only. For any other tab:

```bash
gws sheets spreadsheets get --params '{"spreadsheetId":"<ID>","fields":"sheets.properties.title"}'
gws sheets spreadsheets values get --format csv \
  --params '{"spreadsheetId":"<ID>","range":"Roadmap!A1:H200"}'
```

## Creating a new Doc — always from a Decathlon template

**Never create a blank document with `docs documents create`.** Every new
Google Doc must start from one of the Decathlon corporate A4 templates so it
inherits the brand cover, heading styles, colours and page setup. Create it by
**copying the template file** with the Drive API.

### Pick the most relevant template

Choose the template that best matches what the user is writing — describe the
request to yourself and match it against the intent column:

| Template | File ID | Use it for |
|---|---|---|
| **GDoc A4 Template** | `14qLJMmAVhmoVDah_kEjg1XTkRnUZDZ3v8zst7kKAtKg` | The neutral, general-purpose doc. Title / subtitle / date cover, then numbered `#` sections with body paragraphs and simple tables. Default choice for briefs, notes, specs, reports — anything without a more specific structure. |
| **GDoc A4 Template with Image** | `1fnCEo1v20RIfE0FFoTjXM8SQasrzVt_rS5tFFjsCRgc` | A richer narrative doc that opens with a **hero cover image**, an Introduction, then numbered sections each broken into `##` sub-sections with bullet lists. Reach for it when the content is a story/guide/announcement that benefits from a visual header and lots of nested headings. |
| **GDoc A4 Template Responsibility Framework** | `14EcIr8CrI9qqrPVOaWnLtNSxlQJB2LK20ZuJvjSv9qE` | The governance / RACI document. Pre-built sections for **Target, Purpose (goal + OKR/KPIs), Context, Risks (financial/legal/operational/reputational), Types of guarantees, Players, a RACI responsibilities table, Controls, Lexicon, Contacts and a document history log**. Use it only for responsibility frameworks, ownership/accountability or process-governance docs. |

When unsure, default to **GDoc A4 Template**. Only build a blank doc if the user
*explicitly* asks for an unbranded, empty document.

### Copy the chosen template

```bash
# Copy the selected Decathlon A4 template (swap in the File ID from the table).
# The templates live in a shared drive, so BOTH flags are required:
#   supportsAllDrives:true → without it the copy fails with 404
#   parents:["root"]       → lands the copy in the user's My Drive, which they
#                            OWN and can edit/delete; omitting it creates the
#                            copy inside the shared drive, where the user has no
#                            permission to edit or remove it.
gws drive files copy \
  --params '{"fileId":"14qLJMmAVhmoVDah_kEjg1XTkRnUZDZ3v8zst7kKAtKg","supportsAllDrives":true}' \
  --json  '{"name":"<new document title>","parents":["root"]}'
```

The response contains the new document's `id`; open it at
`https://docs.google.com/document/d/<id>/edit`. Then fill it in with
`gws docs +write` / `gws docs documents batchUpdate` as usual, replacing the
placeholder text (`Title`, `Please write here…`, the *lorem ipsum* filler) with
the real content while keeping the template's heading structure and styles.

Read the fresh copy first with `scripts/gws-fetch.sh` so you can see exactly
which placeholders to replace before editing.

### Filling the copy — `replaceAllText`, not delete-then-insert

**Prefer `replaceAllText` on the template's placeholder strings.** It swaps the
text in place, so every paragraph keeps the style the template gave it. This is
the only editing pattern that is safe by default:

```bash
gws docs documents batchUpdate --params '{"documentId":"<ID>"}' --json '{"requests":[
  {"replaceAllText":{"containsText":{"text":"Title","matchCase":true},"replaceText":"What is Decathlon?"}},
  {"replaceAllText":{"containsText":{"text":"Please write here…","matchCase":true},"replaceText":"<real body text>"}}
]}'
```

**The trap: `deleteContentRange` does not delete formatting.** Wiping the body
(`deleteContentRange` from index 1 to the end, then `insertText` at index 1) is
tempting when the template has far more sections than you need — but Docs keeps
the *character-level* `textStyle` of whatever used to sit at that index, and the
text you insert silently inherits it. Delete a 30 pt Title placeholder and your
new body paragraph comes out at 30 pt semibold, even though its
`paragraphStyle.namedStyleType` still reads `NORMAL_TEXT` — the named style is
correct, the direct formatting on top of it is not.

So **whenever you insert text into a range you just cleared, reset the style of
the inserted range in the same `batchUpdate`**:

```bash
gws docs documents batchUpdate --params '{"documentId":"<ID>"}' --json '{"requests":[
  {"insertText":{"location":{"index":1},"text":"<real body text>"}},
  {"updateParagraphStyle":{"range":{"startIndex":1,"endIndex":<1+len>},
    "paragraphStyle":{"namedStyleType":"NORMAL_TEXT"},"fields":"namedStyleType"}},
  {"updateTextStyle":{"range":{"startIndex":1,"endIndex":<1+len>},"textStyle":{},
    "fields":"fontSize,weightedFontFamily,bold,italic,underline,foregroundColor,backgroundColor"}}
]}'
```

An **empty `textStyle` with an explicit `fields` mask clears** those properties
back to whatever the named style defines — that is the reset. Do *not* hardcode
`11 PT` / `Arial`: read the template's own definition instead, since each
template sets its own body font.

```bash
gws docs documents get --params '{"documentId":"<ID>","fields":"namedStyles.styles(namedStyleType,textStyle)"}'
```

Verify after writing — an export shows the text but not its size, so check the
styles are actually clean:

```bash
gws docs documents get --params '{"documentId":"<ID>","fields":"body.content(paragraph(paragraphStyle(namedStyleType),elements(textRun(textStyle))))"}'
```

Empty `textStyle: {}` objects mean no leftover direct formatting — the paragraph
renders exactly as the template intends.

## Creating a new Slides deck — always from the Decathlon template

**Never create a blank deck with `slides presentations create`.** Every new
Google Slides presentation must start from the Decathlon corporate template so it
inherits the brand theme, layouts and master slides. Create it by **copying the
template file** with the Drive API:

```bash
# Decathlon corporate Slides template: "_00_INTERNAL SLIDE_TEMPLATE_2024"
gws drive files copy \
  --params '{"fileId":"1MHICaPgiKoImRFn0xyfybDNh57bcF0lTavWeW5skerY"}' \
  --json  '{"name":"<new deck title>"}'
```

The response contains the new presentation's `id`; open it at
`https://docs.google.com/presentation/d/<id>/edit`. Then apply edits with
`slides presentations batchUpdate` as usual.

Only fall back to `gws slides presentations create` if the user *explicitly*
asks for a blank, unbranded deck.

### Never delete the template slides — hide them instead

The copied template ships with a rich set of example/layout slides (title,
agenda, section dividers, content patterns, charts, closing…). Once you have
generated the deck's actual content, **do not delete these template slides with
`deleteObject`.** Deleting them throws away the reference material you (and the
user) need when iterating later — re-styling a slide, adding a section, or
picking a layout that matches the brand.

Instead, **hide them** by marking each template slide as *skipped* — they stay
in the file, out of the presented deck, and remain available to copy from on the
next iteration:

```bash
# Hide (skip) a leftover template slide instead of deleting it
gws slides presentations batchUpdate --params '{"presentationId": "<ID>"}' \
  --json '{"requests":[{"updateSlideProperties":{"objectId":"<SLIDE_ID>","slideProperties":{"isSkipped":true},"fields":"isSkipped"}}]}'
```

Batch every template slide into a single `batchUpdate` call. To reveal one again
while iterating, send the same request with `"isSkipped":false`. Only use
`deleteObject` on a template slide when the user *explicitly* asks to permanently
remove it.

### Insert new slides from the template's named layouts

The template also carries the **named layouts** shown in the Slides UI under the
little ▾ next to the *+ New slide* button — `blanc + logo`, `BLANK_4`,
`BLUE PAGE 1`, `CHAPTER 1`…`CHAPTER 4`, `COVER BLUE`, `COVER WHITE`,
`EMPTY BLUE/GREY/WHITE`, `HIGHLIGHT01`…`HIGHLIGHT04`, etc. These are the branded
building blocks — **use them instead of building slides from scratch or from a
bare `BLANK` layout.**

Each entry in that menu is a layout in the deck with a `displayName`. List them
first, then create the slide against the matching `layoutId`:

```bash
# 1. List the template's named layouts (== the entries in the "+ ▾" menu)
gws slides presentations get --params '{"presentationId":"<ID>","fields":"layouts(objectId,layoutProperties.displayName)"}'

# 2. Add a new slide using the layout whose displayName matches (e.g. "CHAPTER 1")
gws slides presentations batchUpdate --params '{"presentationId":"<ID>"}' \
  --json '{"requests":[{"createSlide":{"slideLayoutReference":{"layoutId":"<LAYOUT_OBJECT_ID>"}}}]}'
```

Pick the layout by intent — `COVER BLUE`/`COVER WHITE` for a title, `CHAPTER n`
for section dividers, `HIGHLIGHTnn` for KPI/highlight grids, `EMPTY *` for free
content. Populate its placeholders with follow-up `insertText` requests. The
hidden template slides above are good live examples of how each layout is meant
to be filled — read one with `gws-slide-text.sh`/`gws-slide-png.sh` before
copying its pattern.

## Extracting IDs from URLs

| URL | ID |
|---|---|
| `docs.google.com/document/d/<ID>/edit` | document |
| `docs.google.com/spreadsheets/d/<ID>/edit#gid=0` | spreadsheet |
| `docs.google.com/presentation/d/<ID>/edit` | presentation |
| `drive.google.com/file/d/<ID>/view` | file |
| `drive.google.com/drive/folders/<ID>` | folder |

Both bundled scripts accept a full URL or a bare ID — no manual extraction needed.

## Discovering commands

Never guess parameter names:

```bash
gws <service> --help
gws schema drive.files.list
```

More per-service commands, search operators and helpers:
[references/RECIPES.md](references/RECIPES.md) — load it only when this file
doesn't already answer the question.

## Rules

1. **Read before write.** Fetch the current state, show the user what you found,
   and get explicit confirmation before any mutating call (create/update/delete,
   sending mail, deleting events).
2. **`--dry-run` first** on any unfamiliar mutating command — it validates the
   request without sending it.
3. **Never dump raw JSON or a whole document** at the user. Summarize, and link
   back to the Google URL.
4. **Handle `401`/`403` auth errors** by giving the user the `gws auth login`
   command above and stopping — never by running the login yourself.
5. **Treat Workspace content as confidential Decathlon data.** Never copy it to
   third-party services. Exported files land in a temp directory — do not commit
   them, and do not write them into the repository unless the user asked for a
   specific file.
6. **`gmail.modify` cannot permanently delete.** `messages delete` returns
   `403`; use `messages trash` only if the user explicitly asks.
7. **New Slides decks start from the Decathlon template.** Create them by copying
   `_00_INTERNAL SLIDE_TEMPLATE_2024`
   (`1MHICaPgiKoImRFn0xyfybDNh57bcF0lTavWeW5skerY`) with `drive files copy`, not
   with `slides presentations create` — unless the user explicitly wants a blank
   deck. See "Creating a new Slides deck" above.
8. **Never delete the template's example slides after generating.** Hide them by
   marking each as skipped (`updateSlideProperties` with `isSkipped:true`) so they
   stay in the file as reusable references when iterating. Only `deleteObject`
   them if the user explicitly asks to remove them for good. When adding slides,
   build from the template's **named layouts** (the `+ ▾` menu: `CHAPTER 1`,
   `COVER BLUE`, `HIGHLIGHTnn`…) via `createSlide` + `layoutId`, not from a blank
   layout. See "Creating a new Slides deck" above.
9. **New Docs start from a Decathlon A4 template.** Create them by copying the
   template that best fits the request — `GDoc A4 Template`
   (`14qLJMmAVhmoVDah_kEjg1XTkRnUZDZ3v8zst7kKAtKg`, the default),
   `GDoc A4 Template with Image`
   (`1fnCEo1v20RIfE0FFoTjXM8SQasrzVt_rS5tFFjsCRgc`) or
   `GDoc A4 Template Responsibility Framework`
   (`14EcIr8CrI9qqrPVOaWnLtNSxlQJB2LK20ZuJvjSv9qE`) — with `drive files copy`
   (`supportsAllDrives:true` + `parents:["root"]`, or the copy 404s / lands in a
   shared drive the user can't edit), not with `docs documents create`, unless
   the user explicitly wants a blank doc. See "Creating a new Doc" above.
10. **Fill a copied Doc with `replaceAllText`, and reset the style whenever you
    insert into a cleared range.** `deleteContentRange` removes text but keeps
    the *character-level* formatting that was at that index, so text you
    `insertText` there silently inherits it (a deleted 30 pt Title leaves your
    body paragraph at 30 pt, even though `namedStyleType` still reads
    `NORMAL_TEXT`). Follow every such `insertText` with `updateParagraphStyle`
    (`namedStyleType`) **and** `updateTextStyle` with an empty `textStyle` plus
    an explicit `fields` mask to clear the leftover direct formatting, then
    verify with a `paragraph(paragraphStyle,elements.textRun.textStyle)` field
    mask. See "Filling the copy" above.
