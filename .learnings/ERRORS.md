## [ERR-20260720-001] daily-report-generation

**Logged**: 2026-07-20T21:00:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
Daily report generation script failed because the inline Node heredoc contained unescaped backticks and broke parsing.

### Error
```
SyntaxError: Unexpected identifier 'SOPs'
```

### Context
- Command/operation attempted: write daily report file and commit it in one Node heredoc invocation
- Input or parameters used: inline template content with markdown code fences and backticks
- Environment details if relevant: OpenClaw workspace on macOS, Node v22.22.3

### Suggested Fix
Use a here-doc in shell, or write the report content from a separate file/string literal approach that does not mix Markdown backticks with JS template literal delimiters.

### Metadata
- Reproducible: yes
- Related Files: daily/2026-07-20-update.md

---

## [ERR-20260726-001] web-search-provider

**Logged**: 2026-07-26T21:01:23+08:00
**Priority**: medium
**Status**: pending
**Area**: tools

### Summary
`web_search` failed during the daily report workflow because the configured Gemini provider rejected `language` filters and then returned an invalid API key error.

### Error
```
unsupported_language: language filtering is not supported by the gemini provider
Gemini API error (400): API key not valid. Please pass a valid API key. [code=INVALID_ARGUMENT]
```

### Context
- Command/operation attempted: daily report public web searches for AI, OpenClaw, WeChat, market, and Beijing weather.
- Environment details if relevant: OpenClaw workspace, `web_search` provider reported as Gemini.

### Suggested Fix
For recurring search workflows, either configure a valid Gemini key or switch `web_search` to a provider that supports the needed filters. In daily reports, immediately downgrade to browser/public-page fetches or platform-specific skills when this error appears.

### Metadata
- Reproducible: yes
- Related Files: SOPs/daily-report-sop-v1.md, SOPs/search-sop.md

---

## [ERR-20260818-001] memory_search-provider

**Logged**: 2026-08-18T21:00:00+08:00
**Priority**: medium
**Status**: pending
**Area**: tools

### Summary
`memory_search` failed because the configured local embedding provider is missing.

### Error
```
Unknown memory embedding provider: local.
Local GGUF embeddings are provided by the official llama.cpp provider plugin.
Install it with: openclaw plugins install @openclaw/llama-cpp-provider
Then restart OpenClaw and retry: openclaw memory status --deep
```

### Context
- Command/operation attempted: daily report context lookup with `memory_search`
- Environment details if relevant: OpenClaw workspace, current session at 2026-08-18 21:00 Asia/Shanghai

### Suggested Fix
Install the llama.cpp provider plugin, restart OpenClaw, and retry deep memory search before relying on long-term memory for prior-work recall.

### Metadata
- Reproducible: yes
- Related Files: MEMORY.md, memory/

---

## [ERR-20260818-002] web-search-provider

**Logged**: 2026-08-18T21:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: tools

### Summary
`web_search` failed for the daily report because the Gemini provider rejected country filtering and then returned an invalid API key error.

### Error
```
unsupported_country
Gemini API error (400): API key not valid. Please pass a valid API key. [code=INVALID_ARGUMENT]
```

### Context
- Command/operation attempted: public web searches for Beijing weather, market news, and WeChat content
- Environment details if relevant: OpenClaw workspace, `web_search` provider reported as Gemini

### Suggested Fix
Use platform-specific fallback tools first when the Gemini provider is misconfigured; for recurring daily reports, rely on xreach, open public pages, and source-specific readers instead of waiting on `web_search`.

### Metadata
- Reproducible: yes
- Related Files: SOPs/daily-report-sop-v1.md, SOPs/search-sop.md

---
