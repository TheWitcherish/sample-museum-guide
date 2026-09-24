"""Chapter 1 - the Certification runner. Provided whole; read it out loud on stream.

It imports the experiment you build in cases.py and runs it. The scoreboard prints a report;
you read it. That is the whole idea: the check is mechanical, not a vibe.

    uv run python 1_first_agent_and_tools/certify.py

Verified against strands-agents-evals==1.4.0: Experiment is executed with run_evaluations().
"""

from __future__ import annotations

from cases import build_experiment


def main() -> None:
    experiment = build_experiment()
    report = experiment.run_evaluations()
    print(report)


if __name__ == "__main__":
    main()
