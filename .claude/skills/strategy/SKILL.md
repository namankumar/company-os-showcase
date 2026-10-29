---
name: strategy
description: Create executive-grade strategy docs
---

# Strategy Doc Generator

## Purpose
Create executive-grade strategy alignment documents — roadmap, timeline, GTM, growth, and product marketing narratives. Designed to position Product as the owner and appeal to senior leadership (VP/C-level, ex-Meta/FAANG caliber).

## Dependencies
- `.claude/skills/utils/voice.md` — apply before all output
- `.claude/skills/utils/writeDocs.md` — apply when editing existing docs

## Reads
- `context/current-context.md` — decision-making context (the "why now" for any strategy)
- `context/okr-status.md` — company OKRs (strategy must serve company goals, surface overlap)
- `context/narrative-map.md` — active narratives (strategy should reinforce or challenge these)
- `context/org-dynamics.md` — political context (who benefits, who loses, how to position)
- `context/room/` — room analysis (audience dynamics, stakeholder positions, what persuades whom)
- `docs/strategy/` — prior strategy docs
- `docs/market-research/` — landscape, TAM, trends
- `docs/narrative/` — positioning
- `docs/product/master-prd-roadmap.md` — master PRD and roadmap (source of truth)

## Writes
- `docs/strategy/` — strategy docs, execution plans
- `docs/gtm/` — GTM plans

## Trigger
"run strategy" or "create a strategy doc" or "write a strategy alignment"

## Process

### Step 1: Gather Context
Before creating anything, ask the user the following questions. Do not proceed until these are answered.

