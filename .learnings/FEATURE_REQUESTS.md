# FEATURE_REQUESTS.md

## [FEAT-20260512-001] fliggy_cli_hotel_search

**Logged**: 2026-05-12T23:24:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Requested Capability
支持用飞猪 CLI 查询酒店（至少支持按城市/区域/日期/价格筛选并返回候选列表）。

### User Context
用户在旅行决策场景下，希望直接通过飞猪 CLI 获取更贴近中国用户实际预订渠道的酒店结果，而不是只依赖 Google Travel 粗筛。

### Complexity Estimate
medium

### Suggested Implementation
确认是否已有内部/第三方飞猪 CLI；若无，则评估：
1. 是否存在可安装的公开 CLI；
2. 是否需要用 browser automation 包一层飞猪检索 SOP；
3. 是否需要新建一个 travel/fliggy skill 统一封装查询参数与输出格式。

### Metadata
- Frequency: first_time
- Related Features: hotel_search, travel_booking

---
