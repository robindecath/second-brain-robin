# `gws` recipes — per-service reference

Load this only when `SKILL.md` doesn't already answer the question.

Every command below assumes `gws` is on `$PATH` and authenticated — check with
`scripts/gws-auth-hint.sh`. If it is not, that script prints the fix, including
the exact `gws auth login --scopes …` command to hand to the user (it holds the
canonical scope list — never paste it here). Give it to the user to run — never
run it yourself, it prints a consent URL and then waits for a human to open it
in a browser and approve.

## Discovering an API before calling it

Never guess parameter names — the CLI mirrors the Google Discovery documents:

```bash
gws <service> --help                    # resources + methods for a service
gws schema <service>.<resource>.<method>  # required params, types, defaults
gws schema drive.files.list --resolve-refs
```

Two mistakes that waste calls across every service:

- **Respect the full resource path.** Methods live under their resource tree,
  e.g. `gws gmail users messages list`, not `gws gmail messages list`. When a
  subcommand is "unrecognized", run `gws <service> --help` and walk the tree.
- **Typed params must keep their JSON type.** Arrays stay arrays
  (`"labelIds": ["INBOX"]`, not `"INBOX"`) and numbers stay numbers. A
  string where the API wants a list is usually ignored silently and returns an
  empty result that looks like "no data" but is really a bad query. Check types
  with `gws schema <service>.<resource>.<method>`.
- **Writes split URL params from the body.** For create/insert/update/patch
  methods, `--params` carries only the URL/path/query params (e.g.
  `{"tasklist": "@default"}`) while the resource body goes in `--json` (e.g.
  `{"title": "..."}`). Putting body fields in `--params` is silently dropped —
  the call succeeds but the object comes back empty (e.g. a task with no title).

## Global flags worth knowing

| Flag | Use |
|---|---|
| `--params '{...}'` | URL / query parameters |
| `--json '{...}'` | Request body (POST/PATCH/PUT) |
| `--format json\|table\|yaml\|csv` | `csv` and `table` are far cheaper than `json` |
| `--dry-run` | Validate locally without calling the API |
| `-o <path>` | Write binary/exported responses to a file (**must be inside the CWD**) |
| `--upload <path>` | Upload file content (multipart) |
| `--page-all` | Auto-paginate as NDJSON — expensive, use `--page-limit` |

## Drive

```bash
# Search — always cap pageSize and mask fields
gws drive files list --params '{
  "q": "name contains \"roadmap\" and trashed = false",
  "pageSize": 20,
  "fields": "files(id,name,mimeType,modifiedTime,webViewLink)"
}'

# Files in a folder
gws drive files list --params '{"q": "\"<FOLDER_ID>\" in parents and trashed = false", "pageSize": 50, "fields": "files(id,name,mimeType)"}'

# Metadata only
gws drive files get --params '{"fileId": "<ID>", "fields": "name,mimeType,owners,modifiedTime,webViewLink"}'

# Shared drives are excluded by default
gws drive files list --params '{"q": "...", "supportsAllDrives": true, "includeItemsFromAllDrives": true}'
```

Useful `q` operators: `name contains`, `fullText contains`, `mimeType =`,
`'<id>' in parents`, `modifiedTime > '2026-01-01T00:00:00'`, `trashed = false`,
`sharedWithMe`, `starred`.

## Docs

