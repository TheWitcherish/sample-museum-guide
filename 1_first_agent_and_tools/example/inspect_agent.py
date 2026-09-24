"""Chapter 1 solution - where the numbers come from."""

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
