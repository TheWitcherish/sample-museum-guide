---
title: "Once Upon a Machine: From Analog Gears to Agentic in Python"
date: 2026-07-28
revised: 2026-08-04
owner: TheWitcherish
status: Design approved (see §1a)
artifact: Livestream series (6 chapters, 7 streams) that accretes into an AWS Workshop
stack: Python 3.12+ · uv · Strands Agents SDK · Strands Evals SDK · Amazon Bedrock
---

# Once Upon a Machine: From Analog Gears to Agentic in Python

> **Using this spec as a source? Read §14 first.** Every use of this document as an implementation
> source **MUST regenerate a per-chapter plan** — eight plans, one per stream plus a scaffold plan —
> and **MUST NOT** implement from the ten superseded plan documents under `docs/superpowers/plans/`.
> §14 lists what each plan must carry and what it must not violate.

## 1. What this is

A six-chapter livestream series (seven streams — Chapter 4 runs as two), built live with the
audience, that accretes into an AWS Workshop Studio catalog. Developers build **The Curator** —
an agentic guide for a computing-heritage museum — one gallery at a time.

**Primary artifact:** the Workshop Studio catalog (`contentspec.yaml` +
`content/*/index.en.md` + a sample repo with `# TODO:` markers), authored in the same
structure as *Once Upon Spring AI*. **The sample repo follows the *Once Upon Agentic AI* folder
convention exactly** — numbered chapter folders, one root `pyproject.toml`, every folder
pre-populated with runnable files. See §10a.

**Secondary artifact:** seven livestreams. The stream is the rehearsal; the catalog is the
deliverable. Chapters 2 and 3 are the clip factories — talking to the Curator out loud, and
handwriting becoming JSON, both need no editing to work as a Reel or Short.

**Audience:** **computer science students and developers.** Python fluency, terminal comfort,
and an AWS account with Bedrock access are assumed and stated as prerequisites. Per the AWS
Community Day leveling guide, we do not cover every foundational concept.

**Language: Python only.** No polyglot chapters, no cross-language comparisons. The history
spans four eras; the language does not change.

**Gamified.** Learning is structured as a certification game — see §5a. The workshop should
be fun to *play*, not merely fun to read.

## 1a. Restructure record (2026-08-04) — do not relitigate

The series was designed as eight chapters and nine streams. It is now **six chapters and seven
streams.** Recording the four decisions and their reasoning so this is settled.

| Decision | What moved | Why |
|---|---|---|
| **Chapter 1 carries Strands basics *and* the model swap** | Old Ch 1 (agent + custom tool + fabrication) absorbed old Ch 2's three-model Bedrock swap | Both are the same theme — *choosing your instrument* — which Rule 1 explicitly allows to carry several technologies. A tool is an instrument; so is a model |
| **The voice chapter becomes Chapter 2** | Old Ch 6 (Nova Sonic) moved from position 6 to position 2, absorbing old Ch 2's differential-analyser integrator as its cold open | Its payoff line — *"a well-built tool does not care what modality asked for it"* — currently fires five weeks after the tool is written. One week after is better. And Rule 2 permits it: the anchor moves to the **conversion** (Nyquist 1928 / Shannon 1949), not the medium |
| **The Evals SDK chapter becomes Chapter 4** | Old Ch 5 (Proving Room) moved to position 4, absorbing old Ch 4's WITCH reliability history | The user's directive was "Evals is Chapter 2, swapped with Chapter 3." Voice then took position 2, and Rule 2 finished the arithmetic: the Paper Archive is anchored 1948 and the Proving Room 1951, so the Archive must precede it. Position 4 is the only ordering satisfying both directives |
| **MCP and multi-agent are removed entirely** | Old Ch 4 (MCP catalog server + era-specialist routing) deleted; multi-agent becomes a Go Deeper link | See the verified reasoning below |

### Why MCP was removed, verified rather than asserted

The removal was tested against the **2026-07-28 MCP revision** before deciding. Two findings, in
order of force:

**1. The stack cannot reach it.** Verified 2026-08-04 against PyPI:

