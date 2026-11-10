#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate complete RO locale (_ro) to all campaign languages via MyMemory."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from _cendora_i18n_embed import _ro
from _gen_cendora_i18n_once import BLOCKED, FORM

OUT = Path(__file__).with_name("_cendora_locales_all.json")
CACHE = Path(__file__).with_name("_cendora_translate_cache.json")

TARGETS = {
    "pt": "pt",
    "sk": "sk",
    "si": "sl",
    "hr": "hr",
    "hu": "hu",
    "cs": "cs",
    "de": "de",
    "es": "es",
    "lt": "lt",
    "pl": "pl",
    "lv": "lv",
}


def load_cache() -> dict[str, str]:
    if CACHE.is_file():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(c: dict[str, str]) -> None:
    CACHE.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8")


def tr(text: str, tgt: str, cache: dict[str, str]) -> str:
    key = f"ro|{tgt}|{text}"
    if key in cache:
        return cache[key]
    q = urllib.parse.quote(text[:4800])
    url = f"https://api.mymemory.translated.net/get?q={q}&langpair=ro|{tgt}"
    for attempt in range(10):
        try:
            with urllib.request.urlopen(url, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            out = data.get("responseData", {}).get("translatedText", "")
            if out and "MYMEMORY WARNING" not in out.upper():
                cache[key] = out
                save_cache(cache)
                time.sleep(0.8)
                return out
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed: {text[:50]}")


def translate_dict(ro: dict[str, Any], tgt: str, cache: dict[str, str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for k, v in ro.items():
        if k in ("ty_alt",):
            out[k] = v
            continue
        if k == "ty_steps":
            out[k] = [tr(s, tgt, cache) for s in v]
            continue
        if k == "ty_badges":
            out[k] = tuple(tr(s, tgt, cache) for s in v)
            continue
        if isinstance(v, str):
            out[k] = tr(v, tgt, cache)
        else:
            out[k] = v
    return out


def main() -> None:
    cache = load_cache()
    ro = _ro()
    all_loc: dict[str, Any] = {"ro": ro}
    if OUT.is_file():
        all_loc = json.loads(OUT.read_text(encoding="utf-8"))

    for code, tgt in TARGETS.items():
        if code in all_loc and len(all_loc[code]) > 150:
            print("skip", code)
            continue
        print("translate", code, flush=True)
        loc = translate_dict(ro, tgt, cache)
        if code in FORM:
            loc["label_name"] = FORM[code]["label_name"]
            loc["label_tel"] = FORM[code]["label_tel"]
            loc["label_addr"] = FORM[code]["label_addr"]
            loc["ph_name"] = FORM[code]["ph_name"]
            loc["ph_tel"] = FORM[code]["ph_tel"]
            loc["ph_addr"] = FORM[code]["ph_addr"]
        if code in BLOCKED:
            loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[code]
        loc["cta_inline"] = loc.get("cta", "")
        all_loc[code] = loc
        OUT.write_text(json.dumps(all_loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("done", OUT)


if __name__ == "__main__":
    main()
