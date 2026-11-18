# -*- coding: utf-8 -*-
"""CALVOR campaign — single source of truth for 13 offer prices (gen + verify)."""

from __future__ import annotations

NBSP = "\u00a0"

GEOS: dict[str, dict] = {
    "762": {
        "geo": "hu",
        "lang": "hu",
        "tr": "hu",
        "price": 39999.00,
        "was": 79998.00,
        "currency": "HUF",
        "slug": "calvor",
        "cpa": 16.0,
    },
    "763": {
        "geo": "ro",
        "lang": "ro",
        "tr": "ro",
        "price": 379.00,
        "was": 758.00,
        "currency": "RON",
        "slug": "calvor",
        "cpa": 16.0,
    },
    "765": {
        "geo": "si",
        "lang": "sl",
        "tr": "si",
        "price": 79.00,
        "was": 158.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 16.0,
    },
    "1673": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "price": 89.00,
        "was": 178.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 17.0,
    },
    "1851": {
        "geo": "hr",
        "lang": "hr",
        "tr": "hr",
        "price": 99.00,
        "was": 198.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 16.0,
    },
    "2283": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "price": 89.00,
        "was": 180.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 17.0,
    },
    "2285": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "price": 89.00,
        "was": 178.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 20.0,
    },
    "2287": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 299.00,
        "was": 598.00,
        "currency": "PLN",
        "slug": "calvor",
        "cpa": 21.0,
    },
    "2289": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cs",
        "price": 1999.00,
        "was": 3998.00,
        "currency": "CZK",
        "slug": "calvor",
        "cpa": 18.0,
    },
    "3426": {
        "geo": "lv",
        "lang": "lv",
        "tr": "lv",
        "price": 99.00,
        "was": 198.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 18.0,
    },
    "3990": {
        "geo": "it",
        "lang": "it",
        "tr": "it",
        "price": 69.00,
        "was": 138.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 17.0,
        "folder": "calvor-3990",
    },
    "4067": {
        "geo": "sk",
        "lang": "sk",
        "tr": "sk",
        "price": 99.00,
        "was": 198.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 16.0,
    },
    "4276": {
        "geo": "lt",
        "lang": "lt",
        "tr": "lt",
        "price": 99.00,
        "was": 198.00,
        "currency": "EUR",
        "slug": "calvor",
        "cpa": 18.0,
    },
}


def list_was_price(cfg: dict) -> float:
    if "was" in cfg:
        return float(cfg["was"])
    return float(cfg["price"] * 2)


def fmt_price(amount: float, currency: str) -> str:
    sep = NBSP
    if currency == "CZK":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s}{sep}Kč"
    if currency == "PLN":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s}{sep}zł"
    if currency == "HUF":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s}{sep}Ft"
    if currency == "RON":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        if amount == int(amount) or abs(amount - whole) < 0.01:
            return f"{whole_s}{sep}lei"
        frac = int(round((amount - whole) * 100))
        return f"{whole_s},{frac:02d}{sep}lei"
    if amount == int(amount):
        return f"{int(amount)}{sep}€"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s}{sep}€"


def offer_folder(offer: str) -> str:
    cfg = GEOS[offer]
    if cfg.get("folder"):
        return cfg["folder"]
    return f"calvor-{offer}"


def formatted_pair(offer: str) -> tuple[str, str]:
    cfg = GEOS[offer]
    now = fmt_price(cfg["price"], cfg["currency"])
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    return now, was


VERIFY_ROWS: list[tuple[str, str, str, str, str, str]] = []
for oid, cfg in GEOS.items():
    now, was = formatted_pair(oid)
    VERIFY_ROWS.append(
        (cfg["geo"].upper(), oid, cfg["geo"], offer_folder(oid), now, was)
    )

VERIFY_ROWS.sort(key=lambda r: (r[0] != "IT", r[0]))

# Italian template literals used before i18n replace (now/was display).
IT_PRICE_NOW = formatted_pair("3990")[0]
IT_PRICE_WAS = formatted_pair("3990")[1]