"""Chapter 1 - the thin measurement helper (NOT named inspect.py - that shadows the stdlib).

It exists to show WHERE the numbers come from, so the Experiment output is not magic.
Chapter 4 deletes it and replaces it with real OpenTelemetry capture - the honest arc:
hand-rolled measurement first, instrumentation once you know what you are measuring.

You build this file LIVE.
"""

from __future__ import annotations

# TODO 1: given an agent result, print per-turn token counts (input / output).
# TODO 2: measure and print wall-clock latency for a single turn.
# TODO 3: return a small typed record so cases.py / the Experiment can read the numbers.
