---
name: codex-multi-agent-operating-system
description: "Use when the user wants Codex to become stronger through multiple agents, subagents, agent team, parallel workers, reviewer agents, BMAD/Superpowers style collaboration, 多Agent协作, 多智能体, or coordinated research/design/build/review workflows"
---

# Codex Multi-Agent Operating System

Coordinate Codex work as an agent team without letting the skill list fragment the task.

## Default Router

Use the smallest team that can reduce risk:

| User intent | Route |
|---|---|
| Vague idea, product, MVP, PRD, architecture | `multi-agent-product-studio` |
| 2+ independent research or analysis lanes | `parallel-research-synthesis` |
| Written implementation plan with independent tasks | `subagent-driven-development` |
| Multiple independent failures or subsystems | `dispatching-parallel-agents` |
| Review before merge/ship | `subagent-code-review-board` or `requesting-code-review` |
| Need reusable context for agents/handoff | `context-pack-builder` |
| Need domain-specific agent team design | `agent-team-harness` |

## Operating Rules

1. Confirm whether real subagent/multi-agent tools are available. If absent, search with `tool_search`.
2. Split work into independent lanes only when file ownership, data needs, and verification do not collide.
3. Give each lane a self-contained packet: goal, context, files, constraints, output format, and verification.
4. Merge with evidence: compare outputs, resolve conflicts, run checks, and note residual risk.
5. Never pretend a subagent ran. If only local parallel tool calls ran, say so.

## Source Ideas

- Superpowers: planning, subagent execution, review, verification.
- BMAD Method: PM, analyst, architect, developer, UX, QA, and roundtable roles.
- oh-my-skills harness/team: agent team architecture patterns.
- Anthropic Agent Skills: concise `SKILL.md` structure and progressive disclosure.