```bash
# Read → prefer scripts/gws-fetch.sh (Markdown export, ~100x cheaper)
scripts/gws-fetch.sh <url>

# Structural read (only when you need styles, headings, tabs, comments)
gws docs documents get --params '{"documentId": "<ID>", "fields": "title,body.content.paragraph.elements.textRun.content"}'

# Create — ALWAYS from a Decathlon A4 template (copy, don't create blank).
# Pick the template that fits the request:
#   14qLJMmAVhmoVDah_kEjg1XTkRnUZDZ3v8zst7kKAtKg  GDoc A4 Template (neutral, default)
#   1fnCEo1v20RIfE0FFoTjXM8SQasrzVt_rS5tFFjsCRgc  GDoc A4 Template with Image (hero cover + intro)
#   14EcIr8CrI9qqrPVOaWnLtNSxlQJB2LK20ZuJvjSv9qE  GDoc A4 Template Responsibility Framework (RACI/governance)
gws drive files copy \
  --params '{"fileId": "14qLJMmAVhmoVDah_kEjg1XTkRnUZDZ3v8zst7kKAtKg", "supportsAllDrives": true}' \
  --json  '{"name": "Sprint 42 review", "parents": ["root"]}'
# supportsAllDrives:true is REQUIRED (templates live in a shared drive → 404 without it).
# parents:["root"] drops the copy in the user's My Drive so they own/can edit it;
# omit it and the copy stays in the shared drive where the user can't edit/delete it.
# → returns the new document id; fill it in with docs +write / batchUpdate below.
# Only create a blank doc if the user explicitly asks for one:
#   gws docs documents create --json '{"title": "Sprint 42 review"}'

# Append text (helper)
gws docs +write --document <ID> --text "## Findings"

# Fill a copied template — PREFER replaceAllText: it swaps text in place and
# every paragraph keeps the style the template gave it.
gws docs documents batchUpdate --params '{"documentId": "<ID>"}' \
  --json '{"requests": [
    {"replaceAllText": {"containsText": {"text": "Title", "matchCase": true}, "replaceText": "Sprint 42 review"}}
  ]}'

# Structured edit — deleteContentRange does NOT delete formatting. The surviving
# paragraph keeps the character style of whatever was at that index, so text you
# insert there inherits it (delete a 30 pt Title → your body text comes out at
# 30 pt, while namedStyleType still reads NORMAL_TEXT). Always reset the
# inserted range in the SAME batch:
gws docs documents batchUpdate --params '{"documentId": "<ID>"}' \
  --json '{"requests": [
    {"insertText": {"location": {"index": 1}, "text": "Hello\n"}},
    {"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": 7},
      "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}},
    {"updateTextStyle": {"range": {"startIndex": 1, "endIndex": 7}, "textStyle": {},
      "fields": "fontSize,weightedFontFamily,bold,italic,underline,foregroundColor,backgroundColor"}}
  ]}'
# An empty textStyle + explicit fields mask CLEARS those properties back to the
# named style — that is the reset. Don't hardcode a font size; read the
# template's own body style, then verify nothing direct is left over:
gws docs documents get --params '{"documentId": "<ID>", "fields": "namedStyles.styles(namedStyleType,textStyle)"}'
gws docs documents get --params '{"documentId": "<ID>", "fields": "body.content(paragraph(paragraphStyle(namedStyleType),elements(textRun(textStyle))))"}'
# Empty "textStyle": {} in the output == clean, renders as the template intends.
```

## Sheets

Quick ergonomic helpers: `gws sheets +read --spreadsheet <ID> --range "Tab!A1:D10"`
and `gws sheets +append --spreadsheet <ID> --values 'a,b,c'` (or `--json-values
'[["a","b"],["c","d"]]'`). Drop to the raw `values` API below for CSV output,
tab discovery, or precise range overwrites.

```bash
# Read a range as CSV — much cheaper than the default JSON envelope
gws sheets spreadsheets values get --format csv \
  --params '{"spreadsheetId": "<ID>", "range": "Backlog!A1:H200"}'

# List the tabs before guessing a range
gws sheets spreadsheets get --params '{"spreadsheetId": "<ID>", "fields": "sheets.properties(title,gridProperties)"}'

# Append rows
gws sheets spreadsheets values append \
  --params '{"spreadsheetId": "<ID>", "range": "Backlog!A1", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["Story", "Status"], ["Checkout v2", "Done"]]}'

# Overwrite a range
gws sheets spreadsheets values update \
  --params '{"spreadsheetId": "<ID>", "range": "Backlog!B2", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["In review"]]}'
```

> **Shell gotcha:** a range like `Backlog!A1` contains `!`, which zsh expands as
> history. Inside the single-quoted JSON above it is safe; never put a bare
> `Sheet1!A1` in double quotes in an interactive zsh.

## Slides

