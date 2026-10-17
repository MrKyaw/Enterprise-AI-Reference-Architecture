# AI UX & Interaction Patterns

**Status:** Proposed · **Last reviewed:** 2026-10-17

Interaction design for AI features. Probabilistic systems break assumptions that classical UI patterns rely on — these patterns keep users informed, in control, and able to recover. Informs the [copilots reference architecture](../reference-architectures/copilots/README.md) and [product lifecycle](../lifecycles/product-lifecycle.md).

## Trust & transparency

| Pattern | Intent | Use when | Watch out |
|---|---|---|---|
| **Citation display** | Show sources for grounded claims | Knowledge tasks | Citations must resolve to the actual evidence |
| **Provenance/source badges** | Mark content as AI-generated vs human-authored | Mixed content surfaces | Users ignore badges if inconsistent |
| **Confidence surfacing** | Communicate uncertainty honestly | Decision-support | Fake precision is worse than a range or a caveat |
| **Reasoning trace (collapsed)** | Let users inspect how a conclusion was reached | High-stakes outputs | Verbose traces overwhelm; keep summary-first |
| **Model/version disclosure** | State which model/version produced output | Regulated or audited contexts | Usually secondary UI; keep accessible |
| **Known-limitations notice** | Set expectations on first use / at boundaries | New capabilities | One-time and dismissible, not nagging |
| **Provenance on retrieval misses** | Say "no source found" instead of guessing | RAG answers | Must be a real state, not a rarity |

## Control & recoverability

| Pattern | Intent | Watch out |
|---|---|---|
| **Human confirmation before action** | Prevent unintended effects ([HITL](../design-patterns/human-in-the-loop-approval.md)) | Confirmation fatigue — batch or tiered approvals |
| **Diff / review-before-apply** | Show exactly what will change | Diffs need clear accept/reject granularity |
| **Undo / redo for AI actions** | Make mistakes cheap and reversible | Requires state capture of the prior condition |
| **Draft vs committed states** | Separate suggestion from reality | Must be visibly distinct |
| **Edit-and-accept** | Let users correct instead of regenerate | Feeds improvement signals |
| **Cancel/abort streaming** | Stop generation mid-flight | Salvage partial output if useful |
| **Regenerate/variant request** | Ask for alternatives | Bound the number to avoid thrash |
| **Scope controls** | Let users constrain what the AI uses (sources, date range, systems) | Complexity; sensible defaults matter |
| **Autonomy level indicator** | Show what the system may do on its own | Must reflect real state, not static copy |

## Input & prompting UX

| Pattern | Intent | Watch out |
|---|---|---|
| **Prompt suggestions / starter prompts** | Teach capabilities by example | Suggestions rot; keep them current |
| **Structured input scaffolds** | Templates/fields instead of blank box | Less flexible; good for repeat tasks |
| **Disambiguation prompt** | Ask a clarifying question rather than guess | Must be rare enough not to annoy |
| **Context attachment UI** | Explicitly attach documents/records | Integrity and permission checks required |
| **Follow-up refinement chips** | Cheap iteration ("shorter", "more formal") | Can mask the need for better defaults |
| **Voice/multimodal input** | Alternative input modes | Accessibility and error-handling burden |

## Feedback & learning

| Pattern | Intent | Watch out |
|---|---|---|
| **Thumbs/rating** | Cheap signal capture | Sparse and gameable; use with other signals |
| **Structured correction** | Capture *why* the output was wrong | Requires taxonomy and review capacity |
| **Escalation to human** | Route beyond system competence | Needs a real destination and SLA |
| **Feedback→regression pipeline** | Turn failures into test cases | Triage discipline ([evaluation cycle](../lifecycles/evaluation-lifecycle.md)) |
| **Silent-failure telemetry** | Detect abandonment/regeneration as quality signals | Privacy review required |

## Presentation patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Streaming / progressive rendering** | Reduce perceived latency | Partial-then-changed text is disorienting if unstable |
| **Skeleton + progress with stage labels** | Explain long operations ("searching → reading → composing") | Honest stage naming (no fake steps) |
| **Error states with recovery paths** | Never a dead end | Must suggest requery/fallback, not just apologize |
| **Graceful degradation notice** | Tell users when capability is reduced | Avoid technical jargon |
| **Inline vs panel vs full-page** | Match AI assistance to workflow intimacy | Context switching cost |
| **AI-content placeholder honesty** | Don't fabricate content in empty states | Empty-state copy shapes trust |
| **Accessibility (screen reader, keyboard, focus)** | Ensure AI features are usable by everyone | Streaming text needs ARIA live-region care |
| **Localization-aware output** | Language, tone, and format per locale | Model quality varies by language |

## Conversation-specific patterns

| Pattern | Intent | Watch out |
|---|---|---|
| **Session memory affordances** | Show what the assistant remembers | Must be inspectable and clearable |
| **Context window warnings** | Tell users when history is dropped | Requires honesty about summarization |
| **Reference to earlier turns** | Allow explicit "as we discussed" | Depends on reliable memory |
| **Interruption handling** | Correct mid-response gracefully | State consistency |
| **Multi-thread/topic separation** | Keep unrelated tasks apart | Overhead vs. clarity |

## Anti-patterns

- Confident presentation with no uncertainty affordance
- Irreversible AI actions with no confirmation or undo
- Blank chat box with no guidance as the only interface
- Feedback collection with no visible consequence
- Fake progress steps that don't reflect real work
- Autonomy that differs from what the UI states
- Ignoring accessibility for streaming/non-deterministic content
