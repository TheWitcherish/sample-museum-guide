"""Carried forward from Chapter 1, unchanged - the Certification runner. Read it out loud.

It imports the experiment and task you build in cases.py, runs them, and prints the scoreboard.
The check is mechanical, not a vibe.

    uv run python 2_voice_agent/certify.py

Verified 2026-10-15 against strands-agents-evals 1.6.0: run_evaluations(task) takes the task.
"""

from __future__ import annotations

from cases import build_experiment, task


def main() -> None:
    report = build_experiment().run_evaluations(task)
    passed = sum(report.test_passes)
    print(f"{passed}/{len(report.test_passes)} passed")
    report.display()


if __name__ == "__main__":
    main()
