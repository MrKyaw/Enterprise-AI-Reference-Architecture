"""Pipeline implementation for Inference Starter Kit.

This is a scaffold. Replace run_pipeline() with the real implementation.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field


@dataclass
class PipelineInput:
    text: str
    tenant_id: str


@dataclass
class PipelineResult:
    output: str
    citations: list[str] = field(default_factory=list)
    request_id: str = ""
    status: str = "scaffold"


def run_pipeline(payload: PipelineInput) -> PipelineResult:
    """Run the inference-starter-kit pipeline.

    Implement these steps:
      1. Authenticate the workload and apply rate limits at the gateway.
      2. Screen input and redact PII before assembly.
      3. Route to the pinned primary model with a declared fallback.
      4. Screen output and enforce response policy.
      5. Emit tokens, cost, latency, and a correlation ID for every call.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[inference-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
