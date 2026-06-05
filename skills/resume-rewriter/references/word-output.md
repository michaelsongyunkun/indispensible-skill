# Word Output Rules

Use this reference when the user expects a Word resume deliverable.

## Deliverable Contract

The final resume deliverable is a `.docx` file. Markdown is a staging format for authoring, review, and traceability.

Generate two files for substantial rewrites:

1. `candidate-role-resume.docx`: final clean Word resume.
2. `candidate-role-notes.md`: change summary, risks, and confirmation questions.

Do not put notes, critique, before/after tables, or uncertainty markers into the final `.docx` unless the user explicitly wants an annotated version.

## Layout

Use A4 page size with compact but readable margins. For one-page resumes, start with 0.55 inch margins. Use a professional font stack that works in Word:

- Chinese: Microsoft YaHei or DengXian fallback.
- English: Aptos, Arial, or Calibri fallback.

Recommended hierarchy:

- Name: 18-22 pt, bold, centered.
- Contact line: 9-10 pt, centered.
- Section heading: 11-12 pt, bold, subtle bottom border or spacing.
- Role/project heading: 10-11 pt, bold.
- Body bullets: 9-10 pt, compact spacing.

## Content

Final Word resume should contain only verified content:

- no `[待确认]` markers,
- no internal notes,
- no "why this changed" commentary,
- no diagnostic tables,
- no unsupported metrics.

If a fact is attractive but unconfirmed, leave it out of the `.docx` and place it in the notes file.

## Validation

After generating `.docx`:

1. Reopen it with `python-docx` and check it has paragraphs.
2. If the Documents renderer is available, render to PNG and visually inspect all pages.
3. If rendering is unavailable, state that structural validation passed but visual render QA was skipped.
