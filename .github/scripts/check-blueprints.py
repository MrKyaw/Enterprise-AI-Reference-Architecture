"""Run each scaffold's smoke tests in its own process with pinned dependencies."""
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
kits = sorted((ROOT / "blueprints").glob("*-starter-kit"))
baseline = (ROOT / "blueprints/inference-starter-kit/requirements.txt").read_text()
failures = []
for kit in kits:
    if (kit / "requirements.txt").read_text() != baseline:
        failures.append(kit.name)
        print(f"{kit.name}: requirements differ; install and verify independently")
        continue
    environment = dict(os.environ, PYTHONPATH=str(kit / "src"))
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=kit, env=environment, capture_output=True, text=True,
    )
    print(f"{kit.name}:\n{result.stdout}", flush=True)
    if result.returncode:
        failures.append(kit.name)
        print(result.stderr, file=sys.stderr)
print(f"Starter kits: {len(kits)} checked; {len(failures)} failures")
sys.exit(bool(failures) or not kits)
