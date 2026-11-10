#!/usr/bin/env python3
"""Extract locale strings by parallel line alignment it/cendora vs geo/ferrox HTML."""
from __future__ import annotations

import difflib
import pprint
import re
from pathlib import Path

from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"

GEOS = {
    "pt": ("pt", "ferrox-1476"),
    "sk": ("sk", "ferrox-536"),
    "si": ("si", "ferrox-535"),
    "hr": ("hr", "ferrox-537"),
    "hu": ("hu", "ferrox-534"),
    "pl": ("pl", "ferrox-540"),
    "cs": ("cz", "ferrox-538"),
}


def texts(html: str) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r">([^<>]+)<", html):
        t = m.group(1).strip()
        if not t or t.startswith("http") or t.startswith("/"):
            continue
        if t in {"|", "→"}:
            continue
        out.append(t)
    return out


def align(it: list[str], geo: list[str]) -> dict[str, str]:
    pairs: dict[str, str] = {}
    sm = difflib.SequenceMatcher(None, it, geo)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("equal", "replace") and (i2 - i1) == (j2 - j1):
            for a, b in zip(it[i1:i2], geo[j1:j2]):
                if a != b:
                    pairs[a] = b
    return pairs


def swap_cendora(s: str) -> str:
    return (
        s.replace("FERROX™", "CENDORA™")
        .replace("FERROX", "CENDORA")
        .replace("oțel inoxidabil", "antiaderent")
        .replace("oțel inoxidabil", "antiaderent")
        .replace("inox", "antiaderent")
        .replace("acciaio inossidabile", "antiaderente")
        .replace("inoxidável", "antiaderente")
        .replace("antiaderentidável", "antiaderente")
        .replace("aço inoxidável", "antiaderente")
        .replace("3 camadas", "12 peças")
        .replace("3 straturi", "12 piese")
    )


def main() -> None:
    it_c = (ROOT / "it/cendora/index.html").read_text(encoding="utf-8")
    it_f = (SG / "it/ferrox/index.html").read_text(encoding="utf-8")
    it_c_tx = texts(it_c)
    it_f_tx = texts(it_f)
    it_f2c = align(it_f_tx, it_c_tx)

    from _cendora_i18n_embed import _ro

    out: dict[str, dict] = {"ro": _ro()}
    for code, (geo, folder) in GEOS.items():
        geo_html = (SG / geo / folder / "index.html").read_text(encoding="utf-8")
        geo_tx = texts(geo_html)
        it_f2geo = align(it_f_tx, geo_tx)
        loc: dict = {}
        for key, it_val in IT_STRINGS.items():
            if key in ("ty_steps",):
                loc[key] = [
                    swap_cendora(
                        it_f2geo.get(
                            it_f,
                            it_f2geo.get(it_val, _map_via_bridge(it_val, it_f2c, it_f2geo)),
                        )
                    )
                    for it_f, it_c in zip(
                        [x for x in it_f2c if it_f2c[x] in it_val],
                        [it_f2c[x] for x in it_f2c if it_f2c[x] in it_val],
                    )
                ] or [_map_via_bridge(x, it_f2c, it_f2geo) for x in it_val]
                continue
            if key in ("ty_badges",):
                loc[key] = tuple(swap_cendora(_map_via_bridge(x, it_f2c, it_f2geo)) for x in it_val)
                continue
            if not isinstance(it_val, str):
                loc[key] = it_val
                continue
            loc[key] = swap_cendora(_map_via_bridge(it_val, it_f2c, it_f2geo))
        # fill gaps from _ro structure with geo meta
        meta_title = re.search(r"<title>([^<]+)</title>", geo_html)
        if meta_title:
            loc["title"] = swap_cendora(meta_title.group(1).strip())
        meta_desc = re.search(r'name="description" content="([^"]+)"', geo_html)
        if meta_desc:
            loc["description"] = swap_cendora(meta_desc.group(1).strip())
        loc.update(_form_ui(code))
        loc.update(_blocked(code))
        loc["cta_inline"] = loc.get("cta", loc.get("cta_inline", ""))
        loc["ty_alt"] = IT_STRINGS["ty_alt"]
        # fallback: any value still italian -> use _ro if same key differs
        ro = _ro()
        for k, v in loc.items():
            if isinstance(v, str) and v == IT_STRINGS.get(k):
                loc[k] = ro[k]
        out[code] = loc

    # manual romance/germanic without ferrox page: translate from _ro() key packs
    for code in ("es", "de", "lt", "lv"):
        out[code] = _manual_from_ro(code)

    header = Path(__file__).with_name("build_cendora_i18n.py").read_text(encoding="utf-8").split("TRANSLATIONS")[0]
    body = "TRANSLATIONS: dict[str, dict[str, Any]] = " + pprint.pformat(out, width=120, sort_dicts=False)
    footer = Path(__file__).with_name("build_cendora_i18n.py").read_text(encoding="utf-8").split("_validate")[1]
    Path(__file__).with_name("build_cendora_i18n.py").write_text(
        header + body + "\n\ndef _validate" + footer,
        encoding="utf-8",
    )


def _map_via_bridge(it_c: str, it_f2c: dict[str, str], it_f2geo: dict[str, str]) -> str:
    if it_c in it_f2geo:
        return it_f2geo[it_c]
    for f, c in it_f2c.items():
        if c == it_c:
            g = it_f2geo.get(f)
            if g:
                return g
    for f, g in it_f2geo.items():
        if f == it_c:
            return g
    return it_c


def _form_ui(code: str) -> dict[str, str]:
    from _cendora_align_locales import FORM

    return FORM.get(code, {})


def _blocked(code: str) -> dict[str, str]:
    from _cendora_align_locales import BLOCKED

    msg, btn = BLOCKED.get(code, BLOCKED["ro"])
    return {"form_blocked_msg": msg, "form_blocked_btn": btn}


def _manual_from_ro(code: str) -> dict:
    from _cendora_i18n_embed import _de, _es, _lt, _lv

    return {"es": _es, "de": _de, "lt": _lt, "lv": _lv}[code]()


if __name__ == "__main__":
    main()
