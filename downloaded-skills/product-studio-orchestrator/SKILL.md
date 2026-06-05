---
name: product-studio-orchestrator
description: Use when the user explicitly asks for Codex subagents, multi-agent, parallel agents, or agent collaboration while building, reviewing, or iterating a complete product.
---

# Product Studio Orchestrator

Use this skill to coordinate a complete product build with custom Codex subagents.

## Core Pattern

Keep the parent agent as the conductor. Spawn subagents only when the user explicitly asks for multi-agent or parallel work. Do not let child agents recursively fan out unless the user explicitly requests it.

## Agent Roster

| Phase | Agent | Sandbox | Output |
| --- | --- | --- | --- |
| Product | `product_strategist` | read-only | MVP scope, acceptance criteria, risks |
| UX | `ux_architect` | read-only | flows, screens, states, handoff |
| Frontend | `frontend_builder` | workspace-write | UI implementation and verification |
| Backend | `backend_builder` | workspace-write | APIs, data, services, backend tests |
| QA | `qa_reviewer` | read-only | findings, missing tests, release risks |
| Release | `release_integrator` | workspace-write | integration fixes and final evidence |

## Workflow

1. Restate the product goal, known constraints, and success criteria.
2. Spawn `product_strategist` and `ux_architect` for independent planning when the task is not already fully specified.
3. Synthesize their output into a short build plan with disjoint frontend and backend write scopes.
4. Spawn `frontend_builder` and `backend_builder` only after write scopes are clear.
5. Continue useful parent-agent work while builders run: inspect project structure, identify verification commands, and prepare integration checklist.
6. Review builder outputs before trusting them. Check changed files, contracts, and test evidence.
7. Spawn `qa_reviewer` for read-only acceptance and regression review.
8. Use `release_integrator` for cross-slice fixes or perform integration locally when the parent agent is already on the critical path.
9. Run fresh verification before completion claims. Report actual evidence and any gaps.

## Delegation Rules

- Give each worker a concrete task, file/module ownership, and explicit non-goals.
- Keep frontend and backend write sets disjoint whenever possible.
- Use read-only agents for exploration, product, UX, docs, and QA.
- Do not delegate the immediate blocking task if the parent agent needs it before doing anything useful.
- Do not duplicate work between parent and child agents.
- Do not trust agent success reports without inspecting diffs and verification output.

## Starter Prompt

```text
Use product-studio-orchestrator. Build this product with subagents.

Goal:
<describe the product>

Constraints:
<stack, deadline, scope, assets, deployment target>

Please spawn product_strategist and ux_architect first if scope is unclear.
Then split frontend_builder and backend_builder with disjoint write scopes.
Use qa_reviewer before final integration, and only claim completion after fresh verification.
```

## Completion Checklist

- Product scope and non-goals are explicit.
- UX flow, states, and component boundaries are defined.
- Frontend and backend contracts match.
- Tests or focused verification cover the accepted user flow.
- QA findings are addressed or listed as known issues.
- Final answer includes changed files, verification evidence, and remaining risks.
