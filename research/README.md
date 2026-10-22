# Research & Technology Evaluation

The team's architecture research function: horizon scanning of emerging AI/ML techniques, architectures, and platforms; time-boxed validation prototypes; and internal briefs with findings and recommendations.

## The research-to-standards pipeline

```
Horizon scan → Time-boxed prototype → Research brief → Evaluation score
    → Cross-cutting review (EA, Cloud, Data, Cybersecurity)
    → Standards update (approved technologies, reference architectures, patterns)
```

Research that doesn't change anything is curiosity, not architecture work. Every brief ends with a recommendation and a clear adoption path.

## Contents

| Directory | What lives there |
|---|---|
| [briefs/](briefs/) | Plans or published findings with explicit evidence status, named `YYYY-MM-short-topic.md` |
| [prototypes/](prototypes/) | Time-boxed validation prototypes, one directory each with its own `README.md` |

## Rules for prototypes

- **Time-boxed, always.** 2–4 weeks. A prototype that runs longer is a project — sponsor it properly or kill it.
- **Question-first.** Start with the decision the prototype will inform (e.g., "does provider X's embedding model beat our current one on our golden set at lower cost?"), not the tech we want to play with.
- **Disposable.** Prototypes are not production seeds. If something survives, it gets rebuilt properly against the reference architecture.
- **Safe data only.** Prototypes use synthetic or cleared data; no production PII in validation work.

## Rules for briefs

- ≤ 4 pages; executive summary first
- Ends with: recommendation, adoption path, and what would change our mind
- Findings that change standards are presented to the Head of AI Governance and Architecture and peer leads for cross-cutting review before adoption
- Rejected technologies are recorded too — so the question stays closed

## Evidence and publication status

The current [embedding brief](briefs/2026-10-embedding-evaluation.md) and [prototype directory](prototypes/prototype-embedding-models/README.md) contain an evaluation plan, not an executed experiment. Do not infer customer data, benchmark results, cost savings, or model approval from a plan. Publish findings only with reproducible measurements, limitations, and disclosure permission; see the [publication review](../docs/publication-review.md).
