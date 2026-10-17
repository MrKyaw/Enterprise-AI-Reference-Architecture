# ML Engineering Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns specific to building and serving machine-learning models. Applied across [ML project](../lifecycles/ml-project-lifecycle.md) and [MLOps](../lifecycles/mlops-lifecycle.md) lifecycles and the [inference reference architecture](../reference-architectures/inference/README.md).

## Training & feature patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Train/serve consistency** | Identical transformations in training and inference | Always | Reimplemented feature logic is the #1 silent quality killer |
| **Feature store** | Shared, versioned, point-in-time-correct features | Multiple models reuse features; online+offline serving | Point-in-time joins must be verified, not assumed |
| **Baseline-first** | Establish the simplest viable baseline before complexity | Always | Skipped baselines make "improvements" unmeasurable |
| **Ablation** | Remove components to attribute contribution | Feature/architecture claims | Correlated features mislead |
| **Transfer learning / fine-tuning** | Adapt a pretrained model to a task | Limited task data; domain shift | Catastrophic forgetting; evaluate base-model regressions |
| **Distillation** | Compress a large model into a smaller one | Latency/cost constraints at scale | Quality cliff on edge cases; keep the teacher for evaluation |
| **Ensembling** | Combine models for robustness | Variance reduction matters more than latency | Interpretability and serving cost |
| **Data augmentation & synthetic data** | Expand training coverage | Sparse classes/rare events | Synthetic bias; label provenance must be tracked |
| **Active learning** | Label the most informative examples | Labeling budget constrained | Feedback loops can amplify existing bias |

## Evaluation patterns (offline)

| Pattern | Intent | Watch out |
|---|---|---|
| **Held-out + out-of-time evaluation** | Estimate generalization honestly | Random splits on temporal data leak |
| **Cross-validation** | Variance-aware model selection | Not valid for grouped/time-series data without grouping |
| **Segment/subgroup analysis** | Detect harm hidden by aggregate metrics | Requires enough per-segment samples |
| **Calibration analysis** | Align predicted confidence with reality | Especially for decisions with thresholds |
| **Error analysis & slicing** | Understand *where* and *how* it fails | Aggregate metrics hide systematic failures |
| **Backtesting** | Replay historical decisions | Requires care to avoid lookahead bias |

## Deployment patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Batch scoring** | Periodic bulk predictions | Latency-tolerant, volume-heavy | Freshness windows; reprocessing on backfill |
| **Online (real-time) scoring** | Per-request predictions | Interactive experiences | Latency budgets include feature lookup |
| **Streaming scoring** | Predictions on event streams | Continuous signals | Ordering, state, backpressure |
| **Shadow deployment** | Run new model alongside old, compare, no user impact | First rollout; risky changes | Needs logging/comparison infrastructure |
| **Canary deployment** | Small traffic slice to the new model | Measurable quality signals exist | Requires enough traffic for significance |
| **A/B test / online experiment** | Randomized comparison of business impact | Capacity for statistical rigor | Metric pollution; novelty effects |
| **Champion/challenger** | Incumbent vs candidate compared continuously | Long-lived models with ground truth | Promotion criteria must be pre-registered |
| **Multi-armed bandit** | Balance exploration and exploitation | High-volume, fast feedback, low regret tolerance | Non-stationarity; auditability of allocations |
| **Logical fallback** | Deterministic path when a model is unavailable | Any decision-critical model | A fallback never tested is not a fallback |

## Serving & efficiency patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Prediction cache** | Avoid recomputation for repeated inputs | Staleness must be acceptable and bounded |
| **Embedding cache** | Reuse embeddings for unchanged content | Invalidate on embedding-model change |
| **Batch inference with microbatching** | Improve GPU utilization | Latency vs throughput trade-off |
| **Model router / cascade** | Route easy cases to cheap models, hard to strong | Requires routing-quality evaluation |
| **Quantization / pruning** | Reduce serving cost | Quality regression on edge cases |
| **Warm pools & autoscaling on queue depth** | Manage cold-start latency | Cold starts on latency-critical paths |

## Monitoring patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Input drift detection** | Notice when data distribution shifts | Needs a reference distribution and defined windows |
| **Prediction drift detection** | Notice output changes without ground truth | False positives from legitimate seasonality |
| **Delayed ground-truth tracking** | Measure real performance when labels arrive | Label latency can hide degradation for weeks |
| **Proxy metrics** | Early signals before ground truth | Only valid if proxy↔outcome correlation was verified |
| **Model quality SLO** | Alert on quality, not just uptime | Requires a sampled, automated quality check |
| **Feedback capture** | Collect corrections and outcomes for retraining | Consent and classification apply to feedback data |

## Anti-patterns

- Feature engineering duplicated between training and serving
- Promoted models with no pre-registered comparison criteria
- Drift dashboards with no retraining trigger wired to them
- A/B tests run until significance appears, in either direction
- Fallback paths never exercised in a failure drill
- Model quality measured only in the notebook
