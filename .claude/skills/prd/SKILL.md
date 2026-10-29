---
name: prd
description: Create PRDs, briefs, checklists, decision logs
---

# Product Artifacts

## Purpose
Create product documentation and artifacts. Everything a product lead needs: PRDs, feature briefs, design handoffs, launch checklists, strategy docs, decision logs, and tracking artifacts.

## Reads
- `context/room/<group-name>.md` — room analysis from read-room skill (for alignment docs, release notes, and any artifact with a stakeholder audience)
- `docs/strategy/` — strategic context
- `docs/market-research/` — landscape
- `docs/narrative/` — positioning
- `docs/product/master-prd-roadmap.md` — master PRD (source of truth for {{PRODUCT}})
- `docs/product/` — existing specs
- `docs/feedback/` — user pain points, quotes, feature requests

## Writes
- `docs/product/` — PRDs, feature briefs, design briefs, use cases

## Process
1. Identify artifact type from the list below
2. Gather requirements and context from conversation, existing docs in `docs/`, and any linked references
3. Use the matching template. Fill in what's known, flag what's missing as open questions.
4. Apply `.claude/skills/utils/writeDocs.md` rules before finalizing. Every artifact goes through the writing skill.
5. Save to `docs/{{PRODUCT}}-<topic>.md`

## Trigger
"create PRD for [feature]", "write ticket for [task]", "feature brief for [X]", "launch checklist for [X]", "let's shape", "run prd", `/prd`

## Artifact Types

| Tier      | Artifact                       | When to Use                                                          |
| --------- | ------------------------------ | -------------------------------------------------------------------- |
| Core      | PRD                            | New product area or major feature requiring eng + design alignment   |
| Core      | Feature Brief                  | Smaller feature, doesn't need full PRD weight                        |
| Core      | Design Brief                   | Handing off to design. User flows, requirements, edge cases          |
| Core      | Source of Truth                | Living reference doc for a product area (e.g., {{PRODUCT}} Operating Model) |
| Execution | Launch Checklist               | Go/no-go criteria before shipping                                    |
| Execution | Testing Checklist              | QA scenarios, edge cases, regression                                 |
| Execution | Release Notes                  | Post-launch comms for users or stakeholders                          |
| Strategy  | Strategy Doc                   | Multi-month plan with phases, workstreams, milestones                |
| Strategy  | Alignment Doc                  | Cross-team alignment on goals, dependencies, owners                  |
| Strategy  | Decision Log                   | Record why we chose X over Y                                         |
| Tracking  | Competitive Positioning Matrix | Feature comparison table against competitors                         |
| Tracking  | Shipped Archive                | What deployed, when, what metrics moved                              |

---

## Tier 1: Core Product Artifacts

### PRD (Product Requirements Document)

For new product areas or major features that need eng + design + leadership alignment. Overkill for small features (use Feature Brief instead).

```markdown
# [Feature Name] — PRD

**Author**: {{YOUR_NAME}}
**Date**: [Date]
**Status**: Draft / In Review / Approved
**Audience**: Engineering, Design, Leadership

## Background
The strategic "why now." Not internal scheduling (eng estimates, phase labels, sprint details). Cover: what's broken or missing, who feels the pain, what they do today instead, and what forces make this urgent now (market shifts, competitive moves, user requests, migration deadlines). The reader should understand urgency from this section alone.

Every factual claim needs a source, a link, or a qualifier. If you can't cite it, don't state it as fact.

## Goal
What we're trying to achieve. Be specific about the outcome, not the output. What changes for the user or the business when this ships.

## Measure of Success
One north star metric stated as a bold sentence. Supporting metrics and counter metrics below.

**North star:** [The one metric that defines success. Bold, specific, measurable.]

Supporting metrics:
- [Metric that indicates health]
- [Metric that indicates health]

Counter metrics (flags if we're gaming the north star):
- [Metric that should NOT degrade]

## User Stories
User stories are the backbone of the PRD. Each story is a self-contained unit with its own requirements, flow, design considerations, technical considerations, and edge cases. No standalone Design, Technical, or Edge Cases sections.

Reference structure: see `docs/product/halliday-prd.md` for the format.

### [N]. [Short title]

**As a [user type], I want [goal] so that [benefit].**

- Requirements: [What must be true for this story to be complete]
- Flow:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

#### Design Considerations

1. [Design detail, UX pattern, or edge case with expected behavior]
2. [Design detail]

#### Technical Considerations

1. [API endpoint, data source, or implementation detail]
2. [Technical detail]

## Open Questions
- [Question — who needs to answer it]

## Appendix
Reference material that supports the PRD but isn't core to the decision: competitive tables, protocol mechanics, research data.
```

