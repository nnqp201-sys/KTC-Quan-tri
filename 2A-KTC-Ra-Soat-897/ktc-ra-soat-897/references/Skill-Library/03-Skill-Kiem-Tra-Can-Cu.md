# 03-Skill-Kiem-Tra-Can-Cu

## Purpose
Verify whether the legal and internal basis cited in a document is relevant, sufficient, and appropriate for the intended action.

## Skill role
This skill is the basis gate. It prevents weak, irrelevant, or missing citations from reaching approval.

## Trigger conditions
Use this skill when:
- A draft cites laws, decrees, circulars, or internal decisions
- The user asks whether the basis is correct
- The document must follow internal regulations or a special approval route

## Inputs
Required:
- Draft document
- Cited legal or internal references

Optional:
- Topic of the document
- Applicable internal regulation set
- Expected level of authority

## Expected output
The skill should produce:
- Basis validation summary
- Missing basis items
- Weak or unnecessary citations
- Suggested stronger replacements if available

## Review logic
1. Read the document purpose.
2. Identify all cited bases.
3. Check whether each cited basis matches the purpose.
4. Check whether the cited authority is suitable for the institution and context.
5. Check whether any critical basis is missing.
6. Check whether the basis list is too broad or unfocused.
7. Summarize the result in a form usable for revision.

## Basis evaluation rules
- Prefer the most local and relevant internal regulation when it governs the matter.
- Use higher-level legal sources when the matter requires external legal authority.
- Remove references that do not materially support the document.
- Keep the basis list focused and defensible.

## Style rules for the review output
- State clearly what is valid and what needs correction.
- Distinguish missing basis from weak basis.
- Make revision guidance practical, not abstract.

## Safety and quality rules
- Do not confirm an unverified citation as correct.
- Do not recommend unrelated sources.
- Do not leave the user with a basis list that looks complete but is legally weak.

## Common failure patterns to avoid
- Citing a legal source that does not govern the issue
- Missing the internal regulation that should be primary
- Over-citing many bases without need
- Using a basis with too little relationship to the actual decision or action

## Review handoff
After basis review, send the document to:
- `04-Skill-Chuan-Hoa-Van-Ban` if wording needs cleanup
- `02-Skill-Kiem-Tra-The-Thuc` if the document structure also needs a final format check
