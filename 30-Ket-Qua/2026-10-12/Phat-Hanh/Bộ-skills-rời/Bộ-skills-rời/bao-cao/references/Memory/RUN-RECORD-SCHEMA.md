# KTC-RIS Run Record Schema v1.0

```yaml
run_id: RIS-YYYYMMDD-HHMM-<period>
started_at:
completed_at:
report_period:
report_type:
skill_runs: []
sources: []
operations: []
decisions: []
exceptions: []
outputs: []
qa: []
learning_candidates: []
status: in_progress|completed|blocked|superseded
supersedes_run_id:
notes:
```

Quy tắc: ưu tiên Drive File ID/URI; không dùng Run Record thay văn bản nguồn; không xóa lịch sử quyết định, dùng `superseded`; Run Record là bằng chứng quá trình, không phải căn cứ pháp lý.
