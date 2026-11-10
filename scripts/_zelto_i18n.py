# -*- coding: utf-8 -*-
"""ZELTO landing translations — IT from _zelto_it_strings; geos from locale_*.py."""
from __future__ import annotations

from _zelto_it_strings import IT_STRINGS
from _zelto_i18n_data import GEO_TRANSLATIONS

TRANSLATIONS: dict[str, dict] = {
    "it": dict(IT_STRINGS),
    **GEO_TRANSLATIONS,
}
