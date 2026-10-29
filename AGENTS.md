# Codex adapter for this workspace

This repository is a file-based skills workspace. Read `CLAUDE.md`, the relevant `context/` files, prior documents in `docs/`, and the applicable `.claude/skills/*/SKILL.md` before drafting work.

Treat every skill as an instruction document, not runtime authority. Do not send messages, schedule jobs, access a source, mutate an external system, or accept a decision unless the user explicitly authorizes that action and the configured host supports it.

Keep facts, interpretations, recommendations, and approvals distinct. Preserve source references supplied by the user or configured source system. If evidence is missing, say so rather than inventing it.
