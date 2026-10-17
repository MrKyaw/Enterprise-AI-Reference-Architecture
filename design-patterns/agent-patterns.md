# Agent Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns for LLM-driven agents that plan, use tools, and take action. Lifecycle context in the [agent lifecycle](../lifecycles/agent-lifecycle.md); baseline in the [agentic reference architecture](../reference-architectures/agentic/README.md); interoperability rules in [agent protocols](../standards/agent-protocols.md).

> Governing principle: **autonomy is a design decision, not a default.** Every action has a side-effect class; every run has bounds; every capability has a kill switch.

## Core loop patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Tool use / function calling** | Extend capability via typed tools | Almost always vs. free-text parsing | Validate arguments server-side |
| **ReAct (reason + act)** | Interleave reasoning and tool calls | Multi-step tasks needing observation | Loop risk; token growth |
| **Plan-and-execute** | Plan fully, then execute steps | Predictable multi-step workflows | Brittle when the world changes mid-plan |
| **Reflection / self-critique** | Review and revise before acting/answering | Quality-critical outputs | Cost; false confidence |
| **Router/dispatcher** | Classify request, delegate to the right handler | Mixed request types | Misrouting is a silent failure |
| **Deterministic-first** | Fixed workflow, model only at decision points | Business processes | The most under-used and most reliable option |
| **Retry with alternate strategy** | Try a different approach on failure | Transient/tool-specific failures | Bounded retries required |

## Memory patterns

| Pattern | Intent | Scope | Watch out |
|---|---|---|---|
| **Working memory (context window)** | Current task state | Turn/session | Token limits; truncation policy |
| **Conversation buffer / rolling summary** | Retain dialogue context | Session | Summaries lose specifics |
| **Episodic memory** | Recall prior interactions/events | User/session | Privacy + retention obligations |
| **Semantic memory (knowledge store)** | Durable facts, often via [RAG](rag-patterns.md) | System/tenant | Grounding + freshness |
| **Procedural memory** | Learned workflows/tool sequences | System | Versioning; drift |
| **Externalized scratchpad/artifact store** | Persist intermediate work | Session/run | Cleanup and isolation |
| **Scoped memory isolation** | Per-user/per-tenant separation | Always multi-user | Cross-tenant leakage is a critical defect |

## Multi-agent patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Supervisor / orchestrator** | One agent decomposes and delegates | Clear hierarchy, bounded subtasks | Supervisor becomes a bottleneck/failure point |
| **Hierarchical** | Supervisors of supervisors | Large decomposable tasks | Cost and coordination overhead |
| **Sequential pipeline** | Fixed handoff chain of specialists | Well-understood staged workflows | No adaptability |
| **Blackboard / shared state** | Agents contribute to shared workspace | Collaborative problem solving | Synchronization and conflict resolution |
| **Swarm / decentralized** | Peer agents coordinate locally | Emergent/robust exploration | Unpredictable behavior; hard to audit |
| **Market/auction** | Agents bid on tasks | Resource allocation at scale | Complexity rarely pays off |
| **Debate / critic pairs** | Adversarial review improves output | High-stakes reasoning | Cost; convergence to plausible consensus |
| **Handoff with context transfer** | Pass task + evidence + authority | Cross-team/domain boundaries | Authority must not escalate during handoff |

## Safety & control patterns

| Pattern | Intent | Notes |
|---|---|---|
| **Human-in-the-loop approval** | Gate write/irreversible actions ([detail](human-in-the-loop-approval.md)) | Enforced outside the model |
| **Side-effect classification** | Label tools read / reversible / irreversible | Drives gating and review tier |
| **Sandbox isolation** | Execute in bounded environment (control AI-11) | Blast radius limited by infrastructure |
| **Authorization boundary** | Explicit maximum authority per run/autonomy level | Declared and tested, not implied |
| **Bounded autonomy (step/cost/time ceilings)** | Prevent runaway execution | Termination is mandatory |
| **Kill switch** | Immediate stop for an agent/system | Tested quarterly |
| **Tool registry allowlist** | Only registered tools callable | Registry = authorization boundary |
| **Dry-run / staged commit** | Preview the action's effect | Where the target system supports it |
| **Escalation policy** | Route uncertainty/stalls to humans | Expiry defaults to deny |
| **Loop detection** | Detect repeated states/calls | Step-inflation is the earliest cost signal |

## Orchestration & operational patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Trajectory logging** | Record every step, tool call, decision | Immutable + correlated (control AI-7) |
| **Step budget & budgeting per task** | Bound cost and time | Budgets too low cause premature failure |
| **State machine / explicit FSM** | Deterministic control flow where possible | Prefer over "let the model decide" |
| **Idempotent tool contracts** | Safe retries | Required for any write |
| **Compensation / rollback steps** | Undo partial work | Needs [saga pattern](general-architecture.md) |
| **Graceful halt** | Stop and escalate instead of guessing | Default behavior on uncertainty |

## Choosing an agent pattern

```
Fixed, well-understood process           → deterministic workflow (no agent)
Single tool + single decision            → tool-use with structured output
Multi-step, unpredictable steps          → ReAct with bounds
Parallel/subtask decomposition           → supervisor + specialists
High-stakes reasoning                    → debate/critic + human review
Relationship reasoning over entities     → graph retrieval + agentic RAG
```

## Anti-patterns

- Multi-agent architectures for problems a single well-scoped agent solves
- Unbounded loops with no step/cost/time ceiling
- Shared credentials across agents (no attribution, huge blast radius)
- Autonomy increased quietly via prompt changes
- Tools that write without idempotency or approval
- "The agent will figure it out" as a control strategy
- Memory shared across tenants
