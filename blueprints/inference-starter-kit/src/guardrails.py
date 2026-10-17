# src/guardrails.py
"""Input/output guardrails for inference service."""
import re

# Input filtering patterns
INJECTION_PATTERNS = [
    r"(?i)ignore previous instructions",
    r"(?i)<sys>",
    r"(?i)you are now",
]

# Output filtering patterns
PII_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{-2,}\b",  # Email
]

def sanitize_input(text: str) -> str:
    """Filter untrusted input before it reaches the model."""
    for pattern in INJECTION_PATTERNS:
        text = re.sub(pattern, "[FILTERED]", text, flags=re.IGNORECASE)
    return text

def sanitize_output(text: str) -> str:
    """Filter output for sensitive data before sending to user."""
    for pattern in PII_PATTERNS:
        text = re.sub(pattern, "[REDACTED]", text)
    return text