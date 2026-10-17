# src/main.py
"""FastAPI inference service with gateway client and guardrails."""
from fastapi import FastAPI, HTTPException
from .guardrails import sanitize_input, sanitize_output

app = FastAPI(title="Inference Starter Kit", description="Sample inference service")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/query")
async def query(request: dict):
    """Process a query through the gateway with guardrails."""
    user_input = request.get("message", "")
    
    # Sanitize input
    safe_input = sanitize_input(user_input)
    
    # TODO: route through AI gateway
    # response = await gateway_client.send(safe_input)
    
    # For now, return sanitized input
    sanitized_output = sanitize_output(safe_input)
    
    return {"response": sanitized_output, "source": "starter-kit"}