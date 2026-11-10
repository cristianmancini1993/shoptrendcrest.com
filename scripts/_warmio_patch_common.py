# -*- coding: utf-8 -*-
"""Validate WARMIO locale phrase bundles."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _phrase_keys() -> list[str]:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "_warmio_it_strings", ROOT / "_warmio_it_strings.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    s = mod.IT_STRINGS
    ty = s["ty_steps"]
    keys = [
        "title", "description", "og_title", "og_description", "topbar", "rating", "gift",
        "h1_mobile", "h1_desktop", "lead", "alt_hero_mobile", "alt_hero_desktop",
        "cta", "cta_inline", "form_note_hero", "form_note_form",
        "f1_h", "f1_p", "f2_h", "f2_p", "f3_h", "f3_p", "f4_h", "f4_p",
        "form_h2", "form_p", "submit_btn", "ty1", "ty2", "ty3",
        "why1_eye", "why1_h", "why1_t1", "why1_t2", "why1_t3", "why1_p1", "why1_p2",
        "why2_eye", "why2_h", "why2_t1", "why2_t2", "why2_t3", "why2_p1", "why2_p2",
        "why3_eye", "why3_h", "why3_t1", "why3_t2", "why3_t3", "why3_p1", "why3_p2",
        "compare_label", "compare_h", "compare_aria", "cmp_th_old",
        "cmp_row_cons", "cmp_old_cons", "cmp_win_cons",
        "cmp_row_func", "cmp_old_func", "cmp_win_func",
        "cmp_row_inst", "cmp_old_inst", "cmp_win_inst",
        "cmp_row_hum", "cmp_old_hum", "cmp_win_hum",
        "cmp_row_air", "cmp_old_air", "cmp_win_air",
        "cmp_row_ctrl", "cmp_old_ctrl", "cmp_win_ctrl",
        "cmp_row_warr", "cmp_old_warr", "cmp_win_warr",
        "testimonials_h", "rev1_h", "rev1_p", "rev2_h", "rev2_p", "rev3_h", "rev3_p",
        "author1", "author2", "author3", "alt_t1", "alt_t2", "alt_t3",
        "kit_eye", "kit_h", "kit_li1", "kit_li2", "kit_li3", "kit_li4", "kit_li5", "kit_li6",
        "alt_w1", "alt_w2", "alt_w3", "alt_kit",
        "faq_h", "faq1_q", "faq1_a", "faq2_q", "faq2_a", "faq3_q", "faq3_a",
        "faq4_q", "faq4_a", "faq5_q", "faq5_a",
        "ty_product", "ty_order_header", "ty_pay",
    ]
    assert len(keys) == 115
    return keys


PHRASE_KEYS = _phrase_keys()


def validate_bundle(code: str, bundle: dict[str, str]) -> None:
    missing = [k for k in PHRASE_KEYS if k not in bundle]
    extra = [k for k in bundle if k not in PHRASE_KEYS]
    if missing:
        raise ValueError(f"{code}: missing {len(missing)} keys, e.g. {missing[:5]}")
    if extra:
        raise ValueError(f"{code}: unknown keys {extra[:5]}")
