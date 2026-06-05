# Extraction Strategy

Use this reference when the generic crawler produces sparse or noisy records.

## Structure Detection

Prefer stable, repeated page patterns over visual guesses:

- Same-host links with similar URL shapes often identify detail pages.
- Repeated containers with headings, links, descriptions, and price-like text often identify list cards.
- `rel=next`, anchor text such as `next`, and incrementing `page` query parameters often identify pagination.
- JSON-LD blocks with `Product`, `Offer`, `Article`, `ItemList`, or `WebPage` can provide cleaner fields than visible HTML.

Run `--inspect` on unfamiliar sites before crawling broadly. Use its `top_container_paths`, `sample_records`, `next_pages`, and JSON-LD counts to decide whether the default heuristic is sufficient.

Run `--suggest-config` when a page appears to have repeated cards but no selector config yet. Treat the output as a starter: tighten `list_item`, then field selectors, then pagination.

## Selector Configs

Use a JSON or simple YAML config when the site exposes stable classes or attributes. Keep selectors conservative:

```yaml
selectors:
  list_item: ".product-card"
  title: "h2, .title"
  link: "a"
  price: ".price, [itemprop=price]"
  summary: ".description"
  next_page: "a[rel=next], .pagination .next"
fields:
  image:
    selector: "img"
    attr: "src"
    type: "url"
  tags:
    selector: ".tag, .category"
    type: "list"
    multiple: true
  date:
    selector: "time"
    attr: "datetime"
    type: "date"
cleaning:
  title:
    - remove_site_suffix
```

Supported selector syntax is tag names, `.class`, `#id`, `[attr]`, `[attr=value]`, comma-separated alternatives, and descendant selectors. If config output is noisy, tighten `list_item` before changing field selectors.

Use `fields` for non-default fields or attribute extraction. Common field types are `text`, `url`, `date`, `money`, and `list`. Use `multiple: true` for tags, categories, gallery images, or repeated facts.

## Detail Pages

Enable same-host detail crawling when list pages omit important fields:

```json
{
  "detail": {
    "enabled": true,
    "max_pages": 20,
    "selectors": {
      "summary": ".product-description",
      "brand": ".brand",
      "sku": "[itemprop=sku]"
    }
  }
}
```

Keep detail limits modest. Prefer detail crawling for fields that are genuinely absent from list pages, not for re-reading values already available.

## Field Fallbacks

Use conservative fallback chains:

- `title`: `h1`, `h2`, anchor text, `<title>`, `og:title`
- `link`: detail anchor, canonical URL, current page URL
- `project_name`: product/name labels, heading, title
- `price`: configured selector, `[itemprop=price]`, currency text, nearby offer text
- `summary`: meta description, card paragraph, first descriptive sentence

Do not invent missing values. Leave missing fields blank and report field coverage.

## Cleaning

Normalize whitespace, decode HTML entities, resolve relative URLs, remove duplicate rows, and keep source URLs. Deduplicate by canonical link first, then by normalized `(project_name or title, price)` when links are missing.

Built-in cleaners:

- `normalize_whitespace`: collapse repeated whitespace.
- `remove_site_suffix`: remove trailing site names such as `Title | Site`.
- `parse_money`: keep the numeric money portion.
- `lower` / `upper`: normalize case.
- `{remove_suffix: "..."}`: remove a fixed suffix.
- `{replace: {old: "...", new: "..."}}`: replace fixed text.

Default type cleaning resolves `url` fields, normalizes simple dates to `YYYY-MM-DD`, and joins list fields with `; `.

## Error Handling

Record per-URL errors without stopping the whole crawl. Include HTTP status, content type, elapsed time, timeout, robots decisions, parsing failures, skipped duplicate URLs, raw record count, deduped count, configured selectors, and field coverage percentages in the report.

## Anti-Blocking Etiquette

Use a descriptive user agent, low concurrency, retries with backoff, and clear limits. Avoid identity rotation, CAPTCHA solving, login bypasses, and other evasion tactics.
