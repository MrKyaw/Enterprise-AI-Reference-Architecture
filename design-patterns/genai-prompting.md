# GenAI & Prompting Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns for building with foundation models. Implements the [GenAI/LLMOps lifecycle](../lifecycles/genai-llmops-lifecycle.md) and [prompt lifecycle](../lifecycles/prompt-lifecycle.md).

## Prompting patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Prompt template** | Parameterized, versioned instruction | Always | Version drift between code and prompt |
| **Few-shot exemplars** | Shape format and edge cases | Format/edge behavior matters | Token cost; exemplar bias |
| **Chain-of-thought** | Improve multi-step reasoning | Reasoning tasks | Latency/cost; can leak reasoning in output |
| **Decomposition** | Split a complex task into simpler prompts | Multi-part tasks, testability | Orchestration complexity |
| **Self-consistency** | Sample several paths, take the consensus | High-stakes single answers | Multiplicative cost |
| **Self-critique / reflection** | Model reviews and improves its draft | Quality-sensitive generation | Can converge on plausible-but-wrong consensus |
| **Structured output** | Enforce schema (JSON/typed) | Machine-consumed outputs | Always validate server-side |
| **Grounding instruction** | Answer only from provided context; cite | Knowledge tasks | Requires retrieval/evidence to exist |
| **Refusal & uncertainty behavior** | Explicit "I don't know" / hand-off paths | User-facing systems | Silence is worse than abstention |
| **Untrusted-content delimiting** | Clear separation of instructions vs data | Any external content in context | Defense-in-depth only — not a control by itself |

### Guardrail sandwich

Wrap every user-facing generation:

```
Input filter (policy, injection, PII)
      ↓
[ instructions | governed context | user request ]
      ↓
Model generation (structured where possible)
      ↓
Output filter (policy, PII, schema validation, safety)
      ↓
Deterministic post-processing (formatting, permission check, action gate)
```

The sandwich is enforced **outside** the model by deterministic systems ([controls](../security/ai-security-controls.md)). Prompt instructions are not a guardrail.

## Context engineering patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Context minimization** | Send only what the task needs | Over-minimizing removes necessary signal |
| **Context ordering** | Place critical instructions and evidence deliberately | Recency effects differ by model |
| **Context compression / summarization** | Fit long histories into the window | Summaries lose specifics — keep references |
| **Scratchpad / working notes** | Model maintains intermediate state | Must be bounded; can leak into output |
| **Tool-result injection** | Structured tool outputs into the loop | Treat tool output as untrusted |
| **Retrieval-then-generate** | Ground generation in retrieved evidence | See [RAG patterns](rag-patterns.md) |

## Model selection & efficiency patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Model cascade / router** | Cheap model first, escalate on confidence/failure | Requires routing evaluation + escalation budget |
| **Task-specific model choice** | Match model to task tier | Fragmented config; keep a decision record |
| **Provider failover** | Contingency provider on outage/degradation | Behavioral differences must be evaluated |
| **Semantic caching** | Reuse answers for semantically similar requests | Cache correctness; never bypass ACLs or policy |
| **Exact-match caching** | Reuse identical requests | Invalidation on model/prompt change |
| **Prompt caching (provider-side)** | Reduce cost/latency on stable prefixes | Prefix stability requirements |
| **Batch/async generation** | Offline bulk generation at lower cost | Not for interactive paths |
| **Speculative/degraded serving** | Cheaper path under load | Quality must remain acceptable; log degradation |

## Quality & evaluation patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **[Evaluation in CI](evaluation-in-ci.md)** | Gate prompt/model/config changes | Threshold tuning is empirical |
| **LLM-as-judge** | Scalable quality scoring | Calibrate to humans; pin judge version |
| **Golden task set** | Representative quality baseline | Rot and overfitting to the set |
| **Adversarial prompt suite** | Injection/jailbreak resistance | Must evolve with new attack techniques |
| **Regression set from production failures** | Prevent repeat failures | Triage discipline required |
| **Human review sampling** | Judgment automation can't provide | Cadence and workload must be sustainable |

## Cost & latency patterns

| Pattern | Intent |
|---|---|
| Token budget per request/run | Bound worst-case cost |
| Streaming responses | Perceived latency improvement |
| Output length control | Cost is often output-dominated |
| Tiered quality tiers | Serve different quality levels to different contexts |
| Cost attribution tagging | Enable per-workload governance |

## Anti-patterns

- Prompts as the safety layer
- Provider SDK calls bypassing the gateway
- Semantic cache ignoring user permissions
- Structured output consumed without schema validation
- Router/cascade tuned once, never re-evaluated
- Context stuffed to the limit "just in case"
