"""Pipeline implementation for Integration Starter Kit.

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
    """Run the integration-starter-kit pipeline.

    Implement these steps:
      1. Define API and event contracts before implementation.
      2. Register schemas and enforce compatibility in CI.
      3. Implement idempotent producers and consumers with keys.
      4. Add dead-letter handling and a tested replay path.
      5. Propagate trace context across every hop.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[integration-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
