# Sample Company OS instructions

This is a fictional, file-based operating workspace. It is an input to a Codex or Claude Code host, not an autonomous service.

Before drafting or changing an operating brief:

1. Read `context/company.md`, `context/priorities.md`, and `context/decision-boundaries.md`.
2. Read the relevant original notes in `sources/`.
3. Read existing documents in `docs/` before replacing them.
4. Follow `.agents/skills/operating-brief/SKILL.md`.

Rules:

- Keep facts, inferences, recommendations, and accepted decisions visibly separate.
- Cite factual claims with `sources/path.md#Lx-Ly` references.
- Use `unknown` when the sources do not establish a claim.
- Do not send messages, access external services, change customer data, schedule work, or mark a decision accepted without a direct human instruction.
- A source link is evidence navigation, not proof that an inference is correct.

`scripts/check_source_links.py` checks link shape and local existence only. It does not verify semantics, authority, freshness outside this workspace, or model quality.
