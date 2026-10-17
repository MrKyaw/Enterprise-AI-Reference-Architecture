# GenAI / LLMOps Lifecycle

**Status:** Proposed · **Owner:** AI engineering · **Last reviewed:** 2026-10-17

Lifecycle for applications built on foundation models — prompt-driven, retrieval-augmented, and tool-using systems. Extends [MLOps](mlops-lifecycle.md): classical MLOps optimizes a trained artifact, LLMOps manages a **configuration surface** (prompts, model versions, retrieval settings, guardrails) against **statistical, non-deterministic** outputs.

## What makes LLMOps different

| Classical ML | GenAI / LLM |
|---|---|
| Train a model, ship weights | Configure a model, ship prompts + retrieval + config |
| Deterministic outputs | Non-deterministic; same input, different output |
| Metrics: accuracy, AUC | Metrics: task success, faithfulness, tool-call accuracy, safety |
| Data drift is the main risk | Also *behavioral* drift from provider-side model updates |
| Retraining is the change | Prompt/model/config change is the routine change |
| External provider rare | Usually multi-provider, versioned externally |

## Phases

### 1. Use-case framing & feasibility
- Task decomposition: which parts need generative reasoning vs deterministic logic
- Baseline: does a non-LLM approach suffice? (rules, search, templates)
- Cost/latency envelope estimated before building
- **Artifact:** framing doc with task taxonomy

### 2. Design
- Select reference architecture(s): [inference](../reference-architectures/inference/README.md), [RAG](rag-lifecycle.md), [agent](agent-lifecycle.md), [copilots](../reference-architectures/copilots/README.md)
- Model selection criteria ([model-provider standards](../standards/model-provider-standards.md))
- Guardrail and context-engineering design ([GenAI patterns](../design-patterns/genai-prompting.md))
- **Gate:** design review for novel/high-risk designs

### 3. Prompt & context engineering
- Prompt templates versioned in source control ([prompt lifecycle](prompt-lifecycle.md))
- Context assembled with attribution and minimization
- Structured output contracts where downstream systems consume the result
- **Artifact:** versioned prompts + context spec

### 4. Evaluation
- Golden task set + adversarial set, with explicit thresholds ([evaluation lifecycle](evaluation-lifecycle.md))
- LLM-as-judge where human review is too slow, **calibrated against human labels**
- Regression gates in CI; no prompt/config change ships without passing them
- **Artifact:** eval report per candidate config

### 5. Deployment
- Config packaged and promoted like code; together with eval results and rollback target
- Canary or shadow comparing new vs incumbent config on live traffic
- Fallback model/router configured ([patterns](../design-patterns/genai-prompting.md))
- **Artifact:** deployment record + rollback plan

### 6. Observability
- Traces of full request path: input → retrieval → prompt → model → tools → output
- Quality sampling: automated judges + human review on a sampling schedule
- Cost per request, tokens, cache hit rate, latency percentiles
- Safety events: guardrail blocks, injection attempts, tool denials

### 7. Continuous improvement & change management
- Prompt/model/config changes follow the same eval gates as code
- Provider model updates are **detected and treated as changes** — pin versions, test deprecation timelines
- Feedback capture: thumbs, edits, escalations, task abandonment
- **CT analogue:** re-index retrieval corpora, refresh prompts, re-tune routing

### 8. Retirement
- Decommission prompts, endpoints, keys; delete logs per retention; migrate users

## Model & provider change handling

1. **Pinned** provider/model versions in configuration
2. **Deprecation watch:** provider lifecycle tracked; replacement evaluated before forced migration
3. **Change test:** every provider or version change re-runs the full eval suite
4. **Multi-provider contingency** configured for production workloads

## Anti-patterns

- Prompt changes merged with no eval run ("it looked better")
- Logging raw user content without classification handling
- Unpinned model versions with no deprecation plan
- LLM-as-judge trusted without calibration against human labels
- Treating a demo-day result as an evaluation
