---
name: cinematic-video-workflow
description: Orchestrate a complete short-video production workflow from idea to screenplay, character geometry, scene geometry, and Vidu video generation. Use when the user asks to create a cinematic short video, micro-film, ad, animated short, storyboard-to-video workflow, character-consistent video, scene-consistent video, or an end-to-end process from script to character sheets to scene layouts to final video.
---

# Cinematic Video Workflow

Use this skill as a coordinator, not as a replacement for specialist skills. It receives a short-video brief, invokes screenplay and visual-generation sub-skills in order, manages intermediate artifacts, preserves character and scene consistency, and prepares or executes final Vidu generation.

## Dependencies

Required existing skills:

- `$screenplay-writer`: write or refine the screenplay, shot breakdown, characters, scenes, dialogue, emotion, and duration.
- `$vidu-skills`: generate video or image-to-video outputs with Vidu CLI/API.

Pluggable reserved skills:

- `$character-geometry-generator`: reserved interface for character geometry sheets and turnarounds. If unavailable, create structured prompts and mark generation as pending.
- `$scene-geometry-generator`: reserved interface for scene layout and spatial geometry views. If unavailable, create structured prompts and mark generation as pending.

Load only the references needed for the current task:

- `references/schema.md`: canonical output JSON schema and field rules.
- `references/subskill-interfaces.md`: expected handoff contracts for screenplay, geometry, and Vidu sub-skills.
- `references/error-handling.md`: failure logging and retry guidance.
- `references/persistence.md`: project-run artifact saving rules for briefs, scripts, prompts, task results, and output files.
- `references/realism.md`: realism rules for physical motion, camera behavior, lighting, texture, Vidu settings, and post-generation review.

Use templates as prompt sources:

- `templates/screenplay-prompt.md`
- `templates/character-geometry-prompt.md`
- `templates/scene-geometry-prompt.md`
- `templates/video-generation-prompt.md`

## Inputs

Normalize the user brief into these parameters:

- `idea`: required video concept or theme.
- `genre`: short drama, micro-film, ad, animation, narrative film, promo, or similar.
- `duration`: target duration such as 30s, 60s, or 90s.
- `aspect_ratio`: `16:9`, `9:16`, or `1:1`.
- `style`: visual style such as realistic, cinematic, anime, cyberpunk, warm, suspenseful.
- `audience`: optional target audience.
- `characters`: optional user-provided character constraints.
- `setting`: optional user-provided scene or location constraints.
- `language`: output language.
- `output_mode`: `screenplay_only`, `screenplay_plus_geometry`, or `full_video`.
- `consistency_priority`: boolean; default `true` for video workflows.

If important inputs are missing, infer safe defaults and state them. Ask at most 1-3 concise questions only when missing information would materially change the result, such as brand restrictions, exact product claims, real-person likeness permissions, or required duration/platform constraints.

## Workflow

1. Receive the brief and check missing information.
2. Invoke `$screenplay-writer` with the normalized brief and screenplay template. Require a complete screenplay with title, summary, character list, scene list, shot list, visual descriptions, actions, dialogue or voiceover, emotional tone, and duration suggestions.
3. Run the Natural Description Pass. Polish environment descriptions and character actions so they feel observable, motivated, and shootable while preserving plot, dialogue meaning, shot IDs, duration, and locked character/scene facts.
4. Run the Script Quality Gate. Score and fix the hook, pacing, character motivation, dialogue economy, and shootability before downstream work.
5. Run the Realism Pass. Add concrete physical, optical, material, lighting, environmental, and lens constraints that make the result feel photographed rather than generated.
6. Run the Motion Naturalness Pass. Make every visible action physically plausible, motivated, and readable for the character species/body type.
7. Run the Shot Language Pass. Add shot size, camera angle, camera movement, lens/visual emphasis, transition logic, and camera motivation for each shot.
8. Run the Performance Layer. Add playable acting beats: intention, external action, micro-expression, line delivery rhythm, physical tension, and prop/space interaction.
9. Run the Scene Continuity Check. Verify object placement, light direction, entrances/exits, screen direction, character positions, and cross-shot spatial logic.
10. Parse the improved screenplay into structured `characters`, `scenes`, and `shots`. Preserve IDs for traceability, such as `char_01`, `scene_01`, and `shot_001`.
11. Generate character design records and character geometry prompts for each major character.
12. Invoke `$character-geometry-generator` when available. If unavailable, leave `output_ref` empty or `pending` and record a warning in `errors`.
13. Generate scene design records and scene geometry prompts for each major scene.
14. Invoke `$scene-geometry-generator` when available. If unavailable, leave `output_ref` empty or `pending` and record a warning in `errors`.
15. Lock the screenplay, character bible, scene bible, geometry outputs, aspect ratio, duration, style, realism constraints, and motion constraints as the consistency package.
16. Invoke `$vidu-skills` for final generation. Prefer shot-level generation and assembly when the workflow needs strong control; use whole-video generation only when Vidu supports the requested duration and style in one pass. For Vidu `.com`, prefer the current REST API when CLI submit endpoints return 404.
17. Run the Realism Review after generation when media is available. Check identity consistency, believable motion, lighting continuity, camera stability, material texture, anatomy, scale, and scene geography. If flaws are material, output a targeted retry prompt.
18. Save the workflow run artifacts when the user asks to save changes or when a video is generated in a local project. Use `scripts/save_workflow_run.py` when a structured JSON result is available.
19. Return structured JSON plus a concise execution log with called skills, input summaries, output summaries, failure steps, and retry suggestions.

