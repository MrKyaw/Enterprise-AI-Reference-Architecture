"""Pipeline implementation for Agent Starter Kit.

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
    """Run the agent-starter-kit pipeline.

    Implement these steps:
      1. Turn the goal into a plan with explicit success criteria.
      2. Select tools from the registry; validate arguments against the tool schema.
      3. Check the authorization boundary; route side effects to human approval.
      4. Execute, then verify the outcome by querying the target system.
      5. Compensate on partial failure; log every step with a correlation ID.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[agent-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
