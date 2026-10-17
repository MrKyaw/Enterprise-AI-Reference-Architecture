# AI Security

Security requirements owned by Cybersecurity and embedded into AI architecture and design reviews. Architecture review **incorporates** these controls; it does not replace the security team's independent threat modeling and red-teaming.

## Documents

| Document | Purpose |
|---|---|
| [ai-security-controls.md](ai-security-controls.md) | The control set every AI workload must satisfy |
| [red-team-integration.md](red-team-integration.md) | How adversarial testing findings flow into architecture and standards |
| [secure-sdlc.md](secure-sdlc.md) | Security checkpoints embedded in every phase of the AI delivery lifecycle |

## Principles

1. **Assume the model can be manipulated.** Models process attacker-influenced input by design; controls live *around* the model, not *in* it.
2. **Guardrails outside the model.** Policy enforcement (approval gates, filters, egress rules) must be deterministic systems, not prompt instructions.
3. **Least privilege, short-lived.** Every component and agent gets the minimum credential scope for the minimum time.
4. **Everything is logged.** Prompt, decision, tool call, output — correlated and immutable for anything with side effects.