## Output Modes

- `screenplay_only`: continue through Step 9, then output `screenplay`, logs, and any assumptions.
- `screenplay_plus_geometry`: continue through Step 15 and output `screenplay`, `character_designs`, `scene_designs`, `video_plan`, and logs.
- `full_video`: execute the complete workflow through Step 19.

## Natural Description Pass

Before extracting geometry or generating video prompts, revise the screenplay for natural environment and action writing:

- Environment descriptions should be grounded in visible details, sound, light, weather, object placement, texture, and spatial relationships. Avoid generic mood labels unless they are tied to something the camera or microphone can capture.
- Character actions should reveal intention through small physical choices, rhythm, hesitation, gaze, breath, hand movement, posture shifts, interaction with props, and movement through space. Avoid abstract verbs like "feels", "realizes", or "is sad" unless paired with visible behavior.
- Keep motion causality clear: each action should have a reason, reaction, or emotional pressure from the previous beat. Do not stack unrelated gestures just to make the shot busy.
- Preserve continuity with locked character traits and scene layouts. If polishing exposes a continuity problem, fix the smallest local description and record it in `naturalization_pass.notes`.
- Keep descriptions concise enough for production and video prompts. Prefer one precise sensory detail over three ornamental adjectives.
- Do not rewrite the plot, add new characters, change product claims, alter dialogue intent, or change timing unless the user explicitly asks.

Record the pass in `screenplay.naturalization_pass` with `status`, `environment_changes`, `action_changes`, and `notes`.

## Realism Pass

Before geometry and video generation, convert broad style requests such as "realistic", "cinematic", "premium", or "natural" into concrete constraints:

- Physical realism: gravity, weight transfer, contact shadows, object collision, scale, plausible speed, and cause-effect motion.
- Optical realism: lens height, focal length feel, depth of field, exposure, motion blur, rolling handheld limits, and focus behavior.
- Lighting realism: one primary light direction, motivated fill, shadow softness, reflection behavior, time of day, and consistent color temperature.
- Material realism: fur, skin, cloth, metal, glass, paper, food, liquids, dust, fingerprints, floor texture, and prop wear should react to light plausibly.
- Environmental realism: background sound, air movement, practical clutter, surface imperfections, and spatial occlusion should support the setting without distracting.
- Generation realism: prefer fewer clean actions, stable camera geography, specific subject descriptions, concrete negatives, and shot-level generation when whole-video prompts cause identity or motion drift.

Record this in `screenplay.realism_pass` with `status`, `physical_constraints`, `optical_constraints`, `lighting_constraints`, `material_constraints`, `environment_constraints`, and `generation_constraints`.

## Motion Naturalness Pass

Before generating video prompts, make character motion physically plausible and emotionally motivated:

- Break actions into cause, anticipation, main action, reaction, and settle. For animals, include weight shift, paw placement, head turn, tail/ear response, speed change, and recovery after jumps or turns.
- Keep movement within species/body constraints. Avoid human-like gestures for animals, impossible acceleration, floating, sliding, limb warping, or sudden teleporting between positions.
- Tie every movement to a visible trigger: sound, object motion, another character's gaze, obstacle, curiosity, fear, play, fatigue, or attraction to light/food/props.
- Prefer one clean readable action per shot for very short videos. If several actions are needed, chain them through a prop, eyeline, or sound cue.
- Add video negative constraints for unnatural motion: floating bodies, sliding feet/paws, extra limbs, broken joints, inconsistent scale, physics-defying jumps, random speed changes, and unmotivated camera motion.

Record this in `screenplay.motion_naturalness_pass` with `status`, `motion_rules`, `fixed_actions`, and `negative_motion_constraints`.

## Script Quality Gate

Before extracting structure, evaluate whether the screenplay is strong enough to generate:

- Hook: the first 3 seconds create a clear visual, question, conflict, or promise.
- Pacing: every 8-12 seconds contains new information, emotional pressure, action choice, or visual escalation.
- Motivation: each major action follows from a character goal, fear, obstacle, or reaction.
- Dialogue economy: lines reveal conflict, decision, relationship, or subtext; remove explanatory filler.
- Shootability: every beat can be expressed by camera, performance, sound, or edit.

If a check fails, revise the smallest relevant beat and record the result in `screenplay.quality_gate`. Use a 1-5 score per check, with `revision_notes` explaining only material fixes.

