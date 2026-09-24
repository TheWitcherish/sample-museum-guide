"""Chapter 1 - When Computers Were People.

Your first Curator agent, its tools, and choosing a model on evidence.

You build this file LIVE. It ships as import-plus-TODO lines (spec 10a rule 5):
open it, fill the gaps, watch the agentic loop appear.

Run it with:  uv run python 1_first_agent_and_tools/curator.py
"""

from __future__ import annotations

import os
from typing import Final

# The model id is read from the environment with a verified fallback (never hard-coded alone).
# On stream, list what your account can actually reach FIRST, then set it:
#   aws bedrock list-inference-profiles --query 'inferenceProfileSummaries[].inferenceProfileId'
#   export MODEL_ID=YOUR_MODEL
DEFAULT_MODEL_ID: Final[str] = "REPLACE_ME_verify_live_with_aws_bedrock_list_inference_profiles"
MODEL_ID: Final[str] = os.environ.get("MODEL_ID", DEFAULT_MODEL_ID)

# TODO 1: build the first Curator agent - persona + system prompt, one Agent, one model.
#         from strands import Agent
#         curator = Agent(model=MODEL_ID, system_prompt="You are the Curator ...")

# TODO 2: ask it a CATALOG question with no tool available -
#         "How many dekatrons does the WITCH have?" - and watch it confidently invent a number.
#         This is the problem the whole series exists to solve.

# TODO 3: write find_exhibit - a deterministic @tool that reads the shared catalog.json and
#         returns the real record. Re-ask: the cycle count goes 1 -> 2. That diff IS the loop.
#         from strands import tool

# TODO 4: a SECOND question, arithmetic this time -
#         "How many years between the Comptometer patent and the WITCH going operational?"
#         Reveal: you do not write this one. `from strands_tools import calculator`.

# TODO 5: the model swap. Run the SAME experiment against three Bedrock model ids and read
#         pass rate / tokens / latency. Choose your instrument on evidence, not on a tour.


def main() -> None:
    raise SystemExit("Build the Curator live: fill in TODO 1-5, then run this file.")


if __name__ == "__main__":
    main()
