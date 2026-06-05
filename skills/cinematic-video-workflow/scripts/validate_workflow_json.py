#!/usr/bin/env python3
"""Validate the minimal shape of a cinematic-video-workflow JSON artifact."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "project_name",
    "user_input",
    "screenplay",
    "character_designs",
    "scene_designs",
    "video_plan",
    "final_video",
    "artifact_manifest",
    "execution_log",
    "errors",
]

REQUIRED_SCREENPLAY = [
    "title",
    "summary",
    "characters",
    "scenes",
    "shots",
    "naturalization_pass",
    "quality_gate",
    "shot_language_pass",
    "performance_layer",
    "scene_continuity_check",
]
REQUIRED_NATURALIZATION_PASS = ["status", "environment_changes", "action_changes", "notes"]
REQUIRED_QUALITY_GATE = ["status", "scores", "issues", "revision_notes"]
REQUIRED_QUALITY_SCORES = ["hook", "pacing", "motivation", "dialogue_economy", "shootability"]
REQUIRED_REALISM_PASS = [
    "status",
    "physical_constraints",
    "optical_constraints",
    "lighting_constraints",
    "material_constraints",
    "environment_constraints",
    "generation_constraints",
]
REQUIRED_MOTION_NATURALNESS_PASS = [
    "status",
    "motion_rules",
    "fixed_actions",
    "negative_motion_constraints",
]
REQUIRED_SHOT_LANGUAGE_PASS = ["status", "coverage", "notes"]
REQUIRED_PERFORMANCE_LAYER = ["status", "character_beats", "notes"]
REQUIRED_SCENE_CONTINUITY_CHECK = ["status", "continuity_map", "issues", "notes"]
REQUIRED_VIDEO_PLAN = ["global_prompt", "shot_prompts", "transitions", "audio_notes"]
REQUIRED_FINAL_VIDEO = ["status", "output_ref", "notes", "realism_review"]
REQUIRED_REALISM_REVIEW = [
    "status",
    "scores",
    "issues",
    "successful_elements",
    "retry_prompt",
]
REQUIRED_REALISM_REVIEW_SCORES = [
    "identity_consistency",
    "motion_believability",
    "lighting_continuity",
    "camera_naturalness",
    "material_texture_realism",
    "anatomy_scale_correctness",
    "scene_geography_stability",
]
REQUIRED_ARTIFACT_MANIFEST = ["run_dir", "files", "external_refs", "skipped"]


def require_keys(obj: dict, keys: list[str], location: str) -> list[str]:
    return [f"{location}: missing key '{key}'" for key in keys if key not in obj]


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    errors.extend(require_keys(data, REQUIRED_TOP_LEVEL, "$"))

    if isinstance(data.get("screenplay"), dict):
        errors.extend(require_keys(data["screenplay"], REQUIRED_SCREENPLAY, "$.screenplay"))
        naturalization_pass = data["screenplay"].get("naturalization_pass")
        if isinstance(naturalization_pass, dict):
            errors.extend(
                require_keys(
                    naturalization_pass,
                    REQUIRED_NATURALIZATION_PASS,
                    "$.screenplay.naturalization_pass",
                )
            )
        else:
            errors.append("$.screenplay.naturalization_pass: must be an object")

        quality_gate = data["screenplay"].get("quality_gate")
        if isinstance(quality_gate, dict):
            errors.extend(require_keys(quality_gate, REQUIRED_QUALITY_GATE, "$.screenplay.quality_gate"))
            scores = quality_gate.get("scores")
            if isinstance(scores, dict):
                errors.extend(require_keys(scores, REQUIRED_QUALITY_SCORES, "$.screenplay.quality_gate.scores"))
            else:
                errors.append("$.screenplay.quality_gate.scores: must be an object")
        else:
            errors.append("$.screenplay.quality_gate: must be an object")

        realism_pass = data["screenplay"].get("realism_pass")
        if isinstance(realism_pass, dict):
            errors.extend(require_keys(realism_pass, REQUIRED_REALISM_PASS, "$.screenplay.realism_pass"))
        else:
            errors.append("$.screenplay.realism_pass: must be an object")

        motion_naturalness_pass = data["screenplay"].get("motion_naturalness_pass")
        if isinstance(motion_naturalness_pass, dict):
            errors.extend(
                require_keys(
                    motion_naturalness_pass,
                    REQUIRED_MOTION_NATURALNESS_PASS,
                    "$.screenplay.motion_naturalness_pass",
                )
            )
        else:
            errors.append("$.screenplay.motion_naturalness_pass: must be an object")

        shot_language_pass = data["screenplay"].get("shot_language_pass")
        if isinstance(shot_language_pass, dict):
            errors.extend(
                require_keys(
                    shot_language_pass,
                    REQUIRED_SHOT_LANGUAGE_PASS,
                    "$.screenplay.shot_language_pass",
                )
            )
        else:
            errors.append("$.screenplay.shot_language_pass: must be an object")

        performance_layer = data["screenplay"].get("performance_layer")
        if isinstance(performance_layer, dict):
            errors.extend(
                require_keys(
                    performance_layer,
                    REQUIRED_PERFORMANCE_LAYER,
                    "$.screenplay.performance_layer",
                )
            )
        else:
            errors.append("$.screenplay.performance_layer: must be an object")

        scene_continuity_check = data["screenplay"].get("scene_continuity_check")
        if isinstance(scene_continuity_check, dict):
            errors.extend(
                require_keys(
                    scene_continuity_check,
                    REQUIRED_SCENE_CONTINUITY_CHECK,
                    "$.screenplay.scene_continuity_check",
                )
            )
        else:
            errors.append("$.screenplay.scene_continuity_check: must be an object")
    else:
        errors.append("$.screenplay: must be an object")

    if isinstance(data.get("video_plan"), dict):
        errors.extend(require_keys(data["video_plan"], REQUIRED_VIDEO_PLAN, "$.video_plan"))
    else:
        errors.append("$.video_plan: must be an object")

    if isinstance(data.get("final_video"), dict):
        errors.extend(require_keys(data["final_video"], REQUIRED_FINAL_VIDEO, "$.final_video"))
        realism_review = data["final_video"].get("realism_review")
        if isinstance(realism_review, dict):
            errors.extend(require_keys(realism_review, REQUIRED_REALISM_REVIEW, "$.final_video.realism_review"))
            scores = realism_review.get("scores")
            if isinstance(scores, dict):
                errors.extend(
                    require_keys(scores, REQUIRED_REALISM_REVIEW_SCORES, "$.final_video.realism_review.scores")
                )
            else:
                errors.append("$.final_video.realism_review.scores: must be an object")
        else:
            errors.append("$.final_video.realism_review: must be an object")
    else:
        errors.append("$.final_video: must be an object")

    if isinstance(data.get("artifact_manifest"), dict):
        errors.extend(require_keys(data["artifact_manifest"], REQUIRED_ARTIFACT_MANIFEST, "$.artifact_manifest"))
    else:
        errors.append("$.artifact_manifest: must be an object")

    for key in ["character_designs", "scene_designs", "execution_log", "errors"]:
        if key in data and not isinstance(data[key], list):
            errors.append(f"$.{key}: must be a list")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.json_path.read_text(encoding="utf-8-sig"))
    except Exception as exc:  # noqa: BLE001
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("Root JSON value must be an object.", file=sys.stderr)
        return 2

    errors = validate(data)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Workflow JSON shape is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
