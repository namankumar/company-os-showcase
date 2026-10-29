---
name: shape
description: Give form to a fuzzy idea before committing to a PRD or strategy doc
---

# Shape

## Purpose
Take a rough idea and give it a clear enough shape to decide whether it's worth building — and what exactly to build. Output is a pitch, not a spec. The reader is you and maybe one other person. Shape is thinking. PRD is communicating.

Do not rubber-stamp the idea. The job is to find out if it's worth building, not to confirm that it is.

## Does NOT do
- Write requirements or user stories
- Produce a launch plan
- Spec the UI
- Do new research (synthesize from existing context; flag gaps)

Those belong in PRD and strategy. Shape produces the input to those skills.

## Reads (load selectively — only what's relevant to the idea)
- `docs/market-research/` — demand signals, competitive analyses, precedent
- `docs/product/master-prd-roadmap.md` — conflicts or reinforcements with existing roadmap
- `docs/strategy/` — active strategic bets this idea should serve or challenge
- `docs/gtm/` — distribution context: who we're reaching, how, what's working
- `docs/narrative/` — positioning and messaging this idea must fit or shift
- `context/current-context.md` — why now, constraints, active decisions
- `docs/feedback/` — user signal behind the idea
- `docs/product/{{PRODUCT}}-funnel.md` — funnel and product data (load if idea touches acquisition, activation, or retention)

## Writes
- `docs/product/shape-[idea-name].md`

## Trigger
"shape this idea", "let's shape", "give shape to", `/shape`

---

## Prime Directives (non-negotiable, apply to every decision)

1. Don't validate solutions. Validate problems. The solution space opens after the problem is locked.
2. A thesis that doesn't rule something out isn't a thesis.
3. Synthesize from existing context first. Flag gaps — don't go research.
4. If you can't name who has the problem and what they do today instead, the problem isn't real yet.
5. Every feature must change what users DO, not just what they CAN do.
6. Appetite is a constraint, not an estimate. "We don't know yet" is not an appetite.
7. Distribution is not separate from the feature — it's part of the shape.

---

## Priority Hierarchy (never skip these under time or context pressure)
Step 0 > Retrospective Check > Falsifiable Thesis > Why Us / Why Now > Risk Types > everything else.

---

## AskUserQuestion Protocol
One issue = one question. Never batch. Lead with your recommendation. NUMBER each issue (1, 2, 3...) and LETTER each option (A, B, C). Label with NUMBER + LETTER (e.g., "1A", "1B"). Recommended option always listed first. One sentence max per option. If a section has no issues, say so and move on — don't manufacture rigor. If the fix is obvious, state what you'll do and proceed without asking.

---

## Process

### Step 1: Take input
Ask for three things only:

1. **The raw idea** — whatever form it's in, even one sentence
2. **What prompted it** — user feedback, market signal, your own observation, a leadership ask, a competitor move
3. **Your hypothesis** — what you think should be done

Do not ask for more. Everything else is what shaping produces.

---

### Step 2: Load context
Read the relevant files from the Reads list. Only load what's relevant to this specific idea. Look for:
- Prior analyses that validate or contradict the premise
- Existing roadmap items this overlaps with or conflicts with
- User signals that confirm or complicate the problem
- Competitors who have tried this — what happened?

Surface what you found before proceeding. Flag anything that changes the premise.

---

### Step 3: Retrospective Check (mandatory)
Before shaping, check if this idea has been attempted before. Read `docs/product/` for prior pitches, specs, or shelved work on similar ideas.

If found: what happened? What rabbit holes did it hit? Were the same problems present?

Recurring attempts at the same shape without learning from prior attempts is a signal the idea has a structural problem. Flag it explicitly.

---

### Step 4: Step 0 — Nuclear Challenge (mandatory)

Challenge the premise before shaping anything.

