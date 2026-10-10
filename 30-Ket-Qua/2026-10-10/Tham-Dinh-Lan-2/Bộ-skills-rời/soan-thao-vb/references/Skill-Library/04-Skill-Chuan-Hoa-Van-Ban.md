# 04-Skill-Chuan-Hoa-Van-Ban

## Purpose
Rewrite or clean up a document so it becomes more consistent, more formal, and easier to approve.

## Skill role
This skill is the language-polish gate. It refines drafts without changing their meaning, making them more suitable for administrative use.

## Trigger conditions
Use this skill when:
- A draft is too informal or inconsistent
- The user wants a polished version
- A document needs language cleanup before approval
- The document already has the right structure but the wording needs improvement

## Inputs
Required:
- Raw draft text
- Style target

Optional:
- Priority corrections
- Tone preference
- Audience or issuing unit

## Expected output
The skill should produce:
- Cleaned and standardized text
- A brief note on main changes made
- A warning list for any content that should be checked by another skill

## Review logic
1. Read the full draft.
2. Identify wording that is informal, repetitive, or unclear.
3. Preserve the original meaning.
4. Improve clarity and consistency.
5. Adjust language to administrative style.
6. Keep the output natural and readable.
7. Flag any content that needs legal or structural review.

## Style rules
- Use formal administrative language.
- Keep sentence structure direct and stable.
- Avoid excessive ornament or literary phrasing.
- Keep terminology consistent across the document.
- Do not make the text sound artificially polished.

## Quality rules
- Preserve meaning exactly unless the user explicitly asks for substantive rewriting.
- Remove repetition where it weakens readability.
- Make transitions clearer.
- Standardize terms, names, and references when appropriate.

## Safety and quality rules
- Do not change policy meaning without instruction.
- Do not rewrite beyond the user’s intent.
- Do not use this skill to fix legal basis or structure problems.
- Do not over-polish so the result becomes unnatural.

## Common failure patterns to avoid
- Overly long sentences
- Inconsistent terminology
- Informal expressions
- Repeated wording that weakens authority
- Smoothing the text so much that meaning shifts

## Review handoff
After wording cleanup, send the document to:
- `03-Skill-Kiem-Tra-Can-Cu` if basis review is still needed
- `02-Skill-Kiem-Tra-The-Thuc` if format needs a final check

