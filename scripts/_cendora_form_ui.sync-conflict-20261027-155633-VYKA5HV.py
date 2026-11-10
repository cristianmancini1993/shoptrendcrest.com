#!/usr/bin/env python3
"""Per-offer form labels/placeholders + confirmed lp/_key only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SITE = json.loads((ROOT / "content/cendora/site.json").read_text(encoding="utf-8"))
SITE_DOMAIN: str = (_SITE.get("domain") or "").strip().replace("https://", "").rstrip("/")
PRODUCT_SLUG: str = (_SITE.get("product_slug") or "").strip()

OFFER_LP_KEY: dict[str, tuple[str, str]] = {
    "1476": ("1496", "31e9407b5c50cced10662c864645101050908a07"),
}

OFFER_GEO: dict[str, str] = {
    "1387": "ro",
    "1476": "pt",
    "1874": "sk",
    "1875": "si",
    "1876": "hr",
    "2409": "hu",
    "3176": "es",
    "3177": "de",
    "3178": "lt",
    "3179": "pl",
    "3251": "cz",
    "4095": "lv",
    "4373": "it",
}

OFFER_TR: dict[str, str] = {
    "1387": "ro",
    "1476": "pt",
    "1874": "sk",
    "1875": "si",
    "1876": "hr",
    "2409": "hu",
    "3176": "es",
    "3177": "de",
    "3178": "lt",
    "3179": "pl",
    "3251": "cs",
    "4095": "lv",
    "4373": "it",
}


def _ui_from_tr(tr: dict[str, str]) -> dict[str, str]:
    return {
        "name_l": tr["label_name"],
        "name_p": tr["ph_name"],
        "tel_l": tr["label_tel"],
        "tel_p": tr["ph_tel"],
        "addr_l": tr["label_addr"],
        "addr_p": tr["ph_addr"],
        "submit": tr["submit_btn"],
        "form_note": tr.get("form_note_form", ""),
        "form_blocked_msg": tr.get("form_blocked_msg", ""),
        "form_blocked_btn": tr.get("form_blocked_btn", ""),
        "blocked_msg": tr.get("form_blocked_msg", ""),
        "blocked_btn": tr.get("form_blocked_btn", ""),
    }


def sync_form_ui(translations: dict[str, dict]) -> None:
    global FORM_UI
    FORM_UI = {}
    for oid, tr_code in OFFER_TR.items():
        tr = translations.get(tr_code)
        if not tr or "label_name" not in tr:
            continue
        FORM_UI[oid] = _ui_from_tr(tr)


FORM_UI: dict[str, dict[str, str]] = {
    oid: {
        "name_l": "…",
        "name_p": "…",
        "tel_l": "…",
        "tel_p": "…",
        "addr_l": "…",
        "addr_p": "…",
        "submit": "…",
        "form_note": "",
        "form_blocked_msg": "",
        "form_blocked_btn": "",
    }
    for oid in OFFER_GEO
}
