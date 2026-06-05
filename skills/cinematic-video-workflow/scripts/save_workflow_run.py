#!/usr/bin/env python3
"""Save a cinematic-video-workflow result as a resumable project run."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "cinematic-video-run"


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def copy_media(result: dict[str, Any], media_dir: Path) -> list[dict[str, str]]:
    saved: list[dict[str, str]] = []
    output_ref = result.get("final_video", {}).get("output_ref", "")
    if not output_ref:
        return saved

    src = Path(output_ref)
    if not src.exists() or not src.is_file():
        return saved

    media_dir.mkdir(parents=True, exist_ok=True)
    dest = media_dir / src.name
    if src.resolve() != dest.resolve():
        shutil.copy2(src, dest)
    saved.append(
        {
            "kind": "final_video",
            "path": str(dest),
            "description": "Copied final generated video.",
        }
    )
    return saved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow_result", type=Path)
    parser.add_argument("--project-dir", type=Path, default=Path.cwd())
    parser.add_argument("--slug", default="")
    args = parser.parse_args()

    result = json.loads(args.workflow_result.read_text(encoding="utf-8-sig"))
    project_name = result.get("project_name") or result.get("screenplay", {}).get("title") or "cinematic-video-run"
    run_slug = slugify(args.slug or project_name)
    run_dir = args.project_dir / "workflow_runs" / f"{date.today().isoformat()}-{run_slug}"
    run_dir.mkdir(parents=True, exist_ok=True)

    write_json(run_dir / "brief.json", result.get("user_input", {}))
    write_json(run_dir / "screenplay.json", result.get("screenplay", {}))
    write_json(run_dir / "video_plan.json", result.get("video_plan", {}))
    write_json(
        run_dir / "execution-log.json",
        {
            "execution_log": result.get("execution_log", []),
            "errors": result.get("errors", []),
        },
    )

    files = [
        {"kind": "brief", "path": str(run_dir / "brief.json"), "description": "Normalized user brief."},
        {"kind": "screenplay", "path": str(run_dir / "screenplay.json"), "description": "Detailed screenplay and passes."},
        {"kind": "video_plan", "path": str(run_dir / "video_plan.json"), "description": "Video generation prompts and plan."},
        {"kind": "execution_log", "path": str(run_dir / "execution-log.json"), "description": "Execution log and errors."},
    ]
    files.extend(copy_media(result, run_dir / "media"))

    manifest = result.setdefault("artifact_manifest", {})
    manifest["run_dir"] = str(run_dir)
    manifest["files"] = files
    manifest.setdefault("external_refs", [])
    manifest.setdefault("skipped", [])

    write_json(run_dir / "workflow-result.json", result)

    readme = [
        f"# {project_name}",
        "",
        f"- Date: {date.today().isoformat()}",
        f"- Output mode: {result.get('user_input', {}).get('output_mode', '')}",
        f"- Final video status: {result.get('final_video', {}).get('status', '')}",
        "",
        "## Files",
        "",
    ]
    for item in files:
        readme.append(f"- {item['kind']}: `{Path(item['path']).name}` - {item['description']}")
    readme.append("")
    readme.append("Resume from `workflow-result.json`.")
    (run_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")

    print(str(run_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
