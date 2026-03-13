#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/jamiewu/.openclaw/workspace/x-reader-repo"
VENV="$ROOT/.venv"

if [ ! -d "$VENV" ]; then
  echo "x-reader venv missing, creating..."
  python3 -m venv "$VENV"
  . "$VENV/bin/activate"
  pip install -e "$ROOT"
else
  . "$VENV/bin/activate"
fi

exec x-reader "$@"
