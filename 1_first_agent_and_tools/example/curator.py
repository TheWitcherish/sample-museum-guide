"""Chapter 1 solution - the Curator, its two tools, and the questions from the stream.

    uv run python 1_first_agent_and_tools/example/curator.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Final

from inspect_agent import measure
from strands import Agent, tool
from strands_tools import calculator

# Verified ACTIVE in us-west-2 on 2026-09-24. Override with: export MODEL_ID=YOUR_MODEL
DEFAULT_MODEL_ID: Final[str] = "global.anthropic.claude-sonnet-5"
MODEL_ID: Final[str] = os.environ.get("MODEL_ID", DEFAULT_MODEL_ID)

CATALOG: Final[Path] = Path(__file__).resolve().parents[2] / "catalog.json"

SYSTEM_PROMPT: Final[str] = (
    "You are the Curator of a computing-heritage museum. Answer visitors warmly and briefly. "
    "Use find_exhibit for any fact about an exhibit and calculator for any arithmetic. "
    "Never guess a number the catalog can give you."
)


@tool
def find_exhibit(name: str) -> str:
    """Look up an exhibit in the museum catalog by name or id.

    Args:
        name: Part of the exhibit's name or id, for example "WITCH" or "comptometer".
    """
    exhibits = json.loads(CATALOG.read_text(encoding="utf-8"))["exhibits"]
    query = name.lower()
    matches = [e for e in exhibits if query in e["name"].lower() or query in e["id"]]
    if not matches:
        return f"No exhibit matches {name!r}."
    return json.dumps(matches[0])


def build_curator(model_id: str = MODEL_ID) -> Agent:
    return Agent(model=model_id, system_prompt=SYSTEM_PROMPT, tools=[find_exhibit, calculator])


def main() -> None:
    curator = build_curator()
    for question in (
        "How many dekatrons does the WITCH have?",
        "How many years between the Comptometer patent and the WITCH going operational?",
    ):
        print(f"\n> {question}")
        print(measure(curator(question)))


if __name__ == "__main__":
    main()
