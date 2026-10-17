# Pattern — Evaluation in CI

**Status:** Proposed · **Type:** quality

## Context

AI systems regress silently: a chunking change, model update, or prompt tweak can degrade quality with no failing test. Traditional unit tests don't measure answer quality, retrieval relevance, or faithfulness.

## Forces

- Quality is a spectrum, not pass/fail — thresholds must be explicit
- Full evaluation suites are slow and expensive; PR gates need fast feedback
- Golden sets rot as the domain changes

## Solution

Maintain versioned evaluation datasets alongside the system and run tiered evaluation in CI:

1. **PR gate (fast, < 5 min)** — small representative golden set; hard thresholds on core metrics (e.g., retrieval hit-rate, faithfulness, task success)
2. **Nightly (full)** — complete golden set plus adversarial/red-team prompts; trend dashboards
3. **Pre-release** — held-out human review sample; comparison against current production baseline

Every dataset entry carries: input, expected properties (not brittle exact strings), origin, and review date. Datasets are refreshed on a scheduled cadence and whenever production failures reveal gaps.

## Consequences

- ✅ Quality regressions block deployment with the same friction as failing tests
- ✅ Model/provider upgrades become measurable decisions, not leaps of faith
- ⚠️ Requires ongoing ownership — assign a curator per golden set
- ⚠️ Threshold tuning is empirical; expect a calibration period

## Known uses

- Required by the [RAG](../reference-architectures/rag/README.md) and [fine-tuning](../reference-architectures/fine-tuning/README.md) reference architectures
