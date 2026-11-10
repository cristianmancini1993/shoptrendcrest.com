# -*- coding: utf-8 -*-
"""LEAFORA order forms: name → phone → address (localized per geo)."""

WEBHOOK = "https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o"
UID = "019fd3be-dca9-7be5-9ba1-36a2f751f582"

# offer_id: lp, key, thank-you path, labels/placeholders, submit button
_SPECS: dict[str, dict] = {
    "1745": {
        "lp": "1765",
        "key": "f17f8e987caae9306820990299daea5640362191",
        "ty": "https://homeshopspot.com/pl/leafora-1745/thank-you.html",
        "name_l": "Imię i nazwisko*",
        "name_ph": "Jan Kowalski",
        "tel_l": "Numer telefonu*",
        "tel_ph": "+48 512 345 678",
        "addr_l": "Adres dostawy*",
        "addr_ph": "ul. Marszałkowska 10/5, 00-590 Warszawa",
        "btn": "Zamów teraz",
    },
    "2653": {
        "lp": "2680",
        "key": "af164f26915f3f205a3a86e4a992c9a1e1f0810e",
        "ty": "https://homeshopspot.com/hu/leafora-2653/thank-you.html",
        "name_l": "Teljes név*",
        "name_ph": "Kovács János",
        "tel_l": "Telefonszám*",
        "tel_ph": "+36 30 123 4567",
        "addr_l": "Szállítási cím*",
        "addr_ph": "Andrássy út 45., 1061 Budapest",
        "btn": "Rendelés utánvéttel",
    },
    "2657": {
        "lp": "2684",
        "key": "fd96f2903b946bafd653b169ed92a261377c511c",
        "ty": "https://homeshopspot.com/ro/leafora-2657/thank-you.html",
        "name_l": "Nume și prenume*",
        "name_ph": "Ion Popescu",
        "tel_l": "Număr de telefon*",
        "tel_ph": "+40 721 123 456",
        "addr_l": "Adresă de livrare*",
        "addr_ph": "Str. Victoriei 10, Ap. 5, 010001 București",
        "btn": "COMANDĂ ACUM",
    },
    "3188": {
        "lp": "3222",
        "key": "55e86b78a65b5f9328ee24dc43b0391bb18a635e",
        "ty": "https://homeshopspot.com/de/leafora-3188/thank-you.html",
        "name_l": "Vor- und Nachname*",
        "name_ph": "Hans Müller",
        "tel_l": "Telefonnummer*",
        "tel_ph": "+49 170 1234567",
        "addr_l": "Lieferadresse*",
        "addr_ph": "Musterstraße 45, 10115 Berlin",
        "btn": "Jetzt bestellen",
    },
    "3189": {
        "lp": "3223",
        "key": "9f02b625377ebce06b1be0a33385b863ebdf3f50",
        "ty": "https://homeshopspot.com/lt/leafora-3189/thank-you.html",
        "name_l": "Vardas ir pavardė*",
        "name_ph": "Jonas Petraitis",
        "tel_l": "Telefono numeris*",
        "tel_ph": "+370 612 34567",
        "addr_l": "Pristatymo adresas*",
        "addr_ph": "Gedimino pr. 10-5, 01103 Vilnius",
        "btn": "Užsisakykite dabar",
    },
    "3190": {
        "lp": "3224",
        "key": "c06e21866c335186775b297703801325c9f98e12",
        "ty": "https://homeshopspot.com/cz/leafora-3190/thank-you.html",
        "name_l": "Jméno a příjmení*",
        "name_ph": "Jan Novák",
        "tel_l": "Telefonní číslo*",
        "tel_ph": "+420 601 123 456",
        "addr_l": "Doručovací adresa*",
        "addr_ph": "Václavské nám. 1, 110 00 Praha",
        "btn": "Objednat nyní",
    },
    "3191": {
        "lp": "3225",
        "key": "f76296955190b857ec8a5960f7bf6dbb128d21a7",
        "ty": "https://homeshopspot.com/pt/leafora-3191/thank-you.html",
        "name_l": "Nome completo*",
        "name_ph": "João Silva",
        "tel_l": "Número de telefone*",
        "tel_ph": "+351 912 345 678",
        "addr_l": "Morada de entrega*",
        "addr_ph": "Rua Augusta 45, 1100-048 Lisboa",
        "btn": "Encomendar agora",
    },
    "3192": {
        "lp": "3226",
        "key": "3a38abb7bbcf3f3508fb04e8b366fa2b02a047a2",
        "ty": "https://homeshopspot.com/es/leafora-3192/thank-you.html",
        "name_l": "Nombre y apellidos*",
        "name_ph": "Juan García",
        "tel_l": "Número de teléfono*",
        "tel_ph": "+34 612 345 678",
        "addr_l": "Dirección de entrega*",
        "addr_ph": "Calle Mayor 45, 28013 Madrid",
        "btn": "Haz tu pedido",
    },
    "4065": {
        "lp": "4105",
        "key": "d7bfe1e7694bb53280d53f9d630671d29fb21e89",
        "ty": "https://homeshopspot.com/sk/leafora-4065/thank-you.html",
        "name_l": "Meno a priezvisko*",
        "name_ph": "Ján Novák",
        "tel_l": "Telefónne číslo*",
        "tel_ph": "+421 901 123 456",
        "addr_l": "Doručovacia adresa*",
        "addr_ph": "Hlavná 45, 811 01 Bratislava",
        "btn": "Objednajte si teraz",
    },
    "4066": {
        "lp": "4106",
        "key": "fac6ba9f94744f3ddccdfab05b01084b95c08d1c",
        "ty": "https://homeshopspot.com/lv/leafora-4066/thank-you.html",
        "name_l": "Vārds un uzvārds*",
        "name_ph": "Jānis Bērziņš",
        "tel_l": "Tālruņa numurs*",
        "tel_ph": "+371 21 234 567",
        "addr_l": "Piegādes adrese*",
        "addr_ph": "Brīvības iela 45, LV-1010 Rīga",
        "btn": "Pasūtiet tagad",
    },
    "4188": {
        "lp": "4228",
        "key": "fc5af37bfce57261f13c388e66f8053db7ee5f16",
        "ty": "https://homeshopspot.com/it/leafora-4188/thank-you.html",
        "name_l": "Nome e cognome*",
        "name_ph": "Mario Rossi",
        "tel_l": "Numero di telefono*",
        "tel_ph": "+39 312 345 6789",
        "addr_l": "Indirizzo di consegna*",
        "addr_ph": "Via Roma 45, Interno 12, 00100 Roma",
        "btn": "ORDINA ADESSO",
    },
}


