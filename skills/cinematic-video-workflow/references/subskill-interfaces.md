# Sub-Skill Interfaces

Use these contracts when handing work to specialist skills.

## Screenplay Writer

Invoke `$screenplay-writer` with:

- Normalized user input.
- Output mode: complete screenplay plus shot breakdown.
- Requirements: title, summary, character list, scene list, shot list, visual descriptions, character actions, dialogue/voiceover, emotion, duration.
- Language: match `user_input.language`.

Expected return:

- Full screenplay text.
- Extractable characters, scenes, and shots.
- Assumptions or safety notes when relevant.

## Character Geometry Generator

Reserved skill name: `$character-geometry-generator`.

If available, invoke once per major character or as a batch, depending on the tool. Input:

- Character ID and name.
- Visual description and locked traits.
- Requested views: front, side, back, optional 3/4.
- Neutral pose and consistent lighting.
- Style and aspect ratio constraints.
- Negative constraints that prevent redesign.

Expected return:

- Image path, asset ID, job ID, or URL.
- Any warnings about visual ambiguity.

If unavailable, do not block the workflow. Store the prompt in `geometry_prompt`, set `output_ref` to `pending`, and continue.

## Scene Geometry Generator

Reserved skill name: `$scene-geometry-generator`.

If available, invoke once per major scene or as a batch. Input:

- Scene ID and scene name.
- Spatial description and locked traits.
- Overall composition.
- Floor-plan or layout guidance.
- Foreground, midground, background.
- Key object locations.
- Character movement zones.
- Camera position suggestions.
- Light direction and atmosphere.

Expected return:

- Image path, asset ID, job ID, or URL.
- Any warnings about unclear spatial logic.

If unavailable, store the prompt, set `output_ref` to `pending`, and continue.

## Vidu Skills

Invoke `$vidu-skills` after the consistency package exists.

Input:

- Screenplay text.
- Structured shots.
- Character geometry references and prompts.
- Scene geometry references and prompts.
- Global visual style.
- Aspect ratio and duration.
- Shot-level prompts when available.

Strategy:

- Prefer shot-level generation when character/scene consistency is important, duration is long, or the script has multiple locations.
- Use whole-video generation when the requested output is short, simple, and Vidu supports the requested control surface.
- If shot-level generation is used, request consistent reference usage, then assemble or provide assembly instructions.
- For Vidu `.com`, if `vidu-cli task submit` returns a 404 due to endpoint mismatch, use the official REST API instead:
  - Submit: `POST https://api.vidu.com/ent/v2/text2video`
  - Query: `GET https://api.vidu.com/ent/v2/tasks/{task_id}/creations`
  - Header: `Authorization: Token <VIDU_TOKEN>`
- Save non-secret metadata such as `task_id`, `model`, `duration`, `aspect_ratio`, `resolution`, `credits`, and local output path. Never save the API key or Authorization header.

Realism defaults for short text-to-video drafts:

- `model`: `viduq3-turbo`
- `style`: `general`
- `movement_amplitude`: `auto`
- `resolution`: `720p` unless the user requests a higher available resolution.
- Keep the prompt physically grounded: stable camera height, motivated light, contact shadows, realistic material texture, simple action chain, and targeted negative constraints.