## Shot Language Pass

For each shot, add cinematic direction without overloading the video prompt:

- `shot_size`: close-up, medium, wide, insert, over-the-shoulder, POV, or another clear framing.
- `camera_angle`: eye-level, low angle, high angle, profile, three-quarter, top-down, or motivated variant.
- `camera_movement`: locked-off, slow push-in, handheld follow, pan, tilt, dolly, tracking, or motivated stillness.
- `visual_emphasis`: what the viewer should notice first.
- `transition`: why the next shot follows, such as action match, eyeline match, sound bridge, reveal, or contrast.

Camera choices should serve story clarity and emotion. Do not add dramatic camera moves unless they make the beat easier to understand or feel.

## Performance Layer

For important character beats, add actor-playable performance notes:

- `intention`: what the character wants in the moment.
- `outer_action`: what the audience can see them do.
- `micro_expression`: one or two subtle face/eye/breath details when useful.
- `delivery`: pace, pause, volume, restraint, or interruption for dialogue/voiceover.
- `physical_tension`: posture, hand behavior, stillness, distance, or release.
- `space_or_prop_interaction`: how the character uses nearby objects or movement zones.

Performance notes must support the existing action. Avoid adding gestures that contradict locked character traits or continuity.

## Scene Continuity Check

Before geometry generation, create a compact continuity map:

- Track doors, windows, furniture, props, light direction, and important background elements.
- Track where each character starts, moves, exits, and looks within each scene.
- Preserve screen direction and camera geography unless a deliberate disorientation is requested.
- Check that repeated props and wardrobe details stay stable across shots.
- If a continuity issue appears, fix the smallest local description and record it in `screenplay.scene_continuity_check.issues`.

## Realism Review

After video generation, inspect the returned media when possible. If a browser/video inspection tool is available, sample the opening, midpoint, and ending frames. Otherwise use the generation result and known prompt risks.

Score 1-5:

- Subject identity consistency.
- Motion believability.
- Lighting and shadow continuity.
- Camera/lens naturalness.
- Material and texture realism.
- Anatomy/scale correctness.
- Scene geography stability.

If any critical score is below 4, produce `final_video.realism_review.retry_prompt` with targeted fixes rather than a generic rerun. The retry prompt should mention the exact flaw to correct and preserve the successful parts.

## Artifact Persistence

When working inside a local project, save a resumable workflow run if the user asks to save, asks for traceability, or a video/image asset is generated:

- Default directory: `workflow_runs/<YYYY-MM-DD>-<slug>/` under the current project/workspace.
- Save `brief.json`, `screenplay.json`, `video_plan.json`, `workflow-result.json`, `execution-log.json`, and `README.md` when the data exists.
- Save or copy final media into the same run folder when possible; if the media is already elsewhere, record the absolute path in `artifact_manifest.files`.
- Never save API keys, bearer tokens, signed request headers, or secrets. Redact sensitive query strings in logs unless the URL is itself the deliverable and needed temporarily for download.
- Add `artifact_manifest` to the final JSON with run directory, saved files, external refs, and skipped artifacts.

Use `scripts/save_workflow_run.py <workflow-result.json> --project-dir <dir> --slug <slug>` when a structured result file is available. If not, create the same file structure manually from available artifacts.

## Consistency Management

After the screenplay is accepted or reasonably finalized, lock the following as the source of truth:

- Character identity: name, age range, body proportion, face, hair, clothing, palette, props, posture, and performance notes.
- Scene identity: location, spatial layout, foreground/midground/background, object placement, lighting direction, atmosphere, camera positions, and movement zones.
- Visual style: medium, lens language, color palette, texture, motion style, and negative constraints.

Do not silently redesign characters or scenes later. If a later step requires changes, record the change in the log and update dependent prompts consistently.

## Geometry Requirements

Character geometry sheets exist to preserve visual continuity during video generation. Each prompt should request front view, side view, back view, optional 3/4 view, body proportion, clothing, hairstyle, color palette, props, posture traits, and neutral readable lighting.

Scene geometry layouts exist to preserve spatial logic and stable camera blocking. Each prompt should request overall composition, floor-plan-like spatial layout, foreground/midground/background, key object positions, character movement zones, camera positions, light direction, and atmosphere notes.

## Error Handling

Never fail silently. For each failed step, add an `errors[]` entry with `step`, `skill`, `reason`, `impact`, and `retry_suggestion`. Continue with the best available structured artifact when possible. If a generation sub-skill is unavailable, output the prompt and mark the generation result as `pending`.

## Final Response

Return the canonical JSON object described in `references/schema.md`. If the user does not need raw JSON, include a compact human summary before or after the JSON, but keep the JSON complete enough for the next agent or tool to resume the workflow.

## Examples

See:

- `examples/01-drama-short.md`
- `examples/02-ad-short.md`
- `examples/03-animation-short.md`
