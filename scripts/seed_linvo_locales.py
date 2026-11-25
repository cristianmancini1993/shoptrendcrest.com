#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build content/linvo/locales/*.json from IT_STRINGS via DeepL (merge-safe)."""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "content/linvo/locales"

from _linvo_it_strings import IT_STRINGS  # noqa: E402
from _luno_form_snippets import _FORM_META  # noqa: E402

DEEPL_LANG = {
    "de": "DE",
    "hu": "HU",
    "pt": "PT-PT",
    "es": "ES",
    "pl": "PL",
    "cs": "CS",
    "lv": "LV",
    "sk": "SK",
}

PLACEHOLDER_RE = re.compile(r"\{[a-z_]+\}")
LINVO_ONLY_RE = re.compile(r"^\s*LINVO™\s*$")

# Keys never sent to DeepL (stay Italian in all locales per user rule)
SKIP_TRANSLATE_KEYS = frozenset({"manual_in_box"})

_FORM_KEYS = (
    "label_name",
    "label_tel",
    "label_addr",
    "ph_name",
    "ph_tel",
    "ph_addr",
    "submit_btn",
)

_LANG_FOR_OFFER = {
    "1912": "de",
    "1915": "hu",
    "2480": "pt",
    "3163": "es",
    "3167": "pl",
    "3169": "cs",
    "3910": "lv",
    "4321": "sk",
}


