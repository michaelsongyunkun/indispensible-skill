# Canonical Output Schema

Return this object for every workflow run. Omit fields only when the user explicitly asks for a lightweight answer; otherwise keep empty arrays/strings so the next agent can resume.

```json
{
  "project_name": "",
  "user_input": {
    "idea": "",
    "genre": "",
    "duration": "",
    "aspect_ratio": "",
    "style": "",
    "audience": "",
    "characters": [],
    "setting": "",
    "language": "",
    "output_mode": "screenplay_only | screenplay_plus_geometry | full_video",
    "consistency_priority": true
  },
  "screenplay": {
    "title": "",
    "summary": "",
    "characters": [],
    "scenes": [],
    "shots": [],
    "naturalization_pass": {
      "status": "not_run | applied | skipped",
      "environment_changes": [],
      "action_changes": [],
      "notes": ""
    },
    "quality_gate": {
      "status": "not_run | passed | revised | failed",
      "scores": {
        "hook": 0,
        "pacing": 0,
        "motivation": 0,
        "dialogue_economy": 0,
        "shootability": 0
      },
      "issues": [],
      "revision_notes": ""
    },
    "realism_pass": {
      "status": "not_run | applied | skipped | revised",
      "physical_constraints": [],
      "optical_constraints": [],
      "lighting_constraints": [],
      "material_constraints": [],
      "environment_constraints": [],
      "generation_constraints": []
    },
    "motion_naturalness_pass": {
      "status": "not_run | applied | skipped | revised",
      "motion_rules": [],
      "fixed_actions": [],
      "negative_motion_constraints": []
    },
    "shot_language_pass": {
      "status": "not_run | applied | skipped",
      "coverage": [],
      "notes": ""
    },
    "performance_layer": {
      "status": "not_run | applied | skipped",
      "character_beats": [],
      "notes": ""
    },
    "scene_continuity_check": {
      "status": "not_run | passed | revised | failed",
      "continuity_map": [],
      "issues": [],
      "notes": ""
    }
  },
  "character_designs": [
    {
      "id": "char_01",
      "name": "",
      "description": "",
      "locked_traits": {
        "face": "",
        "body": "",
        "hair": "",
        "wardrobe": "",
        "palette": "",
        "props": "",
        "posture": ""
      },
      "geometry_prompt": "",
      "output_ref": "",
      "status": "pending | generated | failed"
    }
  ],
  "scene_designs": [
    {
      "id": "scene_01",
      "scene_name": "",
      "description": "",
      "locked_traits": {
        "location": "",
        "layout": "",
        "foreground": "",
        "midground": "",
        "background": "",
        "key_objects": "",
        "lighting": "",
        "camera_positions": "",
        "atmosphere": ""
      },
      "geometry_prompt": "",
      "output_ref": "",
      "status": "pending | generated | failed"
    }
  ],
  "video_plan": {
    "global_prompt": "",
    "shot_prompts": [],
    "transitions": [],
    "audio_notes": ""
  },
  "final_video": {
    "status": "not_requested | pending | generated | failed",
    "output_ref": "",
    "notes": "",
    "realism_review": {
      "status": "not_run | passed | retry_recommended | failed",
      "scores": {
        "identity_consistency": 0,
        "motion_believability": 0,
        "lighting_continuity": 0,
        "camera_naturalness": 0,
        "material_texture_realism": 0,
        "anatomy_scale_correctness": 0,
        "scene_geography_stability": 0
      },
      "issues": [],
      "successful_elements": [],
      "retry_prompt": ""
    }
  },
  "artifact_manifest": {
    "run_dir": "",
    "files": [],
    "external_refs": [],
    "skipped": []
  },
  "execution_log": [
    {
      "step": "",
      "skill": "",
      "input_summary": "",
      "output_summary": "",
      "status": "success | skipped | warning | failed"
    }
  ],
  "errors": [
    {
      "step": "",
      "skill": "",
      "reason": "",
      "impact": "",
      "retry_suggestion": ""
    }
  ]
}
```

## Field Rules

- Keep `id` values stable once created.
- Keep `locked_traits` consistent across all downstream prompts.
- `output_ref` may be a local file path, generated asset ID, API job ID, URL, or `pending`.
- `shots[]` should preserve screenplay fields and may include `shot_language`, `performance_notes`, and `continuity_notes`.
- `shot_prompts[]` should include `shot_id`, `duration`, `scene_id`, `characters`, `prompt`, `negative_prompt`, `references`, and when available, `shot_language`, `performance_notes`, and `continuity_notes`.
- `screenplay.naturalization_pass` should summarize meaningful description changes without duplicating the entire screenplay.
- `screenplay.quality_gate.scores` uses 1-5 values after evaluation; use `0` only when the gate was not run.
- `screenplay.realism_pass` should convert style words into physical, optical, lighting, material, environmental, and generation constraints.
- `screenplay.realism_pass.generation_constraints[]` should feed directly into `video_plan.global_prompt`, `shot_prompts[]`, and negative prompts.
- `screenplay.motion_naturalness_pass.motion_rules[]` should state movement rules relevant to the characters, such as animal gait, object-triggered motion, and recovery after action.
- `screenplay.motion_naturalness_pass.fixed_actions[]` should describe any action beats revised for plausibility.
- `screenplay.motion_naturalness_pass.negative_motion_constraints[]` should feed directly into video prompts.
- `screenplay.shot_language_pass.coverage[]` should summarize per-shot camera decisions without duplicating full prompts.
- `screenplay.performance_layer.character_beats[]` should list only meaningful acting beats for major characters or turning points.
- `screenplay.scene_continuity_check.continuity_map[]` should track spatial facts needed by scene geometry and video generation.
- `artifact_manifest.files[]` should include `kind`, `path`, and `description` for saved local artifacts.
- `artifact_manifest.external_refs[]` should include non-secret task IDs, generated asset IDs, or final public media URLs when useful.
- `artifact_manifest.skipped[]` should explain expected artifacts that were not saved.
- `final_video.realism_review.scores` uses 1-5 values after generated media is inspected; use `0` only when review was not run.
- `final_video.realism_review.retry_prompt` should be specific and preserve successful elements.
- For `screenplay_only`, set `final_video.status` to `not_requested`.
- For missing pluggable geometry skills, set the related `status` to `pending` and add a non-fatal `errors[]` entry.
