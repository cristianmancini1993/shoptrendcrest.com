#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble scripts/_taigor_i18n.py from shared UI strings + TAIGOR product copy."""
from __future__ import annotations

import importlib.util
import pprint
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_mod(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _brand(s: str) -> str:
    return s.replace("LEAFORA™", "TAIGOR™").replace("LEAFORA", "TAIGOR").replace(
        "GlacierAir™", "TAIGOR™"
    ).replace("GlacierAir", "TAIGOR")


def _fix_val(val):
    if isinstance(val, str):
        return _brand(val)
    if isinstance(val, list):
        return [_brand(x) for x in val]
    if isinstance(val, tuple):
        return tuple(_brand(x) for x in val)
    return val


COPY_UI_KEYS = {
    "submitting",
    "cookie_text",
    "cookie_accept",
    "cookie_learn",
    "info",
    "about",
    "contact",
    "privacy",
    "terms",
    "cookie",
    "ship",
    "refund",
    "contacts",
    "rights",
    "ty_title",
    "ty_desc",
    "ty_h1",
    "ty_sub",
    "ty_alt",
    "ty_eyebrow",
    "ty_action_title",
    "ty_action_body",
    "ty_action_warn",
    "ty_hours_h",
    "ty_hours",
    "ty_next_h",
    "ty_badges",
    "hours",
    "mins",
    "secs",
    "countdown",
    "stock_l",
    "stock_r",
    "live",
    "live0",
    "label_name",
    "label_tel",
    "label_addr",
    "ph_name",
    "ph_tel",
    "ph_addr",
    "author1",
    "author2",
    "author3",
}

UI_ALIASES = {
    "label_phone": "label_tel",
    "ph_phone": "ph_tel",
    "btn": "submit_btn",
}


def load_ui_translations() -> dict[str, dict]:
    leafora = _load_mod("_leafora_i18n", "_leafora_i18n.py").TRANSLATIONS
    ro = _load_mod("_leafora_ro_strings", "_leafora_ro_strings.py").RO_STRINGS
    ga2 = _load_mod("_ga_i18n_part2", "_ga_i18n_part2.py").TRANSLATIONS
    ga3 = _load_mod("_ga_i18n_part3", "_ga_i18n_part3.py").TRANSLATIONS
    ui: dict[str, dict] = {k: dict(v) for k, v in leafora.items()}
    ui["ro"] = dict(ro)
    ui["si"] = dict(ga2["si"])
    ui["hr"] = dict(ga2["hr"])
    ui["lv"] = dict(ga3["lv"])
    for lang, table in ui.items():
        for src, dst in UI_ALIASES.items():
            if src in table and dst not in table:
                table[dst] = table[src]
    return ui


from _taigor_locale_core import TAIGOR_CORE  # noqa: E402

# Override GlacierAir/Leafora countdown (−70 %) for TAIGOR (−50 %).
TAIGOR_UI_OVERRIDES: dict[str, dict[str, str]] = {
    "ro": {
        "live0": "<strong>41 de persoane</strong> vizualizează TAIGOR™ acum",
    },
    "si": {
        "author1": "Roberto G. — Preverjen nakup",
        "author2": "Davide M. — Preverjen nakup",
        "author3": "Marco T. — Preverjen nakup",
    },
    "hr": {
        "author1": "Roberto G. — Potvrđena kupnja",
        "author2": "Davide M. — Potvrđena kupnja",
        "author3": "Marco T. — Potvrđena kupnja",
    },
    "lv": {
        "author1": "Roberto G. — Apstiprināts pirkums",
        "author2": "Davide M. — Apstiprināts pirkums",
        "author3": "Marco T. — Apstiprināts pirkums",
    },
}

TAIGOR_COUNTDOWN: dict[str, str] = {
    "it": "⏰ Lo sconto del 50% termina tra",
    "lt": "⏰ −50 % nuolaida baigiasi po",
    "es": "⏰ El descuento del 50 % termina en",
    "pt": "⏰ O desconto de −50 % termina em",
    "pl": "⏰ Promocja −50 % kończy się za",
    "cs": "⏰ Sleva −50 % končí za",
    "ro": "⏰ Reducerea de −50 % se încheie în",
    "sk": "⏰ Zľava −50 % končí o",
    "si": "⏰ Popust −50 % se konča v",
    "hr": "⏰ Popust od −50 % završava za",
    "hu": "⏰ A −50 % kedvezmény vége:",
    "de": "⏰ Das −50 %-Angebot endet in",
    "lv": "⏰ −50 % atlaide beidzas pēc",
}


def build() -> dict:
    ui_all = load_ui_translations()
    it_defaults_boot = _load_mod("_taigor_it_strings", "_taigor_it_strings.py").IT_STRINGS
    ui_all.setdefault("it", {})
    for k, v in it_defaults_boot.items():
        if k in COPY_UI_KEYS and isinstance(v, str):
            ui_all["it"][k] = v
        elif k == "ty_badges" and isinstance(v, tuple):
            ui_all["it"][k] = v
    it_keys = [
        k
        for k, v in _load_mod("_taigor_it_strings", "_taigor_it_strings.py").IT_STRINGS.items()
        if isinstance(v, (str, list, tuple))
    ]
    out: dict = {}
    for lang, core in TAIGOR_CORE.items():
        if lang not in ui_all and lang != "it":
            raise KeyError(f"Missing UI locale: {lang}")
        merged: dict = {}
        leaf = ui_all[lang]
        it_defaults = _load_mod("_taigor_it_strings", "_taigor_it_strings.py").IT_STRINGS
        for k in COPY_UI_KEYS:
            if k in leaf:
                merged[k] = _fix_val(leaf[k])
            elif k in it_defaults and isinstance(it_defaults[k], str):
                merged[k] = it_defaults[k]
        merged.update(core)
        if lang == "it":
            for k, v in it_defaults.items():
                if k in COPY_UI_KEYS:
                    if isinstance(v, str):
                        merged[k] = v
                    elif k == "ty_badges" and isinstance(v, tuple):
                        merged[k] = v
            if "ty_steps" in core:
                merged["ty_steps"] = core["ty_steps"]
        if lang in TAIGOR_UI_OVERRIDES:
            merged.update(TAIGOR_UI_OVERRIDES[lang])
        if lang in TAIGOR_COUNTDOWN:
            merged["countdown"] = TAIGOR_COUNTDOWN[lang]
        missing = [k for k in it_keys if k not in merged]
        if missing:
            raise KeyError(f"{lang} missing keys: {missing[:8]}... ({len(missing)} total)")
        out[lang] = merged
    return out


def main() -> None:
    tr = build()
    target = ROOT / "_taigor_i18n.py"
    body = (
        "# -*- coding: utf-8 -*-\n"
        '"""TAIGOR™ mini chainsaw landing + thank-you translations."""\n\n'
        "TRANSLATIONS = "
        + pprint.pformat(tr, width=120, sort_dicts=False)
        + "\n"
    )
    target.write_text(body, encoding="utf-8")
    print(f"Wrote {target} ({len(tr)} locales)")


if __name__ == "__main__":
    main()
