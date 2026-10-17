# Production Issues

Real failure modes observed in production AI/ML systems — with symptom, root cause, impact, fix, prevention, and the open work that remains. Every entry maps back to a pattern, control, or lifecycle so the fix is structural, not tribal.

## Why this exists

Most AI incidents are **not novel**. They are recurring, well-understood failure modes that teams rediscover one at a time. This library is the memory of the organization: read it before designing, and add to it after every incident.

**Every production incident becomes an entry here** ([operations lifecycle](../lifecycles/operations-incident-lifecycle.md)), and every entry links to the controlling artifact that prevents recurrence.

## Categories

| File | Focus | Issues | Prefix |
|---|---|---|---|
| [quality-and-hallucination.md](quality-and-hallucination.md) | Wrong, unsupported, or confidently bad output | 13 | `Q-` |
| [retrieval-and-data.md](retrieval-and-data.md) | Retrieval, indexing, data quality, ACLs, freshness | 13 | `R-` |
| [cost-and-latency.md](cost-and-latency.md) | Spend spikes, runaway cost, latency regressions | 12 | `C-` |
| [security-and-injection.md](security-and-injection.md) | Injection, exfiltration, secrets, permissions | 13 | `S-` |
| [agents-and-tools.md](agents-and-tools.md) | Tool misuse, loops, unsafe actions, autonomy | 13 | `A-` |
| [platform-operations.md](platform-operations.md) | MLOps, drift, scaling, incidents, vendors, governance | 15 | `O-` |

## Entry format

Each issue includes:

| Field | Meaning |
|---|---|
| **Symptom** | What you observe first (often a user complaint, not an alert) |
| **Root cause** | The system condition that produces it |
| **Impact** | Business/technical consequence and blast radius |
| **Fix** | Immediate remediation |
| **Prevention** | Structural control, pattern, or lifecycle gate that stops recurrence |
| **Future work** | What is still unsolved — honest open problems |

## Severity guide

| Severity | Definition | Response |
|---|---|---|
| **Critical** | Harm to people/customers, data breach, unauthorized action, regulatory exposure | Immediate containment; incident declared |
| **High** | Silent quality collapse, cost runaway, availability loss on a critical path | Mitigate within the day; root-cause within a week |
| **Medium** | Degraded quality, elevated cost, user-visible inconsistency | Planned fix in the next cycle |
| **Low** | Friction, minor inaccuracy, cosmetic trust erosion | Backlog |

## How to use before designing

1. Scan the categories relevant to your planned workload
2. For each issue, confirm the **prevention** control is in your design
3. If a prevention control is missing from our standards, propose an update ([CONTRIBUTING](../CONTRIBUTING.md))
4. Add anticipated failure modes to your design review submission

## The five cross-cutting causes

Across all 79 catalogued issues, five causes recur:

1. **Unmeasured change** — something changed (prompt, model, index, data) without evaluation ([EDD](../approaches/driven-development-approaches.md))
2. **Controls in the model instead of around it** — prompt instructions used as security/safety controls ([controls](../security/ai-security-controls.md))
3. **No attribution or visibility** — cost, quality, or permission failures invisible until they hurt ([FinOps](../lifecycles/finops-cost-lifecycle.md))
4. **Silent divergence** — train/serve, definition drift, index staleness, provider version changes ([MLOps](../lifecycles/mlops-lifecycle.md))
5. **Unbounded behavior** — loops, context, retries, autonomy without ceilings ([agent lifecycle](../lifecycles/agent-lifecycle.md))

Fix the cause pattern, not just the instance.

## Contributing an issue

After any incident, add an entry with the fields above, link it from the category table, and open a PR. If the issue generalizes to a control or pattern, update that artifact in the same PR ([red-team loop](../security/red-team-integration.md)).
