---
name: status
description: Track workstream status across projects, dependencies, blockers, escalations
---

# Status Skill

## Purpose

Track the live status of every item across every workstream in a project. Scans configured work-tracker, conversation, document, and call-note snapshots to build an item-level status view. Each item's status is reconciled across multiple sources (an issue might be "in progress" in the tracker but "blocked" in a conversation). Output is usable for leadership updates, parallel-workstream visibility, and early detection of stalls and dependencies.

## Reads
- `sources/README.md` — public configuration boundary; check configured snapshot freshness before a source read
- `context/cadences.md` — sprint cycles, deadlines (for milestone mapping and timeline context)
- `context/okr-status.md` — OKR targets (flag when status changes affect KR progress)
- `cache/status/status-*.md` — prior status snapshot (diff against most recent; optional)
- `context/current-context.md` — {{YOUR_NAME}}'s decision-making context, interpretive notes across workstreams
- `context/meeting-notes.md` — optional meeting extractions when maintained by the operator
- `docs/product/master-prd-roadmap.md` — master PRD and roadmap (on-demand, for milestone mapping)

## Writes
- `cache/status/status-[YYYY-MM-DD].md` — the status snapshot for today
- All cache files owned by status (see `.claude/skills/utils/sources.md` registry)

**{{YOUR_NAME}}'s context is the lens.** Raw data from sources is necessary but not sufficient. {{YOUR_NAME}}'s inline notes provide the interpretive layer: why something matters, what the real priority is, what the politics are behind a blocker. Always read `context/current-context.md` before interpreting signals.

## Core Concepts

### Projects
A project is a product or initiative with its own set of workstreams. Each project gets its own status file.

Current projects:
- **{{PRODUCT}}** — `cache/status/status-[YYYY-MM-DD].md`

### Workstreams
A workstream is a functional area that ships work toward the project. Workstreams are dynamic: they can split, merge, or go dormant based on what's actually happening.

**Starting workstreams for {{PRODUCT}}:**

| Workstream | What it covers | Key people | Primary source |
|---|---|---|---|
| Product delivery | Product work, defects, infrastructure, integrations | {{ENG_LEAD}}, delivery team | Configured work tracker |
| Design | UX, UI, flows, design system, prototypes | {{DESIGNER}} | Configured work tracker and discussion snapshot |
| Go-to-market | Launch, website, content, customer communication | {{GTM_LEAD}}, GTM team | Configured document and conversation snapshots |
| Partnerships | External integration and commercial work | {{PARTNERSHIPS_LEAD}}, partnerships team | Configured document and conversation snapshots |
| Legal & compliance | Terms, policy, compliance, licensing | {{LEGAL_OWNER}} | Configured document and conversation snapshots |
| Quality | Testing, triage, feedback loops | {{QA_LEAD}}, quality team | Configured work tracker and discussion snapshot |
| Measurement | Product and business measurement | {{ANALYTICS_OWNER}}, delivery team | Configured metrics snapshot |

If a scan reveals activity that doesn't fit these, create a new workstream. If a workstream has had zero activity for 2+ weeks, mark it dormant.

### Items
An item is a discrete unit of work. It could be a tracker issue, a planning-board item, a commitment from a conversation, or an action item from a call. Every item gets tracked individually.

Each item has:
- **ID**: tracker issue ID, planning-board item ID, or a generated slug for conversation/call items (e.g., `conversation-policy-review`)
- **Title**: what it is
- **Owner**: who's responsible
- **Workstream**: which workstream it belongs to
- **Status**: the reconciled status across all sources
- **Sources**: where this item appears and what each source says

### Multi-Source Reconciliation

An item can appear in multiple places. When sources disagree, apply these rules:

