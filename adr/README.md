# Architecture Decision Records (ADRs)

Immutable records of significant architectural decisions: context, options considered, decision, and consequences. ADRs are how deviations from reference architectures and standards are justified and tracked.

## Format

Use [0000-template.md](0000-template.md). Numbering is zero-padded and sequential: `NNNN-short-title.md`. **Never renumber or edit an accepted ADR** — supersede it with a new one that references it.

## Lifecycle

`Proposed` → `Accepted` → (optionally) `Superseded by ADR-NNNN` or `Deprecated`

## When an ADR is required

- Any deviation from a [reference architecture](../reference-architectures/) (tag `deviation`)
- Choice of a non-approved technology or provider
- Build-vs-buy decisions ([framework](../docs/build-vs-buy-framework.md))
- Anything a future team would ask "why did they do that?" about

## Index

| ADR | Title | Status |
|---|---|---|
| _(none yet)_ | | |

## Adding an ADR

1. Copy `0000-template.md` to `NNNN-short-title.md` using the next number
2. Link it from this index
3. Open a PR (see [CONTRIBUTING.md](../CONTRIBUTING.md))
