---
name: multi-agent-product-studio
description: "Use when the user asks Codex to build or plan a product, MVP, web app, SaaS, admissions product, feature, PRD, architecture, UX flow, or launch plan using multiple agents, BMAD roles, product team mode, 多Agent产品开发, or 专家小组"
---

# Multi-Agent Product Studio

Run product work as a compact BMAD-style team.

## Role Stack

Use only the roles needed:

| Role | Use for |
|---|---|
| Analyst | Market, user, competitor, requirement ambiguity |
| PM | PRD, scope, acceptance criteria, roadmap |
| UX | flow, information architecture, interface states |
| Architect | technical approach, data model, integration risk |
| Developer | implementation plan and code execution |
| QA/Reviewer | test plan, code review, edge cases, release confidence |

## Flow

1. Extract the product goal, user, constraints, deadline, and success criteria.
2. Run a short roundtable if ambiguity or risk is high; otherwise assign only the missing role.
3. Produce one durable artifact: PRD, implementation plan, architecture brief, QA checklist, or shipped code.
4. For implementation, hand off to `writing-plans`, then `subagent-driven-development` or `mvp-product-shipping-loop`.
5. Before saying done, use `verification-before-completion`.

## Output Contract

For planning: deliver assumptions, decisions, scope, non-goals, acceptance criteria, and next tasks.

For building: deliver changed files, verification evidence, unresolved risks, and the user-facing URL/file when relevant.

