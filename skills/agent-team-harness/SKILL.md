---
name: agent-team-harness
description: "Use when designing a reusable agent team, domain-specific subagents, multi-agent architecture, harness, expert pool, producer-reviewer loop, supervisor workflow, or when the user wants Codex to create/strengthen skills for coordinated agents"
---

# Agent Team Harness

Design a reusable multi-agent team before creating new skills or workflows.

## Architecture Patterns

| Pattern | Use when |
|---|---|
| Pipeline | Work has dependent stages: research -> spec -> build -> review |
| Fan-out/fan-in | Independent lanes can run in parallel and merge |
| Expert pool | Different inputs need different specialists |
| Producer-reviewer | One agent creates, another critiques, loop until acceptable |
| Supervisor | One coordinator assigns and reconciles dynamic tasks |

## Harness Design

1. Identify the domain, outputs, risks, and repeat frequency.
2. Choose the smallest architecture pattern that solves the coordination problem.
3. Define each role with inputs, outputs, allowed tools, stop conditions, and review criteria.
4. Convert repeated role behavior into Codex skills only when it will recur.
5. Validate with a realistic pressure scenario before installing broadly.

## Codex Notes

Use `skill-creator` for new skills. Use `context-pack-builder` for role packets. Use `codex-multi-agent-operating-system` when the user wants execution rather than harness design.