def _render(offer_id: str, s: dict) -> str:
    return f"""<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
<label for="name">{s["name_l"]}</label>
<input id="name" type="text" name="name" autocomplete="name" placeholder="{s["name_ph"]}" required><br>
<label for="tel">{s["tel_l"]}</label>
<input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{s["tel_ph"]}" required><br>
<label for="street-address">{s["addr_l"]}</label>
<input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{s["addr_ph"]}" required><br>
<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer_id}" />
<input name="lp" type="hidden" value="{s["lp"]}" />
<input name="thankyoupage" type="hidden" value="{s["ty"]}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}" />
<input name="_key" type="hidden" value="{s["key"]}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{s["btn"]}</button>
</div>
<script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
</form>"""


FORMS: dict[str, str] = {oid: _render(oid, spec) for oid, spec in _SPECS.items()}

LANDINGS: dict[str, str] = {
    "1745": "pl/leafora-1745/landing.html",
    "2653": "hu/leafora-2653/landing.html",
    "2657": "ro/leafora-2657/landing.html",
    "3188": "de/leafora-3188/landing.html",
    "3189": "lt/leafora-3189/landing.html",
    "3190": "cz/leafora-3190/landing.html",
    "3191": "pt/leafora-3191/landing.html",
    "3192": "es/leafora-3192/landing.html",
    "4065": "sk/leafora-4065/landing.html",
    "4066": "lv/leafora-4066/landing.html",
    "4188": "it/leafora-4188/landing.html",
}
