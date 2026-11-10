# -*- coding: utf-8 -*-
from __future__ import annotations

import importlib

_LOCALE_MODULES = {
    "hu": "locale_hu",
    "ro": "locale_ro",
    "si": "locale_si",
    "pt": "locale_pt",
    "hr": "locale_hr",
    "es": "locale_es",
    "de": "locale_de",
    "pl": "locale_pl",
    "cs": "locale_cs",
    "lv": "locale_lv",
    "sk": "locale_sk",
    "lt": "locale_lt",
}

def _load(code: str) -> dict:
    mod = importlib.import_module(_LOCALE_MODULES[code])
    return dict(mod.STRINGS)

GEO_TRANSLATIONS: dict[str, dict] = {
    "hu": _load("hu"),
    "ro": _load("ro"),
    "si": _load("si"),
    "pt": _load("pt"),
    "hr": _load("hr"),
    "es": _load("es"),
    "de": _load("de"),
    "pl": _load("pl"),
    "cs": _load("cs"),
    "lv": _load("lv"),
    "sk": _load("sk"),
    "lt": _load("lt"),
}

from _zelto_footer_extra import FOOTER_EXTRA

for _code, _extra in FOOTER_EXTRA.items():
    GEO_TRANSLATIONS[_code].update(_extra)
