#!/usr/bin/env python3
"""Verify generated WARMIO HTML in repo (not live)."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent

spec = importlib.util.spec_from_file_location("gen", SCRIPTS / "gen_warmio_geos.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

nf_spec = importlib.util.spec_from_file_location("nf", SCRIPTS / "warmio_network_forms.py")
nfmod = importlib.util.module_from_spec(nf_spec)
assert nf_spec.loader is not None
nf_spec.loader.exec_module(nfmod)


def main() -> int:
    failed: list[str] = []
    for offer, cfg in mod.GEOS.items():
        geo = cfg["geo"]
        for suffix in ("index.html", "thank-you/index.html"):
            p = ROOT / geo / f"warmio-{offer}" / suffix
            html = p.read_text(encoding="utf-8")
            now = mod.fmt_price(cfg["price"], cfg["currency"])
            if now not in html:
                failed.append(f"{offer} {suffix}: missing price {now!r}")
            if "About us</a>" in html:
                failed.append(f"{offer} {suffix}: English About us")
            if "All rights reserved" in html:
                failed.append(f"{offer} {suffix}: English rights")
            if "Powered by WHATECH" in html:
                failed.append(f"{offer} {suffix}: English Powered by")
        lp = (ROOT / geo / f"warmio-{offer}" / "index.html").read_text(encoding="utf-8")
        labs = re.findall(
            r'for="(name|tel|street-address|postal-code|address-level2)"',
            lp,
        )
        exp = nfmod.FIELD_ORDER.get(offer, ["name", "tel", "street-address"])
        if labs != exp:
            failed.append(f"{offer} LP: field order {labs} expected {exp}")
        if re.search(r"2 (anni|Jahre|lata|mesi)", lp, re.I):
            failed.append(f"{offer} LP: possible 2-year warranty leak")
        ty = (ROOT / geo / f"warmio-{offer}" / "thank-you/index.html").read_text(
            encoding="utf-8"
        )
        if re.search(r'ty-trust__badge">[^<]*2 ', ty):
            failed.append(f"{offer} TYP: 2-year badge")
    print(f"Failed: {len(failed)}")
    for line in failed:
        print(line)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
