---
name: resume-rewriter
description: Rewrite, polish, tailor, audit, and output resumes/CVs as Word `.docx` documents using source evidence, STAR/XYZ structure, JD matching, ATS keywords, and truthfulness controls. Use when improving a resume, tailoring for a JD, rewriting bullets, quantifying experience, auditing exaggeration, producing a Word resume, editing resume-data.js/JSON/YAML/Markdown/HTML resume content, or working on Michael resume-polisher/recruiting-assistant products. Do not use for inventing a resume from scratch or broad career advice without resume content.
---

# Resume Rewriter

## Default Deliverable

Default to a polished Word `.docx` resume as the final deliverable. Use Markdown only as an intermediate working draft or when the user explicitly asks for plain text.

For rewritten resumes:

1. Draft the clean resume body in Markdown.
2. Save the draft beside the output for traceability.
3. Convert the clean resume Markdown to `.docx` with `scripts/resume_markdown_to_docx.py`.
4. Deliver the `.docx` path first, then mention any supporting Markdown/report files.

For diagnosis-only requests, output a written diagnostic in chat unless the user asks for a file. For rewrite, tailoring, or full resume improvement, create a Word document.

## Core Rule

Rewrite the resume, not reality. Every stronger sentence must trace back to the source resume, a user-provided clarification, or a clearly marked inference that still needs user confirmation.

Never fabricate employers, dates, education, awards, tools, metrics, ownership level, certifications, publications, or project outcomes. If the resume lacks evidence for a JD-critical claim, write "no evidence in the resume" and ask for the missing fact instead of inventing it.

## Workflow Selection

Choose one path from the user's request:

| User request | Workflow |
|---|---|
| "看看哪里要改", "诊断一下", "review my resume" | Diagnosis only |
| "帮我润色/优化/改简历" without a JD | General rewrite |
| "根据这个 JD 改", "tailor for this role" | JD tailoring |
| "只改这段经历/项目/技能" | Surgical rewrite |
| "有没有吹过头", "audit this version" | Truthfulness audit |

## Productized Resume Tools

When the request involves a local resume app rather than only a document, inspect the app before rewriting copy. Common local projects include `ai-resume-polisher-local` and `ai-recruiting-assistant`.

For resume product work:

1. Locate the resume source shape: uploaded doc extraction, `resume-data.js`, JSON store, parser output, generated Markdown, or UI state.
2. Preserve the same truthfulness rules as document rewriting.
3. Keep parser, scorer, rewrite prompt, export, and UI presentation separated where the codebase already does.
4. Add tests for parsing, scoring normalization, export content, and high-risk truthfulness downgrades.
5. Verify the app flow with a realistic resume fixture and confirm the final document/export matches the visible result.

Avoid using app code to silently invent stronger facts. If a product feature proposes metrics or stronger claims, mark them as suggestions needing user confirmation.

When the user asks to edit a file, preserve the original unless they explicitly say to overwrite it. For large rewrites, produce a concise change preview first if the edit would introduce inferred facts or reorder/delete major content.

## Intake

1. Identify the source format: plain text, Markdown, DOCX/PDF extracted text, HTML, `resume-data.js`, JSON, or YAML.
2. Locate the target file only when the user wants a file edited. If multiple resume-like files exist, choose the obvious one by name and recency; ask only when ambiguity can cause data loss.
3. Determine the target role, seniority, country/language, and whether a JD is present.
4. Keep source facts separate from inferred improvements. Use `[待确认]` or `Needs confirmation` for anything not directly supported.

## Diagnosis

Check the resume by module:

- Positioning: headline, summary, target role, first-screen proof.
- Experience: action specificity, result strength, scope, ownership, relevance.
- Projects: problem, method, deliverable, measurable outcome.
- Skills: JD relevance, evidence, keyword naturalness.
- Education, awards, certifications: factual clarity and ordering.

Prioritize issues by hiring impact:

1. Facts that look inflated or unverifiable.
2. JD-critical gaps.
3. Weak first-screen positioning.
4. Vague bullets with no action/result.
5. Style, grammar, and compactness.

## Rewrite Process

