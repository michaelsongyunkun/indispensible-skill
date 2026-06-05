# Example 2: Ad Short

User request:

```text
Use $cinematic-video-workflow to make a 30-second ad-style short for a smart thermos. It should feel warm, premium, and family-oriented. 16:9, Chinese, full workflow.
```

Expected workflow behavior:

1. Ask a concise question only if brand claims, logo use, or product facts are required. Otherwise state assumptions.
2. Invoke `$screenplay-writer` for a restrained product story rather than a slogan-heavy ad.
3. Extract product hero object as a key prop in character and scene continuity notes.
4. Generate character geometry prompts for parent/child or other visible characters.
5. Generate scene geometry prompts for kitchen, morning commute, or classroom depending on the screenplay.
6. Build Vidu prompts with locked product appearance, color, material, and placement.

Special checks:

- Avoid unsupported product claims.
- Keep the product visually consistent across shots.
- Include audio notes for soft domestic sound design and optional voiceover.
- Prefer shot-level generation if the product must remain visually identical.
