# Implementation boundary

## Included and implemented

- A portable file layout for context, original notes, output documents, and skills.
- Explicit instructions for a Codex or Claude Code host to prepare a brief.
- A deterministic local checker for `sources/...#Lx-Ly` references in `docs/`.
- A fictional worked brief and decision record that distinguish evidence from a proposal.

## Deliberately not included

- Model execution, evaluation, or quality scoring.
- External source connectors, authentication, schedules, notifications, or message sending.
- A database, multi-user collaboration, permissions service, or production audit trail.
- Automatic decision acceptance, operational changes, or autonomous follow-through.

The skill instructions influence a capable host. They are not runtime enforcement. Any production system would need independently implemented identity, authorization, source freshness, effect controls, and verification.
