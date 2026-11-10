#!/usr/bin/env python3
"""Adrice Network form HTML per FORVEX™ offer — matches network embed field order."""
from __future__ import annotations

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"


def thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com/{geo}/forvex-{offer}/thank-you/"


def _esc(msg: str) -> str:
    return msg.replace("'", "\\'")


def _input(
    field_id: str,
    *,
    itype: str,
    name: str,
    autocomplete: str,
    placeholder: str,
    required: bool,
    invalid: str | None = None,
) -> str:
    req = " required" if required else ""
    inv = ""
    if invalid and required:
        e = _esc(invalid)
        inv = f' oninvalid="this.setCustomValidity(\'{e}\')" oninput="this.setCustomValidity(\'\')"'
    return (
        f'<input id="{field_id}" type="{itype}" name="{name}" autocomplete="{autocomplete}" '
        f'placeholder="{placeholder}"{req}{inv}><br>\n'
    )


def _blocked(offer: str, geo: str, fields: str, message: str) -> str:
    return f"""<form class="tm-order-form order-form order-form--blocked" method="post" lang="{geo}" data-forvex-blocked="1" onsubmit="event.preventDefault();var e=this.querySelector('.form-blocked-msg');if(e)e.hidden=false;return false;">
{fields}<input name="offer" type="hidden" value="{offer}" />
<p class="form-blocked-msg" role="alert" hidden style="color:#b91c1c;text-align:center;margin-top:12px;font-weight:600;line-height:1.45;">{message}</p>
<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn" aria-disabled="true">Zamówienie tymczasowo niedostępne</button>
</div>
</form>"""


def _wrap(offer: str, lp: str, key: str, geo: str, fields: str, submit: str) -> str:
    ty = thankyou_url(geo, offer)
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


def _nta(
    geo: str,
    name_l: str,
    name_p: str,
    tel_l: str,
    tel_p: str,
    addr_l: str,
    addr_p: str,
    v_name: str,
    v_tel: str,
    v_addr: str,
) -> str:
    return (
        f"<label for=\"name\">{name_l}</label>\n"
        + _input("name", itype="text", name="name", autocomplete="name", placeholder=name_p, required=True, invalid=v_name)
        + f"<label for=\"tel\">{tel_l}</label>\n"
        + _input("tel", itype="tel", name="tel", autocomplete="tel", placeholder=tel_p, required=True, invalid=v_tel)
        + f"<label for=\"street-address\">{addr_l}</label>\n"
        + _input(
            "street-address",
            itype="text",
            name="street-address",
            autocomplete="street-address",
            placeholder=addr_p,
            required=True,
            invalid=v_addr,
        )
    )


def _nat(
    geo: str,
    name_l: str,
    name_p: str,
    addr_l: str,
    addr_p: str,
    tel_l: str,
    tel_p: str,
    v_name: str,
    v_addr: str,
    v_tel: str,
) -> str:
    return (
        f"<label for=\"name\">{name_l}</label>\n"
        + _input("name", itype="text", name="name", autocomplete="name", placeholder=name_p, required=True, invalid=v_name)
        + f"<label for=\"street-address\">{addr_l}</label>\n"
        + _input(
            "street-address",
            itype="text",
            name="street-address",
            autocomplete="street-address",
            placeholder=addr_p,
            required=True,
            invalid=v_addr,
        )
        + f"<label for=\"tel\">{tel_l}</label>\n"
        + _input("tel", itype="tel", name="tel", autocomplete="tel", placeholder=tel_p, required=True, invalid=v_tel)
    )


