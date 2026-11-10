#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ensure ?v=20260926 on all trimex product image URLs in campaign landings."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_VERSION = "20260926"
IMG_RE = re.compile(
    r"(?P<prefix>/assets/img/products/trimex/[^\"'?\\s>]+)"
    r"(?P<q>\?v=[0-9]+)?"
)


def fix_html(text: str) -> tuple[str, int]:
    n = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal n
        n += 1
        return f"{m.group('prefix')}?v={TARGET_VERSION}"

    return IMG_RE.sub(repl, text), n


def main() -> None:
    paths = sorted(ROOT.glob("**/trimex-*/index.html"))
    paths.append(ROOT / "it/trimex-3209/index.html")
    total = 0
    for path in paths:
        if "it/trimex/index.html" in path.as_posix():
            continue
        text = path.read_text(encoding="utf-8")
        new_text, n = fix_html(text)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: {n} image URL(s) updated")
        total += n
    print(f"done ({total} updates)")


if __name__ == "__main__":
    main()
