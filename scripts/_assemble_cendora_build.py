#!/usr/bin/env python3
"""Assemble final build_cendora_i18n.py (single TRANSLATIONS dict)."""
from __future__ import annotations

import importlib
import pprint
from pathlib import Path
from typing import Any

from _cendora_align_locales import BLOCKED, FORM
from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

# Native product+UI packs keyed by locale code (keys match IT_STRINGS).
from _cendora_native_packs import NATIVE_PACKS  # noqa: WPS433

ROOT = Path(__file__).resolve().parent


def _load_aligned() -> dict[str, dict[str, Any]]:
    import build_cendora_i18n as mod

    importlib.reload(mod)
    return dict(mod.TRANSLATIONS)


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


def main() -> None:
    aligned = _load_aligned()
    premium = {"ro", "pt", "es", "de"}
    out: dict[str, dict[str, Any]] = {}
    for lang in ("ro", "pt", "sk", "si", "hr", "hu", "es", "de", "lt", "pl", "cs", "lv"):
        if lang in premium:
            base: dict[str, Any] = dict(NATIVE_PACKS[lang])
        else:
            base = dict(aligned.get(lang, NATIVE_PACKS[lang]))
            base.update(NATIVE_PACKS[lang])
        out[lang] = _finalize(lang, base)
        for k, it_val in IT_STRINGS.items():
            if k not in out[lang]:
                out[lang][k] = NATIVE_PACKS.get(lang, _ro()).get(k, _ro()[k])
            elif isinstance(it_val, str) and out[lang][k] == it_val:
                fallback = aligned.get(lang, {}).get(k) or NATIVE_PACKS.get(lang, {}).get(k) or _ro()[k]
                out[lang][k] = fallback
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
    (ROOT / "build_cendora_i18n.py").write_text(
        header + pprint.pformat(out, width=120, sort_dicts=False) + footer,
        encoding="utf-8",
    )
    print("assembled", len(out), "locales")


if __name__ == "__main__":
    main()