def _extended_postal(
    *,
    name_l: str,
    name_p: str,
    tel_l: str,
    tel_p: str,
    addr_l: str,
    addr_p: str,
    zip_l: str,
    zip_p: str,
    city_l: str,
    city_p: str,
    v_name: str,
    v_tel: str,
    v_addr: str,
    v_zip: str,
) -> str:
    return (
        f"<label for=\"name\">{name_l}</label>\n"
        + _input("name", itype="text", name="name", autocomplete="name", placeholder=name_p, required=True, invalid=v_name)
        + f"<label for=\"tel\">{tel_l}</label>\n"
        + _input("tel", itype="tel", name="tel", autocomplete="tel", placeholder=tel_p, required=True, invalid=v_tel)
        + f"<label for=\"street-address\">{addr_l}</label>\n"
        + _input(
            "street-address",
            itype="text",
            name="street-address",
            autocomplete="street-address",
            placeholder=addr_p,
            required=True,
            invalid=v_addr,
        )
        + f"<label for=\"postal-code\">{zip_l}</label>\n"
        + _input(
            "postal-code",
            itype="text",
            name="postal-code",
            autocomplete="postal-code",
            placeholder=zip_p,
            required=True,
            invalid=v_zip,
        )
        + f"<label for=\"address-level2\">{city_l}</label>\n"
        + _input(
            "address-level2",
            itype="text",
            name="address-level2",
            autocomplete="address-level2",
            placeholder=city_p,
            required=False,
        )
    )


