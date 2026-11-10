#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build content/cendora/locales/*.json from IT_STRINGS via DeepL (preferred) or Ferrox HTML alignment."""
from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "content/cendora/locales"
SG = ROOT.parent / "shopgearspot.com"

from _cendora_it_strings import IT_STRINGS  # noqa: E402

DEEPL_LANG = {
    "ro": "RO",
    "pt": "PT-PT",
    "sk": "SK",
    "si": "SL",
    "hr": "HR",
    "hu": "HU",
    "es": "ES",
    "de": "DE",
    "lt": "LT",
    "pl": "PL",
    "cs": "CS",
    "lv": "LV",
    "el": "EL",
}

FERROX_PAGES = {
    "ro": SG / "ro/ferrox-539/index.html",
    "pt": SG / "pt/ferrox-1476/index.html",
    "sk": SG / "sk/ferrox-536/index.html",
    "si": SG / "si/ferrox-535/index.html",
    "hr": SG / "hr/ferrox-537/index.html",
    "hu": SG / "hu/ferrox-534/index.html",
    "cs": SG / "cz/ferrox-538/index.html",
}


def deepl_translate(texts: list[str], target: str) -> list[str]:
    key = (os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("DEEPL_AUTH_KEY not set")
    url = "https://api-free.deepl.com/v2/translate"
    if key.endswith(":fx"):
        url = "https://api-free.deepl.com/v2/translate"
    body = urllib.parse.urlencode(
        [("auth_key", key), ("source_lang", "IT"), ("target_lang", target)]
        + [("text", t) for t in texts],
        doseq=True,
    ).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return [t["text"] for t in data["translations"]]


def ferrox_it_to_geo_pairs() -> dict[str, dict[str, str]]:
    it_f = (SG / "it/ferrox/index.html").read_text(encoding="utf-8")
    it_c = (ROOT / "it/cendora/index.html").read_text(encoding="utf-8")
    # Unique Italian snippets that differ between ferrox and cendora (longest first)
    pairs: list[tuple[str, str]] = []
    for m in re.finditer(r">([^<>]{8,}?)<", it_f):
        s = m.group(1).strip()
        if "FERROX" in s or "ferrox" in s or "inox" in s.lower() or "antiader" in s.lower():
            if s in it_c:
                continue
    # Direct meta/title swaps from known IT files
    it_f_lines = it_f.splitlines()
    it_c_lines = it_c.splitlines()
    import difflib

    sm = difflib.SequenceMatcher(None, it_f_lines, it_c_lines)
    it_f_to_c: dict[str, str] = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and (i2 - i1) == (j2 - j1):
            for a, b in zip(it_f_lines[i1:i2], it_c_lines[j1:j2]):
                if a != b:
                    it_f_to_c[a] = b

    out: dict[str, dict[str, str]] = {}
    for code, path in FERROX_PAGES.items():
        geo_html = path.read_text(encoding="utf-8")
        geo_lines = geo_html.splitlines()
        sm2 = difflib.SequenceMatcher(None, it_f_lines, geo_lines)
        it_to_geo_line: dict[str, str] = {}
        for tag, i1, i2, j1, j2 in sm2.get_opcodes():
            if tag == "equal":
                for a, b in zip(it_f_lines[i1:i2], geo_lines[j1:j2]):
                    it_to_geo_line[a] = b
            elif tag == "replace" and (i2 - i1) == (j2 - j1):
                for a, b in zip(it_f_lines[i1:i2], geo_lines[j1:j2]):
                    it_to_geo_line[a] = b

        mapped: dict[str, str] = {}
        for it_f_line, it_c_line in it_f_to_c.items():
            geo_line = it_to_geo_line.get(it_f_line)
            if not geo_line:
                continue
            # Apply same structural change: replace ferrox IT fragments inside line
            new_line = geo_line
            for f_snip, c_snip in _snippet_pairs(it_f_line, it_c_line):
                g_f = _map_snippet(f_snip, it_f_line, geo_line)
                g_c = _map_snippet(c_snip, it_c_line, geo_line)
                if g_f and g_c and g_f in new_line:
                    new_line = new_line.replace(g_f, g_c, 1)
            mapped[it_c_line] = new_line
        out[code] = mapped
    return out


def _snippet_pairs(a: str, b: str) -> list[tuple[str, str]]:
    if a == b:
        return []
    # whole line fallback
    return [(a, b)]


def _map_snippet(snip: str, it_line: str, geo_line: str) -> str | None:
    if snip not in it_line:
        return None
    # If geo line shares HTML structure, try naive: same snippet position in text nodes
    if snip in geo_line:
        return snip
    return None


def build_locale_deepl(code: str) -> dict[str, str | list[str]]:
    target = DEEPL_LANG[code]
    keys = [k for k in IT_STRINGS if k not in ("ty_badges", "ty_steps")]
    strings = [str(IT_STRINGS[k]) for k in keys]
    batch = 40
    translated: list[str] = []
    for i in range(0, len(strings), batch):
        chunk = strings[i : i + batch]
        translated.extend(deepl_translate(chunk, target))
        time.sleep(0.3)
    loc: dict[str, str | list[str]] = {}
    for k, t in zip(keys, translated):
        loc[k] = t
    loc["ty_steps"] = deepl_translate(list(IT_STRINGS["ty_steps"]), target)
    loc["ty_badges"] = deepl_translate(list(IT_STRINGS["ty_badges"]), target)
    return loc


def main() -> int:
    LOCALES.mkdir(parents=True, exist_ok=True)
    have_deepl = bool((os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY") or "").strip())
    if have_deepl:
        for code in DEEPL_LANG:
            print(f"DeepL → {code}...")
            loc = build_locale_deepl(code)
            (LOCALES / f"{code}.json").write_text(
                json.dumps(loc, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        print("Done (DeepL).")
        return 0

    print("DEEPL_AUTH_KEY not set — using DeepL-free Ferrox alignment for 7 geos + manual ES/DE/LT/PL/LV from warmio UI merge.")
    from build_cendora_i18n import TRANSLATIONS  # noqa: WPS433

    for code, tr in TRANSLATIONS.items():
        if code == "it":
            continue
        (LOCALES / f"{code}.json").write_text(
            json.dumps(tr, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print("Wrote locales from _cendora_i18n.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