1. **What is this doc about?** (product name, initiative, or decision)
2. **Who is the audience?** (names, roles — then load their room files from `context/room/<group-name>.md` for what they care about, what persuades them, and current positions)
3. **What is the current state?** (where things stand right now — launch readiness, market moment, competitive window)
4. **What are your strategic bets?** (2-4 theses you're putting forward — what you believe and why)
5. **What phases does the roadmap have?** (time periods, themes, key deliverables per phase)
6. **What are you deliberately NOT doing?** (tradeoffs, cuts, things you're deferring)
7. **What narratives should marketing push?** (key stories, claims, proof points)
8. **What's the growth strategy?** (channels, loops, launch plan)
9. **What are you asking for?** (headcount, budget, decisions)
10. **What are the top risks?** (and how you'd mitigate each)
11. **What decisions do you need from leadership?** (real tradeoffs, not softballs)

### Step 2: Evaluate Each Strategy
Before writing the doc, score every strategic bet against these four criteria. Present the evaluation to the user as a table and discuss before proceeding.

| Criteria | Question | Signal |
|----------|----------|--------|
| **Market Size** | How large is the addressable market? Is it growing? | TAM/SAM figures, growth rate, adjacencies |
| **Defensibility** | Can this be copied easily? What moats does it create? | Network effects, switching costs, proprietary tech, regulatory barriers |
| **Strengths Alignment (SWOT)** | Does this play to our strengths and avoid our weaknesses? | Team capability, existing assets, brand fit, resource availability |
| **Precedent** | Has something similar succeeded elsewhere? | Comparable companies, analogous markets, proven playbooks — precedent raises confidence |

**How to use this:**
- Rate each bet **High / Medium / Low** on each criterion.
- A bet that scores Low on 2+ criteria needs a strong justification or should be cut.
- Precedent is a confidence booster, not a requirement — but bets with zero precedent should be flagged as higher-risk.
- Surface the evaluation table to the user and discuss before moving to doc creation.

### Step 3: Create the Doc
Generate a markdown file in `docs/` using the structure below. Follow all formatting rules exactly.

### Step 4: Review
Walk the user through the doc section by section. Ask if anything needs to be adjusted before finalizing.

## Document Structure

```
# [Product/Initiative] — Product Strategy & Execution Plan

**Owner:** Product — [Name]
**Date:** [Month Year]
**Status:** Draft
**Stakeholders:** [Teams]
**Decision needed by:** [DATE]
**Read time:** ~[X] minutes

---

**TL;DR:** [One sentence. The entire doc compressed into a single claim or ask.]

**How to read this doc:** Sections 1–2 for strategic context (X min). Sections 3–7 for execution plan (X min). Section 10 for decisions needed (X min).

---

## 1. Current State
## 2. Strategy
## 3. Product Roadmap
## 4. Product Overview
## 5. Go-to-Market & Growth
## 6. Narrative Portfolio
## 7. Metrics & Milestones
## 8. Resource & Budget Ask
## 9. Risks
## 10. Open Decisions

---

## Version History
| Date | Change |
|------|--------|
```

## Formatting Rules

These are non-negotiable. They are what make the doc read as senior product leadership, not project management.

### Meta & Header
- **Owner**, not Author. "Owner: Product — [Name]"
- **Stakeholders** as a separate line — Owner decides, stakeholders input
- Include **Status** (Draft / For Review / Final), **Decision needed by**, and **Read time**
- **TL;DR** — one sentence, right after the header. If they read nothing else, they get the point.
- **"How to read this doc"** — routing guide with time estimates per section group

### Per Section
- **1 page max per section.** No exceptions.
- **Bold the first sentence of every section** as a topic sentence — execs skim headers then first lines. If those two tell the story, you've won.
- **Blockquote callouts** — use sparingly (1-2 per doc) for the most important insights. The thing you'd say if you had 30 seconds in an elevator.
- **Tables: 4-5 columns max.** Wider reads as "I didn't synthesize."
- **Bullets: 2 lines max each.** If it's longer, it's a paragraph pretending to be a bullet.
- **No emojis.** Unless explicitly requested.

### Section-Specific Guidance

**1. Current State** — Frame the "why now." Not a primer — a forcing function. What changed, why it matters, what happens if we don't move.

**2. Strategy** — 3-4 bets as falsifiable theses: "We believe X because Y, and we'll know we're right when Z." If a bet doesn't rule something out, it's not a strategy. Each bet must include its evaluation from Step 2 (Market Size, Defensibility, Strengths Alignment, Precedent) — inline or as a summary table. Bets without precedent should be explicitly flagged as exploratory.

**3. Product Roadmap** — Phased, outcome-oriented. Each phase gets: Goal, Key bets shipping, What we're deliberately not doing, Exit criteria to next phase. Include Owner column — Product assigns, teams execute.

**4. Product Overview** — Grouped by phase. Each capability gets: What it is (one sentence), Who it's for, Why this phase. Cut items included with reason. Link to PRD/Figma for depth.

**5. Go-to-Market & Growth** — Channels ranked by expected impact. Growth loops with why they compound. Target customer embedded in channel logic — no separate ICP section.

**6. Narrative Portfolio** — Narratives Product is directing for marketing to execute. Each gets: Name, Core claim (one sentence), Target audience, Proof points (2-3), Channels. Mark as Launch or Phase 2.

**7. Metrics & Milestones** — North star stated with conviction (no justification paragraph). 3-5 supporting metrics. One table. Revenue model: one line on mechanism, one line on target.

**8. Resource & Budget Ask** — Specific, not hedged. "$X" not "$X-$Y." Every line ties to a roadmap phase. Frame hires as coordinating with Product on priorities.

**9. Risks** — Top 5 max. Ordered by severity. Each with a concrete mitigation — not "we'll monitor it."

**10. Open Decisions** — 2-4 real decisions with real tradeoffs. Each includes enough context to decide in the room. Lead with a recommendation: "Option A (recommended) / Option B."

### Structural Signals of Seniority
- Tradeoffs stated explicitly (what you're NOT doing)
- Exit criteria between phases
- Recommendations on open decisions (don't just ask — lead)
- Owner column on deliverables
- "Not Shipping" items with rationale

### What to Never Include
- Table of contents (it's under 10 pages)
- Logos or cover pages
- Footnotes
- Wireframes or technical specs (link out)
- ICP as a standalone section (embed in GTM)
- Revenue projection spreadsheets (one line on model + target)
- "Why we chose this metric" justifications

### Version History
- Table at the bottom: Date, Change (one line each)
- Shows the doc is a living artifact

## Output Destination
- Save as `.md` in `docs/`
- Never write directly to Google Drive/Docs — local markdown first, output to Drive only when explicitly requested
