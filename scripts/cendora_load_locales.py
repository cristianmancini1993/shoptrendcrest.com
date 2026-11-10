#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Load and validate content/cendora/locales/*.json against IT_STRINGS."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "content/cendora/locales"

# Offer lang → locale file stem
OFFER_LANG: dict[str, str] = {
    "ro": "ro",
    "pt": "pt",
    "sk": "sk",
    "si": "sl",
    "hr": "hr",
    "hu": "hu",
    "es": "es",
    "de": "de",
    "lt": "lt",
    "pl": "pl",
    "cz": "cs",
    "lv": "lv",
    "it": "it",
}

REQUIRED_LOCALES = frozenset(OFFER_LANG.values())


def load_it_strings() -> dict[str, Any]:
    from _cendora_it_strings import IT_STRINGS  # noqa: WPS433

    return dict(IT_STRINGS)


def load_translations() -> dict[str, dict[str, Any]]:
    """All locale JSON files (stem → dict)."""
    if not LOCALES_DIR.is_dir():
        raise FileNotFoundError(f"Missing {LOCALES_DIR}")
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(LOCALES_DIR.glob("*.json")):
        out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return out


def validate(translations: dict[str, dict[str, Any]], it: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing_files = REQUIRED_LOCALES - set(translations)
    if missing_files:
        errors.append(f"Missing locale files: {', '.join(sorted(missing_files))}")
    expected = set(it)
    for code in sorted(REQUIRED_LOCALES):
        if code not in translations:
            continue
        data = translations[code]
        keys = set(data)
        miss = expected - keys
        extra = keys - expected
        if miss:
            errors.append(f"{code}.json: missing keys ({len(miss)}): {sorted(miss)[:8]}…")
        if extra:
            errors.append(f"{code}.json: extra keys ({len(extra)}): {sorted(extra)[:8]}…")
    return errors


def main() -> int:
    it = load_it_strings()
    tr = load_translations()
    errors = validate(tr, it)
    if errors:
        print("cendora_load_locales: FAILED", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"OK: {len(tr)} locale files, {len(it)} keys each")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
