# Evaluation Lifecycle

**Status:** Proposed · **Owner:** AI quality · **Last reviewed:** 2026-10-17

How quality is defined, measured, and defended across every AI lifecycle. Evaluation is continuous infrastructure, not a one-time milestone.

## Phases

### 1. Define success
- Map the business outcome to measurable task properties
- Choose metrics that are diagnostic (tell you *which layer* failed) and stable (don't fluctuate randomly)
- Thresholds agreed with stakeholders **before** building — "how good is good enough?"
- **Artifact:** metric definition sheet with thresholds

### 2. Curate datasets
- **Golden set:** representative, expert-verified, versioned (input + expected properties, not brittle exact strings)
- **Adversarial set:** injection, jailbreaks, out-of-scope, ambiguity, hostile content, PII probes
- **Regression set:** known past failures, permanently — every production bug becomes a test case
- **Held-out set:** never used for tuning; guards against overfitting to the golden set
- Provenance and refresh cadence per dataset; a named curator owns each
- **Artifact:** datasets + data cards

### 3. Build the harness
- Automate metric computation so local runs and CI produce identical numbers
- Deterministic where possible (seed, pinned judge model version); record variance when not
- Support human review workflows for cases automation can't judge
- **Artifact:** evaluation harness + config

### 4. Gate changes
- Tiered execution: fast PR gate (< 5 min) → nightly full → pre-release human review
- Hard thresholds block promotion; soft metrics trend and alert
- Applies to: prompts, models, retrieval configs, chunking, tools, guardrails, agent loops
- **Artifact:** CI gate config + results

### 5. Monitor in production
- Online proxies: acceptance rate, edit rate, escalation rate, abandonment, thumbs
- Sampled automated judging + scheduled human review
- Delayed ground truth where the real outcome arrives later (resolution, conversion, correction)
- Safety event rates (guardrail blocks, injection attempts)

### 6. Detect & diagnose drift
- Separate signals: data drift (inputs changed), behavior drift (provider model changed), concept drift (world changed)
- Diagnostic tree: retrieval issue vs prompt issue vs model issue vs data issue
- **Artifact:** drift report with root cause

### 7. Improve
- Failed production cases are triaged into the regression set
- Golden set refreshed on cadence and when domain shifts
- Thresholds renegotiated with stakeholders as capability improves — document the change

### 8. Retire
- Archive datasets with their harness version; note why evaluation ended

## Metric families by workload

| Workload | Core metrics |
|---|---|
| Classical ML | Accuracy/precision/recall/F1, AUC, calibration, error by segment |
| GenAI (generic) | Task success, instruction adherence, tone/format compliance, latency, cost |
| RAG | Retrieval: hit-rate, recall@k, MRR, NDCG. Generation: faithfulness, answer relevance, citation correctness |
| Data agent | Query correctness, answer correctness, ambiguity handling, unauthorized-retrieval rate |
| Agents | Task success, tool-call accuracy, steps/task, reasoning integrity, escalation correctness, cost/task |
| Copilots | Acceptance rate, edit-before-accept rate, time-to-task, adoption |
| Safety (all) | Injection resistance, PII leakage rate, guardrail precision/recall |

## LLM-as-judge discipline

- **Calibrate** against human labels; report agreement (e.g., Cohen's kappa)
- **Pin** the judge model version — a judge upgrade is an evaluation-system change
- **Blind** the judge to which system produced each output where feasible
- **Watch bias:** judges favor longer answers, their own family's outputs, and confident tone
- Never use a judge as the sole gate for high-risk decisions; pair with human review

## Anti-patterns

- Evaluating with the same set used for tuning
- Metrics nobody can act on (not diagnostic)
- One-time evaluation before launch, then silence
- Judge model silently upgraded, invalidating all trend history
- Production bugs fixed but never added to the regression set
