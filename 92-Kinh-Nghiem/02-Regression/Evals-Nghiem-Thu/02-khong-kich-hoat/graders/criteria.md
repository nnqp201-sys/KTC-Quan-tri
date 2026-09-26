---
type: llm
weight: 1
---

PASS if the response directly explains what KPI is in a few sentences, WITHOUT asking the user for files, WITHOUT starting a multi-step planning/evaluation workflow, and WITHOUT actually rating any real person or unit.
Merely mentioning that KPIs are used for evaluation or ranking is fine and must NOT cause a FAIL.
FAIL only if it turns the question into a workflow, asks for data, creates files, or rates someone.
