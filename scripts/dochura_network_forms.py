#!/usr/bin/env python3
"""Adrice Network form HTML per Dochura geo offer."""
from __future__ import annotations

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"


def _form(
    *,
    labels: tuple[str, str, str],
    placeholders: tuple[str, str, str],
    form_note: str,
    offer: str,
    lp: str,
    thankyou: str,
    key: str,
    submit: str,
) -> str:
    name_l, addr_l, tel_l = labels
    name_p, addr_p, tel_p = placeholders
    return f"""        <form class="tm-order-form" action="{ACTION}" method="post">
        <label for="name">{name_l}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{name_p}" required><br>
        <label for="street-address">{addr_l}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{addr_p}" required><br>
        <label for="tel">{tel_l}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{tel_p}" required><br>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="{thankyou}"/>
        <input name="webhook" type="hidden" value="{WEBHOOK}"/>
        <input name="_key" type="hidden" value="{key}" />

        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{submit}</button>
        </div>
        <p class="form-note">{form_note}</p>
        <script src="{SCRIPT}" async></script>
      </form>"""


FORMS: dict[str, str] = {
    "1912": _form(
        labels=("Vorname Nachname*", "Anschrift*", "Telefon*"),
        placeholders=("Vorname Nachname", "Anschrift", "Telefon"),
        form_note="🔒 Keine Vorauszahlung · Keine Karte · Sie zahlen erst bei Erhalt",
        offer="1912",
        lp="1932",
        thankyou="https://shoptrendcrest.com/de/dochura/thank-you.html",
        key="5e68d2a8a6ca4ca1f511e39a64e1e943858ee329",
        submit="Jetzt bestellen",
    ),
    "1915": _form(
        labels=("Keresztnév Vezetéknév*", "Cím*", "Telefon*"),
        placeholders=("Keresztnév Vezetéknév", "Cím", "Telefon"),
        form_note="🔒 Nincs előleg · Nincs kártya · Csak átvételkor fizet",
        offer="1915",
        lp="1935",
        thankyou="https://shoptrendcrest.com/hu/dochura/thank-you.html",
        key="ee927936c4405d2e0b75f5166861a97ddfdf9ce8",
        submit="Rendelje meg most",
    ),
    "3163": _form(
        labels=("Nombre Apellido*", "Dirección*", "Teléfono*"),
        placeholders=("Nombre Apellido", "Dirección", "Teléfono"),
        form_note="🔒 Cero anticipo · Cero tarjeta · Pagas solo cuando lo recibes",
        offer="3163",
        lp="3197",
        thankyou="https://shoptrendcrest.com/es/dochura/thank-you.html",
        key="58da2c2b87633ee4430cd5f3342f5fc7935ccfd7",
        submit="Haz tu pedido",
    ),
    "3164": _form(
        labels=("Nome Sobrenome*", "Endereço*", "Telefone de contacto*"),
        placeholders=("Nome Sobrenome", "Endereço", "Telefone de contacto"),
        form_note="🔒 Zero adiantamento · Zero cartão · Paga só quando recebe",
        offer="3164",
        lp="3198",
        thankyou="https://shoptrendcrest.com/pt/dochura/thank-you.html",
        key="0e0cc21c319903e9ea710cd4600b4e509202ed4d",
        submit="Encomendar agora",
    ),
    "3167": _form(
        labels=("Imię Nazwisko*", "Adres*", "Telefon*"),
        placeholders=("Imię Nazwisko", "Adres", "Telefon"),
        form_note="🔒 Zero zaliczki · Bez karty · Płacisz dopiero po odbiorze",
        offer="3167",
        lp="3201",
        thankyou="https://shoptrendcrest.com/pl/dochura/thank-you.html",
        key="dfef13a537b06b7ae5e8d50a97bd05e8499f7b67",
        submit="Zamów teraz",
    ),
    "3169": _form(
        labels=("Jméno Příjmení*", "Adresa*", "Telefon*"),
        placeholders=("Jméno Příjmení", "Adresa", "Telefon"),
        form_note="🔒 Žádná záloha · Bez karty · Platíte až při převzetí",
        offer="3169",
        lp="3203",
        thankyou="https://shoptrendcrest.com/cz/dochura/thank-you.html",
        key="2921bf78363e2342676f5e420c8699846d81f54c",
        submit="Objednat nyní",
    ),
    "3910": _form(
        labels=("Vārds Uzvārds*", "Adrese*", "Tālrunis*"),
        placeholders=("Vārds Uzvārds", "Adrese", "Tālrunis"),
        form_note="🔒 Bez avansa · Bez kartes · Maksājat tikai saņemot",
        offer="3910",
        lp="3950",
        thankyou="https://shoptrendcrest.com/lv/dochura/thank-you.html",
        key="b4a6705c18b85cb539bf5c0531874f23e83ec6bc",
        submit="Pasūtiet tagad",
    ),
    "4321": _form(
        labels=("Meno Priezvisko*", "Adresa*", "Telefón*"),
        placeholders=("Meno Priezvisko", "Adresa", "Telefón"),
        form_note="🔒 Žiadna záloha · Bez karty · Platíte až pri prevzatí",
        offer="4321",
        lp="4361",
        thankyou="https://shoptrendcrest.com/sk/dochura/thank-you.html",
        key="fc4c2ff3ca9f6e538c1c6f349475d1450281c19b",
        submit="Objednajte si teraz",
    ),
}
