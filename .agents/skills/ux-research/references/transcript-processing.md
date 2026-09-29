# Transcript processing and flash debriefs

Covers turning raw session data into clean, anonymized records and per-session insights with cumulative memory.

## Part 1 — Transcript cleaning

Use [../assets/cleaned-transcript-template.md](../assets/cleaned-transcript-template.md).

### Required inputs

1. Research objectives for the session
2. Raw transcript or notes
3. Output language

If the raw text is already in the message, process it directly and infer missing details rather than blocking on questions.

### Absolute neutrality rule

Remove noise. Never alter meaning.

Do:

- Remove filler words and hesitations ("um", "uh", "euh", "bah", "like"), stutters, and false starts.
- Fix obvious speech-to-text and typing errors.
- Attribute turns clearly to moderator and participant.
- Group the exchange under the protocol sections it belongs to.
- Redact PII per [privacy-and-consent.md](privacy-and-consent.md), using typed placeholders.
- Mark unclear audio as `[inaudible]` rather than guessing.

Do not:

- Summarize, shorten, or compress answers. The cleaned output keeps the full depth of the original.
- Translate. If the session was in French, the cleaned transcript stays in French, unless the user explicitly asks otherwise.
- Smooth away emotional reactions, strong adjectives, hedging, or domain-specific vocabulary — these carry the signal.
- Add interpretation, headings that editorialize, or inferred intent.
- Reorder answers to make them read better.

### Modifying a cleaned transcript

If the user asks to change the cleaned record after generation:

1. Do not jump ahead to analysis.
2. State the advantages and the risks of the edit, specifically the risk of confirmation bias and loss of original context.
3. Ask for explicit confirmation before applying it.
4. Only then regenerate the transcript.

## Part 2 — Post-session flash debrief

Use [../assets/flash-debrief-template.md](../assets/flash-debrief-template.md). Run it as soon after the session as possible, while memory is fresh.

### Inputs

The moderator's one or two "hot impressions" — what struck them most — plus the participant segment. If the user already gave them, proceed directly.

### Triangulation

Confront each hot impression with the factual record, and be intellectually honest when they disagree.

- **Validation:** the impression is supported. Cite the exact quote or observed behavior that proves it.
- **Nuance:** the impression is partly right. State the objective qualification.
- **Contradiction:** the record contradicts the impression. Say so plainly and show the evidence.

Keep only the categories that actually apply to the session. A debrief with no contradictions is fine; a debrief that never finds any across a whole study is a warning sign about the analysis.

### Per-session output

- Up to five key insights, each with a concrete product or design impact.
- Frictions and blockers, separated into critical (task failed or was abandoned) and moderate (hesitation, recovery, workaround).
- Methodology notes: weak signals worth probing, and specific questions to add for the next session.
- One golden quote: the single most representative verbatim, anonymized.

### Cumulative memory

From session two onwards, compare the current session against previous ones and maintain a running synthesis.

- Use qualitative strength language: **recurring**, **isolated**, **systemic**, **emerging**, **contradicted**.
- Do not report "4 out of 6 participants" style counts on small qualitative samples; they imply measurement the sample cannot support.
- Distinguish confirmed patterns from single-session observations.
- Track disconfirming evidence explicitly, including anything an earlier session suggested that later sessions did not reproduce.
- Note when new sessions stop producing new themes — that is the saturation signal for stopping fieldwork.

### Sharing debriefs

- A chat-sized summary should carry only product impacts and frictions, never raw verbatims with identifying detail.
- Keep the participant ID, never the name.
- Label the debrief as per-session evidence, not study conclusions.

## Handoff to synthesis

When all participants are processed, move to cross-study synthesis with [synthesis-and-modeling.md](synthesis-and-modeling.md), carrying forward: confirmed patterns, cumulative frictions, contradictions, open questions, and unused weak signals.
