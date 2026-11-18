#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify Calvor™ campaign forms + translation (local HTML)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from calvor_campaign_prices import GEOS, offer_folder  # noqa: E402
from calvor_network_forms import (  # noqa: E402
    ACTION,
    FORM_UI,
    FORMS,
    OFFER_GEO,
    OFFER_LP_KEY,
    SCRIPT,
    WEBHOOK,
    thankyou_url,
)

ROOT = SCRIPTS.parent

IT_SNIPPETS = re.compile(
    r"(?i)(offerto da capitaladv|prodotti selezionati|alcune immagini in questa|"
    r"contrassegno alla consegna|tutti i diritti riservati|>chi siamo<|manuale in italiano|"
    r"cose ricevi|operativo dal primo giorno|telecomando incluso|allà consegna:)"
)


def field_order(html: str) -> list[str]:
    return re.findall(r'<input id="([^"]+)"', html)


def required_flags(html: str, fid: str) -> bool:
    m = re.search(rf'<input id="{fid}"[^>]*>', html)
    return bool(m and "required" in m.group(0))


def verify_form(offer: str, html: str) -> list[str]:
    errs: list[str] = []
    if WEBHOOK not in html:
        errs.append("webhook")
    if ACTION not in html or 'method="post"' not in html:
        errs.append("action/method")
    if SCRIPT not in html:
        errs.append("js-v2")
    lp, key = OFFER_LP_KEY[offer]
    ty = thankyou_url(OFFER_GEO[offer], offer)
    for needle in (f'value="{offer}"', f'value="{lp}"', f'value="{key}"', ty):
        if needle not in html:
            errs.append(f"missing {needle[:40]}")
    ui = FORM_UI[offer]
    order = field_order(html)
    expected: list[str]
    if ui["layout"] == "nta":
        expected = ["name", "tel", "street-address"]
    elif ui["layout"] == "atn":
        expected = ["name", "street-address", "tel"]
    elif ui["layout"] == "hu":
        expected = ["name", "tel", "street-address", "address-level2", "postal-code"]
    else:
        expected = ["name", "tel", "street-address", "postal-code", "address-level2"]
    if order[: len(expected)] != expected:
        errs.append(f"field order {order} expected {expected}")
    if ui["layout"] == "hu":
        if required_flags(html, "postal-code") is not True:
            errs.append("HU postal required")
        if required_flags(html, "address-level2") is not False:
            errs.append("HU city must be optional")
    if ui["layout"] == "ro":
        if required_flags(html, "postal-code") is not True:
            errs.append("RO postal required")
        if required_flags(html, "address-level2") is not False:
            errs.append("RO city must be optional")
    if ui["layout"] == "atn" or ui["layout"] == "nta":
        for fid in expected:
            if not required_flags(html, fid):
                errs.append(f"{fid} must be required")
    btn = re.search(r'<button name="submit"[^>]*>([^<]+)</button>', html)
    if not btn or btn.group(1) != ui["submit"]:
        errs.append(f"submit {btn.group(1) if btn else None!r}")
    # localized placeholders
    name_ph = re.search(r'id="name"[^>]*placeholder="([^"]*)"', html)
    if name_ph and name_ph.group(1) == ui["name_l"].rstrip("*"):
        errs.append("name placeholder equals label (need example)")
    return errs


def italian_hits(html: str) -> list[str]:
    return sorted(set(IT_SNIPPETS.findall(html)))


IT_CAMPAIGN_TY = "https://shoptrendcrest.com/it/calvor-3990/thank-you/"


def main() -> int:
    print("| GEO | Offer | Form | TY form | Webhook | i18n LP | i18n TY |")
    print("|-----|-------|------|---------|---------|---------|---------|")
    fails: list[str] = []
    for oid, cfg in sorted(GEOS.items(), key=lambda x: (x[0] != "3990", x[1]["geo"])):
        folder = offer_folder(oid)
        lp_p = ROOT / cfg["geo"] / folder / "index.html"
        ty_p = ROOT / cfg["geo"] / folder / "thank-you" / "index.html"
        for label, path in (("LP", lp_p), ("TY", ty_p)):
            if label == "TY" and oid == "3990":
                pass
        lp_html = lp_p.read_text(encoding="utf-8")
        ty_html = ty_p.read_text(encoding="utf-8")
        fe = verify_form(oid, lp_html)
        if oid == "3990" and IT_CAMPAIGN_TY not in lp_html:
            fe = fe + ["IT thankyoupage"]
        if oid == "3990" and "/it/3990/thank-you/" in lp_html:
            fe = fe + ["IT bad thankyou path"]
        it_lp = italian_hits(lp_html) if oid != "3990" else []
        it_ty_hits = italian_hits(ty_html) if oid != "3990" else []
        form_st = "OK" if not fe else "FAIL"
        wh = "OK" if WEBHOOK in lp_html else "FAIL"
        i_lp = "OK" if not it_lp else f"{len(it_lp)} IT"
        i_ty = "OK" if not it_ty_hits else f"{len(it_ty_hits)} IT"
        if fe or it_lp or (oid != "3990" and it_ty_hits):
            fails.append(f"{cfg['geo']}/{oid}: form={fe} it_lp={it_lp} it_ty={i_ty}")
        print(
            f"| {cfg['geo'].upper()} | {oid} | {form_st} | — | {wh} | {i_lp} | {i_ty} |"
        )
    if fails:
        print("\nDetails:")
        for f in fails:
            print(" ", f)
        return 1
    print("\nLocal campaign verify: OK (13 LP + translation spot-check).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())