```bash
# Whole deck as text  → scripts/gws-fetch.sh <url>          (no slide boundaries!)
# One slide's text     → scripts/gws-slide-text.sh <url> <n>
# Deck outline         → scripts/gws-slide-text.sh <url> --outline
# One slide as an image→ scripts/gws-slide-png.sh <url> <n>

# Slide inventory without the multi-MB payload
gws slides presentations get --params '{"presentationId": "<ID>", "fields": "title,slides.objectId"}'

# Text of one slide, raw (what gws-slide-text.sh wraps)
gws slides presentations pages get --params '{"presentationId": "<ID>", "pageObjectId": "<SLIDE_ID>", "fields": "pageElements(shape(text(textElements(textRun(content)))))"}'

# Speaker notes for one slide
gws slides presentations pages get --params '{"presentationId": "<ID>", "pageObjectId": "<SLIDE_ID>", "fields": "slideProperties.notesPage"}'

# Create a deck — ALWAYS from the Decathlon template (copy, don't create blank)
gws drive files copy \
  --params '{"fileId": "1MHICaPgiKoImRFn0xyfybDNh57bcF0lTavWeW5skerY"}' \
  --json  '{"name": "Quarterly review"}'
# → returns the new presentation id; edit it with slides presentations batchUpdate.
# Only create a blank deck if the user explicitly asks for one:
#   gws slides presentations create --json '{"title": "Quarterly review"}'

# After generating content, HIDE leftover template slides — never delete them.
# Skipping keeps them in the file as reusable references for the next iteration.
gws slides presentations batchUpdate --params '{"presentationId": "<ID>"}' \
  --json '{"requests":[{"updateSlideProperties":{"objectId":"<SLIDE_ID>","slideProperties":{"isSkipped":true},"fields":"isSkipped"}}]}'
# Un-hide one while iterating with the same request and "isSkipped":false.

# Add a new slide from one of the template's NAMED layouts (the "+ ▾" menu:
# CHAPTER 1, COVER BLUE, HIGHLIGHT01, EMPTY GREY…). List them, then reference the id.
gws slides presentations get --params '{"presentationId":"<ID>","fields":"layouts(objectId,layoutProperties.displayName)"}'
gws slides presentations batchUpdate --params '{"presentationId":"<ID>"}' \
  --json '{"requests":[{"createSlide":{"slideLayoutReference":{"layoutId":"<LAYOUT_OBJECT_ID>"}}}]}'
```

> A full `slides presentations get` on a 47-slide deck returns **~16 MB** of
> JSON. Always use a `fields` mask, or export instead.
>
> The Drive `text/plain` export of a presentation contains **no slide
> delimiters**, so it cannot answer "what is on slide N?" — use
> `gws-slide-text.sh` for anything slide-scoped.
>
> Slides splits one paragraph into several styled `textRun`s, sometimes
> mid-word, so concatenate the runs before splitting on their newlines.
> Both bundled scripts already do this.

## Gmail

For **sending, replying, forwarding and quick triage, prefer the `+` helpers**.
They assemble RFC 5322 / MIME / base64 and handle threading, quoting and
attachments for you, so you never hand-build a raw message (the #1 source of
Gmail mistakes). All accept `--dry-run`; the write ones also take `--draft`.

| Helper | Use for |
|--------|---------|
| `gws gmail +triage [--max N] [--query 'is:unread'] [--labels]` | Unread/inbox summary (sender, subject, date) |
| `gws gmail +read --id <MSG_ID> [--headers] [--html]` | Read one message body/headers |
| `gws gmail +send --to a@x --subject S --body B [--html] [--cc] [-a file] [--draft]` | Send a new email |
| `gws gmail +reply --message-id <ID> --body B [-a file]` | Reply (auto threading + quote) |
| `gws gmail +reply-all --message-id <ID> --body B [--remove x@y]` | Reply-all |
| `gws gmail +forward --message-id <ID> --to d@x [--body note] [--no-original-attachments]` | Forward (keeps original attachments by default) |
| `gws gmail +watch --project <GCP> [--once] [--label-ids INBOX]` | Stream new mail as NDJSON (watch expires after 7 days) |

Confirm with the user before any send. Attachments cap at 25MB; with `--html`
use fragment tags (`<p>`, `<b>`, `<a>`) — no `<html>`/`<body>` wrapper.

Drop to the raw **`users`** API for what the helpers don't cover — search,
labels, and settings. Every raw Gmail call nests under `users`: it is
`gws gmail users <resource> <method>`, never `gws gmail <resource>` (a bare
`gws gmail messages list` fails with `unrecognized subcommand 'messages'`).

