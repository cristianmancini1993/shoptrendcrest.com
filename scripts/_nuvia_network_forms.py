# -*- coding: utf-8 -*-
"""Adrice Network form HTML per Nuvia offer — 3 fields: name, phone, address."""
from __future__ import annotations

import importlib.util
from pathlib import Path

from _order_form_fields_i18n import tm_order_fields_html

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

TM_FORM_CSS = """
.order-form.tm-order-form label{display:block;font-size:13px;font-weight:700;margin:0 0 5px;color:var(--color-text);}
.order-form.tm-order-form button[type="submit"]{
  display:block;width:100%;background:var(--color-accent);color:#fff;border:none;
  font-family:var(--font);font-size:16px;font-weight:800;padding:17px;
  border-radius:var(--radius-sm);cursor:pointer;margin-top:4px;
}
.order-form.tm-order-form button[type="submit"]:active{background:var(--color-accent-dark);}
"""

LABELS = {
    "pt": {
        "label_name": "Nome e apelido*",
        "label_phone": "Número de telefone*",
        "label_addr": "Morada de envio*",
    },
    "el": {
        "label_name": "Όνομα και επώνυμο*",
        "label_phone": "Αριθμός τηλεφώνου*",
        "label_addr": "Διεύθυνση παράδοσης*",
    },
    "bg": {
        "label_name": "Име и фамилия*",
        "label_phone": "Телефонен номер*",
        "label_addr": "Адрес за доставка*",
    },
    "ro": {
        "label_name": "Nume și prenume*",
        "label_phone": "Număr de telefon*",
        "label_addr": "Adresa de livrare*",
    },
    "lt": {
        "label_name": "Vardas ir pavardė*",
        "label_phone": "Telefono numeris*",
        "label_addr": "Pristatymo adresas*",
    },
    "es": {
        "label_name": "Nombre y apellidos*",
        "label_phone": "Número de teléfono*",
        "label_addr": "Dirección de envío*",
    },
    "hu": {
        "label_name": "Teljes név*",
        "label_phone": "Telefonszám*",
        "label_addr": "Szállítási cím*",
    },
    "de": {
        "label_name": "Vor- und Nachname*",
        "label_phone": "Telefonnummer*",
        "label_addr": "Lieferadresse*",
    },
    "cs": {
        "label_name": "Jméno a příjmení*",
        "label_phone": "Telefonní číslo*",
        "label_addr": "Doručovací adresa*",
    },
    "sk": {
        "label_name": "Meno a priezvisko*",
        "label_phone": "Telefónne číslo*",
        "label_addr": "Doručovacia adresa*",
    },
    "lv": {
        "label_name": "Vārds un uzvārds*",
        "label_phone": "Tālruņa numurs*",
        "label_addr": "Piegādes adrese*",
    },
    "pl": {
        "label_name": "Imię i nazwisko*",
        "label_phone": "Numer telefonu*",
        "label_addr": "Adres dostawy*",
    },
}

FORM_META = {
    "pt/nuvia": {"lang": "pt", "offer": "1633", "lp": "1653", "key": "b9fc0df73cc24202cc5110946bcae3353db14462"},
    "gr/nuvia": {"lang": "el", "offer": "1842", "lp": "1862", "key": "755513f30dbace7c3b8de93fed11f15e0a02b295"},
    "bg/nuvia": {"lang": "bg", "offer": "1843", "lp": "1863", "key": "90b46c9abc8992a2de7f641e5d95d62df514e9f6"},
    "ro/nuvia": {"lang": "ro", "offer": "1844", "lp": "1864", "key": "06960bd438304079a706dbdc891aa77d61f11f11"},
    "lt/nuvia-v17": {"lang": "lt", "offer": "2136", "lp": "2159", "key": "d88ba1a53ed5ea9b2d841a5dd4797faeda18c246"},
    "es/nuvia": {"lang": "es", "offer": "2297", "lp": "2322", "key": "90fbc58284cdcbad296d4d8f2ab59d29fe9f6ae3"},
    "hu/nuvia-v17": {"lang": "hu", "offer": "2881", "lp": "2914", "key": "573e3bd0d611c1b1d4ad91a80f91b37bc579d1cb"},
    "de/nuvia": {"lang": "de", "offer": "2934", "lp": "2968", "key": "25de2a06d7bfd1009ca4481500800c6cb4ba4738"},
    "cz/nuvia": {"lang": "cs", "offer": "3143", "lp": "3177", "key": "86ebac761342c70ab2796914e465450e4ea5212a"},
    "sk/nuvia-v17": {"lang": "sk", "offer": "3844", "lp": "3884", "key": "71bfc73c42ccaca3aac67b7cf660a82b2cfa2739"},
    "lv/nuvia-v17": {"lang": "lv", "offer": "3845", "lp": "3885", "key": "93f26d9cce8b94c8e0952aaafe1ca02aac63c7ff"},
    "pl/nuvia": {"lang": "pl", "offer": "3141", "lp": "3175", "key": "65daf2495e1b0517cc51a3aa0b57581828423f73"},
}


def _load_copy() -> dict[str, dict]:
    path = Path(__file__).with_name("_nuvia_copy_data.py")
    spec = importlib.util.spec_from_file_location("_nuvia_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


COPY = _load_copy()

LANG_TO_GEO = {
    "pt": "pt",
    "el": "gr",
    "bg": "bg",
    "ro": "ro",
    "lt": "lt",
    "es": "es",
    "hu": "hu",
    "de": "de",
    "cs": "cz",
    "sk": "sk",
    "lv": "lv",
    "pl": "pl",
}


def build_form(rel: str) -> str:
    meta = FORM_META[rel]
    lang = meta["lang"]
    c = COPY[lang]
    fields = tm_order_fields_html(LANG_TO_GEO[lang], indent="")
    thankyou = f"https://gadgetshifthub.com/{rel}/thank-you.html"
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post">
{fields}
<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{meta['offer']}" />
<input name="lp" type="hidden" value="{meta['lp']}" />
<input name="thankyoupage" type="hidden" value="{thankyou}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{meta['key']}" />
<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{c['btn']}</button>
</div>
<p class="form-note">{c['form_note']}</p>
</form>"""


FORMS = {rel: build_form(rel) for rel in FORM_META}

IT_COD_FORM = """<form class="tm-order-form order-form cod-form" novalidate>
          <div class="cod-form__field">
            <label for="name">Nome e cognome*</label>
            <input class="cod-form__input" id="name" type="text" name="name" autocomplete="name" placeholder="Mario Rossi" required minlength="3">
            <span class="cod-form__error">Inserisci nome e cognome valido</span>
          </div>
          <div class="cod-form__field">
            <label for="phone">Numero di telefono*</label>
            <input class="cod-form__input" id="phone" type="tel" name="phone" autocomplete="tel" placeholder="+39 312 345 6789" required>
            <span class="cod-form__error">Inserisci un numero valido</span>
          </div>
          <div class="cod-form__field">
            <label for="address">Indirizzo di consegna*</label>
            <input class="cod-form__input" id="address" type="text" name="address" autocomplete="street-address" placeholder="Via Roma 45, Interno 12, 00100 Roma" required minlength="10">
            <span class="cod-form__error">Inserisci indirizzo completo</span>
          </div>
          <button type="submit" class="cta-btn">CONFERMA ORDINE</button>
          <p class="form-note">🔒 Pagamento alla consegna · Zero anticipo · Reso 30 giorni</p>
        </form>"""
