# -*- coding: utf-8 -*-
"""Adrice HTML forms for AUREN electric fireplace geo landings."""

from __future__ import annotations

import json
from pathlib import Path

WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"

FORM_META = {
    "pl/auren-1987": {"offer": "1987", "lp": "2008", "key": "93dd62a5a4f987910176f99103f5f73cb831befb"},
    "cz/auren-2400": {"offer": "2400", "lp": "2425", "key": "973b6853f359b2dc82f6e131a902126fba4abf51"},
    "es/auren-2635": {"offer": "2635", "lp": "2662", "key": "ce52f8fe99398bf301d01f91e1dac239860e02c6"},
    "pt/auren-2636": {"offer": "2636", "lp": "2663", "key": "79c9e492ae5109ea012a06d66ac8eee5df78259a"},
    "de/auren-2665": {"offer": "2665", "lp": "2692", "key": "a04999c202f01ccfea28ecca727b2b04db5c637a"},
    "hu/auren-2668": {"offer": "2668", "lp": "2695", "key": "26af2f477db6b9a9eb68256a3743201e4915d81f"},
    "sk/auren-4357": {"offer": "4357", "lp": "4397", "key": "7ef632ed19446d6808b6d78050c553c8ee46ec09"},
    "lv/auren-4358": {"offer": "4358", "lp": "4398", "key": "c300c8c5510b6a15acc700733bbe317502784f2c"},
}

LANG_BY_REL = {
    "pl/auren-1987": "pl",
    "cz/auren-2400": "cs",
    "es/auren-2635": "es",
    "pt/auren-2636": "pt",
    "de/auren-2665": "de",
    "hu/auren-2668": "hu",
    "sk/auren-4357": "sk",
    "lv/auren-4358": "lv",
}

# Adrice submit button labels (confirmed network copy).
SUBMIT_LABELS = {
    "pl/auren-1987": "Zamów teraz",
    "cz/auren-2400": "Objednat nyní",
    "es/auren-2635": "Haz tu pedido",
    "pt/auren-2636": "Encomendar agora",
    "de/auren-2665": "Jetzt bestellen",
    "hu/auren-2668": "Rendeljen most",
    "sk/auren-4357": "Objednajte si teraz ",
    "lv/auren-4358": "Pasūtiet tagad",
}

_LOC = Path(__file__).resolve().parent / "locales" / "auren_fireplace"


def _load_locale(lang: str) -> dict:
    return json.loads((_LOC / f"{lang}.json").read_text(encoding="utf-8"))


def build_form(rel: str) -> str:
    meta = FORM_META[rel]
    lang = LANG_BY_REL[rel]
    c = _load_locale(lang)
    geo = rel.split("/")[0]
    oid = meta["offer"]
    ty = f"https://gadgetshifthub.com/{geo}/auren-{oid}/thank-you.html"
    btn = SUBMIT_LABELS[rel]
    note = c["form_note"]

    return f"""            <form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
<label for="name">{c["label_name"]}</label>
<input id="name" type="text" name="name" autocomplete="name" placeholder="{c["ph_name"]}" required><br>
<label for="tel">{c["label_tel"]}</label>
<input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{c["ph_tel"]}" required><br>
<label for="street-address">{c["label_addr"]}</label>
<input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{c["ph_addr"]}" required><br>
<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{meta["offer"]}" />
<input name="lp" type="hidden" value="{meta["lp"]}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{meta["key"]}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{btn}</button>
</div>
<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
</form>
        <p class="form-note">{note}</p>"""


FORMS = {rel: build_form(rel) for rel in FORM_META}
