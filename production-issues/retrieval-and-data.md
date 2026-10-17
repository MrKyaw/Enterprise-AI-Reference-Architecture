# Production Issues — Retrieval & Data (`R-`)

Failures in ingestion, indexing, retrieval, permissions, and data quality. These usually masquerade as generation problems.

> **Rule:** when answer quality drops, investigate retrieval first. Most "the model got worse" incidents are retrieval or data incidents.

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| R-01 | Relevant document exists but is never retrieved | Chunking destroyed context, embedding mismatch, or query/document vocabulary gap | Wrong or missing answers | Re-chunk; hybrid search; query rewriting; rerank |
| R-02 | Retrieval returns nothing for ordinary questions | Over-strict metadata filters or ACL logic | Users conclude the system is broken | Filter fallback; filter extraction validation; empty-result alerting |
| R-03 | Unauthorized content appears in an answer | ACLs applied after retrieval or not at all | Critical: data leak, compliance breach | Retrieval-time ACL filtering + negative tests |
| R-04 | Answers based on obsolete content | No freshness SLO; stale index | Confidently wrong guidance | Freshness SLO; last-updated surfacing; source-owner alerts |
| R-05 | Deleted source still answerable | Deletion not propagated to index/cache | Privacy/compliance violation | Deletion propagation pipeline + verification |
| R-06 | Query works in English, fails elsewhere | Evaluation set English-only; embedding model weaker on other languages | Unequal access | Multilingual evaluation; language-specific tuning |
| R-07 | Identifiers/IDs/codes not found | Dense-only retrieval; tokens lack semantic meaning | Missing key records | Hybrid search; keyword boost for identifiers |
| R-08 | Tables/figures mangled or empty in answers | Naive text extraction destroyed structure | Misread numbers | Per-type parsing; table-aware chunking |
| R-09 | Duplicate chunks crowd out diversity | Overlapping chunking + no dedup | Templates missed | Dedup by content hash; MMR/diversity reranking |
| R-10 | Retrieval quality silently degrades as corpus grows | Index growth without re-tuning; stale embeddings | Gradual quality loss | Corpus-growth monitoring; scheduled retrieval eval |
| R-11 | Answer cites a chunk that doesn't support the claim | Citation generated post-hoc rather than derived from evidence | False accountability | Derive citations from used evidence; verify spans |
| R-12 | Feature/data pipeline silently produces nulls | Upstream schema change without contract enforcement | Model degradation; wrong decisions | Data contracts; schema-drift alerts; fail-fast |
| R-13 | Train/serve skew produces worse production results | Feature logic duplicated between training and serving | Unexplained quality drop | Single transformation definition; feature store; skew monitoring |

---

## R-03 — Unauthorized content in an answer

**Symptom:** A user receives an answer containing information they are not entitled to see. Often discovered by the user, occasionally by an audit.

**Root cause:** ACLs enforced after retrieval (filter the final answer) rather than at retrieval, or the ingestion pipeline dropped permission metadata, or the index carries grants from a service account with broader access than end users.

**Impact:** **Critical.** This is a data breach. Regulatory notification may apply. Trust damage is severe because the failure is invisible without negative testing.

**Fix:** Stop the bleeding by disabling the feature or the affected corpus; rebuild the index with permission metadata; implement retrieval-time filtering keyed to user identity; add negative tests that assert denial.

**Prevention:** [Retrieval-time authorization](../design-patterns/security-patterns.md), identity propagation from the request through retrieval, ACL mapping in the [corpus charter](../lifecycles/rag-lifecycle.md), and permission tests in the [testing strategy](../approaches/testing-strategy.md).

**Future work:** Attribute-level filtering for partially accessible documents; automated ACL-consistency verification against source systems on a schedule; differential-privacy-flavored aggregate answers when detailed access is denied.

---

## R-01 — Relevant document exists but is never retrieved

**Symptom:** Users know the answer is documented, yet the assistant says it can't find it. Retrieval logs show the correct document was never a candidate.

**Root cause:** Usually one of four: chunking split the answer across boundaries; the embedding model doesn't represent the document's vocabulary; the query uses terminology that doesn't appear in the document (vocabulary gap); or a metadata filter excluded it.

**Impact:** Medium–High. Produces abstentions or wrong answers with high user confidence that the content exists, which damages trust in the whole system.

**Fix:** Add hybrid (keyword+dense) retrieval; inspect chunk boundaries for the specific failing document; add query expansion/rewriting; verify filters aren't excluding valid sources.

**Prevention:** Retrieval evaluation independent of generation (hit rate, recall@k) with a golden set per corpus; per-type chunking specs; filter-fallthrough metrics.

**Future work:** Automatic chunk-boundary optimization driven by retrieval failures; learned sparse retrieval tuned to the corpus vocabulary; synonym/ontology expansion from a domain glossary ([ontology-driven approach](../approaches/delivery-and-practice-approaches.md)).

---

## R-05 — Deleted source still answerable

**Symptom:** A deletion or right-to-erasure request is completed in the source system, but the content still appears in answers weeks later.

**Root cause:** The index, caches, embeddings, and conversation logs are separate stores from the source. Deletion was implemented only where the request landed.

**Impact:** **Critical** in regulated contexts. Direct compliance violation with evidence trail proving it.

**Fix:** Immediate purge from index and caches; invalidate semantic caches keyed on those documents; scan logs; document the remediation.

**Prevention:** [Deletion propagation](../lifecycles/data-lifecycle.md) as a designed pipeline with verification, treating embeddings and caches as derived personal data, and a deletion-propagation graph in data architecture patterns.

**Future work:** Provenance graphs that enumerate every derived copy automatically; cryptographic erasure for derived artifacts; automated deletion verification with periodic audits.

---

## R-13 — Train/serve skew

**Symptom:** The model performs well offline and worse in production, with no explanation in drift dashboards.

**Root cause:** Feature transformations implemented twice — once in the training pipeline, once in the serving path — and they drifted. Differences are often subtle: timezone handling, null defaults, rounding, category encoding.

**Impact:** High. Silent quality loss that monitoring misses because inputs look "normal" and outputs look plausible.

**Fix:** Compare training-time and serving-time feature values for a sample of production requests; reconcile the differing transformation; backfill.

**Prevention:** One transformation definition used by both paths (feature store or shared library); distribution comparison between training and serving features as a monitor; [feature store pattern](../design-patterns/ml-engineering.md).

**Future work:** Automated feature-consistency assertion as a deployment gate; point-in-time verification tooling; skew detection that triggers automatic investigation rather than just alerting.
