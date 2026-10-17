# Enterprise AI Reference Architecture

Central source of truth for **reference architectures, technology standards, design patterns, and platform strategy** for AI/ML workloads.

This repository is how we scale architecture: instead of reviewing every initiative centrally, we publish standards, blueprints, and checklists that project architects and tech leads can apply independently.

---

## Contents

| Directory | Purpose |
|---|---|
| [`reference-architectures/`](reference-architectures/) | Canonical reference architectures per workload type (training, inference, RAG, agentic, fine-tuning) |
| [`design-patterns/`](design-patterns/) | Reusable, cross-cutting implementation patterns |
| [`standards/`](standards/) | Approved technologies, frameworks, model providers, data platforms, integration patterns |
| [`blueprints/`](blueprints/) | Starter kits engineering teams can scaffold from without central involvement |
| [`security/`](security/) | AI security controls, secure-design requirements, red-team integration |
| [`adr/`](adr/) | Architecture Decision Records (numbered, immutable once accepted) |
| [`research/`](research/) | Horizon-scanning briefs and time-boxed validation prototypes |
| [`docs/`](docs/) | Governance processes: design review, technology evaluation, build-vs-buy |

## How to use this repo

1. **Starting a new AI initiative?** Start from the matching reference architecture in [`reference-architectures/`](reference-architectures/). If your design conforms, no central review is needed — just record deviations as ADRs in your own project.
2. **Choosing a technology?** Check [`standards/approved-technologies.md`](standards/approved-technologies.md) first. Anything not on the approved list requires a time-boxed evaluation (see [`docs/technology-evaluation-criteria.md`](docs/technology-evaluation-criteria.md)).
3. **High-risk or novel design?** Open a design review per [`docs/architecture-review-process.md`](docs/architecture-review-process.md) and use [`docs/design-review-checklist.md`](docs/design-review-checklist.md).
4. **Build vs buy decision?** Follow [`docs/build-vs-buy-framework.md`](docs/build-vs-buy-framework.md) and record the outcome as an ADR.

## Lifecycle

- **Proposed** → **Accepted** → **Deprecated** → **Removed**
- Standards and reference architectures are reviewed every 6 months or immediately when validated research changes the landscape (see [`research/`](research/)).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All changes go through pull request review by the architecture team; standards changes additionally require cross-cutting review with Enterprise Architecture, Cloud Platform, Data, and Cybersecurity.

## License

MIT — see [LICENSE](LICENSE).
