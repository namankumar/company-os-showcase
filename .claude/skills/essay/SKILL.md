---
name: essay
description: Write expressive, well-reasoned, persuasive essays on any topic
---

# Essay

## Purpose

Write essays that are interesting to read. Not content, not thought leadership, not posts. Essays: a thesis worth defending, an arc that moves, an ending that arrives somewhere new.

## Dependencies

- `.claude/skills/utils/voice.md` — mandatory before every draft
- `memory/feedback_manifesto_writing.md` — {{YOUR_NAME}}'s editing style and register preferences

## Reads

- `context/current-context.md` — if topic touches active work
- `projects/growsocial/planning/bank.md` — for experience-based topics, personal angles
- `docs/essays/` — prior essays (avoid repeating theses)

## Writes

- `docs/essays/[topic-slug].md` — local file first
- Google Doc only if explicitly requested

## Trigger

"write an essay" or "essay about" or `/essay`

---

## Doctrine

Six principles. Named D1-D6. Referenced by number in process steps and evals.

**D1 — Thesis worth defending**
The claim must be non-obvious. "Speed matters" is not a thesis. "Speed failed as a message because customers valued predictability more" is. Test: can a smart person reasonably disagree? If not, you're announcing, not arguing. The essay exists to make the non-obvious feel inevitable by the end.

**D2 — Progression, not accumulation**
Each section creates a problem the next must solve. If sections can be reordered without losing meaning, it's a listicle. Remove any section and the arc should break.

**D3 — Evidence that feels discovered**
The reader should arrive at the conclusion with you, not be handed it. Specific details do this better than general truths. A number, a name, a moment in time. "Three engineers lost their weekends" hits harder than "the team sacrificed."

**D4 — Declared, not explained**
Teaching language signals insecurity. Declare the position, let the reader catch up. Explaining your argument to the reader is the same as apologizing for it.

**D5 — Tension held honestly**
Name the strongest counterargument. Then dissolve it. Not dismiss it, dissolve it. This is what separates persuasion from propaganda.

**D6 — Ending that arrives**
The last paragraph should not summarize. It should arrive. If the last line could also be the first line, cut it. A command beats a conclusion. The essay earns the ending.

---

## Arc Anatomy

Every essay has six structural moments. Not sections. Moments. The essay can treat them in one paragraph or several, but all six must be present.

1. **Opening tension** — a contradiction, a scene, a counterintuitive fact. Not a thesis statement. Creates a question the reader has to read to answer.
2. **Stakes** — what's at risk if the thesis is wrong. Not backstory. Why this argument matters.
3. **Escalation** — the case builds. Each paragraph creates a problem the next solves.
4. **The turn** — the essay surprises. The strongest counterargument lands at full weight, or the thesis reframes into something bigger. Without the turn, there's no drama. The turn is where readers decide whether to trust you.
5. **Climax** — where the insight hits hardest. Often the shortest moment. One paragraph, sometimes one sentence.
6. **Landing** — not a conclusion. Where the reader finds themselves after the journey. Specific, new, doesn't restate anything.

---

## Doctrine × Arc Mapping

Consulted in Step 3 before drafting begins. Doctrine is applied per arc moment, not globally.

| Arc moment | Doctrine | What to do |
|---|---|---|
| Opening tension | D1 | Create the question the thesis answers, in negative form. Don't state the thesis. Imply it as an absence or contradiction. |
| Stakes | D3 | One specific detail (number, name, moment) that makes the stakes concrete. General stakes are not stakes. |
| Escalation | D2, D3, D4 | Each paragraph creates a problem the next solves (D2). Every general claim gets a specific anchor (D3). No sentence explains what the previous one meant (D4). |
| Turn | D5 | Name the strongest counterargument at full weight. Steelman it. Then dissolve it. Soft acknowledgment ("some might argue...") is not the turn. |
| Climax | D1, D4 | This is where the thesis becomes inevitable. Declare it (D4). If the climax reads like an explanation, it hasn't arrived yet. |
| Landing | D6 | Arrive somewhere new. Last line is a specific detail, action, or question. If it could be the first line, cut it. |

---

## Input

- **Topic** (optional) — any form, even one sentence
- **Seed insight** (optional) — {{YOUR_NAME}}'s intuition, a contrarian take, a framing to explore

## No-Input Mode

If no topic is given, load `context/current-context.md` and `projects/growsocial/planning/bank.md`. Surface 3-5 candidate topics. Each gets:

- One-sentence topic description
- Candidate thesis — the non-obvious angle worth arguing (D1)
- Why now — why this topic has resonance at this moment

{{YOUR_NAME}} picks one (or none). Don't draft until a topic is confirmed.

## Clarifying Questions (max 3, ask before drafting)

1. **Audience** — who is reading this? (default: thoughtful technology professional)
2. **Register** — conviction/urgency, reflective, combative, or elegiac?
3. **Length** — short (~400 words), medium (~800), or long (~1200+)?

If no insight provided and {{YOUR_NAME}} didn't seed a thesis, surface a candidate thesis and wait for confirmation before drafting.

---

## Process

### Step 1: Find the thesis (D1)

- Must be non-obvious and defensible (a smart person can disagree)
- One sentence. If it doesn't rule something out, it's not a thesis.
- Present to {{YOUR_NAME}} before drafting if no seed insight was provided.

### Step 2: Select a linguistic device

- Pick ONE from voice.md device table before drafting
- Device selection drives structure, not the other way around
- State the device chosen and why (one sentence) before drafting

### Step 3: Map the arc

- Place all six arc moments: opening tension → stakes → escalation → turn → climax → landing
- Annotate each moment with its governing doctrine from the Doctrine × Arc table
- At the turn: name the specific counterargument that will be steelmanned. This is required before drafting begins. No turn = no draft.
- Test D2: can any section be reordered without losing meaning? If yes, restructure before proceeding.

### Step 4: Draft

- Generate fast. First draft is a punching bag.
- Apply voice.md rules during drafting (not as a post-pass)
- Draft each arc moment by applying its assigned doctrine from Step 3
- D3 check per paragraph in escalation: what specific detail, number, or moment anchors this claim? If none, the claim is weak.
- D4 check per sentence: does this sentence explain what the previous one meant? If yes, delete it.
- At the turn: steelman the counterargument first, then dissolve it. If the counterargument feels easy to answer, it's not the strongest one.
- At the climax: read it aloud. Does it declare or explain? If it explains, rewrite as a declaration.

### Step 5: Self-review

Run internally against `evals/essay.md`. Fix before presenting. Don't surface failures to {{YOUR_NAME}} unless a structural problem (missing turn, no thesis) requires his input.

### Step 6: Present

Output the essay. Below it, two lines only:
- `Device: [device name]`
- `Thesis: [one sentence]`

{{YOUR_NAME}} reacts to the essay, not the explanation of it.

---

## Editing Mode

After presenting, {{YOUR_NAME}} will push back. Rules from manifesto writing feedback apply:

- Generate fast, expect heavy editing. Don't over-polish.
- When he says "rewrite," produce a new version. Don't explain why the old one was fine.
- "Undo" is a thinking step. He compares versions. Don't ask why he reverted.
- His best lines come from corrections, not first drafts. The ratio of generation to editing is roughly 1:50.
