# heldout-owner-dependency

Partition: heldout. These cases are public. The held-out label separates reporting groups; it does not mean the test data is secret.

Original skill: `.claude/skills/status/SKILL.md` at `60a18dbdda4f113c325912824dc361b35a118da5`.

Prepare a status update for the review package. Reconcile ownership by latest accepted assignment, preserve unresolved dependencies, and compare prior state. A newer proposal is not an accepted reassignment; distinguish the owner of the package from the owner of its dependency.
Use the original status skill unchanged. Read relevant prior documents and all local source records. Write only cache/status/status-2026-10-28.md. Preserve the original artifact format or the honest partial stage if a gate is unresolved. Do not contact anyone or change instructions. Add a final ## Evaluation Results table with columns ID | Value | Sources; derive these row values from the records: q71-owner, q71-status, q71-dependency, q72-owner, proposed-reassignment. Sources must use the stable record IDs provided in the fixture. State missing original dependencies without fabricating replacements. The table is a bounded artifact extraction contract, not proof of host execution or business impact.

## Control labels

Positive: hand_authored_positive_control. Negative: deliberate_latest_proposal_over_accepted_assignment. The negative changes only the `q71-owner` extracted claim, so the grader must detect the violated obligation. Neither control is an observed agent outcome.

## Missing dependencies

The public source does not include `.claude/skills/utils/voice.md` or `.claude/skills/utils/sources.md`. The fixtures do not replace them. A host task that needs them stays `not_reached`. You can still calibrate the offline document checks.

## Finite body checks

The grader checks specific sections, table rows, and seeded statements before Evaluation Results. It cannot judge every possible contradiction or the quality of arbitrary prose. A correct appendix cannot make up for a missing or contradictory document body. Two hand-written negative controls keep the correct appendix while testing those body failures. They test the grader, not an agent.

## Appendix boundary regressions

Two more hand-written negative controls place a known contradictory claim after the results table or after an inline `Note: ## Evaluation Results` pseudo-heading. The real results heading must stand alone and begin the final section. Text that merely mentions the heading must not hide the rest of the document from grading. Both controls passed incorrectly before the parser-boundary fix. This is a record of that bounded parser regression, not a model-behavior result.
