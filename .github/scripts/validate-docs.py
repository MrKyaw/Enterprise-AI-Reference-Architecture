"""Validate tracked Markdown paths, fences, privacy exclusions, and catalog counts."""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
errors = []
files = [ROOT / name for name in tracked if name.endswith(".md")]
for path in files:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    fence = None
    visible = []
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, info = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not info.strip():
                fence = None
            continue
        if fence is None:
            visible.append(line)
        elif r"\n" in line and "subgraph" in line:
            errors.append(f"{relative}:{number}: literal newline escapes in diagram")
    if fence:
        errors.append(f"{relative}: unclosed code fence")
    for target in re.findall(r"\]\(([^)]+)\)", "\n".join(visible)):
        target = target.strip().split(' "', 1)[0]
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:|^#", target):
            continue
        local = unquote(target.split("#", 1)[0])
        if local and not (path.parent / local).exists():
            errors.append(f"{relative}: missing local link {target}")
    if re.search(r"\b(?:Thiri5|Thri5|Capgemini|RadComm)\b|/Users/|/home/[a-zA-Z][^ /]*/", text, re.I):
        errors.append(f"{relative}: customer/employer reference or personal absolute path")

for name in tracked:
    parts = Path(name).parts
    base = Path(name).name
    if base.startswith(".env") and base not in {".env.example", ".env.sample"}:
        errors.append(f"{name}: private environment file tracked")
    if base.endswith((".pem", ".key", ".tfstate", ".tfstate.backup")) or base == "credentials.json":
        errors.append(f"{name}: private credential/state file tracked")
    if "node_modules" in parts or ".venv" in parts:
        errors.append(f"{name}: generated dependency directory tracked")

counts = {
    "lifecycles": len(list((ROOT / "lifecycles").glob("*-lifecycle.md"))),
    "reference architectures": len(list((ROOT / "reference-architectures").glob("*/README.md"))),
    "use cases": len([p for p in (ROOT / "use-cases").glob("*.md") if p.name != "README.md"]),
    "starter kits": len(list((ROOT / "blueprints").glob("*-starter-kit/README.md"))),
}
readme = (ROOT / "README.md").read_text()
expanded = {"llm-gateway", "human-in-the-loop-approval", "evaluation-in-ci", "architecture-as-code", "semantic-layer-grounding"}
pattern_files = {p.stem for p in (ROOT / "design-patterns").glob("*.md") if p.name != "README.md"}
pattern_summary = f"{len(pattern_files - expanded)} catalogs + {len(pattern_files & expanded)} expanded treatments"
if pattern_summary not in readme:
    errors.append(f"README.md: missing current pattern inventory '{pattern_summary}'")
issue_files = [p for p in (ROOT / "production-issues").glob("*.md") if p.name != "README.md"]
issue_ids = set()
for path in issue_files:
    issue_ids.update(re.findall(r"\b[QRCSAO]-\d{2}\b", path.read_text()))
issue_summary = f"{len(issue_ids)} indexed scenarios in {len(issue_files)} categories"
if issue_summary not in readme:
    errors.append(f"README.md: missing current issue inventory '{issue_summary}'")
for label, count in counts.items():
    if f"{count} {label}" not in readme:
        errors.append(f"README.md: missing current count '{count} {label}'")
for error in errors:
    print(error, file=sys.stderr)
print(f"Markdown: {len(files)} files checked; {len(errors)} failures; inventory: {counts}")
sys.exit(bool(errors))