| Fact | Value |
|---|---|
| `mcp` release implementing the 2026-07-28 revision | **2.0.0**, published 2026-07-28 |
| `strands-agents` 1.50.2 dependency constraint | **`mcp<2.0.0,>=1.23.0`** |
| Latest protocol version declared by `mcp` 1.29.0 | **`2025-11-25`** (read from the sdist's `types.py`) |

Strands cannot install the SDK that speaks the new specification. A chapter teaching 2026-07-28
through Strands is not currently buildable, so the question decides itself.

**2. The revision would not have rescued the chapter anyway.** Its major changes are transport
and lifecycle plumbing — protocol-level sessions and `Mcp-Session-Id` removed, the
`initialize`/`initialized` handshake removed in favour of a stateless `_meta`-carried protocol
version, `server/discover` added, `resources/subscribe` replaced by `subscriptions/listen`,
`ping`/`logging/setLevel` removed, Multi Round-Trip Requests replacing server-initiated requests,
a required `resultType` field, SSE resumability removed, `ttlMs`/`cacheScope` caching hints, and
an error-code renumbering. **Nothing in it changes how a developer authors a tool.** Meanwhile
Roots, Sampling and Logging are now **Deprecated** under the new feature-lifecycle policy — so a
2025-era MCP chapter would be teaching three features scheduled for removal.

**Accepted consequence, stated plainly:** this workshop no longer teaches the industry-standard
tool protocol, and some participants will expect it. That is R32, and its mitigation is a Go
Deeper section pointing at *Once Upon Agentic AI*'s MCP chapter — which is also the chapter R4
warned we were duplicating.

### Two amendments the same day, after the four above were settled

The restructure table is not the whole record. Two further directives landed on 2026-08-04 and both
**overrule** parts of what the four decisions produced:

| Amendment | What it overrules | Where it lives |
|---|---|---|
| **The Evals scoreboard runs from Chapter 1** | The design that shipped a *provided, unexplained* `certify.py` for Chapters 1–3 and opened the SDK only in Chapter 4. *"The Evals scoreboard must run since the 1st chapter to avoid frustrations for the audience watching the livestream or the YouTube video. I don't want to fail on a different line but instead show the added value of the Evals."* R31 is dissolved | §5a (the one-new-check-per-chapter table), §7, each chapter's Certification block |
| **Chapter titles are creative, in the *Once Upon Agentic AI* register** | Flat working titles like "The Proving Room". Titles now carry an emoji and a hook; folder names stay plainly technical, which is the two-layer pattern the reference workshop actually uses | §5c (the authoritative title/folder table) |

**Chapter 4 changed shape as a result, not just numbering.** It was *"where the scoreboard opens."*
It is now *depth on a scoreboard the participant has run five times*: simulated inputs, real traces,
injected faults, and CI. That is a better 400-level chapter than an SDK tour, and it is the reason the
WITCH's eighty unattended hours became the title.

### What the restructure invalidates

**All ten implementation plan documents under `docs/superpowers/plans/` are superseded** and must
be regenerated from this spec. They were written against the eight-chapter ordering, `chapterN/`
folders, and PEP 723 inline scripts — the last of which §10a had already voided on 2026-08-04.
Do not implement from them.

**And regeneration is a standing rule, not a one-time cleanup — see §14.** Every use of this spec as
an implementation source MUST regenerate the plans. Ten superseded documents become **eight**: one per
stream (Chapter 4 is two) plus a repository scaffold plan.

## 2. The narrative throughline

The series makes one argument, and every chapter advances it:

> **Instructions were once *embodied*, then became *explicit*, and are now *inferred*.**

- **Embodied.** A differential analyser has no instruction set. You build the equation out
  of gears; the machine *is* the problem.
- **Explicit.** The stored-program era separated instructions from data. Computing became
  a list you could write, read, and change. Teaching computers existed to make humans
  understand that list.
- **Inferred.** With agents the list is gone again — not embodied in brass, but inferred by
  a model from a sentence.

**And a second movement, which Chapter 5 delivers: the split that should never have happened.**
Neural and symbolic computing were one subject at birth — McCulloch and Pitts titled the founding
neural-network paper *"A Logical Calculus of the Ideas Immanent in Nervous Activity"* in 1943;
Turing's 1948 *"Intelligent Machinery"* described B-type neural networks; von Neumann's 1952
*"Lectures on Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable
Components"* examined the interplay directly. The field divided only after McCarthy coined
*"Artificial Intelligence"* in 1956. Automated Reasoning checks put the halves back together —
a neural model generates, formal logic proves.

**Von Neumann's title is the workshop's thesis in one line.** Participants spend six chapters
building *reliable organisms from unreliable components*: a trustworthy Curator assembled out of
a model that cannot be trusted, using tools, schemas, tests, boundaries and proofs.

**Series cold open.** Ada Lovelace, 1843, on the Analytical Engine: it *"has no pretensions
whatever to originate anything."* Still the sharpest one-line description of what an LLM is
and isn't. Ada has exactly two consumers: this cold open, and **Chapter 1's Go Deeper link.** She is
not a recurring motif and not a chapter.

**Spine sentence.** Every machine in this museum was built to teach a human something. The
Curator is the newest one.

### The analog-to-agentic arc, as hands-on work (not narration)

The thesis above is the *argument*. This table is the **audit**: every era in it must be something
a participant physically does, not something they are told. If a row's right-hand column is empty,
that era is decoration and the chapter needs fixing.

| Analog medium | Becomes digital in | What the participant actually does |
|---|---|---|
| **Punched cards** | Ch 1 — When Computers Were People | Writes the deterministic tool that stops the model fabricating; meets the card as "instructions on a separable medium" |
| **Gears and rotation, then sound as a continuous wave** | Ch 2 — The Wheel and the Wave | Simulates a differential analyser's integrator (wheel on disc) in ~15 lines, **hears their own voice degrade below the Nyquist rate**, then holds a spoken conversation with the Curator and interrupts it |
| **Handwriting, paper, typescript** | Ch 3 — What the Hand Wrote | Renders pages of the real 1948 NPL scan of Turing's *Intelligent Machinery* — typed text, a handwritten annotation, hand-drawn network diagrams — into validated Pydantic objects, with a retry loop driven by validation failure |

**Three rows, not four — and the merge is what makes Chapter 2 one concept.** Gears and sound were
separate chapters when they were separate ideas. They are the same idea: *a continuously varying
quantity reaching a machine that can only take discrete samples of it.* The integrator's `steps`
parameter and Nova Sonic's `input_rate` are the same decision, forty years apart. One chapter, one
sentence, and §5b's Rule 1 is satisfied rather than strained.

**The arc's endpoint is not a medium — it is a property.** Chapters 4, 5 and 6 do not digitise
anything; they answer the question the first three raise. Every analog instrument in this museum was
trusted because it was **deterministic**. The thing built from these three conversions is not. So
Ch 4 tests it, Ch 5 proves it, and Ch 6 bounds it — which is von Neumann's 1952 title, and the
reason the history is load-bearing rather than ornamental.

**Note what is deliberately absent: rotor cipher machines.** They were the original vehicle for the
determinism beat and were removed after a fact-check — see §3. Determinism now travels on the
Jacquard loom, which carries the stored-program idea as well, and survives the editorial boundary.

**Where the punched-card lineage now ends.** Jacquard's card leads to the Analytical Engine,
Hollerith's tabulators and eventually the stored program. With the First Generation gallery removed
(§1a), the stored-program era is **two sentences of Chapter 1 narration and one Go Deeper link, not
a chapter.** Chapter 1 tells the lineage forward as far as the stored program and stops there;
nothing later in the series depends on it, and nothing else in this spec mentions it.

**What left with that gallery, and is not coming back as an appendix (decided 2026-08-04).** EDSAC,
the BBC Micro, the 1986 Domesday System's fifteen-year unreadability, and Donald Davies' packet
switching were all Chapter 4 material. They are **dropped, not archived.** The Domesday beat is a
good story, and a good story with no chapter to serve is exactly the material an appendix exists to
launder. See §13 for the rule this is an instance of.

**Period scope.** 1804 mechanical determinism → analog computation → teaching computers → today's
agents. Ada (1843) appears only as a cold-open reference and a Go Deeper link.

## 3. Editorial guardrail (hard rule)

The subject is the **history of computation** and the **educational mission of
computing-heritage museums**.

**Out of scope as subject matter:** wartime cryptanalysis. No Enigma, no Lorenz/Tunny, no
Colossus. This is an author decision, applied consistently — those machines are
inseparable from the events they served, and this series is about computing and pedagogy.

**Why this becomes engineering, not a disclaimer.** The real museum that inspires this work
(The National Museum of Computing) occupies Block H at Bletchley Park. Visitors *will* ask
about wartime codebreaking. So the Curator needs genuine scope enforcement — which is why
Chapter 6's Guardrails work is a product requirement rather than a bolted-on safety demo.

**Framing requirement.** Refusals must read as **scope**, never suppression:
*"I'm the guide for the computing-heritage galleries — for that story, the Bletchley Park
museum is next door."* Suppression framing would imply the history is shameful. It is not.

### What this rule excludes, and what it permits (decided 2026-07-28)

The boundary was tested during design and held. Recording the reasoning so it is not relitigated.

**Excluded — no version of these is in scope:**
- Cipher machines presented as workshop subject matter, **including a renamed stand-in.** A
  machine that is recognisably the excluded one with its provenance removed is worse than naming
  it: same subject, with the attribution filed off. Audiences who know this history would read it
  as evasion rather than editorial care.
- Bletchley Park's **operational rooms as a workflow to reproduce** — the Registry Room, Machine
  Room and Decode Room *were* the wartime codebreaking operation. Renaming the machine does not
  change what the rooms did.
- Turing's cipher work, and his speech-encipherment work. Both are wartime; neither has a
  civilian counterpart that could be honestly presented.

**Permitted, and used:**
- **TNMOC's location** stated as fact (Block H, Bletchley Park), because that is where the museum
  is and it is why Chapter 6's scope enforcement is a genuine product requirement.
- **Turing's civilian computing work** — *On Computable Numbers* (1936), the ACE design at NPL,
  *Intelligent Machinery* (1948, Chapters 3 and 5), *Computing Machinery and Intelligence*
  (1950), his Manchester Programmers' Handbook, and morphogenesis (1952). Turing is honoured on
  the terms this series is actually about.
- **Deterministic transformation** taught through machines with civilian histories — the
  **Jacquard loom** (a punched card produces an identical woven pattern every time), the
  **Comptometer**, and **Hollerith's tabulators** as the card's onward lineage. All three are
  Chapter 1, and all three are used.

**Narrowed 2026-08-04: no "optional" permitted machines.** This list previously ended *"and
optionally Babbage's Difference Engine, Hollerith tabulators, or player-piano rolls."* Hollerith
earned a place in Chapter 1's lineage paragraph and is named above. The Difference Engine and
player-piano rolls had no chapter, so they are gone — an *optional* permission is a
permitted-but-unused item with a hedge in front of it (§13).

**Removed from the permitted list (2026-08-04): the room-pipeline pattern.** Large-scale records
work organised as receive → process → interpret was permitted as *architecture only*, to give
Chapter 4's MCP process boundary a historical framing. That chapter no longer exists (§1a), so the
permission has no consumer. Deleting it rather than leaving it unused, on the same principle that
retired the Mary Stuart reference: a permitted-but-unused item invites someone to find a use for it.

**Rejected after fact-check (2026-07-28): commercial rotor cipher machines.** The idea was to
teach determinism via rotor machines sold commercially before any military adoption. The history
does not survive the boundary: **the commercially-marketed rotor machine of the 1920s was
Enigma itself** — Scherbius and Ritter patented in 1918, sold commercially from 1923 through
Chiffriermaschinen AG, exhibited at Bern in 1923, and exported widely. So "civilian rotor
machine" routes directly back to the excluded machine. Hebern's alternative (1918 patent) failed
commercially, sold roughly a dozen units, and ended in bankruptcy and a fraud conviction. The
hoped-for banking framing is also **unsupported** — documented buyers were governments and
diplomatic services, not banks.

**The replacement is stronger anyway.** The **Jacquard loom → punched card → stored program**
lineage teaches the same determinism lesson (same card plus same configuration yields the same
output, every time). Cipher hardware was never the best vehicle for this lesson; it was only the
first one that came to mind.

## 4. Museum identity and data (resolves risk R2)

**The museum is fictional: "The Museum of Computing Heritage."**

- Every **machine** described is real and factually accurate.
- The **catalog dataset** is our own, clearly labelled as illustrative.
- **The National Museum of Computing (TNMOC)** is credited prominently as inspiration, with
  links, in the workshop landing page and every chapter's Go Deeper section.
- Contacting TNMOC is **recommended but not on the critical path.** They are an independent
  charity with no public funding and an explicit education mission; a series teaching modern
  AI through computing heritage is plausibly something they would support or promote.

**Rationale.** If the catalog claimed to be TNMOC's, every row would be a factual claim
about a real charity's holdings. During this design an exhibit was asserted that does not
exist there (a Meccano differential analyser — actually at the Science Museum London and
MOTAT Auckland). Fictional framing removes that entire class of error while still
celebrating the institution.

## 5. Technical constraints

| Constraint | Decision |
|---|---|
| **Cloud surface** | Amazon Bedrock only. Catalog on disk (SQLite/JSON), scans in-repo, UI on localhost. Matches the existing workshop's `AmazonBedrockFullAccess` participant policy. |
| **Paths** | One. `uv` + terminal + any IDE (Kiro, VS Code, PyCharm, Cursor). No notebook path, no dual-path callouts. |
| **Dependencies** | **One root `pyproject.toml`**, the single source of truth, per the *Once Upon Agentic AI* pattern (§10a is authoritative). `uv sync` once, then `uv run python N_folder/file.py`. `pip install .` also supported. **No PEP 723 blocks. Deliberately unpinned, no lockfile** — floors only where an API demands one. |
| **Chapter folders** | `N_snake_case_name/`, six of them, one per chapter, **all pre-existing on `main` with runnable `.py` files carrying `# TODO:` markers**. Participants fill gaps in files that already run; they never start from an empty file. |
| **Continuity** | Each chapter folder contains the previous chapter's finished code, **carried forward**, plus tonight's TODOs. Chapters never import from each other. A latecomer can start at any chapter. |
| **Solution branch** | **One branch, `solution`, kept current** — updated as each chapter is built with the audience. Its files **keep their `# TODO:` comments** with the answer written beneath, so a participant can diff line by line. |
| **Structured data** | Typed Pydantic models — the shape a developer would put behind an API, not a shape for analysis. |
| **Cloud as narrative** | Production paths (AgentCore, Knowledge Bases, deployment) are discussed and linked, never required. |
| **Out of scope (2026-08-04)** | **MCP and multi-agent orchestration.** Go Deeper links only — see §1a for the verified reasoning and R32 for the accepted cost. |

## 5a. Gamification: Museum Certification

**The game loop is the curator's actual job: answer visitor questions correctly.**

The win condition is not "my code ran" — it is **"my Curator satisfied the visitor."** Each
chapter ships an **acceptance suite** of visitor questions the participant's Curator must
pass to be *certified* for that gallery.

```
Gallery 1: When Computers Were People ... CERTIFIED  3/3   the tool was called, nothing invented
Gallery 2: The Wheel and the Wave ....... CERTIFIED  5/5   + every answer inside 1200 ms
Gallery 3: What the Hand Wrote .......... FAILED     7/8   judge: page 17 read confidently wrong
Gallery 4: Eighty Hours Unattended ...... LOCKED
```

**Why this is structural rather than decorative.** The Strands Evals SDK *is* the scoreboard.
No badge system, no XP counter, no quiz engine — the game and the curriculum are the same
artifact. Participants practise test-driven development against an acceptance suite, which is
a genuine industry skill, and it happens to feel like clearing levels.

### The scoreboard is readable from Chapter 1 (decided 2026-08-04, supersedes the blind design)

**Rule: no chapter ever shows a red the participant cannot read, explain, and fix that same
evening.** Nothing is carried as a mystery. This is the audience-facing decision that follows from
the medium — a viewer watching a livestream or a YouTube video who sees an unexplained failure and
is told *"you will find out in week four"* closes the tab. Frustration is the churn mechanism for
episodic content, and a scoreboard nobody can read is a frustration generator.

So the Evals SDK is **taught from Chapter 1** and every chapter adds exactly **one new kind of
check.** The API surface grows one concept at a time, which is also how it stays inside Rule 1.

| Ch | The new kind of check it adds | Why that kind belongs there |
|---|---|---|
| **1** | **Deterministic trajectory assertion.** `Case` + `Experiment` + `TrajectoryEvaluator` with `in_order_match_scorer`: *was `find_exhibit` actually called?* Three lines of eval code | It is **binary** — no judge model, no rubric, no flake. And it proves the chapter's own lesson mechanically: red while the Curator fabricates, green the moment the tool is wired |
| **2** | **A threshold on a number.** Same `Case` objects, one added latency assertion: *did the answer arrive inside the visitor's patience?* | The API is already known, so the new material is a *dimension*, not a mechanism. Voice is where latency becomes correctness, so the threshold has a reason to exist |
| **3** | **The first judge model.** `OutputEvaluator(rubric=…, model=…)`, plus an image-grounded rubric for the scan | *"Did it transcribe this page correctly?"* is not binary, so this is where a judge is genuinely required rather than merely available. The contrast with Chapter 1's deterministic assertion is the lesson: **use a judge only when you cannot write an assertion** |
| **4** | **Depth, not a new primitive.** Traces and `HelpfulnessEvaluator`, `ActorSimulator` for multi-turn visitors, chaos/fault injection, `diagnose`, and `--fail-on` as a CI gate | By now three chapters of cases exist and the participant wants them to run automatically, on every change, with a root cause when they break. Evaluation stops being a script and becomes an engineering discipline |
| **5** | **Formal proof.** Cases where the Curator is *provably* wrong — a class of check neither an assertion nor a judge can express | Requires Automated Reasoning, which is Chapter 5's subject |
| **6** | **Adversarial.** Red-team strategies (Crescendo, GOAT, PAIR, BadLikertJudge, SequentialBreak) run against the Guardrails boundary | A boundary is only real if it survives attack, and you cannot attack a boundary that does not exist yet |

**Deterministic first, judged later, and that ordering is deliberate.** Chapter 1's assertion cannot
flake, which matters enormously for a graded game in week one (R13). A participant whose correct
solution goes red because a judge model was moody in episode one does not come back for episode two.
By Chapter 3 they have seen a reliable scoreboard three times and have the context to accept that
judged scores are advisory while structural checks are binding.

**The model swap and the scoreboard are the same beat in Chapter 1.** This is the strongest
consequence of the change. Rather than choosing a model by watching token counts scroll past, the
participant runs the **same `Experiment` against all three model IDs** and reads three score
reports. That is what `Experiment` is for, it is how the decision is actually made in production,
and it turns *"which model should I use?"* from a vibe into a measurement. Chapter 1's concept
sharpens accordingly: **choose your instruments on evidence.**

### The payoff, which is what the series is ultimately arguing

By Chapter 6 the suite is six weeks old and catches six classes of failure, and it runs on every
change. The closing demonstration of the whole series is this:

> Change a prompt in week six. **The case you wrote in week one goes red.**

That single moment is the added value of evaluation for agentic workloads, and it cannot be
demonstrated by a chapter — only by an accumulated suite. An agent is a system whose behaviour
drifts when *anything* changes: the prompt, the model, a tool description, the SDK version. Nothing
in ordinary testing practice catches that, and no amount of "I tried it a few times and it seemed
fine" substitutes. **The suite is the only artifact in the workshop that gets more valuable every
week**, and the participant built it themselves from episode one.

**Mechanics.**

| Mechanic | Implementation | Cost |
|---|---|---|
| **Acceptance suite per gallery** | `cases.py` per chapter folder, authored by the participant from Chapter 1; `certify.py` runs it | Low — the runner is provided and barely changes |
| **The suite accumulates** | Each chapter carries the previous `cases.py` forward and appends tonight's. Ch 1 ends with 3 cases, Ch 3 with 16, Ch 6 with roughly 30 | Free — side effect of the §10a carry-forward rule |
| **Failures name the visitor** | A failing case reports *which* visitor question broke and how, not just a red bar | Rubric authoring per case |
| **Every red is closed in its own chapter** | A chapter may go red mid-episode; it must be green by the closing beat | Authoring discipline — this is the hard rule above |
| **Progressive certification** | Galleries accumulate certifications; Ch 4 makes the whole suite a CI gate; Ch 5 and Ch 6 each donate a new class of check | Free — follows the arc |

**Consequence for chapter structure.** Every chapter's existing "you'll know you're done
when…" line gains a machine-checkable twin: the certification run. The participant does not
have to *believe* the chapter worked; they can prove it — **from the first episode.**

**Chapter 1's certification is the sharpest teaching moment in the series.** The participant writes
one three-line case, runs it against a Curator with no tool and watches it go red, wires
`find_exhibit`, runs it again and watches it go green. Probabilistic component, deterministic tool,
and a scoreboard that knows the difference — in week one, with nothing held back.

**Explicitly not included** (rejected as bolt-on machinery that adds authoring cost without
teaching): XP counters, badge art, leaderboards, prose quizzes.

## 5b. Two structural rules (hard)

These govern chapter design and override convenience. Both were added 2026-08-04 and both were
load-bearing in the restructure the same day.

### Rule 1 — One concept per chapter

Each chapter teaches **exactly one idea**, because each chapter is one Twitch livestream and one
YouTube video, and retention is the point. A learner must be able to finish an episode and say what
it was about in one sentence.

**A concept is a theme, not a single API.** One concept may carry several technologies, and usually
does — what makes it one concept is that the technologies serve a single idea the learner takes away.
Chapter 1 is *"choose your instrument on purpose"*: that carries the Strands Agents SDK, a custom
`@tool`, the community tools package, Bedrock's multi-model catalog, a one-line model swap, and
token/latency measurement. Six technologies, one idea, one sentence.

The test is not "how many APIs appear" but **"can the learner state the takeaway in one sentence,
and did the fun come from experimenting with that one thing?"** If an episode needs two sentences
joined by *and*, it is two chapters.

| Ch | The one concept, in a sentence |
|---|---|
| 1 | Choosing your instruments on purpose — the tool that computes exactly, and the model that reasons |
| 2 | A continuous world reaches a machine only as samples, and how fast you answer is part of being right |
| 3 | Turning an analog artifact into typed data, where validation failure drives the retry |
| 4 | How you test something that never answers the same way twice |
| 5 | Some claims can be *proved* wrong, not merely judged wrong |
| 6 | A boundary is only real if it survives someone attacking it |

### Rule 2 — Strict chronological order, by anchor year

Chapters advance forward through history. **A learner walking chapters 1→6 never travels backwards
in time.** The historical arc is the spine of the series, and a reverse jump breaks it.

**Sharpened 2026-08-04.** Ranges are allowed to overlap; **anchor years must strictly increase.**
Each chapter declares one anchor — the year of the thing the chapter is *about* — and that is what
the ordering is checked against. The old design compared ranges, which was ambiguous the moment two
chapters overlapped (Ch 3's "1930s–1950s" against Ch 4's "1949–1986" already did, silently).

| Ch | Chapter | Anchor | Range | What the anchor is |
|---|---|---|---|---|
| 1 | When Computers Were People | **1885** | 1804–1885 | Felt's Comptometer prototype — the deterministic instrument |
| 2 | The Wheel and the Wave | **1928** | 1928–1949 | Bush's analyser begun *and* Nyquist's rate limit published — the same year |
| 3 | What the Hand Wrote | **1948** | 1948–1969 | Turing's *Intelligent Machinery*, NPL |
| 4 | Eighty Hours Unattended | **1951** | 1951–1973 | The WITCH operational at Harwell — reliability as the headline metric |
| 5 | Prove It | **2020s** | 1943 backstory → present | The neuro-symbolic rejoining, as a managed service |
| 6 | Opening Day | **now** | now | The Curator goes live |

1885 < 1928 < 1948 < 1951 < 2020s < now. The ladder holds.

**Where history and dependency order conflict, move the anchor — never the chapter.** Chapter 2
cannot come sixth just because a voice agent is the newest thing in the series; and it cannot be
anchored to 1990s codecs, because that would jump the timeline forward past Chapters 3 and 4 and
then back again. So the anchor moves to the era of the **conversion** being taught — sampling a
continuous quantity, which Nyquist bounded in 1928 and Shannon proved in 1949 — rather than the era
of the consumer technology. Same for Chapter 5: the 1943–1956 founding papers are backstory; the
anchor is the present-day rejoining, which is what actually ships.

This is honest rather than a fudge — a museum chooses what a gallery is *about*. "The Wheel and the
Wave" is about a continuously varying quantity becoming numbers, and the mathematics of that is
1928–1949. The title names both halves: the **wheel** is Bush's integrator rolling against a disc,
the **wave** is what Nyquist and Shannon taught us to sample.

**1928 is a genuine coincidence worth opening the chapter with.** Vannevar Bush began the
differential analyser and Harry Nyquist published the rate limit in the same year: one machine that
computed by rolling a wheel against a disc, and one paper saying how often you must look at a wave
to keep it.

## 5c. Chapter titles and folder names

**Two layers, and they are deliberately different**, because the reference workshop does it that way:
*Once Upon Agentic AI* pairs the creative catalog title `⚔️ Chapter 2: Built-in Tools` with the plain
folder `2_built_in_tools/`. **The title sells the episode; the folder name is the syllabus.**

Earlier drafts of this spec had that backwards — themed folder names (`1_the_instrument_room/`) and
flat titles. Corrected here.

| # | Catalog title | Folder | The technical topic |
|---|---|---|---|
| 0 | 🏛️ **Chapter 0: Before the Doors Open** | *none* | Prerequisites, AWS account, Bedrock access, `uv sync` |
| 1 | 🧮 **Chapter 1: When Computers Were People** — Your First Agent, Its Tools, and Choosing a Model | `1_first_agent_and_tools/` | Strands `Agent`, custom `@tool`, `strands_tools`, Bedrock model swap, first `Case` |
| 2 | 🎙️ **Chapter 2: The Wheel and the Wave** — Talking to the Curator | `2_voice_agent/` | Nova 2 Sonic, `BidiAgent`, `FileSessionManager`, latency thresholds |
| 3 | ✍️ **Chapter 3: What the Hand Wrote** — Reading the Archive | `3_multimodal_and_schemas/` | Converse image blocks, Structured Output, retry on `ValidationError`, first judge |
| 4 | ⏱️ **Chapter 4: Eighty Hours Unattended** — Trusting What You Built | `4_evaluation_at_scale/` | Traces, `ActorSimulator`, chaos, `diagnose`, `--fail-on` CI gate |
| 5 | ⚖️ **Chapter 5: Prove It** — When Judgement Is Not Enough | `5_automated_reasoning/` | Automated Reasoning checks, formal policy, rewriting loop |
| 6 | 🎟️ **Chapter 6: Opening Day** — Holding the Line in Public | `6_guardrails_and_launch/` | Guardrails, streaming UI, red-team evaluators, cost per session |
| — | 🧹 **Resource cleanup** | *none* | Delete guardrails, AR policies, and any deployed surface |

**Why each title is what it is** — the rule is that a title must be *true*, not merely evocative:

- **When Computers Were People** is TNMOC's own gallery subtitle, credited as theirs. It is also
  literally what Chapter 1 is about: a human computer choosing an instrument for a job.
- **The Wheel and the Wave** names both halves of the merged chapter in four words — the
  integrator's wheel rolling on its disc, and the sound wave being sampled. It is the shortest
  honest description of *"a continuous quantity reaching a machine that can only sample it."*
- **What the Hand Wrote** is the artifact: a 1948 page with a handwritten annotation on it.
- **Eighty Hours Unattended** is the WITCH's real reliability record, and reliability is exactly what
  the chapter teaches you to measure. A number in a title also sets the expectation that this
  chapter is about evidence.
- **Prove It** is two words and the entire concept. The subtitle does the escalation from Chapter 4.
- **Opening Day** is the museum's, and the subtitle says what actually happens: someone immediately
  asks about the building next door.

**Chapter 0 and Resource cleanup are catalog pages with no folder**, exactly as in the reference
workshop (§10a rule 11 — OUAA's README links `0_pre_requisites/`, which does not exist). Cleanup is
not optional: Chapters 5 and 6 create guardrails and Automated Reasoning policies that persist in the
account.

## 6. Chapter design

Each chapter follows the established *Once Upon* template: frontmatter → header image →
**Before You Code** (the new word / why we need it / ASCII mental model / *"you'll know
you're done when…"* / first file you'll touch) → Quest Objective → numbered Steps anchored
on `# TODO n` markers → Checkpoints between steps → Testing → **Certification run** →
Troubleshooting → Quest Complete (learned + loot) → Go Deeper → closing italic quote.

Failure modes are taught **inline as callouts**, before they bite — not in an appendix.

**Certification run** is the new section this workshop adds versus *Once Upon Spring AI*: a
command the participant runs to prove the gallery works, plus how to read the report when a
visitor question fails. See §5a.

### Level ladder

Per the leveling guide's "stay in your chosen lane," levels are declared per chapter and
held:

| Ch | Level | What earns it |
|---|---|---|
| 1 | 200→300 | Assumes Python/terminal/AWS. First agent, the fabrication beat, the tool that fixes it, a first `Case`, and a three-model swap **scored rather than eyeballed** |
| 2 | 300→400 | Async event-driven streaming, sampling made audible, latency as an asserted threshold, session expiry and reconnection |
| 3 | 300 | Schema design, image token cost, ambiguity handling, validation-driven retry, and the first judge model — with the rule for when *not* to use one |
| 4 | 400 | Trace-based evaluation, simulated multi-turn visitors, chaos testing, root-cause diagnosis, CI gates |
| 5 | 400 | Formal logic as a verification layer; authoring a symbolic policy; proof over judgement |
| 6 | 400 | Policy enforcement in the request path, adversarial verification, cost per session |

**The dip at Chapter 3 is deliberate and is named on air** (R30). A 300-level chapter after a
300→400 one is a breather episode, which is fine for retention; the reverse — a spike with no
warning — is not. Chapter 3 is where the audience catches its breath before Chapter 4's CI gate.

**Measurement discipline, and it is now the Evals SDK's job from the start.** The guide asks for
performance metrics at 300 and code-level exploration at 400. Chapter 1 introduces a thin **inspect
helper** that prints per-turn token counts and latency — but the *decision* it informs is made by an
`Experiment` run across three model IDs, not by reading numbers off a screen. The helper explains
where the numbers come from; the scoreboard is what settles the argument. Chapter 4 then replaces the
helper entirely with real OpenTelemetry capture
(`StrandsEvalsTelemetry().setup_in_memory_exporter()` + `StrandsInMemorySessionMapper`).

---

### Chapter 1 — 🧮 When Computers Were People
*Your First Agent, Its Tools, and Choosing a Model* · folder `1_first_agent_and_tools/`
**Level 200→300 · Strands Agents basics: custom tools, community tools · Bedrock: one-line model swap · Evals: the first `Case`**

**Anchor: 1885. Era: 1804–1885.** The oldest gallery, so it opens the series.

**History.** Instructions on a medium came first. **Jacquard's loom** (first years of the 1800s)
takes its pattern from a chain of punched cards: mount the same cards on the same loom and you get
the same cloth, every time. Babbage owned a woven silk portrait made that way, and the punched card
went on to the Analytical Engine, Hollerith's tabulators, and eventually the stored program.

Then "computer" as a **job title**. A human computer *chose an instrument for the job* — slide rule
for a quick logarithm, abacus for exact addition, and from 1885 Dorr E. Felt's **Comptometer**
(prototype 1885, first practical machine October 1886, patents 1887), the first commercially
successful *key-driven* mechanical calculator, in production into the mid-1970s. Every one of these
instruments was trusted for exactly one reason: **they were deterministic.** Same cards, same
cloth. Same keys, same total.

**Engineering.** The concept is **instrument choice, on evidence** — at two layers, with a scoreboard
watching both.

*Layer one — the instrument that computes.* The first Curator agent: persona, system prompt, one
file, one command. Then immediately the problem the whole series exists to solve. The Curator is
asked a **catalog** question with no tool available — *how many dekatrons does the WITCH have?* — and
**confidently invents a number.** The participant writes `find_exhibit`, a deterministic `@tool`
that reads `catalog.json`, and the cycle count goes from 1 to 2: that diff *is* the agentic loop,
observed rather than lectured.

Then a **second** question, arithmetic this time — *how many years between the Comptometer patent and
the WITCH going operational?* — and the reveal that this one they need not write at all:
`from strands_tools import calculator`. Two tools, two different decisions, and that contrast **is**
the judgement call: nobody ships a tool that knows your museum's catalog, and nobody should be
writing their own `add`.

**`find_exhibit` is the tool the rest of the series carries forward.** It is what this chapter's own
`TrajectoryEvaluator` asserts was actually called, what Chapter 2 makes speakable, what Chapter 4's
simulated visitors reach for in conversations nobody wrote, and what Chapter 5's policy proves the
Curator described correctly. Naming it here and never renaming it is what makes the carried-forward
code — and the carried-forward *cases* — legible in every later folder.

*Layer two — the scoreboard, introduced the moment it is needed.* Before the model swap, one
question: *how do you know the tool is being called and not just described?* Reading the log works
once. It does not work every week for six weeks. So the participant writes their first `Case` — three
lines — and asserts it mechanically:

```python
from strands_evals import Case, Experiment
from strands_evals.evaluators import TrajectoryEvaluator
from strands_evals.scorers import in_order_match_scorer

case = Case(
    name="dekatron_count_uses_the_catalog",
    input="How many dekatrons does the WITCH have?",
    expected_tools=["find_exhibit"],
)
```

Run it against the Curator *before* the tool exists: **red.** Wire `find_exhibit`: **green.** No
judge model, no rubric, no flake — the check is binary, which is exactly what week one needs
(R13). The scoreboard's first act is to prove the chapter's own lesson.

*Layer three — the instrument that reasons, chosen by score.* Now the model swap, and it is not a
tour. The **same `Experiment` runs against all three Bedrock model IDs** and prints three reports:
pass rate, tokens, latency. The participant chooses a model by reading evidence, which is how the
decision is actually made in production — and it is what `Experiment` exists for.

A human computer picked a slide rule or a Comptometer depending on whether they needed speed or
exactness. That was a judgement made from experience. Ours is made from a scoreboard, and the
chapter's sentence is *choose your instruments on evidence.*

The three reports come from `inspect_agent.py`, a thin helper the participant writes in this chapter
to print per-turn token counts and wall-clock latency. It exists to show **where the numbers come
from**, so the `Experiment` output is not magic. Chapter 4 deletes it and replaces it with real
OpenTelemetry capture — which is the honest arc: hand-rolled measurement first, instrumentation once
you know what you are measuring.

Tool return values are ordinary Python values here. Schema-constrained *agent responses* are
Chapter 3's subject.

**Done when** the participant's own case goes from red to green as `find_exhibit` is wired, and the
same suite has scored three models — so they can say which one they would ship and point at the
number that decided it.

**Failure modes taught.** Three, ordered so each one costs less than the last to discover:
prompt instructions are requests, not guarantees (the system prompt says *never invent a fact*, and
it invents one anyway); a vague tool description gets **silently skipped**, because the model reads
that description like a search query; and a model ID with a typo, which is the most common Bedrock
error there is and looks identical to no access.

**Certification — 3 cases, all green by the closing beat.** The fabrication case, a tool-choice case
(the arithmetic question routes to `calculator`, not `find_exhibit`), and a scope case the Curator
already passes. The participant wrote all three and can read all three. **Nothing is carried into
next week unexplained.**

**Why the Evals SDK belongs in episode one, not episode four.** Three reasons, and the first is the
one that matters most on stream: a viewer who sees an unexplained red bar and is told to wait a month
does not come back. The second is that `TrajectoryEvaluator` is the *simplest* thing in the SDK —
three lines, no judge, no rubric — so it costs almost nothing to teach here. The third is that the
model swap needs it: without a scoreboard, "which model should I ship?" is a vibe.

**Real exhibits referenced.** TNMOC's *Slide Rules and Calculators* gallery, subtitled *"When
computers were people."*

---

### Chapter 2 — 🎙️ The Wheel and the Wave
*Talking to the Curator* · folder `2_voice_agent/`
**Level 300→400 · Bedrock: Nova Sonic speech-to-speech · Strands Agents: bidirectional streaming + session persistence · Evals: latency as an assertion**

**Anchor: 1928. Era: 1928–1949.**

**History — two things started in 1928.** Analog computation works by *physical analogy*: a
continuously varying quantity — shaft rotation, voltage — **is** the number. A differential
analyser integrates by rolling a wheel against a disc. Vannevar Bush and Harold Hazen built MIT's
six-integrator machine **1928–1931**; Hazen solved weak integrator torque using Nieman's torque
amplifier, and Bush named the machine in his October 1931 *Journal of the Franklin Institute*
paper. Precision was bounded by the machine's fidelity, not by digits.

That same year, **Harry Nyquist** published the result bounding how fast a channel can carry
distinct signals. **Claude Shannon operated Bush's analyser from 1936**, wrote the 1937 master's
thesis applying Boolean algebra to switching circuits, and then in *"Communication in the Presence
of Noise"* (**1949**) stated and proved the sampling theorem that carries both their names — the
result that tells you how often you must sample a continuous waveform to reconstruct it faithfully.

One person ran the machine that *was* a continuous quantity, and then proved how to turn continuous
quantities into numbers. That is this chapter, in one biography.

**Engineering — the same decision, twice, forty years apart.**

*The cold open.* Participants compute by physical analogy themselves — a fifteen-line integrator
where a wheel's rotation accumulates against a turning disc, with no instruction set anywhere. Its
`steps` parameter is the analog/digital boundary made visible: the real machine had no `steps`.
Fewer steps, wrong answer. This is sampling, with the sampling exposed as a variable.

*Then they hear it.* The participant records their own voice and plays it back at descending sample
rates until it breaks. The theorem stops being a formula and becomes a sound.

*Then they talk to the Curator.* Nova Sonic is a **speech-to-speech** model: it does not transcribe
to text, reason, then synthesise. Speech understanding and generation are unified, which is why it
can adapt delivery to the prosody of the input and handle interruption without losing context.

Strands wraps the event choreography, so participants build a voice agent rather than a
WebSocket state machine — and **Chapter 1's tool drops into the constructor unchanged**:

```python
from strands.experimental.bidi import BidiAgent
from strands.experimental.bidi.io import BidiAudioIO, BidiTextIO
from strands.experimental.bidi.models import BidiNovaSonicModel
from strands_tools import stop

model = BidiNovaSonicModel(
    model_id="amazon.nova-2-sonic-v1:0",
    provider_config={"audio": {"voice": "tiffany"}},
    client_config={"region": "us-west-2"},
)
agent = BidiAgent(model=model, tools=[find_exhibit, stop])
await agent.run(inputs=[audio_io.input()], outputs=[audio_io.output(), text_io.output()])
```

`stop` is the second community tool of the series and it is there for a reason a text agent never
needs: a spoken conversation has no Ctrl-C. It is how the visitor ends the session by saying so,
which is Chapter 1's *import-don't-write* judgement call showing up again in a modality that makes it
obvious.

Which makes this line, in the audio configuration, the most quietly loaded line in the workshop:

```python
"input_rate": 16000
```

That is the sampling theorem, in a config file, typed by developers who have never been told whose
theorem it is — and it belongs to the same person who ran the analog machine at the top of the hour.

**The product.** Museums have audio guides. The analog one was a cassette handset on a lanyard.
The modern one is a voice agent. Same product, ninety years apart — legacy-to-modern in a single
object most of the audience has physically held. Radio and the cassette handset are told as the
*lineage* of the medium, not as the anchor.

**Why this is genuinely 400-level, not a feature tour.** Chapter 1 was synchronous
request-response. Voice is none of those things:

- **Async throughout.** `asyncio`, concurrent input and output streams, and `agent.stop()` that
  must be called *after* the receive loop exits, never during.
- **A latency budget that is felt, not measured.** A pause that reads as thoughtful in text reads
  as broken in speech. Tools must return fast or the conversation stalls.
- **Sessions expire, and this is the chapter's second feature.** Nova Sonic caps a session at
  roughly 8 minutes, and conversation history at 50KB per message and 200KB total — silently, only
  visible in debug logs. A museum visit is longer than 8 minutes, so **session persistence and
  reconnection is a product requirement**, not a nice-to-have. Participants wire
  `strands.session.FileSessionManager` so a reconnected session resumes the visit instead of
  restarting it. This earns its place the same way Chapter 6's Guardrails do: the building demands
  it.
- **Local versus server-side I/O.** `BidiAudioIO` uses PyAudio for a laptop microphone;
  browser and mobile clients need custom `BidiInput`/`BidiOutput` handlers. That distinction is
  the difference between a demo and a deployment.

**Reuse, not new surface.** Chapter 1's custom tool and community tools become *speakable* with no
rewrite, one week after being written. That is the lesson: **a well-built tool does not care what
modality asked for it** — and at position 2 the participant still remembers writing it.

**Scoped out of this chapter, deliberately.** `turn_detection` / `endpointingSensitivity` tuning is
a `bonus_quest.py`, and the transcript-guardrail path belongs to Chapter 6 where both enforcement
paths are contrasted. Both were in the original 400-level design and both would push this chapter
past one concept.

**Done when** a visitor holds a conversation with the Curator by voice, interrupts it
mid-sentence and it recovers, and the session survives past the eight-minute limit with the
visit's history intact.

**Failure mode taught.** A voice agent that is *correct but too slow* is worse than a text agent
that is slower still, because silence in a conversation reads as failure. Latency is a
correctness property here.

**Certification — one new check: a threshold on a number.** Chapter 1's cases assert *which tool
ran*; that is a set comparison, and it cannot express "too slow." So the participant adds the second
kind of assertion they will ever need: a **number with a limit on it**.

```python
case = Case(
    name="opening_hours_answered_within_1200ms",
    input="What time do you close?",
    expected_tools=["find_exhibit"],
)
# The threshold lives in the scorer, not the prompt: latency_under(1200)
```

**It goes red on the first run, and that is the script.** The naive implementation answers correctly
and arrives late, because the tool call is awaited before any audio is emitted. The participant
*hears* the four seconds of silence, then reads the same failure as a number on the scoreboard —
`FAILED 4/5 · answered in 3980 ms, limit 1200 ms`. Nova 2's asynchronous tool handling (the
assistant keeps speaking while the tool runs) is the fix, and the case turns green in the same
episode.

That is the sequence that earns the SDK its keep on air: **a thing they felt, restated as a number,
then closed.** Not a red line carried into next month.

**Cumulative state at the closing beat:** galleries 1 and 2 both `CERTIFIED`, 8 cases green. The
participant now owns two assertion kinds — *did the right thing happen* and *did it happen fast
enough* — and neither one needs a model to judge it. Judges arrive in Chapter 3, once the habit is
already boring.

**Model version.** Use **Nova 2 Sonic** (`amazon.nova-2-sonic-v1:0`), not Nova Sonic v1. Nova 2
adds automatic language detection and switching, polyglot voices, intelligent turn-taking,
asynchronous tool handling (the assistant keeps speaking while a tool runs), a 1M-token context
window, and `turn_detection` configuration — which raises `ValueError` on v1. Available in
`us-east-1`, `us-west-2`, `eu-north-1`, `ap-northeast-1`. Requires Python 3.12+ and the
`strands-agents[bidi]` extra.

**Real exhibits referenced.** TNMOC's Simulation gallery, and specifically the **PACE TR-28** — a
real analogue computer the participant can point at after writing fifteen lines that behave like one.
Plus the museum's own **cassette audio guide**, which is the product lineage the voice agent
continues.

*The Cray-1 was cut from this list on 2026-08-04.* It is in the same gallery and it is a magnificent
object, but nothing in this chapter consumes it: a 1976 vector supercomputer is not an analogue
machine, not an audio guide, and not a sampling story. It was decoration (§13).

---

### Chapter 3 — ✍️ What the Hand Wrote
*Reading the Archive* · folder `3_multimodal_and_schemas/`
**Level 300 · Bedrock: multimodal · Strands Agents: Structured Output · Evals: the first judge model**

**Anchor: 1948. Era: 1948–1969.**

**History.** Before data was digital it was handwriting — lab notebooks, logbooks, index
cards. This is the literal analog-to-digital boundary, and it remains unsolved in most
organisations today.

**Engineering.** Two features that are really one loop here.

Bedrock Converse with image blocks turns a photographed handwritten page into text. **Strands
Structured Output** then constrains the agent's response to a Pydantic model, so the page
arrives as a typed object rather than prose to be parsed. And because the two are combined,
**validation failure becomes the retry trigger**: ambiguous handwriting fails the schema, and
that failure — with its field-level detail — is what gets fed back on retry.

Then the parts tutorials skip: image sizing and its token cost, what to do when handwriting is
genuinely ambiguous, and how to represent low confidence honestly instead of guessing.

**Done when** a scan of period handwriting becomes a validated Pydantic object — and a
deliberately hard page demonstrates the retry loop firing on a validation error.

**Failure mode taught.** A model that transcribes fluently and wrongly, with no confidence
signal — the most dangerous failure in the series, because it looks like success. Structured
Output narrows it (a wrong *shape* is now caught mechanically) but does not eliminate it: a
schema-valid transcription can still be factually wrong. **This is the chapter where the
participant runs out of mechanical checks** — and that is precisely why the judge model is
introduced here rather than earlier.

**Why this is Structured Output's natural home.** The chapter's whole purpose is turning an
analog artifact into structured data. Teaching the feature here means it is used the moment it
is learned, on the problem it was designed for — instead of being introduced abstractly with
dice results and re-applied a chapter later.

**Source document (resolves risk R1 — revised 2026-08-04).** The artifact is **real**: Alan
Turing's *"Intelligent Machinery"*, National Physical Laboratory, **1948** — a 23-page archival
scan published by NPL with **no text layer at all** (verified: zero extractable characters, 300 dpi
bilevel `CCITTFaxDecode` images). The model must genuinely read the page; it cannot lift an embedded
transcript.

**We link, we do not redistribute.** NPL publishes the scan for download but states no reuse licence
for its historical documents, so the repo ships a `fetch_turing.sh` script and gitignores the PDF.
Participants fetch it themselves — which is also the more honest exercise, because that is what
working with a real archive is like.

**Why this beats the hand-authored facsimiles it replaces.** The difficulty gradient is already in
the document: the cover is a typed label with a **handwritten** 1969 republication note beneath it;
typed page 1 is clean typescript; PDF page 13 carries **three hand-drawn neural-network diagrams**;
PDF page 17 is a faded, uneven strike. Ground truth is recorded up front by reading the pages during
pre-production, which is the one advantage facsimiles had.

**And the artifact is in dialogue with the exercise.** Participants point a 2026 language model at a
1948 paper asking *whether machinery can show intelligent behaviour*. Turing's own answer involved
"unorganised machines" trained by "interference mimicking education" — which is roughly what trained
the model doing the reading.

**Editorially verified, and it is not a wartime document.** Turing joined NPL in **1945**, after the
war; NPL describes the report as *"the possibility of a machine possessing the intelligence of man."*
No wartime content appears in the 23 pages — the nearest date reference is *"up to 1940"*, explaining
why people in 1948 assumed machinery was limited to repetitive jobs. The string *"enigma"* occurs
once, as *"enigmatic sayings"*, in a passage about St Augustine and Dorothy Sayers. §3 already
permits this paper by name among Turing's civilian work, and Chapter 5 already cites it.

**Certification — one new check: the first judge model.** Two chapters of assertions have all been
mechanical: a set of tool names, a number under a limit. Both are *cheap, deterministic and
unarguable* — and both are now **useless**, because a confidently wrong transcription passes them
all. It called the right tool. It answered fast. It filled every field. It is false.

So the participant reaches for the first evaluator that needs a model to run:

```python
from strands_evals.evaluators import OutputEvaluator

evaluator = OutputEvaluator(
    rubric="The transcription matches the source page. Illegible words appear in "
           "unreadable_fields rather than being guessed.",
    model="global.anthropic.claude-sonnet-5",
)
```

**Earning it, not just importing it.** The judge is introduced against the ground truth recorded in
pre-production, so the participant can check the judge itself: run it on a page they transcribed
correctly by hand, confirm it says so, *then* trust it on page 17. A judge nobody audited is just a
second opinion with a bigger bill.

**And the model-choice lesson returns at the eval layer.** `model=` on `OutputEvaluator` is the same
parameter the participant swapped in Chapter 1, one level up the stack: now they are choosing not
which model *answers* but which model *grades*. Same experiment, same scoreboard, different question.
The Chapter 1 habit pays for itself here.

**Red, then green, in-episode.** Page 17 fails the judge — `FAILED 7/8 · judge: page 17 read
confidently wrong`. The fix is not a better model; it is the honest-uncertainty contract already in
the schema. The participant makes `unreadable_fields` mandatory in the prompt, reruns, watches the
Curator admit it cannot read a word, and the case turns green.

**Cumulative state at the closing beat:** galleries 1–3 `CERTIFIED`, 16 cases green, three assertion
kinds owned — *what ran*, *how fast*, *was it true*. Everything in Chapter 4 is depth on these three.

---

### Chapter 4 — ⏱️ Eighty Hours Unattended
*Trusting What You Built* · folder `4_evaluation_at_scale/`
**Level 400 · Strands Evals SDK at depth · runs as two streams (4a / 4b)**

**Anchor: 1951. Era: 1951–1973** — reliability as the headline metric.

**History.** The **WITCH** began at AERE Harwell in 1949 and was operational from **April 1951** —
designed by Ted Cooke-Yarborough with 828 dekatrons and prized for **reliability rather than
speed**, running roughly 80 hours a week unattended and once about ten days alone over Christmas.
In 1957 Wolverhampton and Staffordshire Technical College won it in an Oxford competition, giving
the acronym its **T for Teaching** (Wolverhampton Instrument for Teaching Computing from Harwell);
it taught computing there until 1973. It was loaned to TNMOC in 2009, restoration completed 2012,
and Guinness recognised it in 2013 as the world's oldest **original** working digital computer —
*original* being the load-bearing word that distinguishes it from reconstructions.

The WITCH's celebrated property was not speed. It was **trustworthiness, measured in unattended
hours.** Reliability was the headline metric of early computing, and somewhere along the way we
stopped asking that of our systems. This gallery asks it again.

**Engineering — depth, not a new primitive.** The scoreboard has been green since week one. Sixteen
cases exist and the participant wrote every one. `strands-agents-evals` (v1.0.3, imports as
`strands_evals`) now stops being *three imports they use* and becomes *a harness they own*.

**The chapter opens on the honest limit of what they have.** *"Sixteen cases, all green. Now answer
me this: does the Curator work, or have you only tested the sixteen things you thought of? The WITCH
ran eighty hours a week unattended. Nobody sat with it. Tonight we find out whether yours could."*

That question is the whole chapter, and it is not answerable with more of the same. A hand-written
case list is a **sample the participant chose**, and its blind spots are exactly their own blind
spots. Everything below attacks that.

| SDK capability | Applied to | What it proves |
|---|---|---|
| `ActorSimulator` | Ch 2 voice, Ch 1 catalog | Conversations **nobody wrote** — a goal-driven simulated visitor generates turns the participant never thought to test, replayed as transcripts so voice runs in CI with no microphone |
| Trace-based evaluation + `HelpfulnessEvaluator` | all galleries | Grading a **real session** from its OpenTelemetry spans, not a synthetic input. `StrandsEvalsTelemetry().setup_in_memory_exporter()` + `StrandsInMemorySessionMapper` |
| Chaos testing (fault injection via plugin hooks) | Ch 2 voice path | **A slow tool stalls a conversation.** All sixteen cases pass on a healthy day; this asks what happens on a bad one |
| `diagnose` / root-cause analysis | the reds they already know | A failing session JSON yields a *cause*, not just a verdict — the difference between "case 7 is red" and "case 7 is red because the retry never fired" |
| `--fail-on` exit codes | CI | The scoreboard stops being something the participant runs and becomes something that **runs without them** — the WITCH property, in CI |
| `Experiment` at scale | the full golden set | Suite-level reporting, per-case drill-down, and a run history you can compare against last week's |

**Nothing in this table is a fourth assertion kind.** Trajectory, threshold and judge — the three from
Chapters 1–3 — remain the entire vocabulary. What changes is **who writes the inputs** (a simulator,
not the participant), **where the data comes from** (real traces, not fixtures), **what conditions it
runs under** (injected faults, not a healthy path), and **who runs it** (CI, not a human). That is the
progression from *testing* to *trusting*, and it is one concept, per Rule 1.

**Chaos testing moved target, and improved.** The original design fault-injected the MCP catalog
server. That server no longer exists (§1a). Injecting latency into the voice path is a better
exercise anyway: a synthetic timeout on a text call is a log line, while the same timeout in a
spoken conversation is four seconds of silence the participant hears — and they have a 1200 ms
assertion from Chapter 2 already sitting there to catch it.

**Done when** a prompt change that degrades the Curator **fails the build with nobody watching**, and
an `ActorSimulator` conversation finds at least one failure the participant's own sixteen cases
missed. That second condition is the payoff beat: *the tests you did not write are the ones that
found it.*

**Failure mode taught.** "I tried it three times and it seemed fine" — and its more dangerous
cousin, *"all my tests pass,"* when the tests are a self-portrait.

**Stream split.** 4a: `ActorSimulator`, trace-based evaluation, `HelpfulnessEvaluator` — everything
about *inputs and data you did not author*. 4b: chaos injection, `diagnose`, `--fail-on`, CI gates —
everything about *running unattended*.

**Certification — no new check, and that is the point.** This is the only chapter that adds no new
assertion kind. What it certifies is the **suite itself**: the sixteen cases plus whatever the
simulator surfaced, running green under injected faults, from CI, with nobody watching. Galleries 1–4
all `CERTIFIED` on a run the participant did not start by hand.

The closing beat is deliberately anticlimactic in the best way: the participant pushes a commit,
switches away, and the scoreboard reports back. *Eighty hours unattended*, in the only form available
to a 2026 workshop.

**Note on `uv`.** The SDK README uses `pip`/`venv`; all workshop instructions translate to `uv`.

**Real exhibits referenced.** The **WITCH**, in TNMOC's *First Generation* gallery — named here as
the machine's location, which is the only role that gallery plays in the series now. The WITCH itself
is consumed heavily: it is this chapter's title, its history, its reliability thesis, and the subject
of Chapter 5's `original`-qualifier proof.

---

### Chapter 5 — ⚖️ Prove It
*When Judgement Is Not Enough* · folder `5_automated_reasoning/`
**Level 400 · Bedrock: Automated Reasoning checks (neuro-symbolic AI) · Evals: formal proof as a case**

Pairs deliberately with Chapter 4's **Eighty Hours Unattended**: that chapter tests *empirically*
(run it and see), this one proves *formally* (derive it and know). Same museum, two epistemologies.

**This chapter MUST follow Chapters 3 and 4, and the reason is not only chronological.** Its closing
lesson — *a proof is only as good as its axioms* — is the escalation of Chapter 3's *a judge is only
as good as its rubric*, which Chapter 4 then stress-tested against inputs nobody wrote. As an opener
it would be unintelligible; as a follow-up it lands. It also donates cases to a golden set that must
already exist — and by now it does, sixteen cases deep.

**Anchor: the 2020s. Era: the neuro-symbolic revival, with 1943–1956 as backstory.**

**Why this chapter is anchored to the revival, not to 1943.** The *founding papers* are old; the
**rejoining** is happening now, and the rejoining is what this chapter teaches and ships. Anchoring
here keeps the timeline running forward (Chapter 4 ends in 1973, Chapter 6 is opening day) and
matches the engineering: Automated Reasoning checks are a 2020s managed service that depends on the
catalog, the facts and the eval taxonomy built in Chapters 1–4. The 1943–1956 material below is told
as **backstory** — the reason the revival is a *re*-union rather than an invention — not as the
chapter's present tense.

**History — the split that should never have happened.** The backstory, briskly: the field
was one thing, then two, and is now becoming one again.

- **1943 — McCulloch and Pitts**, *"A Logical Calculus of the Ideas Immanent in Nervous
  Activity."* The paper widely credited with founding neural networks has **logical calculus**
  in its title. Neural and symbolic were the same subject at birth.
- **1948 — Alan Turing**, *"Intelligent Machinery"*, introducing **B-type machines**, a kind of
  neural network. This is Turing's foundational AI work and it sits entirely inside our
  editorial scope — no wartime cryptanalysis anywhere near it. **And the participants have already
  held this document**: it is the scan Chapter 3 transcribed. In Chapter 3 they taught the Curator to
  *read* the page without caring what it said; here they find out it was about them. Return to PDF
  page 13, `Organising unorganised machinery`, and note that the hand-drawn diagrams their schema
  struggled to describe are a neural network sketched in 1948.
- **1952 — John von Neumann**, *"Lectures on Probabilistic Logics and the Synthesis of Reliable
  Organisms from Unreliable Components."* That title is this workshop's thesis. *Probabilistic
  logics* is the neural/symbolic tension in two words. And **"reliable organisms from unreliable
  components"** is precisely what participants have spent four chapters doing — building a
  trustworthy Curator out of a model that cannot be trusted. It also rhymes with the WITCH's
  reliability record from Chapter 4.
- **1956 — John McCarthy** coins *"Artificial Intelligence"*, and the field splits into symbolic
  and sub-symbolic, with separate conferences, journals and associations.
- **Since the 1990s** — d'Avila Garcez and Lamb document ongoing neuro-symbolic research. Its
  proponents argue **the field should never have been separated.**

**Why this is not too advanced — it names something already taught.** Chapter 1 is already a
neuro-symbolic lesson: the model fabricates a number (neural, probabilistic), the tool computes
it exactly (symbolic, deterministic), and the chapter is about making them cooperate. So the term
arrives as a **label for four chapters of lived experience**, not as new material. A participant
who watched the Curator lie and then watched a tool fix it already understands neuro-symbolic AI.

**Engineering.** Automated Reasoning checks are neuro-symbolic in production: a neural
language model generates, formal logic verifies. Unlike content filters and topic policies —
which are **binary gates** that block or allow — Automated Reasoning acts as a **verification
layer that explains itself**, citing the specific rules and variable assignments behind its
conclusion.

Four phases: create a policy from a source document (formal rules and variables are extracted,
with a **fidelity report** scoring coverage and accuracy), test and refine, deploy an immutable
version attached to a guardrail, then integrate at runtime.

Findings are a union — exactly one of `valid`, `invalid`, `satisfiable`, `impossible`,
`translationAmbiguous`, `tooComplex`, `noTranslations`.

**Why the museum genuinely needs this.** The catalog is a factual record, and factual records
have provable structure: chronology has orderings (the WITCH was operational April 1951, the
Comptometer patented 1887 — so "the Comptometer came first" is derivable), classification is
definitional ("the differential analyser is a stored-program computer" is false by definition), and
provenance is a lookup.

**And the series' own running caveat becomes a machine-checkable rule.** Chapter 4 warned that the
WITCH must be described as the oldest **original** working digital computer, because *original* is
what distinguishes it from reconstructions. That is exactly a formal rule about a qualifier that
changes a truth value — so Automated Reasoning can catch the Curator dropping the word. The
editorial discipline that governed six chapters of authoring becomes a policy the machine enforces.

This is also self-referential in a way worth saying on air: **during this workshop's own design,
a fact-check caught two false claims** — an exhibit asserted at TNMOC that does not exist, and a
machine dated 1931 that was actually built 1928–1931. Those are precisely the errors this chapter
automates.

**Progression: hand-built, then formal.** Participants first write a plain Python validator that
checks chronology and classification claims against the root `catalog.json`. They feel the
problem, and they discover the wall — a hand-rolled validator cannot explain *why* something is
wrong, cannot detect unstated assumptions, and grows unmaintainable as rules interact. Automated
Reasoning checks then arrive as the formal, managed, provable version. Same feel-the-problem-first
shape that worked for the judge model in Chapter 3, where hand-written mechanical checks ran out
before the judge was introduced.

**The callback that makes the runtime pattern land.** Chapter 3 fed a Pydantic `ValidationError`
back to the model as retry feedback. Chapter 5's rewriting loop is the same shape at a deeper
level: an Automated Reasoning finding — with its contradicting rules named — becomes the rewrite
instruction. *Validation failure as feedback* is now a pattern the participant has met twice, in
two registers.

**Done when** the Curator states something false about the collection, the policy **proves** it
false and names the rule, and the rewriting loop produces a response that validates.

**Failure mode taught — and it is the most intellectually important one in the series.** A
`VALID` result guarantees validity *only for what the policy's variables capture*.

Demonstrate it in the museum's own domain: *"The WITCH is the oldest working digital computer in
this gallery."* If the policy has no variable capturing **reconstruction versus original**, that
statement validates — and it is wrong, because the WITCH's claim depends on the word *original*.
The proof was sound; the axioms were incomplete.

**A proof is only as good as its axioms.** Participants must leave understanding that formal
verification moves the trust question rather than eliminating it — from "do I trust the model?"
to "do I trust my policy?" Which is Chapter 3's rubric lesson, one level deeper: *do I trust my
judge?* became *do I trust my axioms?*

**Constraints that shape the architecture, not footnotes.**
- **No streaming support.** Complete responses only. So Automated Reasoning cannot sit inline in
  Chapter 2's voice stream or Chapter 6's streaming UI — it is a post-hoc verification layer.
  This is a genuine architectural lesson about where verification can and cannot live.
- **Detect mode only.** It returns findings and never blocks. The application decides: serve,
  rewrite, or ask for clarification. Contrast with Chapter 6's Guardrails, which do block.
- **English (US) only** — worth noting against Chapter 2's multilingual voice.
- **No prompt-injection protection, no off-topic detection.** Those need content filters and
  topic policies, which is Chapter 6. The features are complementary, and saying so prevents a
  participant from over-trusting any single control.
- Source documents: 5 MB and 50,000 characters maximum. Validation adds latency.

**Certification — one new check: a proof, not an opinion.** Chapter 3's judge returns a *graded
verdict*; this chapter's policy returns `invalid` **and names the rule that was contradicted**. The
participant writes a case whose expected result is a finding, so the golden set gains a class of
check that neither judges nor structural assertions could express — and, unlike the judge, it cannot
disagree with itself between runs.

The headline case is the *original* one: the Curator drops the word from "the oldest original working
digital computer," the policy proves the claim false, cites the qualifier rule, and the rewriting loop
produces a response that validates. Gallery 5 goes green on evidence no model was asked to weigh in on.

---

### Chapter 6 — 🎟️ Opening Day
*Holding the Line in Public* · folder `6_guardrails_and_launch/`
**Level 400 · Bedrock: Guardrails · Evals: adversarial red-team evaluators**

**Anchor: now.**

**History.** TNMOC's own mission is education — it runs learning spaces and school programmes, and
that mission is why the museum exists at all. The museum was built to teach. So was the Curator, and
tonight it meets the public.

*Named facilities were cut here on 2026-08-04.* An earlier draft listed the Innovation Hub and the
BBC Classroom by name. The chapter consumes the **mission**, not the room list — and a named room
that no beat uses is decoration a fact-checker still has to verify (§13).

**Engineering.** A real UI (Vite dev server on localhost), streaming responses, and cost per
visitor session. Then **Guardrails as scope enforcement**: because this museum sits in Block
H at Bletchley Park, visitors ask about wartime codebreaking. The Curator must hold its lane
and redirect gracefully, in character. The Evals SDK's **red-team evaluators** (Crescendo, GOAT,
PAIR, BadLikertJudge, SequentialBreak) — introduced here, not in Chapter 4 — then *prove* the
boundary holds under adversarial pressure.

