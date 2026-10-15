"""Chapter 2 bonus quest - for when you finish early: a Curator that lets hesitant visitors finish.

Some visitors pause mid-question ("the WITCH has... um... how many..."). Nova Sonic may decide
the turn is over and answer too soon. Turn-taking is tunable.

Optional. Run it with:  uv run python 2_voice_agent/bonus_quest.py
"""

from __future__ import annotations

# TODO 1: copy your voice Curator from voice_curator.py.

# TODO 2: BedrockNovaSonicModel's `params` are merged into Nova Sonic's sessionStart event
#         (verified 2026-10-15 in the strands-agents 1.61.0 source). Pass:
#         params={"turnDetectionConfiguration": {"endpointingSensitivity": "LOW"}}
#         Values are HIGH, MEDIUM or LOW - see the Nova 2 Sonic "Turn-taking controllability" docs.

# TODO 3: ask the same hesitant question at HIGH and at LOW. Which one interrupted you?


def main() -> None:
    raise SystemExit("Bonus quest: fill in TODO 1-3, then run this file.")


if __name__ == "__main__":
    main()
