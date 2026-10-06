# MCP Evaluation Workshop Server

This is a small, intentionally poorly documented MCP server for attendees who
do not bring a server to the evaluation workshop. Its four working text tools
have ambiguous names and descriptions, giving attendees useful problems to
discover and capture in evaluation scenarios.

The repository includes evaluation scaffolding and several agent choices, but
no evaluation tasks or improved server implementation. Attendees write the
tasks during the workshop.

## Setup

The setup script supports macOS and Linux. It installs
[mise](https://mise.jdx.dev/) when needed, then installs the pinned Python,
`uv`, and project dependencies:

```sh
./setup.sh
```

If `mise` was newly installed and is not yet on your `PATH`, restart your shell
or use the full command path printed by the setup script.

## Prepare Evaluations

Install MCPChecker:

```sh
mise run setup-evals
```

Then install only the agent you want to use:

```sh
mise run setup-agent-claude
# or: mise run setup-agent-codex
```

These targets install the ACP wrappers required for Claude Code and Codex.
Gemini and OpenCode provide ACP through their native CLIs, so their agent files
expect `gemini` or `opencode` to already be installed and on `PATH`. Each agent
uses its normal login or API-key configuration; sign in before starting an
evaluation. The built-in provider agents do not need an install target, but do
require the relevant provider credentials.

## Run The Server

```sh
mise run server
```

The streamable HTTP endpoint is:

```text
http://127.0.0.1:8000/mcp
```

Stop the server with `Ctrl-C`.

Pass a port to use something other than `8000`:

```sh
mise run server 9000
```

To listen on another address as well:

```sh
HOST=0.0.0.0 mise run server 9000
```

The seeded `mcp-config.yaml` expects port `8000`. Update its URL if you run the
server on another port.

## Write And Run Evals

Add task YAML files under `tasks/`. The task set in `eval.yaml` discovers YAML
files recursively, so attendees can use either `tasks/example.yaml` or organize
their work into subdirectories.

`eval.yaml` uses `agents/claude-code.yaml` for both the agent and LLM judge by
default. To use another definition, change both file paths in `eval.yaml` to one
of these files:

- `agents/claude-code.yaml`
- `agents/codex.yaml`
- `agents/gemini.yaml`
- `agents/opencode.yaml`
- `agents/builtin-anthropic.yaml`
- `agents/builtin-google.yaml`
- `agents/builtin-openai.yaml`

With the server running in another terminal and at least one task added, run:

```sh
mise run eval
```

## Available Tasks

```sh
mise tasks
```

- `mise run setup` installs dependencies from the lockfile.
- `mise run setup-evals` installs the pinned MCPChecker release.
- `mise run setup-agent-claude` installs the Claude Code ACP wrapper.
- `mise run setup-agent-codex` installs the Codex ACP wrapper.
- `mise run server [port]` starts the MCP server, using port `8000` by default.
- `mise run eval` runs the task files selected by `eval.yaml`.

## Workshop Notes

The source comments above the tools explain their real behavior for humans.
FastMCP derives tool metadata from function names, signatures, and docstrings,
so those comments are not sent to MCP clients and do not make tool selection
easier for an agent.
