"""Observability Starter Kit — FastAPI entry point (scaffold)."""
from __future__ import annotations

import os
import uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from guardrails import redact, screen_input
from pipeline import PipelineInput, run_pipeline

KIT = "observability-starter-kit"
app = FastAPI(title="Observability Starter Kit", version="0.1.0")


class RunRequest(BaseModel):
    input: str = Field(min_length=1, max_length=8000)
    tenant_id: str = Field(default="demo", max_length=64)


class RunResponse(BaseModel):
    output: str
    citations: list[str] = Field(default_factory=list)
    request_id: str
    status: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "kit": KIT}


@app.post("/v1/run", response_model=RunResponse)
def run(request: RunRequest) -> RunResponse:
    verdict = screen_input(request.input)
    if not verdict.allowed:
        raise HTTPException(status_code=400, detail=verdict.reason)

    result = run_pipeline(
        PipelineInput(text=redact(request.input), tenant_id=request.tenant_id)
    )
    return RunResponse(
        output=result.output,
        citations=result.citations,
        request_id=result.request_id or str(uuid.uuid4()),
        status=result.status,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
