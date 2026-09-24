"""Chapter 1 solution - the first Case: was find_exhibit actually called?"""

from __future__ import annotations

from curator import build_curator
from inspect_agent import measure
from strands_evals import Case, Experiment
from strands_evals.evaluators import ToolCalled

case = Case(
    name="dekatron_count_uses_the_catalog",
    input="How many dekatrons does the WITCH have?",
    expected_trajectory=["find_exhibit"],
)


def task(case: Case) -> dict[str, object]:
    result = build_curator()(case.input)
    return {"output": str(result), "trajectory": list(measure(result).tools)}


def build_experiment() -> Experiment:
    return Experiment(cases=[case], evaluators=[ToolCalled(tool_name="find_exhibit")])
