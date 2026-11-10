#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify generated AUREN fireplace geo landings."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED = [
    {"geo": "pl", "lang": "pl", "offer_id": "1987", "currency": "PLN", "price": 399},
    {"geo": "cz", "lang": "cs", "offer_id": "2400", "currency": "CZK", "price": 2290},
    {"geo": "es", "lang": "es", "offer_id": "2635", "currency": "EUR", "price": 96},
    {"geo": "pt", "lang": "pt", "offer_id": "2636", "currency": "EUR", "price": 112},
    {"geo": "de", "lang": "de", "offer_id": "2665", "currency": "EUR", "price": 89},
    {"geo": "hu", "lang": "hu", "offer_id": "2668", "currency": "HUF", "price": 29999},
    {"geo": "sk", "lang": "sk", "offer_id": "4357", "currency": "EUR", "price": 97},
    {"geo": "lv", "lang": "lv", "offer_id": "4358", "currency": "EUR", "price": 99},
]

CPA_DISPLAY_FORBIDDEN = re.compile(r"\b(cpa|CPA)\b")


def check_file(path: Path, offer: dict) -> list[str]:
    errs: list[str] = []
    if not path.exists():
        return [f"missing {path.relative_to(ROOT)}"]

    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()

    if f'lang="{offer["lang"]}"' not in text:
        errs.append(f'{rel}: expected lang="{offer["lang"]}"')
    if f'content="{offer["offer_id"]}"' not in text:
        errs.append(f"{rel}: wrong offer-id meta")
    if "AUREN" not in text:
        errs.append(f"{rel}: missing AUREN brand")
    if CPA_DISPLAY_FORBIDDEN.search(text):
        errs.append(f"{rel}: CPA must not appear on page")

    slug = f"auren-{offer['offer_id']}"
    if f"PRODUCT_SLUG: '{slug}'" not in text:
        errs.append(f"{rel}: wrong PRODUCT_SLUG")
    if f"  PRICE: {offer['price']}," not in text:
        errs.append(f"{rel}: wrong SITE_CONFIG PRICE")
    if f"  CURRENCY: '{offer['currency']}'," not in text:
        errs.append(f"{rel}: wrong CURRENCY")

    if path.name == "index.html":
        if f"/{offer['geo']}/about-us.html" not in text:
            errs.append(f"{rel}: footer legal links should use /{offer['geo']}/")

    return errs


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    all_errs: list[str] = []
    for offer in EXPECTED:
        slug = f"auren-{offer['offer_id']}"
        rel_dir = ROOT / offer["geo"] / slug
        all_errs.extend(check_file(rel_dir / "index.html", offer))
        all_errs.extend(check_file(rel_dir / "thank-you.html", offer))

    if all_errs:
        for e in all_errs:
            print(f"FAIL: {e}")
        return 1

    print("OK: all 8 AUREN geos verified (price, offer id, lang, brand)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
