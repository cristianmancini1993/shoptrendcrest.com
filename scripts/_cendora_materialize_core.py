#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Align Ferrox™ (shopgearspot) pages with CENDORA™ IT source for locale extraction."""
from __future__ import annotations

import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"
DOMAIN = "shoptrendcrest.com"
PRODUCT_SLUG = "cendora"

# shopgearspot ferrox campaign pages (same 12-piece kit line)
FERROX_BY_GEO: dict[str, tuple[str, str]] = {
    "ro": ("ro", "ferrox-539"),
    "pt": ("pt", "ferrox-1476"),
    "sk": ("sk", "ferrox-536"),
    "si": ("si", "ferrox-535"),
    "hr": ("hr", "ferrox-537"),
    "hu": ("hu", "ferrox-534"),
    "cz": ("cz", "ferrox-538"),
}

OFFERS: dict[str, dict] = {}  # filled from offers.json in main


def _read(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def _line_text(line: str) -> str | None:
    """Extract human-visible text from a single HTML line (heuristic)."""
    if not line.strip() or line.strip().startswith("<") and ">" in line:
        m = re.search(r">([^<]+)<", line)
        if m:
            t = m.group(1).strip()
            if t and not t.startswith("http"):
                return t
    return None


def align_lines(a: list[str], b: list[str]) -> list[tuple[str, str]]:
    """Pair lines with identical structure; return (text_a, text_b) for changed text."""
    pairs: list[tuple[str, str]] = []
    sm = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        la = a[i1:i2]
        lb = b[j1:j2]
        if len(la) == len(lb):
            for x, y in zip(la, lb):
                tx, ty = _line_text(x), _line_text(y)
                if tx and ty and tx != ty:
                    pairs.append((tx, ty))
        elif len(la) == 1 and len(lb) == 1:
            tx, ty = _line_text(la[0]), _line_text(lb[0])
            if tx and ty and tx != ty:
                pairs.append((tx, ty))
    return pairs


def build_it_ferrox_to_cendora() -> dict[str, str]:
    it_f = _read(SG / "it/ferrox/index.html")
    it_c = _read(ROOT / "it/cendora/index.html")
    pairs = align_lines(it_f, it_c)
    out: dict[str, str] = {}
    for old, new in pairs:
        out[old] = new
    # Brand / product tokens
    for old, new in list(out.items()):
        out[old.replace("FERROX™", "FERROX")] = new.replace("CENDORA™", "CENDORA")
    return out


def build_it_to_geo(geo_key: str) -> dict[str, str]:
    folder = FERROX_BY_GEO[geo_key][1]
    geo = FERROX_BY_GEO[geo_key][0]
    it_f = _read(SG / "it/ferrox/index.html")
    geo_f = _read(SG / geo / folder / "index.html")
    pairs = align_lines(it_f, geo_f)
    return {it: loc for it, loc in pairs}


def translate_html_from_ferrox(
    geo_html: str,
    it_to_geo: dict[str, str],
    it_ferrox_to_cendora: dict[str, str],
) -> str:
    """Apply IT ferrox→geo ferrox map, then swap product copy ferrox IT→cendora IT."""
    html = geo_html
    # Longest keys first to avoid partial replacements
    for it_f, it_c in sorted(it_ferrox_to_cendora.items(), key=lambda x: -len(x[0])):
        if it_f not in html:
            # try via geo mapping: it_f -> geo_text
            geo_t = it_to_geo.get(it_f)
            if geo_t and geo_t in html:
                target = it_to_geo.get(it_c, it_c)
                if it_c in it_to_geo:
                    target = it_to_geo[it_c]
                else:
                    # translate cendora IT snippet by replacing known ferrox IT parts
                    target = it_c
                    for fbit, cbit in it_ferrox_to_cendora.items():
                        if fbit in target:
                            target = target.replace(fbit, it_to_geo.get(cbit, cbit))
                html = html.replace(geo_t, target, 1)
        else:
            html = html.replace(it_f, it_to_geo.get(it_c, it_c), 1)
    html = html.replace("FERROX™", "CENDORA™").replace("FERROX", "CENDORA")
    html = html.replace("ferrox", PRODUCT_SLUG)
    html = html.replace("shopgearspot.com", DOMAIN)
    html = html.replace("ferrox-lp", "cendora-lp")
    html = html.replace("/assets/img/products/ferrox/", "/assets/img/products/cendora/")
    return html


def fmt_price(amount: float, currency: str) -> str:
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Kč"
    if currency == "PLN":
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},{frac:02d} zł"
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Ft"
    if currency == "RON":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s} lei"
    if abs(amount - round(amount)) < 0.001:
        return f"{int(round(amount))} €"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s} €"


def was_price(now: float) -> int:
    return int(round(now * 2))


def patch_prices(html: str, now: float, currency: str) -> str:
    was = was_price(now)
    now_s = fmt_price(now, currency)
    was_s = fmt_price(float(was), currency)
    html = re.sub(r'<span class="was">[^<]*</span>', f'<span class="was">{was_s}</span>', html)
    html = re.sub(r'<span class="now">[^<]*</span>', f'<span class="now">{now_s}</span>', html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {now}", html, count=1)
    # FAQ cash price
    html = re.sub(
        r"(Alla consegna consegni |À la livraison|Alla consegna|Na entrega|Bei Lieferung|Al entregar|Przy dostawie|Doručení|Dostava|Kiszállításkor)[^<]{0,80}",
        lambda m: m.group(0),  # leave — patched per locale in post-pass
        html,
        count=0,
    )
    return html


def load_offers() -> dict[str, dict]:
    data = json.loads((ROOT / "content/cendora/offers.json").read_text(encoding="utf-8"))
    return {str(o["id"]): o for o in data if o.get("geo") != "it"}
