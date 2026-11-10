#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Smoke-check FLAMORA fireplace landings (local files or live URL base)."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = sys.argv[1] if len(sys.argv) > 1 else ""

SITES = [
    ("pl/flamora-1987", "399 zł", "798 zł", "1987", "2008"),
    ("cz/flamora-2400", "2 290 Kč", "4 580 Kč", "2400", "2425"),
    ("es/flamora-2635", "96 €", "192 €", "2635", "2662"),
    ("pt/flamora-2636", "112 €", "224 €", "2636", "2663"),
    ("de/flamora-2665", "89 €", "178 €", "2665", "2692"),
    ("hu/flamora-2668", "29 999 Ft", "59 998 Ft", "2668", "2695"),
    ("sk/flamora-4357", "97 €", "194 €", "4357", "4397"),
    ("lv/flamora-4358", "99 €", "198 €", "4358", "4398"),
]

BAD_FRAGMENTS = [
    "kamīnzāle",
    "TĀLVADĪBAS PULS",
    "gewählt",
    "W PREZENTE",
    "kurýru",
    "kuriéru",
    ", a ott ",
    "metros recomendados",
    "On/off",
    "nie publikujemy",
    "kamīnss",
]

FORM_ORDER = re.compile(
    r'label for="name".*?label for="tel".*?label for="street-address"',
    re.DOTALL | re.IGNORECASE,
)


def load(rel: str, name: str) -> str:
    if BASE:
        url = f"{BASE.rstrip('/')}/{rel}/{name}"
        with urlopen(url, timeout=30) as r:
            return r.read().decode("utf-8", "replace")
    return (ROOT / rel / name).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    for rel, now, was, offer, lp in SITES:
        for page in ("index.html", "thank-you.html"):
            try:
                html = load(rel, page)
            except Exception as e:
                errors.append(f"{rel}/{page}: fetch failed: {e}")
                continue
            if page == "index.html":
                if now not in html:
                    errors.append(f"{rel}: missing price {now}")
                if was not in html and "-50%" in html:
                    errors.append(f"{rel}: missing was price {was}")
                if f'value="{offer}"' not in html:
                    errors.append(f"{rel}: missing offer {offer}")
                if f"FORM_OFFER: '{offer}'" not in html and f'value="{offer}"' not in html:
                    errors.append(f"{rel}: offer id not in page")
                if f'value="{lp}"' not in html:
                    errors.append(f"{rel}: missing lp {lp}")
                if not FORM_ORDER.search(html):
                    errors.append(f"{rel}: form field order not name→tel→address")
                for bad in BAD_FRAGMENTS:
                    if bad in html:
                        errors.append(f"{rel}: contains bad fragment «{bad}»")
                if "žádanou teplotu" not in html and "požadovanou teplotu" not in html:
                    if rel.startswith("pl/"):
                        if "żądaną temperaturę" not in html:
                            errors.append(f"{rel}: block 01 temp semantics missing")
                    elif rel.startswith("de/"):
                        if "gewünschte Temperatur" not in html:
                            errors.append(f"{rel}: block 01 temp semantics missing")
            if "thank-you" in page:
                ty = f"/{rel}/thank-you.html"
                if ty not in html and rel.replace("/", "/") in html:
                    pass
    if errors:
        print("FAILURES:")
        for e in errors:
            print(" -", e)
        return 1
    print(f"OK: {len(SITES) * 2} pages checked ({BASE or 'local'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
