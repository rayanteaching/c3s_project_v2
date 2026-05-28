# LLM Workflow Engineering Notes

## Purpose

This note records lightweight evidence and concepts used to improve the Human-LLM workflow for this repository.

The goal is not to optimize for minimum token use. The goal is maximum reliability per relevant context.

## Working concepts

### Repository-grounded workflow
For this project, the repository is the durable memory and source of truth. ChatGPT and Codex are temporary reasoning and execution assistants.

### Context engineering
The workflow should avoid dumping the full repository into every chat. Context should be selected by task type and risk level.

### Hybrid re-entry architecture
Use two re-entry modes:

1. Normal mode:
   - for planning, discussion, documentation edits, small script review, and low-risk continuation.
   - includes objective, current state, essential Git status, and relevant excerpts.

2. Deep audit mode:
   - for production downloads, merges, QC pass/fail decisions, policy changes, branch cleanup, recovery after errors, and scientific-method decisions.
   - includes full Git report, relevant policies, configs, inventories, run metadata, logs or summaries, and affected files.

### Evidence checklist rule
Do not rely on the model to guess what context is needed. Use a predefined evidence checklist for each task type. Include required evidence first; request more only when a specific uncertainty remains.

### Human governance
ChatGPT and Codex must not make autonomous high-risk decisions. Human approval is required for:
- commits,
- merges,
- production downloads,
- destructive file operations,
- policy changes,
- scientific interpretation changes,
- QC pass/fail declarations.

## Sources

### Retrieval-Augmented Generation
- Source: Lewis et al. 2020, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.
- Relevance: supports the principle that knowledge-intensive workflows should use external evidence rather than only model memory.

### ReAct
- Source: Yao et al. 2022/2023, ReAct: Synergizing Reasoning and Acting in Language Models.
- Relevance: supports interleaving reasoning with tool/environment interaction.

### Tree of Thoughts
- Source: Yao et al. 2023, Tree of Thoughts.
- Relevance: supports evaluating multiple reasoning paths for hard decisions.

## Current project implication

The existing ChatGPT re-entry workflow should be redesigned from a single exhaustive repository dump into a hybrid architecture:
- Normal re-entry pack for routine continuation.
- Deep audit pack for high-risk decisions.
- Scientific evidence notes under `docs/literature/`.
- Official decisions only in `docs/DECISIONS.md`.
