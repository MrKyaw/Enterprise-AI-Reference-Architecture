"""Local input screening and redaction (defense in depth, not a control)."""
from __future__ import annotations

import re
from dataclasses import dataclass

MAX_INPUT_CHARS = 8000

PII_PATTERNS = [
    re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"),          # email
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),                  # SSN-shaped
    re.compile(r"\b(?:\d[ -]*?){13,16}\b"),                  # card-shaped
    re.compile(r"\b\+?\d[\d ()-]{7,}\d\b"),               # phone-shaped
]

INJECTION_PATTERNS = [
    re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.I),
    re.compile(r"disregard\s+.*\s+instructions", re.I),
    re.compile(r"reveal\s+.*(system\s+prompt|instructions)", re.I),
    re.compile(r"you\s+are\s+now\s+", re.I),
]


@dataclass
class Verdict:
    allowed: bool
    reason: str = ""


def screen_input(text: str) -> Verdict:
    if len(text) > MAX_INPUT_CHARS:
        return Verdict(False, "input_too_large")
    for pattern in INJECTION_PATTERNS:
        if pattern.search(text):
            return Verdict(False, "possible_prompt_injection")
    return Verdict(True)


def redact(text: str) -> str:
    for pattern in PII_PATTERNS:
        text = pattern.sub("[REDACTED]", text)
    return text
