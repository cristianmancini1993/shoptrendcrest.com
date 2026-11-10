# -*- coding: utf-8 -*-
"""Smoke-check 12 Noventis landings + thank-you pages (local or live base URL)."""

from __future__ import annotations

import re
import sys
import urllib.request

from pathlib import Path

import _smartwatch_ui as ui

ROOT = Path(__file__).resolve().parents[1]

BAD_PATTERNS = [
    (r"Disponibilità", "Italian stock label"),
    (r"Odgovorite na poziv za potvrdu", "Croatian TYP (non-HR)"),
    (r"Što učiniti sada", "Croatian TYP eyebrow (non-HR)"),
    (r"plaćanje pouzećem", "Croatian meta/chrome (non-HR)"),
    (r"Wrist calls", "English ES tag"),
    (r"Handgelenk ruft", "DE tag not fixed"),
    (r"Prepustnice in kalorije", "SI passes typo"),
    (r"Passagens e calorias", "PT passes typo"),
    (r"JĀ, ES VĒLU", "LV CTA typo"),
    (r"Saderība Android e iPhone", "LV Android/iPhone"),
    (r"z zápěstí", "CZ grammar"),
    (r"Koupil jsem ho pro maminku", "CZ Marie review gender"),
    (r"ojačano stiklo", "HR stiklo typo"),
    (r"bez vadjenja", "HR vadjenja typo"),
    (r"s zapešća", "HR s zapešća"),
    (r"Kupila sam ga za majku", "LT HR review 3"),
    (r"Trapūs materialai", "LT compare row"),
    (r"To se misli za dni", "SI machine phrase"),
    (r"prikazen se dobro bere", "SI machine phrase"),
    (r"Dragi pametni uri", "SI compare heading"),
    (r"-Ja, ja\.", "SI FAQ typo"),
    (r"Καλεί ο καρπός", "GR wrist tag"),
    (r"Περάσματα,", "GR steps heading"),
    (r"Китката ме зове", "BG wrist tag"),
    (r"ходене или влак", "BG train typo"),
    (r"umflaturi zilnice", "RO bumps typo"),
    (r"Se piensa por los días", "ES machine phrase"),
    (r"Horas de dormir", "ES sleep tag"),
    (r"mit Händen frei", "DE hands phrase"),
    (r"tägliche Beulen", "DE bumps"),
    (r"praktyczne z technologii", "PL tech phrase"),
    (r"zdravju vašega zdravnika", "SI bad disclaimer"),
    (r"zdrowia lekarza", "PL bad disclaimer"),
    (r"Gesundheit Ihres Arztes", "DE bad disclaimer"),
    (r"salud de su médico", "ES bad disclaimer"),
    (r"здравето на Вашия лекар", "BG bad disclaimer"),
]

FORM_REQUIRED = [
    'name="name"',
    'name="tel"',
    'name="street-address"',
    'name="offer"',
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "hss-verify/1.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def load_html(base: str, geo: str, slug: str, page: str) -> str:
    if base == "local":
        return (ROOT / geo / slug / page).read_text(encoding="utf-8")
    url = f"{base}/{geo}/{slug}/{page}"
    return fetch(url)


def check_page(base: str, geo: str, slug: str, page: str, is_hr: bool) -> list[str]:
    issues: list[str] = []
    try:
        html = load_html(base, geo, slug, page)
    except Exception as exc:
        return [f"LOAD {exc}"]
    for pat, label in BAD_PATTERNS:
        if is_hr:
            if "non-HR" in label or label == "LT HR review 3":
                continue
        elif label.startswith("HR "):
            continue
        if re.search(pat, html, re.I):
            issues.append(label)
    if page == "landing.html":
        for needle in FORM_REQUIRED:
            if needle not in html:
                issues.append(f"missing form field {needle}")
        if 'href="#order-form"' not in html:
            issues.append("missing order CTA anchor")
    if "thank-you" in page and 'fbq(\'track\', \'Purchase\'' not in html:
        issues.append("missing Purchase pixel")
    return issues


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "local"
    if base != "local":
        base = base.rstrip("/")
    failures = 0
    for offer_id, cfg in ui.OFFERS.items():
        geo = cfg["geo"]
        slug = ui.slug_for(offer_id)
        is_hr = geo == "hr"
        for page in ("landing.html", "thank-you.html"):
            issues = check_page(base, geo, slug, page, is_hr)
            status = "OK" if not issues else "FAIL"
            print(f"{status} {geo}/{slug}/{page}")
            for i in issues:
                print(f"  - {i}")
                failures += 1
    print(f"done — {failures} issue(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
