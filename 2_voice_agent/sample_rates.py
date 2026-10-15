"""Chapter 2 - hear the sampling theorem instead of reading it (Nyquist 1928, Shannon 1949).

Record three seconds of your own voice, then play it back at lower and lower sample rates until
it breaks. Below twice the highest frequency in your voice, the detail is simply gone.

You build this file LIVE.  Run it with:  uv run python 2_voice_agent/sample_rates.py
Needs a microphone. macOS asks for permission the first time: allow it for your terminal.
"""

from __future__ import annotations

# TODO 1: open a PyAudio input stream (pyaudio ships with the bidi-pyaudio extra), mono, 16-bit,
#         at 16000 Hz - the same rate the voice Curator uses - and record three seconds.
#         Use `with` / try-finally so the stream and PyAudio are always closed.

# TODO 2: keep every Nth sample to reach 8000, 4000, 2000 and 1000 Hz. No filter on purpose:
#         you want to HEAR what undersampling does, not hide it.

# TODO 3: play each version back at its own rate and say the rate out loud before each one.
#         Where does your voice stop being words?


def main() -> None:
    raise SystemExit("Build the sample-rate demo live: fill in TODO 1-3, then run this file.")


if __name__ == "__main__":
    main()
