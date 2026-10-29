#!/usr/bin/env python3
"""Validate local source path and line-range references in docs/. No model calls."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = re.compile(r"(?P<path>sources/[A-Za-z0-9_./-]+\.md)#L(?P<start>[1-9][0-9]*)(?:-L?(?P<end>[1-9][0-9]*))?")


def main() -> int:
    errors: list[str] = []
    references = 0
    for document in sorted((ROOT / "docs").glob("*.md")):
        text = document.read_text(encoding="utf-8")
        for match in REFERENCE.finditer(text):
            references += 1
            source = ROOT / match.group("path")
            if not source.is_file():
                errors.append(f"{document.relative_to(ROOT)}: missing {match.group('path')}")
                continue
            line_count = len(source.read_text(encoding="utf-8").splitlines())
            start = int(match.group("start"))
            end = int(match.group("end") or start)
            if start > end or end > line_count:
                errors.append(f"{document.relative_to(ROOT)}: invalid {match.group(0)} (source has {line_count} lines)")
    if not references:
        errors.append("no source references found in docs/")
    if errors:
        print("Source-link check failed:", *errors, sep="\n- ", file=sys.stderr)
        return 1
    print(f"Source-link check passed: {references} local references in docs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