| Scenario | Resolution |
|---|---|
| Work tracker says "In Progress", conversation says "blocked on X" | Status = **Blocked**. The newer source is more current. Flag the discrepancy. |
| System of record says "Done", no contrary evidence | Status = **Done** (trust system of record unless contradicted) |
| Conversation commitment with no tracker issue | Status = **Untracked**. Create a tracking entry. Flag it. |
| Work tracker says "In Progress", no activity for 5+ days | Status = **Stale**. Flag it. |
| Call notes say "agreed to do X", no issue created | Status = **Untracked commitment**. Highest priority to flag. |

**The real status is the worst-case across sources.** If any source says blocked, it's blocked until proven otherwise.

### Dependencies
A dependency is when item A or workstream A is blocked by or waiting on item B, workstream B, or an external party. Track at both item level and workstream level.

## Process

### Step 1: Load Prior State

Read the most recent `cache/status/status-*.md`. This is the baseline. Everything in this run is a diff against it.

### Step 2: Scan Sources

Refresh configured stale snapshots according to the operator's private source registry. For each source owned by this workflow, check freshness and scan if stale using the host's parallel-work protocol. Each worker writes only its configured snapshot and returns a status message (success/error/stuck). Do NOT have workers return full data to the main conversation.

Snapshot classes to check:
- work tracker and delivery snapshot
- conversation and document snapshot
- customer-signal snapshot
- product and business metrics snapshot

Also read `context/current-context.md` for {{YOUR_NAME}}'s interpretive notes and, when present, `context/meeting-notes.md` for recent meeting extractions. These are local files, not host-backed sources.

If a source is unavailable, note it and continue.

### Step 3: Build Item Registry

Merge all items from all sources into a single registry. For each item:

```
| ID | Title | Workstream | Owner | Status | Sources | Last updated | Depends on | Blocks |
```

**Status values:**
- `Done` — shipped/completed, confirmed by source
- `In Progress` — actively being worked
- `Blocked` — waiting on something, can't proceed
- `Stale` — in progress but no activity for 5+ days
- `Untracked` — commitment or work spotted in a conversation/call with no tracker issue
- `At Risk` — timeline or resource concern flagged

**Reconciliation pass:** For items appearing in multiple sources, apply the reconciliation rules above. Log any discrepancies.

### Step 4: Build Workstream Snapshots

Roll up items into workstream-level views:

```
### [Workstream Name]

**Status:** 🟢 On Track | 🟡 At Risk | 🔴 Blocked | ⚪ Dormant
**Owner:** [person]
**Source of record:** [configured system of record]
**Last activity:** [date, source]

**Items:**
| ID | Title | Owner | Status | Last updated | Notes |
|---|---|---|---|---|---|

**Blocked items:**
- [item] — blocked by [what/who] — since [date]

**Untracked commitments:**
- [commitment from conversation/call] — [who said it] — [date]

**Dependencies:**
- Waiting on [workstream/external] for [what] — since [date]
- [workstream/external] waiting on us for [what] — since [date]
```

Workstream status is derived from its items:
- 🟢 All items progressing, no blockers
- 🟡 Some items stale or at risk, or unresolved dependencies
- 🔴 Any item blocked with no path forward
- ⚪ No items, no activity

### Step 5: Build Dependency Map

Cross-cutting view of all dependencies (item-to-item and workstream-to-workstream):

```
## Dependency Map

### Item Dependencies
| Item | Depends on | Owner of dependency | Status | Since |
|---|---|---|---|---|

### Workstream Dependencies
| From | Waiting on | For what | Status | Since |
|---|---|---|---|---|
```

Mark dependencies as:
- 🟢 **Resolved** — delivered, unblocked
- 🟡 **In progress** — being worked, ETA known
- 🔴 **Stalled** — no visible progress, needs escalation
- ⚪ **New** — just identified this scan

### Step 6: Diff Against Prior State

Compare current snapshot to the prior `cache/status/status-*.md`:
- Items that changed status (what moved, what regressed)
- New items (from any source)
- Items that disappeared (completed, dropped, dormant)
- Items that haven't moved (same state 2+ scans)
- Dependencies that resolved or newly appeared
- Source discrepancies (system of record says X, conversation says Y)