---

### Feature Brief

Lighter than a PRD. For features where scope is clear and you mostly need to align eng on what to build.

```markdown
# [Feature Name] — Feature Brief

**Author**: {{YOUR_NAME}}
**Date**: [Date]
**Status**: Draft / In Review / Approved

## What
One paragraph. What are we building and why.

## Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| [Requirement] | P0 / P1 / P2 | |

## User Flow
Step-by-step for the primary flow. Keep it tight.

1. User does [X]
2. System responds with [Y]
3. Edge case: [Z happens], system [handles it by...]

## Design Notes
What the UI should do. Link Figma if available, otherwise describe layout and interactions.

## Technical Notes
Anything eng needs to know: API changes, new endpoints, data model changes, dependencies.

## Success Criteria
How we know this shipped correctly. Specific, measurable.
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Open Questions
- [ ] [Question]
```

---

### Design Brief

Handoff to design. Contains everything a designer needs to start without a kickoff meeting.

```markdown
# [Feature Name] — Design Brief

**Author**: {{YOUR_NAME}}
**Date**: [Date]
**Status**: Draft / Ready for Design / In Design

## Context
What this feature does and why we're building it. Link to PRD or Feature Brief if one exists.

## User Flows

### Flow 1: [Name]
1. **Entry point**: Where the user starts (e.g., sidebar, settings, notification)
2. **Steps**: Walk through the flow
3. **Exit**: Where the user ends up
4. **Error states**: What can go wrong and what the user should see

### Flow 2: [Name]
[Same structure]

## Requirements for Design
| Requirement | Type | Notes |
|-------------|------|-------|
| [Requirement] | Must have / Nice to have | |

## Edge Cases & Empty States
| State | What the User Sees | Notes |
|-------|-------------------|-------|
| Empty state (no data) | [Description] | |
| Error state | [Description] | |
| Loading state | [Description] | |
| [Other edge case] | [Description] | |

## Constraints
- Platform constraints (small-screen viewport, embedded surface, etc.)
- Existing patterns to follow or break from
- Accessibility requirements

## Design Principles Check
Which design principles are most relevant to this feature? For each, note how the design honors it or why it doesn't apply.

| Principle | Relevant? | How this design honors it |
|-----------|-----------|--------------------------|
| [Principle name] | Yes / No | [Specific design choice] |

Flag any principle the design intentionally violates, with reasoning.

## References
- [Link to existing UI / Figma for context]
- [Competitor reference if relevant]
- [Related PRD or Feature Brief]
```

---

### Source of Truth

Living reference doc for a product area. Gets updated as decisions are made. The canonical answer to "how does X work in our product."

```markdown
# [Product Area] — Source of Truth

**Owner**: {{YOUR_NAME}}
**Last Updated**: [Date]
**Status**: Active

## Overview
What this product area is, what it covers, and its role in the broader product.

## Current State
How it works today. Be precise enough that a new team member could understand the system.

## Key Decisions
| Decision | Date | Rationale | Alternatives Considered |
|----------|------|-----------|------------------------|
| [Decision] | [Date] | [Why] | [What else we looked at] |

## Architecture / Model
How the pieces fit together. Diagrams welcome, but a clear bulleted breakdown works too.

## Rules & Constraints
Hard rules this area operates under. Things that should never change without explicit discussion.
- [Rule 1]
- [Rule 2]

## Open Items
- [ ] [Thing that's unresolved or needs revisiting]

## Changelog
| Date | Change | Reason |
|------|--------|--------|
| [Date] | [What changed] | [Why] |
```

