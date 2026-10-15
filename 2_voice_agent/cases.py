"""Chapter 2 - the scoreboard grows a second kind of assertion: a number with a limit on it.

Chapter 1's case is carried forward as working code: it asks WHICH tool ran. That is a set
comparison, and it cannot express "too slow". Tonight you add the check that can.

You build the TODOs LIVE. Verified 2026-10-15 against strands-agents-evals 1.6.0, which still
ships no latency evaluator - so you write one.
"""

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

# TODO 1: write LatencyUnder - a ~10-line subclass of strands_evals.evaluators.Evaluator.
#         evaluate(evaluation_case) returns [EvaluationOutput(score=..., test_pass=..., reason=...)]
#         with a reason the room can read: "answered in 3980 ms, limit 1200 ms".
#         The threshold lives in the evaluator, not the prompt: LatencyUnder(1200).

# TODO 2: write the voice case - a question the Curator must answer out loud, fast:
#         voice_case = Case(name="witch_answered_within_1200ms", input="...", ...)

# TODO 3: time what the visitor FEELS. BidiAgent has no metrics object, so measure it yourself:
#         send() the case input as text, then read receive() until the first BidiAudioStartEvent
#         and record the milliseconds in between (time.perf_counter). Three lines, no OpenTelemetry.


def task(case: Case) -> dict[str, object]:
    # TODO 4: route the voice case to your stopwatch from TODO 3; everything else stays here.
    result = build_curator()(case.input)
    return {"output": str(result), "trajectory": list(measure(result).tools)}


def build_experiment() -> Experiment:
    # TODO 5: add voice_case and LatencyUnder(1200). Expect red on the first run - you will HEAR
    #         the silence before you read it on the scoreboard. That is the script.
    return Experiment(cases=[case], evaluators=[ToolCalled(tool_name="find_exhibit")])
