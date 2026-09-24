"""Chapter 1 - your first Case: does find_exhibit actually run, or is it just described?

The scoreboard's first act proves the chapter's own lesson. Run it against the Curator
BEFORE the tool exists: red. Wire find_exhibit: green. No judge model, no rubric, no flake.

You build this file LIVE. Verified 2026-09-24 against strands-agents-evals 1.4.0
(imports as `strands_evals`; never install the typosquat named `strands-evals`).
"""

from __future__ import annotations

# TODO 1: import the evals surface:
#         from strands_evals import Case, Experiment
#         from strands_evals.evaluators import ToolCalled

# TODO 2: write the first Case - assert the tool is CALLED, not described:
#         case = Case(
#             name="dekatron_count_uses_the_catalog",
#             input="How many dekatrons does the WITCH have?",
#             expected_trajectory=["find_exhibit"],
#         )

# TODO 3: the task - run the Curator on the case and report which tools it called:
#         def task(case: Case) -> dict[str, object]:
#             curator = build_curator()          # from curator.py
#             result = curator(case.input)
#             tools = [...]                      # tool names from result.metrics.tool_metrics
#             return {"output": str(result), "trajectory": tools}

# TODO 4: build the experiment for certify.py - deterministic, no judge:
#         def build_experiment() -> Experiment:
#             return Experiment(cases=[case], evaluators=[ToolCalled(tool_name="find_exhibit")])
