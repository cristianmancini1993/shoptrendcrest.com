#!/usr/bin/env python3
"""Per-offer form labels/placeholders + confirmed lp/_key only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SITE = json.loads((ROOT / "content/cendora/site.json").read_text(encoding="utf-8"))
SITE_DOMAIN: str = (_SITE.get("domain") or "").strip().replace("https://", "").rstrip("/")
PRODUCT_SLUG: str = (_SITE.get("product_slug") or "").strip()

# Confirmed Adrice lp/_key (buyer network embeds).
OFFER_LP_KEY: dict[str, tuple[str, str]] = {
    "1387": ("1406", "bfaf8a8d8f3f5285fbf87c3616581b86f6886e9b"),
    "1476": ("1496", "31e9407b5c50cced10662c864645101050908a07"),
    "1874": ("1894", "0fb3b777d6284f2618ee6119070651547029e2a3"),
    "1875": ("1895", "d16aa4ee0aa82cb50fccbf992a6cf6447a237290"),
    "1876": ("1896", "aff24016433518c2a9c8192afe693f24d9c817c8"),
    "2409": ("2434", "ba45ebc620cdf881f6b555ebf345c213e544ae0b"),
    "3176": ("3210", "ef1eecc2ab3ddc7b01bdc1ecee2c9a5c76a0400b"),
    "3177": ("3211", "feaaf365b3bfd853b4fc9b265145b08a57bafe55"),
    "3178": ("3212", "554b43383d85970a492667f31cd6bdb35030ae11"),
    "3179": ("3213", "9284f944be23b667b5f083f1c256ac6773e78073"),
    "3251": ("3285", "d31410347f6a0eeeefaef2785028354e02323e51"),
    "4095": ("4135", "846167920ffa5186bf49e51c085dd25da88ee156"),
    "4373": ("4413", "a0dd47dd694477be3a228c4b7c62eee06108e06c"),
}

_OFFERS = json.loads((ROOT / "content/cendora/offers.json").read_text(encoding="utf-8"))
_LOCALES = ROOT / "content/cendora/locales"

OFFER_GEO: dict[str, str] = {str(o["id"]): o["geo"] for o in _OFFERS}
OFFER_LANG: dict[str, str] = {str(o["id"]): o["lang"] for o in _OFFERS}


def _form_ui_for_offer(offer_id: str, lang: str) -> dict[str, str]:
    path = _LOCALES / f"{lang}.json"
    if not path.is_file():
        raise FileNotFoundError(f"Missing locale for offer {offer_id}: {path}")
    loc = json.loads(path.read_text(encoding="utf-8"))
    required = (
        "label_name",
        "label_tel",
        "label_addr",
        "ph_name",
        "ph_tel",
        "ph_addr",
        "submit_btn",
        "form_blocked_msg",
        "form_blocked_btn",
        "form_note_form",
    )
    missing = [k for k in required if k not in loc or not str(loc[k]).strip()]
    if missing:
        raise KeyError(f"offer {offer_id} locale {lang}: missing form keys {missing}")
    return {
        "name_l": loc["label_name"],
        "name_p": loc["ph_name"],
        "tel_l": loc["label_tel"],
        "tel_p": loc["ph_tel"],
        "addr_l": loc["label_addr"],
        "addr_p": loc["ph_addr"],
        "submit": loc["submit_btn"],
        "form_note": loc["form_note_form"],
        "blocked_msg": loc["form_blocked_msg"],
        "blocked_btn": loc["form_blocked_btn"],
        "v_name": loc.get("err_name", loc["label_name"]),
        "v_tel": loc.get("err_tel", loc["label_tel"]),
        "v_addr": loc.get("err_addr", loc["label_addr"]),
    }


FORM_UI: dict[str, dict[str, str]] = {
    str(o["id"]): _form_ui_for_offer(str(o["id"]), o["lang"]) for o in _OFFERS
}
