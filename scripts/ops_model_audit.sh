#!/usr/bin/env bash
set -euo pipefail

TS="$(date '+%Y-%m-%d %H:%M:%S %Z')"
TMP="$(mktemp)"

cleanup() {
  rm -f "$TMP"
}
trap cleanup EXIT

echo "[ops-model-audit] started at $TS"

if ! openclaw status >"$TMP" 2>&1; then
  echo "ALERT: openclaw status 执行失败"
  cat "$TMP"
  exit 2
fi

STATUS_TEXT="$(cat "$TMP")"

# 抽取 Sessions 表格，便于查看当前会话模型
SESSIONS_BLOCK="$(awk '
  /^Sessions$/ {in_block=1; next}
  /^FAQ:/ {in_block=0}
  in_block {print}
' "$TMP")"

if [[ -n "$SESSIONS_BLOCK" ]]; then
  echo "\n[Sessions 模型概览]"
  echo "$SESSIONS_BLOCK"
else
  echo "\nWARN: 未提取到 Sessions 表格"
fi

# 基础异常检测（尽量避免误报）
ALERTS=()

if echo "$STATUS_TEXT" | grep -Eiq 'Gateway .*unreachable'; then
  ALERTS+=("Gateway 不可达")
fi

if echo "$STATUS_TEXT" | grep -Eiq 'OpenClaw status.*failed|status command failed'; then
  ALERTS+=("status 输出疑似失败")
fi

if [[ ${#ALERTS[@]} -gt 0 ]]; then
  echo "\nALERT: ${ALERTS[*]}"
  exit 1
fi

echo "\nOK: 网关可达，未发现明显异常。"
exit 0
