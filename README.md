# The Curator — Once Upon a Machine

> **This is a sample repository** for a livestream/workshop, not production code. You build
> **The Curator** — an agentic guide for a computing-heritage museum — one gallery at a time,
> live with the audience. Each chapter folder ships as runnable files with `# TODO:` markers you
> fill in as you follow along.

Built with **Python 3.12+ · uv · Strands Agents · Strands Agents Evals · Amazon Bedrock**.

## Setup

```bash
uv sync                              # installs the latest compatible Strands releases (no lockfile)
export MODEL_ID=YOUR_MODEL           # a Bedrock model id your account can reach (see below)
export AWS_REGION=YOUR_AWS_REGION
```

Find a model id your account can actually call before you rely on one:

```bash
aws bedrock list-inference-profiles --query 'inferenceProfileSummaries[].inferenceProfileId'
```

Prerequisites: Python fluency, terminal comfort, and an AWS account with Amazon Bedrock access.

## The adventure map — six galleries

Each chapter builds on the previous one.

| # | Gallery | You'll learn |
|---|---------|--------------|
| 🧮 1 | [When Computers Were People](1_first_agent_and_tools/) | Your first Strands `Agent`, a custom `@tool` (`find_exhibit`), a community tool (`calculator`), your first `Case`, and choosing a Bedrock model on evidence. |
| 🎙️ 2 | The Wheel and the Wave | Talking to the Curator: Nova Sonic, `BidiAgent`, session persistence, latency thresholds. |
| ✍️ 3 | What the Hand Wrote | Reading the archive: Converse image blocks, structured output, retry on validation, the first judge. |
| ⏱️ 4 | Eighty Hours Unattended | Trusting what you built: traces, `ActorSimulator`, chaos, diagnosis, a `--fail-on` CI gate. |
| ⚖️ 5 | Prove It | Automated Reasoning checks, formal policy, the rewriting loop. |
| 🎟️ 6 | Opening Day | Guardrails, streaming UI, red-team evaluators, cost per session. |

## Chapter 1 — how to play

1. Build the agent in `1_first_agent_and_tools/curator.py` and ask it a catalog question — watch it invent an answer.
2. Write `find_exhibit`, a deterministic `@tool` that reads the shared `catalog.json`. Ask again — now it looks it up.
3. Import `calculator` from `strands_tools` for the arithmetic question — the tool you don't write.
4. Write your first `Case` in `cases.py` and run `uv run python 1_first_agent_and_tools/certify.py`: red before the tool, green after.
5. Swap three Bedrock model ids and choose your instrument on evidence.
