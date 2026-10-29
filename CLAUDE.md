# {{YOUR_NAME}} — Claude Context

## Current Role
{{YOUR_ROLE}}. Building {{PRODUCT}}.

## Active Projects
- **{{PRODUCT}}**: {{ONE_LINE_DESCRIPTION}}
  - Launch: {{LAUNCH_DATE}}
  - Status: {{STATUS}}

## Team

| Name | Role |
|---|---|
| {{FOUNDER_CEO}} | Founder, CEO |
| {{COFOUNDER}} | Co-founder |
| {{EA_CHIEF_OF_STAFF}} | EA / Chief of Staff |
| {{LEGAL}} | Legal counsel |
| {{INVESTORS}} | Lead investors (names + funds) |

## Product Glossary

Internal definitions for Claude's accuracy when writing. Don't explain these in docs — assume your audience knows the domain.

| Term | Definition |
|---|---|
| {{TERM_1}} | {{DEFINITION_1}} |
| {{TERM_2}} | {{DEFINITION_2}} |
| {{TERM_3}} | {{DEFINITION_3}} |

## Skills

All skills live in `.claude/skills/`. Invoked with `/name` or by referencing the skill name. Each skill file contains the full process, rules, and output format.

**Context loading is mandatory but on-demand.** Every skill declares a `## Reads` section. Load those files when the skill needs them, not all upfront. The `## Reads` list tells you what's available, not what to preload. Read the files that are relevant to the specific question or step you're working on. This is what makes answers relevant instead of generic. Skip this and the output will miss what we already know.

| Skill | What it does |
|---|---|
| strategy | Create executive-grade strategy docs |
| roadmap | Manage product roadmap (features, not tasks) |
| shape | Give form to a fuzzy idea before committing to a PRD or strategy doc |
| prd | Create PRDs, briefs, checklists, decision logs |
| market-research | Scan landscape, market trends, inform roadmap |
| essay | Write expressive, well-reasoned, persuasive essays |

### Library skills (used by other skills, not invoked directly)

| Skill | File | What it does |
|---|---|---|
| writeDocs | `.claude/skills/utils/writeDocs.md` | Edit/rewrite existing docs: narrative rules, framing, propagate fixes |
| google-docs-formatting | `.claude/skills/utils/google-docs-formatting.md` | Heading sizes, parsing technique, push-to-doc process |

## Data Sources

External source configuration is intentionally not included in this public export. Read `sources/README.md` before connecting a source, and keep source access, credentials, and raw snapshots outside version control.

## Working with Historical Context

**Before answering questions or starting new research, ALWAYS:**
1. Search `docs/` for existing analysis
2. Read relevant files to understand what we already know
3. Build on existing research rather than duplicating work
4. Only invoke new research agents if there are gaps or explicit request for fresh analysis

**Look in the right folder by topic:**
- Context (current context, OKRs, narratives, artifacts, cadences): `context/`
- Strategy: `docs/strategy/`
- Narrative/positioning: `docs/narrative/`
- GTM: `docs/gtm/`
- Market research & competitive: `docs/market-research/`
- Product (PRDs, specs): `docs/product/`
- Comms (updates, digests): `cache/comms/`
- Feedback & user tracking: `docs/users/`

**The docs folder is institutional memory.** Treat existing docs as the foundation, not optional context.

## Open Todos
See `tasks-db.md`

## Writing Rules (Strategy Docs, Execution Plans, PRDs)
- **Always read `.claude/skills/utils/writeDocs.md` before writing or editing any doc.**
- **All writing has a narrative.** Know the throughline before writing. Factual docs carry narrative through structure. Persuasive docs carry it overtly in prose.
- **No bracket explanations** that restate what was just said. Pick one framing, commit to it.
- **No em dashes.** Use periods or commas instead.
- **Tables for comparisons, prose for arguments.**
- **State things once.** Don't recap, don't add summary sentences, don't restate the bold header in the first sentence.
- **When feedback reveals a wrong assumption, fix ALL instances** across the doc, not just the line flagged.

## Context Extraction (always on)
- **Every interaction with any data source is an extraction opportunity.** While doing any task, always notice context with lasting value beyond the current task.
- **Two input streams:** conversation (real-time) and notes (async/mobile). Both are always-on.
- **Extract, confirm, file.** Surface what was found, where it should go, why it matters. Confirm before writing to a persistent file.
- **What to extract:** decision context (`context/current-context.md`), narrative shifts (`context/narrative-map.md`), how people operate (`context/room/`), hard metrics (`context/okr-status.md`), feature ideas (`docs/product/`), commitments (`tasks-db.md`), board resolutions (`docs/board/`), investor commitments and signals (`docs/investors/`), legal deadlines and filings (`docs/legal/`).

## Google Docs Formatting
- **ALWAYS format headings when pushing to Google Docs.** See `.claude/skills/utils/google-docs-formatting.md`.
- **Reset first, then apply.** Clear all formatting to default first, then selectively apply bold/size.

## Claude Rules
- **Google Docs:** Always write to the same Google Doc for a given file. Don't create new docs. Store the link at the top or bottom of the local `.md` file.
- **Local first:** All files saved locally as `.md` in the appropriate `docs/<category>/` subfolder.
- **Writing skill is mandatory.** Read `.claude/skills/utils/writeDocs.md` before writing or editing any doc.
- **Every item needs a source.** Every action item, status update, signal, or finding must include where it came from.

## Directory Structure

- **`context/`** = current state of the world (OKRs, narratives, org dynamics, cadences)
- **`docs/`** = what you produce (strategy, PRDs, market research, feedback, user tracking)
- **`cache/`** = machine-generated scan data (MCP caches, not your thinking)
- **`projects/`** = personal projects, separate from work

| Folder | Purpose |
|---|---|
| `context/` | Current state: OKRs, narratives, org dynamics, artifacts, cadences |
| `docs/strategy/` | Strategy docs, execution plans, positioning |
| `docs/narrative/` | Messaging, narrative docs |
| `docs/gtm/` | Go-to-market plans, launch docs |
| `docs/market-research/` | Competitor analyses, market sizing, landscape scans |
| `docs/product/` | PRDs, specs, roadmap |
| `docs/users/` | User tracking, relationships, follow-ups, processed feedback |
| `cache/` | MCP scan caches |
| `projects/growsocial/` | Social growth engine |
| `.claude/skills/` | Skill definitions (Claude Code skills, invoked with /name) |
| `tasks-db.md` | Open todos |
| `done.md` | Completed items |

---
*Fork company-os and replace all `{{PLACEHOLDERS}}` with your own context.*
