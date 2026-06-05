#!/usr/bin/env python3
"""Polite heuristic web crawler that exports CSV, XLSX, and JSON."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import zipfile
from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from xml.sax.saxutils import escape


DEFAULT_FIELDS = ["title", "link", "project_name", "price", "summary"]
PRICE_RE = re.compile(
    r"(?i)(?:(?:[$\u20ac\u00a3\u00a5]|USD|EUR|GBP|RMB|CNY)\s?[\d][\d,.]*|"
    r"[\d][\d,.]*\s?(?:USD|EUR|GBP|RMB|CNY))"
)
TEXT_TAGS = {"a", "h1", "h2", "h3", "h4", "p", "span", "div", "li"}
BLOCK_TAGS = {"article", "li", "section", "div"}
VOID_TAGS = {"meta", "link", "br", "img", "input", "hr", "area", "base", "col", "embed", "param", "source", "track", "wbr"}
RESERVED_SELECTOR_KEYS = {"list_item", "next_page"}
URL_FIELD_NAMES = {"link", "url", "image", "image_url", "thumbnail", "photo"}
LIST_FIELD_NAMES = {"tags", "categories", "images"}


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def canonical_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    filtered = [
        (k, v)
        for k, v in query
        if not k.lower().startswith(("utm_", "fbclid", "gclid"))
    ]
    return urllib.parse.urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path or "/",
            urllib.parse.urlencode(filtered, doseq=True),
            "",
        )
    )


def same_host(base: str, candidate: str) -> bool:
    return urllib.parse.urlsplit(base).netloc == urllib.parse.urlsplit(candidate).netloc


@dataclass
class FieldConfig:
    selector: str = ""
    attr: str = ""
    field_type: str = "text"
    multiple: bool = False
    cleaners: list[object] = field(default_factory=list)


@dataclass
class CrawlConfig:
    selectors: dict[str, str] = field(default_factory=dict)
    field_configs: dict[str, FieldConfig] = field(default_factory=dict)
    cleaning: dict[str, list[object]] = field(default_factory=dict)
    detail_enabled: bool = False
    detail_max_pages: int = 20
    detail_selectors: dict[str, str] = field(default_factory=dict)
    detail_field_configs: dict[str, FieldConfig] = field(default_factory=dict)


@dataclass
class FetchResult:
    content: str | None
    error: str | None
    status: int | None = None
    content_type: str = ""
    elapsed_ms: int = 0
    robots_allowed: bool | None = None
    robots_reason: str = ""


@dataclass
class Node:
    tag: str
    attrs: dict[str, str]
    parent: "Node | None" = None
    children: list["Node"] = field(default_factory=list)
    text_parts: list[str] = field(default_factory=list)

    def add_child(self, child: "Node") -> None:
        self.children.append(child)

    def text(self) -> str:
        parts = list(self.text_parts)
        for child in self.children:
            child_text = child.text()
            if child_text:
                parts.append(child_text)
        return clean_text(" ".join(parts))

    def attr(self, name: str) -> str:
        return self.attrs.get(name, "")

    def classes(self) -> set[str]:
        return set(self.attr("class").split())

    def descendants(self, tag: str | None = None) -> Iterable["Node"]:
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.descendants(tag)


class TreeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("document", {})
        self.stack = [self.root]
        self.title = ""
        self.meta: dict[str, str] = {}
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs = {k.lower(): v or "" for k, v in attrs_list}
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].add_child(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            content = attrs.get("content")
            if key and content:
                self.meta[key.lower()] = clean_text(content)
        if tag == "link":
            rel = attrs.get("rel", "").lower()
            href = attrs.get("href", "")
            if rel and href:
                self.links.append((rel, href))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for idx in range(len(self.stack) - 1, 0, -1):
            if self.stack[idx].tag == tag:
                del self.stack[idx:]
                break

    def handle_data(self, data: str) -> None:
        text = clean_text(data)
        if text:
            self.stack[-1].text_parts.append(text)


def parse_html(content: str) -> TreeParser:
    parser = TreeParser()
    parser.feed(content)
    title_node = next(parser.root.descendants("title"), None)
    parser.title = title_node.text() if title_node else ""
    return parser


def split_selector(selector: str) -> list[str]:
    return [part.strip() for part in selector.split(",") if part.strip()]


def parse_simple_selector(selector: str) -> dict[str, str]:
    selector = selector.strip()
    attr_name = attr_value = ""
    attr_match = re.search(r"\[([a-zA-Z_:-][\w:.-]*)(?:=(['\"]?)(.*?)\2)?\]", selector)
    if attr_match:
        attr_name = attr_match.group(1).lower()
        attr_value = attr_match.group(3) or ""
        selector = selector[: attr_match.start()] + selector[attr_match.end() :]

    id_value = ""
    id_match = re.search(r"#([\w:-]+)", selector)
    if id_match:
        id_value = id_match.group(1)
        selector = selector.replace(f"#{id_value}", "", 1)

    classes = re.findall(r"\.([\w:-]+)", selector)
    selector = re.sub(r"\.[\w:-]+", "", selector).strip()
    tag = selector.lower() if selector else ""
    return {"tag": tag, "id": id_value, "classes": " ".join(classes), "attr": attr_name, "value": attr_value}


def simple_selector_matches(node: Node, selector: str) -> bool:
    parsed = parse_simple_selector(selector)
    if parsed["tag"] and node.tag != parsed["tag"]:
        return False
    if parsed["id"] and node.attr("id") != parsed["id"]:
        return False
    if parsed["classes"] and not set(parsed["classes"].split()).issubset(node.classes()):
        return False
    if parsed["attr"]:
        if parsed["attr"] not in node.attrs:
            return False
        if parsed["value"] and node.attr(parsed["attr"]) != parsed["value"]:
            return False
    return True


def selector_matches(node: Node, selector: str) -> bool:
    parts = [part for part in selector.split() if part]
    if not parts or not simple_selector_matches(node, parts[-1]):
        return False
    ancestor = node.parent
    for part in reversed(parts[:-1]):
        while ancestor is not None and not simple_selector_matches(ancestor, part):
            ancestor = ancestor.parent
        if ancestor is None:
            return False
        ancestor = ancestor.parent
    return True


def select_all(root: Node, selector: str) -> list[Node]:
    matches: list[Node] = []
    for option in split_selector(selector):
        for node in root.descendants():
            if selector_matches(node, option):
                matches.append(node)
    return unique_nodes(matches)


def select_first(root: Node, selector: str) -> Node | None:
    matches = select_all(root, selector)
    return matches[0] if matches else None


def unique_nodes(nodes: Iterable[Node]) -> list[Node]:
    seen: set[int] = set()
    output = []
    for node in nodes:
        if id(node) not in seen:
            seen.add(id(node))
            output.append(node)
    return output


def load_config(path: str | None) -> CrawlConfig:
    if not path:
        return CrawlConfig()
    config_path = Path(path)
    text = config_path.read_text(encoding="utf-8")
    if config_path.suffix.lower() == ".json":
        raw = json.loads(text)
    else:
        raw = parse_simple_yaml(text)
    if not isinstance(raw, dict):
        return CrawlConfig()
    selectors = normalize_selectors(raw.get("selectors", raw))
    field_configs = parse_field_configs(raw.get("fields", {}), selectors)
    cleaning = normalize_cleaning(raw.get("cleaning", {}))
    detail_raw = raw.get("detail", {}) if isinstance(raw.get("detail", {}), dict) else {}
    detail_selectors = normalize_selectors(detail_raw.get("selectors", {}))
    return CrawlConfig(
        selectors=selectors,
        field_configs=field_configs,
        cleaning=cleaning,
        detail_enabled=parse_bool(detail_raw.get("enabled", False)),
        detail_max_pages=parse_int(detail_raw.get("max_pages", 20), 20),
        detail_selectors=detail_selectors,
        detail_field_configs=parse_field_configs(detail_raw.get("fields", {}), detail_selectors),
    )


def normalize_selectors(raw: object) -> dict[str, str]:
    if not isinstance(raw, dict):
        return {}
    selectors: dict[str, str] = {}
    for key, value in raw.items():
        if isinstance(value, str) and clean_text(value):
            selectors[str(key)] = clean_text(value)
    return selectors


def parse_field_configs(raw_fields: object, selectors: dict[str, str]) -> dict[str, FieldConfig]:
    configs: dict[str, FieldConfig] = {}
    for field_name, selector in selectors.items():
        if field_name not in RESERVED_SELECTOR_KEYS:
            configs[field_name] = FieldConfig(selector=selector, field_type=infer_field_type(field_name))
    if not isinstance(raw_fields, dict):
        return configs
    for field_name, raw in raw_fields.items():
        name = str(field_name)
        if isinstance(raw, str):
            configs[name] = FieldConfig(selector=clean_text(raw), field_type=infer_field_type(name))
        elif isinstance(raw, dict):
            selector = raw.get("selector") or raw.get("selectors") or configs.get(name, FieldConfig()).selector
            if isinstance(selector, list):
                selector = ", ".join(str(item) for item in selector if clean_text(str(item)))
            configs[name] = FieldConfig(
                selector=clean_text(str(selector or "")),
                attr=clean_text(str(raw.get("attr", ""))),
                field_type=clean_text(str(raw.get("type", infer_field_type(name)))).lower(),
                multiple=parse_bool(raw.get("multiple", name in LIST_FIELD_NAMES)),
                cleaners=normalize_cleaner_list(raw.get("clean", raw.get("cleaners", []))),
            )
    return configs


def normalize_cleaning(raw: object) -> dict[str, list[object]]:
    if not isinstance(raw, dict):
        return {}
    return {str(key): normalize_cleaner_list(value) for key, value in raw.items()}


def normalize_cleaner_list(value: object) -> list[object]:
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value:
        return [value]
    if isinstance(value, dict):
        return [value]
    return []


def parse_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def parse_int(value: object, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def infer_field_type(field_name: str) -> str:
    name = field_name.lower()
    if name in URL_FIELD_NAMES or name.endswith("_url"):
        return "url"
    if name in LIST_FIELD_NAMES:
        return "list"
    if "date" in name or name in {"published", "updated"}:
        return "date"
    if name in {"price", "amount", "cost"}:
        return "money"
    return "text"


def parse_simple_yaml(text: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_map: dict[str, str] | None = None
    for raw_line in text.splitlines():
        line = strip_yaml_comment(raw_line).rstrip()
        if not line.strip():
            continue
        if not raw_line.startswith((" ", "\t")):
            key, sep, value = line.partition(":")
            if not sep:
                continue
            key = key.strip()
            value = value.strip()
            if value:
                data[key] = strip_quotes(value)
                current_map = None
            else:
                current_map = {}
                data[key] = current_map
            continue
        if current_map is not None:
            key, sep, value = line.strip().partition(":")
            if sep:
                current_map[key.strip()] = strip_quotes(value.strip())
    return data


def strip_yaml_comment(line: str) -> str:
    quote = ""
    for idx, char in enumerate(line):
        if char in {"'", '"'} and (idx == 0 or line[idx - 1] != "\\"):
            quote = "" if quote == char else char if not quote else quote
        if char == "#" and not quote and (idx == 0 or line[idx - 1].isspace()):
            return line[:idx]
    return line


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def node_path(node: Node) -> str:
    parts = []
    current = node
    while current.parent is not None:
        siblings = [child for child in current.parent.children if child.tag == current.tag]
        idx = siblings.index(current) if current in siblings else 0
        parts.append(f"{current.tag}:{idx // 3}")
        current = current.parent
    return "/".join(reversed(parts[-5:]))


def find_heading(node: Node) -> str:
    for tag in ("h1", "h2", "h3", "h4"):
        for child in node.descendants(tag):
            text = child.text()
            if text:
                return text
    for child in node.descendants("a"):
        text = child.text()
        if len(text) > 2:
            return text
    return ""


def find_price(text: str) -> str:
    match = PRICE_RE.search(text)
    return clean_text(match.group(0)) if match else ""


def find_summary(node: Node, title: str, price: str) -> str:
    candidates = []
    for tag in ("p", "div", "span"):
        for child in node.descendants(tag):
            text = child.text()
            if len(text) >= 24 and text != title and text != price:
                candidates.append(text)
    candidates.sort(key=len)
    return candidates[0] if candidates else ""


def extract_json_ld(content: str, page_url: str) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    blocks = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        content,
        flags=re.I | re.S,
    )
    for block in blocks:
        try:
            data = json.loads(html.unescape(block.strip()))
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        idx = 0
        while idx < len(items):
            item = items[idx]
            idx += 1
            if not isinstance(item, dict):
                continue
            graph = item.get("@graph")
            if isinstance(graph, list):
                items.extend(x for x in graph if isinstance(x, dict))
            typ = str(item.get("@type", ""))
            if not any(x in typ.lower() for x in ("product", "article", "itemlist", "creativework", "webpage")):
                continue
            offers = item.get("offers") if isinstance(item.get("offers"), dict) else {}
            price = clean_text(str(offers.get("price", ""))) if offers else ""
            url = item.get("url") or page_url
            records.append(
                {
                    "title": clean_text(str(item.get("headline") or item.get("name") or "")),
                    "link": urllib.parse.urljoin(page_url, str(url)),
                    "project_name": clean_text(str(item.get("name") or "")),
                    "price": price,
                    "summary": clean_text(str(item.get("description") or "")),
                    "_source": "json-ld",
                }
            )
    return records


def extract_by_config(parser: TreeParser, page_url: str, config: CrawlConfig) -> list[dict[str, str]]:
    selectors = config.selectors
    if not selectors and not config.field_configs:
        return []
    containers = select_all(parser.root, selectors["list_item"]) if selectors.get("list_item") else [parser.root]
    records = []
    field_names = list(OrderedDict.fromkeys([*DEFAULT_FIELDS, *config.field_configs.keys()]))
    for container in containers:
        record = {field_name: extract_config_field(container, field_name, page_url, config) for field_name in field_names}
        title = record.get("title") or find_heading(container)
        price = record.get("price") or find_price(container.text())
        record["title"] = clean_text(title)
        record["link"] = record.get("link") or canonical_url(page_url)
        record["project_name"] = record.get("project_name") or title
        record["price"] = clean_text(price)
        record["summary"] = record.get("summary") or find_summary(container, title, price)
        record["_source"] = "config"
        records.append(record)
    return records


def extract_config_field(root: Node, field_name: str, page_url: str, config: CrawlConfig) -> str:
    field_config = config.field_configs.get(field_name)
    selector = field_config.selector if field_config else config.selectors.get(field_name, "")
    if not selector:
        return ""
    nodes = select_all(root, selector)
    if not nodes:
        return ""
    multiple = field_config.multiple if field_config else field_name in LIST_FIELD_NAMES
    selected_nodes = nodes if multiple else nodes[:1]
    values = [extract_node_value(node, field_name, page_url, field_config) for node in selected_nodes]
    values = [value for value in values if value]
    return "; ".join(OrderedDict.fromkeys(values))


def extract_node_value(node: Node, field_name: str, page_url: str, field_config: FieldConfig | None) -> str:
    attr = field_config.attr if field_config else ""
    if not attr:
        if field_name == "link":
            attr = "href"
        elif infer_field_type(field_name) == "url":
            attr = "src"
        elif infer_field_type(field_name) == "date":
            attr = "datetime"
    value = node.attr(attr) if attr else node.text()
    if not value and field_name == "link":
        value = node.attr("data-href")
    if not value and infer_field_type(field_name) == "url":
        value = node.attr("href") or node.attr("data-src")
    if not value:
        value = node.text()
    if (field_config and field_config.field_type == "url") or infer_field_type(field_name) == "url":
        return canonical_url(urllib.parse.urljoin(page_url, value)) if value else ""
    return clean_text(value)


def extract_cards(parser: TreeParser, page_url: str) -> list[dict[str, str]]:
    anchors = []
    for anchor in parser.root.descendants("a"):
        href = anchor.attr("href")
        text = anchor.text()
        if not href or not text:
            continue
        absolute = urllib.parse.urljoin(page_url, href)
        if same_host(page_url, absolute):
            anchors.append((anchor, absolute, text))

    path_counts: dict[str, int] = defaultdict(int)
    for anchor, _, _ in anchors:
        container = nearest_container(anchor)
        path_counts[node_path(container)] += 1

    repeated_paths = {path for path, count in path_counts.items() if count >= 2}
    records = []
    seen_containers: set[int] = set()
    for anchor, link, text in anchors:
        container = nearest_container(anchor)
        if id(container) in seen_containers:
            continue
        if repeated_paths and node_path(container) not in repeated_paths:
            continue
        seen_containers.add(id(container))
        all_text = container.text()
        title = find_heading(container) or text or parser.meta.get("og:title") or parser.title
        price = find_price(all_text)
        summary = find_summary(container, title, price)
        records.append(
            {
                "title": clean_text(title),
                "link": canonical_url(link),
                "project_name": clean_text(title),
                "price": price,
                "summary": summary,
                "_source": "heuristic",
            }
        )

    if not records:
        page_title = parser.meta.get("og:title") or parser.title
        records.append(
            {
                "title": clean_text(page_title),
                "link": canonical_url(page_url),
                "project_name": clean_text(page_title),
                "price": find_price(parser.root.text()),
                "summary": parser.meta.get("description") or parser.meta.get("og:description") or "",
                "_source": "page-fallback",
            }
        )
    return records


def nearest_container(node: Node) -> Node:
    current = node
    while current.parent is not None:
        if current.tag in BLOCK_TAGS and len(current.text()) > 20:
            return current
        current = current.parent
    return node


def find_next_pages(parser: TreeParser, page_url: str, config: CrawlConfig | None = None) -> list[str]:
    candidates = []
    selector = config.selectors.get("next_page", "") if config else ""
    if selector:
        for node in select_all(parser.root, selector):
            href = node.attr("href")
            if href:
                candidates.append(urllib.parse.urljoin(page_url, href))
    for rel, href in parser.links:
        if "next" in rel:
            candidates.append(urllib.parse.urljoin(page_url, href))
    for anchor in parser.root.descendants("a"):
        text = anchor.text().lower()
        href = anchor.attr("href")
        if not href:
            continue
        if text in {"next", "next page", ">", ">>"} or "next" in text:
            candidates.append(urllib.parse.urljoin(page_url, href))
    return [
        canonical_url(url)
        for url in OrderedDict.fromkeys(candidates)
        if same_host(page_url, url)
    ]


class Fetcher:
    def __init__(
        self,
        user_agent: str,
        timeout: int,
        retries: int,
        delay: float,
        respect_robots: bool,
    ) -> None:
        self.user_agent = user_agent
        self.timeout = timeout
        self.retries = retries
        self.delay = delay
        self.respect_robots = respect_robots
        self.last_fetch = 0.0
        self.robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}

    def allowed(self, url: str) -> tuple[bool, str]:
        if not self.respect_robots:
            return True, "robots ignored by user option"
        parsed = urllib.parse.urlsplit(url)
        robots_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, "/robots.txt", "", ""))
        if robots_url not in self.robots_cache:
            rp = urllib.robotparser.RobotFileParser()
            rp.set_url(robots_url)
            try:
                rp.read()
            except Exception as exc:  # noqa: BLE001
                return True, f"robots unavailable: {exc}"
            self.robots_cache[robots_url] = rp
        allowed = self.robots_cache[robots_url].can_fetch(self.user_agent, url)
        return allowed, "allowed by robots.txt" if allowed else "disallowed by robots.txt"

    def fetch(self, url: str) -> FetchResult:
        allowed, reason = self.allowed(url)
        if not allowed:
            return FetchResult(None, reason, robots_allowed=False, robots_reason=reason)
        wait = self.delay - (time.time() - self.last_fetch)
        if wait > 0:
            time.sleep(wait)
        headers = {"User-Agent": self.user_agent, "Accept": "text/html,application/xhtml+xml"}
        request = urllib.request.Request(url, headers=headers)
        for attempt in range(self.retries + 1):
            started = time.time()
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    self.last_fetch = time.time()
                    content_type = response.headers.get("content-type", "")
                    status = getattr(response, "status", None)
                    elapsed_ms = int((time.time() - started) * 1000)
                    if "text/html" not in content_type and "application/xhtml" not in content_type:
                        return FetchResult(
                            None,
                            f"unsupported content type: {content_type}",
                            status,
                            content_type,
                            elapsed_ms,
                            True,
                            reason,
                        )
                    raw = response.read()
                    charset = response.headers.get_content_charset() or "utf-8"
                    return FetchResult(
                        raw.decode(charset, errors="replace"),
                        None,
                        status,
                        content_type,
                        elapsed_ms,
                        True,
                        reason,
                    )
            except urllib.error.HTTPError as exc:
                if attempt >= self.retries:
                    return FetchResult(None, str(exc), exc.code, "", int((time.time() - started) * 1000), True, reason)
                time.sleep(min(2**attempt, 8))
            except (urllib.error.URLError, TimeoutError) as exc:
                if attempt >= self.retries:
                    return FetchResult(None, str(exc), elapsed_ms=int((time.time() - started) * 1000), robots_allowed=True, robots_reason=reason)
                time.sleep(min(2**attempt, 8))
        return FetchResult(None, "unknown fetch error", robots_allowed=True, robots_reason=reason)


def clean_records(records: Iterable[dict[str, str]], fields: list[str], config: CrawlConfig) -> list[dict[str, str]]:
    cleaned_records = []
    for record in records:
        cleaned = {}
        for field_name in fields:
            field_config = config.field_configs.get(field_name) or config.detail_field_configs.get(field_name)
            value = record.get(field_name, "")
            cleaned[field_name] = clean_field_value(field_name, value, field_config, config)
        if any(cleaned.values()):
            cleaned_records.append(cleaned)
    return cleaned_records


def clean_field_value(field_name: str, value: object, field_config: FieldConfig | None, config: CrawlConfig) -> str:
    if isinstance(value, list):
        text = "; ".join(clean_text(str(item)) for item in value if clean_text(str(item)))
    else:
        text = clean_text(str(value or ""))
    field_type = field_config.field_type if field_config else infer_field_type(field_name)
    if field_type == "url" and text:
        text = canonical_url(text)
    elif field_type == "date" and text:
        text = normalize_date(text)
    elif field_type == "list" and text:
        text = normalize_list_value(text)
    cleaners = [*config.cleaning.get(field_name, []), *(field_config.cleaners if field_config else [])]
    for cleaner in cleaners:
        text = apply_cleaner(text, cleaner)
    return text


def normalize_date(value: str) -> str:
    match = re.search(r"\b(\d{4})[-/](\d{1,2})[-/](\d{1,2})\b", value)
    if match:
        year, month, day = match.groups()
        return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
    match = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b", value)
    if match:
        month, day, year = match.groups()
        return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
    return value


def normalize_list_value(value: str) -> str:
    parts = re.split(r"\s*[;,|]\s*", value)
    return "; ".join(OrderedDict.fromkeys(clean_text(part) for part in parts if clean_text(part)))


def apply_cleaner(value: str, cleaner: object) -> str:
    if not value:
        return ""
    if isinstance(cleaner, str):
        if cleaner == "lower":
            return value.lower()
        if cleaner == "upper":
            return value.upper()
        if cleaner == "remove_site_suffix":
            return remove_site_suffix(value)
        if cleaner == "parse_money":
            return parse_money(value)
        if cleaner == "normalize_whitespace":
            return clean_text(value)
        return value
    if isinstance(cleaner, dict):
        if "remove_suffix" in cleaner:
            suffix = str(cleaner["remove_suffix"])
            return value[: -len(suffix)].strip() if suffix and value.endswith(suffix) else value
        if "replace" in cleaner and isinstance(cleaner["replace"], dict):
            old = str(cleaner["replace"].get("old", ""))
            new = str(cleaner["replace"].get("new", ""))
            return value.replace(old, new) if old else value
    return value


def remove_site_suffix(value: str) -> str:
    for sep in (" | ", " - ", " – ", " — "):
        if sep in value:
            left, right = value.rsplit(sep, 1)
            if left and right:
                return left.strip()
    return value


def parse_money(value: str) -> str:
    match = PRICE_RE.search(value)
    if not match:
        return value
    money = match.group(0)
    return re.sub(r"(?i)(USD|EUR|GBP|RMB|CNY|[$\u20ac\u00a3\u00a5])", "", money).strip()


def merge_detail_record(base: dict[str, str], detail: dict[str, str]) -> dict[str, str]:
    merged = dict(base)
    for key, value in detail.items():
        value = clean_text(str(value or ""))
        if not value or key.startswith("_"):
            continue
        if key in {"link", "title", "project_name"} and merged.get(key):
            continue
        current = clean_text(str(merged.get(key, "")))
        if not current or len(value) > len(current):
            merged[key] = value
    return merged


def dedupe(records: Iterable[dict[str, str]], fields: list[str]) -> list[dict[str, str]]:
    output: OrderedDict[str, dict[str, str]] = OrderedDict()
    for record in records:
        cleaned = {field: clean_text(record.get(field, "")) for field in fields}
        if "link" in cleaned and cleaned["link"]:
            cleaned["link"] = canonical_url(cleaned["link"])
        if not any(cleaned.values()):
            continue
        key = cleaned.get("link") or "|".join(
            [cleaned.get("project_name", "").lower(), cleaned.get("title", "").lower(), cleaned.get("price", "")]
        )
        if key and key not in output:
            output[key] = cleaned
    return list(output.values())


def build_field_coverage(records: list[dict[str, str]], fields: list[str]) -> dict[str, dict[str, float | int]]:
    total = len(records)
    return {
        field_name: {
            "count": sum(1 for record in records if record.get(field_name)),
            "percent": round((sum(1 for record in records if record.get(field_name)) / total) * 100, 1) if total else 0,
        }
        for field_name in fields
    }


def inspect_page(content: str, page_url: str, config: CrawlConfig) -> dict[str, object]:
    parser = parse_html(content)
    anchors = [anchor for anchor in parser.root.descendants("a") if anchor.attr("href")]
    containers = [nearest_container(anchor) for anchor in anchors]
    path_counts: dict[str, int] = defaultdict(int)
    for container in containers:
        path_counts[node_path(container)] += 1
    configured = extract_by_config(parser, page_url, config)
    heuristic = extract_cards(parser, page_url)
    return {
        "title": parser.meta.get("og:title") or parser.title,
        "meta_description": parser.meta.get("description") or parser.meta.get("og:description") or "",
        "json_ld_records": len(extract_json_ld(content, page_url)),
        "configured_records": len(configured),
        "heuristic_records": len(heuristic),
        "next_pages": find_next_pages(parser, page_url, config),
        "top_container_paths": [
            {"path": path, "count": count}
            for path, count in sorted(path_counts.items(), key=lambda item: item[1], reverse=True)[:8]
        ],
        "sample_records": dedupe(configured or heuristic, DEFAULT_FIELDS)[:5],
    }


def suggest_config(content: str, page_url: str) -> dict[str, object]:
    parser = parse_html(content)
    anchors = [anchor for anchor in parser.root.descendants("a") if anchor.attr("href")]
    containers = [nearest_container(anchor) for anchor in anchors]
    path_counts: dict[str, int] = defaultdict(int)
    path_nodes: dict[str, Node] = {}
    for container in containers:
        path = node_path(container)
        path_counts[path] += 1
        path_nodes.setdefault(path, container)
    list_selector = ""
    if path_counts:
        best_path = max(path_counts, key=path_counts.get)
        list_selector = selector_for_node(path_nodes[best_path])
    selectors = {
        "list_item": list_selector or "article, li, .card",
        "title": "h1, h2, h3, .title, [itemprop=name]",
        "link": "a[href]",
        "price": ".price, [itemprop=price]",
        "summary": "p, .summary, .description, [itemprop=description]",
    }
    next_selectors = []
    if any("next" in rel for rel, _ in parser.links):
        next_selectors.append("a[rel=next]")
    if any("next" in anchor.text().lower() for anchor in parser.root.descendants("a")):
        next_selectors.append("a.next")
    selectors["next_page"] = ", ".join(next_selectors) or "a[rel=next], a.next"
    field_suggestions = {
        "image": {"selector": "img", "attr": "src", "type": "url"},
        "date": {"selector": "time, .date, [datetime]", "attr": "datetime", "type": "date"},
        "tags": {"selector": ".tag, .category, [rel=tag]", "type": "list", "multiple": True},
    }
    return {
        "selectors": selectors,
        "fields": field_suggestions,
        "cleaning": {"title": ["remove_site_suffix"], "price": ["normalize_whitespace"]},
        "detail": {"enabled": False, "max_pages": 20, "selectors": {}},
        "notes": [
            "Tighten list_item first if records are noisy.",
            "Enable detail only when list pages omit important fields.",
        ],
    }


def selector_for_node(node: Node) -> str:
    classes = sorted(node.classes())
    if node.attr("id"):
        return f"{node.tag}#{node.attr('id')}"
    if classes:
        return f"{node.tag}." + ".".join(classes[:2])
    return node.tag


def write_csv(path: Path, records: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


def xlsx_col_name(index: int) -> str:
    name = ""
    while index:
        index, rem = divmod(index - 1, 26)
        name = chr(65 + rem) + name
    return name


def write_xlsx(path: Path, records: list[dict[str, str]], fields: list[str]) -> None:
    rows = [fields] + [[record.get(field, "") for field in fields] for record in records]
    sheet_rows = []
    for row_idx, row in enumerate(rows, start=1):
        cells = []
        for col_idx, value in enumerate(row, start=1):
            ref = f"{xlsx_col_name(col_idx)}{row_idx}"
            cells.append(f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>')
        sheet_rows.append(f'<row r="{row_idx}">{"".join(cells)}</row>')
    sheet = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f'<sheetData>{"".join(sheet_rows)}</sheetData></worksheet>'
    )
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", CONTENT_TYPES)
        zf.writestr("_rels/.rels", ROOT_RELS)
        zf.writestr("xl/workbook.xml", WORKBOOK)
        zf.writestr("xl/_rels/workbook.xml.rels", WORKBOOK_RELS)
        zf.writestr("xl/worksheets/sheet1.xml", sheet)


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>"""
ROOT_RELS = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""
WORKBOOK = """<?xml version="1.0" encoding="UTF-8"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets><sheet name="data" sheetId="1" r:id="rId1"/></sheets></workbook>"""
WORKBOOK_RELS = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>"""


def enrich_with_detail_pages(
    records: list[dict[str, str]],
    config: CrawlConfig,
    fetcher: Fetcher,
    start_url: str,
    report: dict[str, object],
) -> list[dict[str, str]]:
    if not config.detail_enabled:
        return records
    detail_config = CrawlConfig(
        selectors=config.detail_selectors,
        field_configs=config.detail_field_configs,
        cleaning=config.cleaning,
    )
    enriched = []
    detail_seen: set[str] = set()
    report.setdefault("detail_visited", [])
    report.setdefault("detail_errors", [])
    for record in records:
        link = record.get("link", "")
        if (
            not link
            or link in detail_seen
            or not same_host(start_url, link)
            or len(detail_seen) >= config.detail_max_pages
        ):
            enriched.append(record)
            continue
        detail_seen.add(link)
        result = fetcher.fetch(link)
        if result.error or result.content is None:
            report["detail_errors"].append({"url": link, "error": result.error, "status": result.status})
            enriched.append(record)
            continue
        report["detail_visited"].append({"url": link, "status": result.status, "elapsed_ms": result.elapsed_ms})
        parser = parse_html(result.content)
        detail_records = extract_by_config(parser, link, detail_config)
        if not detail_records:
            detail_records = extract_json_ld(result.content, link) or extract_cards(parser, link)
        enriched.append(merge_detail_record(record, detail_records[0] if detail_records else {}))
    return enriched


def crawl(args: argparse.Namespace) -> tuple[list[dict[str, str]], dict[str, object]]:
    start_url = canonical_url(args.url)
    config = load_config(args.config)
    fields = resolve_fields(args.fields, config)
    fetcher = Fetcher(args.user_agent, args.timeout, args.retries, args.delay, not args.ignore_robots)
    queue = [start_url]
    visited: set[str] = set()
    records = []
    report: dict[str, object] = {
        "visited": [],
        "skipped": [],
        "errors": [],
        "robots": [],
        "field_coverage": {},
        "configured_selectors": config.selectors,
    }

    while queue and len(visited) < args.max_pages:
        url = queue.pop(0)
        if url in visited:
            report["skipped"].append({"url": url, "reason": "duplicate queue entry"})
            continue
        visited.add(url)
        result = fetcher.fetch(url)
        report["robots"].append({"url": url, "allowed": result.robots_allowed, "reason": result.robots_reason})
        if result.error:
            report["errors"].append({"url": url, "error": result.error, "status": result.status})
            continue
        if result.content is None:
            continue
        report["visited"].append(
            {
                "url": url,
                "status": result.status,
                "content_type": result.content_type,
                "elapsed_ms": result.elapsed_ms,
            }
        )
        parser = parse_html(result.content)
        configured_records = extract_by_config(parser, url, config)
        page_records = extract_json_ld(result.content, url) + (configured_records or extract_cards(parser, url))
        records.extend(page_records)
        for next_url in find_next_pages(parser, url, config):
            if next_url not in visited and next_url not in queue and len(visited) + len(queue) < args.max_pages:
                queue.append(next_url)

    raw_count = len(records)
    records = enrich_with_detail_pages(records, config, fetcher, start_url, report)
    cleaned = dedupe(clean_records(records, fields, config), fields)
    report["field_coverage"] = build_field_coverage(cleaned, fields)
    report["record_count"] = len(cleaned)
    report["raw_record_count"] = raw_count
    report["deduped_record_count"] = raw_count - len(cleaned)
    report["requested_fields"] = fields
    return cleaned, report


def resolve_fields(fields_arg: str, config: CrawlConfig) -> list[str]:
    fields = [field.strip() for field in fields_arg.split(",") if field.strip()]
    if fields_arg == ",".join(DEFAULT_FIELDS):
        configured_fields = [
            field_name
            for field_name in [*config.field_configs.keys(), *config.detail_field_configs.keys()]
            if field_name not in RESERVED_SELECTOR_KEYS and field_name not in fields
        ]
        fields.extend(configured_fields)
    return fields


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract structured website data to CSV, XLSX, and JSON.")
    parser.add_argument("url", help="Start URL to crawl")
    parser.add_argument("--output", default="./crawl-output", help="Output path prefix without extension")
    parser.add_argument("--fields", default=",".join(DEFAULT_FIELDS), help="Comma-separated export fields")
    parser.add_argument("--config", help="Optional JSON or simple YAML selector config")
    parser.add_argument("--inspect", action="store_true", help="Fetch one page and print extraction diagnostics")
    parser.add_argument("--suggest-config", action="store_true", help="Fetch one page and print a starter selector config")
    parser.add_argument("--max-pages", type=int, default=5, help="Maximum pages to fetch")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds to wait between requests")
    parser.add_argument("--timeout", type=int, default=20, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=2, help="Fetch retries per page")
    parser.add_argument(
        "--user-agent",
        default="CodexWebCrawlerSkill/1.1 (+https://openai.com; educational polite crawler)",
        help="Descriptive user agent",
    )
    parser.add_argument("--ignore-robots", action="store_true", help="Skip robots.txt checks only with permission")
    args = parser.parse_args()

    if args.max_pages < 1:
        print("--max-pages must be at least 1", file=sys.stderr)
        return 2

    if args.inspect or args.suggest_config:
        config = load_config(args.config)
        fetcher = Fetcher(args.user_agent, args.timeout, args.retries, args.delay, not args.ignore_robots)
        start_url = canonical_url(args.url)
        result = fetcher.fetch(start_url)
        if result.error or result.content is None:
            print(json.dumps({"url": start_url, "error": result.error}, ensure_ascii=False, indent=2))
            return 1
        if args.suggest_config:
            print(json.dumps(suggest_config(result.content, start_url), ensure_ascii=False, indent=2))
            return 0
        print(json.dumps(inspect_page(result.content, start_url, config), ensure_ascii=False, indent=2))
        return 0

    records, report = crawl(args)
    output = Path(args.output)
    fields = resolve_fields(args.fields, load_config(args.config))
    write_csv(output.with_suffix(".csv"), records, fields)
    write_xlsx(output.with_suffix(".xlsx"), records, fields)
    output.with_suffix(".json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    output.with_suffix(".report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(records)} records to {output.with_suffix('.csv')}, {output.with_suffix('.xlsx')}, and {output.with_suffix('.json')}")
    print(f"Report: {output.with_suffix('.report.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
