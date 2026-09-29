# Protocol — Data Triangulation

**Purpose:** Test each candidate finding against every source type available, and report honestly when only one type exists.

Triangulation is not "find more evidence for what I already believe". It is asking each source type the same question and recording what each one says, including when they disagree.

---

## 1. Check what exists first

Run this before triangulating, once per study:

| Source type | Present? | Covers | Identifier scheme |
|---|---|---|---|
| Qualitative | | sessions, dates, segments | `P##:MM:SS` |
| Quantitative survey | | n, fielding window, segments | `SURVEY:row · Qn` |
| Product analytics | | events, date range, population | `EVT:name · range` |
| Repository / prior studies | | study IDs, dates | `REPO:study-id · finding-id` |

If only one type exists, **say so and stop triangulating**. Report the finding as single-source with its scope limit intact. Do not simulate corroboration by quoting the same qualitative sessions twice under different labels.

---

## 2. The cross-check

For each candidate finding, ask each available source the same three questions:

1. **Does this source speak to this finding at all?** (Often the honest answer is no.)
2. **If it speaks, does it agree, disagree, or qualify?**
3. **For whom?** Which segment, which time window, which sample.

Record the result as one of:

| Status | Meaning | How to write it |
|---|---|---|
| **Converging** | Two or more source types point the same way | State the finding directly; cite all sources |
| **Qualifying** | Sources agree on the effect but disagree on scope or size | State the finding *with* the boundary condition |
| **Diverging** | Sources point different ways | Report both. Do not pick a winner. Explain the likely reason and what would resolve it |
| **Silent** | Other sources have nothing to say on this | Single-source finding; scope narrowly |

**Divergence is a finding, not a problem to be tidied away.** Qual saying "the filter is confusing" while analytics shows heavy filter use usually means the two are measuring different moments — first-time versus repeat, or intent versus success. Say that.

---

## 3. What each source can and cannot establish

| Source | Establishes | Cannot establish |
|---|---|---|
| Qualitative | Why; mental models; language; unmet needs; failure mechanisms | Prevalence, magnitude, market size |
| Survey | Prevalence within the sample frame; attitude distribution; segment differences | Behaviour; causation; anything about non-respondents |
| Analytics | What happened, at what volume, in what sequence | Why; intent; satisfaction; the experience of users who never arrived |
| Repository / prior work | Change over time; whether this is new or recurring | Current state without fresh verification |

Never let a source carry a claim from the right-hand column. The most common breach: using analytics drop-off to assert a *reason*.

---

## 4. Sequencing

Pick the order deliberately and say which you used.

- **Qual → Quant (validate):** a qualitative finding is checked for prevalence in survey or analytics. Guard: you can only find what you went looking for. Run the challenger audit after.
- **Quant → Qual (explain):** an anomaly in the numbers is explained by returning to transcripts. Guard: do not treat the first plausible explanation as the only one.
- **Parallel:** both analysed independently, then compared. Strongest; use where the schedule allows.

---

## 5. Recording the result

```
F-03 · Users cannot confirm total before committing
├── Qual        CONVERGING   4/12 participants, all consumer tier
│                            [P02:18:40, P05:09:12, P07:24:55, P11:31:02]
├── Survey      CONVERGING   Q14 "unclear cost" 34% (n=418)
│                            enterprise segment 6% (n=57) → QUALIFYING
├── Analytics   CONVERGING   checkout_back_nav 41% of abandons <8s
│                            [EVT:checkout_back_nav · 2026-02-01→03-31]
└── Repo        SILENT       no prior study on checkout
STATUS: three_source, converging, bounded to consumer tier
```

---

## 6. Prohibitions

- Do not count two analyses of the same raw data as two sources.
- Do not report a percentage from a qualitative sample.
- Do not average across source types into a single score.
- Do not describe a finding as "validated" when the validating source was silent — "validated" requires an explicit agreeing signal, not an absence of contradiction.
- Do not drop the qualifying condition when the finding is summarised into a headline. The headline inherits the boundary.
