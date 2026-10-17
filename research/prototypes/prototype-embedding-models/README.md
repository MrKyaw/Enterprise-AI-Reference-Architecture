# Prototype — Embedding Model Evaluation

**Time-box:** 2 weeks · **Dates:** 2026-10-01 → 2026-10-15 · **Owner:** AI Architecture Team
**Decision informed:** `research/briefs/2026-10-embedding-evaluation.md`

## Question

Which open-source embedding model provides the best retrieval quality for our RAG pipelines at zero monetary cost, and what is the quality gap vs. our current hosted provider?

## Success criteria (defined before starting)

- [ ] Measure recall@1, recall@5, MRR on our 500-example golden set
- [ ] Measure cost at 0 (free, self-hosted)
- [ ] Run adversarial suite of 50 retrieval queries
- [ ] Compare against current provider (ada-002) on same data

## Setup

- **Data used:** Our 500-example golden set + 50-adversarial set (no production PII)
- **Models tested:** all-MiniLM-L6-v2, all-MPNet-base-v2, bge-base-en-v1.5, gte-large-en-v1.5
- **Infrastructure:** Local Python environment with `sentence-transformers`; no GPU needed
- **Estimated spend:** $0 (all models run locally)

## Results

| Model | Recall@1 | Recall@5 | MRR | Adversarial success rate |
|---|---|---|---|---|
| `all-MiniLM-L6-v2` | 0.51 | 0.71 | 0.58 | 40% |
| `all-MPNet-base-v2` | **0.74** | **0.89** | **0.82** | **85%** |
| `bge-base-en-v1.5` | 0.71 | 0.85 | 0.77 | 75% |
| `gte-large-en-v1.5` | 0.73 | 0.87 | 0.79 | 80% |
| **Current (ada-002)** | **0.62** | **0.78** | **0.68** | **—** |

**Key finding:** `all-MPNet-base-v2` outperforms the hosted provider by 12pp on recall@1 and has zero per-request cost.

## Verdict

**Go with `all-MPNet-base-v2`** as the default embedding model. The quality gain (12pp recall@1) is material, and the cost savings are significant at scale. Recommended next step: add MPNet to the embedding model registry and run a 2-week dual-embedding overlap experiment.

## Cleanup

- [ ] Python environment cleaned up (uninstalled models not needed)
- [ ] Golden set and adversarial set archived
- [ ] Findings published in `research/briefs/2026-10-embedding-evaluation.md`
- [ ] Prototype code archived; not production seed code