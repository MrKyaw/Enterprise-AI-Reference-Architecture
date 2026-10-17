# Prompt Lifecycle

**Status:** Proposed · **Owner:** AI engineering · **Last reviewed:** 2026-10-17

Prompts are production configuration. They determine behavior as much as code does, so they get the same versioning, review, and evaluation discipline.

## Phases

### 1. Authoring
- Start from a template: role/task, constraints, output contract, examples, refusal behavior
- Explicit about grounding ("answer only from provided context"), uncertainty ("say you don't know"), and safety boundaries
- Structured output format declared with a schema when machines consume it
- **Artifact:** prompt template with documented intent and variables

### 2. Versioning
- Prompts live in source control (or a prompt registry) — never only in a database row edited in a UI
- Each version: ID, author, change summary, linked evaluation run
- Prompt and the code that assembles context version together
- **Artifact:** versioned prompt + changelog entry

### 3. Evaluation
- Every change runs the [evaluation suite](../design-patterns/evaluation-in-ci.md): golden set + adversarial set
- Record metric deltas vs the incumbent version; regressions block promotion
- Test edge behavior: empty context, conflicting context, hostile context, out-of-scope requests
- **Artifact:** evaluation report per candidate version

### 4. Deployment
- Prompts promoted through environments like code (dev → staging → production)
- A/B or canary where traffic volume permits; shadow comparison otherwise
- Rollback target identified before deployment
- **Artifact:** deployment record

### 5. Observation
- Sampled output review; user feedback signals (thumbs, edits, escalations, abandonment)
- Guardrail trigger rates as a prompt-quality signal
- Cost/latency shifts caused by prompt verbosity or format

### 6. Iteration
- Prompt changes are normal maintenance — but always eval-gated
- Root-cause before rewriting: is the failure prompt, retrieval, model, or data?
- Keep prompt complexity low; complexity is where subtle regressions hide

### 7. Retirement
- Deprecate old versions with a note; keep history for audit and rollback

## Prompt engineering techniques (catalog)

| Technique | Purpose |
|---|---|
| Zero-shot instruction | Clear task statement; first choice for capable models |
| Few-shot examples | Shape format and edge-case handling |
| Chain-of-thought | Improve multi-step reasoning (weigh cost/latency) |
| Decomposition | Split complex tasks into smaller prompts |
| Role/persona | Constrain tone and domain framing |
| Output schema / structured output | Machine-consumable results |
| Delimiting untrusted content | Separate instructions from data (injection defense) |
| Self-consistency | Sample multiple paths, take consensus |
| Reflection / self-critique | Model reviews its own draft before returning |
| Retrieval-grounded synthesis | Answer strictly from provided context with citations |

**Any technique applied to a production prompt must be measured, not assumed to help** — many popular techniques cost tokens and latency for no measurable gain on a given task.

## Anti-patterns

- Prompts edited directly in production with no version history
- Prompt changes without an evaluation run
- Secrets or access tokens embedded in prompts
- Relying on the prompt as a security control (guardrails and authorization live outside the model)
- Ever-growing prompt bloat replacing proper retrieval or logic