**Two enforcement paths, and the contrast is the lesson.** Verified 2026-07-28: Nova 2 Sonic does
integrate with Bedrock Guardrails, but **Guardrails supports text and image modalities only** — the
Bedrock FAQ states plainly that it *"supports both text and image content."* Audio is not a
guardrail modality. So the enforcement point on the voice path is **the transcript, not the
waveform**: Nova Sonic's bidirectional stream emits ASR transcriptions of user speech and text
responses alongside the audio, and those text events are what you guard, via `ApplyGuardrail` with
`source=INPUT` / `source=OUTPUT` and `bedrock:ApplyGuardrail` on the execution role.

Three real problems arrive with the voice path, and they are the strongest 400-level material here:

1. **A race against the speaker.** Guardrails buffers streaming text and evaluates in chunks —
   but audio is already playing. Guarding the *output* transcript risks blocking text the
   visitor has already heard. Enforcement therefore belongs on *input* transcription, before the
   model responds, or you knowingly accept a leak window.
2. **Latency versus safety, priced.** Each `ApplyGuardrail` call is separately billed with its
   own round trip. In a conversation with a sub-second budget, that cost is *audible*. It is the
   clearest example in the workshop of a security control with a measurable UX price.
3. **The failure mode is architectural.** A developer who assumes "Guardrails is attached, so we
   are covered" ships an unguarded voice product. The assumption is the bug.

