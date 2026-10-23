# Enterprise AI Reference Architecture

[![Documentation validation](https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture/actions/workflows/mermaid-lint.yml/badge.svg)](https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture/actions/workflows/mermaid-lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: proposed guidance](https://img.shields.io/badge/status-proposed%20guidance-blue)](docs/README.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

A vendor-neutral collection of enterprise AI architecture guidance, customer-facing leadership practices, decision frameworks, and runnable starter scaffolds. Use it to connect business discovery, solution design, hands-on validation, security review, delivery, operations, and outcome measurement.

The content is a public reference for adaptation. Proposed standards are not evidence of organizational approval, regulatory compliance, customer deployment, or production certification. Starter kits expose working service skeletons with placeholder pipelines; implementing a real workload requires domain logic, authentication, integration, evaluation, and operational assurance.

[Start here](#start-here) · [Leadership](#practical-architecture-leadership) · [Catalog](#content-catalog) · [Starter kits](#run-a-starter-kit) · [Validation](#validation-and-evidence) · [Privacy](#public-information-and-privacy) · [Contributing](CONTRIBUTING.md)

## Who this is for

- **Enterprise architects:** align capabilities, standards, governance, investment, and lifecycle decisions.
- **Solution architects:** discover customer constraints, compare options, define contracts, and coordinate delivery.
- **AI and principal architects:** validate model/data assumptions, design controls, inspect implementations, and guide operations.
- **Engineering and platform leads:** use patterns, starter scaffolds, review checklists, and failure scenarios to make delivery decisions.

This is a set of practices and examples to evaluate in your environment. Read the status and scope of each document before adopting it.

## Start here

1. **Understand the problem.** Capture the business owner, affected workflow, baseline, constraints, and success/stop criteria in the [engagement worksheet](templates/architecture-leadership-engagement.md).
2. **Select the relevant design.** Match a [use case](use-cases/README.md) to one of the [reference architectures](reference-architectures/README.md); document alternatives and assumptions.
3. **Validate the risky parts.** Run a bounded prototype or integration experiment and record reproducible evidence. Use the [technology evaluation criteria](docs/technology-evaluation-criteria.md).
4. **Agree the controls and decision.** Apply the [design review checklist](docs/design-review-checklist.md), [AI security controls](security/ai-security-controls.md), and your organization's decision rights.
5. **Implement and operate.** Extend a [starter kit](blueprints/README.md), complete the [production gates](docs/poc-to-production.md), rehearse recovery, and agree receiving ownership.
6. **Check the outcome.** Compare reliability, adoption, costs, and business results with the original [business case](docs/business-case-and-value.md) before expansion.

## Practical architecture leadership

**Customer obsession · Technical credibility · Ownership · Trust · Delivery · Business impact**

The [practical leadership guide](docs/practical-architecture-leadership.md) translates leadership principles into decisions and work products that an architect can demonstrate:

- All 16 Amazon Leadership Principles mapped to architect behaviors, evidence, and warning signals, with primary-source attribution.
- Ten complementary leadership behaviors: consultative, servant, situational, transformational, technical, adaptive, collaborative, outcome-based, ethical, and coaching.
- Eight customer stages from discovery to expansion, with artifacts, owners, and exit evidence.
- An illustrative retail integration walkthrough covering source contracts, idempotency, delayed data, recovery, and decision trade-offs.
- Customer relationship habits, a delivery cadence, and authentic interview stories grounded in work you can substantiate.

Use the [engagement worksheet](templates/architecture-leadership-engagement.md) to record the baseline, assumptions, options, experiments, decisions, readiness, and outcome review. The guide complements the [solution design lifecycle](docs/solution-design-lifecycle.md); it does not add another approval chain.

## Content catalog

The following inventory reflects files in this repository, reviewed on **2026-10-22**. A file count measures the collection's scope, not the completeness or maturity of an implementation.

| Collection | Inventory | What you can use |
|---|---|---|
| [Lifecycles](lifecycles/README.md) | **24 lifecycles** | Activities, artifacts, exit gates, and ownership through delivery and retirement |
| [Reference architectures](reference-architectures/README.md) | **9 reference architectures** | 8 workload architectures plus the enterprise-first family (secure agentic enterprise and 19 first-principle blueprints) |
| [Design patterns](design-patterns/README.md) | **13 catalogs + 5 expanded treatments** | Software, data, ML, MLOps, GenAI, RAG, agents, reliability, security, UX, scaling, cost, domain patterns |
| [Approaches](approaches/README.md) | **3 guidance documents** | Driven-development methods, delivery practices, and testing strategy |
| [Use cases](use-cases/README.md) | **8 use cases** | Problem statements, workflows, options, trade-offs, candidate metrics, and failure modes |
| [Production issues](production-issues/README.md) | **79 indexed scenarios in 6 categories** | Quality, retrieval, cost/latency, security, agents/tools, platform operations |
| [Blueprints](blueprints/README.md) | **18 starter kits + 20 enterprise-first blueprints** | Service skeletons, pipeline stubs, smoke tests, Terraform baselines, readiness checklists, and enterprise architecture blueprints |
| [Governance](docs/README.md) | Process guides | Discovery, diligence, review, NFRs, value, modernization, and leadership |
| [Standards](standards/README.md) | Proposed templates | Technologies, model providers, integration, agent protocols, AI-assisted development |
| [Security](security/README.md) | Controls and review guidance | Secure SDLC, AI controls, red-team feedback |
| [Research](research/README.md) | Templates and an evaluation plan | Hypotheses, authorized experiments, reproducibility, and decision evidence |
| [ADRs](adr/README.md) | Decision-record template | Context, alternatives, trade-offs, ownership, consequences |
| [Architect resources](resources/README.md) | Role paths and curated references | Technical foundations, leadership, implementation skills, and learning plans |

### Lifecycle map

| Area | Included lifecycles |
|---|---|
| Software and product | Software development, product, technology, API, experimentation, documentation/knowledge, enablement/adoption |
| Data and models | Data, ML project, MLOps, model risk, evaluation |
| Generative AI | GenAI/LLMOps, RAG, prompts, agents, agent factory |
| Operations and commercial | Operations/incidents, FinOps, vendors/third parties |
| Specialized domains | Edge AI, quantum computing, physical AI, embodied AI |

The cross-cutting [solution design lifecycle](docs/solution-design-lifecycle.md) lives in `docs/` and is separate from the 24 lifecycle files.

### Patterns and approaches

The pattern catalogs cover intent, applicability, trade-offs, and common mistakes. Expanded documents cover the [LLM gateway](design-patterns/llm-gateway.md), [human approval](design-patterns/human-in-the-loop-approval.md), [evaluation in CI](design-patterns/evaluation-in-ci.md), [architecture as code](design-patterns/architecture-as-code.md), and [semantic grounding](design-patterns/semantic-layer-grounding.md).

The [development approaches](approaches/driven-development-approaches.md) include test-, behavior-, acceptance-, domain-, data-, model-, evaluation-, prompt-, retrieval-, security-, contract-, documentation-, outcome-, and evidence-driven practices. Select methods according to the problem and risk; their names do not establish that a design is correct.

## Enterprise-first architecture blueprints

Architecture blueprints where one concern is the primary optimization target. They are design documents, not runnable starter kits.

| Blueprint family | Documents | Use when |
|---|---|---|
| [Enterprise-first](reference-architectures/enterprise-first/README.md) | 20 blueprints: secure agentic enterprise plus production-first, AI-first, compliance-first, quality-first, security-first, data-first, user-first, cost-first, resilience-first, governance-first, privacy-first, observability-first, evaluation-first, ethics-first, explainability-first, accessibility-first, sustainability-first, safety-first, and interoperability-first | A single concern must be the tie-breaker in an enterprise AI design |

## Run a starter kit

Requires Python 3.12 for the documented example. Run each kit in its own environment because the skeletons use the same module names.

```sh
git clone https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture.git
cd Enterprise-AI-Reference-Architecture/blueprints/inference-starter-kit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
PYTHONPATH=src pytest -q
PYTHONPATH=src uvicorn main:app --host 127.0.0.1 --port 8080
```

From another terminal:

```sh
curl http://127.0.0.1:8080/health
curl -X POST http://127.0.0.1:8080/v1/run \
  -H 'Content-Type: application/json' \
  -d '{"input":"smoke test","tenant_id":"demo"}'
```

The expected pipeline status is `scaffold`. A `tenant_id` in a request is an input value, not authenticated tenant identity. The local input screening and regex redaction are examples, not comprehensive authorization, injection prevention, or privacy controls. Keep the skeleton local until the required controls are implemented.

### Kit families

| Family | Kits |
|---|---|
| Core workload designs | inference, rag, agent, data-agent, copilot, fine-tuning, training, intelligent-automation |
| Specialized domains | edge-ai, physical-ai, embodied-ai, quantum, agent-factory |
| Cross-cutting | evaluation, observability, ai-security, integration |
| Integrated enterprise | secure-agentic-enterprise |

Each kit contains a FastAPI skeleton, typed models, placeholder pipeline steps, input-screening examples, smoke tests, a non-root Dockerfile, and a Terraform baseline. Infrastructure files are starting points that need environment-specific review; they are not deployed infrastructure or evidence of a successful cloud validation.

Read the [blueprint catalog](blueprints/README.md) and the selected kit's README before implementation. Copying `.env.example` does not load it into the Python process automatically; export required settings explicitly.

## Architecture work and decisions

| Goal | Start with |
|---|---|
| Lead discovery and earn customer confidence | [Leadership guide](docs/practical-architecture-leadership.md) and [worksheet](templates/architecture-leadership-engagement.md) |
| Design an integration or modernization | [Solution lifecycle](docs/solution-design-lifecycle.md), [integration patterns](standards/integration-patterns.md), [legacy modernization](docs/legacy-modernization.md) |
| Compare technologies or build vs buy | [Evaluation criteria](docs/technology-evaluation-criteria.md), [build-vs-buy framework](docs/build-vs-buy-framework.md), [ADR template](adr/0000-template.md) |
| Define acceptance criteria | [NFRs](docs/non-functional-requirements.md), [testing strategy](approaches/testing-strategy.md), [evaluation lifecycle](lifecycles/evaluation-lifecycle.md) |
| Review a design | [Review process](docs/architecture-review-process.md), [checklist](docs/design-review-checklist.md), [review request](templates/design-review-request.md) |
| Prepare production operation | [POC-to-production gates](docs/poc-to-production.md), [operations lifecycle](lifecycles/operations-incident-lifecycle.md), [failure scenarios](production-issues/README.md) |
| Grow team capability | [Architect resource hub](resources/README.md), [enablement lifecycle](lifecycles/enablement-adoption-lifecycle.md) |

### Governance status

Documents marked `Proposed` describe practices to review and adapt. A reference to “approved” technology describes the approval process an adopting organization must establish; the public list is a template with unfilled entries. This repository does not grant internal approval or verify a deployment's compliance.

Changes follow the [contribution and review process](CONTRIBUTING.md). Standards and reference-architecture changes need the reviewers and control evidence specified there. Identify real decision-makers in your organization rather than copying placeholder roles as if a review had occurred.

## Validation and evidence

Documentation validation checks tracked Markdown links, code fences, collection counts, excluded private-file types, named customer references, and Mermaid syntax. It does not certify architectural correctness, external website availability, legal compliance, or freedom from all sensitive information.

Requires Node.js 22.12+ and Python 3.12 for the CI tooling:

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm test
```

To scan secrets locally with Gitleaks installed:

```sh
gitleaks git --log-opts=--all --redact --no-banner .
```

The local review passed checks for **169 Markdown files**, **61 Mermaid diagrams**, and **68 smoke tests across 17 starter kits**. The locked documentation tooling had **0 npm audit findings** at review time. The kit tests emit an upstream dependency deprecation warning, recorded in the review.

See the [publication and validation review](docs/publication-review.md) for the scope, results, limitations, and public metadata considerations. Blueprint smoke checks exercise the skeletons; provider integrations, model quality, cloud deployments, and workload performance require separate validation.

### Measure business outcomes honestly

| Area | Useful measure | Agreement required |
|---|---|---|
| Quality | Correctness, grounded answers, harmful-output rates, task success | Representative evaluation data, slice coverage, acceptance threshold |
| Reliability | Availability, error rate, recovery time, freshness | SLO, measurement window, operational owner |
| Latency | End-to-end p50/p95/p99 under the intended workload | Workload, concurrency, error accounting, target |
| Cost | Build/run/support cost per completed task | Attribution model, review effort, budget envelope |
| Adoption and trust | Active usage, abandonment, authorized customer feedback | Baseline, observation period, privacy controls |
| Business impact | Cycle time, error reduction, realized capacity, revenue protection | Business owner, baseline, attribution limits |

Targets in examples are illustrative until agreed for a specific engagement. Do not claim performance improvements, customer outcomes, or cost savings without reproducible evidence and permission to share it.

## Public information and privacy

Publish only generic architecture practices, authorized public references, synthetic fixtures, and appropriately reviewed examples. Keep customer identities, employer-confidential details, live transcripts, internal topology, credentials, cloud state, and restricted benchmark data outside this public repository.

The [leadership guide](docs/practical-architecture-leadership.md) uses a company-neutral illustrative scenario. The [embedding research documents](research/briefs/2026-10-embedding-evaluation.md) are an evaluation plan, not published experimental findings or customer evidence.

Secret scans can find supported credential patterns; they cannot prove that every document is non-confidential. Historical Git commits retain author metadata, including an email address. Updating files does not remove information from old commits, forks, caches, or previously downloaded copies. See [publication guidance](docs/publication-review.md) and [SECURITY.md](SECURITY.md) before publishing sensitive material.

## Repository map

```text
reference-architectures/   Proposed workload designs
lifecycles/               Delivery, model, data, operations, and retirement phases
design-patterns/          Pattern catalogs and expanded treatments
approaches/               Development methods, delivery practices, testing
use-cases/                Business scenarios and design trade-offs
production-issues/        Failure scenarios and prevention guidance
blueprints/               17 runnable starter scaffolds
standards/                Proposed technology and integration templates
security/                 Security controls and review practices
research/                 Research templates and an evaluation plan
docs/                     Governance, leadership, and publication review
templates/                Review request and engagement worksheet
resources/                Architect competencies and learning references
adr/                      Architecture decision records
.github/                  Validation scripts, workflow, issue forms, ownership
```

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Open focused pull requests with the problem, resulting behavior, and validation evidence. Use the [changelog](CHANGELOG.md) for content history; unreleased additions are not a published version or approval record.

Before publication, review the complete diff for customer information, credentials, claims, source attribution, broken links, and ownership assumptions. Add new documents to their directory index and link them to the lifecycle or decision they support.

## License

[MIT](LICENSE). Original copyright notices are preserved. Linked third-party resources retain their own terms and licenses.

---

⭐ Star this repo if you find it useful!

[Report Bug](https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture/issues/new?template=bug_report.yml) · [Request Feature](https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture/issues/new?template=feature_request.yml) · [Ask Question](https://github.com/MrKyaw/Enterprise-AI-Reference-Architecture/issues/new?template=question.yml)