---

## Tier 2: Execution Artifacts

### Launch Checklist

Go/no-go criteria before shipping. Run through this before every launch. If any P0 item is red, don't ship.

```markdown
# [Feature/Release] — Launch Checklist

**Target Date**: [Date]
**Owner**: {{YOUR_NAME}}
**Status**: Pre-launch / Go / No-Go

## Go/No-Go Criteria
| Criteria | Status | Owner | Notes |
|----------|--------|-------|-------|
| Core functionality tested on [platform] | :red_circle: / :yellow_circle: / :green_circle: | [Name] | |
| Edge cases covered | :red_circle: / :yellow_circle: / :green_circle: | [Name] | |
| Performance acceptable | :red_circle: / :yellow_circle: / :green_circle: | [Name] | |
| Error handling in place | :red_circle: / :yellow_circle: / :green_circle: | [Name] | |
| Analytics/monitoring live | :red_circle: / :yellow_circle: / :green_circle: | [Name] | |

## Pre-Launch
- [ ] Feature flags configured
- [ ] Staging tested end-to-end
- [ ] Rollback plan documented
- [ ] Support team briefed (if user-facing)
- [ ] Release notes drafted

## Launch Day
- [ ] Deploy to production
- [ ] Smoke test core flows
- [ ] Monitor error rates for [X] minutes
- [ ] Confirm analytics firing
- [ ] Announce internally

## Post-Launch (24-48h)
- [ ] Review error logs
- [ ] Check key metrics against targets
- [ ] Collect initial user feedback
- [ ] Document issues found
- [ ] Retrospective scheduled (if warranted)

## Rollback Plan
**Trigger**: [What condition triggers rollback]
**Steps**:
1. [Step 1]
2. [Step 2]
**Owner**: [Who executes rollback]
```

---

### Testing Checklist

QA scenarios for a feature. Covers happy path, edge cases, and regression.

```markdown
# [Feature] — Testing Checklist

**Tester**: [Name]
**Date**: [Date]
**Build/Version**: [Version]

## Setup
- [ ] [Environment prerequisite]
- [ ] [Test data required]
- [ ] [Account state needed]

## Core Flows
| # | Scenario | Steps | Expected Result | Pass/Fail | Notes |
|---|----------|-------|-----------------|-----------|-------|
| 1 | [Happy path] | [Steps] | [Expected] | | |
| 2 | [Alternate path] | [Steps] | [Expected] | | |

## Edge Cases
| # | Scenario | Expected Result | Pass/Fail | Notes |
|---|----------|-----------------|-----------|-------|
| 1 | [Edge case] | [Expected] | | |

## Error Handling
| # | Scenario | Expected Error | Pass/Fail | Notes |
|---|----------|----------------|-----------|-------|
| 1 | [Error condition] | [Expected message/behavior] | | |

## Regression
- [ ] [Existing feature 1 still works]
- [ ] [Existing feature 2 still works]

## Platform-Specific
| Platform | Tested | Issues |
|----------|--------|--------|
| Embedded surface | | |
| [Other] | | |

## Blockers Found
| Issue | Severity | Ticket | Status |
|-------|----------|--------|--------|
| [Issue] | P0 / P1 / P2 | [Link] | |
```

---

### Release Notes

Post-launch communication. Adapt tone for audience: internal team, users, or stakeholders.

```markdown
# [Release Name] — Release Notes

**Version**: [Version]
**Date**: [Date]
**Audience**: Internal / Users / Stakeholders

## What's New
- **[Feature 1]**: [One sentence on what it does and why it matters]
- **[Feature 2]**: [One sentence]

## Improvements
- [Improvement 1]
- [Improvement 2]

## Fixes
- [Bug fix 1]
- [Bug fix 2]

## Known Issues
- [Issue still open, with workaround if available]

## What's Next
[One or two sentences on what's coming. No promises, just direction.]
```

