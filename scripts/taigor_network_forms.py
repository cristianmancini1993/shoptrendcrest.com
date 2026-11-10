#!/usr/bin/env python3
"""Adrice Network form HTML per TAIGOR™ offer — 3 fields: name → tel → full address."""
from __future__ import annotations

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"


def thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com/{geo}/taigor-{offer}/thank-you/"


# (name, tel, address) — browser validation messages
_VALIDATION: dict[str, tuple[str, str, str]] = {
    "lt": (
        "Įveskite vardą ir pavardę.",
        "Įveskite telefono numerį.",
        "Įveskite pilną adresą.",
    ),
    "es": (
        "Introduzca su nombre completo.",
        "Introduzca su número de teléfono.",
        "Introduzca su dirección completa.",
    ),
    "pt": (
        "Indique o nome completo.",
        "Indique o telefone.",
        "Indique a morada completa.",
    ),
    "pl": (
        "Podaj imię i nazwisko.",
        "Podaj numer telefonu.",
        "Podaj pełny adres.",
    ),
    "cz": (
        "Vyplňte jméno a příjmení.",
        "Vyplňte telefon.",
        "Vyplňte celou adresu.",
    ),
    "ro": (
        "Introduceți numele complet.",
        "Introduceți numărul de telefon.",
        "Introduceți adresa completă.",
    ),
    "sk": (
        "Vyplňte meno a priezvisko.",
        "Vyplňte telefón.",
        "Vyplňte celú adresu.",
    ),
    "si": (
        "Vnesite ime in priimek.",
        "Vnesite telefonsko številko.",
        "Vnesite celoten naslov.",
    ),
    "hr": (
        "Unesite ime i prezime.",
        "Unesite broj mobitela.",
        "Unesite punu adresu.",
    ),
    "hu": (
        "Adja meg a teljes nevét.",
        "Adja meg a telefonszámát.",
        "Adja meg a teljes címet.",
    ),
    "de": (
        "Bitte geben Sie Ihren Namen ein.",
        "Bitte geben Sie Ihre Telefonnummer ein.",
        "Bitte geben Sie Ihre vollständige Anschrift ein.",
    ),
    "lv": (
        "Ievadiet vārdu un uzvārdu.",
        "Ievadiet tālruņa numuru.",
        "Ievadiet pilnu adresi.",
    ),
    "it": (
        "Inserisci nome e cognome.",
        "Inserisci il numero di telefono.",
        "Inserisci indirizzo completo.",
    ),
}


def _invalid_msg(msg: str) -> str:
    return msg.replace("'", "\\'")


def _fields(
    *,
    geo: str,
    name_l: str,
    name_p: str,
    tel_l: str,
    tel_p: str,
    addr_l: str,
    addr_p: str,
) -> str:
    vn, vt, va = _VALIDATION[geo]
    vn, vt, va = _invalid_msg(vn), _invalid_msg(vt), _invalid_msg(va)
    clear = "this.setCustomValidity('')"
    return (
        f'<label for="name">{name_l}</label>\n'
        f'<input id="name" type="text" name="name" autocomplete="name" '
        f'placeholder="{name_p}" required '
        f"oninvalid=\"this.setCustomValidity('{vn}')\" oninput=\"{clear}\"><br>\n"
        f'<label for="tel">{tel_l}</label>\n'
        f'<input id="tel" type="tel" name="tel" autocomplete="tel" '
        f'placeholder="{tel_p}" required '
        f"oninvalid=\"this.setCustomValidity('{vt}')\" oninput=\"{clear}\"><br>\n"
        f'<label for="street-address">{addr_l}</label>\n'
        f'<input id="street-address" type="text" name="street-address" '
        f'autocomplete="street-address" placeholder="{addr_p}" required '
        f"oninvalid=\"this.setCustomValidity('{va}')\" oninput=\"{clear}\"><br>\n"
    )


