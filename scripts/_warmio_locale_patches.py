# -*- coding: utf-8 -*-
"""Full native WARMIO phrase bundles per geo."""

from _warmio_patch_common import validate_bundle
from _warmio_langs import cs, de, es, hr, hu, it, lt, lv, pl, pt, ro, si, sk

LOCALE_PATCH: dict[str, dict[str, str]] = {
    "it": it.PATCH,
    "lt": lt.PATCH,
    "es": es.PATCH,
    "pt": pt.PATCH,
    "pl": pl.PATCH,
    "cs": cs.PATCH,
    "ro": ro.PATCH,
    "sk": sk.PATCH,
    "si": si.PATCH,
    "hr": hr.PATCH,
    "hu": hu.PATCH,
    "de": de.PATCH,
    "lv": lv.PATCH,
}

for _code, _bundle in LOCALE_PATCH.items():
    validate_bundle(_code, _bundle)
