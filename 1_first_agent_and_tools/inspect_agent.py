"""Chapter 1 - the thin measurement helper (NOT named inspect.py - that shadows the stdlib).

It exists to show WHERE the numbers come from, so the Experiment output is not magic.
Chapter 4 deletes it and replaces it with real OpenTelemetry capture - the honest arc:
hand-rolled measurement first, instrumentation once you know what you are measuring.

You build this file LIVE.
"""

from __future__ import annotations

# TODO 1: given an agent result, print per-turn token counts:
#         result.metrics.accumulated_usage["inputTokens"] / ["outputTokens"] / ["totalTokens"]
# TODO 2: print latency - result.metrics.accumulated_metrics["latencyMs"] - and the cycle count,
#         result.metrics.cycle_count (it goes 1 -> 2 when find_exhibit is wired).
# TODO 3: return a small frozen dataclass so the model-swap comparison can read the numbers.
#         (verified 2026-09-24 against strands-agents 1.57.0)
