#!/usr/bin/env python3
"""Per-offer form labels/placeholders + confirmed lp/_key only (Granvia™)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from _granvia_form_examples import GRANVIA_FORM_EXAMPLES, GRANVIA_NAME_LABEL_OVERRIDES  # noqa: E402
_SITE = json.loads((ROOT / "content/granvia/site.json").read_text(encoding="utf-8"))
SITE_DOMAIN: str = (_SITE.get("domain") or "").strip().replace("https://", "").rstrip("/")
PRODUCT_SLUG: str = (_SITE.get("product_slug") or "").strip()

# Confirmed Adrice lp/_key (buyer network embeds).
OFFER_LP_KEY: dict[str, tuple[str, str]] = {
    "3047": ("3081", "65f31e51164273ded5aa79533c4957ea238776fd"),
    "3048": ("3082", "f9c97e9dba4f2c16db0517c3e678fc0670d43a05"),
    "3049": ("3083", "fce8930d8add42d6b04fc707ee9a88e4341bc194"),
    "3050": ("3084", "e9a913ea364ad2a1418db1423763579f6bda8dbb"),
    "3052": ("3086", "04d58879e2c3af9f0c1d1dcab6a08dbe9d017626"),
    "3053": ("3087", "a8dc09278720d024d9c7890363bc8977eee812db"),
}

_OFFERS = json.loads((ROOT / "content/granvia/offers.json").read_text(encoding="utf-8"))
_LOCALES = ROOT / "content/granvia/locales"

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
    if lang in GRANVIA_FORM_EXAMPLES:
        for key, expected in GRANVIA_FORM_EXAMPLES[lang].items():
            actual = str(loc.get(key, "")).strip()
            if actual != expected:
                raise ValueError(
                    f"offer {offer_id} locale {lang}: {key} must be {expected!r}, got {actual!r}"
                )
        want_label = GRANVIA_NAME_LABEL_OVERRIDES.get(lang)
        if want_label and str(loc.get("label_name", "")).strip() != want_label:
            raise ValueError(
                f"offer {offer_id} locale {lang}: label_name must be {want_label!r}"
            )
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
