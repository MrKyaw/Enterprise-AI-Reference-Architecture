# Operations & Incident Lifecycle

**Status:** Proposed · **Owner:** Operations · **Last reviewed:** 2026-10-17

How AI systems are run and how failures are handled. AI adds failure modes that classical monitoring misses — quality and safety failures with no error code.

## Steady-state operations

| Domain | What is monitored |
|---|---|
| Availability | Uptime, error rate, dependency health (provider, vector store, data platform) |
| Latency | p50/p95/p99 by stage (gateway, retrieval, model, tools, guardrails) |
| Cost | Spend per request/task/agent-run; burn-rate alerts; budget ceilings |
| Quality | Sampled automated judges, user feedback, task success |
| Safety | Guardrail blocks, injection attempts, tool denials, PII detector hits |
| Data | Freshness, schema drift, volume anomalies for retrieval/feature pipelines |
| Drift | Input distribution, output behavior, delayed ground-truth performance |

**Rule:** if it has an SLO, it has an alert; if it has an alert, it has a runbook; if it has a runbook, someone is on call for it.

## Incident lifecycle

### 1. Detect
- Alerts (threshold, anomaly, burn-rate) or user reports
- Quality/safety degradation counts as an incident even when the system is "up"

### 2. Triage
- Severity assignment by user impact × blast radius × reversibility
- Declare an incident owner; open a channel; start a timeline log
- Decide: mitigate now vs investigate first (default: stop the bleeding)

### 3. Mitigate
Order of preference:
1. **Disable** the failing capability (feature flag / kill switch)
2. **Degrade** gracefully (fallback model, non-AI path, cached answer)
3. **Roll back** to the last known-good version (model, prompt, index, config)
4. **Patch forward** only when rollback is unsafe or unavailable

### 4. Resolve
- Restore normal operation with evidence, not optimism
- Verify quality metrics recovered, not just availability metrics

### 5. Communicate
- Status updates on a fixed cadence; avoid speculation about cause
- Distinguish "AI output was wrong" incidents from "system was down" incidents in comms

### 6. Postmortem
- **Blameless.** Focus on system conditions, not individuals
- Contents: timeline, impact, root cause, contributing factors, what went well, action items with owners and dates
- AI-specific questions:
  - Was this a **quality** failure, **safety** failure, **reliability** failure, or **cost** failure?
  - Did guardrails work? Did they fire late or not at all?
  - Was the change (prompt/model/index/data) gated by evaluation? If not, why not?
  - Did monitoring detect it, or did a user?

### 7. Feed back
- Every production failure becomes a case in the **regression evaluation set** ([evaluation lifecycle](evaluation-lifecycle.md))
- Generalizable findings update [security controls](../security/ai-security-controls.md) or reference architectures ([red-team loop](../security/red-team-integration.md))
- Action items tracked to closure; recurring causes escalate to architecture review

## AI-specific incident playbooks (required)

| Scenario | First action | Follow-up |
|---|---|---|
| Harmful/incorrect output at scale | Disable capability or tighten guardrails | Root cause, regression test, eval gate |
| Prompt injection exploited | Block offending content path; rotate affected credentials | Control update |
| Runaway agent (loops/cost) | Trip kill switch; revoke tools | Bounds review, trajectory eval |
| Provider outage/degradation | Failover to contingency provider | Capacity and concurrency review |
| Data leak via prompt/response | Disable, preserve evidence, notify per policy | Forensic review, control update |
| Model/provider silent change | Pin/rollback version; compare eval | Change-detection automation |

## Chaos & game-day practice

- Scheduled failure injection: kill the model endpoint, corrupt the index, delay the provider, feed hostile input
- Verify degradation paths actually work (a fallback never tested is not a fallback)
- Game-days for agent kill switch and approval-gate bypass attempts

## Anti-patterns

- Monitoring infrastructure only, never output quality
- Alerts without runbooks or owners
- Postmortems that stop at "the model was wrong"
- Disabling evaluation gates during incidents and forgetting to re-enable them
- Blaming the user for trusting an AI output that the system presented confidently
