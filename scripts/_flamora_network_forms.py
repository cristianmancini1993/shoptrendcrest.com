# -*- coding: utf-8 -*-
"""Adrice HTML forms for FLAMORA electric fireplace geo landings."""

WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"


def _form(
    *,
    label_name: str,
    ph_name: str,
    label_addr: str,
    ph_addr: str,
    label_tel: str,
    ph_tel: str,
    offer: str,
    lp: str,
    ty: str,
    key: str,
    btn: str,
    form_note: str,
) -> str:
    return f"""      <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">{label_name}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{ph_name}" required><br>
        <label for="tel">{label_tel}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{ph_tel}" required><br>
        <label for="street-address">{label_addr}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{ph_addr}" required><br>
        <input name="uid" type="hidden" value="{UID}">
        <input name="offer" type="hidden" value="{offer}">
        <input name="lp" type="hidden" value="{lp}">
        <input name="thankyoupage" type="hidden" value="{ty}">
        <input name="webhook" type="hidden" value="{WEBHOOK}">
        <input name="_key" type="hidden" value="{key}">
        <div style="margin-top:10px;text-align:center">
          <button name="submit" type="submit" class="cta-btn">{btn}</button>
        </div>
        <p class="form-note">{form_note}</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
      </form>"""


FORM_META = {
    "pl/flamora-1987": {"offer": "1987", "lp": "2008", "key": "93dd62a5a4f987910176f99103f5f73cb831befb"},
    "cz/flamora-2400": {"offer": "2400", "lp": "2425", "key": "973b6853f359b2dc82f6e131a902126fba4abf51"},
    "es/flamora-2635": {"offer": "2635", "lp": "2662", "key": "ce52f8fe99398bf301d01f91e1dac239860e02c6"},
    "pt/flamora-2636": {"offer": "2636", "lp": "2663", "key": "79c9e492ae5109ea012a06d66ac8eee5df78259a"},
    "de/flamora-2665": {"offer": "2665", "lp": "2692", "key": "a04999c202f01ccfea28ecca727b2b04db5c637a"},
    "hu/flamora-2668": {"offer": "2668", "lp": "2695", "key": "26af2f477db6b9a9eb68256a3743201e4915d81f"},
    "sk/flamora-4357": {"offer": "4357", "lp": "4397", "key": "7ef632ed19446d6808b6d78050c553c8ee46ec09"},
    "lv/flamora-4358": {"offer": "4358", "lp": "4398", "key": "c300c8c5510b6a15acc700733bbe317502784f2c"},
}

FORMS = {
    "pl/flamora-1987": _form(
        label_name="Imię Nazwisko*",
        ph_name="Anna Kowalska",
        label_addr="Adres*",
        ph_addr="ul. Marszałkowska 10, 00-590 Warszawa",
        label_tel="Telefon*",
        ph_tel="+48 512 345 678",
        offer="1987",
        lp="2008",
        ty="https://gadgetshifthub.com/pl/flamora-1987/thank-you.html",
        key=FORM_META["pl/flamora-1987"]["key"],
        btn="Zamów teraz",
        form_note="🔒 Bez zaliczki · Bez karty · Płacisz tylko przy odbiorze",
    ),
    "cz/flamora-2400": _form(
        label_name="Jméno Příjmení*",
        ph_name="Jan Novák",
        label_addr="Adresa*",
        ph_addr="Václavské nám. 1, 110 00 Praha",
        label_tel="Telefon*",
        ph_tel="+420 601 234 567",
        offer="2400",
        lp="2425",
        ty="https://gadgetshifthub.com/cz/flamora-2400/thank-you.html",
        key=FORM_META["cz/flamora-2400"]["key"],
        btn="Objednat nyní",
        form_note="🔒 Bez zálohy · Bez karty · Platíte jen při převzetí",
    ),
    "es/flamora-2635": _form(
        label_name="Nombre Apellido*",
        ph_name="María García",
        label_addr="Dirección*",
        ph_addr="Calle Mayor 10, 28013 Madrid",
        label_tel="Teléfono*",
        ph_tel="+34 612 345 678",
        offer="2635",
        lp="2662",
        ty="https://gadgetshifthub.com/es/flamora-2635/thank-you.html",
        key=FORM_META["es/flamora-2635"]["key"],
        btn="Haz tu pedido",
        form_note="🔒 Sin anticipo · Sin tarjeta · Solo pagas a la entrega",
    ),
    "pt/flamora-2636": _form(
        label_name="Nome completo*",
        ph_name="Ana Silva",
        label_addr="Morada*",
        ph_addr="Rua Augusta 10, 1100-053 Lisboa",
        label_tel="Telefone de contacto*",
        ph_tel="+351 912 345 678",
        offer="2636",
        lp="2663",
        ty="https://gadgetshifthub.com/pt/flamora-2636/thank-you.html",
        key=FORM_META["pt/flamora-2636"]["key"],
        btn="Encomendar agora",
        form_note="🔒 Sem adiantamento · Sem cartão · Paga apenas na entrega",
    ),
    "de/flamora-2665": _form(
        label_name="Vorname Nachname*",
        ph_name="Anna Müller",
        label_addr="Anschrift*",
        ph_addr="Friedrichstraße 10, 10117 Berlin",
        label_tel="Telefon*",
        ph_tel="+49 151 23456789",
        offer="2665",
        lp="2692",
        ty="https://gadgetshifthub.com/de/flamora-2665/thank-you.html",
        key=FORM_META["de/flamora-2665"]["key"],
        btn="Jetzt bestellen",
        form_note="🔒 Keine Vorauszahlung · Keine Karte · Sie zahlen nur bei Lieferung",
    ),
    "hu/flamora-2668": _form(
        label_name="Teljes név*",
        ph_name="Kovács Anna",
        label_addr="Cím*",
        ph_addr="Andrássy út 10, 1061 Budapest",
        label_tel="Telefon*",
        ph_tel="+36 30 123 4567",
        offer="2668",
        lp="2695",
        ty="https://gadgetshifthub.com/hu/flamora-2668/thank-you.html",
        key=FORM_META["hu/flamora-2668"]["key"],
        btn="Rendeljen most",
        form_note="🔒 Nincs előleg · Nincs kártya · Csak átvételkor fizet",
    ),
    "sk/flamora-4357": _form(
        label_name="Meno Priezvisko*",
        ph_name="Ján Novák",
        label_addr="Adresa*",
        ph_addr="Hlavná 10, 811 01 Bratislava",
        label_tel="Telefón*",
        ph_tel="+421 912 345 678",
        offer="4357",
        lp="4397",
        ty="https://gadgetshifthub.com/sk/flamora-4357/thank-you.html",
        key=FORM_META["sk/flamora-4357"]["key"],
        btn="Objednajte si teraz",
        form_note="🔒 Bez zálohy · Bez karty · Platíte len pri prevzatí",
    ),
    "lv/flamora-4358": _form(
        label_name="Vārds Uzvārds*",
        ph_name="Anna Bērziņa",
        label_addr="Adrese*",
        ph_addr="Brīvības iela 10, LV-1010 Rīga",
        label_tel="Tālrunis*",
        ph_tel="+371 2123 4567",
        offer="4358",
        lp="4398",
        ty="https://gadgetshifthub.com/lv/flamora-4358/thank-you.html",
        key=FORM_META["lv/flamora-4358"]["key"],
        btn="Pasūtiet tagad",
        form_note="🔒 Bez avansa · Bez kartes · Maksājat tikai pie saņemšanas",
    ),
}
