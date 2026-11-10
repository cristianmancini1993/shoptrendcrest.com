#!/usr/bin/env python3
"""Chunked RO → campaign locales via MyMemory."""
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
CHUNK = 12
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


def tr_one(text: str, tgt: str) -> str:
    q = urllib.parse.quote(text[:4500])
    url = f"https://api.mymemory.translated.net/get?q={q}&langpair=ro|{tgt}"
    with urllib.request.urlopen(url, timeout=90) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    out = data.get("responseData", {}).get("translatedText", "")
    if not out or "MYMEMORY WARNING" in out.upper():
        raise RuntimeError("translate failed")
    return out


def build_locale(code: str, tgt: str) -> dict[str, Any]:
    ro = _ro()
    flat_keys = [k for k in ro if k not in ("ty_steps", "ty_badges")]
    loc: dict[str, Any] = {}
    for i in range(0, len(flat_keys), CHUNK):
        chunk_keys = flat_keys[i : i + CHUNK]
        for k in chunk_keys:
            loc[k] = tr_one(str(ro[k]), tgt)
            time.sleep(0.5)
    loc["ty_steps"] = [tr_one(s, tgt) for s in ro["ty_steps"]]
    loc["ty_badges"] = [tr_one(s, tgt) for s in ro["ty_badges"]]
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
    return loc


def main() -> None:
    all_loc: dict[str, Any] = {"ro": _ro()}
    if OUT.is_file():
        all_loc.update(json.loads(OUT.read_text(encoding="utf-8")))
    for code, tgt in TARGETS.items():
        if code in all_loc and len(all_loc[code]) > 150:
            print("skip", code)
            continue
        print("build", code, flush=True)
        all_loc[code] = build_locale(code, tgt)
        OUT.write_text(json.dumps(all_loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
