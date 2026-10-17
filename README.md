# Enterprise AI Reference Architecture

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs Status](https://img.shields.io/badge/docs-all-blue.svg)](docs/README.md)
[![Standards](https://img.shields.io/badge/standards-proposed-orange.svg)](standards/README.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A complete, vendor-neutral **architecture knowledge base for enterprise AI/ML**: reference architectures, technology standards, design patterns, blueprints, security controls, and the governance processes that keep them true — from prototype to production.

> **The premise:** central architecture does not scale by reviewing everything. It scales by publishing standards, checklists, and blueprints that engineering teams apply independently — while central architects focus on high-risk and novel designs.

---

## Table of Contents

- [Who this is for](#who-this-is-for)
- [Quick start](#quick-start)
- [Repository map](#repository-map)
- [The standards lifecycle](#the-standards-lifecycle)
- [Core workflows](#core-workflows)
- [Documentation catalog](#documentation-catalog)
- [Contributing](#contributing)
- [License](#license)

## Who this is for

- **Architects & tech leads** — designing or reviewing AI/ML systems who need canonical patterns and a defensible review process
- **Engineering teams** — starting a new AI initiative who want a compliant head start without waiting on central review
- **Governance & security partners** — aligning AI controls, SSDLC, and red-teaming with architecture practice

## Quick start

1. **Pick your workload** — find your scenario in [`reference-architectures/`](reference-architectures/) (training, inference, RAG, agentic, fine-tuning, data agent, copilots, intelligent automation)
2. **Conform or deviate** — full conformance = self-certify with the [design review checklist](docs/design-review-checklist.md); deviations = [ADR](adr/README.md) + [review](docs/architecture-review-process.md)
3. **Choose approved tech** — anything not on [`standards/approved-technologies.md`](standards/approved-technologies.md) requires [evaluation](docs/technology-evaluation-criteria.md)
4. **Ship safely** — gates from [prototype → production](docs/poc-to-production.md) with [security controls](security/ai-security-controls.md) at every phase

## Repository map

```mermaid
flowchart TB
    subgraph Governance [Governance]
        DOCS[docs/<br/>review process · NFRs · build-vs-buy · value]
        ADR[adr/<br/>decision records]
        TPL[templates/ · .github/<br/>PR & issue templates]
    end
    subgraph Knowledge [Architecture Knowledge]
        RA[reference-architectures/<br/>8 workload types]
        PAT[design-patterns/<br/>reusable solutions]
        STD[standards/<br/>approved tech · protocols · integration]
        BP[blueprints/<br/>starter kits]
    end
    subgraph Assurance [Assurance]
        SEC[security/<br/>controls · SSDLC · red team]
        RES[research/<br/>briefs · prototypes]
    end

    RA --> PAT --> STD
    DOCS --> RA
    DOCS -->|feeds| ADR
    SEC -.controls.-> RA
    RES -.updates.-> STD
    BP -.embodies.-> RA
```

```
.
├── reference-architectures/   # Canonical designs per workload type (RA)
├── design-patterns/           # Reusable, cross-cutting patterns
├── standards/                 # Approved technologies & binding standards
├── blueprints/                # Starter kits for independent adoption
├── security/                  # AI controls, secure SDLC, red-team loop
├── research/                  # Briefs + time-boxed validation prototypes
├── adr/                       # Architecture Decision Records (numbered)
├── docs/                      # Processes: review, NFRs, value, lifecycle
├── templates/                 # Review request & reusable templates
└── .github/                   # PR/issue templates, CODEOWNERS
```

## The standards lifecycle

```
Horizon scan (research) → Time-boxed prototype → Research brief
    → Evaluation score → Cross-cutting review (EA · Cloud · Data · Security)
    → Publish standard → Blueprints & checklists → Independent adoption
```

Every standard carries a status — `Proposed → Approved → Deprecated → Removed` — and nothing is deleted; deprecations keep a 12-month trail.

## Core workflows

| I want to… | Do this |
|---|---|
| Start a new AI initiative | Match a [reference architecture](reference-architectures/); self-certify or request [review](docs/architecture-review-process.md) |
| Use a technology that isn't approved | Run an [evaluation](docs/technology-evaluation-criteria.md); add an ADR |
| Make a build-vs-buy call | Follow the [framework](docs/build-vs-buy-framework.md); record the outcome as an ADR |
| Take a prototype to production | Pass the five gates in [poc-to-production.md](docs/poc-to-production.md) |
| Evaluate a new/emerging technology | [Research process](research/README.md) → brief → standards update |
| Design a system of record integration | [Solution design lifecycle](docs/solution-design-lifecycle.md) + [legacy modernization](docs/legacy-modernization.md) |
| Quantify an initiative's value | [Business cases & value](docs/business-case-and-value.md) |

## Documentation catalog

| Document | Purpose |
|---|---|
| [docs/README.md](docs/README.md) | Index of all governance processes |
| [docs/architecture-review-process.md](docs/architecture-review-process.md) | Who reviews what — T0 self-cert → T3 governance |
| [docs/design-review-checklist.md](docs/design-review-checklist.md) | The review checklist (usable for self-certification) |
| [docs/non-functional-requirements.md](docs/non-functional-requirements.md) | NFR set with numbers, not adjectives |
| [docs/poc-to-production.md](docs/poc-to-production.md) | Five gated transitions to sustained operation |
| [docs/solution-design-lifecycle.md](docs/solution-design-lifecycle.md) | Discovery → design → diligence → deployment → expansion |
| [docs/technology-evaluation-criteria.md](docs/technology-evaluation-criteria.md) | Weighted scoring rubric (security = pass/fail gate) |
| [docs/build-vs-buy-framework.md](docs/build-vs-buy-framework.md) | Evidence-based build-vs-buy decisions |
| [docs/business-case-and-value.md](docs/business-case-and-value.md) | Opportunity discovery, ROI, KPIs, kill criteria |
| [docs/legacy-modernization.md](docs/legacy-modernization.md) | Incremental AI on existing systems |
| [security/README.md](security/README.md) | Controls, SSDLC, red-team integration |
| [standards/README.md](standards/README.md) | Approved technologies & binding standards |
| [research/README.md](research/README.md) | Horizon scanning & validation prototypes |
| [adr/README.md](adr/README.md) | Architecture Decision Records |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) — it defines change types, required reviewers, naming conventions, and the deprecation rule. Standards and reference architecture changes require cross-cutting review before adoption. Please also read our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT — see [LICENSE](LICENSE).
