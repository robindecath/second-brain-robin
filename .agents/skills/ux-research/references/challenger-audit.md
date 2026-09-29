# Protocol — Challenger Audit (Anti-Flattening)

**Purpose:** Actively hunt for the evidence that would weaken each finding, and protect minority perspectives from being averaged out of existence.

Summarisation compresses toward the modal case. The loud, fluent, frequently-repeated signal survives; the single participant who said something inconvenient does not. This protocol is the counterweight, and it is **mandatory before any deliverable is rendered** — not an optional extra pass.

---

## 1. The stance

For each finding, temporarily adopt the position that it is **wrong**, and search the corpus for the evidence that would prove it. Only then return to the evidence for it.

Search terms should be drawn from the *opposite* of the finding. If the finding is "users find the filter confusing", search for moments of successful filter use, expressions of confidence, and participants who never mentioned filters at all.

---

## 2. The five queries

Run all five per finding. Record the result of each, including nulls.

### Q1 — Disconfirming instances
Who in the corpus did *not* experience this? What did they do instead, and what was different about them or their context?

> `P09 completed the flow without hesitation [P09:12:30] — prior customer, had a saved payment method.`

### Q2 — Minority positions
Who said the opposite, or something orthogonal? Record it verbatim with its ID. A view held by one participant out of twelve is reported as exactly that — not omitted, not inflated.

> `P04 wanted fewer details at this step, not more [P04:22:10].`

Two participants disagreeing with ten is not noise. It is often the segment you failed to recruit enough of.

### Q3 — Subtle frictions
Scan for signals that carry no strong verbal marker: hesitations, self-corrections, re-reads, repeated scrolling, task completed but slowly, "it's fine, I guess". These are systematically lost in summarisation because they generate no quotable sentence. Log them by timestamp with a behavioural description.

> `P06 paused 14s at the consent step, scrolled up twice, then continued without comment [P06:08:12–08:26].`

### Q4 — Silence and absence
What did *no one* mention that you expected them to? Who is missing from the sample entirely? Whose absence changes the finding's scope?

> `No participant mentioned the help link. Three had it visible on screen for >30s.`
> `No screen-reader users in sample; accessibility claims out of scope.`

### Q5 — Alternative explanations
List at least two rival explanations for the same evidence. State what would distinguish between them.

> `Alt A: pricing ambiguity. Alt B: moderator prompt introduced the idea of cost (P02, P05 both prompted). Distinguisher: unprompted mentions — 2 of 4.`

Q5 catches moderator-introduced findings, which are among the most common false positives in qualitative work.

---

## 3. Outcome per finding

| Result | Action |
|---|---|
| Disconfirming evidence found and it is bounded | Keep the finding; attach the boundary condition explicitly |
| Disconfirming evidence found and it is substantial | Downgrade to hypothesis; report the tension as the finding |
| Rival explanation not distinguishable from the evidence | Report both; name the study that resolves it |
| Nothing found after all five queries | Record `searched: none found` — never leave the field empty |

An empty counter-evidence field means the audit was not run. `none found` means it was.

---

## 4. Protecting minority perspectives in output

- **Never** aggregate a minority view into the majority statement to make the narrative cleaner.
- Minority positions get **named space** in every deliverable — a section, a row, a slide — not a footnote.
- Report with counts and context: *"2 of 12 participants, both returning users, wanted the opposite."*
- Where a minority view maps to a segment (accessibility need, low bandwidth, non-native language, expert user, edge-case workflow), flag it as a potential **underrecruited segment**, and say so in the open questions.
- If the sample was too small to detect a minority view, say that too. Absence of minority evidence in n=8 is not evidence of consensus.

---

## 5. Audit block

Attach this to every finding. It travels with the finding into the deliverable.

```
CHALLENGER AUDIT · F-03
Q1 disconfirming   P09 completed without friction (returning, saved card) [P09:12:30]
Q2 minority        P04, P12 wanted less detail, not more [P04:22:10, P12:16:44]
Q3 subtle friction P06 14s pause + double scroll, no verbal signal [P06:08:12]
Q4 silence         nobody mentioned help link; no enterprise users in qual sample
Q5 alternatives    (a) cost ambiguity (b) moderator priming — 2 of 4 unprompted
VERDICT            Hold at high confidence, bounded to consumer tier + new users.
                   Minority view reported separately as F-03b.
```

---

## 6. Self-check before rendering

- Did every finding get all five queries, or did I stop when the first one came back empty?
- Is there any participant whose contribution appears in no finding at all? Why not?
- Did any quote get trimmed in a way that removes its hedge?
- Does the deliverable read as more certain than the evidence ledger?
- Would a participant reading this recognise what they said?

If the last question is uncomfortable, the synthesis flattened something.
