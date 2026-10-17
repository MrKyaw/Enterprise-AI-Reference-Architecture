# Production Issues — Agents & Tools (`A-`)

Failures specific to systems that take actions. These carry the highest blast radius and the least tolerance for "we'll fix it in the next release."

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| A-01 | Agent loops indefinitely, burning cost and time | No termination condition; oscillating plan; unhelpful tool error repeated | Cost/time runaway; hung workflows | Step/cost/time ceilings; loop detection; kill switch |
| A-02 | Agent performs an action nobody approved | Autonomy level higher than intended; approval gate bypassable | Critical: unauthorized change | Enforce approval outside the model; verify gate; declare authorization boundary |
| A-03 | Wrong tool called with hallucinated arguments | Tool contracts too loose; arguments unvalidated | Incorrect actions; data corruption | Typed contracts; server-side validation; dry-run |
| A-04 | Agent reports success without doing the work | Fabricated tool results or ignored errors | Silent failure; downstream chaos | Verify outcomes; never trust self-reported success |
| A-05 | Partial failure leaves inconsistent state | No compensation/rollback; non-idempotent steps | Broken records; manual cleanup | Saga/compensation; idempotency keys |
| A-06 | Agent escalates too much or too little | Miscalibrated confidence/escalation policy | Toil or missed exceptions | Calibrate on labeled cases; measure escalation correctness |
| A-07 | Multi-agent system deadlocks or ping-pongs | Circular delegation; no ownership of final decision | Stalled workflows | Explicit termination and ownership rules |
| A-08 | Agent memory pollutes later sessions | Shared or uncleared memory; poisoned memory write | Wrong decisions; data leakage across users | Scoped memory; retention/clearing; write validation |
| A-09 | Autonomy crept up silently | Capability expansion without review | Unreviewed risk expansion | Autonomy as explicit state; re-review on capability change |
| A-10 | Tool credentials usable far beyond the task | Over-scoped, long-lived service credentials | Large blast radius | Per-tool least privilege; short-lived tokens |
| A-11 | Agent follows injected instructions from a tool's response | Tool output treated as trusted | Critical: unauthorized action | Treat all tool output as untrusted; authority from router |
| A-12 | Cost per task varies wildly and unpredictably | No per-task budget; variable reasoning depth | Unforecastable spend | Per-task budgets; routing; caching |
| A-13 | Trajectory unreconstructable during incident | Missing step-level logging/correlation | Cannot diagnose or prove behavior | Immutable trajectory logging with correlation IDs |

---

## A-02 — Unapproved action by an agent

**Symptom:** A record was deleted, an email sent, or a payment released that no human approved.

**Root cause:** One of: the approval gate was advisory in the prompt rather than enforced in the orchestrator; the tool was callable without the gate; autonomy level was raised during a config/prompt change; or the gate existed but its failure mode was "allow."

**Impact:** **Critical.** Possibly irreversible business or customer harm, plus regulatory exposure and loss of stakeholder trust in the entire program.

**Fix:** Immediate containment — revoke the tool's credentials and disable the capability. Preserve audit logs. Then enforce the gate in the orchestrator/policy engine for the affected tool class and verify with a negative test that the action cannot occur without approval.

**Prevention:** [Human-in-the-loop approval pattern](../design-patterns/human-in-the-loop-approval.md) enforced **outside** the model; [side-effect classification](../security/ai-security-controls.md) for every tool; explicit [authorization boundary](../lifecycles/agent-lifecycle.md) per autonomy level; [red-teaming](../security/red-team-integration.md) that specifically attempts to bypass the gate.

**Future work:** Formal verification of the gate path; automatic detection when an agent's effective authority exceeds its declared boundary; a platform-level interlock that refuses irreversible actions for agents not explicitly authorized for that class.

---

## A-04 — Agent reports success without doing the work

**Symptom:** The agent says the ticket was updated, the file uploaded, or the change applied — but the target system shows no change.

**Root cause:** The agent narrated an intended action as completed, or a tool returned an ambiguous response that the model interpreted as success, or an error was swallowed by a retry wrapper.

**Impact:** High. Silent failure with false confidence — the worst combination because humans stop checking, and the error surfaces days later as a downstream discrepancy.

**Fix:** Verify outcomes by querying the target system after an action; treat tool responses as evidence, not truth; fix the error-swallowing retry wrapper.

**Prevention:** Outcome verification as a workflow step; tool contracts that return verifiable identifiers/versions; never letting the model summarize a tool's success without a check ([agent patterns](../design-patterns/agent-patterns.md)).

**Future work:** Post-action reconciliation jobs that compare intended vs actual state; standardized tool result contracts including verification handles; automated detection of narration-without-action patterns in trajectories.

---

## A-05 — Partial failure leaves inconsistent state

**Symptom:** An agent completes steps 1–3, fails at step 4, and the system is left half-updated — a record created but not linked, a payment authorized but not recorded.

**Root cause:** Multi-step side effects executed without compensation logic or idempotency, on the assumption that later steps succeed.

**Impact:** High. Manual cleanup, data-quality debt, and occasionally financial discrepancies.

**Fix:** Implement compensating actions for the completed steps; make steps idempotent so retries are safe; add reconciliation for affected records.

**Prevention:** [Saga/compensation pattern](../design-patterns/general-architecture.md), idempotency keys for writes ([reliability patterns](../design-patterns/reliability-resilience.md)), and dry-run/staged commit where the target supports it.

**Future work:** Declarative compensation in tool contracts (each write tool declares its inverse); automatic sagas for common multi-step workflows; state-reconciliation verification as a standard built-in.

---

## A-13 — Unreconstructable trajectory

**Symptom:** During an incident, nobody can explain what the agent did or why. Logs show tool calls without the reasoning or context that produced them.

**Root cause:** Logging captured final outputs and maybe tool names, but not the assembled context, plan state, tool arguments, tool responses, or the decision points between steps. Correlation IDs missing across services.

**Impact:** High. Incident resolution becomes guesswork; root-cause analysis is impossible; audit and regulatory explanation unavailable; the same failure recurs because learning is impossible.

**Fix:** Instrument the loop for full trajectory capture immediately, even if verbose, and reconstruct the affected run from whatever exists; then set retention and sampling policy.

**Prevention:** [Trajectory logging](../design-patterns/agent-patterns.md) with correlation IDs end-to-end, classified/redacted at the logging boundary (controls AI-6/AI-7), and [operations lifecycle](../lifecycles/operations-incident-lifecycle.md) requirements for postmortems.

**Future work:** Replayable trajectories for simulation and regression testing; privacy-preserving trajectory capture for high-sensitivity contexts; standardized trajectory schema so incidents across systems are comparable.