---

## Tier 3: Strategy & Alignment Artifacts

### Strategy Doc

Multi-month product strategy. Phases, workstreams, milestones, success criteria. This is the format behind the 6-month plans.

```markdown
# [Strategy Name]

**Author**: {{YOUR_NAME}}
**Date**: [Date]
**Status**: Draft / Active / Archived
**Timeframe**: [Start] to [End]

## Thesis
The core bet in 2-3 sentences. What we believe, what we're building toward, and why now.

## Current Position
Where we are today. What's working, what's not, and what's changed since the last strategy.

## Phases

### Phase 1: [Name] — [Timeframe]
**Goal**: [What this phase achieves]

| Workstream | Deliverables | Owner | Status |
|------------|-------------|-------|--------|
| [Workstream] | [What ships] | [Person] | Not started / In progress / Done |

**Exit Criteria**: [How we know Phase 1 is done]

### Phase 2: [Name] — [Timeframe]
[Same structure]

### Phase 3: [Name] — [Timeframe]
[Same structure]

## Milestones
| Milestone | Date | Phase | Dependency |
|-----------|------|-------|------------|
| [Milestone] | [Date] | [Phase #] | [What it depends on] |

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk] | High / Med / Low | High / Med / Low | [What we do about it] |

## Success Metrics
| Metric | Baseline | 3-Month Target | 6-Month Target |
|--------|----------|----------------|----------------|
| [Metric] | [Current] | [Target] | [Target] |

## Open Questions
- [ ] [Question]
```

---

### Alignment Doc

For cross-team alignment. When multiple teams or stakeholders need to agree on goals, dependencies, and who owns what. Load relevant room files for each stakeholder's current positions and what framing works for them.

```markdown
# [Initiative] — Alignment Doc

**Author**: {{YOUR_NAME}}
**Date**: [Date]
**Status**: Draft / Aligned / Needs Discussion
**Teams Involved**: [Team 1, Team 2, ...]

## Objective
What we're trying to accomplish together. One paragraph.

## Shared Goals
| Goal | Owner | Success Criteria | Timeline |
|------|-------|-----------------|----------|
| [Goal] | [Team/Person] | [How we measure] | [When] |

## Dependencies
| Team A Needs | From Team B | By When | Status |
|-------------|-------------|---------|--------|
| [What's needed] | [Who provides it] | [Date] | Blocked / On Track / Done |

## Division of Responsibility
| Area | Owner | Notes |
|------|-------|-------|
| [Area] | [Team/Person] | |

## Decisions Needed
| Decision | Options | Recommendation | Decided By | Deadline |
|----------|---------|----------------|------------|----------|
| [Decision] | [A, B, C] | [Recommendation] | [Person] | [Date] |

## Communication Plan
- **Sync cadence**: [Weekly / Biweekly / As needed]
- **Channel**: [team channel / meeting / document comments]
- **Escalation path**: [Who to ping if blocked]

## Open Questions
- [ ] [Question — who needs to answer]
```

---

### Decision Log

Record of product decisions. Indexed by date. The answer to "why did we do it this way?"

```markdown
# Decision Log — [Product Area]

**Owner**: {{YOUR_NAME}}
**Last Updated**: [Date]

## How to Use
Add new decisions at the top. Include context, options considered, and rationale. Link to related docs where relevant.

---

### [YYYY-MM-DD] [Decision Title]

**Context**: What prompted this decision.

**Options Considered**:
| Option | Pros | Cons |
|--------|------|------|
| [Option A] | [Pros] | [Cons] |
| [Option B] | [Pros] | [Cons] |

**Decision**: [What we chose]

**Rationale**: [Why. Be specific enough that future-you understands the tradeoff.]

**Impact**: [What this affects downstream]

**Revisit If**: [Under what conditions we'd reconsider]

---
```

