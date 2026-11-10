#!/usr/bin/env python3
"""Generate de, es, lt, pl, lv locales with cached MyMemory calls."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from _gen_cendora_i18n_once import BLOCKED, FORM
from _cendora_it_strings import IT_STRINGS

OUT = Path(__file__).with_name("_cendora_locales_extra.json")
CACHE = Path(__file__).with_name("_cendora_translate_cache.json")
CODES = {"de": "de-DE", "es": "es-ES", "lt": "lt-LT", "pl": "pl-PL", "lv": "lv-LV"}

_PROTECT = ("{price}", "{n}", "CENDORA™", "<strong>", "</strong>", '<span class="hl">', "</span>")


def load_cache() -> dict[str, str]:
    if CACHE.is_file():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(c: dict[str, str]) -> None:
    CACHE.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8")


def mymemory(text: str, tgt: str) -> str:
    q = urllib.parse.quote(text[:4500])
    url = f"https://api.mymemory.translated.net/get?q={q}&langpair=it|{tgt.split('-')[0]}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    out = data.get("responseData", {}).get("translatedText", "")
    if not out or "MYMEMORY WARNING" in out.upper():
        raise RuntimeError("mymemory failed")
    return out


def translate(text: str, tgt: str, cache: dict[str, str]) -> str:
    key = f"{tgt}\0{text}"
    if key in cache:
        return cache[key]
    shielded = text
    placeholders: list[str] = []
    for ph in _PROTECT:
        if ph in shielded:
            shielded = shielded.replace(ph, f"⟦{len(placeholders)}⟧")
            placeholders.append(ph)
    for attempt in range(12):
        try:
            out = mymemory(shielded, tgt)
            for i, ph in enumerate(placeholders):
                out = out.replace(f"⟦{i}⟧", ph)
            cache[key] = out
            time.sleep(1.2)
            return out
        except Exception:
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"translate failed: {text[:60]}")


def build(code: str, tgt: str, cache: dict[str, str]) -> dict[str, Any]:
    loc: dict[str, Any] = {}
    for k, v in IT_STRINGS.items():
        if k == "ty_steps":
            loc[k] = [translate(x, tgt, cache) for x in v]
            continue
        if k == "ty_badges":
            loc[k] = tuple(translate(x, tgt, cache) for x in v)
            continue
        if isinstance(v, str):
            if k == "ty_alt":
                loc[k] = v
                continue
            loc[k] = translate(v, tgt, cache)
        else:
            loc[k] = v
    loc.update(FORM[code])
    loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[code]
    loc["cta_inline"] = loc["cta"]
    return loc


def main() -> None:
    cache = load_cache()
    out: dict[str, Any] = {}
    if OUT.is_file():
        out = json.loads(OUT.read_text(encoding="utf-8"))
    for code, tgt in CODES.items():
        if code in out and len(out[code]) >= len(IT_STRINGS) - 2:
            print("skip", code)
            continue
        print("build", code, flush=True)
        out[code] = build(code, tgt, cache)
        save_cache(cache)
        OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("done", OUT)


if __name__ == "__main__":
    main()
