---
name: xhs-image-intel
description: Use when collecting public or authorized Xiaohongshu, RedNote, or XHS notes by theme and extracting structured information from note images, screenshots, comments, links, exports, or local xiaohongshu-mcp results. Also use for XHS research-to-output workflows such as admissions case collection, market notes, copywriting intelligence, creator/content analysis, and normalized CSV/JSON/Excel datasets.
---

# XHS Image Intel

## Overview

Use this skill to turn a theme such as "留学中介避坑" or "小户型装修" into a structured dataset of Xiaohongshu notes plus image-level intelligence. It composes Xiaohongshu access tools with image understanding and export skills; it does not bypass login, CAPTCHA, rate limits, private content, or platform restrictions.

## Tool Selection

Prefer tools in this order:

1. Connected `xiaohongshu-mcp` tools if available. Use `tool_search` to look for `xiaohongshu`, `xhs`, or `rednote` tools before assuming they are absent.
2. A local `xhs` CLI if installed, especially the `xhs-cli` skill/command that supports `xhs search ... --json` and `xhs read ... --json`.
3. User-provided screenshots, image folders, CSV/Excel exports, or pasted note links when live collection is unavailable.

For exports, invoke the Spreadsheets skill for `.xlsx`, the Notion connector/skill for Notion databases, or write JSON/CSV directly. For local images, use image viewing/OCR/vision capabilities available in the current environment.

## Safety Gate

Before collection, confirm the data source is public or authorized. Do not request or log raw cookies. Do not automate actions that create side effects, including publish, like, favorite, comment, reply, or cookie deletion, unless the user explicitly asks for those actions in a separate request.

Stop and ask for confirmation when the request involves private accounts, personal contact harvesting, identity profiling, medical/legal/financial targeting, or bypassing authentication/risk controls.

## Workflow

1. Define the run:
   - Theme or keyword.
   - Target count, default `20` notes.
   - Filters, default `note_type="图文"`, `sort_by="综合"`, `publish_time="不限"`.
   - Output format, default `csv` plus `json`.
   - Extraction fields, default to `references/output-schema.md`.

2. Check access:
   - If MCP tools exist, call `check_login_status` when available.
   - If login is missing, explain the needed user-side login step. Do not ask the user to paste cookies.

3. Collect note candidates:
   - With MCP, call `search_feeds` using the theme and filters.
   - Keep `feed_id`, `xsec_token`, title, author, note URL, cover/image URLs, and visible engagement metrics.
   - Deduplicate by `feed_id` or canonical URL.

4. Fetch details:
   - Call `get_feed_detail` for selected candidates.
   - Use comments only when they are relevant; default to `load_all_comments=false`.
   - Preserve source fields separately from inferred image analysis.

5. Extract image intelligence:
   - For each image, identify OCR text, product/service names, brands, price or discount text, location clues, scene, style, visual objects, audience, pain points, selling points, and evidence snippets.
   - Add confidence per field. Mark uncertain facts as `unknown` rather than inventing.
   - Never infer sensitive personal attributes from people in images.

6. Normalize and export:
   - Save raw collection as JSONL.
   - Save image insights as JSONL.
   - Use `scripts/merge_image_intel.py` to produce a flat CSV/JSON dataset.
   - If the user wants Notion or Excel, load the relevant skill/connector and map fields from the normalized JSON.

7. Report quality:
   - State note count, image count, skipped items, failed items, and output paths.
   - Include filter settings and whether data came from MCP, CLI, or user-provided files.

## MCP Details

Read `references/xiaohongshu-mcp.md` when using `xpzouying/xiaohongshu-mcp`, especially for required IDs/tokens and filters.

## Output Schema

Read `references/output-schema.md` before creating the final dataset, or when the user asks for custom extraction fields.

## Helper Script

Use `scripts/merge_image_intel.py` after collection and vision extraction:

```powershell
python scripts/merge_image_intel.py --notes notes.jsonl --images image_insights.jsonl --out results.csv --json-out results.json
```

Each line in `notes.jsonl` should describe one note. Each line in `image_insights.jsonl` should describe one image and include a `note_id` that matches the note record.

## Research-To-Output Modes

Choose a mode before extraction:

- **Admissions cases**: preserve school, major, applicant background, offer result, timeline, evidence snippets, and uncertainty. Do not infer private identity details.
- **Copywriting intelligence**: extract hook, title pattern, pain point, selling point, image composition, CTA, audience, tone, and reusable content pattern.
- **Product/market notes**: extract user problem, solution, price/value clues, competitor names, UX screenshots, objection, and adoption signal.
- **Image-heavy reference boards**: extract visual style, layout, color, object, text overlay, scene type, and confidence.

Keep raw source records separate from analysis so future runs can re-score or reformat the same notes.

## Local MCP Clues

If live XHS collection is requested, look for local tooling under `C:\Users\Michael Song\Documents\Codex\tools\xiaohongshu-mcp` and prior outputs under `Documents\Codex\2026-06-04\mcp-server-mcp-skill`. Use available login/status/start scripts only when the user has authorized the account/session. Never expose or paste cookies in final output.
