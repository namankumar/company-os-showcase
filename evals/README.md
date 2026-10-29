# Company OS workflow evaluation

This evaluation package loads the original Company OS skills and controlled company files, prepares reset workspaces, and independently checks produced Markdown artifacts. It is not a company-automation runtime, model simulator or replacement set of showcase skills.

## Evidence layers
1. Deterministic software checks: reset/binding checks and graders behave as tested.
2. Host/model task outcomes: an actual configured host follows the original skill. No model trials were authorized or performed for this release.
3. Operational impact: company outcomes, time saved and adoption remain unmeasured.

Hand-authored positive/negative controls are grader calibration, never agent success rates. Skills guide a host; only the configured host enforces tool/action restrictions.

## System map
~~~mermaid
flowchart TD
    A[Original skills and templates at pinned revision] --> B[Dependency and source preflight]
    C[Synthetic company files and prior artifacts] --> D[New isolated reset workspace]
    B --> D
    D --> E[Task prompt and source/config/reset hashes]
    E -. separately authorized host .-> F[Actual artifact and host evidence]
    G[Hand-authored calibration controls] --> H[Independent bounded artifact grader]
    F --> H
    H --> I[Calibration report and baseline/candidate scorecard]
    I --> J[Pass / fail / inconclusive / not reached]
~~~

The CLI never invokes a model, follows fixture instructions, accesses connectors, starts agents, sends messages or changes Company OS behavior.

## Dependency closure
Offline checks need Python 3.9+ and the standard library only. No install, server, API key, model download or account is needed.

Task manifests bind the original adapter, workspace instructions, skill and writing utilities. The reviewed source omits some companions:
- .claude/skills/utils/voice.md is referenced by writing instructions but absent.
- The private .claude/skills/utils/sources.md registry is absent; no source-refresh capability is implied.
- Host tools, real connectors, permissions and model identity are not supplied.

Synthetic context and snapshots are task data, not invented companion skills. Preflight preserves missing prerequisites as not reached instead of altering instructions. A separately authorized operator can later select a complete existing original workspace; no dependency or product update is performed here.

## Reproducible commands
Run from the repository root after cloning. These commands make only local evaluation outputs; they never launch a model or connector.

```sh
python3 --version
python3 -m unittest discover -s evals/tests -v
eval_workdir="$(python3 -c 'from pathlib import Path; import tempfile; print(Path(tempfile.mkdtemp(prefix="company-os-eval-")).resolve())')"
python3 evals/company_os_eval.py preflight > "$eval_workdir/preflight.json"
python3 evals/company_os_eval.py calibrate --out "$eval_workdir/calibration" > "$eval_workdir/calibration-summary.json"
python3 evals/company_os_eval.py scorecard --out "$eval_workdir/scorecard" > "$eval_workdir/scorecard-summary.json"
cat "$eval_workdir/scorecard/scorecard.md"
```

`preflight` confirms source bindings and reports dependency gaps. A zero exit means that assessment completed, not that host execution is ready. `calibrate` returns nonzero if any known control is misclassified. `scorecard` without imported runs shows all task/arm rows as unrun, with no model comparison.

To prepare one reset workspace without running its task:

```sh
python3 evals/company_os_eval.py prepare --task source-conflict-status --arm baseline --trial 1 --out "$eval_workdir/manual-baseline"
```

The new directory contains `manifest.json` and `workspace/`. Inspect the manifest and missing prerequisites before authorizing a configured host. After an operator produces the task's artifact, use `grade --run "$eval_workdir/manual-baseline"`. An absent artifact returns `not_reached` with exit 1. Do not put result files inside the run directory: its metadata and protected workspace inventory are checked. Import multiple run directories with `scorecard --runs PARENT --out NEW_DIR`. New output directories must not exist beforehand. Paths must use real, resolved ancestors; the quickstart resolves the macOS temporary-directory alias for that reason. Each arm/trial retains its identity; missing arms, invalid imports and lost successful artifacts remain visible.

No host launcher or model-trace importer is included. Even an imported passing artifact does not certify a model run or absence of external effects.

## Task and artifact contract
Cases cover source conflict, resumed correction, proposal versus approval, source/tool unavailability, completion evidence, instruction text inside source data, owner/dependency conflict and unsupported strategy claims.

Each task invokes an existing original skill. The task asks for its normal local Markdown artifact plus a bounded Evaluation Results table for seeded-state checks. That exact heading must be the last section, containing only its three-column table. The independent grader reads actual bytes, evaluates finite source-linked assertions and checks protected inputs/output paths. An artifact's self-reported passed flag is not proof.

Exact seeded-state/citation checks do not establish arbitrary factual entailment, executive writing quality or open-ended strategy quality. Those need independent human/model assessment. Outside-workspace effects cannot be proven absent from an artifact alone.

## Baseline and candidate
Both arms bind original source and identical reset inputs. Neither changes product prompts, runtime, routing, retrieval, models or tools. No experimental product variant is implemented.

Unrun trials have null success/cost/latency and a reason. Missing dependencies are not model failures. Artifact failures, invalid runs, missing observations and unrun cases remain distinct; comparison is inconclusive without actual comparable host trials.

## Heldout cases
The development/heldout split reserves cases from product/prompt tuning. Public heldout data is a partition convention, not secret data or contamination-free measurement. No tuning/training occurs. Future independent evaluation may require additional hidden tasks.

## Provenance and export boundary
See source-lock.json, tasks.json and COMPARISON.md. Original instructions/templates remain byte-bound to the existing reviewed source. No private source paths/registry, real company/client/user data, account details, credentials or paid-run receipts are published. Existing license/IP terms are unchanged; no new license is added.

Evaluation-driven product changes are on hold. Original-workspace failures are reported; only evaluation package defects may be fixed.