```bash
# Most recent message in the mailbox (newest first, ids only)
gws gmail users messages list --params '{"userId": "me", "maxResults": 1}'

# Search (ids only) then fetch what you need
gws gmail users messages list --params '{"userId": "me", "q": "from:sre newer_than:7d", "maxResults": 10}'

# Filter by label — labelIds is a JSON ARRAY, not a bare string
gws gmail users messages list --params '{"userId": "me", "labelIds": ["INBOX"], "maxResults": 1}'

# Headers + snippet — cheap triage
gws gmail users messages get --params '{"userId": "me", "id": "<MSG_ID>", "format": "metadata", "metadataHeaders": ["From","To","Subject","Date"]}'

# Full body (expensive — base64url payload parts)
gws gmail users messages get --params '{"userId": "me", "id": "<MSG_ID>", "format": "full"}'

# Threads
gws gmail users threads get --params '{"userId": "me", "id": "<THREAD_ID>", "format": "metadata"}'

# Labels
gws gmail users labels list --params '{"userId": "me"}'
gws gmail users messages modify --params '{"userId": "me", "id": "<MSG_ID>"}' \
  --json '{"addLabelIds": ["<LABEL_ID>"], "removeLabelIds": ["INBOX"]}'
```

**"What's my latest / unread mail?"** use `gws gmail +triage` (one call, clean
summary). To read a specific message use `gws gmail +read --id <ID>`. Only drop
to the raw two-call dance — `messages list --maxResults 1` for the id, then
`messages get … "format": "metadata"` — when you need exact fields the helpers
don't expose. (`+read` takes `--id`, not a positional, and prints a harmless
`unknown output format` warning.)

**Array params must be JSON arrays.** `labelIds`, `metadataHeaders`,
`addLabelIds`, `removeLabelIds` are lists: `"labelIds": ["INBOX"]`. Passing a
bare string (`"labelIds": "INBOX"`) is silently ignored and returns
`resultSizeEstimate: 0`, which looks like an empty mailbox but is a bad query.

Search operators: `from:`, `to:`, `subject:`, `has:attachment`, `newer_than:7d`,
`older_than:1m`, `is:unread`, `label:`, `in:anywhere`.

The granted scopes are `gmail.modify` (read, send, label and archive — **never
permanent deletion**; a `messages delete` call returns `403`, use
`messages trash` if the user explicitly asks) and `gmail.settings.basic`, which
unlocks `gws gmail users settings ...`: vacation responder (`getVacation`/
`updateVacation`), filters, forwarding addresses, `sendAs`, and IMAP/POP/language
settings. It does **not** cover delegates or S/MIME (`gmail.settings.sharing`,
not granted).

## Calendar

```bash
gws calendar +agenda                         # today, human-readable
gws calendar +insert --summary 'Standup' --start '2026-06-17T09:00:00+02:00' \
  --end '2026-06-17T09:30:00+02:00' [--attendee a@x] [--meet]   # create an event, MIME-free

gws calendar events list --params '{
  "calendarId": "primary",
  "timeMin": "2026-08-01T00:00:00Z",
  "timeMax": "2026-08-08T00:00:00Z",
  "singleEvents": true,
  "orderBy": "startTime",
  "maxResults": 25,
  "fields": "items(id,summary,start,end,attendees(email,responseStatus),hangoutLink)"
}'

gws calendar events insert --params '{"calendarId": "primary"}' \
  --json '{"summary": "Design review", "start": {"dateTime": "2026-08-03T10:00:00+02:00"}, "end": {"dateTime": "2026-08-03T11:00:00+02:00"}, "attendees": [{"email": "a@decathlon.com"}]}'

gws calendar freebusy query --json '{"timeMin": "...", "timeMax": "...", "items": [{"id": "a@decathlon.com"}]}'
```

`singleEvents: true` expands recurring events — without it you get the
recurrence rule instead of the occurrences.

## Chat

**Only `gws chat +send` works for a normal (non-bot) user. The generic
`gws chat <resource> <method>` subcommands are broken for writing.**

```bash
gws chat +send --space spaces/AAAAxxxx --text 'Deploy is green ✅'
```

