"""Pipeline implementation for Intelligent Automation Starter Kit.

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
    """Run the intelligent-automation-starter-kit pipeline.

    Implement these steps:
      1. Ingest and classify the work item; deduplicate by business key.
      2. Route the routine path to deterministic rules.
      3. Call ML scoring or an agent only for the judgment slice.
      4. Apply the policy and approval gate before any side effect.
      5. Verify the outcome and compensate on partial failure.

    Keep every external call behind the AI gateway and emit a span per stage.
    """
    return PipelineResult(
        output=(
            f"[intelligent-automation-starter-kit] scaffold response for tenant {payload.tenant_id!r}. "
            "Replace run_pipeline() with the real implementation."
        ),
        citations=[],
        request_id=str(uuid.uuid4()),
        status="scaffold",
    )
