# Company OS workflow evaluation scorecard

Actual model trials: **0**. Model uplift, latency and cost: **unmeasured**.

| Task | Split | Arm | Planned model trials | Actual model trials | Imported artifacts | Artifact pass / fail / not reached | Host outcome |
|---|---|---|---:|---:|---:|---|---|
| source-conflict-status | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| source-conflict-status | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| resumed-accepted-correction | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| resumed-accepted-correction | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| proposal-vs-approval-shape | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| proposal-vs-approval-shape | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| unavailable-source-recovery | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| unavailable-source-recovery | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| completion-evidence-gap | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| completion-evidence-gap | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| instruction-in-source-authority | development | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| instruction-in-source-authority | development | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| heldout-owner-dependency | heldout | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| heldout-owner-dependency | heldout | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| heldout-strategy-unsupported-claims | heldout | baseline | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |
| heldout-strategy-unsupported-claims | heldout | candidate | 0 | 0 | 0 | 0 / 0 / 0 | not_reached |

Invalid imports: **0** of **0** entries. They remain in the denominator.

## Limitations

- Finite seeded artifact checks do not assess arbitrary prose quality.
- No model or host was launched; submitted artifacts are not verified model runs.
- External actions and full agent behavior remain unknown without host traces.
- Bindings assume a trusted local operator and current suite/source files.
- Calibration controls are hand-authored, never model baseline/candidate outcomes.
