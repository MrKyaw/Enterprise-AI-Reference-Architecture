"""Pipeline implementation for Data Agent Starter Kit.

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
    """Run the data-agent-starter-kit pipeline.

    Implement these steps:
      1. Detect ambiguity and ask a clarifying question when confidence is low.
      2. Retrieve only relevant metrics, dimensions, and joins from the semantic layer.
      3. Synthesize a query against governed definitions; never invent a metric.
      4. Validate and inject the caller's row/column policy before execution.
      5. Return the answer with definition, filters, and time window.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[data-agent-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
