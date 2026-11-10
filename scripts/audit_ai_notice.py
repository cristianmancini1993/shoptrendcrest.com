#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.ai_image_notice_i18n import footer_ai_notice_complete

LANG_RE = re.compile(r'<html[^>]*\blang\s*=\s*["\']([^"\']+)["\']', re.I)


def main() -> None:
    missing: list[str] = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if "thank-you" in rel:
            continue
        if p.name not in ("index.html", "landing.html"):
            continue
        raw = p.read_text(encoding="utf-8")
        if "assets/img/products" not in raw:
            continue
        if "<footer" not in raw.lower():
            continue
        if "window.location.replace" in raw and "<footer" not in raw.lower():
            continue
        lang = LANG_RE.search(raw)
        lang_s = lang.group(1) if lang else rel.split("/")[0]
        if not footer_ai_notice_complete(raw, lang_s):
            missing.append(rel)
    print(f"Incomplete/missing AI notice: {len(missing)}")
    for r in missing:
        print(r)


if __name__ == "__main__":
    main()
