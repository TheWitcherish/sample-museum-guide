"""Chapter 1 - your first Case: does find_exhibit actually run, or is it just described?

The scoreboard's first act proves the chapter's own lesson. Run it against the Curator
BEFORE the tool exists: red. Wire find_exhibit: green. The trajectory check is deterministic -
exactly what week one needs.

You build this file LIVE.

Verified against strands-agents-evals==1.4.0 (imports as `strands_evals`):
  from strands_evals import Case, Experiment
  from strands_evals.evaluators import TrajectoryEvaluator
NOTE: the SDK moved on from the spec's older snippet -
  * Case uses `expected_trajectory=[...]`  (there is NO `expected_tools` field)
  * Experiment is run with `.run_evaluations()`  (not `.run()`)
  * there is NO `strands_evals.scorers` module - TrajectoryEvaluator takes a `rubric` string,
    and the in_order/exact/any_order scorers are internal judge tools, not a public import.
"""

from __future__ import annotations

# TODO 1: import the evals surface (confirmed present in 1.4.0):
#         from strands_evals import Case, Experiment
#         from strands_evals.evaluators import TrajectoryEvaluator

# TODO 2: write the first Case - assert the tool is CALLED, not described. Real field name:
#         case = Case(
#             name="dekatron_count_uses_the_catalog",
#             input="How many dekatrons does the WITCH have?",
#             expected_trajectory=["find_exhibit"],
#         )

# TODO 3: build the experiment and expose it for certify.py to run:
#         def build_experiment() -> Experiment:
#             return Experiment(cases=[case], evaluators=[TrajectoryEvaluator(rubric="...")])

# TODO 4: run it red (no tool) -> wire find_exhibit -> run it green.
