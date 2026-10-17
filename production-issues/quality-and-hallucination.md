# Production Issues — Quality & Hallucination (`Q-`)

Failures where the system gives a wrong, unsupported, or confidently bad answer. Most are detectable only through sampling and evaluation — they never produce an error code.

## Index

| ID | Symptom | Root cause | Impact | Fix |
|---|---|---|---|---|
| Q-01 | Confident fabrication presented as fact | No grounding requirement; model asked to answer without evidence | Misinformed decisions; trust collapse | Require grounding + abstention; cite evidence |
| Q-02 | Answer contradicts an authoritative source | Retrieval returned stale/wrong chunk; no verification | Policy/legal errors | Freshness SLO; answer verification pass; source precedence |
| Q-03 | Quality dropped after a model/provider update | Provider changed model behind an unpinned version | Silent degradation at scale | Pin versions; change detection; re-eval on change |
| Q-04 | Regression after prompt change | Prompt edited without evaluation | Behavior drift; unrepeatable bugs | Eval gate; prompt versioning ([prompt lifecycle](../lifecycles/prompt-lifecycle.md)) |
| Q-05 | Right facts, wrong format; downstream parser fails | No structured output contract | Pipeline errors; rework | Schema-constrained output + server-side validation |
| Q-06 | Inconsistent answers to the same question | Non-determinism + unstable context ordering | User distrust ("it said otherwise yesterday") | Cache/answer normalization; stable context assembly; disclose variability |
| Q-07 | Answers degrade on edge segments (language, domain, dialect) | Evaluation set unrepresentative | Unequal quality; accessibility/compliance gaps | Segment-aware evaluation; targeted data/prompt fixes |
| Q-08 | Over-refusal (safe questions rejected) | Guardrails/prompt too conservative | Capability loss; user workarounds | Measure refusal precision; tune with review |
| Q-09 | Answer is technically correct but unusable (too long/terse) | No user-format evaluation | Adoption failure despite accuracy | Task-success metrics; format evaluation; UX patterns |
| Q-10 | Hallucination only under long context | Context stuffing; middle-of-window degradation | Rare but severe errors at scale | Context minimization; rerank; position-aware assembly |
| Q-11 | Same error recurs months later | Fixed in prompt; never added to regression set | Repeat incidents | Failure→regression pipeline ([evaluation lifecycle](../lifecycles/evaluation-lifecycle.md)) |
| Q-12 | Judge said "good" but humans disagree | Uncalibrated LLM-as-judge | False confidence in quality dashboards | Judge calibration vs human labels; pin judge version |
| Q-13 | Quality varies by time of day / load | Provider throttling or model-version routing under load | Inconsistent experience; SLA breaches | Capacity planning; consistent routing; degradation ladder |

---

## Q-01 — Confident fabrication

**Symptom:** Users report "the assistant made something up," often with citations that look plausible but reference the wrong chunk or a nonexistent section.

**Root cause:** The generation step is allowed to answer without evidence. Either retrieval returned nothing and the prompt didn't permit abstention, or the prompt invited elaboration beyond the context. Instructions alone are not a grounding mechanism.

**Impact:** High. Fabrication is the fastest way to destroy user trust, and it can propagate into decisions, documents, and downstream systems. In regulated contexts it becomes a compliance issue.

**Fix:** Add an explicit abstention path (return "not in the available sources" with the search attempt shown); require citations per claim; add an answer-verification pass for high-stakes flows.

**Prevention:** [Grounding instruction patterns](../design-patterns/rag-patterns.md), refusal behavior in the [prompt lifecycle](../lifecycles/prompt-lifecycle.md), and faithfulness metrics as a hard gate in [evaluation-in-CI](../design-patterns/evaluation-in-ci.md).

**Future work:** Calibrated confidence estimation that reliably distinguishes "supported" from "inferred" from "unknown"; automated claim-level verification against source spans; abstention quality metrics as a first-class evaluation target.

---

## Q-02 — Answer contradicts an authoritative source

**Symptom:** The answer is confidently wrong because it reflects a superseded policy, an old ticket, or a draft document that outranks the current policy in retrieval ranking.

**Root cause:** No source precedence model. All chunks are treated as equally authoritative, so a well-worded obsolete document can outrank the current one. Retrieval has no notion of "this document supersedes that one."

**Impact:** High. Produces confident wrong guidance on exactly the topics where correctness matters most (policy, process, compliance).

**Fix:** Attach authority/supersession metadata at ingestion; retrieve with precedence boosts; surface "last updated" and flag conflicts.

**Prevention:** [Corpus charter](../lifecycles/rag-lifecycle.md) with source precedence, freshness SLOs, and source-owner accountability for staleness.

**Future work:** Automated supersession detection from document lifecycle signals; conflict-aware answering that states "two sources disagree"; integrating record-management systems as the authority source.

---

## Q-06 — Inconsistent answers to the same question

**Symptom:** The same question yields materially different answers across sessions, or one user gets a different answer than a colleague.

**Root cause:** Model non-determinism combined with unstable inputs — context ordering, retrieved chunks differing by tiny query variations, or sampling parameters left at creative defaults.

**Impact:** Medium–High. Erodes trust and makes support/troubleshooting nearly impossible ("it worked for me"). In regulated contexts, inconsistency is indistinguishable from unreliability.

**Fix:** Lower sampling temperature for factual tasks; stable context ordering; caching for identical queries; log the exact assembled context with every answer.

**Prevention:** Deterministic configuration defaults for factual workloads; prompt/context versioning; answer caching with permission-aware invalidation ([GenAI patterns](../design-patterns/genai-prompting.md)).

**Future work:** Verified-cache designs that guarantee the same answer for the same context+user; variance reporting as a standard quality metric; reproducibility mode for auditing an answer weeks later.

---

## Q-12 — Judge says "good," humans disagree

**Symptom:** Quality dashboards are green while users complain. Automated judging reports high scores for answers humans rate as poor.

**Root cause:** The judge model is uncalibrated, biased (prefers longer answers, its own family's style, confident tone), or was silently upgraded. Judge version is not pinned, so trend history is meaningless.

**Impact:** High. It creates false confidence in exactly the system meant to detect quality problems — the failure mode that hides all the others.

**Fix:** Calibrate the judge against human labels on a sample; report agreement; pin the judge version; blind it to which system produced each output.

**Prevention:** [LLM-as-judge discipline](../lifecycles/evaluation-lifecycle.md) in the evaluation lifecycle; human review sampling alongside automated judging; judge upgrades treated as evaluation-system changes requiring recalibration.

**Future work:** Standardized calibration harnesses; bias audits for judges; ensemble judging with disagreement surfacing; uncertainty-aware scoring instead of point scores.
