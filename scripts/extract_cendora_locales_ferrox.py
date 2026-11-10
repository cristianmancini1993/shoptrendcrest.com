#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build locale dicts by aligning shopgearspot Ferrox pages to shoptrendcrest CENDORA IT."""
from __future__ import annotations

import json
import re
from pathlib import Path

from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"

FERROX = {
    "ro": ("ro", "ferrox-539"),
    "pt": ("pt", "ferrox-1476"),
    "sk": ("sk", "ferrox-536"),
    "si": ("si", "ferrox-535"),
    "hr": ("hr", "ferrox-537"),
    "hu": ("hu", "ferrox-534"),
    "cs": ("cz", "ferrox-538"),
}

# DE/ES/LT/PL/LV: warmio geos on HGS — use ferrox-less langs via MyMemory batch file if present
EXTRA_JSON = Path(__file__).with_name("_cendora_locales_extra.json")


def text_nodes(html: str) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r">([^<]+)<", html):
        t = m.group(1).strip()
        if not t or t.startswith("http") or "function" in t or "dataLayer" in t:
            continue
        if re.fullmatch(r"[\d\s:.,€+\-–—|·]+", t):
            continue
        out.append(t)
    return out


def align_lists(a: list[str], b: list[str]) -> dict[str, str]:
    """Map text in a to corresponding text in b (same indices when lengths match)."""
    mapping: dict[str, str] = {}
    if len(a) == len(b):
        for x, y in zip(a, b):
            if x != y:
                mapping[x] = y
        return mapping
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            mapping[a[i]] = b[i]
    return mapping


def ferrox_to_cendora_snips() -> dict[str, str]:
    it_f = (SG / "it/ferrox/index.html").read_text(encoding="utf-8")
    it_c = (ROOT / "it/cendora/index.html").read_text(encoding="utf-8")
    tf = text_nodes(it_f)
    tc = text_nodes(it_c)
    return align_lists(tf, tc)


def locale_from_ferrox(code: str) -> dict[str, str | list[str] | tuple[str, ...]]:
    geo, folder = FERROX[code]
    it_f = (SG / "it/ferrox/index.html").read_text(encoding="utf-8")
    geo_f = (SG / geo / folder / "index.html").read_text(encoding="utf-8")
    it_c = (ROOT / "it/cendora/index.html").read_text(encoding="utf-8")

    tf = text_nodes(it_f)
    tg = text_nodes(geo_f)
    tc = text_nodes(it_c)
    f2g = align_lists(tf, tg)
    f2c = ferrox_to_cendora_snips()

    loc: dict[str, str | list[str] | tuple[str, ...]] = {}
    for key, val in IT_STRINGS.items():
        if key in ("ty_steps", "ty_badges"):
            continue
        if not isinstance(val, str):
            continue
        if val in tc:
            # direct node in cendora IT
            idx = tc.index(val)
            if idx < len(tg):
                loc[key] = tg[idx]
                continue
        # ferrox IT intermediate
        rev = {v: k for k, v in f2c.items()}
        ferrox_it = rev.get(val)
        if ferrox_it and ferrox_it in f2g:
            loc[key] = f2g[ferrox_it]
            continue
        if val in f2g:
            loc[key] = f2g[val]
            continue
        loc[key] = val  # fallback IT (flagged in QA)

    # Brand + domain + product image paths in strings
    for k, v in list(loc.items()):
        if isinstance(v, str):
            s = v.replace("FERROX™", "CENDORA™").replace("FERROX", "CENDORA").replace("ferrox", "cendora")
            s = s.replace("shopgearspot.com", "shoptrendcrest.com")
            loc[k] = s

    # ty_steps / badges from RO template structure — copy from _ro and patch brand
    ro = _ro()
    for k in ("ty_steps", "ty_badges"):
        loc[k] = ro[k]

    return loc


def main() -> None:
    out: dict[str, dict] = {"ro": _ro()}
    for code in FERROX:
        print("extract", code)
        out[code] = locale_from_ferrox(code)

    if EXTRA_JSON.is_file():
        extra = json.loads(EXTRA_JSON.read_text(encoding="utf-8"))
        out.update(extra)

    # Merge form placeholders from _gen_cendora_i18n_once FORM
    from _gen_cendora_i18n_once import BLOCKED, FORM  # noqa: WPS433

    for code, data in out.items():
        if code in FORM:
            data["label_name"] = FORM[code]["label_name"]
            data["label_tel"] = FORM[code]["label_tel"]
            data["label_addr"] = FORM[code]["label_addr"]
            data["ph_name"] = FORM[code]["ph_name"]
            data["ph_tel"] = FORM[code]["ph_tel"]
            data["ph_addr"] = FORM[code]["ph_addr"]
        if code in BLOCKED:
            data["form_blocked_msg"], data["form_blocked_btn"] = BLOCKED[code]
        elif code == "ro" and "form_blocked_msg" not in data:
            data["form_blocked_msg"] = (
                "Cererile online pentru această ofertă sunt temporar dezactivate (integrare în configurare). "
                "Scrieți la info@shoptrendcrest.com — vă sunăm."
            )
            data["form_blocked_btn"] = "Trimitere temporar indisponibilă"

    Path(__file__).with_name("_cendora_locales_merged.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("wrote", len(out), "locales")


if __name__ == "__main__":
    main()
