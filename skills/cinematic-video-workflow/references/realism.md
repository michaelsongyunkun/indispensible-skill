# Realism Reference

Use this reference when the workflow goal is more realistic video generation.

## Realism Pass Checklist

Translate abstract style words into concrete constraints:

- Physical: gravity, contact points, weight shift, believable acceleration/deceleration, object collisions, scale, and cause-effect movement.
- Motion: anticipation before movement, visible contact with surfaces, natural recovery after turns/jumps, no sliding, no floating, no sudden teleporting.
- Camera: motivated height, stable handheld limits, consistent screen direction, limited dramatic moves, plausible motion blur, focus behavior that tracks the subject.
- Lens: describe a lens feel only when useful, such as low floor-level phone camera, natural 35mm documentary feel, shallow depth of field, or wide establishing view.
- Light: one motivated key light, plausible fill, consistent shadow direction, exposure that does not flicker, color temperature tied to time/place.
- Texture: fur clumping, cloth wrinkles, floor grain, dust, fingerprints, scuffs, dampness, reflection, and surface imperfections where relevant.
- Environment: background sound, air movement, practical clutter, occlusion, and object placement that support scale.

## Prompt Strategy

Prefer:

- Specific subjects with locked visual traits.
- Specific location and light direction.
- One or two clear actions per shot.
- Cause-effect chains: trigger, anticipation, action, reaction, settle.
- Concrete camera position and movement.
- Negative constraints targeted to the known risks.

Avoid:

- Many unrelated actions in a short duration.
- Overly broad words such as beautiful, cinematic, realistic, premium without concrete support.
- Impossible camera geography.
- Conflicting lighting or time-of-day language.
- Unnecessary subtitles, labels, logos, or extra subjects.

## Vidu Strategy

For Vidu `.com`, prefer the REST API if CLI submit endpoints return 404:

- Submit: `POST https://api.vidu.com/ent/v2/text2video`
- Query: `GET https://api.vidu.com/ent/v2/tasks/{task_id}/creations`
- Auth header: `Authorization: Token <VIDU_TOKEN>`

Default realistic settings when not otherwise specified:

- `model`: `viduq3-turbo`
- `style`: `general`
- `movement_amplitude`: `auto`
- `resolution`: `720p` for quick drafts, higher only if available and requested
- `audio`: `true` when natural ambient sound is useful
- `aspect_ratio`: follow the brief exactly

Use shot-level generation when:

- The story has multiple locations or major action changes.
- Character identity drifts in whole-video generation.
- Motion becomes unnatural because the prompt contains too many actions.
- The user wants a more controlled final edit.

Use whole-video generation when:

- Duration is short.
- There is one location and one simple action chain.
- The prompt can be expressed as a clear beginning, middle, and ending.

## Realism Review

After generation, inspect these risks:

- Subject identity changes.
- Sliding paws/feet or floating bodies.
- Broken joints, extra limbs, distorted anatomy.
- Scale changes between subjects and props.
- Light direction changes or flickering exposure.
- Camera teleports or unmotivated rapid movement.
- Background objects moving without cause.
- Material texture that looks plastic or over-smoothed.

When retrying, do not rewrite everything. Preserve successful elements and target the failure:

```text
Preserve the warm living room, orange-and-white kitten, cream puppy, red yarn ball, and low floor camera. Fix the previous issue: the puppy's paws slid during the chase. Make every paw contact visible, keep natural puppy gait, reduce speed, and let the puppy settle before lying down.
```