def _form(
    *,
    offer: str,
    geo: str,
    lp: str,
    key: str,
    submit: str,
    name_l: str,
    name_p: str,
    tel_l: str,
    tel_p: str,
    addr_l: str,
    addr_p: str,
) -> str:
    ty = thankyou_url(geo, offer)
    fields = _fields(
        geo=geo,
        name_l=name_l,
        name_p=name_p,
        tel_l=tel_l,
        tel_p=tel_p,
        addr_l=addr_l,
        addr_p=addr_p,
    )
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post" lang="{geo}">
{fields}<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn">{submit}</button>
</div>
<script src="{SCRIPT}" async></script>
</form>"""


FORMS: dict[str, str] = {
    "752": _form(
        offer="752",
        geo="lt",
        lp="766",
        key="07c17d85db7b1d3358520c6e6920b2aa2b83a597",
        submit="Pateikite užsakymą",
        name_l="Vardas ir pavardė*",
        name_p="Jonas Petraitis",
        tel_l="Telefonas*",
        tel_p="+370 612 34567",
        addr_l="Adresas*",
        addr_p="Gedimino pr. 10-5, 01103 Vilnius",
    ),
    "1013": _form(
        offer="1013",
        geo="es",
        lp="1032",
        key="6c673a161fa10b83e5ae6925bcb3404f09d79573",
        submit="Envía tu pedido",
        name_l="Nombre completo*",
        name_p="María García López",
        tel_l="Número de teléfono*",
        tel_p="+34 612 34 56 78",
        addr_l="Dirección completa*",
        addr_p="Calle Mayor 12, 28013 Madrid",
    ),
    "1014": _form(
        offer="1014",
        geo="pt",
        lp="1033",
        key="a031afffb6bc659e4129fe5f3ac5099004e683cc",
        submit="Enviar o pedido",
        name_l="Nome completo*",
        name_p="Ana Silva",
        tel_l="Telefone*",
        tel_p="+351 912 345 678",
        addr_l="Morada*",
        addr_p="Rua da Liberdade 45, 1250-096 Lisboa",
    ),
    "1797": _form(
        offer="1797",
        geo="pl",
        lp="1817",
        key="b3fcefdf00da3f8d741d10735ec9f8b47bb9cbd5",
        submit="Zamów teraz",
        name_l="Imię i nazwisko*",
        name_p="Jan Kowalski",
        tel_l="Telefon*",
        tel_p="+48 512 345 678",
        addr_l="Adres*",
        addr_p="ul. Marszałkowska 10/5, 00-590 Warszawa",
    ),
    "1945": _form(
        offer="1945",
        geo="cz",
        lp="1965",
        key="d61d6e3edf264d67924aec477ca2cdad1fc639a2",
        submit="Objednat nyní",
        name_l="Jméno a příjmení*",
        name_p="Jan Novák",
        tel_l="Telefon*",
        tel_p="+420 601 123 456",
        addr_l="Adresa*",
        addr_p="Václavské nám. 1, 110 00 Praha",
    ),
    "3225": _form(
        offer="3225",
        geo="ro",
        lp="3259",
        key="3224663b037bc74fa8f57f6fd66a86e0128e60e4",
        submit="Comandă cu plată la livrare",
        name_l="Nume și prenume*",
        name_p="Ion Popescu",
        tel_l="Telefon*",
        tel_p="+40 721 234 567",
        addr_l="Adresă completă*",
        addr_p="Str. Victoriei 10, 010096 București",
    ),
    "3228": _form(
        offer="3228",
        geo="sk",
        lp="3262",
        key="8a57fd45bf5bccc4bbbe544ca1321a2cd97c25b6",
        submit="Objednať teraz",
        name_l="Meno a priezvisko*",
        name_p="Peter Horváth",
        tel_l="Telefón*",
        tel_p="+421 912 345 678",
        addr_l="Adresa*",
        addr_p="Hlavná 15, 811 01 Bratislava",
    ),
    "3229": _form(
        offer="3229",
        geo="si",
        lp="3263",
        key="e4166394767d0c6ecac532551f1e09ac66733a5f",
        submit="Pošlji naročilo",
        name_l="Ime in priimek*",
        name_p="Luka Novak",
        tel_l="Telefonska številka*",
        tel_p="+386 41 123 456",
        addr_l="Naslov*",
        addr_p="Slovenska cesta 10, 1000 Ljubljana",
    ),
    "3230": _form(
        offer="3230",
        geo="hr",
        lp="3264",
        key="35afd807932cc362941937031a117f28aa5f524c",
        submit="Naruči s plaćanjem pouzećem",
        name_l="Ime i prezime*",
        name_p="Ivan Horvat",
        tel_l="Broj mobitela*",
        tel_p="+385 91 123 4567",
        addr_l="Adresa*",
        addr_p="Ilica 10, 10000 Zagreb",
    ),
    "3232": _form(
        offer="3232",
        geo="hu",
        lp="3266",
        key="1a637d62528de889c76131f5f4a1b44b2bd4330f",
        submit="Megrendelés",
        name_l="Teljes név*",
        name_p="Nagy Péter",
        tel_l="Telefonszám*",
        tel_p="+36 30 123 4567",
        addr_l="Teljes cím*",
        addr_p="Andrássy út 10., 1061 Budapest",
    ),
    "3248": _form(
        offer="3248",
        geo="de",
        lp="3282",
        key="789e3e387d6ff58740f6567c26131bc7c9a1ba45",
        submit="Jetzt bestellen",
        name_l="Vor- und Nachname*",
        name_p="Thomas Müller",
        tel_l="Telefon*",
        tel_p="+49 151 23456789",
        addr_l="Vollständige Anschrift*",
        addr_p="Hauptstraße 10, 10115 Berlin",
    ),
    "3518": _form(
        offer="3518",
        geo="lv",
        lp="3555",
        key="5bc8d9d901067b7310a738d22d80d7e4108f3683",
        submit="Pasūtiet tagad",
        name_l="Vārds un uzvārds*",
        name_p="Jānis Bērziņš",
        tel_l="Tālrunis*",
        tel_p="+371 21 234 567",
        addr_l="Pilna adrese*",
        addr_p="Brīvības iela 10, LV-1010 Rīga",
    ),
    "4363": _form(
        offer="4363",
        geo="it",
        lp="4403",
        key="6a0ae63f0e0db59e91b473bb9cab12e6a8e503bc",
        submit="ORDINA ORA",
        name_l="Nome e cognome*",
        name_p="Mario Rossi",
        tel_l="Numero di telefono*",
        tel_p="+39 312 345 6789",
        addr_l="Indirizzo completo*",
        addr_p="Via Roma 45, 00100 Roma",
    ),
}
