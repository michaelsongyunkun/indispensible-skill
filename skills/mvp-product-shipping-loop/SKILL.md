---
name: mvp-product-shipping-loop
description: Use when turning Michael Song's product ideas, generated vibe-coding prompts, local app concepts, or MVP requests into working Next.js/Vite/HTML implementations with tests, browser verification, polish, and run instructions. Triggers include AI tools, quizzes, dashboards, games, vibe-coded products, and local prototypes.
---

# MVP Product Shipping Loop

Use this skill when the task is bigger than generating a prompt and smaller than a full product organization. The goal is a working local app with a clear core loop, verification evidence, and a clean handoff.

## Core Workflow

1. Read the project first: `package.json`, README, app/routes/components, tests, docs/specs, and existing design conventions.
2. Convert the request into an MVP contract: target user, core job, first-screen workflow, data model, must-have states, non-goals, and acceptance checks.
3. Choose the smallest stable implementation path:
   - Existing app: follow its stack and component style.
   - Empty folder: prefer a simple React/Next/Vite or static HTML path appropriate to the user's expected deployment.
4. Implement in checkpoints: domain/data logic, UI core loop, persistence/export if needed, tests, then visual polish.
5. Run available commands in order of signal: unit tests, typecheck, lint, build, verify, smoke/browser check.
6. Start the local dev server when the app needs one and give the user the URL.
7. Use browser verification for interactive flows, mobile/desktop layout risk, canvas/game apps, or any UI polish request.
8. Finish with changed files, commands passed/failed, local URL, and remaining risks.

## Prompt Intake And MVP Extraction

When the user provides a rough idea, generated prompt, or vibe-coding brief, extract the MVP contract before coding:

- Core user flow: the first thing a real user can do successfully.
- Inputs and controls: required fields, modes, toggles, uploads, filters, or sliders.
- Output: generated text, result cards, reports, dashboards, exports, saved history, or gameplay state.
- Data model: entities, stored state, scoring rules, prompt versions, and export formats.
- Non-goals: defer secondary pages, monetization, external APIs, auth, or perfect content unless explicitly requested.
- UI expectations: first screen must be the usable product, not a marketing page, unless the user asks for a landing page.
- Acceptance checks: the shortest browser/test path proving the core loop works.

If the folder is empty, prefer React + TypeScript + Vite for small web MVPs unless the prompt clearly implies Next.js, static HTML, or another existing stack. Keep dependencies modest; use proven libraries for games, AI SDKs, parsing, charts, or domain logic when established rules matter.

## Product Patterns

### AI Tools

- Provide input, controls, generate/action button, editable output, copy/export, and graceful empty/error/loading states.
- Keep prompts versioned when the user says the prompt is fixed.
- Do not require a live API for an MVP unless the request explicitly needs it.
- For writing, learning, and assistant tools, provide an editable workspace with style/mode controls, a clear run action, copy/export, and a small history or reset path when useful.

### Quiz, Matching, Tarot, Personality, Idol Apps

- Define scoring or interpretation logic before UI decoration.
- Make results explainable: show why the output was chosen.
- Test edge cases: empty answers, ties, repeated choices, reload/history behavior.

### Operational Dashboards

- Prioritize dense, scannable UI over landing-page composition.
- Add filters, totals, and export controls only when backed by data.
- Verify permission boundaries when admin data exists.

### Games

- Make the first screen playable.
- Implement rules completely before animation polish.
- Verify keyboard/touch controls and restart/game-over paths.
- For classic games, test deterministic rules such as collision, scoring, pause/restart, speed changes, and game-over recovery before adding visual effects.

### Educational Apps

- Provide lesson or task navigation, practice input, checking, hints or explanations, and visible progress.
- Keep feedback specific: show what changed, why the answer/result was chosen, and what the next action is.

## Local Project Clues

Recurring projects include `ai-travel-planner-assistant`, `ai-cooking-coach`, `ai-recruiting-assistant`, `ai-resume-polisher-local`, `ai-tarot-sanctum`, `idol-match-test`, `qingqing-grassland-personality`, and `xhs-copywriting-master`.

Common script names: `dev`, `dev:detached`, `build`, `start`, `test`, `lint`, `typecheck`, `verify`, `smoke`.

## Handoff Standard

The final answer must include what was built or changed, how to run it, the local URL if a server is running, verification commands and browser checks, and known limitations or next checkpoint.