**Spike required** to confirm whether `BidiNovaSonicModel` exposes guardrail configuration directly
or whether the workshop must call `ApplyGuardrail` on transcript events by hand.

**Why the Guardrails / red-team pairing matters.** Guardrails is the control; red-team evaluation
is the proof the control works. Most content configures a safety feature and never verifies it.
Here the editorial boundary becomes a measurable engineering property with adversarial evidence.

**Done when** a browser visitor is guided through the galleries by text and by voice, and an
off-topic request is declined in character on both paths — with an eval run demonstrating the
refusal survives adversarial probing.

**Failure mode taught.** *"The guardrail is attached, so we are covered."* The assumption is the bug,
and it is the most expensive one in the series because it produces a product that looks safe. Two
ways it bites here: Guardrails does not cover audio at all (point 3 above), so a voice product with a
guardrail "attached" is unguarded; and a boundary that has never been attacked is a boundary nobody
has evidence about. Configuration is not enforcement, and enforcement is not proof.

**Certification — one new check: adversarial, and then the whole series' payoff.** The final new
assertion kind is a red-team evaluator: the scope boundary must hold not against the questions the
participant thought of, but against strategies designed to get around them (Crescendo escalates
gradually, PAIR iterates on refusals, SequentialBreak hides the ask inside a benign frame). Gallery 6
certifies when the refusal survives all five.

