#!/usr/bin/env python3
"""Content checks on live shoptrendcrest.com WARMIO pages (not HTTP-only)."""
from __future__ import annotations

import importlib.util
import re
import sys
import urllib.request
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BASE = "https://shoptrendcrest.com"

spec = importlib.util.spec_from_file_location("gen", SCRIPTS / "gen_warmio_geos.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

nf_spec = importlib.util.spec_from_file_location("nf", SCRIPTS / "warmio_network_forms.py")
nfmod = importlib.util.module_from_spec(nf_spec)
assert nf_spec.loader is not None
nf_spec.loader.exec_module(nfmod)

# Confirmed copy fixes (keep in sync with _warmio_sync_copy.py).
COPY_FIX_MARKERS: dict[str, list[str]] = {
    "hu": ["a szállítási cím és az időpont egyeztetése céljából"],
    "si": ["Namestila sem ga nad televizor, priključila v električno vtičnico"],
    "pl": [
        "Złóż zamówienie teraz, zanim skończy się zapas promocyjny",
        "Zużywa do 93% mniej energii niż tradycyjne klimatyzatory",
        "gdy otrzymasz paczkę",
    ],
}

LOCALE_MARKERS: dict[str, list[str]] = {
    "ro": ["mai puțin mucegai", "Usucă aerul și ridică praful"],
    "si": ["KOTLA", "Zarošena okna", "Tristopenjska filtracija HEPA H13"],
    "hr": ["KOTAO", "promotivne zalihe", "Zamagljena stakla"],
    "es": ["Contra reembolso", "Deshumidificación automática"],
    "pl": ["4-letnia gwarancja", "bardziej eleganckie"],
    "sk": ["už kúri s WARMIO", "Zarosené okná", "Pripevníte na stenu"],
    "lv": ["APMAKSA SAŅEMŠANAS BRĪDĪ", "SASILDA JŪS", "ilustrēta rokasgrāmata"],
    "lt": ["Tolygus šilumos paskirstymas", "dėmes kampuose", "akcinių prekių"],
}

FOOTER_BAD = (
    "About us</a>",
    "All rights reserved",
    "Powered by WHATECH MOBILE CO., LIMITED</p>",
    'site-footer__heading">Information</h4>',
)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "warmio-prod-verify/2"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")


def check_lp(offer: str, cfg: dict, html: str) -> list[str]:
    geo = cfg["geo"]
    errs: list[str] = []
    labs = re.findall(
        r'for="(name|tel|street-address|postal-code|address-level2)"',
        html,
    )
    exp = nfmod.FIELD_ORDER.get(offer, ["name", "tel", "street-address"])
    if labs != exp:
        errs.append(f"form fields {labs} != {exp}")
    now = mod.fmt_price(cfg["price"], cfg["currency"])
    was = mod.fmt_price(mod.list_was_price(cfg), cfg["currency"])
    if now not in html:
        errs.append(f"missing price {now!r}")
    if was not in html:
        errs.append(f"missing was {was!r}")
    if cfg["currency"] in ("CZK", "PLN") and ",00" in html and now.replace(" ", "") in html.replace(",00", ""):
        if re.search(r"\d+,\d{2}\s*(Kč|zł)", html):
            errs.append("price still has ,00 decimals")
    for bad in FOOTER_BAD:
        if bad in html and geo != "de":
            if bad == 'site-footer__heading">Information</h4>':
                continue
            errs.append(f"footer EN: {bad[:40]}")
        elif bad in html and geo == "de" and bad.startswith("site-footer"):
            if "Information" in bad:
                continue
            errs.append(f"footer EN: {bad[:40]}")
    if "In tutta Italia entro 24" in html:
        errs.append("Italian delivery leak in features")
    markers = COPY_FIX_MARKERS.get(geo, []) + LOCALE_MARKERS.get(geo, [])
    for m in markers:
        if m not in html:
            errs.append(f"missing copy marker: {m[:50]}")
    if geo == "hu" and "az cím" in html:
        errs.append("HU bad FAQ article az cím")
    if geo == "pl" and "Pan/Pani" in html:
        errs.append("PL Pan/Pani leak")
    if re.search(r'ty-trust__badge">[^<]*\b2\s+(ani|Jahre|lata)', html):
        errs.append("2-year warranty on page")
    return errs


def check_typ(offer: str, cfg: dict, html: str) -> list[str]:
    errs: list[str] = []
    if re.search(
        r'ty-trust__badge">[^<]*(2 anni|2 Jahre|24 mes|2 lata)',
        html,
        re.I,
    ):
        errs.append("TYP badge still 2 years")
    badges = re.findall(r'ty-trust__badge">([^<]+)', html)
    if badges and not any("4" in b for b in badges if "🛡" in b or "Garan" in b or "gwaran" in b.lower()):
        errs.append(f"TYP warranty badge unclear: {badges}")
    geo = cfg["geo"]
    if geo == "si" and "Ostaja le še" not in html and "Ostaja še le" in html:
        errs.append("SI ty_sub word order")
    for bad in FOOTER_BAD:
        if bad in html and geo != "de":
            if "Information" in bad:
                continue
            errs.append(f"footer EN: {bad[:40]}")
    return errs


def main() -> int:
    failed = 0
    for offer, cfg in sorted(mod.GEOS.items(), key=lambda x: x[1]["geo"]):
        geo = cfg["geo"]
        for kind, path in (("LP", ""), ("TYP", "thank-you/")):
            url = f"{BASE}/{geo}/warmio-{offer}/{path}"
            try:
                html = fetch(url)
            except Exception as e:
                print(f"FAIL {offer} {geo} {kind}: fetch {e}")
                failed += 1
                continue
            errs = check_lp(offer, cfg, html) if kind == "LP" else check_typ(offer, cfg, html)
            if errs:
                failed += 1
                print(f"FAIL {offer} {geo} {kind}: " + "; ".join(errs))
            else:
                print(f"OK   {offer} {geo} {kind}")
    print(f"\nFailed: {failed}/26")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
