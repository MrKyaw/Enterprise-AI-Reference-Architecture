# Legacy Modernization in the AI Era

**Status:** Proposed · **Last reviewed:** 2026-10-17

Most AI initiatives land on top of systems that predate them. This document defines how we modernize and integrate legacy applications while adding AI capability — without big-bang rewrites.

## Strategy: incremental, not big-bang

### Strangler-fig for AI integration

1. **Identify the seam** — the interface (API, event, database view) where the legacy system can be bypassed or augmented
2. **Route through a facade** — new AI-enabled capability sits behind a gateway/facade; traffic shifts incrementally
3. **Coexist safely** — legacy and new paths run in parallel with comparison/observability until parity is proven
4. **Retire deliberately** — decommission the old path only with measured evidence; transitional architecture is fine if the end state is documented

### Supporting techniques

- **Domain-driven design:** identify bounded contexts before deciding where AI capability attaches — AI features belong to a context, not smeared across the monolith
- **Event storming:** map the real process (not the documented one) to find where an AI decision point actually adds value
- **Transitional architectures:** temporary bridges (anti-corruption layers, sync jobs) are legitimate — each one gets an owner and a retirement date in an ADR

## Applying AI to legacy: order of operations

```
1. Instrument the legacy system        (observability first — you can't improve what you can't see)
2. Add AI in read-only mode            (summarize, classify, suggest — no side effects)
3. Add evaluation against real traffic (shadow mode; compare AI output to human/system decisions)
4. Add human-in-the-loop action        (per HITL approval pattern)
5. Only then consider autonomous action (agentic RA + direct architecture review required)
```

Skipping to step 4 or 5 on an un-instrumented legacy system is how AI projects become incidents.

## Constraints unique to legacy

- **Data access:** legacy databases often lack governance — apply [data protection controls](../security/ai-security-controls.md) at the integration boundary, not in the legacy system
- **Change windows:** design AI integrations to tolerate batch windows, eventual consistency, and schema drift
- **Skills:** modernization plans must fund the team that will *operate* the result, not only build it
- **Risk containment:** every phase keeps a rollback path; the strangler pattern exists so failure of the new path never breaks the old one

## Review requirements

- Modernization of a system of record → T2 central review (see [architecture review](architecture-review-process.md))
- Any transitional architecture without a retirement date → changes required
