# Research Brief — Embedding Model Evaluation

**Date:** 2026-10-17 · **Author:** AI Architecture Team · **Status:** Published
**Prototype:** `research/prototypes/prototype-embedding-models/`

## Executive summary

We evaluated 5 embedding models (3 open-source, 2 hosted) on our enterprise document retrieval golden set. The top open-source model (`all-MPNet-base-v2`) surpassed the hosted provider's default model by 12% hit-rate at 30% lower cost. **Recommendation:** adopt `all-MPNet-base-v2` with our custom fine-tuning on domain terminology, and discontinue the hosted model for new workloads.

## Question

Should we switch the embedding model used in our RAG pipelines from the current hosted provider (`text-embedding-ada-002`) to an open-source alternative, and what is the total cost of ownership impact?

## Background

- Current provider: hosted text-embedding-ada-002
- Annual embedding cost (current): ~$42,000 at projected 10M requests/month
- Retrieval quality directly impacts answer quality in our RAG pipelines
- Last model evaluation: 14 months ago, before new document types were added

## What we tested

| Model | Provider | Cost per 1K embeds | Hit-rate @k=10 | Notes |
|---|---|---|---|---|
| `text-embedding-ada-002` | Hosted | $0.10 | 0.62 | Default hosted model; good generalist |
| `all-MiniLM-L6-v2` | Open-source | $0.00 | 0.51 | Smallest; fast but lower quality |
| `all-MPNet-base-v2` | Open-source | $0.00 | 0.74 | Good quality/size balance |
| `bge-base-en-v1.5` | Open-source | $0.00 | 0.71 | Strong performance; MIT license |
| `gte-large-en-v1.5` | Open-source | $0.00 | 0.73 | Largest; slower but best quality |

**Evaluation method:** 
- Golden set: 500 Q→relevant-chunks→expected-answer pairs
- Adversarial set: 50 queries designed to frustrate retrieval (negation, complex negation, domain jargon)
- Metric: recall@1, recall@5, mean reciprocal rank
- All tests run on our own data, not vendor benchmarks

## Results

| Metric | Current (ada-002) | Best open-source (MPNet) | Delta |
|---|---|---|---|
| Recall@1 | 0.62 | 0.74 | +12pp |
| Recall@5 | 0.78 | 0.89 | +11pp |
| MRR | 0.68 | 0.82 | +14pp |
| Cost per 1K | $0.10 | $0.00 | N/A (own infra) |

**Adversarial set findings:** 
- `ada-002` fails on negation queries (e.g., "What documents discuss *not* implementing X?)
- `MPNet` handles negation correctly; `bge-base` has similar strength

## Recommendation

**Adopt `all-MPNet-base-v2`** as the default embedding model for all new RAG workloads.

- **Cost savings:** ~$30,000/annual (based on projected volume), since inference runs on our infrastructure
- **Quality gain:** +12% recall@1, which translates to fewer escalation requests from knowledge workers
- **Risk:** Requires re-indexing existing vectors (one-time cost estimated at 20 engineer-hours)
- **Mitigation:** Run dual-embedding during a 2-week overlap period; route 10% of traffic to MPNet, monitor quality, then full switch

## Adoption path

1. **Week 1-2:** Add MPNet to embedding model registry; run dual-embedding experiment
2. **Week 3-4:** Evaluate quality on held-out golden set; if recall@1 ≥ 0.70, proceed
3. **Week 5:** Migrate all new RAG workloads to MPNet
4. **Week 6-8:** Re-index existing corpora; decommission ada-002 embeddings
5. **Week 9:** Full cutover; monitor for 2 weeks; rollback if regression

## What would change our mind

- If a future hosted model matches MPNet's quality at ≤$0.02 per 1K with no ingestion latency, reconsider
- If re-indexing proves to corrupt >5% of existing retrieved results, revert to ada-002

## Cross-cutting review

| Team | Reviewer | Date | Outcome |
|---|---|---|---|
| Enterprise Architecture | | | |
| Cloud Platform | | | |
| Data | | | |
| Cybersecurity | | | |

## Related

- [RAG lifecycle](../../lifecycles/rag-lifecycle.md)
- [Evaluation lifecycle](../../lifecycles/evaluation-lifecycle.md)
- [RAG patterns](../../design-patterns/rag-patterns.md) — especially the embedding model selection guidance
- [Production issues — retrieval and data](../../production-issues/retrieval-and-data.md) — Q-01, Q-03, R-01, R-05