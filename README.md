# Personal Researcher

A small local-first research assistant that searches your saved Markdown sources and returns passages with source citations.

## First lesson: define the agent

- **Goal:** answer a research question using only the documents in `sources/`.
- **Model:** added in a later lesson; it will decide which search to run and synthesize the evidence.
- **Tool:** local Markdown search, returning relevant passages and filenames.
- **Orchestration:** the loop that gives the model the question, runs requested tools, and returns observations.
- **Deployment:** for now, a local command-line program.

## Try the search tool

From this directory, run:

```sh
python3 researcher.py "What makes an agent different from a workflow?"
```

Add `.md` files under `sources/`. Search results include file names and line numbers so answers can be traced to their source.
