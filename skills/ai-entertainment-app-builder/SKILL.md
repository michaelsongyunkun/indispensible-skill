---
name: ai-entertainment-app-builder
description: Build playful AI entertainment apps for Michael Song, including idol matching, personality tests, tarot/divination-style experiences, quiz engines, result cards, narrative scoring, and shareable lightweight web apps. Use when working on idol-match, tarot, qingqing/grassland personality, celebrity/persona matching, or quiz-based consumer apps.
---

# AI Entertainment App Builder

Use this skill for consumer-facing apps where the value is emotional resonance, playful interpretation, and polished result presentation. Make the app actually usable first, then make it delightful.

## Core Workflow

1. Define the fantasy: what the user hopes to learn, feel, compare, or share.
2. Define the interaction model: quiz, card draw, profile input, image/text input, matching, or generated reading.
3. Build the scoring/interpretation layer before visual polish.
4. Keep result logic explainable: show traits, evidence, match reasons, or score bands.
5. Create a result surface with title, summary, key traits, recommendation/match, and share/export affordance if useful.
6. Add content data as structured objects, not scattered copy in components.
7. Test deterministic logic: ties, missing answers, extreme scores, invalid inputs, and repeated runs.
8. Verify the main flow in browser and one compact/mobile viewport.

## Design Guidance

- Use a distinctive theme tied to the subject, not a generic SaaS dashboard.
- Avoid burying the quiz or draw interaction under a landing page.
- Keep text readable and emotionally specific.
- Make progress and completion states obvious.
- For idol/personality matching, distinguish "fun interpretation" from factual claims.
- For tarot/divination-style apps, present output as reflective entertainment, not medical, legal, or financial advice.

## Common Local Project Clues

Look for projects such as `idol-match-test`, `ai-idol-match-test-deploy`, `ai-tarot-sanctum`, and `qingqing-grassland-personality`.

Expected files often include `data/*`, `lib/*engine*`, `tests/*matcher*`, `tests/*quiz*`, `components/*`, and `app/page.tsx`.

## Verification Checklist

- Core flow works from start to result.
- Results are deterministic for the same inputs unless randomness is intentional.
- Result copy fits on mobile.
- No text overlaps cards/buttons.
- Test suite or focused logic tests pass.
- Browser screenshot or live check confirms the app is not blank.

