---
name: product-invent-skill
description: Use when the user wants to invent, validate, scope, plan, design, build, test, run, package, deploy, or iterate a new product, startup idea, SaaS, app, website, AI tool, game, MVP, prototype, vibe-coding prompt, product spec, 产品想法, 创业项目, 应用, 网站, 工具, or 最小可行产品.
---

# Product Invent Skill

## Overview

Use this as an orchestration skill for product development from fuzzy idea to verified MVP. It keeps the work moving through goal definition, invention, market grounding, planning, implementation, testing, verification, and local/deployment readiness.

## Operating Rule

Load only the sub-skills needed for the current stage. Do not front-load every referenced skill if the user is asking for a narrow slice such as naming, competitive research, UI polish, or deployment.

When the user asks to build a product end to end, follow the full sequence below. If the user gives a strong constraint, let the constraint shape the sequence but keep the missing stages visible as risks.

## Invocation Signals

Use this skill even when the user does not name it directly if the request sounds like product invention or product delivery. Common signals include:

- "build me an app", "make a SaaS", "turn this idea into an MVP", "create a prototype", "write a vibe-coding prompt", "ship this product", "design and build this tool".
- "我要做一个产品", "帮我做个应用", "把这个想法做成 MVP", "做一个网站/工具/小游戏", "生成开发提示词", "从 0 到 1 做出来".
- Requests that combine product strategy with implementation, such as user research plus frontend, competitor analysis plus build plan, or prototype plus deployment.

Do not use this skill for isolated maintenance tasks on an existing product unless the user is rethinking product direction, adding a major new workflow, or asking for an MVP-style rebuild.

## Full Product Sequence

1. **Goal definition**
   - **REQUIRED SUB-SKILL:** Use `define-goal`.
   - Convert the idea into a concrete objective, audience, success criteria, constraints, and first useful milestone.
   - Exit when there is a crisp MVP outcome and a visible boundary for what is out of scope.

2. **Invention and product shaping**
   - **REQUIRED SUB-SKILL:** Use `superpowers:brainstorming`.
   - Explore target users, jobs-to-be-done, core workflow, differentiators, risks, and the smallest product that proves value.
   - Prefer a few strong product directions over a long feature dump.

3. **Market and competitor grounding**
   - **REQUIRED SUB-SKILL:** Use `competitor-analysis`.
   - Compare alternatives, pricing/positioning signals, user expectations, gaps, and likely table-stakes features.
   - Browse when current market, pricing, companies, product capabilities, or recommendations matter.

4. **Implementation plan**
   - **REQUIRED SUB-SKILL:** Use `superpowers:writing-plans`.
   - Turn the chosen direction into milestones, technical architecture, data model, UI surfaces, risks, verification plan, and rollout path.
   - Keep the first build small enough to complete and test.

5. **Experience design**
   - **REQUIRED SUB-SKILL:** Use `frontend-design` for any user-facing app, website, dashboard, game, or tool.
   - Use a domain-specific technical skill when applicable, for example `vercel:nextjs`, `chatgpt-apps`, `us-college-planning-agent`, `presentations`, `spreadsheets`, or `documents`.
   - Make the first screen the actual usable product, not a marketing placeholder, unless the user explicitly asks for a landing page.

6. **Build with tests**
   - **REQUIRED SUB-SKILL:** Use `superpowers:test-driven-development` for feature work and bug fixes when behavior can be tested.
   - Start with the highest-risk behavior, then implement the minimum code that satisfies it.
   - Match the repo's existing frameworks, conventions, and test style.

7. **Verify before completion**
   - **REQUIRED SUB-SKILL:** Use `superpowers:verification-before-completion`.
   - Run automated checks and perform realistic manual/browser verification for the user-facing path.
   - Do not claim completion from static inspection alone when the product can be run.

8. **Run, package, or deploy**
   - **REQUIRED SUB-SKILL:** Use `local-webapp-run-deploy` when running or packaging a local web app.
   - **REQUIRED SUB-SKILL:** Use `vercel:verification` for Vercel-hosted or Vercel-targeted products.
   - Give the user the local URL, deployed URL, or exact artifact path, plus any checks that did not run.

## Decision Shortcuts

- If the user asks only for a product idea: use stages 1-3.
- If the user asks for a build prompt: use stages 1-4, then produce a Codex-ready prompt.
- If the user asks to build the MVP: use all stages.
- If the repo already exists: inspect the repo before planning implementation details.
- If the product is primarily frontend: prioritize `frontend-design`, browser verification, and responsive checks.
- If the product is primarily AI/chat: use OpenAI/Vercel/ChatGPT app skills that match the stack.
- If the product is education/admissions related: use `design-master-skill` or `us-college-planning-agent` as applicable.

## Outputs

Prefer concrete artifacts over abstract advice:

- Product brief: audience, problem, promise, MVP scope, non-goals.
- Competitive scan: alternatives, gaps, positioning, table-stakes.
- Implementation plan: milestones, data model, UI map, testing plan.
- Working product: code changes, running URL, verification notes.
- Launch handoff: deployment status, residual risks, next iteration.

## Common Mistakes

- Do not skip goal definition because the idea sounds obvious.
- Do not turn brainstorming into an oversized feature list.
- Do not rely on stale competitor knowledge when current market facts matter.
- Do not design a polished shell before the core workflow works.
- Do not finish without running the product or verifying the primary path.
