# Pattern — Semantic Layer Grounding

**Status:** Proposed · **Type:** data/quality

## Context

AI systems that answer business questions against physical tables re-derive business meaning on every query — and get it wrong differently each time. Two systems computing "active customer" with different logic will disagree, and an agent will confidently present either.

## Forces

- Business definitions live in people's heads or scattered BI reports
- Text-to-SQL over raw schemas multiplies inconsistency and hallucinated joins
- Analysts and agents must not maintain parallel definitions of the same metric
- Governance needs one place where meaning, ownership, and lineage are declared

## Solution

Place a **semantic layer** — governed metrics, dimensions, entity definitions, and relationships — between all consumers (dashboards, applications, data agents) and the physical data:

1. **Single source of meaning** — metrics and dimensions defined once, versioned, reviewed, owned by data governance
2. **Agents query meaning, not tables** — the [data agent](../reference-architectures/data-agent/) resolves questions against semantic definitions; physical SQL is generated *from* the semantic layer, which owns joins and filters
3. **Policy attaches at the semantic layer** — row/column security and masking defined once; every consumer inherits them identically
4. **The same layer serves BI and AI** — dashboards and agents reconciling to the same number is what makes answers trustworthy
5. **Definitions change like code** — versioned, reviewed, with downstream evaluation impact (definition changed → [agent evaluation](../design-patterns/evaluation-in-ci.md) re-runs)

## Consequences

- ✅ Answers are auditable: "which metric definition produced this number?" has one answer
- ✅ Governance scales: control the semantic layer, control meaning everywhere
- ✅ Data agents become dramatically more reliable — they select metrics instead of inventing logic
- ⚠️ Upfront modeling investment; modeling quality is now a production concern
- ⚠️ The semantic layer becomes critical infrastructure — needs SLOs like any other component

## Known uses

- Core of the [data agent reference architecture](../reference-architectures/data-agent/)
- Feeds governed context into [copilots](../reference-architectures/copilots/) that display business metrics
