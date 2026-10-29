# Doc Editor / Rewriter

## Purpose
Edit and rewrite strategy docs, execution plans, and PRDs. Tighten language, fix framing, remove LLM patterns. The output should read like a product lead wrote it.

## Reads
- `context/room/<group-name>.md` — room analysis from read-room skill (load when editing docs that reference group dynamics, stakeholder positions, or audience framing)
- `docs/` — all subdirectories, for context when editing

## Writes
- Edits in place (same file being edited)

## Trigger
"edit this doc", "rewrite this section", "tighten this up", "make this sound human", `/write`

## Narrative First

All writing has an embedded narrative. Even a PRD tells a story: why this feature, why now, why this shape. A status update frames where we are and what matters next. Before writing, know the narrative. What's the throughline the reader should walk away with?

The difference between doc types is how you carry that narrative:

**Factual docs** (PRDs, specs, roadmap items, status updates): The narrative is structural. It lives in what you choose to include, how you sequence it, what gets emphasis. The prose itself stays precise and clean. Let the structure do the arguing.

**Persuasive docs** (strategy, narrative, positioning, pitches): The narrative is overt. Every sentence builds toward the message. Use idioms and metaphors to make the point land. Present with weight, never hype. No shock value unless the situation genuinely calls for it. Confident and direct.

Most docs lean one way. Some have both (a PRD with a "Why Now" section). Match the approach to the section, but always know the narrative.

**Connective tissue:** A line of context between sections can reframe what just landed and set up what's next. Each paragraph should flow from the one before. The reader should never wonder "why are we talking about this now?"

**Bad news needs context.** Frame limitations with the insight that makes them make sense. Context can come before, after, or both.

## Process

### Step 1: Read the Doc
Read the doc (or section) the user points to. If no specific section is given, read the whole thing.

### Step 2: Pull Context
Search `docs/` for related prior docs. Prior docs often have stronger framing, better arguments, or competitor tables that should be pulled into the current doc. Use the strongest version of every argument.

### Step 3: Identify Problems
Flag what's weak. Apply all rules from `.claude/skills/utils/voice.md` (LLM voice, redundancy, rhythm, generic writing, formatting). Then check for domain-specific issues:

**Wrong framing**
- Privacy as an add-on. {{PRODUCT}} replaces failing OpSec. Privacy is the core need.
- Speed as the value prop. The real problem is effort. Convenience > speed.
- Assuming non-crypto-native users. All {{PRODUCT}} users are crypto natives. Don't explain bridges, DeFi, or how wallets work.
- Yield as a differentiator. Yield is table stakes. It gets us in the room. Privacy is why they stay.

**Defensive context**
- Current State explaining strategy decisions (that belongs in Strategy section)
- Preempting objections that later sections already handle
- "That's intentional" disclaimers

### Step 4: Rewrite
Make the edits. Show what changed and why — keep it brief.

- Apply all formatting rules from `.claude/skills/utils/voice.md`.
- When the user's feedback reveals a wrong assumption, find and fix ALL instances across the doc — not just the line they flagged.

### Step 5: Propagate
After any rewrite, scan the rest of the doc for the same issue. If "casual users" got cut from one paragraph but still appears in three others, fix all of them.

## Output Destination
- Edit in place (same file)
- Never write directly to Google Drive/Docs
