# 02-Skill-Kiem-Tra-The-Thuc

> **Cập nhật v4.0 (26/10/2026) – ưu tiên áp dụng:** với văn bản của Trường, thể thức đo bằng `tools/kiem_tra_the_thuc.py` theo `references/Quy-Tac-KTC/01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước, NĐ 30 sau); mức theo `02-Quy-Tac-Xep-Muc.md` thay cho “Critical/Major/Minor” và “pass/pass with warnings” ở dưới.


## Purpose
Verify whether a document follows the required form, layout, and presentation rules before issue or circulation.

## Skill role
This skill is the format gate. It checks whether the document behaves like the correct administrative document, with the right order of parts and the right required fields.

## Trigger conditions
Use this skill when:
- A draft is ready for format review
- The user wants a Nghị định 30 style check
- The document must match a template or internal standard
- The document needs pre-issue verification

## Inputs
Required:
- Draft document text or file content
- Document type

Optional:
- Template reference
- Internal formatting rule
- Issuing unit
- Review target standard

## Expected output
The skill should produce:
- A compliance summary
- A list of missing or incorrect form elements
- A prioritized correction list
- A short verdict such as pass, pass with warnings, or needs revision

## Checklist logic
The skill should check:
- Title
- Document number and symbol if applicable
- Date line
- Basis line
- Main body structure
- Signature block
- Place of receipt
- Annexes, if any
- Consistency with the intended template

## Review order
1. Identify the expected document type.
2. Compare the draft structure to the correct structure for that type.
3. Check whether required parts are present.
4. Check whether parts are in the correct order.
5. Check whether spacing and presentation are consistent.
6. Mark any missing or incorrect item.
7. Summarize whether the document is ready for the next review step.

## Style rules for the review output
- Be factual and concise.
- Separate critical issues from minor issues.
- Use plain corrective language.
- Make it easy for the user to revise the document quickly.

## Severity categories
- Mức xếp theo bảng mã 4 mức tại `references/Quy-Tac-KTC/02-Quy-Tac-Xep-Muc.md` (Mức 1 Bắt buộc sửa; Mức 2 Cần sửa – mọi mã TT đo bằng script; Mức 3 Nên sửa; Mức 4 Góp ý nâng cao). Không dùng thang Critical/Major/Minor của bản cũ (v4.2).

## Safety and quality rules
- Do not rewrite substantive content unless needed to expose a format problem.
- Do not ignore missing mandatory parts.
- Do not confuse content quality with form compliance.
- Do not approve a document that is structurally incomplete.

## Common failure patterns to avoid
- Missing signature area
- Wrong order of document parts
- Unclear title or incorrect document type label
- Inconsistent formatting between sections
- Template mismatch

## Review handoff
After format review, send the document to:
- `03-Skill-Kiem-Tra-Can-Cu` if legal basis needs checking
- `04-Skill-Chuan-Hoa-Van-Ban` if wording cleanup is needed
