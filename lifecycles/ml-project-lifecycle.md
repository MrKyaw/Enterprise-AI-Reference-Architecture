# ML Project Lifecycle

**Status:** Proposed · **Owner:** Data science / ML · **Last reviewed:** 2026-10-17

Structured path from a business problem to a deployed, monitored model. Extends the [SDLC](software-development-lifecycle.md) with ML-specific phases (following a CRISP-ML(Q)-style structure with explicit quality assurance at each step).

## Phases

### 1. Business & requirements understanding
- Business problem, decision to be influenced, and success metric in business terms
- **ML feasibility question:** is this a prediction problem, and is historical data informative?
- Baseline established: what does the current (rules/human/no-system) approach score?
- **Artifact:** problem framing doc + baseline metrics

### 2. Data understanding & preparation
- Source identification, availability, quality, classification, lawful basis
- Exploratory analysis; label quality assessment; leakage scan
- Train/validation/test splits defined **now**, not after modeling
- **Artifact:** data card + split strategy + preprocessing spec
- **Gate:** data quality and leakage review (see [data lifecycle](data-lifecycle.md))

### 3. Modeling
- Candidate approaches from simplest viable upward (rules → linear → tree ensembles → deep learning → LLM where justified)
- Hyperparameter search with tracked experiments ([MLOps](mlops-lifecycle.md))
- Feature engineering logged; features eventually served consistently (see [ML engineering patterns](../design-patterns/ml-engineering.md))
- **Artifact:** experiment log + candidate models

### 4. Evaluation
- Metrics chosen against the business metric, including error asymmetry (cost of false positive vs false negative)
- Held-out and out-of-time evaluation; subgroup/segment analysis for fairness and robustness
- Comparison against baseline and simplest viable model, documented
- **Artifact:** evaluation report with confidence intervals
- **Gate:** evaluation review — no deployment without reporting

### 5. Deployment
- Serving mode: batch, online, or streaming (see [inference RA](../reference-architectures/inference/README.md))
- Shadow or canary rollout before full traffic ([ML deployment patterns](../design-patterns/mlops-deployment.md))
- Feature pipelines and model released together (train/serve consistency)
- **Artifact:** registered model + deployment record

### 6. Monitoring & maintenance
- Input drift, prediction drift, and performance against delayed ground truth
- Retraining triggers defined (scheduled, drift-based, or performance-based)
- Feedback loops capture real outcomes for retraining
- **Artifact:** monitoring dashboard + retraining policy

### 7. Retirement
- Deprecation, consumer migration, artifact and data deletion, credential revocation

## Quality assurance at every phase (the "Q" in CRISP-ML)

| Phase | Quality question |
|---|---|
| Business | Is the problem well-posed and measurable? |
| Data | Is the data sufficient, representative, and lawful? |
| Modeling | Are comparisons fair (same splits, seeds, metrics)? |
| Evaluation | Does it beat baseline meaningfully and safely? |
| Deployment | Is it reproducible and observable in production? |
| Monitoring | Will we notice decay before users do? |

## Common failure modes

- **Leakage:** target or post-outcome information in features — the most common cause of impressive-then-useless models
- **Metric mismatch:** optimizing an offline proxy that no longer tracks the business outcome
- **Split contamination:** time-ordered data split randomly
- **Baseline-free claims:** "improvement" against nothing
- **Deployment without monitoring:** silent decay
