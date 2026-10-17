# RAG Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Patterns for retrieval-augmented generation, organized by the stage they address. Lifecycle context in [RAG lifecycle](../lifecycles/rag-lifecycle.md); implementation baseline in the [RAG reference architecture](../reference-architectures/rag/README.md).

> Ordering rule: **fix retrieval before prompting.** Most "the model hallucinates" problems are retrieval problems. Measure both layers independently.

## Chunking strategies

| Strategy | Intent | Use when | Watch out |
|---|---|---|---|
| **Fixed-size chunks** | Simple, predictable | Homogeneous text | Splits mid-concept |
| **Recursive/structural split** | Respect headings, sections, code blocks | Structured documents | Needs format awareness |
| **Semantic chunking** | Split on meaning shifts | Prose without structure | Cost; inconsistent sizes |
| **Parent-document / hierarchical** | Retrieve small, return large | Need precision + context | Two-level index management |
| **Sentence-window** | Retrieve a sentence, return neighbors | Fine-grained fact retrieval | Context can still be truncated |
| **Sliding window with overlap** | Avoid boundary loss | Dense factual text | Index size growth |
| **Metadata-enriched chunks** | Attach source/section/ACL/date | Always | Metadata quality determines filter quality |
| **Per-type chunking** | Different rules per document type (tables, code, PDFs) | Mixed corpora | More pipeline complexity |

## Query transformation patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Query rewriting** | Resolve references/typos before retrieval | Conversational systems | Adds a model call |
| **Multi-query expansion** | Generate several paraphrases, union results | Recall matters | More retrieval calls; dedup needed |
| **RAG-Fusion (RRF)** | Rank-merge multiple result lists | Multiple query variants/hybrid search | Needs rank fusion, not score averaging |
| **HyDE (hypothetical document)** | Embed an imagined answer instead of the question | Short/vague queries | Can drift off-topic |
| **Step-back prompting** | Retrieve for a more general concept first | Domain jargon mismatches | Extra call; may over-generalize |
| **Query decomposition** | Break multi-part questions into sub-queries | Comparative/multi-hop questions | Orchestration + synthesis complexity |
| **Filter extraction** | Derive metadata filters from the query | Permissions, date ranges, categories | Wrong filters silently drop the answer |

## Retrieval patterns

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Dense (vector) retrieval** | Semantic similarity | Paraphrase-heavy queries | Weak on exact identifiers |
| **Sparse (keyword/BM25)** | Exact terms, IDs, codes | Structured identifiers present | Misses paraphrases |
| **Hybrid search** | Combine dense + sparse | General default | Weight tuning required |
| **Reranking (cross-encoder/LLM)** | Reorder top candidates by relevance | Precision matters | Adds latency/cost |
| **Retrieval-time ACL filtering** | Enforce permissions before results | Any multi-user corpus | Must be tested with negative cases |
| **Graph RAG** | Traverse entities/relations for answers | Relationship-heavy questions | Graph construction and freshness cost |
| **Recursive / iterative retrieval** | Retrieve, assess gaps, retrieve again | Multi-hop questions | Loop bounds required |
| **Fallback to broad retrieval** | Avoid empty results | Filters too strict | Relevance dilution |

## Generation & grounding patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Citation-grounded synthesis** | Answers cite the chunks used | Citations must be verifiable |
| **Refusal on insufficient evidence** | Abstain instead of guessing | Measuring abstention quality |
| **Context compression / rerank-then-summarize** | Fit the best evidence in the window | Losing necessary detail |
| **Answer verification pass** | Check output against retrieved evidence | Extra cost; diminishing returns |
| **Structured answer with evidence blocks** | Machine-consumable grounded output | Schema enforcement |
| **Confidence surfacing** | Show retrieval strength to the user | False confidence is worse than none |

## Adaptive patterns (advanced)

| Pattern | Intent | Use when |
|---|---|---|
| **Self-RAG** | Model decides *whether* and *what* to retrieve, and critiques its own grounding | Not every query needs retrieval |
| **Corrective RAG (CRAG)** | Grade retrieved docs; correct or web/alternate search if poor | Retrieval quality varies |
| **Agentic RAG** | Agent plans retrieval, tools, and verification | Multi-hop or research-like tasks (see [agent patterns](agent-patterns.md)) |
| **Adaptive RAG** | Route query complexity to no-retrieval / single-step / multi-step | Mixed query difficulty at scale |

> These add orchestration, cost, and failure modes. Adopt only with measured retrieval-quality gains over simpler approaches.

## Evaluation patterns

| Layer | Metrics |
|---|---|
| Retrieval | Hit rate, recall@k, MRR, NDCG, filter-correctness |
| Generation | Faithfulness, answer relevance, citation correctness, refusal appropriateness |
| System | Task success, latency, cost, cache hit rate, empty-result rate |

Evaluate layers independently ([evaluation lifecycle](../lifecycles/evaluation-lifecycle.md)); then end-to-end. Maintain an adversarial set with injection payloads embedded in source documents.

## Anti-patterns

- Tuning prompts to fix a retrieval defect
- Indexing without ACLs and filtering afterwards
- Chunking with no evaluation of whether chunks are answerable
- Re-embedding silently (invalidates the whole index)
- Retrieval with no fallback, returning nothing for ordinary questions
- Advanced patterns (self/corrective/agentic RAG) deployed without a simpler baseline to beat
