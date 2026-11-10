# -*- coding: utf-8 -*-
"""LUNO™ Adrice order forms — name → phone → address."""

LANDINGS = {
    "1912": "de/luno-1912/landing.html",
    "1915": "hu/luno-1915/landing.html",
    "2480": "pt/luno-2480/landing.html",
    "3163": "es/luno-3163/landing.html",
    "3167": "pl/luno-3167/landing.html",
    "3169": "cz/luno-3169/landing.html",
    "3910": "lv/luno-3910/landing.html",
    "4321": "sk/luno-4321/landing.html",
}

WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"

_FORM_META = {
    "1912": {
        "labels": ("Vorname Nachname*", "Telefon*", "Anschrift*"),
        "placeholders": (
            "Max Müller",
            "+49 151 23456789",
            "Hauptstraße 15, 10115 Berlin",
        ),
        "submit": "Jetzt bestellen",
        "offer": "1912",
        "lp": "1932",
        "key": "5e68d2a8a6ca4ca1f511e39a64e1e943858ee329",
        "ty": "https://homeshopspot.com/de/luno-1912/thank-you.html",
    },
    "1915": {
        "labels": ("Keresztnév Vezetéknév*", "Telefon*", "Cím*"),
        "placeholders": (
            "Nagy János",
            "+36 30 123 4567",
            "1061 Budapest, Andrássy út 12",
        ),
        "submit": "Rendelje meg most",
        "offer": "1915",
        "lp": "1935",
        "key": "ee927936c4405d2e0b75f5166861a97ddfdf9ce8",
        "ty": "https://homeshopspot.com/hu/luno-1915/thank-you.html",
    },
    "2480": {
        "labels": ("Nome próprio Apelido*", "Telefone*", "Endereço*"),
        "placeholders": (
            "João Silva",
            "+351 912 345 678",
            "Rua Augusta 10, 1100-053 Lisboa",
        ),
        "submit": "Encomendar agora",
        "offer": "2480",
        "lp": "2505",
        "key": "e3f08e2ffec11563109788e01d24244d4f7be150",
        "ty": "https://homeshopspot.com/pt/luno-2480/thank-you.html",
    },
    "3163": {
        "labels": ("Nombre Apellido*", "Teléfono*", "Dirección*"),
        "placeholders": (
            "María García",
            "+34 612 345 678",
            "Calle Mayor 15, 28013 Madrid",
        ),
        "submit": "Haz tu pedido",
        "offer": "3163",
        "lp": "3197",
        "key": "58da2c2b87633ee4430cd5f3342f5fc7935ccfd7",
        "ty": "https://homeshopspot.com/es/luno-3163/thank-you.html",
    },
    "3167": {
        "labels": ("Imię Nazwisko*", "Telefon*", "Adres*"),
        "placeholders": (
            "Jan Kowalski",
            "+48 501 123 456",
            "ul. Marszałkowska 10/5, 00-590 Warszawa",
        ),
        "submit": "Zamów teraz",
        "offer": "3167",
        "lp": "3201",
        "key": "dfef13a537b06b7ae5e8d50a97bd05e8499f7b67",
        "ty": "https://homeshopspot.com/pl/luno-3167/thank-you.html",
    },
    "3169": {
        "labels": ("Jméno Příjmení*", "Telefon*", "Adresa*"),
        "placeholders": (
            "Jan Novák",
            "+420 601 123 456",
            "Václavské náměstí 1, 110 00 Praha",
        ),
        "submit": "Objednat nyní",
        "offer": "3169",
        "lp": "3203",
        "key": "2921bf78363e2342676f5e420c8699846d81f54c",
        "ty": "https://homeshopspot.com/cz/luno-3169/thank-you.html",
    },
    "3910": {
        "labels": ("Vārds Uzvārds*", "Tālrunis*", "Adrese*"),
        "placeholders": (
            "Jānis Bērziņš",
            "+371 20 123 456",
            "Brīvības iela 10, Rīga, LV-1010",
        ),
        "submit": "Pasūtiet tagad",
        "offer": "3910",
        "lp": "3950",
        "key": "b4a6705c18b85cb539bf5c0531874f23e83ec6bc",
        "ty": "https://homeshopspot.com/lv/luno-3910/thank-you.html",
    },
    "4321": {
        "labels": ("Meno Priezvisko*", "Telefón*", "Adresa*"),
        "placeholders": (
            "Ján Novák",
            "+421 901 123 456",
            "Hlavná 15, 811 01 Bratislava",
        ),
        "submit": "Objednajte si teraz",
        "offer": "4321",
        "lp": "4361",
        "key": "fc4c2ff3ca9f6e538c1c6f349475d1450281c19b",
        "ty": "https://homeshopspot.com/sk/luno-4321/thank-you.html",
    },
}


def _render_form(offer_id: str) -> str:
    m = _FORM_META[offer_id]
    ln, lt, la = m["labels"]
    pn, pt, pa = m["placeholders"]
    return f"""<form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
<label for="name">{ln}</label>
<input id="name" type="text" name="name" autocomplete="name" placeholder="{pn}" required><br>
<label for="tel">{lt}</label>
<input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{pt}" required><br>
<label for="street-address">{la}</label>
<input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{pa}" required><br>
<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{m['offer']}" />
<input name="lp" type="hidden" value="{m['lp']}" />
<input name="thankyoupage" type="hidden" value="{m['ty']}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{m['key']}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{m['submit']}</button>
</div>
<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
</form>"""


FORMS = {oid: _render_form(oid) for oid in LANDINGS}
