#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build _warmio_langs/*.py PATCH bundles from IT master + locale data."""
from __future__ import annotations

import importlib.util
import pprint
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_it() -> dict:
    spec = importlib.util.spec_from_file_location(
        "_warmio_it_strings", ROOT / "_warmio_it_strings.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.IT_STRINGS)


def it_to_phrase(s: dict) -> dict[str, str]:
    ty = s["ty_steps"]
    return {
        "title": s["title"],
        "description": s["description"],
        "og_title": s["og_title"],
        "og_description": s["og_description"],
        "topbar": s["topbar"],
        "rating": s["rating"],
        "gift": s["gift"],
        "h1_mobile": s["h1_mobile"],
        "h1_desktop": s["h1_desktop"],
        "lead": s["lead"],
        "alt_hero_mobile": s["alt_hero_mobile"],
        "alt_hero_desktop": s["alt_hero_desktop"],
        "cta": s["cta"],
        "cta_inline": s["cta_inline"],
        "form_note_hero": s["form_note_hero"],
        "form_note_form": s["form_note_form"],
        "f1_h": s["f1_h"],
        "f1_p": s["f1_p"],
        "f2_h": s["f2_h"],
        "f2_p": s["f2_p"],
        "f3_h": s["f3_h"],
        "f3_p": s["f3_p"],
        "f4_h": s["f4_h"],
        "f4_p": s["f4_p"],
        "form_h2": s["form_h2"],
        "form_p": s["form_p"],
        "submit_btn": s["submit_btn"],
        "ty1": ty[0],
        "ty2": ty[1],
        "ty3": ty[2],
        "why1_eye": s["why1_eye"],
        "why1_h": s["why1_h"],
        "why1_t1": s["why1_t1"],
        "why1_t2": s["why1_t2"],
        "why1_t3": s["why1_t3"],
        "why1_p1": s["why1_p1"],
        "why1_p2": s["why1_p2"],
        "why2_eye": s["why2_eye"],
        "why2_h": s["why2_h"],
        "why2_t1": s["why2_t1"],
        "why2_t2": s["why2_t2"],
        "why2_t3": s["why2_t3"],
        "why2_p1": s["why2_p1"],
        "why2_p2": s["why2_p2"],
        "why3_eye": s["why3_eye"],
        "why3_h": s["why3_h"],
        "why3_t1": s["why3_t1"],
        "why3_t2": s["why3_t2"],
        "why3_t3": s["why3_t3"],
        "why3_p1": s["why3_p1"],
        "why3_p2": s["why3_p2"],
        "compare_label": s["compare_label"],
        "compare_h": s["compare_h"],
        "compare_aria": s["compare_aria"],
        "cmp_th_old": s["cmp_th_old"],
        "cmp_row_cons": s["cmp_row_cons"],
        "cmp_old_cons": s["cmp_old_cons"],
        "cmp_win_cons": s["cmp_win_cons"],
        "cmp_row_func": s["cmp_row_func"],
        "cmp_old_func": s["cmp_old_func"],
        "cmp_win_func": s["cmp_win_func"],
        "cmp_row_inst": s["cmp_row_inst"],
        "cmp_old_inst": s["cmp_old_inst"],
        "cmp_win_inst": s["cmp_win_inst"],
        "cmp_row_hum": s["cmp_row_hum"],
        "cmp_old_hum": s["cmp_old_hum"],
        "cmp_win_hum": s["cmp_win_hum"],
        "cmp_row_air": s["cmp_row_air"],
        "cmp_old_air": s["cmp_old_air"],
        "cmp_win_air": s["cmp_win_air"],
        "cmp_row_ctrl": s["cmp_row_ctrl"],
        "cmp_old_ctrl": s["cmp_old_ctrl"],
        "cmp_win_ctrl": s["cmp_win_ctrl"],
        "cmp_row_warr": s["cmp_row_warr"],
        "cmp_old_warr": s["cmp_old_warr"],
        "cmp_win_warr": s["cmp_win_warr"],
        "testimonials_h": s["testimonials_h"],
        "rev1_h": s["rev1_h"],
        "rev1_p": s["rev1_p"],
        "rev2_h": s["rev2_h"],
        "rev2_p": s["rev2_p"],
        "rev3_h": s["rev3_h"],
        "rev3_p": s["rev3_p"],
        "author1": s["author1"],
        "author2": s["author2"],
        "author3": s["author3"],
        "alt_t1": s["alt_t1"],
        "alt_t2": s["alt_t2"],
        "alt_t3": s["alt_t3"],
        "kit_eye": s["kit_eye"],
        "kit_h": s["kit_h"],
        "kit_li1": s["kit_li1"],
        "kit_li2": s["kit_li2"],
        "kit_li3": s["kit_li3"],
        "kit_li4": s["kit_li4"],
        "kit_li5": s["kit_li5"],
        "kit_li6": s["kit_li6"],
        "alt_w1": s["alt_w1"],
        "alt_w2": s["alt_w2"],
        "alt_w3": s["alt_w3"],
        "alt_kit": s["alt_kit"],
        "faq_h": s["faq_h"],
        "faq1_q": s["faq1_q"],
        "faq1_a": s["faq1_a"],
        "faq2_q": s["faq2_q"],
        "faq2_a": s["faq2_a"],
        "faq3_q": s["faq3_q"],
        "faq3_a": s["faq3_a"],
        "faq4_q": s["faq4_q"],
        "faq4_a": s["faq4_a"],
        "faq5_q": s["faq5_q"],
        "faq5_a": s["faq5_a"],
        "ty_product": s["ty_product"],
        "ty_order_header": s["ty_order_header"],
        "ty_pay": s["ty_pay"],
    }


def main() -> None:
    from _warmio_patch_common import validate_bundle

    lang_dir = ROOT / "_warmio_langs"
    lang_dir.mkdir(exist_ok=True)
    it_phrase = it_to_phrase(load_it())
    all_phrases = {"it": it_phrase}
    for path in sorted(lang_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        code = path.stem
        spec = importlib.util.spec_from_file_location(f"w_{code}", path)
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)
        all_phrases[code] = dict(mod.PATCH)
    for code, patch in all_phrases.items():
        validate_bundle(code, patch)
        (lang_dir / f"{code}.py").write_text(
            "# -*- coding: utf-8 -*-\nPATCH = "
            + pprint.pformat(patch, width=120, sort_dicts=False)
            + "\n",
            encoding="utf-8",
        )
        print(f"Wrote _warmio_langs/{code}.py ({len(patch)} keys)")


if __name__ == "__main__":
    main()
