#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build content/granvia/locales/*.json from IT_STRINGS via DeepL."""
from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "content/granvia/locales"

from _granvia_it_strings import IT_STRINGS  # noqa: E402

DEEPL_LANG = {
    "es": "ES",
    "pt": "PT-PT",
    "de": "DE",
    "lt": "LT",
    "hu": "HU",
    "cs": "CS",
}

from _granvia_form_examples import GRANVIA_FORM_EXAMPLES, GRANVIA_NAME_LABEL_OVERRIDES  # noqa: E402

PLACEHOLDERS = GRANVIA_FORM_EXAMPLES


def deepl_translate(texts: list[str], target: str) -> list[str]:
    key = (os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("DEEPL_AUTH_KEY not set")
    url = "https://api.deepl.com/v2/translate" if not key.endswith(":fx") else "https://api-free.deepl.com/v2/translate"
    body = urllib.parse.urlencode(
        [("auth_key", key), ("source_lang", "IT"), ("target_lang", target)]
        + [("text", t) for t in texts],
        doseq=True,
    ).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return [t["text"] for t in data["translations"]]


def build_locale_deepl(code: str) -> dict:
    target = DEEPL_LANG[code]
    keys = [k for k in IT_STRINGS if k not in ("ty_badges", "ty_steps")]
    strings = [str(IT_STRINGS[k]) for k in keys]
    translated: list[str] = []
    batch = 35
    for i in range(0, len(strings), batch):
        translated.extend(deepl_translate(strings[i : i + batch], target))
        time.sleep(0.35)
    loc: dict = {}
    for k, t in zip(keys, translated):
        loc[k] = t
    loc["ty_steps"] = deepl_translate(list(IT_STRINGS["ty_steps"]), target)
    loc["ty_badges"] = deepl_translate(list(IT_STRINGS["ty_badges"]), target)
    for k, v in PLACEHOLDERS.get(code, {}).items():
        loc[k] = v
    loc["h1_desktop"] = loc["h1_desktop"].replace(" AL MINUTO", "").replace(" al minuto", "")
    loc["brand_fix"] = "Granvia™"
    for key in list(loc.keys()):
        if isinstance(loc[key], str):
            loc[key] = (
                loc[key]
                .replace("Granvia™™", "Granvia™")
                .replace("GRANVIA™", "Granvia™")
            )
    loc.pop("brand_fix", None)
    return loc


def main() -> int:
    LOCALES.mkdir(parents=True, exist_ok=True)
    it = {k: (list(v) if isinstance(v, tuple) else v) for k, v in IT_STRINGS.items()}
    (LOCALES / "it.json").write_text(json.dumps(it, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not (os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY")):
        print("DEEPL_AUTH_KEY not set", file=__import__("sys").stderr)
        return 1
    for code in DEEPL_LANG:
        print(f"DeepL → {code}...")
        loc = build_locale_deepl(code)
        (LOCALES / f"{code}.json").write_text(
            json.dumps(loc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
