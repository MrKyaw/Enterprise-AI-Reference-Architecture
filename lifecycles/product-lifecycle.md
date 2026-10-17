# Product Lifecycle (AI)

**Status:** Proposed · **Owner:** Product · **Last reviewed:** 2026-10-17

The outermost lifecycle: how an AI capability moves from an idea to sustained value — and how it ends. Every technical lifecycle nests inside this one.

## Phases

### 1. Ideation & opportunity
- Source ideas from: business pain points, process discovery, support/ops friction, data assets, capability pull (what the platform now makes possible)
- Maintain an opportunity register with rough value/effort/risk scores
- Kill weak ideas early and cheaply
- **Artifact:** opportunity entry

### 2. Discovery & validation
- Talk to real users; observe the actual workflow (not the documented one)
- Define the problem statement and the measurable outcome
- Test the core assumption with a cheap [prototype](../research/prototypes/TEMPLATE.md) per the [research rules](../research/README.md)
- **Gate:** is the problem real, frequent, and worth solving?
- **Artifact:** discovery summary + validated problem statement

### 3. Business case
- Quantified benefit, cost (including sustained run cost), time-to-value, risk-adjusted
- Build vs buy recommendation with evidence ([framework](../docs/build-vs-buy-framework.md))
- **Gate:** funding decision ([business case & value](../docs/business-case-and-value.md))
- **Artifact:** business case + ADR

### 4. Delivery
- Architecture per applicable [reference architecture](../reference-architectures/) via [solution design lifecycle](../docs/solution-design-lifecycle.md)
- Engineering lifecycles execute here ([SDLC](software-development-lifecycle.md), [ML project](ml-project-lifecycle.md), [GenAI](genai-llmops-lifecycle.md))
- [PoC-to-production gates](../docs/poc-to-production.md) govern promotion
- **Artifact:** shipped capability + production readiness record

### 5. Launch & adoption
- Enablement: documentation, training, champions, in-product guidance
- Adoption tracking against baseline; be honest about the adoption curve
- Feedback loops wired into the backlog
- **Artifact:** launch plan + adoption dashboard

### 6. Value realization
- Measure against the business case at 30/90/180 days; report honestly including attribution limits
- Iterate on the levers that move the outcome metric
- **Gate:** is value materializing? If not, diagnose (usability? accuracy? adoption?) before expanding scope
- **Artifact:** value report

### 7. Expansion & scale
- Extend to new use cases, teams, regions, or data sources — each expansion re-runs proportionate discovery/diligence
- Platform-ize what's repeatedly needed into [blueprints](../blueprints/)

### 8. Steady state
- Owned, SLO'd, on-call, budgeted; maintenance cadence defined
- Periodic re-evaluation of value and risk

### 9. Sunset
- Pre-agreed kill criteria evaluated honestly
- Deprecation notice, user migration, data deletion, cost removal
- **Artifact:** sunset decision + decommission record

## Product management for AI: what's different

| Traditional product | AI product |
|---|---|
| Deterministic features | Probabilistic behavior; quality is a spectrum |
| "Done" is definable | "Good enough" must be defined as a threshold and revisited |
| Launch is the midpoint | Launch is the start of continuous evaluation |
| Failures are bugs | Failures include confident wrong answers — trust is fragile and slow to rebuild |
| Adoption depends on usefulness | Also depends on **trust** and demonstrable accuracy |
| Fixed capability | Capability changes when the model/provider changes |

## Trust-building sequence

```
Accuracy on a narrow task → Transparency (citations, confidence) → User control (edit/override)
    → Reliability over time → Expanded scope → Broader autonomy
```

Skip a step and adoption stalls at the first surprising failure.

## Anti-patterns

- Solution looking for a problem (technology-first ideation)
- Value claims never measured post-launch
- Expanding scope before the core use case proves trust
- No kill criteria — zombie initiatives consuming budget indefinitely
- Users never migrated at sunset; old and new run forever
