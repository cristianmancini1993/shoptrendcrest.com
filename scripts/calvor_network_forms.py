#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calvor™ campaign Adrice forms — embed labels/keys + localized placeholders."""

from __future__ import annotations

from _warmio_form_ui import OFFER_GEO, OFFER_LP_KEY
from calvor_campaign_prices import offer_folder as calvor_offer_folder

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/srey7bhi9b1qapk46soc1q9jpb6iwexk"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

# Labels = buyer embed; placeholders = localized examples (names, phones, addresses).
FORM_UI: dict[str, dict[str, str]] = {
    "3990": {
        "name_l": "Nome e cognome*",
        "name_p": "Mario Rossi",
        "tel_l": "Telefono*",
        "tel_p": "+39 333 123 4567",
        "addr_l": "Indirizzo completo*",
        "addr_p": "Via Roma 15, 20121 Milano",
        "submit": "PAGA ALLA CONSEGNA",
        "layout": "nta",
    },
    "1851": {
        "name_l": "Ime i prezime*",
        "name_p": "Ivan Horvat",
        "tel_l": "Telefon*",
        "tel_p": "+385 91 123 4567",
        "addr_l": "Puna adresa*",
        "addr_p": "Ilica 10, 10000 Zagreb",
        "submit": "NARUČITE ODMAH",
        "layout": "nta",
    },
    "765": {
        "name_l": "Ime in priimek*",
        "name_p": "Luka Novak",
        "tel_l": "Telefon*",
        "tel_p": "+386 41 123 456",
        "addr_l": "Celoten naslov*",
        "addr_p": "Slovenska cesta 10, 1000 Ljubljana",
        "submit": "NAROČI ZDAJ",
        "layout": "nta",
    },
    "763": {
        "name_l": "Numele Complet*",
        "name_p": "Ion Popescu",
        "tel_l": "Telefon*",
        "tel_p": "+40 721 234 567",
        "addr_l": "Adresa*",
        "addr_p": "Str. Victoriei 10, 010096 București",
        "postal_l": "Cod poștal*",
        "postal_p": "010096",
        "city_l": "Oraș",
        "city_p": "București",
        "submit": "Trimite comanda",
        "layout": "ro",
    },
    "762": {
        "name_l": "Név és Vezetéknév*",
        "name_p": "Nagy Péter",
        "tel_l": "Telefonszám*",
        "tel_p": "+36 30 123 4567",
        "addr_l": "Utca és Házszám, (lakás, emelet, ajtó)*",
        "addr_p": "Andrássy út 10., 1061 Budapest",
        "city_l": "Város",
        "city_p": "Budapest",
        "postal_l": "Irányítószám*",
        "postal_p": "1061",
        "submit": "Küldje el a rendelést",
        "layout": "hu",
    },
    "1673": {
        "name_l": "Nome próprio Apelido*",
        "name_p": "Ana Silva",
        "tel_l": "Telefone de contacto*",
        "tel_p": "+351 912 345 678",
        "addr_l": "Endereço*",
        "addr_p": "Rua da Liberdade 45, 1250-096 Lisboa",
        "submit": "Encomendar agora",
        "layout": "atn",
    },
    "2283": {
        "name_l": "Nombre Apellido*",
        "name_p": "María García López",
        "tel_l": "Teléfono*",
        "tel_p": "+34 612 34 56 78",
        "addr_l": "Dirección*",
        "addr_p": "Calle Mayor 12, 28013 Madrid",
        "submit": "Haz tu pedido",
        "layout": "atn",
    },
    "2285": {
        "name_l": "Vorname Nachname*",
        "name_p": "Thomas Müller",
        "tel_l": "Telefon*",
        "tel_p": "+49 151 23456789",
        "addr_l": "Adresse*",
        "addr_p": "Hauptstraße 10, 10115 Berlin",
        "submit": "Jetzt bestellen",
        "layout": "atn",
    },
    "2287": {
        "name_l": "Imię Nazwisko*",
        "name_p": "Jan Kowalski",
        "tel_l": "Telefon*",
        "tel_p": "+48 512 345 678",
        "addr_l": "Adres*",
        "addr_p": "ul. Marszałkowska 10/5, 00-590 Warszawa",
        "submit": "Zamów teraz",
        "layout": "atn",
    },
    "2289": {
        "name_l": "Jméno Příjmení*",
        "name_p": "Jan Novák",
        "tel_l": "Telefon*",
        "tel_p": "+420 777 123 456",
        "addr_l": "Adresa*",
        "addr_p": "Václavské náměstí 1, 110 00 Praha",
        "submit": "Objednat nyní",
        "layout": "atn",
    },
    "3426": {
        "name_l": "Vārds Uzvārds*",
        "name_p": "Jānis Bērziņš",
        "tel_l": "Tālrunis*",
        "tel_p": "+371 21 234 567",
        "addr_l": "Adrese*",
        "addr_p": "Brīvības iela 10, LV-1010 Rīga",
        "submit": "Pasūtiet tagad",
        "layout": "atn",
    },
    "4067": {
        "name_l": "Meno Priezvisko*",
        "name_p": "Peter Horváth",
        "tel_l": "Telefón*",
        "tel_p": "+421 912 345 678",
        "addr_l": "Adresa*",
        "addr_p": "Hlavná 15, 811 01 Bratislava",
        "submit": "Objednajte si teraz ",
        "layout": "atn",
    },
    "4276": {
        "name_l": "Vardas Pavardė*",
        "name_p": "Jonas Petraitis",
        "tel_l": "Telefonas*",
        "tel_p": "+370 612 34567",
        "addr_l": "Adresas*",
        "addr_p": "Gedimino pr. 10-5, 01103 Vilnius",
        "submit": "Užsakyti dabar",
        "layout": "atn",
    },
}


