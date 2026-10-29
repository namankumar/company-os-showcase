---
name: operating-brief
description: Prepare a bounded, source-linked operating brief from the local sample workspace.
---

# Operating brief

## Reads

- `context/company.md`
- `context/priorities.md`
- `context/decision-boundaries.md`
- relevant files in `sources/`
- existing `docs/operating-brief.md` and `docs/proposed-decision.md`

## Output contract

Prepare or refresh `docs/operating-brief.md` with these sections:

1. What changed
2. What needs a decision
3. Proposed follow-through
4. Known unknowns
5. Sources

Use source references in the form `sources/path.md#Lx-Ly` for factual claims. Keep these labels distinct:

- **Observed:** directly established by a source.
- **Inference:** a bounded interpretation of cited facts.
- **Proposed:** a recommendation requiring human review.
- **Accepted:** only a direct human approval recorded in the workspace can use this label.

## Guardrails

- Do not fabricate facts, freshness, approval, customer outcomes, or model execution results.
- Do not make external calls, send messages, schedule work, or change an external system.
- Do not change a proposal to accepted without an explicit human decision source.
- If evidence is missing, state the question rather than filling the gap.
