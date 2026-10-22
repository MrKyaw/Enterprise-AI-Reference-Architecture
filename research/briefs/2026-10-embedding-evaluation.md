# Research Plan — Embedding Model Evaluation

**Status:** Proposed evaluation plan · **Owner:** Assign before execution · **Last reviewed:** 2026-10-22

**Related plan:** [Embedding evaluation prototype](../prototypes/prototype-embedding-models/README.md)

## Decision to inform

Determine whether a candidate embedding model improves retrieval for an authorized domain corpus at an acceptable total operating cost. Include the existing retrieval solution as a baseline. No model, provider, or hosting approach is approved by this plan.

## Evidence status

No runnable experiment, authorized corpus, raw measurements, or reproducibility manifest accompanies this brief. Earlier text presented illustrative scores, expenses, and a model-selection recommendation as completed findings. Those unsupported claims have been removed from the current document. No customer system, internal dataset, or measured result is represented here.

## Experiment design

1. Name the business/retrieval owner, data owner, security reviewer, and decision-maker.
2. Define the task, corpus classification, permissions, freshness requirements, and expected load.
3. Create a versioned, authorized relevance set with independent labels and representative difficult queries. Keep restricted data outside the public repository.
4. Select candidate models after checking licensing, language/domain suitability, deployment constraints, and evaluation feasibility. Record exact revisions and configuration.
5. Keep chunking, corpus, ACL filtering, index settings, and query set controlled when comparing embeddings. Record any deliberately varied factor.
6. Measure recall at agreed cutoffs, MRR/nDCG as appropriate, unauthorized retrieval rate, end-to-end latency, errors, and total cost.
7. Repeat measurements with documented hardware, batch size, concurrency, warm/cold conditions, test duration, and uncertainty.
8. Present the trade-off to the owners with a proceed/change/stop recommendation grounded in the recorded evidence.

## Cost model

Self-hosting has compute, storage, operational, evaluation, and maintenance costs even when no per-request provider fee applies. Record the measurement period, currency, utilization, hardware assumptions, support effort, and migration costs before making a comparison.

## Acceptance and decision record

Set criteria before running the experiment. Do not fill a results table with invented examples that could be mistaken for measurements.

| Criterion | Target | Actual evidence | Decision owner |
|---|---|---|---|
| Retrieval quality by relevant slice | To agree | Not measured | To assign |
| Authorization/filter correctness | To agree | Not tested | To assign |
| End-to-end latency and errors | To agree | Not measured | To assign |
| Total run and support cost | To agree | Not measured | To assign |
| Migration and rollback feasibility | To agree | Not demonstrated | To assign |

Publish only approved, sanitized findings. Record the chosen option in an [ADR](../../adr/0000-template.md), with limitations and conditions that would reopen the decision. Follow the [technology evaluation criteria](../../docs/technology-evaluation-criteria.md) before proposing a standards change.
