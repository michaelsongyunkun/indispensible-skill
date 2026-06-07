# Indispensible Skill

Michael Song's personal Codex skill and workflow collection.

This repository contains the skills and workflows that were developed or heavily customized for Michael's recurring work: MVP shipping, US college admissions products, knowledge-base generation, UI/UX design, entertainment apps, writing, resume rewriting, content intelligence, and video/script workflows.

## Structure

| Path | Purpose |
|---|---|
| `skills/` | Active self-developed or locally customized Codex skills. Use these as the canonical versions. |
| `downloaded-skills/` | Frequently used downloaded or locally installed skills that are useful alongside Michael's own skills. Kept separate from `skills/` so provenance stays clear. |
| `workflows/` | Obsidian-friendly workflow maps and operating playbooks. |
| `MANIFEST.md` | Skill inventory, source/status notes, and merge map. |

## Install

Copy any self-developed active skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\mvp-product-shipping-loop "$env:USERPROFILE\.codex\skills\mvp-product-shipping-loop"
```

For a full install on Windows:

```powershell
$repo = "C:\path\to\indispensible-skill"
Copy-Item -Recurse -Force "$repo\skills\*" "$env:USERPROFILE\.codex\skills\"
```

To also install the downloaded/local helper skills:

```powershell
$repo = "C:\path\to\indispensible-skill"
Copy-Item -Recurse -Force "$repo\downloaded-skills\*" "$env:USERPROFILE\.codex\skills\"
```

Restart Codex or open a new thread after installing so the skill list refreshes.

## Active Canonical Skills

- `ai-entertainment-app-builder`
- `agent-team-harness`
- `cinematic-video-workflow`
- `codex-multi-agent-operating-system`
- `context-pack-builder`
- `design-master-skill`
- `knowledge-doc-builder`
- `local-webapp-run-deploy`
- `multi-agent-product-studio`
- `mvp-product-shipping-loop`
- `parallel-research-synthesis`
- `product-invent-skill`
- `resume-rewriter`
- `screenplay-writer`
- `subagent-code-review-board`
- `ui-ux-pro-max`
- `us-college-application-consultant`
- `vibe-coding-prompt-generator`
- `xhs-image-intel`
- `xianxia-longform-writer`

## Downloaded / Local Helper Skills

These are included because Michael uses them often, but they are kept outside the self-developed `skills/` directory:

- `chatgpt-apps`
- `competitor-analysis`
- `define-goal`
- `dispatching-parallel-agents`
- `executing-plans`
- `figma-create-new-file`
- `figma-generate-design`
- `figma-use`
- `gh-address-comments`
- `gh-fix-ci`
- `linear`
- `mcp-builder`
- `notion-research-documentation`
- `notion-spec-to-implementation`
- `openai-docs`
- `pdf`
- `playwright`
- `playwright-interactive`
- `product-studio-orchestrator`
- `requesting-code-review`
- `security-best-practices`
- `security-threat-model`
- `sentry`
- `screenshot`
- `subagent-driven-development`
- `systematic-debugging`
- `speech`
- `together-video`
- `transcribe`
- `using-git-worktrees`
- `verification-before-completion`
- `vidu-skills`
- `web-crawler`
- `writing-plans`
- `yeet`

## Workflow Map

Start with:

- `workflows/codex-skill-workflow-map.md`

It documents which skills to use for common workflows:

- product idea -> MVP -> browser verification -> deployment
- US college admissions consultant product iteration
- knowledge-base, document, and dataset production
- UI/UX design and refactoring
- fiction, screenplay, and video workflows
- Xiaohongshu/content intelligence and market research
- resume/JD rewriting
- MCP, ChatGPT Apps, and agent/tool integration
- GitHub, CI, deployment, and production debugging
- Multi-agent Codex operating loops: agent-team planning, parallel research, subagent development, review boards, and verification

## Notes

Plugin/system skills and old superseded skill versions are intentionally not copied here. Downloaded/local helper skills are included in `downloaded-skills/` only when they are part of Michael's frequent operating layer.