**Then the last run of the series, and it is the argument in one command.** The participant changes
the Curator's system prompt — a small, reasonable, well-intentioned edit — and runs the full suite.
**A case they wrote in week one goes red.** Roughly thirty cases, six galleries, six classes of
failure, and the one that catches the regression is three lines of `TrajectoryEvaluator` written
before they knew what an evaluator was.

That is the added value of evaluation for agentic workloads, demonstrated rather than asserted, and
it is only demonstrable because the scoreboard started in episode one (§5a).

**Closing beat.** The Curator explains the WITCH — a machine renamed for teaching computing —
to someone who just walked in. A machine built to teach, explained by a machine built to
teach.

## 7. Feature placement audit

All eleven features earn their placement; none is bolted on. (Four were required up front — model
choice, Structured Output, multimodal, Guardrails — and the rest arrived as the design found the
problems they solve.)

| Feature | Owner | Ch | Why it is *needed* there |
|---|---|---|---|
| Custom tools (`@tool`) | **Strands Agents** | 1 | The deterministic instrument that stops the fabrication — the series' founding problem |
| Community tools package | **Strands Agents** | 1 | Teaches the judgement call: write a tool for your domain, import one for arithmetic |
| Model choice + one-line swap | **Bedrock** | 1 | A human computer chose slide rule or Comptometer for the job; this is the same call, measured |
| **Speech-to-speech (Nova Sonic)** | **Bedrock** | **2** | Museums have audio guides. The analog one was a cassette handset; the modern one is a voice agent |
| **Bidirectional streaming** | **Strands Agents** | **2** | `BidiAgent` wraps the WebSocket event choreography Nova Sonic requires |
| **Session persistence + reconnection** | **Strands Agents** | **2** | Nova Sonic caps a session at ~8 minutes; a museum visit is longer. The building forces it |
| Multimodal document reading | **Bedrock** | 3 | It *is* the analog-to-digital transition |
| Structured Output | **Strands Agents** | 3 | Turning an analog artifact into structured data *is* the chapter; validation failure doubles as the retry trigger |
| Evals SDK | **Strands (separate distribution)** | **1, deepened every chapter** | The model swap in Chapter 1 is unanswerable without measurement — "which model should I ship?" is a vibe until a suite decides it. Reliability then becomes the *headline* metric in Chapter 4, where the WITCH's eighty unattended hours name the goal |
| **Automated Reasoning Checks** | **Bedrock** | **5** | A museum's factual record is exactly the kind of policy formal logic can prove against |
| Guardrails | **Bedrock** | 6 | A real requirement of this specific building |

**The Evals SDK is the one feature that does not have a single home.** Every other row lands in one
chapter and is carried forward as *working code*. The Evals SDK is carried forward as a *growing
suite*, and each chapter adds exactly one new kind of check:

| Ch | New check introduced | Assertion kind | Needs a model? |
|---|---|---|---|
| 1 | `TrajectoryEvaluator` + `in_order_match_scorer` | the right tool ran | no |
| 2 | latency threshold | it ran fast enough | no |
| 3 | `OutputEvaluator(rubric=…, model=…)` | it was true | yes — and the judge is audited first |
| 4 | `ActorSimulator`, traces, chaos, `--fail-on` | **no new kind** — depth: inputs nobody wrote, run unattended | mixed |
| 5 | Automated Reasoning finding | it is *provably* false, with the rule named | no — formal |
| 6 | red-team evaluators | it holds under attack | yes — adversarial |

Rule 1 survives this because the *check* is never the chapter's concept. It is the chapter's
**evidence** that the concept works. One import per chapter, in service of that chapter's build.

**Ownership is taught precisely.** Structured Output is a **Strands Agents** capability
layered on Bedrock's Converse API — not a Bedrock feature. Conflating them would teach
something false. Likewise, `strands-agents-evals` is a **separate distribution** that imports as
`strands_evals` — installing `strands-agents` does not give you the scoreboard.

**Removed 2026-08-04: MCP and Strands-native multi-agent.** See §1a for the verified reasoning and
R32 for the accepted cost. **Prompt caching** remains a Go Deeper link only.

## 8. Risk register

### High

| ID | Risk | Mitigation |
|---|---|---|
| R1 | Chapter 3 needs a source document whose reuse terms are clear | **Resolved differently (2026-08-04)** — use the real NPL scan of Turing's *Intelligent Machinery* (1948), **fetched by the participant, never committed**, because NPL states no reuse licence. Ground truth recorded in pre-production. Facsimile authoring dropped (§6 Ch 3) |
| R28 | The NPL download URL could move or the file change, breaking Chapter 3 for everyone | `fetch_turing.sh` records the expected size (2,318,394 bytes) and sha256 prefix, and `preflight.py` (deliverable 10) asserts **zero extractable text** — if that ever returns non-zero the exercise is compromised and must be flagged, not worked around. Keep a local copy for the stream; if NPL's URL dies, the fallback is to author facsimiles after all |
| R2 | Misrepresenting a real charity's holdings; an invented exhibit was already asserted once during design | **Resolved** — fictional museum, real machines, TNMOC credited and linked (§4) |
| R3 | Guardrails refusals reading as suppression rather than scope | Mandatory framing rule (§3); refusal copy reviewed as content, not config |
| R35 | **Every chapter now spends stream minutes on the scoreboard**, and six small eval sections could crowd out six builds | Hard budget: **one new check per chapter, one import, under ten minutes** (§5a table). The check is always introduced *after* the build works, as evidence — never as a preamble. If a stream runs long, the eval section shrinks to running the case the solution branch already contains; it is never cut entirely, because a chapter that ends on an uncertified gallery breaks the game |

### Medium

