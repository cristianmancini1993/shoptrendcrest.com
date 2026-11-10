#!/usr/bin/env python3
"""Adrice Network form HTML per LEAFORA geo offers."""
from __future__ import annotations

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"


def thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com/{geo}/leafora-{offer}/thank-you/"


def _fields_block(
    *,
    name_l: str,
    name_p: str,
    addr_l: str,
    addr_p: str,
    tel_l: str,
    tel_p: str,
    order: str,
) -> str:
    name = (
        f'<label for="name">{name_l}</label>\n'
        f'<input id="name" type="text" name="name" autocomplete="name" '
        f'placeholder="{name_p}" required><br>\n'
    )
    addr = (
        f'<label for="street-address">{addr_l}</label>\n'
        f'<input id="street-address" type="text" name="street-address" '
        f'autocomplete="street-address" placeholder="{addr_p}" required><br>\n'
    )
    tel = (
        f'<label for="tel">{tel_l}</label>\n'
        f'<input id="tel" type="tel" name="tel" autocomplete="tel" '
        f'placeholder="{tel_p}" required><br>\n'
    )
    if order == "name_tel_addr":
        return name + tel + addr
    return name + addr + tel


def _form(
    *,
    name_l: str,
    name_p: str,
    addr_l: str,
    addr_p: str,
    tel_l: str,
    tel_p: str,
    order: str,
    offer: str,
    geo: str,
    lp: str,
    key: str,
    submit: str,
) -> str:
    thankyou = thankyou_url(geo, offer)
    fields = _fields_block(
        name_l=name_l,
        name_p=name_p,
        addr_l=addr_l,
        addr_p=addr_p,
        tel_l=tel_l,
        tel_p=tel_p,
        order=order,
    )
    return f"""<form class="tm-order-form" action="{ACTION}" method="post">
{fields}<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{thankyou}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{submit}</button>
</div>
<script src="{SCRIPT}" async></script>
</form>"""


FORMS: dict[str, str] = {
    "1745": _form(
        name_l="Imię Nazwisko*",
        name_p="Imię Nazwisko",
        addr_l="Adres*",
        addr_p="Adres",
        tel_l="Telefon*",
        tel_p="Telefon",
        order="name_addr_tel",
        offer="1745",
        geo="pl",
        lp="1765",
        key="f793753667ea4f2c851af982f25006881d5e94dd",
        submit="Zamów teraz",
    ),
    "1746": _form(
        name_l="Keresztnév Vezetéknév*",
        name_p="Keresztnév Vezetéknév",
        addr_l="Cím*",
        addr_p="Cím",
        tel_l="Telefon*",
        tel_p="Telefon",
        order="name_addr_tel",
        offer="1746",
        geo="hu",
        lp="1766",
        key="1d369e2fd85efae0a0bc720c2b10163c7bbacb47",
        submit="Rendeljen most",
    ),
    "3188": _form(
        name_l="Vorname Nachname*",
        name_p="Vorname Nachname",
        addr_l="Anschrift*",
        addr_p="Anschrift",
        tel_l="Telefon*",
        tel_p="Telefon",
        order="name_addr_tel",
        offer="3188",
        geo="de",
        lp="3222",
        key="5d8cbc83f1bab338255aaa5649306bdd1b223a18",
        submit="Jetzt bestellen",
    ),
    "3189": _form(
        name_l="Vardas Pavardė*",
        name_p="Vardas Pavardė",
        addr_l="Adresas*",
        addr_p="Adresas",
        tel_l="Telefonas*",
        tel_p="Telefonas",
        order="name_addr_tel",
        offer="3189",
        geo="lt",
        lp="3223",
        key="43be7d1bda6b12f7e2a9d8095d77846271d5a7c0",
        submit="Užsisakykite dabar",
    ),
    "3190": _form(
        name_l="Jméno Příjmení*",
        name_p="Jméno Příjmení",
        addr_l="Adresa*",
        addr_p="Adresa",
        tel_l="Telefon*",
        tel_p="Telefon",
        order="name_addr_tel",
        offer="3190",
        geo="cz",
        lp="3224",
        key="8fc959e5bb8d577da9c11d8eb1598f5b2e497cdd",
        submit="Objednat nyní",
    ),
    "3191": _form(
        name_l="Nome Sobrenome*",
        name_p="Nome Sobrenome",
        addr_l="Endereço*",
        addr_p="Endereço",
        tel_l="Telefone de contacto*",
        tel_p="Telefone de contacto",
        order="name_addr_tel",
        offer="3191",
        geo="pt",
        lp="3225",
        key="d400427067d6fc330c3618666ab72aeace9c58fe",
        submit="Encomendar agora",
    ),
    "3192": _form(
        name_l="Nombre Apellido*",
        name_p="Nombre Apellido",
        addr_l="Dirección*",
        addr_p="Dirección",
        tel_l="Teléfono*",
        tel_p="Teléfono",
        order="name_addr_tel",
        offer="3192",
        geo="es",
        lp="3226",
        key="40c4eaab51ad328d8870ec0569feddb996087a94",
        submit="Haz tu pedido",
    ),
    "4065": _form(
        name_l="Meno Priezvisko*",
        name_p="Meno Priezvisko",
        addr_l="Adresa*",
        addr_p="Adresa",
        tel_l="Telefón*",
        tel_p="Telefón",
        order="name_addr_tel",
        offer="4065",
        geo="sk",
        lp="4105",
        key="34f30d7253380f4f29ca10a0b519d28c3377069d",
        submit="Objednajte si teraz ",
    ),
    "1650": _form(
        name_l="Nome e cognome*",
        name_p="Nome e cognome",
        addr_l="Indirizzo*",
        addr_p="Indirizzo",
        tel_l="Telefono*",
        tel_p="Telefono",
        order="name_tel_addr",
        offer="1650",
        geo="it",
        lp="1670",
        key="ad8bc8ca0d740e0056a82535bed04e244380b148",
        submit="ORDINA ADESSO",
    ),
    "2657": _form(
        name_l="Nume și Prenume*",
        name_p="Nume și Prenume",
        addr_l="Adresa completă*",
        addr_p="Adresa completă",
        tel_l="Telefon*",
        tel_p="Telefon",
        order="name_tel_addr",
        offer="2657",
        geo="ro",
        lp="2684",
        key="3371905ec316258f3fad6fb7f07d1e5fd6d434ca",
        submit="COMANDA ACUM",
    ),
}