For any non-trivial rewrite, load `references/rewrite-framework.md`.

1. Convert each weak bullet into context + action + result.
2. Choose verbs by evidence strength, not by desired impressiveness.
3. Use numbers only when present, mathematically derived from present facts, or explicitly marked for confirmation.
4. Replace empty claims such as "熟悉", "掌握", "deep understanding", and "strong communication" with observable actions or remove them.
5. Keep each bullet concise: one main action, one result, one role-relevant keyword cluster.
6. For Chinese resumes, prefer direct business language. For English resumes, prefer action verb + object + method + result.

## JD Tailoring

When a JD or target job is present, load `references/jd-tailoring.md`. If the role type is clear, also load the relevant section from `references/role-competency-library.md`.

1. Parse the JD into responsibilities, hard requirements, preferred skills, implicit expectations, ATS keywords, and business context.
2. Build a JD-to-resume evidence matrix.
3. Move the strongest matching evidence into the top third of the resume.
4. Rewrite related bullets in the JD's language while preserving the candidate's real scope.
5. Compress or remove content that does not support the target role.
6. Audit every inserted keyword: it must be natural, supported, and useful to a recruiter.

## Surgical Rewrite

When the user asks to modify only one section:

1. Keep all unrelated sections unchanged.
2. Output the original text, rewritten version, and reason for each change.
3. If editing a structured file, only touch the requested field or object.
4. Flag missing facts that would make the section stronger instead of filling them in.

## Truthfulness Audit

Run `scripts/audit_resume_text.py` when working with a local text-like resume file or when the user asks for risk checking. Treat script output as heuristic evidence, then apply judgment.

Audit for:

- inflated verbs with insufficient evidence,
- vague participation language,
- unsupported percentages or impact claims,
- subjective traits without proof,
- keyword stuffing,
- mismatched seniority.

When a claim is too strong, downgrade it rather than deleting the useful evidence. Example: change "主导搭建增长体系" to "参与增长指标拆解，并负责周报看板维护" if the source only supports partial execution.

## Output Contracts

For diagnosis:

```markdown
## 关键问题
| 优先级 | 模块 | 问题 | 证据 | 怎么改 |
```

For rewrite:

```markdown
## 修改稿
| 模块 | 原文 | 改写后 | 修改理由 | 风险 |
```

For JD tailoring:

```markdown
## JD 匹配与定制
| JD 要求 | 简历证据 | 判定 | 改写动作 |
```

For file edits, finish with:

- Files changed.
- What changed.
- Risk or confirmation items.
- Validation command and result.

## Word Output

Use `scripts/resume_markdown_to_docx.py` for final Word output:

```bash
python scripts/resume_markdown_to_docx.py clean-resume.md clean-resume.docx
```

The Markdown input should contain only the final resume content, not the critique, before/after table, or internal notes. Put diagnostics and confirmation questions in a separate Markdown file if needed.

Word output rules:

- Use A4 page size, resume-friendly margins, and readable typography.
- Preserve clear hierarchy: candidate name, contact line, sections, roles/projects, bullets.
- Keep bullets concise; avoid tables unless the user explicitly wants them.
- Do not put unconfirmed facts into the Word resume. Put those in a separate notes file.
- If a DOCX render/visual QA tool is available, render and inspect before delivery; if unavailable, validate that the DOCX opens and contains the expected paragraphs.

## Reference Loading

- Load `references/rewrite-framework.md` for any actual rewrite.
- Load `references/jd-tailoring.md` when the user provides a JD or target role.
- Load `references/role-competency-library.md` only for the matching role family.
- Load `references/word-output.md` when creating or validating a Word `.docx` resume.

## Script

Use the audit script on local files:

```bash
python scripts/audit_resume_text.py path/to/resume.md
python scripts/audit_resume_text.py path/to/resume-data.js --json
```

The script supports `.txt`, `.md`, `.js`, `.json`, `.yaml`, and any UTF-8 text file. It does not prove a resume is truthful; it highlights lines that need human review.

Use the Word export script on clean Markdown resume drafts:

```bash
python scripts/resume_markdown_to_docx.py path/to/final-resume.md path/to/final-resume.docx
```

