# Blueprints & Starter Kits

Ready-to-scaffold project templates that let engineering teams start a compliant AI workload **without central involvement**, per the matching reference architecture.

## What a blueprint contains

Each blueprint (`blueprints/{workload}-starter-kit/`) provides:

1. **Scaffolded project structure** — working skeleton code with the approved stack wired up
2. **Infrastructure-as-code** — baseline deployment for the reference architecture's component view
3. **Guardrails pre-wired** — gateway client, logging with PII redaction, eval-in-CI setup
4. **Checklist** — the [design review checklist](../docs/design-review-checklist.md) pre-filled where the blueprint already satisfies the item; the team fills the rest
5. **README quickstart** — from clone to first working deployment in under an hour

## Roadmap

| Blueprint | Target RA | Status |
|---|---|---|
| _(fill)_ rag-starter-kit | [RAG](../reference-architectures/rag/) | Planned |
| _(fill)_ inference-starter-kit | [Inference](../reference-architectures/inference/) | Planned |
| _(fill)_ agent-starter-kit | [Agentic](../reference-architectures/agentic/) | Planned |

## Rules

- Blueprints use **only** [approved technologies](../standards/approved-technologies.md); when a standard changes, the blueprint changes in the same PR
- Blueprints are opinionated: customization is fine, but removing guardrails is not
- Teams own their forked/scaffolded project after generation; blueprint maintainers own the template
