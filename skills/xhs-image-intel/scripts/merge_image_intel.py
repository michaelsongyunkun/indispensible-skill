#!/usr/bin/env python3
"""Merge Xiaohongshu note records and per-image insights into CSV/JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "note_id",
    "note_url",
    "keyword",
    "title",
    "body_text",
    "author_name",
    "author_id",
    "publish_time",
    "likes",
    "favorites",
    "comments_count",
    "shares",
    "image_id",
    "image_url",
    "image_path",
    "ocr_text",
    "products",
    "brands",
    "prices",
    "locations",
    "scene",
    "style_tags",
    "objects",
    "pain_points",
    "selling_points",
    "audience",
    "evidence",
    "confidence",
    "comment_summary",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not path.exists():
        raise FileNotFoundError(path)
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            value = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected JSON object")
        records.append(value)
    return records


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(stringify(item) for item in value if item is not None)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def first_present(record: dict[str, Any], keys: list[str]) -> Any:
    for key in keys:
        if key in record and record[key] not in (None, ""):
            return record[key]
    return ""


def normalize_note(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "note_id": first_present(record, ["note_id", "feed_id", "id"]),
        "note_url": first_present(record, ["note_url", "url", "link"]),
        "keyword": first_present(record, ["keyword", "query", "theme"]),
        "title": first_present(record, ["title", "displayTitle", "name"]),
        "body_text": first_present(record, ["body_text", "description", "desc", "content", "text"]),
        "author_name": first_present(record, ["author_name", "nickname", "user_name"]),
        "author_id": first_present(record, ["author_id", "user_id", "userId"]),
        "publish_time": first_present(record, ["publish_time", "time", "date"]),
        "likes": first_present(record, ["likes", "liked_count", "like_count"]),
        "favorites": first_present(record, ["favorites", "collected_count", "favorite_count"]),
        "comments_count": first_present(record, ["comments_count", "comment_count"]),
        "shares": first_present(record, ["shares", "share_count"]),
        "comment_summary": first_present(record, ["comment_summary", "comments_summary"]),
    }


def normalize_image(record: dict[str, Any]) -> dict[str, Any]:
    note_id = first_present(record, ["note_id", "feed_id", "id"])
    return {
        "note_id": note_id,
        "image_id": first_present(record, ["image_id", "id", "index"]),
        "image_url": first_present(record, ["image_url", "url", "src"]),
        "image_path": first_present(record, ["image_path", "path", "file"]),
        "ocr_text": first_present(record, ["ocr_text", "text"]),
        "products": first_present(record, ["products", "product_names"]),
        "brands": first_present(record, ["brands", "brand_names"]),
        "prices": first_present(record, ["prices", "price_text"]),
        "locations": first_present(record, ["locations", "location_clues"]),
        "scene": first_present(record, ["scene"]),
        "style_tags": first_present(record, ["style_tags", "styles", "tags"]),
        "objects": first_present(record, ["objects", "visual_objects"]),
        "pain_points": first_present(record, ["pain_points"]),
        "selling_points": first_present(record, ["selling_points", "hooks"]),
        "audience": first_present(record, ["audience"]),
        "evidence": first_present(record, ["evidence", "rationale"]),
        "confidence": first_present(record, ["confidence"]),
    }


def merge(notes: list[dict[str, Any]], images: list[dict[str, Any]]) -> list[dict[str, Any]]:
    notes_by_id = {note["note_id"]: note for note in map(normalize_note, notes) if note.get("note_id")}
    rows: list[dict[str, Any]] = []
    for image_record in map(normalize_image, images):
        note = notes_by_id.get(image_record.get("note_id", ""), {})
        row = {field: "" for field in FIELDS}
        row.update(note)
        row.update(image_record)
        rows.append(row)
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: stringify(row.get(field, "")) for field in FIELDS})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes", required=True, type=Path, help="JSONL note records")
    parser.add_argument("--images", required=True, type=Path, help="JSONL image insight records")
    parser.add_argument("--out", required=True, type=Path, help="CSV output path")
    parser.add_argument("--json-out", type=Path, help="Optional JSON output path")
    args = parser.parse_args()

    rows = merge(load_jsonl(args.notes), load_jsonl(args.images))
    write_csv(args.out, rows)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} image rows to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
