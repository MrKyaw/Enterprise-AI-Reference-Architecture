# Agent Lifecycle (AgentOps)

**Status:** Proposed · **Owner:** AI engineering · **Last reviewed:** 2026-10-17

Lifecycle for LLM-driven agents that plan, call tools, and take action. Implementation details in the [agentic reference architecture](../reference-architectures/agentic/README.md) and [agent patterns](../design-patterns/agent-patterns.md). AgentOps = the operational discipline across this lifecycle.

## Phases

### 1. Capability & autonomy framing
- What the agent does, for whom, in which systems
- **Autonomy level declared explicitly** (see table below)
- Side-effect inventory: every action classed read / reversible-write / irreversible
- Non-goals stated (what the agent must never attempt)
- **Artifact:** capability charter + autonomy declaration
- **Gate:** this document is the basis of direct architecture review for side-effecting agents

### 2. Tool & context design
- Tool contracts typed and registered ([agent protocols](../standards/agent-protocols.md))
- Per-tool credentials, least privilege, short-lived ([security controls](../security/ai-security-controls.md))
- Context strategy: system instructions, memory scope, retrieved context
- **Artifact:** tool registry entries + context spec

### 3. Control-loop design
- Pattern selected: single-loop, plan-and-execute, supervisor, hierarchical, blackboard, swarm ([patterns](../design-patterns/agent-patterns.md))
- Termination conditions: success, max steps, max cost, max wall-clock, unrecoverable error
- Human-in-the-loop gates for write/irreversible actions ([HITL pattern](../design-patterns/human-in-the-loop-approval.md))
- **Artifact:** control-loop spec + state machine

### 4. Memory design
- Scope: turn, session, user, tenant — with isolation guarantees
- Types: episodic (what happened), semantic (facts), procedural (how), summary/compression
- Retention, deletion, and poisoning defenses
- **Artifact:** memory spec

### 5. Safety & guardrails
- Input filtering, output filtering, tool-call authorization, egress allowlist, sandbox isolation (control AI-11)
- Prompt-injection defense for all untrusted content ([controls](../security/ai-security-controls.md))
- Kill switch design and test
- **Gate:** threat model + red-team plan

### 6. Evaluation
- Task success rate, tool-call accuracy, reasoning integrity, cost per task, steps per task
- Adversarial suite: injection, tool abuse, unauthorized-action attempts, loop traps
- Trajectory evaluation, not just final-answer evaluation
- **Artifact:** agent eval suite + baselines

### 7. Deployment
- Sandbox/dry-run environment first; then read-only in production; then gated writes
- Feature-flag autonomy level per user group; start narrow
- Observability: full trajectory traces with correlation IDs
- **Artifact:** staged rollout plan + trace pipeline
- **Gate:** [red-team exercise](../security/red-team-integration.md) complete before autonomous writes

### 8. Operations
- Monitors: success rate, escalation rate, cost/task, step inflation (looping), tool-denial spikes, anomaly detection on tool sequences
- Incident runbook: runaway agent, manipulated agent, credential misuse, provider outage
- Quarterly control attestation for high-risk agents

### 9. Evolution
- Capability expansion requires re-review (new tool class = new risk class)
- Model upgrades re-run full behavioral evaluation
- Autonomy increases are explicit, reversible decisions — never gradual drift

### 10. Retirement
- Disable agent, revoke credentials, deregister tools, purge memory, retain audit logs per policy

## Autonomy levels

| Level | Name | Behavior | Approval |
|---|---|---|---|
| L0 | Advisory | Suggests only; human does everything | None |
| L1 | Assisted action | Acts on reversible actions; human does irreversible | HITL for irreversible |
| L2 | Supervised autonomy | Autonomously handles reversible; human approves high-impact | HITL for high-impact |
| L3 | Bounded autonomy | Autonomous within explicit, tested authorization boundary | Policies + spot checks |
| L4 | Full autonomy | Unrestricted within a domain | Rarely justified; direct governance sign-off |

**Default to the lowest level that delivers the value.** Moving up a level is a risk decision with evidence, not a configuration change.

## Anti-patterns

- Side effects enabled before trajectory evaluation exists
- "The prompt says don't do X" as a control (controls live outside the model)
- Unbounded loops with no step/cost ceiling
- Shared credentials across agents (no attribution, unlimited blast radius)
- Autonomy creeping upward one prompt-change at a time, never reviewed
