"""Carried forward from Chapter 1 - where the numbers come from.

BidiAgent produces no metrics summary object, so this helper only serves the text Curator's
carried case. The voice case times its own first audio in cases.py.
"""

from __future__ import annotations

from dataclasses import dataclass

from strands.agent import AgentResult


@dataclass(frozen=True, slots=True)
class Measurement:
    cycles: int
    total_tokens: int
    latency_ms: int
    tools: tuple[str, ...]


def measure(result: AgentResult) -> Measurement:
    metrics = result.metrics
    return Measurement(
        cycles=metrics.cycle_count,
        total_tokens=metrics.accumulated_usage["totalTokens"],
        latency_ms=metrics.accumulated_metrics["latencyMs"],
        tools=tuple(metrics.tool_metrics),
    )