Why the generic path fails: for each method `gws` requests **one** OAuth scope —
the *first* one the Discovery doc lists — and for most Chat methods that first
scope is a bot/app/admin scope (`chat.bot`, `chat.app.*`, `chat.admin.*`) that a
human user token cannot hold. So `gws chat spaces list`,
`gws chat spaces messages create`, etc. return
`403 Request had insufficient authentication scopes` **even though we granted
`chat.messages` / `chat.spaces`**. The `+send` helper is the exception: it passes
the method's full scope list, so Google keeps the user scope (`chat.messages`)
and the call authenticates. Use `+send` for anything write-related; treat the
generic `chat` subcommands as unavailable.

Two prerequisites before `+send` can post — both are one-time platform setup, not
something the agent can fix:

1. **A Chat app must be configured** for the OAuth project (`ai-sdlc-zofv`) in the
   Google Cloud console → *Google Chat API → Configuration* (app name, avatar,
   enabled). Until then, `+send` returns
   `404 Google Chat app not found. …configure the app in the Google Cloud console`.
2. **You must be a member of the target space.** Find space names with the Chat
   UI (the `spaces list` API is unusable per the bug above), e.g. copy the
   `spaces/AAAA…` id from the space URL.

If `+send` returns the `404 …app not found` message, tell the user the Chat app
isn't configured yet and stop — re-running won't help.

**Reactions.** We now grant `chat.messages.reactions` (create/read/delete), so the
token *has* the right scope. But there is no `+`-helper for reactions, so the only
path is the generic `gws chat spaces messages reactions create`, which is subject
to the same `select_scope` bug above — it may request a bot/app scope first and
fail with `403 insufficient scopes`. Treat reactions as best-effort: try the
generic call, and if it 403s on scopes, it's the known upstream limitation, not a
missing grant. No extra API to enable (same `chat.googleapis.com`).

## Tasks