---

## Tier 4: Tracking Artifacts

### Competitive Positioning Matrix

Feature comparison against competitors. Keep it updated as the landscape shifts.

```markdown
# Competitive Positioning — [Category]

**Last Updated**: [Date]
**Owner**: {{YOUR_NAME}}

## Positioning Summary
One paragraph on where we sit in the landscape and our key differentiator.

## Feature Comparison

| Feature | {{PRODUCT}} | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|---------|--------|----------------|----------------|----------------|
| [Feature 1] | [Status/Detail] | [Status/Detail] | [Status/Detail] | [Status/Detail] |
| [Feature 2] | | | | |
| [Feature 3] | | | | |

**Legend**: Full support, Partial, None, Planned

## Where We Win
- [Advantage 1]: [Why it matters to our users]
- [Advantage 2]: [Why it matters]

## Where We Lose
- [Gap 1]: [How we address or when we'll close it]
- [Gap 2]: [How we address it]

## Moves to Watch
| Competitor | Signal | Impact on Us | Response |
|-----------|--------|-------------|----------|
| [Competitor] | [What they did/announced] | [How it affects us] | [Our move] |
```

---

### Shipped Archive

Record of what shipped, when, and what happened. Institutional memory for "what did we actually deliver?"

```markdown
# Shipped Archive — [Product Area]

**Owner**: {{YOUR_NAME}}
**Last Updated**: [Date]

## How to Use
Add new entries at the top after each release. Include what shipped, key metrics if available, and any follow-up needed.

---

### [YYYY-MM-DD] [Release/Feature Name]

**What Shipped**: [Brief description of what went live]

**Key Changes**:
- [Change 1]
- [Change 2]

**Metrics** (first 7 days):
| Metric | Before | After | Notes |
|--------|--------|-------|-------|
| [Metric] | [Value] | [Value] | |

**Issues Found Post-Launch**:
- [Issue 1 — resolved/open]

**Follow-Up**:
- [ ] [Action item]

---
```

---

## Rules

### Writing
- Every artifact goes through `.claude/skills/utils/writeDocs.md` rules before finalizing. No exceptions.
- Write full sentences in descriptions and rationale fields. No fragments or placeholder-style text.
- Primary audience is engineering and leadership. Write so both can read it without translation.
- Tables for structured data and comparisons. Prose for arguments and context.
- State things once. Don't restate the header in the first sentence.
- No em dashes. Periods or commas.
- Flag open questions explicitly.

### PRD-specific rules (from staking PRD session, 2026-03-26)
- **Background = strategic "why now."** No internal scheduling (eng estimates, phase labels, sprint details). Cover: status quo, who the users are, why they'd care, and what forces make this urgent. The reader should understand urgency from this section alone.
- **Verify everything.** For protocol mechanics, read the source code. For competitive claims, verify with primary sources. For data claims, cite or cut. No unsourced assertions stated as fact.
- **User stories are the backbone.** Design considerations, technical considerations, and edge cases all live under the relevant user story as h4 subsections (numbered lists), not in standalone sections. Reference: `docs/product/halliday-prd.md` for the format.
- **One north star metric.** Measure of Success states one north star as a bold sentence. Supporting metrics and counter metrics (flags if you're gaming the north star) below it. Not a table of equal-weight metrics.
- **Cut what doesn't earn its place.** Stakeholders, launch plan, and standalone edge cases tables are not required. Include only if they add information the reader needs. The PRD gets better each time something is cut.
- **Source code is the source of truth for protocol features.** Read it before speculating about what the chain supports. Don't list features the protocol doesn't have.

## Output Destinations
- **Local file**: `docs/{{PRODUCT}}-<topic>.md` (always)
- **Google Doc**: PRDs, Strategy Docs, Alignment Docs (write locally first, sync to Doc)
- **Work tracker**: Tickets (extract from PRD/Feature Brief requirements)
- **Team channel**: Release Notes (adapt format for channel post)
