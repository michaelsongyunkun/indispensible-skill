---
name: web-crawler
description: Build and run compliant web crawlers for user-provided URLs. Use when Codex needs to inspect a website, infer list/detail/pagination structure, extract fields such as title, link, project name, price, and summary, clean and deduplicate records, handle missing fields and crawl errors, respect robots/compliance constraints, apply basic anti-blocking etiquette, and export results as CSV, Excel, and JSON.
---

# Web Crawler

## Overview

Use this skill to turn a website URL into structured data exports. Prefer the bundled script for common list/detail pages, add a selector config when the page has stable CSS classes, then customize parsing logic only when a site needs JavaScript rendering, strict rate limits, or domain-specific fields.

## Quick Start

Run the bundled crawler from this skill folder:

```bash
python scripts/crawl_site.py "https://example.com/products" --output ./crawl-output --max-pages 5 --delay 1
```

The script writes:

- `crawl-output.csv`
- `crawl-output.xlsx`
- `crawl-output.json`
- `crawl-output.report.json`

Use `--fields title,link,project_name,price,summary,image,tags,date` to control exported fields. When `--fields` is omitted, configured custom fields are added to the default fields. Use `--ignore-robots` only when the user explicitly confirms they have permission to crawl the target.

Preview extraction quality before crawling multiple pages:

```bash
python scripts/crawl_site.py "https://example.com/products" --inspect
```

Ask the script for a starter config:

```bash
python scripts/crawl_site.py "https://example.com/products" --suggest-config
```

Use a selector config when the generic heuristic is sparse or noisy:

```yaml
selectors:
  list_item: ".product-card"
  title: "h2, .title"
  link: "a"
  price: ".price"
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
cleaning:
  title:
    - remove_site_suffix
detail:
  enabled: false
  max_pages: 20
  selectors:
    summary: ".product-description"
    brand: ".brand"
```

Run it with:

```bash
python scripts/crawl_site.py "https://example.com/products" --config ./crawler-config.yaml --output ./products
```

## Workflow

1. Confirm the user's target URL and desired fields. If fields are unspecified, extract `title`, `link`, `project_name`, `price`, and `summary`, plus fields declared in config.
2. Check compliance before crawling. Inspect robots.txt where possible, mention rate limits and site terms, and avoid bypassing access controls, CAPTCHAs, paywalls, or login gates.
3. Fetch the start page with a descriptive user agent, retries, timeout, and a delay between requests.
4. Inspect structure before broad crawling when the site is unfamiliar. Use `--inspect` to review candidate records, pagination links, JSON-LD count, and repeated container paths.
5. Infer structure:
   - Detect repeated list cards by grouping links and text blocks with similar DOM paths.
   - Detect detail links by choosing same-host anchors with meaningful text and stable URL patterns.
   - Detect pagination from `rel=next`, `next` labels, page query parameters, or numbered page links.
6. Add a selector config when the page has reliable classes/attributes. Use `--suggest-config` for a starter, then tighten `list_item` first.
7. Extract fields with fallback order:
   - `title`: page title, card heading, anchor text, Open Graph title.
   - `link`: canonical absolute URL from card/detail anchor.
   - `project_name`: heading, product/name labels, title fallback.
   - `price`: currency-looking text, price labels, structured snippets.
   - `summary`: meta description, card paragraph, nearby descriptive text.
8. Enable detail crawling only when list pages omit important fields. Keep `detail.max_pages` modest and same-host.
9. Clean records by normalizing whitespace, resolving URLs, stripping tracking fragments, applying configured cleaners, removing blank-only records, and deduplicating by canonical link or normalized title/name.
10. Export CSV, Excel, and JSON. Include a report with visited pages, detail pages, skipped URLs, robots decisions, HTTP status, errors, raw/deduped counts, configured selectors, and field coverage counts/percentages.
11. If results still look sparse, read `references/extraction-strategy.md`, inspect the page HTML, and patch or extend `scripts/crawl_site.py` only for reusable behavior.

## Script

Use `scripts/crawl_site.py` for a practical baseline crawler. It uses Python standard-library networking and parsing only, so it runs in minimal environments. It supports:

- list/detail/pagination heuristics
- optional JSON or simple YAML selector configs
- `--inspect` diagnostics for one-page extraction previews
- `--suggest-config` starter selector generation
- configurable extra fields such as `image`, `date`, `tags`, `brand`, `author`, and `category`
- optional same-host detail-page enrichment
- field cleaning for URLs, dates, lists, whitespace, site suffixes, replacements, and money text
- robots.txt checks by default
- retry, timeout, delay, and polite user agent settings
- missing-field fallbacks
- duplicate cleanup
- CSV, `.xlsx`, and JSON export
- a machine-readable crawl report

Supported selector syntax is intentionally small: tag names, `.class`, `#id`, `[attr]`, `[attr=value]`, comma-separated alternatives, and descendant selectors such as `.card a`. Advanced configs are best written as JSON if nested YAML parsing becomes limiting. For JavaScript-heavy pages, first try a browser-rendered HTML capture, then feed the rendered HTML or adapt the script to use Playwright if the project environment already includes it.

## Compliance Guardrails

Always state that crawling must follow applicable law, website terms, robots.txt, and data rights. Do not help bypass authentication, CAPTCHAs, paywalls, IP bans, or other access controls. Keep default crawl volume small, use delays, and ask before increasing concurrency or ignoring robots.txt.

## Usage Examples

Extract a small product list:

```bash
python scripts/crawl_site.py "https://example.com/shop" --output ./shop-data --max-pages 3
```

Export custom fields:

```bash
python scripts/crawl_site.py "https://example.com/projects" --fields title,link,project_name,summary --output ./projects
```

Inspect before crawling:

```bash
python scripts/crawl_site.py "https://example.com/projects" --inspect --config ./crawler-config.yaml
```

Generate a starter config:

```bash
python scripts/crawl_site.py "https://example.com/projects" --suggest-config
```

Extract detail-page fields:

```bash
python scripts/crawl_site.py "https://example.com/products" --config ./crawler-config.json --fields title,link,price,image,tags,brand,summary
```

Increase politeness delay:

```bash
python scripts/crawl_site.py "https://example.com/catalog" --delay 3 --max-pages 10
```

## Troubleshooting

- If all records are empty, the site may render content with JavaScript. Capture rendered HTML or use a browser automation tool.
- If robots.txt disallows the URL, stop unless the user proves they own the site or has explicit permission.
- If pages return 403/429, reduce volume, increase delay, and avoid pretending to be a browser or rotating identities.
- If pagination loops, lower `--max-pages` and inspect `crawl-output.report.json`.
- If field quality is low, add a selector config before changing script logic.
- If a selector config produces too many rows, tighten `list_item` first, then field selectors.
- If list pages are thin, enable `detail.enabled` with a low `detail.max_pages` and detail-only selectors.
- If exported values are noisy, add `cleaning` rules or field-level `clean` rules before adding custom parsing code.
