#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install or update Google Ads gtag pixel across all HTML pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_ID = "AW-18360728507"
NEW_ID = "AW-18421302840"

GTAG_BLOCK = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={NEW_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{NEW_ID}');
</script>"""

HEAD_INSERT = re.compile(r"(<head[^>]*>)", re.IGNORECASE)


def update_content(content: str, *, add_if_missing: bool) -> str:
    updated = content.replace(OLD_ID, NEW_ID)
    if add_if_missing and "googletagmanager.com/gtag/js" not in updated:
        updated = HEAD_INSERT.sub(r"\1\n" + GTAG_BLOCK, updated, count=1)
    return updated


def main() -> None:
    changed: list[Path] = []

    for pattern in ("**/*.html", "assets/js/*.js", "scripts/gen_kemppi_geos.py", "scripts/gen_glacierair_geos.py"):
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            original = path.read_text(encoding="utf-8")
            updated = update_content(original, add_if_missing=path.suffix == ".html")
            if updated != original:
                path.write_text(updated, encoding="utf-8", newline="\n")
                changed.append(path)

    print(f"Updated {len(changed)} files")
    missing = [
        p for p in ROOT.glob("**/*.html")
        if "googletagmanager.com/gtag/js" not in p.read_text(encoding="utf-8")
    ]
    print(f"HTML without gtag after update: {len(missing)}")
    for path in sorted(changed)[:10]:
        print(f"  {path.relative_to(ROOT)}")
    if len(changed) > 10:
        print(f"  ... and {len(changed) - 10} more")


if __name__ == "__main__":
    main()
