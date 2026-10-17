# Data Lifecycle

**Status:** Proposed · **Owner:** Data · **Last reviewed:** 2026-10-17

Governs data from acquisition to deletion. Every AI workload's quality, compliance, and trustworthiness is bounded by this lifecycle.

## Phases

### 1. Acquisition / sourcing
- Source registration: owner, purpose, classification, lawful basis, contractual limits
- Ingestion method: batch, CDC (change data capture), streaming, API, file drop
- Consent and purpose-limitation recorded — data collected for X is not silently reused for Y
- **Artifact:** source registration + data-sharing agreement record

### 2. Storage
- Landing (raw) → curated (cleansed, conformed) → consumption zones; no direct-to-consumption shortcuts for governed data
- Classification-based controls: encryption, access policy, masking
- Retention schedule attached at creation, not decided later
- **Artifact:** storage design + access policy

### 3. Transformation
- Transformation as code, versioned and tested ([patterns](../design-patterns/data-architecture.md))
- Contracts at boundaries: schema + semantics + quality expectations
- Data quality checks: completeness, validity, uniqueness, timeliness, consistency
- Lineage captured automatically (source → transform → consumer)
- **Artifact:** pipeline code + contracts + quality results

### 4. Integration & sharing
- Integration patterns per [standards](../standards/integration-patterns.md)
- Cross-boundary transfer requires explicit approval and classification review
- PII handling: minimization, tokenization/pseudonymization where feasible, redaction before non-production use

### 5. Serving / consumption
- Consumers: analytics/BI, applications, AI (**[data agent](../reference-architectures/data-agent/README.md)**, RAG corpora, training sets, feature stores)
- **Semantic layer** mediates business meaning ([pattern](../design-patterns/semantic-layer-grounding.md))
- Access at the consumer layer inherits source ACLs — no widened grants for convenience
- **Artifact:** serving contract + ACL mapping

### 6. Quality & observability
- Freshness, volume, schema drift, distribution shift monitoring
- Anomaly alerts routed to data owners
- Quality SLOs per critical dataset

### 7. Governance & compliance
- Classification, residency, retention, deletion, audit
- Subject-access and deletion requests propagate end-to-end (stores, indexes, caches, features, training sets, logs)
- Data owner accountable per domain (see [domain patterns](../design-patterns/domain-and-business.md))

### 8. Archival
- Cost-tiered storage with a defined access path
- Archived data retains classification and retention obligations
- Archival is not deletion — deletion is a separate, verified act

### 9. Deletion
- Verified deletion across all copies: primary, replicas, backups (per retention), caches, search indexes, embeddings, derived features, model-training snapshots where obligated
- Deletion certificate/record retained
- **Artifact:** deletion record

## Data for AI: additional requirements

| AI use | Additional lifecycle requirement |
|---|---|
| Training / fine-tuning | Lawful basis + consent; representativeness; no leakage from eval sets |
| RAG corpus | Retrieval-time ACLs; deletion propagation to index; freshness SLO |
| Embeddings | Treat embeddings as derived PII when they encode personal content; delete with source |
| Feature store | Point-in-time correctness; train/serve consistency; lineage to source |
| Evaluation sets | Held-out integrity; documented origin; refresh without contaminating training |
| Synthetic data | Provenance labeled; validated not to leak real records |

## Zoning model

```
Raw/Landing ──▶ Curated/Conformed ──▶ Consuming/Products ──▶ AI assets
 (immutable,      (typed, validated,    (semantic layer,      (features, vectors,
  classified)      deduped, owned)       data products)        prompts, evals)
```

Each arrow is a contract. Consumers never read from an earlier zone than their contract allows.

## Anti-patterns

- Data lakes that become swamps (no curation, no owner, no retention)
- PII copied into "test" data
- Deletion implemented only in the primary store
- Embeddings treated as non-personal
- Purpose creep: repurposing data quietly for a new AI use case
