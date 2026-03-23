## [ERR-20260323-001] feishu_bitable_create_record

**Logged**: 2026-03-23T00:15:00+08:00
**Priority**: medium
**Status**: pending
**Area**: config

### Summary
写入飞书索引表失败，日期字段类型不匹配导致创建记录报错。

### Error
```
[bitable.appTableRecord.create] code=1254064 message=DatetimeFieldConvFail
```

### Context
- Operation: feishu_bitable_create_record
- app_token: NTQnbfnthaTIMxsziNzcJaGNnld
- table_id: tblez1cogebbBzwu
- 输入 fields 包含 `写入日期: "2026-03-23"`，疑似目标列为 DateTime 且需要时间戳/完整时间格式。

### Suggested Fix
1. 先读取表字段定义确认 `写入日期` 类型；
2. 按字段要求传毫秒时间戳或 RFC3339 时间字符串；
3. 必要时将该列改为纯文本列以降低写入失败率。

### Metadata
- Reproducible: yes
- Related Files: memory/2026-03-23.md, MEMORY.md

---
