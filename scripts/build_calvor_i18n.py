#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build _calvor_i18n.py: warmio translations rebranded + Calvor IT copy overlay."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def rebrand(text: str) -> str:
    return (
        text.replace("WARMIO™", "Calvor™")
        .replace("WARMIO", "Calvor")
        .replace("products/warmio", "products/calvor")
        .replace("warmio team", "calvor team")
        .replace("warmio-lp", "calvor-lp")
    )


FALLBACK_KEYS: dict[str, str] = {
    "h1": "h1_desktop",
    "form_note_form": "form_note_form",
}

# Manual included is in Italian (per IT source «Manuale in italiano»).
CALVOR_KIT_LI5: dict[str, str] = {
    "de": "Anleitung auf Italienisch",
    "es": "Manual en italiano",
    "pt": "Manual em italiano",
    "pl": "Instrukcja w języku włoskim",
    "cs": "Návod v italštině",
    "ro": "Manual în limba italiană",
    "sk": "Návod v taliančine",
    "sl": "Navodila v italijanščini",
    "hr": "Upute na talijanskom jeziku",
    "hu": "Útmutató olasz nyelven",
    "lt": "Instrukcija italų kalba",
    "lv": "Instrukcija itāļu valodā",
}


def deep_rebrand(val):
    if isinstance(val, str):
        return rebrand(val)
    if isinstance(val, list):
        return [rebrand(x) for x in val]
    if isinstance(val, tuple):
        return tuple(rebrand(x) for x in val)
    return val


def build_translations() -> dict:
    warmio = _load_module("_warmio_i18n").TRANSLATIONS
    calvor_it = _load_module("_calvor_it_strings").IT_STRINGS
    out: dict = {}
    for lang, tr in warmio.items():
        out[lang] = {k: deep_rebrand(v) for k, v in tr.items()}
    out["it"].update(
        {
            k: v
            for k, v in calvor_it.items()
            if isinstance(v, (str, list, tuple))
        }
    )
    for lang, tr in out.items():
        if lang == "it":
            continue
        for key, it_val in calvor_it.items():
            if not isinstance(it_val, str) or key in tr:
                continue
            fb = FALLBACK_KEYS.get(key)
            if fb and fb in tr:
                tr[key] = tr[fb]
            else:
                tr[key] = it_val
    apply_calvor_locale_fixes(out)
    return out


def apply_calvor_locale_fixes(out: dict) -> None:
    import re

    for lang, tr in out.items():
        if lang != "it" and lang in CALVOR_KIT_LI5:
            tr["kit_li5"] = CALVOR_KIT_LI5[lang]
        if lang != "it":
            faq = tr.get("faq3_a")
            if isinstance(faq, str):
                tr["faq3_a"] = re.sub(r"\b120\s*m²", "100 m²", faq)
        if lang == "ro":
            tr["live0"] = "<strong>41 de persoane</strong> vizualizează Calvor™ acum"
            tr["live"] = "<strong>{n} persoane</strong> vizualizează Calvor™ acum"
        if lang == "sk" and isinstance(tr.get("ty_steps"), list):
            tr["ty_steps"] = [
                s.replace("po telefonickej potvrdení", "po telefonickom potvrdení")
                for s in tr["ty_steps"]
            ]


def main() -> None:
    sync = ROOT / "sync_calvor_it_strings.py"
    spec = importlib.util.spec_from_file_location("sync", sync)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.main()

    tr = build_translations()
    out_path = ROOT / "_calvor_i18n.py"
    out_path.write_text(
        "# -*- coding: utf-8 -*-\n"
        '"""Calvor™ campaign translations (generated — run build_calvor_i18n.py)."""\n\n'
        f"TRANSLATIONS = {tr!r}\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path} ({len(tr)} locales)")


if __name__ == "__main__":
    main()