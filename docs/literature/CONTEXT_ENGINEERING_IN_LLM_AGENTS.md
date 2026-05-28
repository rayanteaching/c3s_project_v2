# Context Engineering in LLM-Based Agents

## Source

- Title: Context Engineering in LLM-Based Agents
- Author: Jin Tan Ruan
- Year: 2025
- Type: technical article
- Status: background evidence for repository Human-LLM workflow design

## Relevance to this project

This source supports the repository move from prompt-centric ChatGPT usage to a context-engineered Human-LLM workflow.

The article argues that many agent failures are context failures rather than model failures, and that effective LLM systems require dynamic context assembly rather than dumping all available information into every prompt.

## Key points

- Context engineering is a system design problem, not just prompt writing.
- Useful context includes instructions, user objective, short-term memory, long-term memory, retrieved documents, tool outputs, and output format requirements.
- Too much or irrelevant context can degrade model performance through distraction, confusion, context clash, or context poisoning.
- Four practical context strategies are especially relevant:
  - writing context to durable memory,
  - selecting relevant context,
  - compressing context,
  - isolating context by task or subsystem.
- Retrieval should be relevance-based, not exhaustive.
- Long-term memory must be retrieved carefully; persistent memory should not be injected unless relevant.
- Multi-agent or multi-context workflows can help isolate complexity, but they increase token cost and coordination risk.
- Bigger context windows do not remove the need for context engineering.

## What this supports

This source supports the repository's hybrid ChatGPT re-entry architecture:

- Normal mode for low-risk continuation.
- Deep audit mode for high-risk decisions.
- Evidence checklists by task type.
- Repository files as durable external memory.
- `docs/literature/` as cold scientific and workflow evidence.
- `docs/STATUS.md` and `docs/HANDOFF.md` as hot operational state.
- Avoiding full repository dumps in normal ChatGPT sessions.
- Escalating to deep audit only when risk or uncertainty requires it.

## What this does not support

This source does not prove that any specific C3S, ERA5, NCEP, ECMWF, or verification method is scientifically correct.

It is workflow evidence only. Scientific data-method decisions still require domain-specific sources, official documentation, and repository evidence.

## Project implication

The repository should treat context as a managed resource.

Stored knowledge is not the same as injected context. Most knowledge should remain in the repository until the task type or uncertainty requires retrieval.

## Possible project action

- Keep this note under `docs/literature/`.
- Use it as supporting evidence for the hybrid re-entry protocol.
- Do not add it to normal re-entry packs by default.
- Reference it only when discussing LLM workflow, context engineering, memory, retrieval, or agent design.

## Status

- background
- relevant to LLM workflow architecture
- not an official operational decision by itself
