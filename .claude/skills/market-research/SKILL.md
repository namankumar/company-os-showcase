---
name: market-research
description: Scan landscape, market trends, inform roadmap
---

# Strategic Radar

## Purpose
Scan the competitive landscape, market trends, and ecosystem developments to inform roadmap priorities and strategic positioning.

## Reads
- `docs/market-research/` — current landscape
- `docs/strategy/` — our position
- `docs/product/master-prd-roadmap.md` — master PRD and roadmap (source of truth)

## Writes
- `docs/market-research/` — new intel
- `docs/market-research/` — strategic notes

## When to Use This vs. Analyze-Protocol
- **Strategic radar**: Broad periodic scan. 'What just happened in the market?' Run monthly or when you hear noise.
- **Analyze-protocol**: Deep dive on one entity. "Tell me everything about [company]." Run when you need a thorough analysis.

## Input Sources
1. **Web Search**: Competitor announcements, market news, relevant technical developments
2. **Social and community channels**: Influencers, competitor accounts, practitioner discussion
3. **Competitor Products**: Direct alternatives and adjacent solutions
4. **Industry Reports**: Relevant analyst, investor, and category reports
5. **Ecosystem Updates**: Relevant platforms, standards, and regulation
6. **Internal Analytics**: Available behavioral data for user signals
7. **Feedback Engine Output**: What users are asking for

## Process
1. Scan for relevant developments:
   - Competitor launches/features
   - Regulatory changes relevant to the product category
   - Technology shifts (ZK, MPC, cross-chain)
   - Market movements and adoption trends
2. Assess relevance to {{PRODUCT}}
3. Categorize by timeframe:
   - 🔴 Immediate (respond now)
   - 🟠 Near-term (next 30 days)
   - 🟡 Medium-term (next quarter)
   - ⚪ Long-term (6+ months)
4. Identify opportunities and threats
5. Recommend roadmap adjustments

## Output Format

### Strategic Radar — [Date]

#### Executive Summary
[2-3 sentences on what matters most right now]

#### Immediate Attention
| Signal | Source | Impact | Recommended Action |
|--------|--------|--------|-------------------|
| | | High/Med/Low | |

#### Competitive Landscape
| Competitor | Recent Move | Our Position | Gap/Opportunity |
|------------|-------------|--------------|-----------------|
| Railgun | | | |
| [Other] | | | |

#### Market & Regulatory
- [Trend 1]: [Implication for {{PRODUCT}}]
- [Trend 2]: [Implication for {{PRODUCT}}]

#### Opportunities
- [Opportunity 1] — Timeframe: [X] — Effort: [Low/Med/High]

#### Threats
- [Threat 1] — Likelihood: [X] — Mitigation: [Y]

#### Roadmap Recommendations
- [ ] [Suggested addition/change] — Priority: [X]

## Output Destinations
- Obsidian: `docs/market-research/[date].md`
- Google Doc: Strategic planning doc
- Team channel: Summary to leadership (if significant)

## Trigger
"run market-research" or "scan landscape" or "what's happening in the market"
