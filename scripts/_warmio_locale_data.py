# -*- coding: utf-8 -*-
"""Native WARMIO phrase bundles (non-IT). Populated by seed_warmio_phrases."""

from __future__ import annotations

import importlib.util
from pathlib import Path

_LANG_DIR = Path(__file__).resolve().parent / "_warmio_langs"


def _load(code: str) -> dict[str, str]:
    path = _LANG_DIR / f"{code}.py"
    if not path.exists():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(f"warmio_{code}", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.PATCH)


def _all_codes() -> list[str]:
    return [
        "hu",
        "ro",
        "si",
        "pt",
        "hr",
        "es",
        "de",
        "pl",
        "cs",
        "lv",
        "sk",
        "lt",
    ]


LOCALE_PHRASES: dict[str, dict[str, str]] = {
    code: _load(code) for code in _all_codes()
}
