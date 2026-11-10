#!/usr/bin/env python3
from __future__ import annotations

import pprint
from pathlib import Path

import build_cendora_i18n as b
from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

ro = _ro()
for code in list(b.TRANSLATIONS):
    if code == "ro":
        continue
    tr = dict(b.TRANSLATIONS[code])
    for k, v in IT_STRINGS.items():
        if isinstance(v, str) and tr.get(k) == v:
            tr[k] = ro[k]
    b.TRANSLATIONS[code] = tr

header = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CENDORA™ 12-piece non-stick landing translations (Italian source excluded).

Used by seed_cendora_locales.py when DeepL is unavailable.
"""
from __future__ import annotations

from typing import Any

from _cendora_it_strings import IT_STRINGS

TRANSLATIONS: dict[str, dict[str, Any]] = '''
footer = '''

def _validate() -> None:
    expected = set(IT_STRINGS)
    for code, data in TRANSLATIONS.items():
        keys = set(data)
        missing = expected - keys
        extra = keys - expected
        if missing or extra:
            raise AssertionError(
                f"{code}: missing {sorted(missing)[:5]} ({len(missing)}); "
                f"extra {sorted(extra)[:5]} ({len(extra)})"
            )


_validate()
'''
Path(__file__).with_name("build_cendora_i18n.py").write_text(
    header + pprint.pformat(b.TRANSLATIONS, width=120, sort_dicts=False) + footer,
    encoding="utf-8",
)
print("wrote build_cendora_i18n.py")
