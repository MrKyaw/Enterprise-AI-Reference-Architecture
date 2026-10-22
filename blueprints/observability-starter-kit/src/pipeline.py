"""Pipeline implementation for Observability Starter Kit.

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
    """Run the observability-starter-kit pipeline.

    Implement these steps:
      1. Instrument every request with a correlation ID and stage spans.
      2. Emit token, cost, and latency metrics per stage.
      3. Sample requests for offline quality evaluation.
      4. Define SLIs and SLOs, including a quality SLO.
      5. Alert on burn rate, not raw thresholds.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[observability-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
