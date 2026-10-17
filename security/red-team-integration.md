# Red-Team Integration

**Status:** Proposed · **Owner:** Cybersecurity · **Last reviewed:** 2026-10-17

How adversarial testing (red-teaming) connects to architecture: findings must change controls and standards, not just individual systems.

## Cadence

| Trigger | Scope |
|---|---|
| Before production | Agentic systems and any user-facing AI capability (control AI-10) |
| Major change | New agent capability, new tool class, new provider, significant prompt/agent-loop change |
| Periodic | Annual red-team of the AI gateway and top N systems by blast radius |
| Event-driven | Within 2 weeks of a significant public AI attack technique becoming known (horizon scanning feeds this — see [research/](../research/)) |

## Method

1. **Threat model** — assets, trust boundaries, attacker goals (data exfiltration, unauthorized actions, cost abuse, information disclosure)
2. **Adversarial testing** — attack classes: prompt injection (direct & indirect), jailbreaks, tool abuse, data poisoning, extraction of system prompts/PII, multi-turn manipulation, supply-chain (malicious retrieved content)
3. **Scoring** — severity × exploitability × blast radius
4. **Remediation** — fixes at three levels:
   - **System** — immediate patch, mandatory
   - **Control** — update [ai-security-controls.md](ai-security-controls.md) if the gap is general
   - **Architecture** — update a reference architecture or pattern if the gap is structural

## Feedback loop into architecture

```
Red-team finding
  → logged (issue, severity, affected systems)
  → system fixes tracked to closure
  → generalize-or-not decision within 30 days
      → if generalized: control/RA/pattern update PR in this repo
      → if not: rationale recorded so the question is closed
```

- Findings that generalize become **required updates to standards** — this is how the architecture absorbs new attack knowledge without waiting for the next design review cycle.
- New attack classes discovered in research prototypes feed the annual red-team scope.

## Roles

- **Cybersecurity** owns testing, severity, and the mandate to block go-live
- **AI Architecture** owns the generalize-or-not decision and the resulting repo changes
- **Project teams** own remediation of their systems
