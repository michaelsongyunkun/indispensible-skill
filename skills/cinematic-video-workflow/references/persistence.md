# Artifact Persistence

Save workflow runs when the user asks to save changes, asks for traceability, or a video/image asset is generated in a local project.

## Directory Layout

Default:

```text
workflow_runs/
  YYYY-MM-DD-slug/
    brief.json
    screenplay.json
    video_plan.json
    workflow-result.json
    execution-log.json
    README.md
    media/
```

Use a short slug from the project title or idea. Keep it lowercase ASCII with hyphens.

## Save Rules

- Save `workflow-result.json` as the canonical resumable artifact.
- Save `brief.json` from `user_input`.
- Save `screenplay.json` from `screenplay`, including naturalization, quality, motion, shot language, performance, and continuity passes.
- Save `video_plan.json` from `video_plan`.
- Save `execution-log.json` from `execution_log` and `errors`.
- Copy final videos/images into `media/` when local paths are available.
- Create `README.md` with project name, date, output mode, task IDs, local media files, and next-step notes.

## Secret Handling

Do not save:

- API keys, tokens, Authorization headers, cookies, or signed request headers.
- Full command lines containing secrets.
- Raw signed URLs unless they are required as temporary download sources and clearly marked as expiring.

Do save:

- Non-secret task IDs.
- Model name, duration, aspect ratio, resolution, and prompt text.
- Local output paths.
- Error codes/messages returned by tools, with secrets redacted.

## Resuming

To resume a run, load `workflow-result.json` first. Then inspect `artifact_manifest` to locate local media, prompts, task IDs, and skipped artifacts.