1. **Is this the right problem?** Could a different framing yield a simpler or more impactful solution?
2. **Who has this problem?** How do they solve it today? What does it cost them?
3. **What breaks if we don't build this?** Real pain or hypothetical?
4. **What does context say?** What did market research / competitive analysis / user feedback surface that confirms or complicates the hypothesis?

Map the dream state:
```
CURRENT STATE          THIS IDEA              12-MONTH IDEAL
[where we are] --->   [what this changes] --> [where we want to be]
```

Does this idea move toward the 12-month ideal or away from it?

**STOP.** Surface findings from context load + nuclear challenge. Wait for the user to respond before selecting mode.

---

### Step 5: Mode Selection (mandatory)

Present three options. State which you recommend and why in one sentence. Wait for the user to choose. Once chosen, commit fully — never drift toward a different mode in later sections.

**EXPAND** — What's the cathedral version? Scope up. What would make this 10x more valuable for 2x the effort? Shape the ambitious version. Run full depth at both 50,000ft and 5ft levels.

**HOLD** — Shape exactly what was proposed. Maximum rigor on the boundaries. Full 50,000ft + selective 5ft (only the riskiest elements).

**CUT** — What's the minimum that proves the thesis? Strip to the core. 50,000ft only — enough to decide if the stripped version is worth pursuing.

```
┌─────────────────────────────────────────────────────────┐
│                   MODE COMPARISON                       │
├──────────────────┬──────────┬──────────┬────────────────┤
│                  │ EXPAND   │ HOLD     │ CUT            │
├──────────────────┼──────────┼──────────┼────────────────┤
│ Scope            │ Push up  │ Maintain │ Push down      │
│ 50,000ft         │ Full     │ Full     │ Full           │
│ 5ft              │ Full     │ Selective│ Skip           │
│ Delight opps     │ 3+ items │ Note if  │ Skip           │
│                  │          │ seen     │                │
│ Taste calib.     │ Yes      │ No       │ No             │
│ Complexity Q     │ Big      │ Too      │ Bare           │
│                  │ enough?  │ complex? │ minimum?       │
└──────────────────┴──────────┴──────────┴────────────────┘
```

**STOP.** Wait for mode selection before proceeding.

---

### Step 6: Phase 1 — 50,000ft Strategic Validation

Run this phase fully before proceeding to 5ft. If the idea fails here, stop and surface the verdict. Don't invest 5ft thinking in an idea that doesn't survive strategic scrutiny.

**A. Jobs to be done**
What job is the user hiring this product to do in their life — not in the product, in their life? "Help me transfer money privately" is a product job. "Don't let my employer see what I'm doing with my own money" is a life job. The latter leads to better shape. Frame the problem at the life level.

**B. Falsifiable thesis**
State the core bet as: "We believe X because Y, and we'll know we're right when Z." If it doesn't rule something out, it's not a thesis. Write this before any solution work.

**C. Why Us / Why Now (dual test)**
Two separate answers, both required:
- **Why us**: What makes this defensible if a competitor builds the same thing next quarter? What do we have that they don't — distribution, data, trust, technology, positioning?
- **Why now**: What changed that makes this the right moment? What happens if we wait 3 months?

If either answer is weak, flag it explicitly before proceeding.

**D. Contrarian insight**
What does this idea assume that the market doesn't believe yet? Every defensible product is built on a belief others don't hold. If you can't state yours, the idea may not have a moat.

**E. Who loses if this succeeds?**
Every meaningful product disrupts someone. Who are we taking share from? Who has an incentive to fight back or copy this fast?

**F. Moat vs feature**
Is this a lasting advantage (compounds, hard to replicate) or table stakes (gets copied in 6 months)? Both are worth building, but the strategy and appetite differ significantly. Name which this is.

**G. Business connection**
How does this move the number — more users, higher retention, more revenue per user? If you can't connect it to a business metric, it's a nice-to-have. Also: what are we NOT building if we build this? Name the opportunity cost explicitly.

