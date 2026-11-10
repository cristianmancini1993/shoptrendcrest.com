#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build _forvex_phrases_all.py and _forvex_i18n.py from TAIGOR phrases + FORVEX ES master."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
from _forvex_brushless_i18n import patch_bundle  # noqa: E402
from _forvex_kit_case_i18n import apply_kit_case  # noqa: E402
from _forvex_locale_fixes import apply_locale_fixes  # noqa: E402
from _forvex_pt_patch import apply_pt_patch  # noqa: E402
from _forvex_site_copy_i18n import SITE_COPY_I18N  # noqa: E402
from _forvex_ui_i18n import UI_I18N, apply_ui  # noqa: E402
from _forvex_cmp_fv_i18n import CMP_FV_I18N  # noqa: E402
from _forvex_delivery_i18n import DELIVERY_I18N  # noqa: E402
from _forvex_rev_i18n import REV_I18N  # noqa: E402
from _forvex_es_overlay import ES_OVERLAY, TY_OVERLAY  # noqa: E402
from _taigor_phrases_all import PHRASES as TAIGOR_PHRASES  # noqa: E402

REPL = (
    ("TAIGOR™", "FORVEX™"),
    ("TAIGOR", "FORVEX"),
    ("taigor", "forvex"),
    ("1600 W", "2000 W"),
    ("1600", "2000"),
    ("45 cm", "50 cm"),
    ("45cm", "50 cm"),
)


def scrub_text(s: str) -> str:
    if not s:
        return s
    for a, b in REPL:
        s = s.replace(a, b)
    return s


def scrub_bundle(bundle: dict) -> dict:
    out = {}
    for k, v in bundle.items():
        if isinstance(v, str):
            out[k] = scrub_text(v)
        else:
            out[k] = v
    return out


