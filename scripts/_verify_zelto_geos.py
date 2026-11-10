#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = {
    "762": ("hu", "39999", "79998", "Ft"),
    "763": ("ro", "379", "758", "lei"),
    "765": ("si", "79", "158", "€"),
    "1673": ("pt", "89", "178", "€"),
    "1851": ("hr", "99", "198", "€"),
    "2283": ("es", "89", "178", "€"),
    "2285": ("de", "89", "178", "€"),
    "2287": ("pl", "299", "598", "zł"),
    "2289": ("cz", "1999", "3998", "Kč"),
    "3426": ("lv", "99", "198", "€"),
    "4067": ("sk", "99", "198", "€"),
    "4276": ("lt", "99", "198", "€"),
}

ITALIAN_MARKERS = [
    "lavorativi",
    "Contrassegno alla consegna",
    "acquisto verificato",
    "salotto",
    "Di solito 2–4",
    "Pagamento in contanti al corriere",
]


def norm_price(s: str) -> str:
    return re.sub(r"[\s\u00a0]", "", s)


issues: list[str] = []

for offer, (geo, now, was, _cur) in GEOS.items():
    landing = ROOT / geo / f"zelto-{offer}" / "index.html"
    typ = ROOT / geo / f"zelto-{offer}" / "thank-you" / "index.html"
    for path in (landing, typ):
        if not path.exists():
            issues.append(f"missing {path.relative_to(ROOT)}")
            continue
        html = path.read_text(encoding="utf-8")
        for n in re.findall(r'class="now">([^<]+)', html):
            if norm_price(now) not in norm_price(n):
                issues.append(f"{path.relative_to(ROOT)}: now {n!r} != {now}")
        for w in re.findall(r'class="was">([^<]+)', html):
            if norm_price(was) not in norm_price(w):
                issues.append(f"{path.relative_to(ROOT)}: was {w!r} != {was}")
        if geo != "it":
            for m in ITALIAN_MARKERS:
                if m in html:
                    issues.append(f"{path.relative_to(ROOT)}: Italian leak {m!r}")

    if landing.exists():
        html = landing.read_text(encoding="utf-8")
        if f'value="{offer}"' not in html:
            issues.append(f"{geo}: offer id")
        if html.count('name="name"') != 1 or html.count('name="tel"') != 1:
            issues.append(f"{geo}: name/tel fields")
        if html.count('name="street-address"') != 1:
            issues.append(
                f"{geo}: street-address inputs {html.count('name=\"street-address\"')}"
            )
        for bad in ('name="postal-code"', 'name="address-level2"'):
            if bad in html:
                issues.append(f"{geo}: extra visible field {bad}")
        if re.search(r"cpa|CPL|€/lead", html, re.I):
            issues.append(f"{geo}: CPA visible")

# IT
it_l = ROOT / "it" / "zelto-3990" / "index.html"
it_t = ROOT / "it" / "zelto-3990" / "thank-you.html"
for path in (it_l, it_t):
    if path.exists():
        html = path.read_text(encoding="utf-8")
        for n in re.findall(r'class="now">([^<]+)', html):
            if "69" not in n or "€" not in n:
                issues.append(f"it: now {n}")
        if 'value="3990"' not in html and path == it_l:
            issues.append("it: offer")

print(f"{len(issues)} issue(s)")
for i in issues:
    print(i)
