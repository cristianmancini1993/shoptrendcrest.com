#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CENDORA™ translations for gen_cendora_geos (keys match IT_STRINGS)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from _cendora_align_locales import BLOCKED, FORM
from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS
from _cendora_native_packs import NATIVE_PACKS

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "content/cendora/locales"


def it_campaign_4373() -> dict[str, Any]:
    tr = dict(IT_STRINGS)
    tr["title"] = "CENDORA™ — Set Pentole antiaderente, 12 pezzi"
    tr["ty_product"] = "CENDORA™ — Set Pentole antiaderente, 12 pezzi"
    tr["kit_h"] = "Set Pentole CENDORA™ 12 pezzi, pronti all'uso"
    tr["cta_inline"] = tr["cta"]
    return tr


def _load_json(code: str) -> dict[str, Any] | None:
    path = LOCALES / f"{code}.json"
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if set(data) != set(IT_STRINGS):
        raise AssertionError(f"{path}: key mismatch")
    return data


def _finalize(lang: str, base: dict[str, Any]) -> dict[str, Any]:
    loc = dict(base)
    if lang in FORM:
        loc.update(FORM[lang])
    if lang in BLOCKED:
        loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[lang]
    loc["ty_alt"] = IT_STRINGS["ty_alt"]
    if "cta" in loc:
        loc["cta_inline"] = loc["cta"]
    return loc


TRANSLATIONS: dict[str, dict[str, Any]] = {}
for code in ("ro", "pt", "sk", "si", "hr", "hu", "es", "de", "lt", "pl", "cs", "lv", "el"):
    loaded = _load_json(code)
    if loaded is not None:
        TRANSLATIONS[code] = _finalize(code, loaded)
    elif code in NATIVE_PACKS:
        TRANSLATIONS[code] = _finalize(code, dict(NATIVE_PACKS[code]))
    else:
        TRANSLATIONS[code] = _finalize(code, _ro())

TRANSLATIONS["it"] = _finalize("it", it_campaign_4373())


def _validate() -> None:
    expected = set(IT_STRINGS)
    for code, data in TRANSLATIONS.items():
        missing = expected - set(data)
        if missing:
            raise AssertionError(f"{code}: missing {len(missing)} keys e.g. {sorted(missing)[:3]}")


_validate()
