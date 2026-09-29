# Deliverable — Debrief Presentation Deck

**For:** stakeholders who need the "so what" and hold a decision.
**Not for:** archival documentation. The deck is a decision instrument; the ledger is the record.

---

## Before writing

Establish three things. Without them the deck is a data dump.

1. **The decision** this deck serves, and who owns it.
2. **Audience prior** — what they currently believe. Findings that confirm it need less space; findings that contradict it need more evidence, earlier.
3. **Format** — read-ahead document or live presentation. Read-aheads carry their own narration; live decks do not.

---

## Structure

| # | Slide | Content |
|---|---|---|
| 1 | Title | Study name, dates, method, sample in one line |
| 2 | **Headline** | The single sentence that changes the decision. Lead with the answer |
| 3 | What we did | Method, sample, what is and is not represented ([limits block](../references/confidence-and-limits.md)) |
| 4 | Findings at a glance | 3–5 findings, each with confidence grade |
| 5–n | One slide per finding | See below |
| n+1 | **What we heard that complicates this** | Minority views and disconfirming evidence, named space |
| n+2 | Implications | So-what per finding, mapped to owner |
| n+3 | Recommended actions | Prioritised, with confidence attached |
| n+4 | Open questions | What we could not answer + method to close |
| Appendix | Evidence ledger, full quote bank, survey/analytics detail |

Slide n+1 is not optional and does not get cut for time. It is the anti-flattening guarantee in the artefact itself.

---

## Finding slide anatomy

```
FINDING TITLE — written as a claim, not a topic
"Users can't confirm the total before committing"     [CONFIDENCE: HIGH]

EVIDENCE
  Qual       7 of 12 participants                     [P02, P05, P07, P11 …]
  Survey     34% selected "unclear cost" (n=418)      [SURVEY:Q14]
  Analytics  41% of abandons return-nav within 8s     [EVT:checkout_back_nav]

VERBATIM
  "I'm not clicking that until I know what it's actually going to charge me"
                                                      [P07:24:55]

BUT                                                   ← always present
  Enterprise segment shows no effect (n=57). Two participants wanted
  less detail at this step [P04:22:10, P12:16:44].

SO WHAT
  The lever is an itemised pre-commit total, not discounting.
```

Title as claim, never as topic. "Checkout" is a topic. "Users can't confirm the total before committing" is a finding.

---

## Rules

- Every number on every slide carries n and date range.
- Every quote carries a participant ID and timestamp.
- Confidence grade appears on the finding slide, not only in the appendix.
- Recommendations inherit the confidence of their supporting finding. A low-confidence finding produces a *test*, not a *build*.
- No composite quotes, no illustrative-but-invented examples, no stock persona faces standing in for participants.
- If a finding needs a boundary condition, the boundary goes on the slide, not in the speaker notes.

---

## Common pressure and the response

| Ask | Response |
|---|---|
| "Can we cut the caveats slide?" | Move it, don't cut it. Offer to merge it into the finding slides so each claim carries its own boundary |
| "Can we just say users want X?" | Give the precise version: "7 of 12 participants, all new consumer-tier, said X" |
| "Make it one number" | Offer the number with its frame, plus the qualitative reason it moves |
| "Drop the low-confidence findings" | Reframe as open questions with a named test — they are the research roadmap |
