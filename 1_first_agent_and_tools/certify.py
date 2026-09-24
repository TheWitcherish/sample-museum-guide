"""Chapter 1 - the Certification runner. Provided whole; read it out loud on stream.

It imports the experiment and task you build in cases.py, runs them, and prints the scoreboard.
The check is mechanical, not a vibe.

    uv run python 1_first_agent_and_tools/certify.py

Verified 2026-09-24 against strands-agents-evals 1.4.0: run_evaluations(task) takes the task.
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
