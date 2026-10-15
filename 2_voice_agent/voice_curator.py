"""Chapter 2 - The Wheel and the Wave: talk to the Curator, out loud, on open speakers.

Last week's find_exhibit drops into a speech-to-speech agent unchanged. Tonight you give it a
voice, stop it hearing itself, and watch its connection restart without it forgetting you.

You build this file LIVE. Verified 2026-10-15 against strands-agents 1.61.0: import only from
strands.bidi. strands.experimental.bidi still imports, with a deprecation warning - never teach it.

Run it with:  uv run python 2_voice_agent/voice_curator.py
"""

from __future__ import annotations

import os
from typing import Final

# Verified ACTIVE in us-west-2 on 2026-10-15. Override with:
#   export NOVA_SONIC_MODEL_ID=YOUR_MODEL
#   export AWS_REGION=YOUR_AWS_REGION
DEFAULT_NOVA_SONIC_MODEL_ID: Final[str] = "amazon.nova-2-5-sonic"
NOVA_SONIC_MODEL_ID: Final[str] = os.environ.get("NOVA_SONIC_MODEL_ID", DEFAULT_NOVA_SONIC_MODEL_ID)
DEFAULT_REGION: Final[str] = "us-west-2"
REGION: Final[str] = os.environ.get("AWS_REGION", DEFAULT_REGION)

# TODO 1: give the Curator a voice. BedrockNovaSonicModel(model_id=..., region=..., voice=...),
#         a BidiAgent with tools=[find_exhibit], and one AudioIO for input and output.
#         from curator import find_exhibit          # Chapter 1's tool, unchanged
#         from strands.bidi.agent import BidiAgent
#         from strands.bidi.io import AudioIO
#         from strands.bidi.models import BedrockNovaSonicModel
#         Then type audio={"input": {"sample_rate": 16000}} on purpose. It is already the
#         default - you write it to make the sampling theorem visible in a config dict.

# TODO 2: a spoken conversation has no Ctrl-C. Write end_visit - a five-line tool that ends it:
#         @tool(context=True)
#         def end_visit(tool_context: ToolContext[BidiAgent]) -> str:
#             ...tool_context.agent.cancel()...
#         from strands import ToolContext, tool

# TODO 3: run it on open speakers and listen to it answer ITSELF. Then the fix is one argument:
#         AudioIO(audio_processor={"echo_cancellation": True, "stream_delay_ms": 40})
#         Input and output MUST come from that same AudioIO: it cancels against its own playback.
#         Echo still leaking? stream_delay_ms is the knob. Edit, restart, listen again.

# TODO 4: nobody waits seven minutes on a livestream. Force the connection restart at 60 s:
#         BedrockNovaSonicModel(..., connection={"restart_after_s": 60})
#         Watch for the restart, then ask: "what were we just talking about?"


def main() -> None:
    raise SystemExit("Build the voice Curator live: fill in TODO 1-4, then run this file.")


if __name__ == "__main__":
    main()