**H. Durability**
What market or technology shift would make this irrelevant? If the answer is "soon," either shape something more durable or scope it down to match the window.

**I. Leverage and compounding**
Does this create compounding value — network effects, data flywheels, retention loops? Or is it a one-time improvement that stays flat? Does this need to come before or after something else to have its full impact?

**J. Regulatory / compliance flag**
One question only: does this create legal or compliance exposure? If yes, flag before anything else.

**→ Gate**
Does the idea survive strategic validation? If yes, proceed to 5ft. If no, deliver the verdict: what failed, and what would need to change for the idea to be worth reshaping.

**STOP.** Surface findings. Wait for confirmation before proceeding to 5ft.

---

### Step 7: Phase 2 — 5ft Practical Shaping

Only run this phase if the idea passed the gate.

**A. Problem statement**
The real problem, not the surface symptom. One paragraph. Specific enough that two people would agree on whether a solution solved it. Written before any solution work.

**B. User journey**
Where does this fit in the user's flow? What do they do immediately before and after? A feature is a moment in a journey, not a standalone thing. Trace the surrounding steps — that's where friction and opportunity hide.

**C. Assumption mapping**
List every assumption the idea rests on. Rank by: most critical to the idea AND least validated. The top of that list is where the idea is most likely to break.

**D. Appetite**
How much is this worth? S (days) / M (1-2 weeks) / L (a sprint) / XL (a quarter). This is a constraint, not an estimate. State what we won't trade off to get it.

**E. Solution (rough)**
What the boundaries are. What's in, what's out. Not a spec — a sketch. Enough that a builder could react to it.

Behavior change test: does this change what users DO, or just what they CAN do? If the answer is only "they can now do X," challenge whether it solves a real need or fills a perceived gap.

**F. Interaction model**
Is the mental model familiar or novel? Familiar = lower friction, lower differentiation ceiling. Novel = higher friction, potentially higher ceiling. Name which this is and whether that's acceptable.

What does the user see in the zero state, error state, and first-time experience? A feature is only as good as its worst moment.

How many decisions does the user have to make? Every extra decision is a drop-off risk.

**G. Technical feasibility**
What's the fastest way to test the core technical assumption? Not "can we build it" in the abstract — what's the proof of concept that answers the hardest question?

What has to exist before this can exist?

**H. Distribution**
How does this get into users' hands? Is distribution built into the feature or bolted on? If it requires a separate GTM motion, flag it and load `docs/gtm/` for context on existing channels.

Acquisition loop: does this bring in new users or serve existing ones? These have different resource implications.

Adoption path: how do users discover and adopt this feature after it ships?

**I. Adversarial user**
What would stop adoption even if the idea is good? Not why users won't want it — why they'll want it but not use it. Friction, trust gaps, switching cost, habit.

**J. Downstream breakage**
What does this change or complicate in the rest of the product when it ships? Rabbit holes is about scope. This is about side effects on existing flows.

**K. Rabbit holes**
What could swallow this if we let it. What we're explicitly not solving. Name them so they don't absorb the work.

**L. Build vs buy vs partner**
Should we build this, or is there an integration or partnership that gets us there in a fraction of the time? This affects appetite significantly.

**M. Success metrics**
Define before the solution is locked. What does success look like, specifically and measurably? Metrics defined after get reverse-engineered to fit the solution.

**N. Reversibility rating**
Rate 1-5. 1 = one-way door (decide carefully, high rigor). 5 = easily reversible (decide fast, lower rigor). This should have shaped how much rigor was applied throughout.

**O. Taste calibration (EXPAND mode only)**
Identify 1-2 things in the existing product that are well-executed — use as the quality bar. Identify 1-2 anti-patterns to avoid repeating.

**P. Delight opportunities (EXPAND mode only)**
After shaping the main idea, identify 3+ adjacent quick wins (<30 min each) that would make this feature sing — things a user notices and thinks "oh nice, they thought of that." Present each as its own question: add to pitch / skip / build now.

