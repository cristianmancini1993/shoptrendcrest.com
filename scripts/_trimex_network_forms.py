# -*- coding: utf-8 -*-
"""Adrice Network form HTML per TRIMEX offer landings."""
from __future__ import annotations

from _order_form_fields_i18n import geo_from_rel, tm_order_fields_html

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
ACTION = "https://offers.adricenetwork.com/forms/html/"

FORM_META = {
    "it/trimex-3209": {"offer": "3209", "lp": "3243", "key": "a8f3f892387f175bf6e35938d46afdb47069fd18"},
    "sk/trimex-4042": {"offer": "4042", "lp": "4082", "key": "1bf0bc8a5fbc0b8a85176a7bb97d3ffb61d06a1a"},
    "lv/trimex-4043": {"offer": "4043", "lp": "4083", "key": "d1915bcc71c418cadecbe7e62655590f0f9ef97d"},
    "hu/trimex-2918": {"offer": "2918", "lp": "2951", "key": "c7ae3e69954db9658d5652062f2930a009b4a131"},
    "cz/trimex-2645": {"offer": "2645", "lp": "2672", "key": "7db299e25314debd841906332a75d97dd76bcaf9"},
    "hr/trimex-2643": {"offer": "2643", "lp": "2670", "key": "79f5da0e2b80dcf037084843aec350d6030edb32"},
    "si/trimex-2642": {"offer": "2642", "lp": "2669", "key": "48b1b5522df8bf2e0f3f300cc60d1a13fdc8ae9e"},
    "ro/trimex-2637": {"offer": "2637", "lp": "2664", "key": "7611c6c16811da011ffa39878e1d1e1e90c70d50"},
    "pt/trimex-1816": {"offer": "1816", "lp": "1836", "key": "faf129bc8ab976e80f15993946075650d2a03f1b"},
    "es/trimex-1815": {"offer": "1815", "lp": "1835", "key": "48bb86c195445a81307aec8d4b04697e201f3bde"},
    "pl/trimex-24": {"offer": "24", "lp": "32", "key": "6a77b45564a4ed22ec5557b95fd294fd076a3123"},
    "de/trimex-23": {"offer": "23", "lp": "31", "key": "08bfbb3ff112cf6e054ab7ec7d04dd6811b4d6bc"},
}

def _form(fields: str, offer: str, lp: str, ty: str, key: str, btn: str, note: str) -> str:
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post">
{fields}
        <input name="uid" type="hidden" value="{UID}">
        <input name="offer" type="hidden" value="{offer}">
        <input name="lp" type="hidden" value="{lp}">
        <input name="subid" id="subid" type="hidden" value="">
        <input name="thankyoupage" type="hidden" value="{ty}">
        <input name="webhook" type="hidden" value="{WEBHOOK}">
        <input name="_key" type="hidden" value="{key}">
        <button type="submit" class="cta-btn">{btn}</button>
        <p class="form-note">{note}</p>
      </form>"""


SUBMIT_LABELS: dict[str, str] = {
    "it/trimex-3209": "CONFERMA L'ORDINE",
    "sk/trimex-4042": "Objednajte si teraz",
    "lv/trimex-4043": "Pasūtiet tagad",
    "hu/trimex-2918": "Rendeljen most",
    "cz/trimex-2645": "Objednat nyní",
    "hr/trimex-2643": "Pošaljite narudžbu",
    "si/trimex-2642": "Pošljite naročilo",
    "ro/trimex-2637": "Plasează comanda",
    "pt/trimex-1816": "Encomendar agora",
    "es/trimex-1815": "Haz tu pedido",
    "pl/trimex-24": "Wyślij zamówienie",
    "de/trimex-23": "Bestellung absenden",
}


def build_forms(notes: dict[str, str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for rel, meta in FORM_META.items():
        fields = tm_order_fields_html(geo_from_rel(rel))
        btn = SUBMIT_LABELS[rel]
        geo, slug = rel.split("/", 1)
        ty = f"https://gadgetshifthub.com/{geo}/{slug}/thank-you.html"
        out[rel] = _form(fields, meta["offer"], meta["lp"], ty, meta["key"], btn, notes[rel])
    return out
