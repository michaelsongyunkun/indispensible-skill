---
name: us-college-application-consultant
description: Use when working on Michael Song's US college admissions consultant product: planning Agent, fixed prompts, parent-facing reports, course/GPA helpers, disclaimers, nationality eligibility, similar case matching, activity planning, resource libraries, university/major knowledge bases, DeepSeek/RAG, JSON/Word/SVG exports, analytics events, admin dashboards, login data, permissions, and Excel/download exports.
---

# US College Application Consultant

Use this skill for Michael's unified US admissions consultant project. It covers the planning Agent, knowledge/RAG resources, exports, analytics, admin operations, and permission boundaries in one workflow so the project does not split across overlapping skills.

## Project Map

Common files and folders:

- `server.mjs`: Express routes, auth, admin endpoints, analytics, exports, and static serving.
- `src/client`: browser UI modules, planning flows, dashboard panels, export buttons, and event tracking.
- `src/server`: services, repositories, auth helpers, analytics helpers, and export utilities.
- `src/domain`: admissions planning logic, schemas, calculators, eligibility checks, and report transformations.
- `data` or knowledge folders: resources for schools, majors, activities, cases, requirements, prompt text, and RAG inputs.
- `tests`: prompt/parser, planner, calculator, analytics, permissions, export, and smoke tests.

Read existing code, prompt files, and data contracts before changing behavior. Preserve fixed prompt wording unless the user explicitly asks to revise it.

## Core Rules

- Keep the product parent-facing: practical, calm, specific, and transparent about uncertainty.
- Do not invent admissions rules, rankings, cases, requirements, deadlines, or eligibility. Mark gaps as `needs verification` or `source missing`.
- Separate advice, factual data, and computed results in reports and exports.
- Protect private user/application data. Respect auth boundaries, admin-only views, `.env` secrets, and per-user records.
- Prefer modular additions: shared schemas, domain services, reusable client renderers, and explicit tests over one-off page scripts.

## Planning Agent And Reports

For planning Agent, course helper, GPA calculator, eligibility, similar-case matching, activity planning, and parent reports:

1. Identify the target student profile, grade level, constraints, and user-facing output.
2. Preserve or version fixed consultant prompts and parsing contracts.
3. Keep answers structured: recommendation, rationale, evidence/source, confidence, next action, and caveats.
4. For GPA/course helpers, distinguish inputs, assumptions, calculated values, and non-calculated advice.
5. For similar cases, expose why a case matched and avoid presenting a case as a guarantee.
6. For activity or application plans, include timeline, owner, priority, evidence needed, and export-ready summary.

## Knowledge, RAG, And Exports

- Normalize resources into stable schemas before wiring them into prompts or retrieval.
- Keep knowledge data auditable with source fields, status, and last-reviewed dates when possible.
- For DeepSeek/RAG flows, verify retrieval inputs, prompt assembly, model response parsing, and fallback behavior.
- Support export paths intentionally: JSON for machine reuse, Word/docx for parent-facing reports, SVG/HTML for visual plans, CSV/Excel for admin tables.
- When changing exports, inspect generated output structure and at least one representative file when tools are available.

## Analytics And Admin Dashboard

For login data, feature usage metrics, admin dashboards, event tracking, permissions, and Excel/download exports:

- Define event names, payload fields, user/session identity, timestamp, source page, and privacy constraints before adding tracking.
- Track meaningful product events: register/login/logout, planning submission, prompt run, report view, export/download, resource search, GPA/course helper use, activity planner use, and admin actions.
- Do not track secrets, raw essays, private notes, or unnecessary personally identifying data.
- Admin pages should show totals, filters, recent activity, user-level drilldowns, export/download controls, loading/empty/error states, and permission-denied behavior.
- Verify ordinary users cannot access admin routes, data, or exports.
- For Excel/CSV exports, include stable columns, date ranges, row counts, and filename conventions.

## Verification Checklist

Before final response, check the relevant subset:

- Prompt/parser tests for planning Agent changes.
- Calculator or eligibility tests for GPA/course/nationality logic.
- RAG/search tests for knowledge-base changes.
- Export smoke checks for JSON, Word/docx, SVG/HTML, CSV, or Excel.
- Auth and permission checks for admin routes and user-owned data.
- Analytics event coverage for the user flow changed.
- Browser verification for parent-facing report pages, admin dashboards, and mobile/desktop layouts.
- Final handoff includes changed files, commands run, local URL if served, and unresolved data/source gaps.