def load_taigor_i18n() -> dict:
    spec = importlib.util.spec_from_file_location("_taigor_i18n", ROOT / "_taigor_i18n.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.TRANSLATIONS


def load_lang_patch(code: str) -> dict:
    path = ROOT / "_taigor_langs" / f"{code}.py"
    if not path.exists():
        return {}
    spec = importlib.util.spec_from_file_location(f"patch_{code}", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.PATCH)


def build_overlay_i18n() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {"es": dict(ES_OVERLAY)}
    es_tg = TAIGOR_PHRASES["es"]
    for code in TAIGOR_PHRASES:
        if code == "es":
            continue
        ov: dict[str, str] = {}
        patch = scrub_bundle(load_lang_patch(code))
        for k, fes in ES_OVERLAY.items():
            if not fes:
                continue
            tes = es_tg.get(k, "")
            loc = TAIGOR_PHRASES[code].get(k, "")
            if tes and tes in loc:
                ov[k] = scrub_text(loc.replace(tes, fes))
            elif loc:
                ov[k] = scrub_text(loc)
            else:
                ov[k] = fes
        if code in CMP_FV_I18N:
            ov.update(CMP_FV_I18N[code])
        if code in REV_I18N:
            ov.update(REV_I18N[code])
        if code in UI_I18N:
            ov.update(UI_I18N[code])
        if code in SITE_COPY_I18N:
            ov.update(SITE_COPY_I18N[code])
        result[code] = ov
    return result


def build_phrases() -> dict:
    phrases: dict[str, dict] = {}
    overlay_i18n = build_overlay_i18n()
    for code, bundle in TAIGOR_PHRASES.items():
        p = scrub_bundle(copy.deepcopy(bundle))
        p.update(overlay_i18n.get(code, {}))
        phrases[code] = p
    return phrases


def phrases_to_translations(phrases: dict, taigor_tr: dict) -> dict:
    from _taigor_assemble import build_locale

    ty_i18n = build_overlay_i18n()
    out: dict[str, dict] = {}
    for code, bundle in phrases.items():
        loc = build_locale(bundle)
        loc["cmp_th_taigor"] = "FORVEX™"
        base = copy.deepcopy(taigor_tr.get(code, taigor_tr["es"]))
        for k, v in loc.items():
            if isinstance(v, str) and v:
                base[k] = v
        oi = build_overlay_i18n().get(code, {})
        for k, v in oi.items():
            if isinstance(v, str) and v:
                base[k] = v
        if code == "es":
            base.update(TY_OVERLAY)
        else:
            tg = taigor_tr.get(code, {})
            if "ty_steps" in tg:
                base["ty_steps"] = [
                    scrub_text(s) for s in tg["ty_steps"]
                ]
            if "ty_badges" in tg:
                base["ty_badges"] = tuple(scrub_text(b) for b in tg["ty_badges"])
            for tk, es_val in TY_OVERLAY.items():
                if tk in ("ty_steps", "ty_badges"):
                    continue
                if tk in tg:
                    base[tk] = scrub_text(str(tg[tk]))
                elif isinstance(es_val, str):
                    base[tk] = es_val
        if code in DELIVERY_I18N:
            base["faq1_a"] = DELIVERY_I18N[code]["faq1_a"]
            steps = list(base.get("ty_steps", TY_OVERLAY["ty_steps"]))
            if len(steps) >= 2:
                steps[1] = DELIVERY_I18N[code]["ty_step2"]
            base["ty_steps"] = steps
        if code in SITE_COPY_I18N:
            base.update(SITE_COPY_I18N[code])
        base = apply_ui(base, code)
        base = apply_locale_fixes(base, code)
        if code == "pt":
            base = apply_pt_patch(base)
        out[code] = apply_kit_case(patch_bundle(base, code), code)
    return out


def write_phrases_file(phrases: dict) -> None:
    path = ROOT / "_forvex_phrases_all.py"
    path.write_text(
        '# -*- coding: utf-8 -*-\n"""FORVEX phrase bundles (derived from TAIGOR + ES overlay)."""\n\n'
        f"PHRASES = {repr(phrases)}\n",
        encoding="utf-8",
    )


def write_i18n_file(translations: dict) -> None:
    path = ROOT / "_forvex_i18n.py"
    path.write_text(
        '# -*- coding: utf-8 -*-\n"""FORVEX landing + thank-you translations."""\n\n'
        f"TRANSLATIONS = {repr(translations)}\n",
        encoding="utf-8",
    )


def write_es_strings(it_strings: dict, translations_es: dict) -> None:
    """Key → Spanish text for template replacement map."""
    merged = copy.deepcopy(it_strings)
    for k, v in translations_es.items():
        if isinstance(v, str) and v:
            merged[k] = v
    path = ROOT / "_forvex_es_strings.py"
    path.write_text(
        '# -*- coding: utf-8 -*-\n"""Spanish source strings for FORVEX (key → text)."""\n\n'
        f"ES_STRINGS: dict[str, str | list[str] | tuple[str, ...]] = {repr(merged)}\n",
        encoding="utf-8",
    )


def load_it_strings() -> dict:
    import ast

    text = (ROOT / "_taigor_it_strings.py").read_text(encoding="utf-8")
    marker = "IT_STRINGS"
    start = text.index(marker)
    start = text.index("{", start)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return ast.literal_eval(text[start : i + 1])
    raise ValueError("IT_STRINGS dict not found")


def main() -> None:
    it_strings = load_it_strings()

    phrases = build_phrases()
    write_phrases_file(phrases)
    taigor_tr = load_taigor_i18n()
    translations = phrases_to_translations(phrases, taigor_tr)
    write_i18n_file(translations)
    for k, v in ES_OVERLAY.items():
        if isinstance(v, str) and v:
            translations["es"][k] = v
    translations["es"].update(TY_OVERLAY)
    write_es_strings(it_strings, translations["es"])
    print(f"Wrote phrases + i18n for {len(phrases)} locales")


if __name__ == "__main__":
    main()
