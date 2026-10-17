# MLOps Lifecycle

**Status:** Proposed · **Owner:** ML platform · **Last reviewed:** 2026-10-17

The automation and operational discipline that turns the [ML project lifecycle](ml-project-lifecycle.md) from a one-off exercise into a repeatable system. MLOps is the CI/CD/CT + registry + monitoring backbone.

## The three pipelines

```
CI  Continuous Integration   → code + data + model tests on every change
CD  Continuous Delivery      → deploy models/pipelines automatically with gates
CT  Continuous Training      → trigger retraining from schedule, drift, or performance
```

| Pipeline | Trigger | Contents | Output |
|---|---|---|---|
| CI | PR / merge | Lint, unit tests, data validation, model smoke test, eval gate | Green build |
| CD | Tag / approved release | Package model+pipeline, register artifact, deploy canary → full | Live version |
| CT | Schedule / drift alert / new data | Re-run training → evaluate → register → promote if better | New candidate |

## Lifecycle stages

### 1. Environment & reproducibility
- Pinned dependencies, deterministic seeds, containerized runtimes
- Data versioning and snapshot references — a training run is reproducible from its manifest alone
- Environment parity between development, staging, production

### 2. Experiment management
- Every run logged: parameters, metrics, code commit, data version, artifacts
- Comparison views; "best run" selection is explicit and reviewable, not tribal knowledge

### 3. Pipeline automation
- Training, validation, evaluation, and registration orchestrated as code
- Reusable, metadata-driven pipeline templates (ingestion → transform → feature → train → eval → register)
- Idempotent steps; failed steps retry safely

### 4. Model registry & lineage
- Every model: immutable version, owner, metrics, eval report, parent data/code lineage, approval status
- Promotion is a state transition in the registry (staging → production), not a file copy
- Rollback = point production at the previous registry version

### 5. Deployment automation
- Standard serving targets: batch scoring, real-time endpoints, streaming
- Canary/shadow/A-B rollout patterns ([patterns](../design-patterns/mlops-deployment.md))
- Config-as-code for serving resources and autoscaling

### 6. Monitoring & observability
- **Operational:** latency, throughput, error rate, resource saturation
- **Model:** input drift, prediction drift, delayed-ground-truth performance
- **Data:** schema, null rate, range violations, freshness
- **Business:** the outcome metric the model was supposed to move

### 7. Retraining & continuous improvement
- Triggers: calendar, drift threshold, performance degradation, upstream change
- Automated CT with human approval before production promotion (or auto-promote within pre-agreed guardrails)
- Champion/challenger comparison against the incumbent

### 8. Governance & audit
- Approval records per promotion; who signed off and on what evidence
- Model risk linkage ([model risk lifecycle](model-risk-lifecycle.md))
- Retention policy for runs, artifacts, and logs

### 9. Retirement
- Deregistration, endpoint decommission, artifact/data deletion, dependency cleanup

## MLOps maturity ladder

| Level | Characteristics |
|---|---|
| 0 — Manual | Notebooks, manual deployment, no tracking |
| 1 — Repeatable | Version control + experiment tracking + scripted training |
| 2 — Automated | CI/CD/CT pipelines, registry, monitoring |
| 3 — Governed | Approval gates, lineage, model risk integration, policy-as-code |
| 4 — Adaptive | Automatic retraining within guardrails, automated rollback, self-healing drift response |

Target level depends on risk class; high-impact systems should reach at least level 3.

## Anti-patterns

- Notebook-to-production hand-offs that lose reproducibility
- Retraining without re-evaluation, or auto-promotion with no guardrails
- Monitoring infrastructure only, never monitoring model quality
- Registry as a file share with no lineage
