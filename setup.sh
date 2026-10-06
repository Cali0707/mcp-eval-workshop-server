#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if command -v mise >/dev/null 2>&1; then
    MISE=$(command -v mise)
elif [ -x "$HOME/.local/bin/mise" ]; then
    MISE="$HOME/.local/bin/mise"
else
    if ! command -v curl >/dev/null 2>&1; then
        printf '%s\n' "curl is required to install mise." >&2
        exit 1
    fi

    curl -fsSL https://mise.run | sh
    MISE="$HOME/.local/bin/mise"
fi

cd "$ROOT"
"$MISE" trust --yes mise.toml
"$MISE" install
"$MISE" run setup

printf '\nSetup complete. Start the server with:\n  %s run server\n' "$MISE"
