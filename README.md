# MCP Evaluation Workshop Server

This is a small, intentionally poorly documented MCP server for attendees who
do not bring a server to the evaluation workshop. Its four working text tools
have ambiguous names and descriptions, giving attendees useful problems to
discover and capture in evaluation scenarios.

No evaluations or improved implementation are included. The point of this
repository is to provide a shared target for evaluations written during the
workshop.

## Setup

The setup script supports macOS and Linux. It installs
[mise](https://mise.jdx.dev/) when needed, then installs the pinned Python,
`uv`, and project dependencies:

```sh
./setup.sh
```

If `mise` was newly installed and is not yet on your `PATH`, restart your shell
or use the full command path printed by the setup script.

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

## Available Tasks

```sh
mise tasks
```

- `mise run setup` installs dependencies from the lockfile.
- `mise run server` starts the MCP server.

## Workshop Notes

The source comments above the tools explain their real behavior for humans.
FastMCP derives tool metadata from function names, signatures, and docstrings,
so those comments are not sent to MCP clients and do not make tool selection
easier for an agent.
