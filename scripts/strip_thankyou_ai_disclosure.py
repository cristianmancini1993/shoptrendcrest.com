#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove AI footer disclosure from thank-you pages only."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAT = re.compile(
    r'<p class="(?:site-footer__ai-disclosure|gsh-standalone-footer__ai-disclosure)"[^>]*>.*?</p>\s*',
    re.DOTALL | re.IGNORECASE,
)


def main() -> None:
    n = 0
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT).as_posix()
        if "thank-you" not in rel and not rel.endswith("thank-you.html"):
            continue
        raw = p.read_text(encoding="utf-8")
        new = PAT.sub("", raw)
        if new != raw:
            p.write_text(new, encoding="utf-8")
            n += 1
            print(f"Stripped {rel}")
    print(f"Done: {n} file(s)")


if __name__ == "__main__":
    main()
