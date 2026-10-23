# Enterprise-First Reference Architectures

Architecture blueprints that make one concern the **primary optimization target**. Each document defines the principle, decision rules, required components, security and operational expectations, metrics, and anti-patterns. Other concerns are treated as explicit constraints with budgets.

These are **design documents**, not runnable starter kits. For runnable scaffolds, see [blueprints/](../../blueprints/README.md).

## Blueprints

| Blueprint | Primary concern | Use when |
|---|---|---|
| [Secure Agentic Enterprise](secure-agentic-enterprise.md) | End-to-end secure agent platform | Multiple agents, tools, and business systems with security and governance as constraints |
| [Production-First Enterprise Architecture](production-first.md) | Optimize for reliable operation in production before optimizing for feature richness or demo impact | Use when an AI capability will carry business-critical traffic, has an on-call owner, and must meet availability, latency, and recovery commitments. |
| [AI-First Enterprise Architecture](ai-first.md) | Design the system so AI is the primary interaction and computation layer, with traditional software providing guardrails, state, and determinism | Use when the core user value comes from judgment, generation, retrieval, or automation that deterministic code cannot provide. |
| [Compliance-First Enterprise Architecture](compliance-first.md) | Treat regulatory, contractual, and policy obligations as first-class design inputs and release gates, not as a late-stage review | Use for regulated data, customer-facing AI, or any workload subject to audit, retention, residency, or sector-specific rules. |
| [Quality-First Enterprise Architecture](quality-first.md) | Optimize for correctness, safety, and usefulness first; treat speed and cost as constraints, not the objective | Use when output quality directly affects trust, revenue, safety, or regulatory exposure. |
| [Security-First Enterprise Architecture](security-first.md) | Threat model and control design precede feature design; assume the model can be manipulated and keep controls outside the model | Use for any AI workload with external input, tool access, sensitive data, or side effects. |
| [Data-First Enterprise Architecture](data-first.md) | Make data quality, governance, lineage, and access policy the foundation; models and applications are consumers of governed data | Use when AI outputs depend on enterprise data, especially analytics, RAG, or data agents. |
| [User-First (Human-Centered) Enterprise Architecture](user-first.md) | Optimize for human outcomes, transparency, and control; AI is in service of the user, not the other way around | Use for user-facing AI, copilots, decision support, and any system where adoption and trust determine value. |
| [Cost-First (FinOps-First) Enterprise Architecture](cost-first.md) | Make unit economics a design constraint from day one; every AI capability must justify its cost per successful outcome | Use for high-volume or long-running AI workloads, or when AI spend is a material budget line. |
| [Resilience-First Enterprise Architecture](resilience-first.md) | Design for graceful degradation and recovery; a manipulated or failed model must not take down the business process | Use for customer-facing, revenue-critical, or safety-relevant AI systems. |
| [Governance-First Enterprise Architecture](governance-first.md) | Make ownership, risk tiering, decision rights, and approval explicit before any AI system reaches production | Use in organizations with multiple AI teams, regulated domains, or shared platforms. |
| [Privacy-First Enterprise Architecture](privacy-first.md) | Minimize data collection and exposure; enforce residency, consent, and deletion as system properties, not policy documents | Use whenever personal, customer, employee, or regulated data touches AI pipelines. |
| [Observability-First Enterprise Architecture](observability-first.md) | Instrument for understanding before optimizing; every AI request must be traceable, measurable, and debuggable in production | Use for any AI workload in production, especially where quality decay is invisible to uptime monitoring. |
| [Evaluation-First Enterprise Architecture](evaluation-first.md) | Define success, datasets, and gates before building; no AI behavior change ships without measured evidence | Use for any AI capability whose quality is not self-evident from unit tests. |
| [Ethics-First Enterprise Architecture](ethics-first.md) | Assess and mitigate societal, fairness, and bias impacts before deploying AI that affects people | Use for AI that influences decisions about individuals, groups, or access to services. |
| [Explainability-First Enterprise Architecture](explainability-first.md) | Make AI decisions inspectable, attributable, and contestable by default | Use for decision support, regulated domains, or any AI output that users or auditors must trust. |
| [Accessibility-First Enterprise Architecture](accessibility-first.md) | Design AI interactions for the widest range of users and abilities from the start | Use for any user-facing AI, including copilots, chat, and automated communications. |
| [Sustainability-First Enterprise Architecture](sustainability-first.md) | Treat energy and carbon as design constraints; prefer efficient models and measure impact per outcome | Use for large-scale or always-on AI systems, or where sustainability targets are contractual. |
| [Safety-First Enterprise Architecture](safety-first.md) | Prevent harm first; autonomous and physical actions are bounded by validated envelopes and independent stop paths | Use for agentic systems with side effects, physical AI, embodied AI, or high-impact automation. |
| [Interoperability-First Enterprise Architecture](interoperability-first.md) | Prefer open standards and portable contracts so systems can evolve without lock-in | Use for enterprise platforms, integration-heavy systems, and multi-vendor environments. |

## How to use these blueprints

1. **Pick the blueprint whose primary concern matches your dominant risk.** Most systems need several; choose one as the tie-breaker.
2. **Record the choice and any deviations as an ADR.**
3. **Map the blueprint's metrics to your SLOs and dashboards before implementation.**
4. **Review against the [design review checklist](../../docs/design-review-checklist.md).**

## Related

- [Reference architectures](../README.md)
- [Design patterns](../../design-patterns/README.md)
- [Security controls](../../security/ai-security-controls.md)
- [Non-functional requirements](../../docs/non-functional-requirements.md)
- [Architecture review process](../../docs/architecture-review-process.md)
