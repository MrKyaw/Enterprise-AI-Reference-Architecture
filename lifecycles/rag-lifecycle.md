# RAG Lifecycle

**Status:** Proposed · **Owner:** AI engineering · **Last reviewed:** 2026-10-17

Lifecycle for retrieval-augmented generation — from corpus selection through ingest, retrieval, generation, and evaluation. Implementation details in the [RAG reference architecture](../reference-architectures/rag/README.md) and [RAG patterns](../design-patterns/rag-patterns.md).

## Phases

### 1. Corpus definition
- Which sources are authoritative, current, and permitted for this use case
- Document types, formats, languages, update frequency, and volume
- Access-control model: how source permissions map to retrieval-time filters
- Retention/deletion obligations that must propagate from source → index
- **Artifact:** corpus charter (sources, owners, ACL model, refresh cadence)

### 2. Ingestion & preparation
- Extract → clean → normalize → chunk, with a documented strategy per content type ([patterns](../design-patterns/rag-patterns.md#chunking-strategies))
- Metadata attached: source, version, timestamp, ACL tags, provenance
- Idempotent, incremental ingestion (re-running doesn't duplicate)
- Deletion pipeline: source deletion → index deletion (tested, not assumed)
- **Artifact:** ingestion pipeline + chunking spec

### 3. Embedding & indexing
- Embedding model chosen and **versioned**; re-embedding is a planned migration, not a silent change
- Index type: vector, hybrid (vector + keyword), or graph — per retrieval needs
- Index build reproducible from the corpus + embedding version
- **Gate:** index freshness SLO defined

### 4. Retrieval
- Retrieval strategy: dense, sparse, hybrid, with reranking and query transformation as needed
- Filters applied for ACL and metadata constraints
- Retrieval quality measured **independently of generation** (hit rate, recall@k, MRR)
- **Artifact:** retrieval evaluation report

### 5. Generation & grounding
- Prompt assembly: retrieved context + instructions + citation requirements in a versioned template
- Grounding discipline: answer only from retrieved context or say so; cite sources
- Guardrails on input (injection) and output (policy, PII)
- **Artifact:** generation config + guardrail configuration

### 6. Evaluation
- Two layers: retrieval quality and answer quality (faithfulness, relevance, citation correctness)
- Golden Q→relevant-docs→expected-answer set per corpus; adversarial set for injection via documents
- [Evaluation in CI](../design-patterns/evaluation-in-ci.md) with explicit thresholds
- **Artifact:** evaluation suite + baselines

### 7. Operations
- Freshness monitoring (source change → index visible)
- Retrieval drift: index growth, empty-result rate, filter-fallthrough rate
- Cost/latency: retrieval + reranking + generation decomposed
- Re-index/re-embed as a scheduled or triggered job with rollback

### 8. Evolution
- Add sources, improve chunking, upgrade embeddings, add reranking — each change re-runs evaluation
- Corpus refresh cadence aligned to source update frequency
- **Gate:** every index/embedding/chunking change ships with an evaluation delta

### 9. Retirement
- Decommission index, delete embeddings and cached content, revoke ingestion credentials

## Change-impact matrix

| Change | Re-index? | Re-embed? | Re-eval? |
|---|---|---|---|
| New source added | ✅ | ✅ (new docs) | ✅ |
| Chunking strategy | ✅ | ✅ | ✅ |
| Embedding model | ✅ | ✅ | ✅ |
| Reranker added | ✗ | ✗ | ✅ |
| Prompt template | ✗ | ✗ | ✅ |
| ACL model | ✅ (metadata) | ✗ | ✅ (negative tests) |

## Anti-patterns

- Chunk-first, evaluate-never (no baseline to know if changes help)
- Silent re-embedding that invalidates the index overnight
- ACLs enforced after retrieval instead of at retrieval
- Testing retrieval with generation metrics only (can't tell which layer failed)
- Index as a second system of record with no delete propagation
