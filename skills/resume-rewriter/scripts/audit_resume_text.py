#!/usr/bin/env python3
"""Heuristic resume text audit for overclaiming and vague bullets."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Finding:
    file: str
    line: int
    severity: str
    rule: str
    message: str
    excerpt: str


RULES: list[tuple[str, str, re.Pattern[str], str]] = [
    (
        "review",
        "inflated_ownership",
        re.compile(r"(主导|带领|管理|全权负责|owner|owned|led|architected|from 0 to 1|从0到1)", re.I),
        "High-ownership wording needs source evidence for decision authority, scope, and result.",
    ),
    (
        "improve",
        "vague_participation",
        re.compile(r"(参与|协助|支持|负责相关|负责.*工作|跟进|整理|participated|assisted|supported|responsible for)", re.I),
        "Vague participation language should be replaced with specific action, method, and deliverable.",
    ),
    (
        "review",
        "subjective_trait",
        re.compile(r"(熟悉|掌握|深入理解|较强|优秀|良好|strong|excellent|familiar with|proficient in)", re.I),
        "Subjective ability claims should be backed by observable work or removed.",
    ),
    (
        "review",
        "empty_quantification",
        re.compile(r"(提升|增长|降低|减少|提高|increase|decrease|improve|reduce).{0,20}(\d+(?:\.\d+)?%)", re.I),
        "Percentage impact should include baseline, denominator, or business meaning.",
    ),
    (
        "info",
        "needs_confirmation",
        re.compile(r"(\[待确认\]|待确认|needs confirmation|TBC|TBD)", re.I),
        "Confirmation marker found; keep it visible until the user verifies the fact.",
    ),
]


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def audit_text(text: str, file_label: str = "<text>") -> list[Finding]:
    findings: list[Finding] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        for severity, rule, pattern, message in RULES:
            if pattern.search(line):
                findings.append(
                    Finding(
                        file=file_label,
                        line=line_no,
                        severity=severity,
                        rule=rule,
                        message=message,
                        excerpt=line[:220],
                    )
                )
    return findings


def format_text(findings: list[Finding]) -> str:
    if not findings:
        return "No heuristic resume risks found."

    lines = [f"{len(findings)} heuristic resume risk(s) found:"]
    for item in findings:
        lines.append(
            f"- [{item.severity}] {item.file}:{item.line} {item.rule}: "
            f"{item.message}\n  > {item.excerpt}"
        )
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit resume text for vague wording, inflated ownership, and unsupported quantification."
    )
    parser.add_argument("paths", nargs="*", help="Text-like resume files to audit.")
    parser.add_argument("--text", help="Audit a text string instead of files.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if not args.paths and args.text is None:
        print("Provide at least one file path or --text.", file=sys.stderr)
        return 2

    findings: list[Finding] = []

    if args.text is not None:
        findings.extend(audit_text(args.text))

    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            findings.append(
                Finding(
                    file=str(path),
                    line=0,
                    severity="error",
                    rule="file_missing",
                    message="File does not exist.",
                    excerpt="",
                )
            )
            continue
        findings.extend(audit_text(read_text(path), str(path)))

    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    else:
        print(format_text(findings))

    return 1 if any(item.severity in {"review", "error"} for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