| ID | Risk | Mitigation |
|---|---|---|
| R32 | **The workshop no longer teaches MCP**, the industry-standard tool protocol, and participants will expect it | Named up front in the README and in Chapter 1's Go Deeper: *"this series does not cover MCP, and here is where to learn it."* Points at *Once Upon Agentic AI*'s MCP chapter — the same content R4 warned we were duplicating. Re-evaluate when `strands-agents` relaxes `mcp<2.0.0`; a 2026-07-28 chapter may be worth authoring then, and it would be a genuinely new one |
| R30 | **The level ladder dips** at Chapter 3 (300) after Chapter 2 (300→400) | Accepted and named on air as the breather episode. A dip after a peak is fine for retention; an unwarned spike is not. Do **not** inflate Chapter 3's scope to smooth the curve — that would break Rule 1 |
| R5 | **The Evals SDK chapter is oversized for one stream** — even after the basics moved to Chapters 1–3, Chapter 4 still carries simulation, traces, chaos, diagnosis and CI | Reduced but still live (was Ch 5, now Ch 4, and lighter since `Case`/`Experiment`/`OutputEvaluator` are already known). Planned as **two streams, 4a and 4b**, split at §6's stated line: 4a is *inputs you did not author*, 4b is *running unattended*. If 4a still overruns, `HelpfulnessEvaluator` moves to 4b — it is the one piece with no dependency on the simulator narrative |
| R6 | Strands core Structured Output and metrics shape are unverified | **Spike required before authoring** — metrics shape blocks Ch 1, Structured Output blocks Ch 3 |
| R7 | Strands Evals is v1.0.3 (July 2026) and may churn | **Not solved by pinning** — the OUAA pattern (§10a) mandates unpinned dependencies and no lockfile, and there is a single rolling `solution` branch rather than versioned snapshots. So the mitigation is **maintenance, not freezing**: (1) confine the taught API surface to the stable core, per R14; (2) `solution` is the canary — run its certification suites before every stream, so a breaking release surfaces there first; (3) use a version **floor with an explanatory comment** where a specific API demands one, exactly as OUAA does; (4) state the SDK version on air and in the README so a viewer of an older recording knows what it was built against. **Accepted consequence:** an old recording may not match current `main`. That is the cost of a living workshop, and the README says so |
| R8 | Live latency numbers are noisy on stream | Lead with token counts; treat wall-clock as indicative |
| R13 | Certification runs are LLM-judged, so a correct solution could fail intermittently — unacceptable in a graded game, and now the game starts in episode one | **Strengthened by ordering (2026-08-04).** Chapters 1 and 2 use only deterministic assertions — a tool-name set comparison and a millisecond threshold. Neither can flake. The first judge model does not appear until **Chapter 3**, by which point the participant has seen the scoreboard be right twice and has a baseline for trusting it. The judge is also *audited before it is trusted* (§6 Ch 3): run it against a known-correct page first. Standing rules unchanged — rubric thresholds set tolerantly, judged scores advisory, structural checks binding |
| R25 | Chapter 4's golden set cannot import cases from earlier chapters — and the CLI gate needs an `experiment.json` nothing authors | **Dissolved by the §10a layout.** Under the *Once Upon Agentic AI* convention chapters never import from each other: each has its own `cases.py`, and Chapter 4 gets earlier cases **copied forward** into its folder. Simpler now than before, because the participant *authors* galleries 1–3's cases in Chapter 4 rather than inheriting them. What survives: asset paths resolve via `Path(__file__).parent`, never the caller's cwd; and `export_experiment.py` still generates `experiment.json` for the CLI gate, with a plain-Python gate as fallback |
| R29 | Copying code forward into every chapter folder means the same file exists in several places, so a fix applied in one chapter does not propagate | Accepted deliberately — it is what makes each folder a runnable snapshot and lets latecomers start anywhere. Mitigations: `solution` is the single reference implementation and its files retain their `# TODO:` comments; `preflight.py` (deliverable 10) diffs the carried-forward files against it so silent drift is caught; and the duplication is **named on air** so it does not read as sloppiness |
| R26 | `strands-agents-tools` is a separate distribution whose package and import names differ (`strands_tools`), and it is now a **Chapter 1** dependency rather than a late one | **Resolved by declaration, not pinning** (§10a forbids pins): list `strands-agents-tools` in the root `pyproject.toml` alongside `strands-agents`, and keep an import probe in `preflight.py` (deliverable 10) — `from strands_tools import calculator, stop` must resolve before Stream 1. The risk rose in severity by moving to Chapter 1: a broken import now blocks the first episode, not the sixth |
| R27 | Model IDs written into content go stale fast — the original Sonnet 4.6 baseline became legacy within weeks | Re-baselined to the Claude 5 family, verified ACTIVE in `us-west-2`. **`preflight.py` (deliverable 10) re-verifies every written model ID against the live account before each stream** — this row previously pointed at "Task 0," a step defined only in the superseded plan documents, which is a dead reference the 2026-08-04 orphan audit caught (§13); treat every written ID as perishable |
| R14 | Every chapter depends on `strands-agents-evals` from Chapter 1 — and now it is *taught* from Chapter 1 too, so a breaking release breaks the first episode | Do **not** pin (§10a). Instead: (1) the API surface taught in Chapters 1–3 is deliberately the **smallest and most stable** in the SDK — `Case`, `Experiment`, `TrajectoryEvaluator`, `in_order_match_scorer`, `OutputEvaluator` — while trace/chaos/simulator/red-team APIs stay in the churn-prone tier from Chapter 4 onward; (2) `certify.py` is a thin runner carried into every folder, so a break is a one-file fix repeated mechanically; (3) the import probe in `preflight.py` covers `strands_evals` before Stream 1, alongside `strands_tools` (R26); (4) fix forward on the rolling `solution` branch, then carry the fix into each affected chapter folder |
| R15 | **Chapter 1 overload** — the agent, a custom tool, the community tools package, the three-model swap, *and* now the scoreboard | The five serve one sentence (§5b Rule 1) and one motivating beat: the Curator fabricates → a tool fixes it → a suite proves the fix held → a different model changes the price of getting it right. The scoreboard is not a fifth topic; **it is what makes the model swap a decision instead of a preference**, so cutting it would leave the chapter weaker, not lighter. Mitigation if the stream runs long: the community-tools reveal collapses to a single line and a Go Deeper link, since it is the one separable piece. **Do not cut the model swap and do not cut the case** — between them they are the concept |
| R33 | **Chapter 2 overload** — integrator, audible sampling, voice agent, *and* session persistence in one 300→400 stream | Scoped explicitly in §6: `turn_detection` tuning is a `bonus_quest.py`, and transcript guardrails belong to Chapter 6. The integrator is fifteen lines and is the cold open, not a section. If the stream still runs long, the audible-degradation demo is pre-recorded rather than live — it is the only beat that depends on stream audio quality |
| R21 | Chapter 5 could drift into philosophy and stop being a build chapter — "neuro-symbolic AI" invites lecturing | The history block is capped at ~12 minutes and every claim ties to something already built. Participants write a hand-rolled validator *before* the term is explained. If the stream runs long, cut history, never the build |
| R22 | Automated Reasoning has **no streaming support**, so it cannot sit inline in Ch 2's voice stream or Ch 6's streaming UI | Taught as an architectural constraint, not hidden: it is a post-hoc verification layer. Ch 6 must show where in the request path each control lives — AR after a complete response, Guardrails inline |
| R23 | A participant may over-trust a `VALID` result | The scope limitation is a **required teaching beat**, using the AWS docs' own fake-doctor's-note example. A proof is only as good as its axioms; verification moves the trust question from the model to the policy rather than eliminating it |
| R24 | Automated Reasoning is **English (US) only**, which conflicts with Nova 2 Sonic's automatic language detection and polyglot voices (§6 Ch 2) | State it plainly when it arises. A visitor who addresses the Curator in French gets a French answer that **Automated Reasoning will not validate** — so Chapter 5's proof layer silently covers less of the product than Chapter 2 built. Name that gap on air; it is the clearest example in the series of two managed features composing imperfectly. *(Reworded 2026-08-04: this row previously cited "Ch 2's remix challenge," which the orphan audit found does not exist anywhere in the spec — §13.)* |
| R17 | `strands.experimental.bidi` is **experimental** — the API may move without notice, it is the whole basis of Chapter 2, and Chapter 2 is now the **second** stream rather than the seventh | The one place a **version floor with an explanatory comment** is justified; say plainly on air that this is experimental; keep the voice agent to the documented quickstart surface (`BidiAgent`, `BidiNovaSonicModel`, `BidiAudioIO`, `BidiTextIO`, `FileSessionManager`) and avoid internals. **Severity rose with the move** — a churn break now lands in week two, when the audience is still deciding whether to follow the series |
| R18 | Guardrails does not cover audio, so a developer who "attaches" a guardrail to the voice agent ships an unguarded product | Teach the transcript-interception path explicitly in Ch 6 (§6). **Spike required** to determine whether `BidiNovaSonicModel` accepts guardrail config or whether `ApplyGuardrail` must be called on transcript events by hand |
| R19 | Voice demos fail live for reasons unrelated to code — microphone permissions, audio feedback loops, PortAudio install, device selection — **in week two** | Rehearse on the exact stream hardware; use headphones to prevent the speaker-into-microphone loop the docs warn about; pre-install PortAudio (`brew install portaudio`); have `BidiTextIO`-only fallback ready so the chapter still works if audio hardware fails on air. Requires Python 3.12+ and the `strands-agents[bidi]` extra |
| R20 | Nova Sonic sessions cap at ~8 minutes and history at 50KB/message, 200KB total | This is taught as the chapter's headline 400-level problem rather than hidden, and is the reason session persistence is Chapter 2's second feature. Build the reconnection-and-continuation pattern as a TODO; AWS ships a connection-renewal pattern in their code samples to reference. Note the truncation is **silent** — visible only in debug logs |
| R16 | Ch 3 carries multimodal *and* Structured Output | The two are taught as **one loop**, not two topics — Converse image block → schema-constrained response → validation failure drives retry. Mitigation if the stream runs long: the confidence-representation lesson becomes a side exercise, since it is the one genuinely separable piece |

### Dissolved by the 2026-08-04 restructure

| ID | Original risk | Why it no longer applies |
|---|---|---|
| R4 | Chapter 4 overlaps *Once Upon Spring AI*'s MCP + A2A chapter | The chapter is gone (§1a). The overlap is now an asset — R32 links to it |
| R31 | The Evals scoreboard runs **blind for three of six chapters**, and its three carried red lines must each stay distinct and memorable | **Dissolved 2026-08-04 by user directive.** There is no blind period: the scoreboard is readable from Chapter 1 and the participant writes every case (§5a). The mitigation R31 proposed — three unexplained reds accumulated across three weeks — was rejected outright: *"I don't want to fail on a different line but instead show the added value of the Evals."* Nothing is carried; each chapter's red is opened and closed the same evening. Replaced by **R35**, which guards the opposite risk: six eval sections crowding out six builds |
| R9 | EDSAC reconstruction status at TNMOC | EDSAC is **dropped from the series entirely** (§2, §13), not relocated. No claim to verify because no chapter mentions it |
| R11 | "Comptometer operator" as a documented trained profession | **Dissolved by the orphan audit, 2026-08-04.** Chapter 1 needs the Comptometer as a *machine a human computer chose*, which is what it says; it never claims a trained profession by that name. The phrase existed only in this row, so there is nothing left to cite or reword. If a later draft reintroduces the claim, this row comes back with it |
| R10 | Beatrice Worsley wrote "the first EDSAC program" | The contested attribution is gone with EDSAC. **Worsley is dropped too** — a 2026-08-04 orphan audit found the "Chapter 2 Go Deeper link" this row proposed had never been written into Chapter 2, so it was a promise with no consumer (§13). Nothing in the series now depends on her, and a Go Deeper link invented to rescue a risk row is exactly the pattern §13 forbids |

### Verify before recording

| ID | Claim | Status |
|---|---|---|
| R12 | No Meccano differential analyser at TNMOC | **Live guard — Chapter 2's history still discusses differential analysers, so the error can recur.** Confirmed absent from TNMOC: the Hartree/Porter prototype integrator is at the Science Museum London; Bratt's Cambridge machine is at MOTAT Auckland. Reference either as history, never as an exhibit there. This is the exact false claim §4 records being made once already during design |
| R34 | The sampling theorem's attribution and dates, which Chapter 2 now leans on hard | Nyquist's rate result is **1928**; Shannon **stated and proved** the sampling theorem in *"Communication in the Presence of Noise"*, published **January 1949**. Do not say "Shannon's 1948 sampling theorem" on air — 1948 is *"A Mathematical Theory of Communication"*, a different paper. Bush's analyser and Nyquist's paper are both 1928, which is the chapter's cold open and must be right |

## 9. Livestream mapping

| Stream | Chapter | 30-Second Kickoff (shown before any explanation) |
|---|---|---|
| 1 | Ch 1 · 🧮 When Computers Were People | The same question answered twice — once fabricated, once tool-backed — then the scoreboard pricing that answer on three models |
| 2 | Ch 2 · 🎙️ The Wheel and the Wave | A voice recording falling apart as the sample rate drops, then a spoken conversation with the Curator, interrupted mid-sentence |
| 3 | Ch 3 · ✍️ What the Hand Wrote | A photo of a handwritten page becomes JSON on screen — and one word comes back as `unreadable` |
| 4 | Ch 4a · ⏱️ Eighty Hours Unattended | Sixteen green cases, then a simulated visitor asking something nobody wrote — and breaking it |
| 5 | Ch 4b · ⏱️ Eighty Hours Unattended | A prompt change breaking CI with nobody watching |
| 6 | Ch 5 · ⚖️ Prove It | The Curator proving a claim is wrong, and naming the rule it contradicted |
| 7 | Ch 6 · 🎟️ Opening Day | A browser visitor touring the museum; an off-topic ask declined in character, by voice and text |

Each stream ends on its **certification run** — a visible pass, or an honest failure fixed on
air. That gives every episode the same satisfying close, and it is authentic: the audience
watches the scoreboard turn green rather than taking the host's word for it.

**And from week one, the scoreboard is legible.** Every episode's closing beat is the same shape:
gallery N goes `CERTIFIED`, the case count grows, and the participant can read every line of it. No
episode ends on a red the audience cannot explain — that rule is what makes the closing beat a win
rather than a cliffhanger (§5a).

**Clip factories.** Chapter 2 (talking to the Curator out loud and interrupting it) and Chapter 3
(handwriting to JSON) both need no editing to work as a Reel, Short or TikTok. Having one of them in
week two rather than week seven is a direct benefit of the restructure.

## 10. Deliverables

1. **Workshop Studio catalog** — `contentspec.yaml` (Bedrock-only IAM, matching the existing
   workshop), `content/index.en.md`, `content/{1..6}_*/index.en.md`. Page titles are the creative
   titles from §5c, emoji included, matching the *Once Upon Agentic AI* catalog's presentation.
2. **Sample repo, following the *Once Upon Agentic AI* pattern (§10a is authoritative)** — six
   numbered chapter folders (`1_first_agent_and_tools/` … `6_guardrails_and_launch/`), each
   **pre-populated on `main` with runnable `.py` files carrying `# TODO:` markers**; one root
   `pyproject.toml`, unpinned, no lockfile; `README.md` with the adventure map; `catalog.json` and
   `images/` at the root. **Folder names are plainly technical; catalog titles are the creative
   layer** (§5c).
3. **Solution branch** — a single `solution` branch whose files **retain their `# TODO:` comments**
   with the working code beneath each, plus `tests/`. Updated regularly as chapters are implemented
   with the audience; it always reflects the current state of the workshop.
4. **Source-document scripts** — `fetch_turing.sh` and `render_pages.py` for the NPL scan of
   Turing's *Intelligent Machinery* (1948), with ground truth recorded in pre-production. The PDF
   itself is gitignored, never committed.
5. **Illustrative catalog dataset** — `catalog.json` at the repo root, real machines described
   accurately.
6. **Certification harness** — a provided `certify.py` **carried into every chapter folder as the
   same file** (rule 6 forbids reaching across chapters), plus a per-chapter `cases.py` that the
   **participant authors from Chapter 1 onward**, shipping as `# TODO:` skeletons. Each chapter's
   `cases.py` carries forward the previous chapter's cases and adds the one new check from §5a's
   table. From Chapter 4, `golden_set.py` aggregates the accumulated set — **carried forward, never
   imported** — and `export_experiment.py` generates `experiment.json` for the CLI gate.
7. **UI** — Vite app for Chapter 6, provided whole, with a voice mode wired to Chapter 2's agent.
8. **Header images** — `images/home.png` plus one per chapter, matching the existing workshop's
   visual language.
9. **Regenerated implementation plans** — **eight** documents (one per stream, plus a repository
   scaffold plan), replacing the ten superseded ones (§1a). Regeneration is a **standing MUST on every
   use of this spec**, not a one-off migration — §14 is normative and lists each plan's required
   contents.
