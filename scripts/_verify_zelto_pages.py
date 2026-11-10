#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static checks on generated ZELTO HTML (forms + footer leaks)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    ("it", "3990", False),
    ("hu", "762", True),
    ("ro", "763", True),
    ("si", "765", True),
    ("pt", "1673", True),
    ("hr", "1851", True),
    ("es", "2283", True),
    ("de", "2285", True),
    ("pl", "2287", True),
    ("cz", "2289", True),
    ("lv", "3426", True),
    ("sk", "4067", True),
    ("lt", "4276", True),
]

FIELD_ORDER = re.compile(
    r'<label for="name">.*?<label for="tel">.*?<label for="street-address">',
    re.DOTALL,
)

issues: list[str] = []

for geo, offer, gen in PAGES:
    for kind in ("index.html",):
        if geo == "it":
            path = ROOT / geo / f"zelto-{offer}" / kind
        else:
            path = ROOT / geo / f"zelto-{offer}" / kind
        if not path.exists():
            issues.append(f"missing {path.relative_to(ROOT)}")
            continue
        html = path.read_text(encoding="utf-8")
        if geo != "it":
            for leak in ("Gestito da", "Stati Uniti", ">Contatti<"):
                if leak in html:
                    issues.append(f"{path.relative_to(ROOT)}: Italian footer leak {leak}")
        if 'name="postal-code"' in html or 'name="address-level2"' in html:
            issues.append(f"{path.relative_to(ROOT)}: extra address fields")
        form_m = re.search(
            r'<form class="tm-order-form.*?</form>', html, re.DOTALL
        )
        if not form_m:
            issues.append(f"{path.relative_to(ROOT)}: no form")
            continue
        form = form_m.group(0)
        if not FIELD_ORDER.search(form):
            issues.append(f"{path.relative_to(ROOT)}: field order not name→tel→addr")
        for hid in ("offer", "lp", "_key", "uid", "webhook", "thankyoupage"):
            if f'name="{hid}"' not in form:
                issues.append(f"{path.relative_to(ROOT)}: missing {hid}")
        if 'value=""' not in form and 'value=""' not in form.replace(" ", ""):
            pass
        for inp in re.findall(r'<input id="(name|tel|street-address)"[^>]*>', form):
            if ' value="' in form and f'id="{inp}"' in form:
                chunk = re.search(rf'<input id="{inp}"[^>]*>', form)
                if chunk and ' value="' in chunk.group(0) and 'value=""' not in chunk.group(0):
                    issues.append(f"{path.relative_to(ROOT)}: {inp} has non-empty value")

    ty = (
        ROOT / geo / f"zelto-{offer}" / "thank-you" / "index.html"
        if gen
        else ROOT / geo / f"zelto-{offer}" / "thank-you" / "index.html"
    )
    if ty.exists() and geo != "it":
        html = ty.read_text(encoding="utf-8")
        for leak in ("Gestito da", "Stati Uniti", ">Contatti<"):
            if leak in html:
                issues.append(f"{ty.relative_to(ROOT)}: Italian footer leak {leak}")

print(f"{len(issues)} issue(s)")
for i in issues:
    print(i)
