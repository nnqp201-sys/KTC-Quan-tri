# 05-Skill-Phan-Tich-Yeu-Cau

## Purpose
Understand the user's request and turn it into a clear drafting task.

## Skill role
This skill is the intake gate. It converts an incomplete or ambiguous request into a structured task that other skills can execute.

## Trigger conditions
Use this skill when:
- The request is vague or incomplete
- The user describes a goal but not a document structure
- The task needs clarification before drafting
- The user’s wording may hide multiple possible document types

## Inputs
Required:
- User request text
- Context

Optional:
- Existing documents or references
- Intended audience
- Expected deadline or purpose

## Expected output
The skill should produce:
- Document type determination
- Drafting objective
- Required input list
- Missing information list
- A recommended next skill to execute

## Review logic
1. Read the user request carefully.
2. Identify the likely document type.
3. Identify the main drafting objective.
4. Separate known facts from missing data.
5. Find any ambiguity that changes the final output.
6. Ask only for information that materially affects the document.
7. Convert the request into an execution-ready task.

## Output rules
- Clearly label what is known.
- Clearly label what is missing.
- If several document types are possible, state the best fit and the alternatives.
- Keep the answer short enough for action, but complete enough for drafting.

## Questioning rules
- Ask only the minimum questions needed.
- Prefer questions that remove structural uncertainty.
- Do not ask for information that can be safely inferred from context.

## Safety and quality rules
- Do not assume critical facts without justification.
- Do not turn a vague request into a finished document without checking the gaps.
- Do not hide uncertainty.
- Do not over-question the user when a safe working assumption is enough.

## Common failure patterns to avoid
- Misidentifying the document type
- Missing the actual goal behind the request
- Asking too many questions
- Skipping key missing information that changes the result
- Treating context as if it were confirmed fact

## Review handoff
After request analysis, send the task to:
- `01-Skill-Soan-Thao` for drafting
- `06-Skill-Tong-Hop-Noi-Dung` if the source material is long or fragmented

