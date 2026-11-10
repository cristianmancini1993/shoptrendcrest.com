#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove postal-code and city fields from order forms; keep 3 fields only."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# label + input (optional <br>) for postal / city
EXTRA_FIELD = re.compile(
    r"\s*<label for=\"(?:postal-code\d*|address-level2\d*)\">[^<]*</label>\s*"
    r"<input[^>]*(?:postal-code|address-level2)[^>]*>\s*(?:<br>\s*)?",
    re.IGNORECASE,
)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    updated = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "postal-code" not in text and "address-level2" not in text:
            continue
        new_text, n = EXTRA_FIELD.subn("", text)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print(f"stripped {n} extra field(s) from {path.relative_to(ROOT)}")
            updated += 1

    print(f"done ({updated} files)")


if __name__ == "__main__":
    main()
