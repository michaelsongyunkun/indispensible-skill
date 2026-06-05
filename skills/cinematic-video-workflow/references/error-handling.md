# Error Handling

Record every failed or skipped dependency in `execution_log` and `errors`.

## Non-Fatal Failures

Continue when:

- A pluggable geometry skill is unavailable.
- A geometry generation call fails but the prompt was produced.
- Video generation is not requested by `output_mode`.
- The user asked for only screenplay or intermediate artifacts.

Set the relevant artifact `status` to `pending` or `failed`, and include retry guidance.

## Fatal Failures

Stop and return partial output when:

- No usable `idea` can be inferred.
- The screenplay cannot be generated or parsed enough to identify shots.
- Required safety, legal, brand, or real-person constraints are missing and cannot be safely assumed.
- Vidu generation fails after the user requested `full_video` and no usable output reference exists.

## Retry Suggestions

Make retry advice specific:

- For screenplay failure: suggest tightening genre, duration, protagonist, conflict, or ending.
- For character ambiguity: suggest age range, face/hair/clothing, body type, key props, and reference style.
- For scene ambiguity: suggest location, layout, time of day, key objects, and lighting.
- For video failure: suggest reducing duration, generating shot-by-shot, simplifying motion, adding image references, or changing aspect ratio.
