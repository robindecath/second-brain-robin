# Protocol — Traceable Attribution

**Purpose:** Every claim resolves to a specific location in raw data. Anyone should be able to take a citation from a slide and land on the exact transcript moment, survey row, or event definition.

**Hard rule:** No claim without a citation. If a citation cannot be produced, the claim is removed or restated as an explicit assumption.

---

## 1. Citation formats

Stable across tools. Adapt the identifier scheme to whatever the source system provides, but keep the shape.

| Source | Format | Example |
|---|---|---|
| Interview / session | `[P##:MM:SS]` | `[P07:24:55]` |
| Multi-participant | `[P02, P05, P11]` | with per-quote timestamps where quoted |
| Session note (no recording) | `[P03 · note § topic]` | `[P03 · note § onboarding]` |
| Survey closed question | `[SURVEY:Qn · value · n=]` | `[SURVEY:Q14 · "unclear cost" 34% · n=418]` |
| Survey open text | `[SURVEY:row#### · Qn]` | `[SURVEY:row1187 · Q16]` |
| Survey segment | `[SURVEY:Qn · segment=x · n=]` | `[SURVEY:Q14 · segment=ent · n=57]` |
| Analytics event | `[EVT:event_name · metric · date range]` | `[EVT:checkout_back_nav · 41% · 2026-02-01→03-31]` |
| Funnel step | `[FUNNEL:name · step · rate · range]` | `[FUNNEL:checkout · payment · 59% · Q1 2026]` |
| Support / ticket | `[TICKET:id · date]` | `[TICKET:48221 · 2026-02-14]` |
| Prior study | `[REPO:study-id · finding-id]` | `[REPO:2025-checkout · F-02]` |
| Assumption (no source) | `[ASSUMPTION]` | must state the validating method |

`[ASSUMPTION]` is not a fallback for laziness. It is used when a stakeholder explicitly asks for a provisional artefact, and it must be visually distinct in the deliverable.

---

## 2. Quoting rules

- Verbatim means verbatim. Preserve fillers, hedges, self-corrections, and repetition. "I mean, it's… fine? I guess" carries different information from "it's fine".
- Elision uses `[…]` and may never reverse or soften meaning. Removing a hedge is a meaning change.
- Clarifying insertions use `[square brackets]` and are the writer's words, marked as such.
- Translations: mark `[trans. from FR]` and keep the original available in the ledger. Translate meaning, not just words.
- One quote, one participant, one timestamp. Never composite. Never create a representative quote that no one said.
- A quote used to support a finding must have been given in a context consistent with that finding. Note when a quote was moderator-prompted.

---

## 3. Numbers

Every number carries its denominator and its frame.

- Bad: `34% of users find cost unclear`
- Good: `34% of survey respondents (n=418, fielded Mar 2026, consumer tier) selected "unclear cost" at Q14 [SURVEY:Q14]`

For analytics, cite the event definition, not just the name. If the definition is unavailable, request it; an event whose trigger condition is unknown cannot support a claim about behaviour.

Percentages are never used for qualitative samples. Use counts: `7 of 12`.

---

## 4. The evidence ledger

Maintained continuously, shipped with every deliverable. It is the audit trail that makes the synthesis checkable.

| Finding | Claim | Qual IDs | Quant IDs | Analytics IDs | Counter-evidence | Confidence |
|---|---|---|---|---|---|---|
| F-01 | … | P02, P05, P07, P11 | SURVEY:Q14 | EVT:checkout_back_nav | P09; ent segment | High |
| F-02 | … | P03, P08 | — | — | none found | Low — single source |

Rules:
- Ledger rows are written as findings emerge, not reconstructed afterwards. Reconstruction is where fabrication enters.
- Every row in every deliverable traces to a ledger row.
- The ledger is never summarised for the deliverable. It ships whole.

---

## 5. Chain of custody through rendering

Attribution survives compression. When a finding becomes a persona attribute, a journey pain point, an HMW, or an OST opportunity, the source IDs travel with it.

```
Raw       P07 at 24:55 says …
Observation   "Cannot verify total before commit"     [P07:24:55]
Finding   F-03                                        [P02,P05,P07,P11 + SURVEY:Q14 + EVT:…]
Journey   Payment stage · pain point 2                → F-03
Persona   "Cautious Comparer" · frustration 1         → F-03
HMW       HMW-04                                      → F-03
OST       Opportunity O-02                            → F-03
```

If a deliverable element cannot name its parent finding, it was invented during rendering. Remove it.

---

## 6. Prohibitions

- Never invent, paraphrase into quotation marks, or "improve" a quote.
- Never cite a finding ID as if it were raw evidence — findings cite raw data, deliverables cite findings.
- Never carry a claim forward from a previous synthesis without re-citing its original source.
- Never present a number without n and date range.
- Never attribute a view to "users" when the evidence is participants.
