"""Pre-stream check. Run it before going live:

    uv run python preflight.py 1

Each chapter's feature branch adds its own entry to CHECKS. Exit code 0 means ready.
"""

from __future__ import annotations

import importlib
import importlib.metadata
import json
import os
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Final

ROOT: Final[Path] = Path(__file__).resolve().parent
REGION: Final[str] = os.environ.get("AWS_REGION", "us-west-2")
MODEL_ID: Final[str] = os.environ.get("MODEL_ID", "global.anthropic.claude-sonnet-5")


def imports(*modules: str) -> Callable[[], str]:
    def check() -> str:
        for module in modules:
            importlib.import_module(module)
        return ", ".join(modules)

    return check


def no_typosquat() -> str:
    try:
        importlib.metadata.version("strands-evals")
    except importlib.metadata.PackageNotFoundError:
        return "strands-evals typosquat not installed"
    raise RuntimeError("typosquat 'strands-evals' is installed: uv remove strands-evals")


def aws(*args: str) -> str:
    done = subprocess.run(
        ["aws", *args, "--region", REGION], capture_output=True, text=True, check=False
    )
    if done.returncode != 0:
        raise RuntimeError(done.stderr.strip().splitlines()[-1])
    return done.stdout.strip()


def credentials() -> str:
    aws("sts", "get-caller-identity", "--query", "Account", "--output", "text")
    return "valid (account id hidden for stream)"


def model_active() -> str:
    query = f"inferenceProfileSummaries[?inferenceProfileId=='{MODEL_ID}'].status"
    status = aws("bedrock", "list-inference-profiles", "--query", query, "--output", "text")
    if status != "ACTIVE":
        raise RuntimeError(f"{MODEL_ID} is {status or 'not found'} in {REGION}")
    return f"{MODEL_ID} ACTIVE in {REGION}"


def catalog() -> str:
    exhibits = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))["exhibits"]
    witch = next(e for e in exhibits if e["id"] == "witch")
    return f"{len(exhibits)} exhibits, WITCH has {witch['facts']['dekatron_count']} dekatrons"


def certifies(folder: str) -> Callable[[], str]:
    def check() -> str:
        script = ROOT / folder / "example" / "certify.py"
        done = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True, check=False
        )
        found = re.findall(r"(\d+)/(\d+) passed", done.stdout)
        if done.returncode != 0 or not found:
            raise RuntimeError((done.stderr or done.stdout).strip().splitlines()[-1])
        passed, total = found[-1]
        if passed != total:
            raise RuntimeError(f"example solution is red: {passed}/{total} passed")
        return f"example solution green ({passed}/{total})"

    return check


CHECKS: Final[dict[str, list[tuple[str, Callable[[], str]]]]] = {
    "1": [
        ("imports", imports("strands", "strands_tools.calculator", "strands_evals")),
        ("typosquat guard", no_typosquat),
        ("AWS credentials", credentials),
        ("Bedrock model", model_active),
        ("shared catalog", catalog),
        ("certification", certifies("1_first_agent_and_tools")),
    ],
}


def main() -> int:
    chapter = sys.argv[1] if len(sys.argv) > 1 else ""
    if chapter not in CHECKS:
        print(f"usage: uv run python preflight.py <chapter>   (available: {', '.join(CHECKS)})")
        return 2
    failures = 0
    for name, check in CHECKS[chapter]:
        try:
            print(f"PASS  {name}: {check()}")
        except Exception as error:  # noqa: BLE001 - every failure is reported, none is hidden
            failures += 1
            print(f"FAIL  {name}: {error}")
    print("READY TO GO LIVE" if failures == 0 else f"NOT READY: {failures} check(s) failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
