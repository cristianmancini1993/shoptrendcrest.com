#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map IT_STRINGS → locale via aligned Ferrox text-node indices."""
from __future__ import annotations

import json
import re
from pathlib import Path

from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"

FERROX = {
    "pt": ("pt", "ferrox-1476"),
    "sk": ("sk", "ferrox-536"),
    "si": ("si", "ferrox-535"),
    "hr": ("hr", "ferrox-537"),
    "hu": ("hu", "ferrox-534"),
    "cs": ("cz", "ferrox-538"),
}


def text_nodes(html: str) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r">([^<]+)<", html):
        t = m.group(1).strip()
        if len(t) < 2 or t.startswith("http") or "gtag" in t or "dataLayer" in t:
            continue
        out.append(t)
    return out


def index_map(a: list[str], b: list[str]) -> dict[str, str]:
    m: dict[str, str] = {}
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            m[a[i]] = b[i]
    return m


def cendora_patches(s: str) -> str:
    s = s.replace("FERROX™", "CENDORA™").replace("FERROX", "CENDORA")
    s = s.replace("ferrox", "cendora").replace("shopgearspot.com", "shoptrendcrest.com")
    # Ferrox inox → CENDORA antiaderente (common RO/PT phrases)
    repl = (
        ("oțel inoxidabil", "vase antiaderente"),
        ("din oțel inoxidabil", "antiaderente"),
        ("Inox lucios", "Antiaderent"),
        ("aço inoxidável", "antiaderente"),
        ("acier inoxydable", "antiadhésif"),
        ("Edelstahl", "Antihaft"),
        ("Set de bucătărie din oțel inoxidabil", "Set de vase antiaderente"),
        ("Bateria de cozinha em aço inoxidável", "Conjunto de panelas antiaderentes"),
    )
    for a, b in repl:
        s = s.replace(a, b)
    return s


def build_from_ferrox(code: str) -> dict:
    geo, folder = FERROX[code]
    it_f = text_nodes((SG / "it/ferrox/index.html").read_text(encoding="utf-8"))
    it_c = text_nodes((ROOT / "it/cendora/index.html").read_text(encoding="utf-8"))
    geo_f = text_nodes((SG / geo / folder / "index.html").read_text(encoding="utf-8"))

    f2g = index_map(it_f, geo_f)
    f2c = index_map(it_f, it_c)
    c2f = {v: k for k, v in f2c.items()}

    loc: dict = {}
    for key, val in IT_STRINGS.items():
        if not isinstance(val, str):
            continue
        ferrox_it = c2f.get(val)
        if ferrox_it and ferrox_it in f2g:
            loc[key] = cendora_patches(f2g[ferrox_it])
        elif val in f2g:
            loc[key] = cendora_patches(f2g[val])
        else:
            loc[key] = val

    return loc


def merge_ty_lists(loc: dict, ref: dict) -> None:
    loc["ty_steps"] = list(ref["ty_steps"])
    loc["ty_badges"] = list(ref["ty_badges"])


def main() -> None:
    from _gen_cendora_i18n_once import BLOCKED, FORM  # noqa: WPS433

    out: dict[str, dict] = {"ro": _ro()}
    for code in FERROX:
        loc = build_from_ferrox(code)
        merge_ty_lists(loc, _ro())
        if code in FORM:
            for fk in ("label_name", "label_tel", "label_addr", "ph_name", "ph_tel", "ph_addr"):
                loc[fk] = FORM[code].get(fk.replace("label_", "label_").replace("ph_", "ph_"), loc.get(fk, ""))
            loc["label_name"] = FORM[code]["label_name"]
            loc["label_tel"] = FORM[code]["label_tel"]
            loc["label_addr"] = FORM[code]["label_addr"]
            loc["ph_name"] = FORM[code]["ph_name"]
            loc["ph_tel"] = FORM[code]["ph_tel"]
            loc["ph_addr"] = FORM[code]["ph_addr"]
        if code in BLOCKED:
            loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[code]
        loc["cta_inline"] = loc.get("cta", "")
        out[code] = loc

    Path(__file__).with_name("_cendora_locales_merged.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("locales:", ", ".join(out))


if __name__ == "__main__":
    main()
