# Contributing

Thanks for helping keep our AI architecture standards current and trustworthy.

## Ground rules

- **Everything is a pull request.** No direct pushes to `main`.
- **One concern per PR.** A standard change should not also restructure docs.
- **Evidence over opinion.** Standards and build-vs-buy changes must cite validated research (see [`research/`](research/)) or production experience.
- **Security is not optional.** Any change touching a reference architecture must be reviewed against [`security/ai-security-controls.md`](security/ai-security-controls.md).

## Change types and required reviewers

| Change type | Example | Required reviewers |
|---|---|---|
| Editorial | Typos, wording, broken links | 1 architecture team member |
| New design pattern | Adding a pattern to `design-patterns/` | 2 architecture team members |
| Standard change | Approved frameworks, model providers, data platforms | Architecture team + cross-cutting review (Enterprise Architecture, Cloud Platform, Data, Cybersecurity) |
| Reference architecture change | New workload type, major revision | Architecture team + cross-cutting review + Head of AI Governance and Architecture |

## Adding a document

1. Use the appropriate template:
   - Architecture decision → [`adr/0000-template.md`](adr/0000-template.md)
   - Research brief → [`research/briefs/TEMPLATE.md`](research/briefs/TEMPLATE.md)
   - Validation prototype → [`research/prototypes/TEMPLATE.md`](research/prototypes/TEMPLATE.md)
2. Follow naming conventions (below).
3. Link the new document from its directory `README.md` index.
4. Open a PR using the checklist in `.github/PULL_REQUEST_TEMPLATE.md`.

## Naming conventions

- Directories and files: `kebab-case.md` (e.g. `build-vs-buy-framework.md`)
- Root/directory index files: `README.md` (uppercase)
- ADRs: `NNNN-short-title.md`, zero-padded, never renumbered
- Research briefs: `YYYY-MM-short-topic.md`
- Prototypes: `prototype-<short-name>/` with its own `README.md`
- Branch names: `docs/…`, `standard/…`, `ra/…`, `lifecycle/…`, `pattern/…`, `approach/…`, `research/…` prefixes

## Deprecation

Do not delete standards or architectures. Mark them `Status: Deprecated` with a pointer to the replacement and keep them for 12 months.
