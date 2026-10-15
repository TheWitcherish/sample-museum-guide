"""Chapter 2 cold open - compute by physical analogy, the way Bush's 1928 differential analyser did.

A wheel rolls on a turning disc. Its distance from the centre is the value you feed in; how far
the wheel has turned is the running integral. No instruction set anywhere: the rotation IS the
number.

You build this file LIVE.  Run it with:  uv run python 2_voice_agent/integrator.py
"""

from __future__ import annotations

# TODO 1: write integrate(f, start, stop, steps) -> float. Each step, the disc turns a little and
#         the wheel picks up f(x) * dx of rotation. Accumulate it.

# TODO 2: integrate x from 0 to 1 (the true answer is 0.5) at steps = 1000, 10, 3, 1.
#         Watch the answer drift as steps shrink.

# TODO 3: say it out loud - the real machine had no `steps` parameter. That argument is the
#         analog/digital boundary, and it is the same decision as tonight's sample_rate.


def main() -> None:
    raise SystemExit("Build the integrator live: fill in TODO 1-3, then run this file.")


if __name__ == "__main__":
    main()
