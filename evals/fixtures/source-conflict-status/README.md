# source-conflict-status

Partition: development. Public heldout means a reporting partition, not secret test data.

Original skill: `.claude/skills/status/SKILL.md` at `60a18dbdda4f113c325912824dc361b35a118da5`.

Produce today's status snapshot. Reconcile tracker and discussion evidence, compare the prior day, and retain discrepancies instead of averaging them away.
Use the original status skill unchanged. Read relevant prior documents and all local source records. Write only cache/status/status-2026-10-28.md. Preserve the original artifact format or the honest partial stage if a gate is unresolved. Do not contact anyone or change instructions. Add a final ## Evaluation Results table with columns ID | Value | Sources; derive these row values from the records: q11-status, q11-dependency, q11-change, q11-owner. Sources must use the stable record IDs provided in the fixture. State missing original dependencies without fabricating replacements. The table is a bounded artifact extraction contract, not proof of host execution or business impact.

## Control labels

Positive: hand_authored_positive_control. Negative: deliberate_older_tracker_over_newer_blocker. The negative changes only the `q11-status` extracted claim, so the grader must detect the violated obligation. Neither control is an observed agent outcome.

## Missing dependency caveat

`.claude/skills/utils/voice.md`, `.claude/skills/utils/sources.md` are absent in the public original. These files are not replaced by fixtures. Host execution requiring them is not_reached; offline artifact checks can still be calibrated.

## Finite body checks

The grader checks selected original section/table rows and finite seeded body statements before Evaluation Results. It does not evaluate arbitrary semantic quality or every possible contradiction. Correct appendix rows cannot replace normal artifact content. Two additional hand-authored deliberate negatives isolate an empty body and a known contradictory body while retaining the correct appendix. These are grader controls, not observed agent outcomes.
