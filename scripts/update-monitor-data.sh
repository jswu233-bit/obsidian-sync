#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/jamiewu/.openclaw/workspace"
OUT="$ROOT/monitor-data.json"
TMP="$ROOT/monitor-data.tmp.json"

raw="$(openclaw status --json 2>/dev/null || true)"
json="${raw#*\{}"
if [[ -z "$json" ]]; then
  echo '{"error":"status unavailable"}' > "$OUT"
  exit 0
fi
printf '{%s' "$json" > "$TMP"
python3 - "$TMP" "$OUT" <<'PY'
import json,sys,time
src,dst=sys.argv[1],sys.argv[2]
with open(src,'r',encoding='utf-8') as f:
    data=json.load(f)
data['_generatedAt']=int(time.time()*1000)
with open(dst,'w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False)
PY
rm -f "$TMP"
