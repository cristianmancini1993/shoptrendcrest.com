#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify CALVOR campaign price pairs in landing + thank-you HTML (local)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from calvor_campaign_prices import VERIFY_ROWS  # noqa: E402

ROOT = SCRIPTS.parent

WAS_RE = re.compile(r'<span class="was">([^<]+)</span>')
NOW_RE = re.compile(r'<span class="now">([^<]+)</span>')
TY_WAS_RE = re.compile(r'<span class="ty-price-was">([^<]+)</span>')
TY_NOW_RE = re.compile(r'<span class="ty-price-now">([^<]+)</span>')
TY_PAY_RE = re.compile(r'<div class="ty-summary-pay">([^<]+)</div>')
BAD_IT_PRICE = re.compile(r"(?<![\d])(?:69\s?\u00a0?€|138\s?\u00a0?€)(?![\d])")
UNRESOLVED_PRICE = re.compile(r"\{price\}")


def check_file(path: Path, now: str, was: str, geo: str) -> list[str]:
    errs: list[str] = []
    if not path.is_file():
        return [f"missing {path}"]
    html = path.read_text(encoding="utf-8")
    was_all = WAS_RE.findall(html) + TY_WAS_RE.findall(html)
    now_all = NOW_RE.findall(html) + TY_NOW_RE.findall(html)
    for w in was_all:
        if w != was:
            errs.append(f"{path.name}: was {w!r} expected {was!r}")
    for n in now_all:
        if n != now:
            errs.append(f"{path.name}: now {n!r} expected {now!r}")
    if path.parent.name == "thank-you":
        m = TY_PAY_RE.search(html)
        if not m or now not in m.group(1):
            errs.append(f"{path}: ty-summary-pay missing now {now!r}")
    if geo != "it" and BAD_IT_PRICE.search(html):
        errs.append(f"{path}: stray Italian reference price")
    if UNRESOLVED_PRICE.search(html):
        errs.append(f"{path}: unresolved {{price}} placeholder")
    if now not in html:
        errs.append(f"{path}: formatted now price {now!r} missing in HTML")
    if was not in html:
        errs.append(f"{path}: formatted was price {was!r} missing in HTML")
    return errs


def main() -> int:
    all_errs: list[str] = []
    print("| GEO | Offer | Now | Was |")
    print("|-----|-------|-----|-----|")
    for geo, offer, g, folder, now, was in VERIFY_ROWS:
        lp = ROOT / g / folder / "index.html"
        ty = ROOT / g / folder / "thank-you" / "index.html"
        for p in (lp, ty):
            all_errs.extend(check_file(p, now, was, g))
        disp_now = now.replace("\u00a0", " ")
        disp_was = was.replace("\u00a0", " ")
        print(f"| {geo} | {offer} | {disp_now} | {disp_was} |")
    if all_errs:
        print("\nErrors:")
        for e in all_errs:
            print(f"  {e}")
        return 1
    print("\nLocal: all 26 files OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())