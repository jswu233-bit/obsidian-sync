#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/jamiewu/.openclaw/workspace/camofox-browser"
LOG_DIR="/Users/jamiewu/.openclaw/workspace/.openclaw/logs"
LOG_FILE="$LOG_DIR/camofox-9377.log"
PORT="${CAMOFOX_PORT:-9377}"

mkdir -p "$LOG_DIR"
cd "$ROOT"

if lsof -iTCP:"$PORT" -sTCP:LISTEN -t >/dev/null 2>&1; then
  echo "camofox already listening on :$PORT"
  exit 0
fi

nohup env CAMOFOX_PORT="$PORT" node server.js >>"$LOG_FILE" 2>&1 &
sleep 2

if curl -fsS "http://localhost:$PORT/tabs" >/dev/null; then
  echo "camofox started on :$PORT (log: $LOG_FILE)"
else
  echo "camofox failed to start, check log: $LOG_FILE" >&2
  exit 1
fi
