# Architecture

```mermaid
flowchart LR
    S[Primary notes in sources/] --> H[Codex or Claude Code host]
    C[Human-maintained context/] --> H
    K[Operating-brief skill] --> H
    H --> B[Draft brief in docs/]
    B --> L[Source-link checker]
    L --> R[Human review]
    R -->|accept or reject| D[Decision record]
    D -->|human-maintained update| C
```

The host reads a bounded workspace and prepares a source-linked draft. The deterministic checker verifies local source references. A human remains responsible for acceptance, external action, and updating durable context.

The arrows are a working method, not a runtime service. There is no connector, scheduler, permission service, database, or autonomous execution loop in this repository.
