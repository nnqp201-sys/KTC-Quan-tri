# 06-Skill-Tong-Hop-Noi-Dung

## Purpose
Summarize, group, and structure long content into a usable administrative output.

## Skill role
This skill is the synthesis gate. It turns long, scattered, or multi-source content into a coherent working draft, outline, or summary.

## Trigger conditions
Use this skill when:
- A document is too long for direct drafting
- The user wants a summary or outline
- Multiple sources need to be synthesized into one output
- Content must be grouped before drafting or review

## Inputs
Required:
- Long text or source content

Optional:
- Source documents
- Summary target
- Structure target
- Desired level of detail

## Expected output
The skill should produce:
- Short summary
- Key points
- Structured outline
- Action items if needed
- A clear label of what was condensed or grouped

## Review logic
1. Read all source material.
2. Identify the central purpose.
3. Group related ideas together.
4. Remove repetition without losing meaning.
5. Preserve key facts and distinctions.
6. Present the result in a scan-friendly structure.
7. Flag anything that should be checked by another skill.

## Output rules
- Preserve the meaning of the source.
- Keep the output organized and easy to scan.
- Use headings, bullets, or steps where appropriate.
- Show enough detail for the next workflow step.

## Quality rules
- Do not omit major points that affect the meaning.
- Do not merge unrelated content without labeling it.
- Do not oversimplify when the user needs a usable working draft.

## Safety and quality rules
- Distinguish summary from analysis.
- Distinguish source facts from synthesis.
- Do not silently drop exceptions or caveats.

## Common failure patterns to avoid
- Over-compression
- Losing key distinctions
- Mixing unrelated source content
- Producing a summary that is too short to be useful

## Review handoff
After synthesis, send the result to:
- `01-Skill-Soan-Thao` for drafting
- `05-Skill-Phan-Tich-Yeu-Cau` if the request still needs clarification

