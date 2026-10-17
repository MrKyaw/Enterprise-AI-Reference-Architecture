# Pattern — Human-in-the-Loop Approval

**Status:** Proposed · **Type:** process/safety

## Context

Agentic systems and automated workflows can trigger side effects: sending emails, modifying records, spending money, changing infrastructure. Fully autonomous execution is unsafe for write and irreversible actions.

## Forces

- Autonomy delivers value but mistakes are costly and hard to reverse
- The model deciding "this is safe" is not a control — models can be manipulated (prompt injection)
- Approval friction must scale: trivial actions shouldn't wait hours for a human

## Solution

Classify every tool/action by **side-effect class** and gate execution outside the model:

| Class | Examples | Gate |
|---|---|---|
| Read-only | Search, fetch, summarize | Automatic |
| Reversible write | Create draft, stage change | Policy engine (rules) |
| Irreversible / high-impact | Send, delete, pay, deploy | Human approval, explicit |

- Approval state is stored in the **workflow system**, never in model context
- The approval request shows: proposed action, evidence, blast radius, and expiry
- Time-boxed approvals expire to "deny," never to "allow"

## Consequences

- ✅ Model manipulation cannot directly cause high-impact actions
- ✅ Auditable decision trail with human accountability
- ⚠️ Latency and toil if thresholds aren't tuned — review gate rates quarterly

## Known uses

- Required by the [agentic reference architecture](../reference-architectures/agentic/README.md)
- Pattern 4 in [integration patterns](../standards/integration-patterns.md)
