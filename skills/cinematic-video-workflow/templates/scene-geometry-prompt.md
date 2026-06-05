# Scene Geometry Prompt Template

Use with `$scene-geometry-generator` when available. If unavailable, store the filled prompt in `scene_designs[].geometry_prompt`.

```text
Create a scene geometry layout / spatial design sheet for video consistency.

Scene ID: {{scene_id}}
Scene name: {{scene_name}}
Project style: {{style}}
Aspect ratio target: {{aspect_ratio}}

Scene description:
{{description}}

Locked spatial traits:
- Location: {{location}}
- Overall layout: {{layout}}
- Foreground: {{foreground}}
- Midground: {{midground}}
- Background: {{background}}
- Key objects and positions: {{key_objects}}
- Character movement zones: {{movement_zones}}
- Camera positions: {{camera_positions}}
- Light direction: {{lighting}}
- Atmosphere: {{atmosphere}}

Required output:
- Overall composition view.
- Floor-plan-like layout or clear spatial structure.
- Key object placement.
- Possible camera positions and shot angles.
- Light source direction.
- Notes that clarify mood and spatial logic.

Negative constraints:
- Do not change the location identity or key object positions.
- Do not add unrelated major set pieces.
- Avoid ambiguous scale or impossible camera blocking.
```
