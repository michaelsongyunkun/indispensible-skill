---
name: subagent-code-review-board
description: "Use when the user asks for code review with multiple reviewers, QA board, reviewer agents, adversarial review, security/performance/accessibility review, PR review, 代码审查, 多Agent审查, or before shipping risky code"
---

# Subagent Code Review Board

Review code through multiple lenses, then merge the findings.

## Reviewer Lenses

| Lens | Looks for |
|---|---|
| Spec Auditor | requirement mismatches, missing acceptance criteria |
| Bug Hunter | logic errors, edge cases, regressions |
| Security Reviewer | auth, secrets, injection, unsafe IO, permissions |
| Performance Reviewer | slow paths, repeated work, blocking operations |
| UX/Accessibility Reviewer | broken flows, confusing states, layout/accessibility issues |

## Process

1. Get the review range: staged changes, working tree, branch diff, PR, or named files.
2. Use real reviewer subagents if available; otherwise do separate focused passes yourself.
3. Lead with findings ordered by severity and grounded in file/line references.
4. Include test gaps and residual risk.
5. Avoid style nitpicks unless they hide a real bug or maintainability risk.

## Output Format

Findings first. Then open questions. Then a short summary of reviewed scope and verification.

