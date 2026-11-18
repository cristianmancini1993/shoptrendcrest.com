#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Live CALVOR campaign price span check (was/now pairs only)."""

from __future__ import annotations

import re
import ssl
import urllib.request

from calvor_campaign_prices import VERIFY_ROWS

BASE = "https://shoptrendcrest.com"

WAS = re.compile(r'<span class="was">([^<]+)</span>')
NOW = re.compile(r'<span class="now">([^<]+)</span>')
TY_WAS = re.compile(r'<span class="ty-price-was">([^<]+)</span>')
TY_NOW = re.compile(r'<span class="ty-price-now">([^<]+)</span>')


def fetch(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "calvor-price-check/1.0"})
    with urllib.request.urlopen(req, timeout=25, context=ctx) as resp:
        return resp.read().decode("utf-8", "replace")


def norm(s: str) -> str:
    return s.replace("\u00a0", " ").strip()


def check_lp(html: str, enow: str, ewas: str) -> list[str]:
    errs = []
    was = [norm(x) for x in dict.fromkeys(WAS.findall(html))]
    now = [norm(x) for x in dict.fromkeys(NOW.findall(html))]
    if was != [norm(ewas)]:
        errs.append(f"was={was}")
    if now != [norm(enow)]:
        errs.append(f"now={now}")
    return errs


def check_ty(html: str, enow: str, ewas: str) -> list[str]:
    errs = []
    was = [norm(x) for x in TY_WAS.findall(html)]
    now = [norm(x) for x in TY_NOW.findall(html)]
    if was != [norm(ewas)]:
        errs.append(f"ty-was={was}")
    if now != [norm(enow)]:
        errs.append(f"ty-now={now}")
    if norm(enow) not in norm(html):
        errs.append("now missing in body")
    return errs


def main() -> int:
    errs: list[str] = []
    print("| GEO | Offer | LP | TY | Now | Was |")
    print("|-----|-------|----|----|-----|-----|")
    for geo, offer, g, folder, enow, ewas in VERIFY_ROWS:
        path = f"{g}/{folder}"
        lp_e: list[str] = []
        ty_e: list[str] = []
        try:
            lp_e = check_lp(fetch(f"{BASE}/{path}/"), enow, ewas)
        except Exception as ex:
            lp_e = [str(ex)]
        try:
            ty_e = check_ty(fetch(f"{BASE}/{path}/thank-you/"), enow, ewas)
        except Exception as ex:
            ty_e = [str(ex)]
        lp_st = "OK" if not lp_e else "FAIL"
        ty_st = "OK" if not ty_e else "FAIL"
        if lp_e or ty_e:
            errs.append(f"{geo}: lp {lp_e} ty {ty_e}")
        print(f"| {geo} | {offer} | {lp_st} | {ty_st} | {enow.replace(chr(160), ' ')} | {ewas.replace(chr(160), ' ')} |")
    if errs:
        print("\nLive mismatches:")
        for e in errs:
            print(" ", e)
        return 1
    print("\nLive: all 13 GEO OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())