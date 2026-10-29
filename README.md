# Company OS, a source-linked operating workspace

Most company context lives in meetings, metrics, decisions, and half-finished documents. The practical problem is not producing another summary. It is carrying the right context into the next decision, showing where each claim came from, and leaving a durable record of what changed.

This is a small, fictional workspace that demonstrates that operating pattern. It contains:

- stable context about a sample business;
- two primary-source notes;
- a host-run briefing skill;
- a worked brief and proposed decision with line-level source links; and
- a deterministic checker for those links.

It is designed for an existing Codex or Claude Code host. It has no model backend, connector, scheduler, or autonomy layer. The model is asked to read and write local files; the source-link checker only verifies that cited local paths and line ranges exist. It does not evaluate reasoning or make the brief trustworthy on its own.

## What the example shows

The worked brief notices that a launch target and a repeated onboarding failure share the same constrained workflow. It keeps the evidence, the recommendation, and the decision status separate:

1. evidence stays in `sources/`;
2. the brief identifies a risk and proposed follow-through;
3. the decision log records a recommendation as **proposed**, not accepted; and
4. a person must explicitly update the decision before it changes the workspace's operating context.

That distinction is the point. The workspace makes it easier to resume a decision with its evidence; it does not grant an AI permission to decide or act.

## Run it with an existing host

No setup beyond a local Codex or Claude Code installation is required.

### Codex

From this directory, start Codex and use this prompt:

```text
Read AGENTS.md, context/, sources/, and docs/. Follow .agents/skills/operating-brief/SKILL.md.
Refresh docs/operating-brief.md without inventing facts. Preserve or add line-level source links.
Do not send messages, change external systems, or mark a proposed decision accepted.
```

### Claude Code

From this directory, start Claude Code and use the same prompt. `CLAUDE.md` points it to the equivalent skill in `.claude/skills/operating-brief/`.

```sh
claude
```

The expected result is a revised local Markdown brief. Review it before accepting any recommendation.

## Check the sample's source links

```sh
python3 scripts/check_source_links.py
```

The checker validates only that every `sources/...#Lx-Ly` reference inside `docs/` resolves to an existing local file and line range. It is deliberately deterministic and does not call a model.

## Workspace map

```text
context/     Current, human-maintained orientation and decision boundaries
sources/     Primary notes used as evidence in this sample
docs/        Source-linked briefs and decision records
.agents/     Codex-oriented skill instructions
.claude/     Claude Code-oriented skill instructions
scripts/     Deterministic source-link validation only
```

See [the architecture](docs/architecture.md) and [the implementation boundary](docs/implementation-boundary.md).

## Provenance

This public-safe sample was distilled from existing company-context and operating-brief workflows. It uses fresh fictional material rather than copying any private repository, source connection, client workflow, person, organization, metric, or credential.
