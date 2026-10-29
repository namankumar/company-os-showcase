---
name: roadmap
description: Manage product roadmap (features, not tasks)
---

# Roadmap Orchestrator

## Purpose

Manage product roadmap as a strategic artifact. Roadmap = features/initiatives evaluated against strategy, competitive landscape, and engineering capacity. Every item earns its place (or gets cut) with evidence.

**Difference from todos:**
- **Todos** = tasks with owners and deadlines (this week, this month, this quarter)
- **Roadmap** = features/initiatives evaluated for strategic fit, ROI, and engineering cost

## Reads
- `context/current-context.md` — decision-making context (operating model shift, what {{COO}} expects)
- `context/okr-status.md` — OKR targets (roadmap items must advance company OKRs, flag overlap)
- `context/narrative-map.md` — active narratives (roadmap should reinforce narratives we're pushing)
- `context/cadences.md` — sprint cycles, upcoming milestones (timing context for Now/Next/Later)
- `docs/product/master-prd-roadmap.md` — master PRD and roadmap (source of truth)
- `docs/product/roadmap-prospective.md` — features under consideration
- `docs/strategy/` — strategy docs, execution plans
- `docs/market-research/` — competitive analyses
- `docs/narrative/` — positioning, messaging
- `tasks-db.md` — parking lot items

## Writes
- `docs/product/master-prd-roadmap.md` — master PRD and roadmap (source of truth)
- `docs/product/roadmap-prospective.md` — prospective features

## Input Sources

### Primary
1. **docs/product/master-prd-roadmap.md** — committed roadmap
2. **docs/product/roadmap-prospective.md** — features under consideration (not yet committed)
3. **Parking Lot** — items flagged as "Roadmap Idea" in todos

### Strategic Context (must read before any roadmap update)
5. **Strategy docs** — `docs/*strategy*.md`, `docs/*plan*.md`, `docs/*execution*.md`
6. **Competitive analyses** — `docs/*analysis*.md` (relevant alternatives and category peers)
7. **Narrative docs** — `docs/*narrative*.md`, `docs/*messaging*.md`, `docs/*positioning*.md`
8. **Existing PRDs and feature briefs** — `docs/product/{{PRODUCT}}-*.md`

### Feature Discovery
10. **Conversation history** — features discussed in past sessions but never formally tracked
11. **Team and customer conversations** — feature requests and recurring needs
12. **Work tracker** — issues tagged as "future" or "backlog"

## How to Find Relevant Docs

Don't read everything. Use this triage process:

### Step 0: Read the index
Read `docs/product/master-prd-roadmap.md` first. It contains a "Source Docs" section at the top listing which strategy, competitive, and narrative docs informed the current roadmap. Start there.

### Step 1: Glob for candidates
Search `docs/` with these patterns:
- `docs/*strategy*.md`, `docs/*plan*.md`, `docs/*execution*.md` — strategy
- `docs/*analysis*.md`, `docs/*[competitor-name]*.md` — competitive
- `docs/*narrative*.md`, `docs/*messaging*.md`, `docs/*positioning*.md` — narrative
- `docs/*prd*.md`, `docs/*brief*.md` — product specs

### Step 2: Read headers only
For each file found, read the first 30 lines (title, date, TL;DR, status). This tells you:
- **What it covers** — is this relevant to the features being evaluated?
- **How recent it is** — strategy from 6 months ago may be outdated
- **Status** — Draft docs are lower-weight than Final/Active docs

### Step 3: Deep-read only what's relevant
A doc is relevant if:
- It defines a strategic bet that a roadmap feature claims to advance
- It contains competitive analysis of a market we're entering
- It has a narrative/positioning framework that a feature supports or contradicts
- It's a PRD or feature brief for something on the roadmap

Skip docs that cover different product areas, archived strategies, or topics unrelated to the features being evaluated.

### Step 4: Tag sources in output
Every roadmap justification must cite the specific doc it drew from: "Per {{PRODUCT}}-strategy.md, Phase 2 prioritizes..." This creates traceability and makes it easy to re-evaluate when source docs change.

### Narrative Docs: How They Inform Roadmap
Narrative docs define how we position {{PRODUCT}} to users and the market. They affect roadmap in two ways:
- **Feature prioritization**: A feature that supports the lead narrative gets priority over one that does not. Features that reduce a documented customer tradeoff rank higher.
- **Not Doing reasoning**: If a feature contradicts the product's stated promise, the narrative document is evidence for cutting it.

## Process

### Step 1: Load Strategic Context
1. Read existing `docs/product/master-prd-roadmap.md` — start with the "Source Docs" header to know what's already been referenced
2. Read `docs/product/roadmap-prospective.md` for current state
3. Follow the "How to Find Relevant Docs" triage process to identify which strategy, competitive, and narrative docs to deep-read
4. Scan Parking Lot in `tasks-db.md` for items marked "Roadmap Idea" or "Later"

### Step 2: Build Feature Inventory
Collect every feature/initiative that has been discussed, proposed, or requested. Sources:
- Current roadmap items
- Features mentioned in strategy docs
- Competitive gaps identified in analyses
- Parking lot items
- Features from conversation history

For each feature, tag where it was first proposed (strategy doc, competitive analysis, user request, team discussion, parking lot).

### Step 3: Evaluate Each Feature
For every feature in the inventory, score against these criteria:

**Strategic Fit** (from strategy docs)
- Does this advance one of our strategic bets? Which one?
- Does this align with current phase priorities?
- Reference the specific strategy doc section.

**Competitive Signal** (from competitive analyses)
- Have competitors validated this? Which ones, with what results?
- Is this table stakes (must-have to compete) or differentiation (unique advantage)?
- Reference the specific analysis doc.

**ROI Estimate**
Score each feature on a 2x2:

| | Low Effort | High Effort |
|---|---|---|
| **High Impact** | Do first | Plan carefully |
| **Low Impact** | Fill gaps | Don't do |

Impact criteria:
- **User acquisition**: Will this bring new users? How many (order of magnitude)?
- **Retention**: Will this keep existing users? What % churn does it prevent?
- **Revenue**: Does this unlock revenue? How much (order of magnitude)?
- **Strategic positioning**: Does this create a moat or close a competitive gap?

Provide a brief ROI narrative for each: "This feature drives X because Y. Expected impact: [specific outcome]. Confidence: High/Med/Low based on [evidence]."

**Engineering LOE**
Size for current team. Be specific:
- **T-shirt size**: XS (< 1 week), S (1-2 weeks), M (2-4 weeks), L (1-2 months), XL (2+ months)
- **Who builds it**: Frontend, backend, infra, or cross-cutting?
- **Dependencies**: What needs to exist first? External blockers?
- **Opportunity cost**: What doesn't get built while this is in progress?

### Step 4: Attach Hypotheses
Every feature moving to Now or Next needs a testable hypothesis. No feature ships without a way to prove it worked or failed.

For each committed feature, write:

**Hypothesis:** We believe that [specific change] will result in [specific metric] improving by [X%] because [behavioral/market reason].

**How we'll measure:**
- Primary metric: [The one number that matters]
- Guardrail metrics: [2-3 metrics that ensure we're not breaking something else]

**What would prove us wrong:** [Specific result that falsifies the hypothesis. Not "it doesn't work." Be precise.]

**If we're wrong, it suggests:** [What we'd learn about user behavior or the market. This makes failure valuable.]

**Rules for hypotheses:**
- Must be falsifiable. "Improve engagement" is not a hypothesis.
- Primary metric must be measurable with the operator's available measurement tooling.
- Guardrail metrics prevent tunnel vision (e.g., "conversion goes up but retention drops").
- "If we're wrong" should point to a meaningful insight, not just "users don't want this."
- For Later/Maybe items, hypotheses are optional but encouraged. They sharpen thinking even before commitment.

### Step 5: Make the Call
For each feature, make a clear recommendation with reasoning:
- **On roadmap (Now/Next/Later)**: Why it earned its slot. Reference strategy alignment + ROI.
- **Not doing**: Why not. Be specific. "Low ROI relative to eng cost" or "Competitive analysis shows this isn't what users switch for" or "Doesn't advance any current strategic bet."
- **Maybe**: What evidence would move this to "on roadmap" or "not doing."

### Step 6: Categorize and Output
Categorize by:
- **Now** (this quarter)
- **Next** (next quarter)
- **Later** (future quarters)
- **Maybe** (exploring, not committed)
- **Not Doing** (decided against, with reasoning)

### Step 7: Update Files
1. Update `docs/product/master-prd-roadmap.md` with committed items (Now, Next, Later) and Not Doing
2. Update `docs/product/roadmap-prospective.md` with Maybe items and features under active evaluation
3. Remove "Roadmap Idea" items from `tasks-db.md` Parking Lot
6. Update the "Source Docs" header in `docs/product/master-prd-roadmap.md` with docs referenced this session

## Storage

Four files, each with a distinct purpose:

| File | What lives here | Who reads it |
|------|----------------|-------------|
| `docs/product/master-prd-roadmap.md` | Committed roadmap (Now/Next/Later) + Not Doing. The canonical "what are we building and why." | Everyone. This is the source of truth. |
| `docs/product/roadmap-prospective.md` | Features under consideration (Maybe). Active evaluations, open questions, pending decisions. | Product + eng leads during planning. |

### docs/product/master-prd-roadmap.md structure
```
# {{PRODUCT}} Roadmap

**Last updated**: [Date]
**Source docs**: [List of strategy, competitive, and narrative docs that informed this version]

## Active Strategic Bets
[From strategy docs — the bets this roadmap is built around]

## NOW (This Quarter)
[Committed items with justifications, ROI, LOE]

## NEXT (Next Quarter)
[Planned items with justifications, ROI, LOE]

## LATER (Future Quarters)
[Directional items with triggers for promotion]

## NOT DOING
[Cut items with evidence-based reasoning]
```

### docs/product/roadmap-prospective.md structure
```
# {{PRODUCT}} Roadmap — Under Consideration

**Last updated**: [Date]

## Active Evaluations
[Features being scored right now — strategy fit, ROI, LOE in progress]

## MAYBE
[Features we're exploring but haven't committed to]

## Pending Decisions
[Features waiting on a specific input: user data, competitor move, strategy decision]
```

## Output Format

### Strategic Context Summary

**Active strategic bets** (from strategy docs):
1. [Bet 1] — [one line]
2. [Bet 2] — [one line]

**Key competitive insights** (from analyses):
- [Insight 1 — source doc]
- [Insight 2 — source doc]

---

### NOW (This Quarter)

| Feature | Strategic Bet | ROI | LOE | Owner | Status |
|---------|--------------|-----|-----|-------|--------|
| Feature 1 | Bet it advances | Impact / Confidence | T-shirt + who | Person | In Progress |

**Justifications:**
- **Feature 1**: [2-3 sentences. Why now, what evidence supports this, what it unlocks.]

**Hypotheses:**
- **Feature 1**: We believe [change] will result in [metric] improving by [X%] because [reason].
  - Measure: [primary metric] | Guardrails: [2-3 metrics]
  - Proves us wrong if: [specific falsification]
  - If wrong, we learn: [insight about user behavior]

---

### NEXT (Next Quarter)

| Feature | Strategic Bet | ROI | LOE | Dependencies |
|---------|--------------|-----|-----|--------------|
| Feature 1 | Bet it advances | Impact / Confidence | T-shirt + who | What blocks it |

**Justifications:**
- **Feature 1**: [Why next quarter, not now. What needs to happen first.]

**Hypotheses:**
- **Feature 1**: We believe [change] will result in [metric] improving by [X%] because [reason].
  - Measure: [primary metric] | Guardrails: [2-3 metrics]
  - Proves us wrong if: [specific falsification]
  - If wrong, we learn: [insight about user behavior]

---

### LATER (Future Quarters)

| Feature | Strategic Bet | ROI | LOE | Trigger |
|---------|--------------|-----|-----|---------|
| Feature 1 | Bet it advances | Impact / Confidence | T-shirt | What would move this to Next |

---

### MAYBE (Exploring, Not Committed)

| Feature | Source | Potential ROI | LOE | What We Need to Know |
|---------|--------|--------------|-----|---------------------|
| Feature 1 | Where idea came from | Estimated impact | T-shirt | Question that determines if we commit |

---

### NOT DOING (Decided Against)

| Feature | Source | Why Not | Date |
|---------|--------|---------|------|
| Feature 1 | Where it was proposed | Specific reason with evidence | YYYY-MM-DD |

**Not Doing details:**
- **Feature 1**: [2-3 sentences. What the proposal was, why we're passing. Reference strategy misalignment, low ROI, competitive evidence, or eng cost.]

---

## ROI Framework

When estimating ROI, use this structure:

### Impact Dimensions
- **Acquisition**: New users gained. Estimate order of magnitude (10s, 100s, 1000s).
- **Retention**: Churn prevented. What % of users would leave without this?
- **Revenue**: Direct or indirect revenue. Monthly/annual estimate.
- **Moat**: Does this create switching costs, network effects, or competitive distance?
- **Urgency**: Is there a window? Competitor shipping soon? Market moment?

### Confidence Levels
- **High**: Validated by behavioral data, competitive precedent, or direct user demand
- **Medium**: Supported by strategy thesis but not directly validated
- **Low**: Speculative. Based on intuition or weak signals.

### ROI Summary Format
> **[Feature]**: [Impact dimension] impact. [One sentence on expected outcome]. Confidence: [H/M/L] based on [evidence source].

Example:
> **Enterprise integration**: Acquisition impact. Unlocks a documented customer segment that cannot adopt without it. Confidence: High based on direct research and competitive precedent.

---

## Engineering LOE Framework

### Team Context
Reference current eng team composition when sizing. Today: {{ENG_LEAD}} (eng lead) + engineering team. Update this section as team changes.

### Sizing Guide
| Size | Duration | Scope | Example |
|------|----------|-------|---------|
| XS | < 1 week | Single component, no new infra | UI tweak, config change |
| S | 1-2 weeks | One engineer, existing patterns | New screen, API integration |
| M | 2-4 weeks | Multiple components, some new patterns | New feature end-to-end |
| L | 1-2 months | Cross-cutting, new infrastructure or architecture | New subsystem or deployment model |
| XL | 2+ months | Major platform work, multiple engineers | Major platform integration or migration |

### Opportunity Cost
For L and XL items, explicitly state: "While building this, the team cannot work on [X, Y, Z]." This makes the tradeoff real.

---

## Competitive Stress Test

Run this whenever a competitor ships something, announces a feature, or the landscape shifts. Can be triggered standalone ("stress test the roadmap against X") or as part of a full roadmap review.

### Process
1. **Identify the move.** What did the competitor ship/announce? Link to source.
2. **Assess threat level.** Does this:
   - Directly compete with something on our roadmap? (Feature overlap)
   - Undercut a strategic bet we're making? (Strategy threat)
   - Create urgency for something in Later/Maybe? (Timeline pressure)
   - Invalidate our "Not Doing" reasoning? (Re-evaluation trigger)
3. **Check our position.** For each affected roadmap item:
   - Are we ahead, behind, or at parity?
   - Does our approach still differentiate, or did they close the gap?
   - Do we need to accelerate, pivot, or hold steady?
4. **Recommend action.** One of:
   - **Hold**: Our roadmap is fine. Competitor move doesn't change our calculus. Say why.
   - **Accelerate**: Move item from Later to Next or Next to Now. Say what it displaces.
   - **Pivot**: Change approach based on what competitor validated or invalidated.
   - **Add**: New item needed that wasn't on radar. Score it through the full evaluation.
   - **Cut**: Competitor owns this now, pursuing it is low-ROI. Move to Not Doing.

### Stress Test Output Format

**Competitor move**: [What happened, source, date]

| Our Roadmap Item | Threat Level | Our Position | Action | Reasoning |
|-----------------|-------------|-------------|--------|-----------|
| Feature X | High/Med/Low | Ahead/Parity/Behind | Hold/Accelerate/Pivot/Add/Cut | [Brief] |

**Net roadmap changes**: [Summary of what moved, what got added, what got cut]

**Open questions**: [Anything that needs more investigation before deciding]

### When to Run
- Competitor ships a major feature
- Competitor raises funding or announces partnerships
- Market narrative shifts (new regulation, new chain launch, macro change)
- Quarterly, as part of regular roadmap review
- When someone on the team asks "should we be worried about X?"

---

## Rules

- **Every feature needs evidence.** "Why" must reference strategy docs, competitive analysis, user data, or explicit team decision. Not vibes.
- **Every exclusion needs evidence.** "Why not" must be specific enough that someone can't re-litigate without new information.
- **ROI estimates are required.** Even rough ones. "We don't know the ROI" is a valid answer, but then justify why it's on the roadmap anyway.
- **LOE estimates are required.** T-shirt size minimum. For Now and Next items, include who builds it and what it displaces.
- **Strategy docs are the source of truth.** If a feature doesn't advance a strategic bet, it needs an exceptionally strong standalone case.
- **Competitive analyses inform, not dictate.** "Competitor X did it" is evidence, not a reason. The reason is "this validated demand in our target segment."
- **Update when strategy changes.** New strategy doc or competitive analysis should trigger a roadmap review.
- **Track all considered features.** Never silently drop a discussed feature. Move it to Not Doing with reasoning.

## When to Use This vs. Tasks

**Use Roadmap for:**
- New features that span multiple delivery cycles
- Strategic initiatives with material customer or commercial implications
- Platform work that changes core architecture or operating cost
- Major product redesigns with durable positioning tradeoffs

**Use Tasks for:**
- Tactical work with deadlines (launch prep, analytics setup, bug fixes)
- Tasks blocking people or milestones
- Work happening this week/month/quarter

**If unsure:** Can this be done in one sprint? Tasks. Will this take multiple sprints? Roadmap.

## Execution Help

After showing roadmap, I can:

- Write feature specs or PRDs for any item
- Create design briefs
- Break down features into epics/stories
- Deep-dive on ROI for a specific feature
- Re-evaluate items based on new competitive data
- Run a strategy-roadmap alignment check
- Move items between buckets with updated justification
- Archive shipped features

## Trigger

"show roadmap" / "what's on the roadmap" / "roadmap planning" / "roadmap review"
