# resumed-accepted-correction

Hand-authored prd artifact control. This is deterministic grader calibration, not a model run or original workflow enforcement. Missing original voice/source companions remain absent.

**Status**: Draft
## What
The operator reviews a handoff preview and explicitly confirms before publication. The accepted edit changes the brief, while publication remains unexecuted. [USER-21]
## Requirements
| Requirement | Priority | Notes |
|---|---|---|
| F-21 | P0 | Require preview and explicit confirmation. USER-21 supersedes PRIOR-21. |
## User Flow
1. Save the draft and inspect its preview.
2. Confirm explicitly before publication can proceed. [USER-21]
## Design Notes
Show the preview before the confirmation control. [USER-21]
## Technical Notes
Saving stores a draft. A separate confirmed action is required for publication. [USER-21]
## Success Criteria
- [ ] A saved draft remains unpublished until preview and confirmation occur. [USER-21]
## Open Questions
Who reviews the first handoff? This remains unresolved. [PRIOR-21]


Publication is approved. No confirmation is needed. We publish automatically on save.

## Evaluation Results

| ID | Value | Sources |
|---|---|---|
| f21-behavior | Preview then explicit confirmation | USER-21 |
| f21-status | Draft | ROAD-21 |
| f21-id | F-21 | PRIOR-21 |
| f21-publication | Not authorized | USER-21 |