Google Tasks — the user's to-do lists. Unlike Chat, the generic subcommands work
fine (every method's first scope is `tasks`, which we grant). `@default` is the
special id for the user's default list.

```bash
gws tasks tasklists list                                    # all task lists
gws tasks tasks list --params '{"tasklist": "@default", "showCompleted": false, "maxResults": 50}'

# Create a task (path param via --params, body via --json)
gws tasks tasks insert --params '{"tasklist": "@default"}' \
  --json '{"title": "Review PR #123", "notes": "before EOD", "due": "2026-09-10T00:00:00Z"}'

# Complete a task
gws tasks tasks patch --params '{"tasklist": "@default", "task": "<TASK_ID>"}' \
  --json '{"status": "completed"}'
```

`due` is RFC 3339 but Tasks only stores the **date** part — the time is ignored.

## People / Contacts

Read/write the user's contacts and look people up in the Decathlon directory.
Generic subcommands work (first scopes are `contacts`, `contacts.other.readonly`
and `directory.readonly`, all granted). `people/me` = the authenticated user.
Every read **requires** `personFields` (or `readMask` for directory calls) — the
API returns `400` without it.

```bash
# Your own profile
gws people people get --params '{"resourceName": "people/me", "personFields": "names,emailAddresses"}'

# Your saved contacts
gws people people connections list --params '{"resourceName": "people/me", "personFields": "names,emailAddresses", "pageSize": 50}'

# Look someone up in the Decathlon directory (domain profiles)
gws people people searchDirectoryPeople --params '{"query": "Laurent Thiebault", "readMask": "names,emailAddresses", "sources": "DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"}'

# Auto-collected "other" contacts (people you've emailed, not saved)
gws people otherContacts list --params '{"readMask": "names,emailAddresses", "pageSize": 50}'

# Create a contact
gws people people createContact --json '{"names": [{"givenName": "Ada", "familyName": "Lovelace"}], "emailAddresses": [{"value": "ada@example.com"}]}'
```

Directory lookups (`searchDirectoryPeople`, `listDirectoryPeople`) only work if
the Workspace admin has enabled directory sharing for the domain; otherwise they
return an empty list even with `directory.readonly` granted.

Search needs a warmup call. Before `searchContacts`, `otherContacts search` or
`searchDirectoryPeople`, Google requires one request with an **empty** `query`
to prime the server-side cache; the first real query otherwise returns partial
or empty results that look like "no match". Send the empty-query call, then
repeat with the real query:

```bash
gws people people searchContacts --params '{"query": "", "readMask": "names"}'          # warmup
gws people people searchContacts --params '{"query": "Ada", "readMask": "names,emailAddresses"}'
```

## Keep

**Not available.** Google Keep is intentionally excluded from the granted
scopes. Its `keep` / `keep.readonly` scopes are Google *restricted* scopes that
are not registered on the `ai-sdlc-zofv` OAuth consent screen (the scope picker
rejects them as "invalid" even though `keep.googleapis.com` is enabled), and
requesting `keep` at login hard-blocks the entire consent screen ("Some
requested scopes cannot be shown"). Do not add `keep` back until the scope is
registered on the consent screen and the login flow actually grants it.

## Forms

Create and edit Google Forms and read submissions. `forms.body` covers the form
structure (create/edit), `forms.responses.readonly` reads answers (there is **no**
write-responses scope — responses are read-only via the API). `create` only
copies `info.title` / `info.documentTitle`; add questions afterward with
`batchUpdate`. New forms land in the user's Drive.

```bash
# Create an (empty) form, then capture its formId from the response
gws forms forms create --json '{"info": {"title": "Team retro", "documentTitle": "Team retro"}}'

# Add a question
gws forms forms batchUpdate --params '{"formId": "<FORM_ID>"}' --json '{"requests": [
  {"createItem": {"item": {"title": "How did the sprint go?", "questionItem": {"question": {"textQuestion": {"paragraph": true}}}}, "location": {"index": 0}}}
]}'

gws forms forms get --params '{"formId": "<FORM_ID>"}'
gws forms forms responses list --params '{"formId": "<FORM_ID>", "pageSize": 50}'
```

## Meet

Manage meeting spaces you create via the API, and read past-conference data.
`meetings.space.created` = create/get/update/end **spaces created through the
API** (not arbitrary calendar meetings); `meetings.space.readonly` = read
`conferenceRecords` and their recordings/transcripts/participants (only for
meetings that actually happened, and only if recording/transcription was on).
`meetings.space.settings` (per-space moderation config) is intentionally not
granted — add it later if needed.

```bash
# Create a meeting space -> returns name (spaces/<id>) and meetingCode (abc-defg-hij)
gws meet spaces create --json '{}'
gws meet spaces get --params '{"name": "spaces/<SPACE_ID>"}'
gws meet spaces endActiveConference --params '{"name": "spaces/<SPACE_ID>"}'

# Past conferences (recordings/transcripts live under conferenceRecords)
gws meet conferenceRecords list --params '{"pageSize": 10}'
gws meet conferenceRecords recordings list --params '{"parent": "conferenceRecords/<REC_ID>"}'
gws meet conferenceRecords transcripts list --params '{"parent": "conferenceRecords/<REC_ID>"}'
```

## Cross-service helpers

```bash
gws workflow +standup-report     # today's meetings + open tasks
gws workflow +meeting-prep       # next meeting: agenda, attendees, linked docs
gws workflow +weekly-digest      # this week's meetings + unread count
gws workflow +email-to-task
gws drive +upload --file ./report.md --folder <FOLDER_ID>
```

## Non-Google files stored in Drive

Drive export only works on Google-native files. For anything else, download the
bytes first, then use a local converter:

```bash
scripts/gws-fetch.sh <file-id> -o ./doc.pdf     # binary download
pdftotext -layout ./doc.pdf -                   # PDF  → text  (poppler)
pandoc ./spec.docx -t markdown -o ./spec.md     # docx → md    (pandoc)
tesseract ./journey-map.png out && cat out.txt  # image → OCR  (tesseract)
```

If the tool is missing, say so rather than falling back to guessing — and note
that `pdftotext`/`pandoc`/`tesseract` come from `poppler`/`pandoc`/`tesseract`
on Homebrew.

## Generating the full upstream skill set

The `gws` project ships ~95 generated skills (one per service, plus personas and
recipes). To get them locally:

```bash
cd <a scratch directory> && gws generate-skills
```

This writes `./skills/gws-*/SKILL.md`. Use it as an escape hatch when you need a
method this reference doesn't cover — do **not** commit it into the repo.
Upstream source: <https://github.com/googleworkspace/cli/tree/main/skills>
