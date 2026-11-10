#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace per-page Google Font links with shared /assets/css/fonts.css."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTS_LINK = '<link rel="stylesheet" href="/assets/css/fonts.css?v=20261029">'
FONT_CSS_RE = re.compile(
    r'<link[^>]+href="https://fonts\.googleapis\.com/css2\?family=(?:Montserrat|Poppins)[^"]*"[^>]*/?\s*>',
    re.IGNORECASE,
)
VARS_RE = re.compile(r'(<link[^>]+href="/assets/css/variables\.css)([^"]*)(")')

SKIP = {"node_modules", ".git", "scripts/_tmp"}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP)


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    if FONT_CSS_RE.search(text):
        text = FONT_CSS_RE.sub(FONTS_LINK, text, count=1)
        # Drop duplicate font css links if any remain
        while FONT_CSS_RE.search(text):
            text = FONT_CSS_RE.sub("", text, count=1)
    elif "/assets/css/variables.css" in text and FONTS_LINK not in text:
        text = VARS_RE.sub(rf"\1?v=20261029\3\n{FONTS_LINK}", text, count=1)
    elif "/assets/css/glacierair-landing.css" in text and FONTS_LINK not in text:
        text = text.replace(
            '<link rel="stylesheet" href="/assets/css/glacierair-landing.css',
            f"{FONTS_LINK}\n<link rel=\"stylesheet\" href=\"/assets/css/glacierair-landing.css",
            1,
        )

    text = text.replace(
        'href="/assets/css/variables.css"',
        'href="/assets/css/variables.css?v=20261029"',
    )
    text = text.replace(
        "href='/assets/css/variables.css'",
        "href='/assets/css/variables.css?v=20261029'",
    )
    # nuvia inline Montserrat override
    text = text.replace("font-family: Montserrat, Arial, sans-serif", "font-family: var(--font-base)")

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.html"):
        if should_skip(path):
            continue
        if patch_file(path):
            changed += 1
            print(path.relative_to(ROOT))
    print(f"done: {changed} files")


if __name__ == "__main__":
    main()
