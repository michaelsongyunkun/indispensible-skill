# Example 3: Animated Short

User request:

```text
Use $cinematic-video-workflow to create a 90-second animated short about a lonely moon mechanic who repairs broken stars. 1:1, poetic but clear, no dialogue, screenplay plus geometry only.
```

Expected workflow behavior:

1. Normalize:
   - `genre`: animated short
   - `duration`: 90s
   - `aspect_ratio`: 1:1
   - `style`: poetic animation
   - `language`: Chinese
   - `output_mode`: screenplay_plus_geometry
2. Invoke `$screenplay-writer` and request visual storytelling without dialogue.
3. Extract the moon mechanic and any recurring companion/object as character or prop designs.
4. Generate character geometry prompt emphasizing silhouette, proportions, tools, outfit, and movement.
5. Generate scene geometry prompts for moon workshop, star field, ladder/rail system, and light direction.
6. Stop before Vidu generation and set `final_video.status` to `not_requested`.

Output should include:

- Complete screenplay and shot list.
- Character and scene geometry prompts.
- `video_plan` ready for future Vidu execution.
- Execution log showing video generation was intentionally skipped.
