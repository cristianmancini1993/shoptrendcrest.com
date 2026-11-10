#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA: WARMIO campaign pages (26 files)."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load_geos() -> dict:
    spec = importlib.util.spec_from_file_location(
        "gen_warmio_geos", SCRIPTS / "gen_warmio_geos.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.GEOS, mod.fmt_price, mod.list_was_price


def main() -> int:
    geos, fmt_price, list_was_price = load_geos()
    expected: list[Path] = []
    for offer, cfg in geos.items():
        folder = f"warmio-{offer}"
        expected.append(ROOT / cfg["geo"] / folder / "index.html")
        expected.append(ROOT / cfg["geo"] / folder / "thank-you" / "index.html")

    errs: list[str] = []
    for path in expected:
        if not path.is_file():
            errs.append(f"missing {path.relative_to(ROOT)}")

    it_spot = (
        "Spedizione veloce",
        "Contrassegno",
        "caldaia",
        "stufetta",
        "Paghi al corriere",
        "Garanzia 4 anni",
    )
    for offer, cfg in geos.items():
        lp = ROOT / cfg["geo"] / f"warmio-{offer}" / "index.html"
        if not lp.is_file():
            continue
        html = lp.read_text(encoding="utf-8")
        lang_m = re.search(r'<html lang="([^"]+)"', html)
        if not lang_m or lang_m.group(1) != cfg["lang"]:
            errs.append(f"{lp.relative_to(ROOT)}: lang {lang_m}")
        now = fmt_price(cfg["price"], cfg["currency"])
        was = fmt_price(list_was_price(cfg), cfg["currency"])
        if now not in html:
            errs.append(f"{lp.relative_to(ROOT)}: price now {now!r} not found")
        if was not in html:
            errs.append(f"{lp.relative_to(ROOT)}: price was {was!r} not found")
        offer_m = re.search(r'name="offer"[^>]*value="([^"]*)"', html)
        if not offer_m or not offer_m.group(1).strip():
            errs.append(f"{lp.relative_to(ROOT)}: empty offer")
        if "74€" in html or "148€" in html:
            errs.append(f"{lp.relative_to(ROOT)}: old IT price remnant")
        if cfg["geo"] != "it":
            for s in it_spot:
                if s.lower() in html.lower():
                    errs.append(f"{lp.relative_to(ROOT)}: Italian spot {s!r}")
                    break

    print(f"Expected files: {len(expected)}")
    if errs:
        print("\n".join(errs))
        return 1
    print("QA OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
