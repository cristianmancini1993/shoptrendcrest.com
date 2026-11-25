#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify generated LINVO™ geo landings."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OFFERS: dict[str, dict] = {
    "1912": {"geo": "de", "lang": "de", "price": 92.0, "currency": "EUR"},
    "1915": {"geo": "hu", "lang": "hu", "price": 29999.0, "currency": "HUF"},
    "2480": {"geo": "pt", "lang": "pt", "price": 79.0, "currency": "EUR"},
    "3163": {"geo": "es", "lang": "es", "price": 79.0, "currency": "EUR"},
    "3167": {"geo": "pl", "lang": "pl", "price": 339.0, "currency": "PLN"},
    "3169": {"geo": "cz", "lang": "cs", "price": 1899.0, "currency": "CZK"},
    "3910": {"geo": "lv", "lang": "lv", "price": 85.0, "currency": "EUR"},
    "4321": {"geo": "sk", "lang": "sk", "price": 74.0, "currency": "EUR"},
    "1897": {"geo": "it", "lang": "it", "price": 79.99, "currency": "EUR"},
}

ITALIAN_MARKERS = (
    "Domande frequenti",
    "Nessun anticipo",
    "Completa l'ordine",
    "Cliente verificata",
    "Ordina ora",
    "Chi siamo",
    "Reso entro 14 giorni",
    "Inserisci nome",
)

REQUIRED_ASSETS = (
    "/assets/css/orbimix-landing-alt-linvo.css",
    "/assets/img/products/linvo/hero.webp",
    "orbimix-landing.js",
)


def expected_price_substr(price: float, currency: str) -> list[str]:
    if currency == "EUR":
        if abs(price - round(price)) < 0.001:
            return [str(int(round(price))), "€"]
        return [f"{price:.2f}".replace(".", ","), "€"]
    if currency == "HUF":
        return [f"{int(round(price)):,}".replace(",", " "), "Ft"]
    if currency == "CZK":
        return [f"{int(round(price)):,}".replace(",", " "), "Kč"]
    if currency == "PLN":
        return ["zł", str(int(price)) if price == int(price) else ""]
    return []


def check_file(path: Path, offer: str, cfg: dict) -> list[str]:
    issues: list[str] = []
    if not path.is_file():
        return ["missing file"]
    text = path.read_text(encoding="utf-8")
    lang = cfg["lang"]
    geo = cfg["geo"]
    slug = f"linvo-{offer}"

    if path.name in ("landing.html", "index.html", "thank-you.html") or "thank-you" in path.parts:
        if f'lang="{lang}"' not in text and path.name != "index.html":
            issues.append(f"lang != {lang}")

    if path.name == "landing.html":
        if lang != "it":
            found = sum(1 for m in ITALIAN_MARKERS if m in text)
            if found >= 3:
                issues.append(f"possible Italian leftovers ({found} markers)")
        if f'value="{offer}"' not in text:
            issues.append("missing offer id in form hidden field")
        if "offers.adricenetwork.com" not in text:
            issues.append("missing adrice form action")
        if 'name="tel"' not in text or 'name="street-address"' not in text:
            issues.append("form field names not adrice-shaped")
        if "ORDER_DISABLED: true" in text:
            issues.append("ORDER_DISABLED still true")
        ty = f"https://shoptrendcrest.com/{geo}/{slug}/thank-you.html"
        if ty not in text:
            issues.append("thankyoupage url mismatch")
        for asset in REQUIRED_ASSETS:
            if asset not in text:
                issues.append(f"missing asset ref {asset}")
        parts = expected_price_substr(cfg["price"], cfg["currency"])
        if parts and parts[0] and parts[0] not in text:
            issues.append(f"price {cfg['price']} not found in HTML")

    if path.name == "thank-you.html":
        ty = f"https://shoptrendcrest.com/{geo}/{slug}/thank-you.html"
        if "thank-you.html" not in text and "canonical" in text:
            if ty not in text:
                issues.append("canonical thank-you url mismatch")
        if "AW-18510622150" not in text:
            issues.append("missing Google Ads tag")

    return issues


def main() -> int:
    ok = True
    warn_only = True
    for offer, cfg in OFFERS.items():
        geo = cfg["geo"]
        slug = f"linvo-{offer}"
        base = ROOT / geo / slug
        for rel in ("landing.html", "thank-you.html", "index.html", "thank-you/index.html"):
            p = base / rel if rel != "thank-you/index.html" else base / "thank-you" / "index.html"
            issues = check_file(p, offer, cfg)
            label = f"{geo}/{slug}/{rel}"
            if issues:
                i18n = all("Italian leftovers" in i for i in issues)
                if i18n:
                    print(f"WARN {label}: " + "; ".join(issues))
                else:
                    ok = False
                    warn_only = False
                    print(f"FAIL {label}: " + "; ".join(issues))
            else:
                print(f"OK   {label}")
    if not ok:
        return 1
    if warn_only:
        print("\nStructural checks passed. Re-run seed_linvo_locales.py with DEEPL_AUTH_KEY for full i18n.")
    else:
        print("\nAll LINVO geo checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())