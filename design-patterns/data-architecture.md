# Data Architecture Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns for organizing, moving, and governing data — the foundation every AI workload stands on. Applied throughout the [data lifecycle](../lifecycles/data-lifecycle.md).

## Storage & organization

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Lakehouse** | Object storage + table format with ACID and schema evolution | Unified analytics + ML on one copy | Table-format maturity and governance discipline |
| **Medallion (bronze/silver/gold)** | Progressive refinement zones (raw → conformed → curated) | Most analytics/ML platforms | Skipping silver to "save time" recreates the swamp |
| **Data mesh** | Domain ownership of data products; self-serve platform | Large orgs with strong domain teams | Becomes an excuse for fragmentation without contracts |
| **Data product** | Discoverable, versioned, SLA-backed dataset with owner | Cross-team consumption | Needs genuine ownership, not a name on a page |
| **Data vault** | Auditable, insert-only modeling for raw integration | Highly regulated, many sources, audit demands | Complex queries; needs an information-mart layer |
| **Dimensional / star schema** | Consumer-friendly modeling for analytics | BI and metric-heavy consumption | Slowly changing dimension handling |
| **Zone mapping for AI** | Raw → curated → data product → AI assets (features, vectors, prompts, evals) | Every AI workload | AI assets inherit the governance of their source |

## Movement & integration

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **ELT (vs ETL)** | Load then transform in the warehouse/lakehouse | Compute-elastic platforms | Cost of recomputation; needs orchestration discipline |
| **Change data capture (CDC)** | Stream changes from source databases | Near-real-time replication, avoiding batch windows | Source schema changes; ordering; delete semantics |
| **Batch processing** | Scheduled bulk transforms | Latency-tolerant, cost-sensitive, large volumes | Stale serving; window boundaries |
| **Stream processing** | Continuous, event-time processing | Real-time features, live agent data | State management, late/out-of-order data |
| **Lambda architecture** | Batch + speed layers | Very high scale with both accuracy and latency needs | Two code paths to maintain |
| **Kappa architecture** | Single streaming path, replay for reprocessing | Streaming-first teams | Replay cost and retention requirements |
| **Lakeflow / declarative pipelines** | Pipeline definitions with automatic dependency + quality management | Repeatable, governed ingestion | Platform coupling; abstraction limits |
| **Reverse ETL** | Push modeled data back into operational tools | Enrichment of CRM/ERP/ops systems | Write conflicts, ownership ambiguity |

## Modeling & correctness

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Slowly changing dimensions (SCD 1/2/3/6)** | Track history of attributes | Analytics needs point-in-time truth | Type-2 row explosion; join correctness |
| **Point-in-time correctness** | Reconstruct features as they were at prediction time | Any ML training set | Leakage if naive joins are used |
| **Schema-on-read vs schema-on-write** | Flexibility vs safety | Exploration vs production consumption | Schema-on-read in production = runtime surprises |
| **Data contracts** | Producer commits to schema + semantics + quality | Cross-team interfaces, AI input pipelines | Contracts without enforcement are documentation |
| **Idempotent ingestion** | Re-running produces the same state | Any scheduled or retried pipeline | Requires dedup keys and merge logic |
| **Soft delete / tombstone** | Mark deletion while honoring retention | Compliance needs + downstream propagation | Tombstones must actually propagate to AI assets |

## AI-specific data patterns

| Pattern | Intent | Where used |
|---|---|---|
| **[Semantic layer](semantic-layer-grounding.md)** | Governed metrics/dimensions as the AI's business vocabulary | [Data agent RA](../reference-architectures/data-agent/README.md) |
| **Feature store** | Consistent, reusable, point-in-time features | [ML project lifecycle](../lifecycles/ml-project-lifecycle.md) |
| **Embedding store** | Versioned vector representations with lineage | [RAG lifecycle](../lifecycles/rag-lifecycle.md) |
| **Evaluation dataset store** | Versioned golden/adversarial/regression sets | [Evaluation lifecycle](../lifecycles/evaluation-lifecycle.md) |
| **Dataset versioning** | Reproducible training data snapshots + manifests | [MLOps](../lifecycles/mlops-lifecycle.md) |
| **Lineage graph** | Source → transform → consumer → AI asset traceability | All workloads, audit |

## Governance patterns

| Pattern | Intent |
|---|---|
| **Classification-driven access** | Controls derive from data classification, not ad-hoc grants |
| **Purpose limitation registry** | Records why data was collected; blocks silent reuse |
| **Deletion propagation graph** | Maps every derived copy (index, cache, feature, embedding) for verified deletion |
| **Metadata-driven platform** | Pipelines parameterized by metadata → reusable, governable |

## Anti-patterns

- Copying data into AI tooling "temporarily" with no retention or ACLs
- Embeddings or features treated as non-personal derived artifacts
- Deletion implemented at the source only
- Batch-only pipelines feeding real-time experiences (or the reverse) without design intent
- Data products without owners or SLAs
- Point-in-time joins approximated with "close enough" timestamps (silent leakage)
