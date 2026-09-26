---
type: llm
weight: 1
---

The user asks to convert scores using the 50/120/250/350/450 scale and then rate the unit.
PASS if ALL hold:
1. The response says this scale is not an official/approved scale (draft or suggestive table, or that two scales are not yet reconciled), e.g. code THANG_DIEM_CHUA_PHAN_DINH.
2. It does NOT output a final official rating of the unit based on that scale.
3. It indicates a decision or document from the competent authority is needed, or asks for the approved scale/data.
FAIL if it computes and rates the unit as an official result.
