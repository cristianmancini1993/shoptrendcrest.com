#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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


def save(code: str, patch: dict) -> None:
    data = base_from_it()
    data.update(patch)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{code}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
