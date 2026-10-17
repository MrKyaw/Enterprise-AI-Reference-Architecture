# Standards

Binding technology standards for AI/ML at Mobility Global. "Approved" means: proven in our environment, supported centrally, and secure by default. Anything else needs an evaluation.

## Documents

| Standard | Scope | Status |
|---|---|---|
| [approved-technologies.md](approved-technologies.md) | Frameworks, platforms, data tooling — the master approved list | Proposed |
| [model-provider-standards.md](model-provider-standards.md) | Hosted model providers: selection, contracts, data handling | Proposed |
| [integration-patterns.md](integration-patterns.md) | How AI capabilities integrate with enterprise systems | Proposed |

## How standards are set and changed

1. **Horizon scan** — emerging tech assessed via time-boxed prototypes (see [`research/`](../research/)).
2. **Evaluation** — scored against [`technology-evaluation-criteria.md`](../docs/technology-evaluation-criteria.md).
3. **Cross-cutting review** — Enterprise Architecture, Cloud Platform, Data, and Cybersecurity review before adoption.
4. **Publish** — standard updated here; deprecations follow the 12-month retention rule in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Status values

`Proposed` → `Approved` → `Deprecated` → `Removed`

Using a `Deprecated` technology requires a migration plan; using a `Removed` one requires direct architecture review.
