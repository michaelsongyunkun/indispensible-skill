#!/usr/bin/env python3
"""Self-checks for the web crawler skill script."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import crawl_site


HTML = """
<!doctype html>
<html>
  <head>
    <title>Catalog</title>
    <meta name="description" content="Demo catalog">
    <link rel="next" href="/page/2">
    <script type="application/ld+json">
      {"@type": "Product", "name": "Structured Chair", "url": "/structured-chair",
       "description": "A chair from structured data.", "offers": {"price": "99.00"}}
    </script>
  </head>
  <body>
    <article class="product-card">
      <a class="detail" href="/alpha?utm_source=test"><h2>Alpha Chair</h2></a>
      <span class="price">$49.00</span>
      <p class="description">A compact chair for small spaces.</p>
    </article>
    <article class="product-card">
      <a class="detail" href="/beta"><h2>Beta Table</h2></a>
      <span class="price">79.00 USD</span>
      <p class="description">A useful table with a clean profile.</p>
    </article>
    <a class="next" href="/page/2">Next</a>
  </body>
</html>
"""


class CrawlSiteTests(unittest.TestCase):
    def test_price_detection_handles_common_symbols_and_codes(self) -> None:
        self.assertEqual(crawl_site.find_price("Only $49.00 today"), "$49.00")
        self.assertEqual(crawl_site.find_price("Costs 79.00 USD"), "79.00 USD")
        self.assertEqual(crawl_site.find_price("Price: \u20ac12,50"), "\u20ac12,50")
        self.assertEqual(crawl_site.find_price("Price: \u00a5120"), "\u00a5120")

    def test_configured_selectors_extract_records(self) -> None:
        parser = crawl_site.parse_html(HTML)
        config = crawl_site.CrawlConfig(
            selectors={
                "list_item": ".product-card",
                "title": "h2",
                "link": "a.detail",
                "price": ".price",
                "summary": ".description",
                "next_page": "a.next",
            }
        )
        records = crawl_site.extract_by_config(parser, "https://example.com/products", config)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["title"], "Alpha Chair")
        self.assertEqual(records[0]["link"], "https://example.com/alpha")
        self.assertEqual(records[1]["price"], "79.00 USD")

    def test_json_ld_and_next_page_detection(self) -> None:
        parser = crawl_site.parse_html(HTML)
        config = crawl_site.CrawlConfig(selectors={"next_page": "a.next"})
        json_records = crawl_site.extract_json_ld(HTML, "https://example.com/products")
        next_pages = crawl_site.find_next_pages(parser, "https://example.com/products", config)
        self.assertEqual(json_records[0]["title"], "Structured Chair")
        self.assertEqual(next_pages, ["https://example.com/page/2"])

    def test_simple_yaml_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "crawler-config.yaml"
            path.write_text(
                """
selectors:
  list_item: "#catalog .product-card"
  title: "h2"
  link: "a.detail"
""",
                encoding="utf-8",
            )
            config = crawl_site.load_config(str(path))
        self.assertEqual(config.selectors["list_item"], "#catalog .product-card")
        self.assertEqual(config.selectors["link"], "a.detail")

    def test_field_config_extracts_extra_attributes_and_lists(self) -> None:
        parser = crawl_site.parse_html(
            """
<article class="product-card">
  <a class="detail" href="/alpha"><h2>Alpha Chair | Demo Store</h2></a>
  <img class="photo" src="/alpha.jpg">
  <span class="tag">Furniture</span><span class="tag">Sale</span>
  <time datetime="2026-05-01">May 1, 2026</time>
</article>
"""
        )
        config = crawl_site.CrawlConfig(
            selectors={"list_item": ".product-card", "title": "h2", "link": "a.detail"},
            field_configs={
                "image": crawl_site.FieldConfig(selector="img.photo", attr="src", field_type="url"),
                "tags": crawl_site.FieldConfig(selector=".tag", multiple=True, field_type="list"),
                "date": crawl_site.FieldConfig(selector="time", attr="datetime", field_type="date"),
            },
            cleaning={"title": ["remove_site_suffix"]},
        )
        records = crawl_site.clean_records(
            crawl_site.extract_by_config(parser, "https://example.com/products", config),
            ["title", "link", "image", "tags", "date"],
            config,
        )
        self.assertEqual(records[0]["title"], "Alpha Chair")
        self.assertEqual(records[0]["image"], "https://example.com/alpha.jpg")
        self.assertEqual(records[0]["tags"], "Furniture; Sale")
        self.assertEqual(records[0]["date"], "2026-05-01")

    def test_detail_records_merge_into_list_records(self) -> None:
        base = {"title": "Alpha", "link": "https://example.com/alpha", "summary": "Short"}
        detail = {"link": "https://example.com/alpha", "summary": "Long detail", "brand": "Acme"}
        merged = crawl_site.merge_detail_record(base, detail)
        self.assertEqual(merged["summary"], "Long detail")
        self.assertEqual(merged["brand"], "Acme")

    def test_suggest_config_returns_selectors(self) -> None:
        suggestion = crawl_site.suggest_config(HTML, "https://example.com/products")
        self.assertIn("selectors", suggestion)
        self.assertIn("list_item", suggestion["selectors"])
        self.assertEqual(suggestion["selectors"]["next_page"], "a[rel=next], a.next")


if __name__ == "__main__":
    unittest.main()
