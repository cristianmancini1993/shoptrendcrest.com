#!/usr/bin/env python3
"""Verify live WARMIO campaign URLs on shoptrendcrest.com."""
from __future__ import annotations

import importlib.util
import re
import sys
import urllib.request
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gen", SCRIPTS / "gen_warmio_geos.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

BASE = "https://shoptrendcrest.com"
GEOS = mod.GEOS
fmt_price = mod.fmt_price
list_was_price = mod.list_was_price

LANDING_MARKERS = {
    "de": "WARMIO™",
    "hu": "WARMIO™",
    "pl": "WARMIO™",
    "es": "PROMO",
    "it": "WARMIO™",
}


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "warmio-verify/1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def check_landing(offer: str, cfg: dict) -> list[str]:
    geo = cfg["geo"]
    url = f"{BASE}/{geo}/warmio-{offer}/"
    status, html = fetch(url)
    errs: list[str] = []
    if status != 200:
        errs.append(f"status {status}")
        return errs
    lang_m = re.search(r'<html lang="([^"]+)"', html)
    if not lang_m or lang_m.group(1) != cfg["lang"]:
        errs.append(f"lang={lang_m.group(1) if lang_m else None}")
    now = fmt_price(cfg["price"], cfg["currency"])
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    if now not in html:
        errs.append(f"missing now {now!r}")
    if was not in html:
        errs.append(f"missing was {was!r}")
    om = re.search(r'name="offer"[^>]*value="([^"]*)"', html)
    if not om or om.group(1) != offer:
        errs.append(f"offer={om.group(1) if om else None}")
    ty = f"{BASE}/{geo}/warmio-{offer}/thank-you/"
    tm = re.search(r'name="thankyoupage"[^>]*value="([^"]*)"', html)
    if not tm or tm.group(1) != ty:
        errs.append(f"thankyoupage={tm.group(1) if tm else None}")
    nf_spec = importlib.util.spec_from_file_location(
        "warmio_network_forms", SCRIPTS / "warmio_network_forms.py"
    )
    nf_mod = importlib.util.module_from_spec(nf_spec)
    assert nf_spec.loader is not None
    nf_spec.loader.exec_module(nf_mod)
    FORMS = nf_mod.FORMS
    FIELD_ORDER = nf_mod.FIELD_ORDER

    if offer not in FORMS:
        errs.append("missing network form config")
    lp_m = re.search(r'name="lp"[^>]*value="([^"]*)"', html)
    if not lp_m or not lp_m.group(1).strip():
        errs.append("empty lp")
    expected = FIELD_ORDER.get(offer, ["name", "tel", "street-address"])
    labs = re.findall(
        r'for="(name|tel|street-address|postal-code|address-level2)"',
        html,
    )
    if labs != expected:
        errs.append(f"field order {labs}")
    if "tm-order-form" not in html:
        errs.append("no form")
    if len(html) < 8000:
        errs.append("body too short (stub?)")
    return errs


def check_typ(offer: str, cfg: dict) -> list[str]:
    geo = cfg["geo"]
    url = f"{BASE}/{geo}/warmio-{offer}/thank-you/"
    status, html = fetch(url)
    errs: list[str] = []
    if status != 200:
        errs.append(f"status {status}")
        return errs
    now = fmt_price(cfg["price"], cfg["currency"])
    if now not in html:
        errs.append(f"missing price {now!r}")
    if "WARMIO" not in html:
        errs.append("no WARMIO")
    return errs


def main() -> int:
    rows: list[str] = []
    failed = 0
    for offer, cfg in sorted(GEOS.items(), key=lambda x: x[1]["geo"]):
        geo = cfg["geo"]
        for kind, fn in (("LP", check_landing), ("TYP", check_typ)):
            url = f"{BASE}/{geo}/warmio-{offer}/" + ("thank-you/" if kind == "TYP" else "")
            status, _ = fetch(url)
            errs = fn(offer, cfg) if status == 200 else [f"status {status}"]
            ok = "OK" if not errs else "; ".join(errs)
            if errs:
                failed += 1
            rows.append(f"{offer} {geo} {kind} HTTP {status} {ok}")
    print("\n".join(rows))
    print(f"\nFailed checks: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