def deepl_translate(texts: list[str], target: str) -> list[str]:
    key = (os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("DEEPL_AUTH_KEY not set")
    url = (
        "https://api.deepl.com/v2/translate"
        if not key.endswith(":fx")
        else "https://api-free.deepl.com/v2/translate"
    )
    body = urllib.parse.urlencode(
        [("auth_key", key), ("source_lang", "IT"), ("target_lang", target)]
        + [("text", t) for t in texts],
        doseq=True,
    ).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return [t["text"] for t in data["translations"]]


def should_skip_deepl(text: str) -> bool:
    if LINVO_ONLY_RE.match(text.strip()):
        return True
    if PLACEHOLDER_RE.fullmatch(text.strip()):
        return True
    return False


def protect_placeholders(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}

    def repl(m: re.Match[str]) -> str:
        token = f"⟦PH{len(mapping)}⟧"
        mapping[token] = m.group(0)
        return token

    protected = PLACEHOLDER_RE.sub(repl, text)
    return protected, mapping


def restore_placeholders(text: str, mapping: dict[str, str]) -> str:
    for token, orig in mapping.items():
        text = text.replace(token, orig)
    return text


def serializable_it() -> dict:
    out: dict = {}
    for k, v in IT_STRINGS.items():
        if isinstance(v, tuple):
            out[k] = list(v)
        else:
            out[k] = v
    return out


def form_overrides_for_lang(lang: str) -> dict[str, str]:
    """Pick first offer with matching lang in _FORM_META for label/placeholder hints."""
    for offer, code in _LANG_FOR_OFFER.items():
        if code != lang:
            continue
        meta = _FORM_META.get(offer)
        if not meta:
            continue
        ln, lt, la = meta["labels"]
        pn, pt, pa = meta["placeholders"]
        return {
            "label_name": ln,
            "label_tel": lt,
            "label_addr": la,
            "ph_name": pn,
            "ph_tel": pt,
            "ph_addr": pa,
            "submit_btn": meta["submit"],
        }
    return {}


def build_locale_deepl(code: str, old_it: dict | None) -> dict:
    target = DEEPL_LANG[code]
    existing_path = LOCALES / f"{code}.json"
    existing: dict = {}
    if existing_path.is_file():
        existing = json.loads(existing_path.read_text(encoding="utf-8"))

    loc: dict = dict(existing)
    keys_to_translate: list[str] = []
    texts: list[str] = []

    for key, val in IT_STRINGS.items():
        if isinstance(val, (list, tuple)):
            continue
        assert isinstance(val, str)
        if key in SKIP_TRANSLATE_KEYS:
            if old_it is None or old_it.get(key) != val or key not in loc:
                loc[key] = val
            continue
        source_changed = old_it is None or old_it.get(key) != val
        if key in loc and not source_changed:
            continue
        if key in loc and key not in existing:
            source_changed = True
        if key in loc and not source_changed:
            continue
        if key in loc and old_it and old_it.get(key) == val:
            continue
        if key in loc and old_it and old_it.get(key) != val:
            source_changed = True
        if key in existing and old_it and old_it.get(key) == val:
            continue
        if not source_changed and key in existing:
            continue
        if should_skip_deepl(val):
            loc[key] = val
            continue
        protected, ph_map = protect_placeholders(val)
        keys_to_translate.append(key)
        texts.append((protected, ph_map))

    flat_texts = [t[0] for t in texts]
    translated: list[str] = []
    batch = 30
    for i in range(0, len(flat_texts), batch):
        translated.extend(deepl_translate(flat_texts[i : i + batch], target))
        time.sleep(0.35)

    for (key, ph_map), tr in zip(
        [(k, texts[i][1]) for i, k in enumerate(keys_to_translate)],
        translated,
    ):
        loc[key] = restore_placeholders(tr, ph_map)

    # lists
    for list_key in ("ty_steps", "ty_badges"):
        src = IT_STRINGS[list_key]
        source_changed = old_it is None or old_it.get(list_key) != list(src)
        if list_key in existing and not source_changed:
            loc[list_key] = existing[list_key]
            continue
        if isinstance(src, tuple):
            src_list = list(src)
        else:
            src_list = list(src)
        loc[list_key] = deepl_translate(src_list, target)
        time.sleep(0.2)

    for fk, fv in form_overrides_for_lang(code).items():
        if fk not in loc or (old_it and fk in old_it):
            loc[fk] = fv

    loc["manual_in_box"] = IT_STRINGS["manual_in_box"]
    return loc


def merge_new_keys_only(code: str, old_it: dict, deepl_ok: bool) -> dict:
    """Update locale: add missing keys; refresh changed Italian source when DeepL available."""
    path = LOCALES / f"{code}.json"
    existing: dict = {}
    if path.is_file():
        existing = json.loads(path.read_text(encoding="utf-8"))

    if deepl_ok:
        return build_locale_deepl(code, old_it)

    # best-effort without DeepL: copy IT + form overrides
    loc = dict(existing)
    for key, val in IT_STRINGS.items():
        if isinstance(val, (list, tuple)):
            if key not in loc:
                loc[key] = list(val) if not isinstance(val, list) else val
            continue
        if old_it and old_it.get(key) != val:
            loc[key] = val
        elif key not in loc:
            loc[key] = val
    for fk, fv in form_overrides_for_lang(code).items():
        if fk not in loc:
            loc[fk] = fv
    loc["manual_in_box"] = IT_STRINGS["manual_in_box"]
    return loc


def main() -> int:
    LOCALES.mkdir(parents=True, exist_ok=True)
    it = serializable_it()
    it_path = LOCALES / "it.json"
    old_it: dict | None = None
    if it_path.is_file():
        try:
            old_it = json.loads(it_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            old_it = None
    it_path.write_text(json.dumps(it, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    deepl_ok = bool(os.environ.get("DEEPL_AUTH_KEY") or os.environ.get("DEEPL_API_KEY"))
    if not deepl_ok:
        print("DEEPL_AUTH_KEY not set — writing best-effort locales (IT copy + form overrides).", file=sys.stderr)

    for code in DEEPL_LANG:
        print(f"→ {code}...")
        try:
            if deepl_ok:
                loc = build_locale_deepl(code, old_it)
            else:
                loc = merge_new_keys_only(code, old_it, deepl_ok=False)
        except Exception as exc:
            print(f"  DeepL failed for {code}: {exc}", file=sys.stderr)
            loc = merge_new_keys_only(code, old_it, deepl_ok=False)
        (LOCALES / f"{code}.json").write_text(
            json.dumps(loc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print("Done.")
    return 0 if deepl_ok else 0


if __name__ == "__main__":
    raise SystemExit(main())