FORMS: dict[str, str] = {
    "752": _wrap(
        "752",
        "766",
        "07c17d85db7b1d3358520c6e6920b2aa2b83a597",
        "lt",
        _nta(
            "lt",
            "Vardas ir pavardė:*",
            "Vardas ir pavardė:",
            "Telefonas:*",
            "Telefonas:",
            "Adresas:*",
            "Adresas:",
            "Įveskite vardą ir pavardę.",
            "Įveskite telefono numerį.",
            "Įveskite pilną adresą.",
        ),
        "Pateikite užsakymą",
    ),
    "1013": _wrap(
        "1013",
        "1032",
        "6c673a161fa10b83e5ae6925bcb3404f09d79573",
        "es",
        _nta(
            "es",
            "Nombre completo*",
            "Nombre completo",
            "Número de teléfono*",
            "Número de teléfono",
            "Dirección*",
            "Dirección",
            "Introduzca su nombre completo.",
            "Introduzca su número de teléfono.",
            "Introduzca su dirección completa.",
        ),
        "Envía tu pedido",
    ),
    "1014": _wrap(
        "1014",
        "1033",
        "a031afffb6bc659e4129fe5f3ac5099004e683cc",
        "pt",
        _nta(
            "pt",
            "Nome completo*",
            "Nome completo",
            "Telefone*",
            "Telefone",
            "Morada*",
            "Morada",
            "Indique o nome completo.",
            "Indique o telefone.",
            "Indique a morada completa.",
        ),
        "Encomendar agora",
    ),
    "1429": _blocked(
        "1429",
        "pl",
        _nta(
            "pl",
            "Imię Nazwisko*",
            "Imię Nazwisko",
            "Telefon*",
            "Telefon",
            "Adres*",
            "Adres",
            "Podaj imię i nazwisko.",
            "Podaj numer telefonu.",
            "Podaj pełny adres.",
        ),
        "Zamówienia online dla tej oferty są chwilowo wyłączone (brak konfiguracji integracji). "
        "Napisz na info@shoptrendcrest.com — oddzwonimy.",
    ),
    "1797": _wrap(
        "1797",
        "1817",
        "b3fcefdf00da3f8d741d10735ec9f8b47bb9cbd5",
        "pl",
        _nta(
            "pl",
            "Imię Nazwisko*",
            "Imię Nazwisko",
            "Telefon*",
            "Telefon",
            "Adres*",
            "Adres",
            "Podaj imię i nazwisko.",
            "Podaj numer telefonu.",
            "Podaj pełny adres.",
        ),
        "zamów teraz",
    ),
    "1945": _wrap(
        "1945",
        "1965",
        "d61d6e3edf264d67924aec477ca2cdad1fc639a2",
        "cz",
        _nta(
            "cz",
            "Jméno Příjmení*",
            "Jméno Příjmení",
            "Telefon*",
            "Telefon",
            "Adresa*",
            "Adresa",
            "Vyplňte jméno a příjmení.",
            "Vyplňte telefon.",
            "Vyplňte celou adresu.",
        ),
        "Objednat nyní",
    ),
    "3225": _wrap(
        "3225",
        "3259",
        "3224663b037bc74fa8f57f6fd66a86e0128e60e4",
        "ro",
        _nta(
            "ro",
            "nume și prenume*",
            "nume și prenume",
            "Telefon*",
            "Telefon",
            "Adresa*",
            "Adresa",
            "Introduceți numele complet.",
            "Introduceți numărul de telefon.",
            "Introduceți adresa completă.",
        ),
        "Trimite comanda",
    ),
    "3228": _wrap(
        "3228",
        "3262",
        "8a57fd45bf5bccc4bbbe544ca1321a2cd97c25b6",
        "sk",
        _nta(
            "sk",
            "Meno a priezvisko*",
            "Meno a priezvisko",
            "Telefón*",
            "Telefón",
            "Adresa*",
            "Adresa",
            "Vyplňte meno a priezvisko.",
            "Vyplňte telefón.",
            "Vyplňte celú adresu.",
        ),
        "Objednať teraz",
    ),
    "3229": _wrap(
        "3229",
        "3263",
        "e4166394767d0c6ecac532551f1e09ac66733a5f",
        "si",
        _nta(
            "si",
            "Ime in priimek*",
            "Ime in priimek",
            "Telefon*",
            "Telefon",
            "Naslov*",
            "Naslov",
            "Vnesite ime in priimek.",
            "Vnesite telefonsko številko.",
            "Vnesite celoten naslov.",
        ),
        "Pošlji naročilo",
    ),
    "3230": _wrap(
        "3230",
        "3264",
        "35afd807932cc362941937031a117f28aa5f524c",
        "hr",
        _nta(
            "hr",
            "ime i prezime*",
            "ime i prezime",
            "mobitel*",
            "mobitel",
            "adresa*",
            "adresa",
            "Unesite ime i prezime.",
            "Unesite broj mobitela.",
            "Unesite punu adresu.",
        ),
        "Pošalji narudžbu",
    ),
    "3232": _wrap(
        "3232",
        "3266",
        "1a637d62528de889c76131f5f4a1b44b2bd4330f",
        "hu",
        _nta(
            "hu",
            "Teljes név*",
            "Teljes név",
            "Telefonszám*",
            "Telefonszám",
            "Teljes cím*",
            "Teljes cím",
            "Adja meg a teljes nevét.",
            "Adja meg a telefonszámát.",
            "Adja meg a teljes címet.",
        ),
        "Megrendelés",
    ),
    "3248": _wrap(
        "3248",
        "3282",
        "789e3e387d6ff58740f6567c26131bc7c9a1ba45",
        "de",
        _nta(
            "de",
            "Vorname Nachname*",
            "Vorname Nachname",
            "Telefon*",
            "Telefon",
            "Anschrift*",
            "Anschrift",
            "Bitte geben Sie Ihren Namen ein.",
            "Bitte geben Sie Ihre Telefonnummer ein.",
            "Bitte geben Sie Ihre vollständige Anschrift ein.",
        ),
        "Jetzt bestellen",
    ),
    "3518": _wrap(
        "3518",
        "3555",
        "5bc8d9d901067b7310a738d22d80d7e4108f3683",
        "lv",
        _nta(
            "lv",
            "Vārds Uzvārds*",
            "Vārds Uzvārds",
            "Tālrunis*",
            "Tālrunis",
            "Adrese*",
            "Adrese",
            "Ievadiet vārdu un uzvārdu.",
            "Ievadiet tālruņa numuru.",
            "Ievadiet pilnu adresi.",
        ),
        "Pasūtiet tagad",
    ),
    "4363": _wrap(
        "4363",
        "4403",
        "6a0ae63f0e0db59e91b473bb9cab12e6a8e503bc",
        "it",
        _nta(
            "it",
            "Nome e cognome*",
            "Nome e cognome",
            "Numero di telefono*",
            "Numero di telefono",
            "Indirizzo completo*",
            "Indirizzo completo",
            "Inserisci nome e cognome.",
            "Inserisci il numero di telefono.",
            "Inserisci indirizzo completo.",
        ),
        "ORDINA ORA",
    ),
}
