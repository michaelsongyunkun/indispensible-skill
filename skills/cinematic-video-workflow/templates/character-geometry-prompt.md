# Character Geometry Prompt Template

Use with `$character-geometry-generator` when available. If unavailable, store the filled prompt in `character_designs[].geometry_prompt`.

```text
Create a character geometry sheet / turnaround for video consistency.

Character ID: {{character_id}}
Name: {{name}}
Project style: {{style}}
Aspect ratio target: {{aspect_ratio}}
Role in story: {{role}}

Locked visual traits:
- Face: {{face}}
- Body proportion: {{body}}
- Hair: {{hair}}
- Wardrobe: {{wardrobe}}
- Color palette: {{palette}}
- Props: {{props}}
- Posture and movement traits: {{posture}}

Required views:
- Front view
- Side view
- Back view
- 3/4 view if possible

Image requirements:
- Full body, neutral standing pose, consistent proportions across views.
- Clear clothing silhouette, hairstyle, accessories, and key props.
- Clean readable lighting, plain background, no dramatic camera distortion.
- Preserve the same identity in every view.

Negative constraints:
- Do not redesign clothing, age, body type, hairstyle, or color palette.
- Do not add unrelated props, extra characters, logos, or text labels unless requested.
```
