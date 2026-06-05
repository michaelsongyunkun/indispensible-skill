# Downloaded / Local Helper Skills

This folder contains frequently used downloaded or locally installed skills that support Michael's workflow.

They are intentionally separated from `../skills/`:

- `../skills/` = Michael's self-developed or heavily customized canonical skills.
- `downloaded-skills/` = useful helper skills installed locally, not claimed as Michael-developed.

## Included

- `chatgpt-apps`
- `competitor-analysis`
- `define-goal`
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
- `security-best-practices`
- `security-threat-model`
- `sentry`
- `screenshot`
- `speech`
- `together-video`
- `transcribe`
- `vidu-skills`
- `web-crawler`
- `yeet`

## Install

```powershell
$repo = "C:\path\to\indispensible-skill"
Copy-Item -Recurse -Force "$repo\downloaded-skills\*" "$env:USERPROFILE\.codex\skills\"
```

For skills that originally lived under `~/.agents/skills` (`product-studio-orchestrator`, `vidu-skills`), install them there if you want to preserve their original root:

```powershell
$repo = "C:\path\to\indispensible-skill"
Copy-Item -Recurse -Force "$repo\downloaded-skills\product-studio-orchestrator" "$env:USERPROFILE\.agents\skills\product-studio-orchestrator"
Copy-Item -Recurse -Force "$repo\downloaded-skills\vidu-skills" "$env:USERPROFILE\.agents\skills\vidu-skills"
```