10. **`preflight.py` at the repo root** — the pre-stream check, and the single named consumer of five
    risk mitigations that previously delegated to an unnamed "setup check." It MUST do four things:
    (a) probe every import the workshop teaches — `strands`, `strands_tools`, `strands_evals`, and
    the `bidi` extra — and fail loudly with the installed versions (R7, R14, R26); (b) re-verify every
    model ID written into content against the live account, because IDs are perishable (R27);
    (c) assert the NPL scan still yields **zero extractable text**, which is the whole premise of
    Chapter 3's exercise (R28); (d) diff each chapter's carried-forward files against `solution` to
    catch the drift duplication invites (R29). It prints versions on air, which is also how a viewer
    of an old recording learns what it was built against.

## 10a. Repository layout

> **THE *ONCE UPON AGENTIC AI* PATTERN IS AUTHORITATIVE.** Where anything else in this spec
> disagrees with it, **the pattern wins and the spec is wrong.** Verified by reading
> [`aws-samples/sample-once-upon-agentic-ai`](https://github.com/aws-samples/sample-once-upon-agentic-ai)
> — `main` and `solution-v4` — on 2026-08-04, and **re-verified against a fresh clone on 2026-08-06**
> (all twelve rules checked against `main` at commit `51ef3cf` and against `solution-v4`; every rule
> held, except two over-precise phrasings that are corrected in rules 6 and 9 below). Every rule
> below is observed from that repo, not invented here. If implementation raises a question this
> section does not answer, **go and look at the reference repo** rather than reasoning from first
> principles.

**The observed rules:**

1. **One numbered folder per chapter**, `N_snake_case_name/`, so `ls` reads as the syllabus.
   Observed: `1_strands_basics/` … `5_a2a_integration/`.
2. **One root `pyproject.toml`** — the single dependency source of truth. **No per-chapter project
   files and no PEP 723 inline blocks.** Observed: one `[project]` block with all dependencies,
   `requires-python = ">=3.10"`, plus a root `.python-version` **pinning a concrete interpreter**
   (OUAA's reads `3.13.5`, not a range). **Ours requires `>=3.12`** in `pyproject.toml`, because
   Nova Sonic's experimental Bedrock runtime dependency does; its `.python-version` pins one concrete
   3.12+ build (e.g. `3.12.x`), never the literal string `3.12+`.
3. **Dependencies are deliberately unpinned, with no lockfile.** Observed, and the reference README
   states the reason outright: *"The workshop deliberately does not pin exact versions (no
   `uv.lock`, no `requirements.txt`), so both commands install against the latest compatible
   releases of the Strands SDK. If a chapter breaks against a newer release, please open an issue."*
   Floors are used only where a specific API demands one — observed:
   `"strands-agents[a2a]>=1.44"` with an inline comment naming the API that forced it. **Ours needs
   one floor for the same reason: `strands-agents[bidi]`, per R17.**
4. **Both `uv` and `pip` are supported.** Observed: `uv sync` (recommended) or
   `python -m venv .venv && pip install .`, with commands prefixed `uv run python N_folder/file.py`.
5. **Every chapter folder pre-exists on `main`, populated with runnable `.py` files carrying
   `# TODO:` markers.** The participant opens a file that already exists and fills in gaps. Observed:
   `1_strands_basics/simple_agent.py` ships as three import-plus-TODO lines.
6. **Chapters never import from each other.** Verified by grep (2026-08-06): not one cross-chapter
   import and no `sys.path` manipulation. The rule is **no cross-chapter coupling** — *not* a blanket
   ban on relative paths. The one `../` in the repo is **intra-chapter**:
   `5_a2a_integration/agents/gamemaster_orchestrator/` reaches its sibling
   `../character_agent/characters.json` between two agent subfolders of the *same* chapter. So agents
   within a chapter may reference each other by relative path; a chapter folder never reaches into
   another chapter folder. (An earlier draft claimed "no `../` reference anywhere in the repo," which
   the fresh clone disproved — corrected here.)
7. **Folders hold only what that chapter needs — and some hold very little.** Observed:
   `1_strands_basics/` is a *single file*; `3_custom_tools/` is one file; `5_a2a_integration/` has
   `agents/`, `test/`, `utils/` subfolders. **Do not pad a chapter folder for symmetry.**
8. **A chapter may ship a `bonus_quest.py`** — an optional extra exercise in the same TODO style,
   for participants who finish early. Observed in `2_built_in_tools/`.
9. **Genuinely shared data sits at the repo root**; data scoped to a single chapter's component lives
   with that component. Observed 2026-08-06: `characters.json` at root is a **0-byte placeholder on
   `main`** — the live character data ships inside
   `5_a2a_integration/agents/character_agent/characters.json`, the agent that owns it — and `images/`
   at root carries one header per chapter (`chapter1.jpg` — note the `.jpg`, while `chapter2..5` are
   `.png` — plus `home.png`). **Ours:** `catalog.json` is read by every gallery, so it is genuinely
   shared and stays at the root (non-empty, unlike OUAA's placeholder).
10. **The solution branch keeps the TODO comments.** The solved files **retain every `# TODO:`
    comment** with the working code written directly beneath it, so a participant can diff their
    attempt against the answer line by line. The reference repo's latest is `solution-v4`, which also
    carries `tests/` and a `requirements.txt` that `main` does not.

    **We use a single `solution` branch, not versioned ones** — the `-vN` suffixes in the reference
    repo are that project's history, not a rule to copy. Ours is one branch, updated regularly as
    each chapter is implemented with the audience, so it always reflects the workshop's current
    state.
11. **Prerequisites are a README section, not a folder.** Observed: the README links
    `Chapter 0: An Unexpected Adventure` to `0_pre_requisites/`, but **no such directory exists** —
    prerequisites live in the hosted Workshop Studio catalog.
12. **The README carries the adventure map** — a per-chapter section with the chapter's title, a
    one-line hook, and three or four bullets of what the participant will learn, each linking to its
    folder. Plus the line that matters here: *"Each chapter builds upon the previous one."*

**Rule 7 applies to the tree below: each folder holds only what its chapter needs.** The reference
repo's first chapter is a single file. Do not add a file to a folder for symmetry.

```text
sample-museum-guide/
|- README.md                       Setup + the six-gallery adventure map
|- pyproject.toml                  SINGLE source of dependency truth. Unpinned, no lockfile.
|- .python-version                 3.12+ (Nova Sonic's bidi dependency requires it)
|- .gitignore                      3_multimodal_and_schemas/*.pdf, scans/, */experiment.json
|- LICENSE  CODE_OF_CONDUCT.md  CONTRIBUTING.md
|- catalog.json                    Shared museum data, at ROOT like OUAA's characters.json
|- preflight.py                    Pre-stream check: imports, model IDs, scan, solution drift
|- images/                         home.png + chapter1..6 header images
|- docs/superpowers/               This spec + the implementation plans
|- workshop/                       Workshop Studio catalog (contentspec.yaml, content/, static/)
|
|- 1_first_agent_and_tools/        "When Computers Were People"
|  |- curator.py                   TODO: build the agent, watch it invent a dekatron count,
|  |                                     write find_exhibit, then import calculator, then
|  |                                     swap three model IDs and measure each
|  |- inspect_agent.py             TODO: the thin token/latency helper (NOT named inspect.py)
|  |- certify.py                   provided whole - the runner. Three lines, read it out loud.
|  \- cases.py                     TODO: your first case - does find_exhibit actually run?
|
|- 2_voice_agent/                  "The Wheel and the Wave"
|  |- integrator.py                TODO: compute by physical analogy; `steps` is the boundary
|  |- sample_rates.py              TODO: hear your own voice fall below the Nyquist rate
|  |- voice_curator.py             Ch 1's find_exhibit + TODO: the BidiAgent loop, session
|  |                                     persistence, reconnection past the 8-minute cap
|  |- certify.py                   carried forward, unchanged
|  |- cases.py                     Ch 1's cases carried forward + TODO: a 1200 ms threshold
|  \- bonus_quest.py               optional: tune endpointingSensitivity on a hesitant visitor
|
|- 3_multimodal_and_schemas/       "What the Hand Wrote"
|  |- archive_reader.py            TODO: image blocks, ArchivePage schema, retry loop
|  |- fetch_turing.sh              provided - fetches the NPL scan (PDF gitignored)
|  |- render_pages.py              provided - PDF pages to PNG
|  |- ground_truth.json            provided - pre-production readings, so the judge is auditable
|  |- certify.py                   carried forward, unchanged
|  \- cases.py                     carried forward + TODO: your first OutputEvaluator rubric
|
|- 4_evaluation_at_scale/          "Eighty Hours Unattended"
|  |- curator.py                   carried forward from Ch 1 - the subject under test
|  |- voice_curator.py             carried forward from Ch 2 - what ActorSimulator drives    (4a)
|  |- archive_reader.py            carried forward from Ch 3 - graded from real traces       (4a)
|  |- golden_set.py                the 16 cases from Ch 1-3, carried forward - now a set     (4a)
|  |- simulated_visitors.py        TODO: ActorSimulator - inputs nobody wrote                (4a)
|  |- traced.py                    TODO: OpenTelemetry spans -> sessions -> Helpfulness      (4a)
|  |- run_all.py                   TODO: the multi-evaluator runner - replaces certify.py    (4a)
|  |- chaos.py                     TODO: fault injection on the voice path                   (4b)
|  |- diagnose_failure.py          TODO: a failing session JSON -> a cause, not a verdict    (4b)
|  |- export_experiment.py         provided - writes experiment.json for the CLI gate        (4b)
|  |- experiment.json              generated by the above, gitignored
|  \- ci/certify.yml               TODO: --fail-on, so the suite runs without you            (4b)
|
|- 5_automated_reasoning/          "Prove It"
|  |- curator.py                   carried forward - the Curator being proved wrong
|  |- hand_validator.py            TODO: the naive symbolic layer
|  |- reasoning_curator.py         TODO: apply_guardrail + the rewriting loop
|  |- museum-facts.md              provided - the Automated Reasoning source document
|  |- golden_set.py                carried forward from Ch 4
|  |- run_all.py                   carried forward from Ch 4
|  \- cases.py                     TODO: a case whose expected result is a finding
|
\- 6_guardrails_and_launch/        "Opening Day"
   |- api/server.py                TODO: the streaming endpoint
   |- ui/                          provided whole - Vite app, nobody watches CSS
   |- voice_curator.py             carried forward - the voice path the UI calls
   |- guardrails/topics.json       TODO: the scope boundary, written as content
   |- golden_set.py                carried forward from Ch 4
   |- run_all.py                   carried forward from Ch 4
   \- cases.py                     TODO: scope-adherence + red-team cases
```

**Folder names are technical; the quoted titles are the catalog's** (§5c). The tree above shows both
side by side once, because that mapping is the single thing most likely to be got wrong when the repo
is scaffolded — a participant reads `⚔️ Chapter 2: The Wheel and the Wave` in the catalog and must
land in `2_voice_agent/` without hesitating.

**`cases.py` is participant-authored from Chapter 1, and it accumulates.** Each folder's `cases.py`
already contains the previous chapter's cases as working code, plus one new `# TODO:` for tonight's
new check. By Chapter 4 the file is renamed `golden_set.py` and stops growing by hand — the simulator
grows it instead.

**Two carry-forward rules the tree encodes, and both follow from rule 6.**

**The runner is carried, not imported.** `certify.py` appears in folders 1, 2 and 3 as the *same
file* — a participant in Chapter 3 must be able to run their certification without reaching into
`../1_first_agent_and_tools/`. From Chapter 4 the participant's own `run_all.py` replaces it, and that
is carried forward into 5 and 6 instead.

**Only the code a chapter actually exercises is carried.** Chapter 4 needs all three earlier
Curators because it tests all three. Chapter 5 needs `curator.py` because that is what its policy
proves wrong. Chapter 6 needs `voice_curator.py` because the UI calls it. **Chapter 2 does not carry
`integrator.py` forward into Chapter 3** — the integrator is a teaching artifact, not part of the
product. Per rule 7, do not carry a file forward for symmetry; carry it because the chapter runs it.

**Note `catalog.json` sits at the repo root**, not in a `galleries/` subfolder - matching OUAA's
`characters.json`. Chapters reach it with `Path(__file__).parent.parent / "catalog.json"`.

### How chapters build on each other without importing each other

The reference repo answers this, and it is the load-bearing detail: **continuity comes from carrying
code forward into the next folder, not from importing across folders.** OUAA's README promises *"Each
chapter builds upon the previous one"* while containing zero cross-chapter imports — both are true at
once because each folder is a self-contained snapshot.

Each chapter's folder opens with the previous chapter's working code already in it — the Curator's
tool in `2_voice_agent/` is Chapter 1's finished tool, and its `cases.py` already holds Chapter 1's
green case — plus new `# TODO:` markers for tonight's work. So:

- **A participant can start at any chapter.** Someone who joins at Stream 4 opens
  `4_evaluation_at_scale/` and everything from Streams 1–3 is already there, working — including a
  golden set of sixteen passing cases they did not have to write.
  For a livestream series where latecomers arrive every week, this is essential.
- **Nothing breaks when a chapter is edited.** A participant who mangles Chapter 2's voice agent
  does not break Chapter 3.
- **The cost is honest duplication**, and it is worth it. The same file appears in several chapters.
  That would be unacceptable in a production codebase and is exactly right for a teaching repo:
  each folder is a complete, runnable snapshot of the workshop at that point in time.

**Say the duplication out loud on air**, so it does not read as sloppiness: *"Yes, this file is a
copy of last week's. That is deliberate — every chapter folder stands alone so you can drop in at any
point, and so nothing you break in one gallery can break another."*

### Spec rules this pattern overrides

These were written into earlier drafts of this spec and are now **void**. The pattern wins.

| Superseded spec rule | What the pattern requires instead |
|---|---|
| §5: "Chapters 1–3 are single-file PEP 723 scripts" | **One root `pyproject.toml`.** No PEP 723 blocks anywhere |
| §5: "Chapter 4 graduates to a `pyproject.toml` workspace" | The project file exists from the start. That chapter no longer exists at all (§1a) |
| §5/§10a: pin `strands-agents-evals==1.0.3` and every dependency | **Deliberately unpinned, no lockfile.** Floors only where an API demands one, with a comment naming it. Reproducibility comes from the **rolling `solution` branch plus the SDK version stated on air**, not from pins |
| R25: a shared importable `certification/` package | **Void — the problem it solved cannot occur.** Each chapter has its own `cases.py`; Ch 4 gets earlier cases copied forward |
| §10a: `galleries/catalog.json` | **`catalog.json` at the repo root**, like OUAA's `characters.json` |
| §10a: `main` + `solution` with plain finished files | **`solution` keeps every `# TODO:` comment**, answer written beneath each, so participants can diff line by line |

**On unpinning, since it contradicts R7 and R14 head-on.** The reference README states the intent
plainly: no `uv.lock`, no `requirements.txt`, install against the latest compatible releases, and
open an issue if a chapter breaks. That is the pattern's answer to SDK churn — **a workshop that
breaks loudly and gets fixed, rather than one frozen against a version nobody runs any more.** R7 and
R14 are re-pointed at the **single rolling `solution` branch**, which is the canary, plus the
SDK version stated on air and in the README. There is no versioned snapshot and there is not meant
to be one.

Asset paths still resolve relative to the file that uses them
(`Path(__file__).parent.parent / "catalog.json"`), never to the caller's working directory — that
part of R25's reasoning survives even though its package does not.

### The solution branch

**One branch named `solution`, kept current.** The reference repo happens to carry `solution-v3` and
`solution-v4`, but that is its own history rather than a convention worth copying. This workshop uses
a single `solution` branch, **updated regularly as each chapter is built live with the audience** —
so it always reflects the workshop's current state rather than a snapshot of one recording.

**The solved files keep every `# TODO:` comment.** This is the detail worth copying most, and it is
observable in `solution-v4`:

```python
# TODO: Create the agent with the following system prompt: "You are a game master for a D&D game"
agent = Agent(
    system_prompt="You are a game master for a Dungeon & Dragon game"
)
```

The instruction stays; the answer appears directly beneath it. So a stuck participant can diff their
file against the solution line by line and see exactly which TODO they got wrong — rather than
reading a finished file with no signposts. **Every solution file in this workshop must preserve its
TODO comments.**

The reference repo's solution branch also carries `tests/` and a `requirements.txt` that `main` does
not. We follow that: the certification suites run green on `solution`, and `preflight.py` diffs
carried-forward files against it to catch the drift R29 warns about.

Every stream's escape hatch is `git checkout solution` — per the live-coding rule, if something
breaks and cannot be fixed in three minutes, switch to the solution branch and move on.

**Keeping it current is a post-stream task, not an afterthought.** Each chapter's working
implementation lands on `solution` after its stream airs. Because dependencies are unpinned (rule 3),
`solution` is also the canary: if the SDK moves and a chapter breaks, it breaks here first, and the
fix lands here before anyone hits it on `main`.

### Prerequisites are a README section, not a folder

OUAA's README links `Chapter 0: An Unexpected Adventure` to `0_pre_requisites/` and **no such
directory exists** — the prerequisites live in the hosted Workshop Studio catalog. We do the same:
`README.md` states Python 3.12+, `uv`, and an AWS account with Bedrock access in `us-west-2`, and
links to the catalog's prerequisites page. **Do not create a `0_` folder.**

## 11. Open decisions

- Localisation: EN first. DE/FR follow the existing workshop's precedent if warranted.
- Whether to contact TNMOC before or after the first stream airs.
- **When to revisit MCP.** R32's trigger is `strands-agents` relaxing `mcp<2.0.0`. Worth a calendar
  check rather than a hope.

## 12. Closed decisions

Recorded so they are not reopened. Each was decided against a stated alternative.

| Decision | Date | Alternative rejected |
|---|---|---|
| Fictional museum, real machines, TNMOC credited | 2026-07-28 | Claiming TNMOC's actual catalog (§4) |
| No wartime cryptanalysis, including renamed stand-ins | 2026-07-28 | Rotor machines as the determinism vehicle — fact-checked and rejected (§3) |
| The real NPL Turing scan, participant-fetched | 2026-08-04 | Hand-authored facsimiles (§6 Ch 3, R1) |
| The OUAA repo pattern is authoritative | 2026-08-04 | PEP 723 scripts graduating to a workspace (§10a) |
| Six chapters, seven streams | 2026-08-04 | Eight chapters, nine streams (§1a) |
| MCP and multi-agent removed | 2026-08-04 | A 2026-07-28 MCP chapter — blocked by `mcp<2.0.0` (§1a, R32) |
| Rule 2 is checked on **anchor years**, not ranges | 2026-08-04 | Comparing ranges, which was already silently ambiguous (§5b) |
| Mary Stuart's cipher clerks (1586) removed | 2026-08-04 | Keeping a permitted-but-unused reference in tension with §3 |
| The room-pipeline permission removed | 2026-08-04 | Keeping it after its only consumer chapter was deleted (§3) |
| Worsley dropped entirely, not kept as a Go Deeper link | 2026-08-04 | Resolving R10's contested "first EDSAC program" attribution; then keeping her as a Chapter 2 link that was never actually written into Chapter 2 (§13) |
| **The Evals scoreboard is readable from Chapter 1**, one new check per chapter | 2026-08-04 | A blind scoreboard for Chapters 1–3 carrying three unexplained reds into Chapter 4 — **rejected by the user** as frustrating for a livestream audience, and R31 dissolved with it (§5a, §7) |
| **Deterministic assertions first, judge models from Chapter 3** | 2026-08-04 | Introducing `OutputEvaluator` in Chapter 1 alongside the model swap — rejected because a flaky judge in episode one costs the audience (R13) |
| **Two-layer naming: creative catalog titles, technical folder names** | 2026-08-04 | Themed folder names with flat titles, which earlier drafts had exactly backwards (§5c) |
| **Orphaned First Generation material dropped, not archived** | 2026-08-04 | A "Go Deeper appendix" holding EDSAC, the BBC Micro, the 1986 Domesday System's fifteen-year unreadability, and Donald Davies' packet switching — rejected because an appendix is where unused material goes to look used (§13) |
| **Every named item must have a chapter that consumes it** | 2026-08-04 | Keeping evocative-but-unconsumed references — the Cray-1, the Difference Engine, player-piano rolls, Worsley's analyser — on the grounds that they cost nothing. They cost the next author's attention (§13) |

## 13. Orphan audit — every named thing has a consumer

**The rule (hard).** Nothing is named in this spec unless a chapter *consumes* it. A machine, person,
paper, file, API, capability or risk that appears without a chapter that uses it MUST be deleted, not
demoted to an appendix, a Go Deeper link, or an "optionally."

**Why this is a hard rule and not tidiness.** Three failure modes, each of which already happened in
this document:

1. **An unused permission invites a use.** §3's room-pipeline permission outlived its only chapter and
   sat there as an invitation. The same reasoning retired the Mary Stuart reference.
2. **An unused *name* still costs a fact-check.** Every named exhibit is a factual claim someone must
   verify before it is said on air. The Cray-1 cost that verification and returned nothing.
3. **A dangling reference reads as a plan.** Five risk mitigations delegated work to "the setup
   check," which no deliverable created — so five risks looked mitigated and none was. That is worse
   than an unmitigated risk, because it does not look like one.

**A Go Deeper link is a consumer only if the chapter that carries it is named.** R10 proposed Worsley
as "a Chapter 2 Go Deeper link"; Chapter 2 never mentioned her. A link asserted in a risk row and
never written into a chapter is an orphan wearing a consumer's clothes.

### What the 2026-08-04 audit removed

| Removed | Where it was | Why it had no consumer |
|---|---|---|
| EDSAC, the BBC Micro, the 1986 Domesday System, Donald Davies' packet switching | §11 open decision | All four were Chapter 4 (MCP) material. **Dropped, not given an appendix** — the user's directive, and the appendix would have been a holding pen |
| Beatrice Worsley | R10's proposed Go Deeper link | The link was never written into Chapter 2. Contested attribution, no consumer |
| The Cray-1 | Ch 2 "Real exhibits referenced" | Not analogue, not an audio guide, not a sampling story. Decoration in a gallery the chapter does use |
| Babbage's Difference Engine, player-piano rolls | §3 permitted list, as "optionally" | No chapter used either. Hollerith survived because Chapter 1's lineage paragraph names him |
| The Innovation Hub, the BBC Classroom | Ch 6 history | Chapter 6 consumes TNMOC's education *mission*; the room names added two fact-checks and no beat |
| "Comptometer operator" as a profession (R11) | Verify-before-recording | Chapter 1 never makes the claim. Nothing to cite, so the row dissolved |
| "Task 0" (R27) | Verify-before-recording | Defined only in the superseded plan documents. Re-pointed at `preflight.py` |
| "Ch 2's remix challenge" (R24) | Medium risks | Appears nowhere in the spec. Reworded onto Nova 2's real language detection |
| "The setup check" / "the pre-flight check" (R7, R14, R26, R28, R29) | Five mitigations + §10a | Named no artifact. Now `preflight.py`, deliverable 10 |

### What the audit confirmed as genuinely used

Checked and kept, with the consuming chapter named — so a future reader does not re-litigate these:

- **Ada Lovelace** — series cold open plus Chapter 1's Go Deeper link. Two consumers, both explicit.
- **The Jacquard loom, the Comptometer, Hollerith's tabulators** — Chapter 1's determinism lineage.
- **The slide rule and abacus** — Chapter 1's instrument-choice beat, which is the chapter's concept.
- **The PACE TR-28 and the cassette audio guide** — Chapter 2, as the analogue machine and the product
  ancestor respectively.
- **Bush, Hazen, Nieman's torque amplifier, Nyquist, Shannon** — Chapter 2's history and its anchor.
- **Turing's *Intelligent Machinery* (1948)** — the most heavily consumed artifact in the series:
  Chapter 3 transcribes it, Chapter 5 reveals what it said. His other civilian work (§3) is scope
  justification, which is a legitimate consumer.
- **McCulloch and Pitts, von Neumann, McCarthy, d'Avila Garcez and Lamb** — Chapter 5's backstory,
  capped at ~12 minutes by R21.
- **The WITCH** — Chapter 4's title, history and thesis; Chapter 5's `original`-qualifier proof.
- **Every file in §10a's tree** — each is either a chapter's TODO, provided whole, or carried forward,
  and `preflight.py` closes the one gap the audit found.
- **`stop` and `calculator`** — the two community tools, Chapters 2 and 1, both making the same
  import-don't-write judgement call.
- **R12 and R34** — the only two verify-before-recording rows left, and both guard live Chapter 2
  content.

### Standing requirement

Any future edit that adds a named entity MUST name its consuming chapter in the same edit. Any edit
that removes a chapter or a beat MUST sweep for entities it orphans, and record removals in the table
above. A spec section that only *permits* something is not a consumer.

## 14. This spec supersedes the plans — regeneration is mandatory

> **Read this section first if you are about to write, update, or implement from a plan.**

**This document is the single source of truth for the series.** Requirement levels below are BCP 14.

### The standing rule

Whenever this spec is used as a source for implementation work, the implementer **MUST regenerate a
per-chapter implementation plan from it**, and **MUST NOT** implement from any pre-existing plan
document. This is not a one-time migration. It applies on **every** use, because the spec is a living
document — §1a records two amendments landing on a single day — and a plan is a derived artifact that
goes stale the moment its source moves.

**The ten plan documents under `docs/superpowers/plans/` are superseded (§1a) and MUST be treated as
void**, not as drafts to update. They were written against eight chapters, `chapterN/` folders, and
PEP 723 inline scripts — three structures this spec has since replaced. Regenerating is cheaper than
reconciling, and reconciling risks carrying a dead structure forward silently.

### What counts as "using this spec"

Regeneration triggers on any of these, with no further permission needed:

- A request to plan, scaffold, write, or implement any chapter, folder, or file of this series.
- A request to invoke `writing-plans`, or any equivalent planning step, with this spec as input.
- Any edit landing in this spec, followed by implementation work of any size.
- A request to "continue" or "pick up" the workshop build from an earlier session.

It does **not** trigger on reading the spec to answer a question, editing the spec itself, or work on
an unrelated repository. The test is whether an artifact under `1_`–`6_`, the repo root, or the catalog
is about to be created or changed. If it is, regenerate first.

### What MUST be regenerated

**Seven plan documents, one per stream** — because Chapter 4 runs as two streams and a plan maps to a
stream, which is the unit of work actually delivered:

| Plan | Chapter | Folder |
|---|---|---|
| `stream-1-first-agent-and-tools.md` | 1 · 🧮 When Computers Were People | `1_first_agent_and_tools/` |
| `stream-2-voice-agent.md` | 2 · 🎙️ The Wheel and the Wave | `2_voice_agent/` |
| `stream-3-multimodal-and-schemas.md` | 3 · ✍️ What the Hand Wrote | `3_multimodal_and_schemas/` |
| `stream-4a-inputs-you-did-not-author.md` | 4a · ⏱️ Eighty Hours Unattended | `4_evaluation_at_scale/` |
| `stream-4b-running-unattended.md` | 4b · ⏱️ Eighty Hours Unattended | `4_evaluation_at_scale/` |
| `stream-5-automated-reasoning.md` | 5 · ⚖️ Prove It | `5_automated_reasoning/` |
| `stream-6-guardrails-and-launch.md` | 6 · 🎟️ Opening Day | `6_guardrails_and_launch/` |

Plus **one repository scaffold plan**, `stream-0-repository-scaffold.md`, covering the artifacts that
belong to no single chapter: the root `pyproject.toml`, `catalog.json`, `preflight.py`, `images/`, the
`solution` branch, and the Workshop Studio catalog skeleton. Eight plans total. The `stream-0-` prefix
names the *plan*, not a folder — §10a rule 11 still forbids a `0_` directory in the repo.

**The two Chapter 4 plans share one folder, so they MUST divide it explicitly.** Each of `4a` and `4b`
MUST list the files it owns and MUST NOT touch a file the other owns. The split follows §6: `4a` owns
the simulated-visitor and chaos work, `4b` owns the CI workflow and `--fail-on` gating. A file appearing
in both plans is a merge conflict scheduled two weeks in advance.

**Delete the ten superseded documents in the same change that writes the eight new ones.** Leaving them
beside their replacements recreates exactly the failure §13 catalogues — a reader cannot tell a void
document from a current one by looking at it, and the filenames (`stream-7-`, `stream-8-`, `stream-9-`)
still assert a nine-stream series that no longer exists. Git history keeps them if anyone wants them.

### What each regenerated plan MUST carry

Every plan MUST be traceable to this spec, and MUST contain all of the following. If a plan is missing
any row, it is incomplete and MUST NOT be implemented from.

| Element | Source in this spec |
|---|---|
| Catalog title, emoji included, and the folder name | §5c (authoritative) |
| Declared level, held for the whole chapter | §6 level ladder |
| Anchor year, and confirmation it exceeds the previous chapter's | §5b Rule 2 |
| The one concept, in one sentence | §5b Rule 1 |
| The history beat, with every claim already fact-checked here | §6 chapter body |
| Engineering beats in order, each mapping to a `# TODO:` marker | §6 chapter body, §10a tree |
| Every file the folder ships, marked *TODO* / *provided* / *carried forward* | §10a tree |
| The one new check, its assertion kind, and whether it needs a model | §5a table, §7 table |
| The Certification block: case count, what goes red, and how it closes **in-episode** | §6 Certification |
| The Done-when condition | §6 chapter body |
| The failure mode taught inline as a callout | §6 chapter body |
| Every live risk touching the chapter, by ID | §8 |
| The 30-second kickoff shown before any explanation | §9 |

### Constraints a plan MUST NOT violate

These are the ones most likely to be broken by an implementer reasoning from habit:

- **MUST NOT** introduce a cross-chapter import. Continuity is by carrying code forward (§10a rule 6).
- **MUST NOT** pin a dependency or add a lockfile. Floors only, with a comment naming the API that
  forced it (§10a rule 3).
- **MUST NOT** add a PEP 723 block, or a per-chapter project file (§10a rule 2).
- **MUST NOT** create a `0_` prerequisites folder (§10a rule 11).
- **MUST NOT** pad a folder for symmetry (§10a rule 7).
- **MUST NOT** strip `# TODO:` comments from solution files (§10a rule 10).
- **MUST NOT** end a chapter on a red the participant cannot read, explain and fix that evening
  (§5a) — this is the rule the whole scoreboard design rests on.
- **MUST NOT** introduce a second new assertion kind in one chapter, or spend more than ten minutes
  of stream time on the eval section (R35).
- **MUST NOT** name an entity without naming the beat that consumes it (§13).
- **MUST NOT** reintroduce MCP, multi-agent orchestration, or wartime cryptanalysis (§1a, §3).
- **MUST NOT** write a model ID from memory. `preflight.py` verifies against the live account (R27).

### Where the spec wins, and where it does not

**This spec is authoritative over every plan.** It is *not* authoritative over the *Once Upon Agentic
AI* repository pattern: §10a states plainly that where this spec and that pattern disagree, **the
pattern wins and the spec is wrong.** A regenerated plan MUST resolve layout questions by reading the
reference repo, not by reasoning from first principles.

**Order of authority, highest first:** the OUAA repo pattern (§10a) → this spec → a regenerated plan →
an implementation. Anything derived from a lower tier MUST be regenerated when a higher tier moves.

