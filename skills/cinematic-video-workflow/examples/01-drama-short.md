# Example 1: Drama Short

User request:

```text
Use $cinematic-video-workflow to create a 60-second vertical short drama about a delivery rider who is late but secretly helped the customer's mother. Output full video workflow in Chinese, cinematic realistic style.
```

Expected workflow behavior:

1. Normalize input:
   - `genre`: short drama
   - `duration`: 60s
   - `aspect_ratio`: 9:16
   - `style`: cinematic realistic
   - `language`: Chinese
   - `output_mode`: full_video
   - `consistency_priority`: true
2. Invoke `$screenplay-writer` for the screenplay and shot breakdown.
3. Extract the customer, delivery rider, and mother if visible or voice-only.
4. Create character geometry prompts for visible characters.
5. Create scene geometry prompts for apartment doorway, stairwell, and phone close-up context.
6. Invoke geometry sub-skills when available; otherwise mark geometry outputs as pending.
7. Build Vidu global and shot-level prompts.
8. Invoke `$vidu-skills` or return ready-to-run Vidu prompts if execution is unavailable.

Output should include:

- `screenplay.title`
- `screenplay.shots[]` with 3-second hook and 8-12 second rhythm.
- `character_designs[]` for consistent clothing, face, body, and props.
- `scene_designs[]` for stairwell/apartment layout and lighting.
- `video_plan.shot_prompts[]`
- `final_video.status`
