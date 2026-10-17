# Solution Design Lifecycle

**Status:** Proposed · **Last reviewed:** 2026-10-17

Architecture work spans the full lifecycle of a solution — not just the build. This document defines the standard phases and the architecture artifact required at each. Applies whether the "customer" is an internal business unit or an external client.

## Phases

### 1. Technical discovery
**Goal:** understand the environment before proposing anything.

- Map the existing landscape: systems of record (ERP, CRM, POS, order management, inventory, data platforms), integration fabric, identity, cloud footprint
- Identify data: classifications, volumes, quality, owners, residency constraints
- Identify stakeholders: business sponsor, technical owners, security, data governance
- Capture constraints: compliance regimes, latency/availability expectations, budget envelope

**Artifact:** discovery summary (one page) + current-state diagram.

### 2. Solution design
**Goal:** a design that maps explicitly onto published standards.

- Select the applicable [reference architecture](../reference-architectures/)
- Component view, data flows, integration patterns from [integration-patterns](../standards/integration-patterns.md)
- [NFRs](non-functional-requirements.md) stated with numbers
- Deviations listed with ADR drafts

**Artifact:** design document + future-state diagram + deviation list.

### 3. Technical diligence
**Goal:** survive scrutiny from security, data, and architecture reviewers.

- Security: threat model, [controls mapping](../security/ai-security-controls.md), data-flow review
- Data: classification, lineage, retention, cross-boundary transfers
- Architecture: conformance to standards; deviations justified with evidence
- Commercial: [build-vs-buy](build-vs-buy-framework.md) and [evaluation](technology-evaluation-criteria.md) evidence if new technology is involved

**Artifact:** completed [design review checklist](design-review-checklist.md) + review outcome.

### 4. Onboarding / deployment
**Goal:** implement without re-litigating the design.

- Environment provisioning via IaC / [architecture-as-code](../design-patterns/architecture-as-code.md)
- Integration testing against real interfaces (contract tests, not mocks only)
- Evaluation baseline captured *before* go-live
- Operational readiness review: runbook, on-call, dashboards, budgets

**Artifact:** deployment record + readiness sign-off.

### 5. Expansion
**Goal:** grow into new use cases, data sources, or regions without rework.

- Each expansion re-runs phases 1–3 proportionally (a new data source is a discovery + diligence pass, not a full rebuild)
- Reusable components from [blueprints](../blueprints/) preferred over net-new builds
- Lessons from expansion feed back into standards and reference architectures

**Artifact:** expansion delta design + updated ADRs.

## Translation discipline

At every phase, maintain two views of the same design:

- **Stakeholder view:** problem, value, risk, timeline — no jargon
- **Engineering view:** components, contracts, NFRs, runbooks

If a design only exists in one view, it isn't finished. Executive-ready communication and whiteboard-level technical depth are the same skill applied to different audiences.
