# Indispensible Skill

Michael Song's personal Codex skill and workflow collection.

This repository contains the skills and workflows that were developed or heavily customized for Michael's recurring work: MVP shipping, US college admissions products, knowledge-base generation, UI/UX design, entertainment apps, writing, resume rewriting, content intelligence, and video/script workflows.

## Structure

| Path | Purpose |
|---|---|
| `skills/` | Active self-developed or locally customized Codex skills. Use these as the canonical versions. |
| `workflows/` | Obsidian-friendly workflow maps and operating playbooks. |
| `MANIFEST.md` | Skill inventory, source/status notes, and merge map. |

## Install

Copy any active skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\mvp-product-shipping-loop "$env:USERPROFILE\.codex\skills\mvp-product-shipping-loop"
```

For a full install on Windows:

```powershell
$repo = "C:\path\to\indispensible-skill"
Copy-Item -Recurse -Force "$repo\skills\*" "$env:USERPROFILE\.codex\skills\"
```

Restart Codex or open a new thread after installing so the skill list refreshes.

## Active Canonical Skills

- `ai-entertainment-app-builder`
- `cinematic-video-workflow`
- `design-master-skill`
- `knowledge-doc-builder`
- `local-webapp-run-deploy`
- `mvp-product-shipping-loop`
- `product-invent-skill`
- `resume-rewriter`
- `screenplay-writer`
- `ui-ux-pro-max`
- `us-college-application-consultant`
- `vibe-coding-prompt-generator`
- `xhs-image-intel`
- `xianxia-longform-writer`

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

## Notes

Downloaded/plugin/system skills and old superseded skill versions are intentionally not copied here unless they were locally customized into Michael-specific active workflows. This repository is meant to preserve Michael's current operating layer, not mirror every available Codex plugin or keep obsolete duplicates.
