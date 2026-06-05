# Output Schema

Use this schema unless the user provides custom fields.

## Note-Level Fields

| Field | Type | Description |
| --- | --- | --- |
| `note_id` | string | Feed/note ID |
| `note_url` | string | Canonical note URL if available |
| `xsec_token` | string | Token needed for detail calls; keep out of public reports if sensitive |
| `keyword` | string | Search keyword/theme used |
| `title` | string | Note title |
| `body_text` | string | Note body or description |
| `author_name` | string | Visible author name |
| `author_id` | string | User ID if available |
| `publish_time` | string | Platform publish time if available |
| `likes` | number/string | Like count |
| `favorites` | number/string | Favorite/save count |
| `comments_count` | number/string | Comment count |
| `shares` | number/string | Share count |
| `comment_summary` | string | Optional summary of collected comments |

## Image-Level Fields

| Field | Type | Description |
| --- | --- | --- |
| `image_id` | string | Stable image ID or index |
| `image_url` | string | Source image URL |
| `image_path` | string | Local cached path if downloaded/provided |
| `ocr_text` | string | Text visible in the image |
| `products` | list/string | Product or service names |
| `brands` | list/string | Brand names or logos |
| `prices` | list/string | Price, discount, package, coupon, or fee text |
| `locations` | list/string | City, venue, school, store, route, or address clues |
| `scene` | string | Situation shown, such as dorm, cafe, classroom, wardrobe |
| `style_tags` | list/string | Visual or content style tags |
| `objects` | list/string | Important visible objects |
| `pain_points` | list/string | User problems implied by text/visuals |
| `selling_points` | list/string | Claimed benefits or hooks |
| `audience` | string | Intended audience, if inferable from evidence |
| `evidence` | string | Short source-grounded explanation |
| `confidence` | number | 0.0 to 1.0 confidence for image extraction |

## Extraction Rules

- Prefer exact OCR text for names, prices, locations, and claims.
- Use `unknown` for missing or ambiguous facts.
- Keep visual inference separate from note text and comments.
- Do not infer sensitive attributes about people in images.
- For CSV, join list values with `; `.
