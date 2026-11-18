#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Live Calvor campaign form + i18n check (no form submit)."""

from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path
import sys

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from calvor_campaign_prices import GEOS, offer_folder  # noqa: E402
from calvor_network_forms import WEBHOOK  # noqa: E402
from verify_calvor_campaign import IT_SNIPPETS, verify_form  # noqa: E402

BASE = "https://shoptrendcrest.com"


def fetch(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "calvor-live-verify/1.0"})
    with urllib.request.urlopen(req, timeout=35, context=ctx) as resp:
        return resp.read().decode("utf-8", "replace")


def main() -> int:
    print("| GEO | Form | Webhook | Field order | i18n LP | i18n TY |")
    print("|-----|------|---------|-------------|---------|---------|")
    fail = 0
    for oid, cfg in sorted(GEOS.items(), key=lambda x: (x[0] != "3990", x[1]["geo"])):
        folder = offer_folder(oid)
        base = f"{BASE}/{cfg['geo']}/{folder}/"
        try:
            lp = fetch(base)
            ty = fetch(base + "thank-you/")
        except Exception as ex:
            print(f"| {cfg['geo'].upper()} | FAIL | — | — | — | fetch: {ex} |")
            fail += 1
            continue
        fe = verify_form(oid, lp)
        form_st = "OK" if not fe else f"FAIL ({len(fe)})"
        wh = "OK" if WEBHOOK in lp else "FAIL"
        ord_st = "OK" if not any("field order" in e for e in fe) else "FAIL"
        it_lp = (
            "—"
            if oid == "3990"
            else ("OK" if not IT_SNIPPETS.search(lp) else "FAIL")
        )
        it_ty = (
            "—"
            if oid == "3990"
            else ("OK" if not IT_SNIPPETS.search(ty) else "FAIL")
        )
        if fe or wh != "OK" or it_lp == "FAIL" or it_ty == "FAIL":
            fail += 1
        print(f"| {cfg['geo'].upper()} | {form_st} | {wh} | {ord_st} | {it_lp} | {it_ty} |")
    if fail:
        print(f"\nLive: {fail} GEO issue(s).")
        return 1
    print("\nLive: all 13 GEO OK (HTML check only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())