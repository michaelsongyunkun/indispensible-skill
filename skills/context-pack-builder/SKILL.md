---
name: context-pack-builder
description: "Use when preparing context for subagents, agent handoff, new Codex thread, AGENTS.md, implementation packet, reviewer packet, research packet, 多Agent上下文包, or when repeated work needs a concise reusable brief"
---

# Context Pack Builder

Create a compact packet that another agent can act on without inheriting the whole conversation.

## Packet Shape

```markdown
# Context Pack

## Goal
## Current State
## Relevant Files
## Constraints
## Decisions Already Made
## Unknowns
## Task Lanes
## Verification
## Output Contract
```

## Rules

- Include only task-relevant context; do not paste the whole chat.
- Use absolute or repo-relative file paths.
- Include exact commands or checks when known.
- State what not to change.
- For reviewers, include the expected behavior and diff range.
- For researchers, include source quality expectations and date sensitivity.

## Persistence

If the context should live beyond the current task, write it into `AGENTS.md`, a project doc, or the user's skill/workflow repository only when asked.