def thankyou_url(geo: str, offer: str) -> str:
    folder = calvor_offer_folder(offer)
    return f"https://shoptrendcrest.com/{geo}/{folder}/thank-you/"


def _inp(
    fid: str,
    label: str,
    placeholder: str,
    *,
    required: bool = True,
    itype: str = "text",
) -> str:
    req = " required" if required else ""
    ac = {
        "name": "name",
        "tel": "tel",
        "street-address": "street-address",
        "postal-code": "postal-code",
        "address-level2": "address-level2",
    }.get(fid, fid)
    return (
        f'<label for="{fid}">{label}</label>\n'
        f'<input id="{fid}" type="{itype}" name="{fid}" autocomplete="{ac}" '
        f'placeholder="{placeholder}"{req}><br>\n'
    )


def _body(offer: str) -> str:
    ui = FORM_UI[offer]
    layout = ui["layout"]
    parts: list[str] = []
    if layout == "nta":
        parts.extend(
            [
                _inp("name", ui["name_l"], ui["name_p"]),
                _inp("tel", ui["tel_l"], ui["tel_p"], itype="tel"),
                _inp("street-address", ui["addr_l"], ui["addr_p"]),
            ]
        )
    elif layout == "atn":
        parts.extend(
            [
                _inp("name", ui["name_l"], ui["name_p"]),
                _inp("street-address", ui["addr_l"], ui["addr_p"]),
                _inp("tel", ui["tel_l"], ui["tel_p"], itype="tel"),
            ]
        )
    elif layout == "hu":
        parts.extend(
            [
                _inp("name", ui["name_l"], ui["name_p"]),
                _inp("tel", ui["tel_l"], ui["tel_p"], itype="tel"),
                _inp("street-address", ui["addr_l"], ui["addr_p"]),
                _inp("address-level2", ui["city_l"], ui["city_p"], required=False),
                _inp("postal-code", ui["postal_l"], ui["postal_p"]),
            ]
        )
    elif layout == "ro":
        parts.extend(
            [
                _inp("name", ui["name_l"], ui["name_p"]),
                _inp("tel", ui["tel_l"], ui["tel_p"], itype="tel"),
                _inp("street-address", ui["addr_l"], ui["addr_p"]),
                _inp("postal-code", ui["postal_l"], ui["postal_p"]),
                _inp("address-level2", ui["city_l"], ui["city_p"], required=False),
            ]
        )
    return "".join(parts)


def _form(offer: str) -> str:
    geo = OFFER_GEO[offer]
    lp, key = OFFER_LP_KEY[offer]
    ty = thankyou_url(geo, offer)
    ui = FORM_UI[offer]
    return (
        f'<form class="tm-order-form order-form" action="{ACTION}" method="post">\n'
        f"{_body(offer)}"
        f'<input name="uid" type="hidden" value="{UID}" />\n'
        f'<input name="offer" type="hidden" value="{offer}" />\n'
        f'<input name="lp" type="hidden" value="{lp}" />\n'
        f'<input name="thankyoupage" type="hidden" value="{ty}"/>\n'
        f'<input name="webhook" type="hidden" value="{WEBHOOK}"/>\n'
        f'<input name="_key" type="hidden" value="{key}" />\n'
        f"\n"
        f'<div style="margin-top: 10px; text-align: center">\n'
        f'    <button name="submit" type="submit" class="cta-btn">{ui["submit"]}</button>\n'
        f"</div>\n"
        f'<script src="{SCRIPT}" async></script>\n'
        f"</form>"
    )


FORMS: dict[str, str] = {oid: _form(oid) for oid in FORM_UI}