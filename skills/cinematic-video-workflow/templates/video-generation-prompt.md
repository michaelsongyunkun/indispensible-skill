# Video Generation Prompt Template

Use with `$vidu-skills`.

```text
Generate a complete short video using the locked screenplay, character designs, scene designs, and style constraints.

Project: {{project_name}}
Duration: {{duration}}
Aspect ratio: {{aspect_ratio}}
Visual style: {{style}}
Language: {{language}}
Consistency priority: {{consistency_priority}}

Global story summary:
{{summary}}

Locked character references:
{{character_designs}}

Locked scene references:
{{scene_designs}}

Realism constraints:
{{realism_pass}}

Motion naturalness constraints:
{{motion_naturalness_pass}}

Shot plan:
{{shot_prompts}}

Global generation guidance:
- Preserve character identity, clothing, body proportion, hairstyle, props, and performance traits across shots.
- Preserve scene layout, light direction, key object placement, and camera geography.
- Follow the screenplay beats and shot durations.
- Make the result feel photographed in a real space: motivated light source, consistent shadows, plausible exposure, natural texture, contact shadows, and stable scale.
- Keep motion readable and cinematic; avoid random cuts or unmotivated changes.
- Follow the motion naturalness pass: every movement needs cause, anticipation, main action, reaction, and settle.
- For animals and non-human characters, preserve species-appropriate gait, weight shift, paw/foot contact, head/ear/tail reactions, and recovery after turns or jumps.
- Use realistic camera behavior: grounded camera height, limited handheld drift, plausible motion blur, natural focus behavior, and no sudden camera teleporting.
- Keep actions simple enough for the duration; prefer one clean action chain over many unrelated beats.
- Follow the shot language fields for framing, angle, camera movement, visual emphasis, and transition logic.
- Follow performance notes for intention, micro-expression, line rhythm, physical tension, and prop/space interaction.
- Respect the continuity map for entrances, exits, eyelines, screen direction, object placement, and light direction.
- Use the provided character geometry and scene geometry references whenever supported.

Negative prompt:
inconsistent faces, redesigned clothes, changing hairstyle, extra characters, wrong location layout, unstable camera geography, unreadable hands, distorted body, flickering identity, floating bodies, sliding feet or paws, broken joints, extra limbs, inconsistent scale, physics-defying jumps, random speed changes, unmotivated camera motion, exposure flicker, changing light direction, plastic texture, over-smoothed fur or skin, warped reflections, background objects moving without cause, random text, watermark, logo, subtitles unless requested
```