### Step 7: Write Output

Save to `cache/status/status-[YYYY-MM-DD].md`.

## Output Format

```markdown
# {{PRODUCT}} Status — [Date]

**Last updated:** [timestamp]
**Sources scanned:** Work tracker ✓/✗, delivery ✓/✗, conversations ✓/✗, documents ✓/✗, customer signals ✓/✗, metrics ✓/✗

## Summary

[3-5 sentences. Overall state. What moved, what's stuck, what needs attention. Written for someone who reads only this paragraph.]

## Workstreams

[One block per active workstream. Concise summary format:]

### [Workstream Name] — 🟢/🟡/🔴/⚪

- [What shipped or progressed]
- [What's blocked and by whom]
- [What's next]

---

## Escalations

- [What] — [why it's stuck] — [suggested action]

## Dependencies

| From | Waiting on | What | Days |
|---|---|---|---|

## Changes Since Last Status
- 🟢 [item that shipped/unblocked]
- 🔴 [item that regressed/stalled]
- 🆕 [new item/dependency/workstream]
- ⚠️ [source discrepancy: "system of record says X, conversation says Y"]

## Item Details

[Full workstream item tables — one per active workstream, using Step 4 format]

### [Workstream Name]

**Items:**
| ID | Title | Owner | Status | Last updated | Notes |
|---|---|---|---|---|---|

**Blocked items:**
- [item] — blocked by [what/who] — since [date]

## Design

**Status:** 🟢/🟡/🔴

| Item | Status | Priority | Sprint | Updated |
|---|---|---|---|---|

**In review / decision needed:**
- [item] — [context]

**Handed to eng (design done, eng building):**
- [item] — [eng owner if known]

**Require Design (eng waiting on design):**
- [item] — [sprint] — [priority]

## Customer signals

**Open:** [count] | **Closed (7d):** [count] | **Bot-replied:** [count] | **Human-replied:** [count]
**Avg time to first reply:** [duration]

**Top issue themes:**
| Theme | Count | Sample conversation | Status |
|---|---|---|---|

**Needs attention:**
- [Conversations open 3+ days with no admin reply]

## Untracked Commitments

| Commitment | Who said it | Where | Date | Suggested action |
|---|---|---|---|---|

## Source Discrepancies

| Item | Source A says | Source B says | Suggested resolution |
|---|---|---|---|

## Stale Items

| Item | Workstream | Owner | Last update | Days stale |
|---|---|---|---|---|
```

## Rules

- **Every claim traces to a source.** Don't say "engineering is on track" without citing specific tracker or conversation evidence.
- **Track items, not vibes.** Each item has an ID, owner, status, and source. If you can't name the item, it's not tracked.
- **Reconcile across sources.** An item's real status is the worst-case across all sources where it appears. If a tracker says "in progress" but a conversation says "blocked," it's blocked.
- **Untracked commitments are the highest-priority flag.** Someone said "I'll do X" in a conversation or call and there is no issue for it. These are the things that get dropped.
- **Dependencies are the second-highest-value output.** Catching that one workstream is waiting on another without shared visibility is the actual value.
- **Don't pad.** If a workstream has nothing to report, mark it dormant. No filler.
- **Workstreams are dynamic.** Split, merge, or mark dormant based on actual activity.
- **Status colors are derived, not assigned.** Green/yellow/red comes from the items, not a gut feeling.
- **Diff is mandatory.** Always compare against prior daily status. The value is in what changed.
- **One file per day.** If `cache/status/status-[YYYY-MM-DD].md` already exists, update it in place. Don't create a new file. Add an `## Updated [HH:MM]` section at the top with what changed so {{YOUR_NAME}} can see the diff at a glance.

## Trigger

`/status`, "status update", "project status", "workstream status", "what's the status of {{PRODUCT}}"
