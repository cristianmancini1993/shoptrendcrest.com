#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write content/cendora/locales/*.json (hand-tuned native copy)."""
from __future__ import annotations

import json
from pathlib import Path

from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "content/cendora/locales"


def base_from_it() -> dict:
    d: dict = {}
    for k, v in IT_STRINGS.items():
        d[k] = list(v) if isinstance(v, tuple) else v
    return d


def write(code: str, data: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{code}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


# Locales are appended in emit_cendora_locales_data.py
from emit_cendora_locales_data import LOCALE_PATCHES  # noqa: E402


def main() -> None:
    for code, patch in LOCALE_PATCHES.items():
        data = base_from_it()
        data.update(patch)
        write(code, data)
        print(f"wrote {code}.json ({len(data)} keys)")


if __name__ == "__main__":
    main()
