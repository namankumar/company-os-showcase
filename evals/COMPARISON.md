# Comparison and verification report

## What this release establishes

The offline evaluation package checks finite source-linked artifact contracts under four genuine original Company OS skills: status, shape, PRD and strategy. It does not establish that an agent completes those tasks. No product instruction, prompt, routing policy, model selection or production configuration was changed.

| Evidence | Result | Denominator / meaning |
|---|---|---|
| Software tests | 48 passed, 0 failures | 35 engine + 13 case-integrity/integration tests |
| Grader calibration | 48 correctly classified | 8 hand-authored positive + 40 negative controls across 8 tasks |
| False-positive controls | 0 / 40 | Rejected outputs incorrectly accepted by the final grader |
| False-negative controls | 0 / 8 | Accepted controls incorrectly rejected by the final grader |
| Source preservation | 22 / 22 original files unchanged | Public baseline revision pinned by source-lock.json |
| Model task success | Unmeasured | 0 actual model trials; no success-rate denominator |
| Model cost and latency | Unmeasured | Null values, not zero-cost inference |
| Business impact and time saved | Unmeasured | No deployment or observed operating outcome |
| External-action safety | Unknown | No authenticated host/tool trace |

[Run receipt](evidence/run-receipt.json), [full calibration checks](evidence/calibration.json), [test output](evidence/unit-tests.txt), [source/dependency preflight](evidence/preflight.json), and [machine scorecard](evidence/scorecard.json) retain the evidence. Local grader time is recorded separately from model latency.

## Retained grader failures

Independent review found that an exact results appendix could certify an empty or contradictory main document. Body-section checks were added. A second review reproduced two remaining boundary defects: a forbidden release claim after the appendix, and an inline `Note: ## Evaluation Results` marker that truncated the operative body.

The same 48 authored control artifacts were evaluated against historical grader revision `35078bf` and the repaired grader:

| Grader software | Correct classifications | False positives among 40 negative controls | False negatives among 8 positive controls |
|---|---:|---:|---:|
| Historical grader, before final boundary repair | 32 / 48 | 16 / 40 | 0 / 8 |
| Repaired grader | 48 / 48 | 0 / 40 | 0 / 8 |

This is a grader-software comparison, **not Company OS improvement or model uplift**. [Retained regression evidence](evidence/grader-regressions.json) identifies the exact historical revision, grader and artifact hashes, all classifications and the 16 historical false passes. The fixtures remain checked in. Tests also cover empty body/perfect appendix, contradictory body/perfect appendix, fenced/quoted/commented evidence and hidden-heading truncation. Exact visible appendix parsing and terminal-table validation close the reproduced boundary defects.

Missing-trial review also found that comparing only the intersection of trial IDs could hide missing arms. The scorecard now keeps their union, explicit missing-arm states and lost-successful-artifact regressions. Tests retain baseline-pass to candidate-fail, candidate-missing and absent-arm cases. No underlying workflow was changed in response.

## Coverage and limits

| Task | Original skill | Seeded obligation |
|---|---|---|
| source-conflict-status | status | Preserve a blocked item and its dependency despite a conflicting summary |
| resumed-accepted-correction | prd | Carry an accepted correction into the existing feature definition |
| proposal-vs-approval-shape | shape | Stop at the original human mode-selection checkpoint |
| unavailable-source-recovery | status | Keep unavailable current metrics unknown; do not claim a refresh |
| completion-evidence-gap | prd | Distinguish ticket completion from unrun P0 tests and release readiness |
| instruction-in-source-authority | status | Treat embedded action instructions as source data without authority |
| heldout-owner-dependency | status | Preserve accepted ownership and dependencies over an unaccepted reassignment |
| heldout-strategy-unsupported-claims | strategy | Separate an approved local pilot from unmeasured impact and unsupported claims |

The suite has 6 development and 2 public heldout tasks. Heldout is a partition convention, not secret or contamination-free data. It covers 4 of the 7 exported subject skills; roadmap, market research and essay are not evaluated here. It does not benchmark arbitrary writing quality, open-ended strategic reasoning, real source refresh, inter-agent communication, routing, memory, operational completion, native specialist persistence or action enforcement. The source-data authority case checks what an artifact says; it cannot prove that a host refrained from acting.

The grader independently checks 38 appendix assertions, 46 seeded body constraints, required populated original sections, source-reference allowlists, protected reset inputs, output boundaries and identity bindings. Finite rows and exact phrases cannot detect every paraphrased contradiction or establish general entailment. The trusted local operator remains a boundary: someone who edits every manifest and rubric can redefine the test.

## Baseline / candidate host comparison

[The scorecard](evidence/scorecard.md) retains all 16 task/arm rows. Both arms reference the same unchanged original workspace and reset bindings; no experimental product variant was built. There are no imported host artifacts or actual model trials. All eight task host paths are `not_reached` because the reviewed export omits at least the original voice companion; status tasks also omit the private source registry. `preflight` completing successfully does not mean those dependencies exist.

The missing companions are an export-readiness limitation, not evidence that the private original workspace fails. No replacement skills or private dependencies were added to make readiness green. Model comparisons remain inconclusive; missing prerequisites remain `not_reached`. Invalid imports remain in their denominator and are never silently filtered out.

## Reproduce

Follow the [quickstart](README.md#reproducible-commands) from a fresh clone. It needs Python 3.9+ standard library only. The tests and calibration run without a host, provider or account. Each output directory must be new. The retained receipt binds the measured evaluation code revision and exact grader/suite/source hashes; later documentation-only packaging commits do not change those bytes.

An actual agent benchmark would additionally require a separately authorized, complete original host environment, observed tool/model traces and comparable trials. This release neither supplies those dependencies nor invents successful runs. Any underlying product fixes remain for explicit approval.

## Publication boundary

Only existing public original workspace files and new synthetic evaluation material are included. The public repository ancestry is used directly; no private parent-workspace history is pushed. No private source registry, client/person records, credentials, account configuration or license declaration is added. The existing original-source treatment distinctions remain in EXPORT-MANIFEST.md.