---

### Step 8: Stakeholder Signal
Does this require leadership alignment before work starts? Does it create organizational risk or require a decision from above?

If yes, flag explicitly in the pitch. Don't let it be implicit.

---

### Step 9: Produce the Pitch

Save to `docs/product/shape-[idea-name].md`.

```markdown
# [Idea Name] — Shape Pitch

**Date:**
**Status:** Draft pitch
**Prompted by:** [user feedback / market signal / observation / leadership ask]

---

## 50,000ft

**Jobs to be done**
[What job is the user hiring this to do in their life]

**Falsifiable thesis**
We believe [X] because [Y], and we'll know we're right when [Z].

**Why us / Why now**
- Why us: [what makes this defensible]
- Why now: [what changed, what happens if we wait]

**Contrarian insight**
[What this assumes that the market doesn't believe yet]

**Moat vs feature**
[Lasting advantage / Table stakes — and why]

**Business connection**
[How this moves the number — and what we're not building if we build this]

---

## 5ft

**Problem**
[One paragraph. The real problem, not the surface symptom.]

**Assumption map**
| Assumption | Criticality | Validation status |
|------------|-------------|-------------------|
| [Assumption] | High / Med / Low | Validated / Weak / Unknown |

**Appetite**
[S / M / L / XL — and what we won't trade off to get it]

**Solution**
[What's in. What's out. Not a spec — a sketch.]

**Behavior change**
[What users will DO differently, not just what they can do]

**Rabbit holes**
[What we're explicitly not solving]

**Risks**
| Risk | Type | Severity | Mitigation |
|------|------|----------|------------|
| [Risk] | Technical / Market / Execution / Timing / Org | H/M/L | [What we do about it] |

**Open questions**
| Question | Who answers it | Deadline |
|----------|----------------|---------|
| [Question] | [Person] | [Date] |

**Stakeholder signal**
[Needs leadership alignment / Not applicable — reason]

---

## Dream state delta
```
CURRENT STATE          THIS IDEA              12-MONTH IDEAL
[where we are] --->   [what this changes] --> [where we want to be]
```
[One sentence: does this move toward the ideal or away from it, and by how much?]

## NOT in scope
Items considered during shaping and explicitly deferred:
- [Item] — [one-line rationale]

## Context that shaped this
- [Key finding from existing docs that confirmed or changed the hypothesis]

## Next step
[ ] /prd — shaped, ready to spec
[ ] /strategy — needs leadership alignment first
[ ] /market-research — needs validation before shaping further
[ ] /competitive-analysis — [specific question]
[ ] Not worth building — [why]
```

---

## Completion Summary

End every run with this table:

```
+==============================================================+
|                  SHAPE — COMPLETION SUMMARY                  |
+==============================================================+
| Retrospective check  | found X prior attempts / none        |
| Step 0 challenge     | complete / skipped                   |
| Mode selected        | EXPAND / HOLD / CUT                  |
| 50,000ft gate        | passed / failed / weak               |
| Falsifiable thesis   | written / missing                    |
| Why Us / Why Now     | answered / weak / missing            |
| Contrarian insight   | found / missing                      |
| 5ft phase            | complete / skipped (CUT mode)        |
| Assumption map       | X assumptions, X unvalidated         |
| Risks typed          | X risks, X unresolved                |
| Stakeholder signal   | flagged / not applicable             |
| Reversibility        | X/5                                  |
| Dream state delta    | written / missing                    |
| NOT in scope         | X items                              |
| Unresolved decisions | X (listed below)                     |
| Next step            | /prd / /strategy / needs research    |
+==============================================================+

Unresolved decisions: [list any AskUserQuestion that went unanswered — never silently default]
```

## Output Destination
- `docs/product/shape-[idea-name].md`
- No Google Doc unless explicitly requested
