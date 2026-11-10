# -*- coding: utf-8 -*-
"""3-field order form copy: name, phone, address — keyed by site geo folder (cz, gr, …)."""

from __future__ import annotations

# ln/lp/la = labels; pn/pp/pa = placeholders
FIELDS: dict[str, dict[str, str]] = {
    "it": {
        "ln": "Nome e cognome*",
        "lp": "Numero di telefono*",
        "la": "Indirizzo di consegna*",
        "pn": "Mario Rossi",
        "pp": "+39 312 345 6789",
        "pa": "Via Roma 45, Interno 12, 00100 Roma",
    },
    "de": {
        "ln": "Vor- und Nachname*",
        "lp": "Telefonnummer*",
        "la": "Lieferadresse*",
        "pn": "Max Mustermann",
        "pp": "+49 151 23456789",
        "pa": "Musterstraße 12, 10115 Berlin",
    },
    "es": {
        "ln": "Nombre y apellidos*",
        "lp": "Número de teléfono*",
        "la": "Dirección de envío*",
        "pn": "María García",
        "pp": "+34 612 345 678",
        "pa": "Calle Mayor 10, 28013 Madrid",
    },
    "pt": {
        "ln": "Nome e apelido*",
        "lp": "Número de telefone*",
        "la": "Morada de envio*",
        "pn": "João Silva",
        "pp": "+351 912 345 678",
        "pa": "Rua das Flores 25, 4000-007 Porto",
    },
    "pl": {
        "ln": "Imię i nazwisko*",
        "lp": "Numer telefonu*",
        "la": "Adres dostawy*",
        "pn": "Jan Kowalski",
        "pp": "+48 512 345 678",
        "pa": "ul. Kwiatowa 10, 00-001 Warszawa",
    },
    "cz": {
        "ln": "Jméno a příjmení*",
        "lp": "Telefonní číslo*",
        "la": "Doručovací adresa*",
        "pn": "Jan Novák",
        "pp": "+420 601 123 456",
        "pa": "Ulice 10, 110 00 Praha",
    },
    "sk": {
        "ln": "Meno a priezvisko*",
        "lp": "Telefónne číslo*",
        "la": "Doručovacia adresa*",
        "pn": "Ján Novák",
        "pp": "+421 901 123 456",
        "pa": "Hlavná 10, 811 01 Bratislava",
    },
    "hu": {
        "ln": "Teljes név*",
        "lp": "Telefonszám*",
        "la": "Szállítási cím*",
        "pn": "Kovács János",
        "pp": "+36 30 123 4567",
        "pa": "Fő utca 10, 1051 Budapest",
    },
    "ro": {
        "ln": "Nume și prenume*",
        "lp": "Număr de telefon*",
        "la": "Adresa de livrare*",
        "pn": "Ion Popescu",
        "pp": "+40 712 345 678",
        "pa": "Strada Victoriei 10, 010063 București",
    },
    "hr": {
        "ln": "Ime i prezime*",
        "lp": "Broj telefona*",
        "la": "Adresa za dostavu*",
        "pn": "Ivan Horvat",
        "pp": "+385 91 123 4567",
        "pa": "Ilica 10, 10000 Zagreb",
    },
    "si": {
        "ln": "Ime in priimek*",
        "lp": "Telefonska številka*",
        "la": "Naslov za dostavo*",
        "pn": "Janez Novak",
        "pp": "+386 41 123 456",
        "pa": "Slovenska cesta 10, 1000 Ljubljana",
    },
    "lv": {
        "ln": "Vārds un uzvārds*",
        "lp": "Tālruņa numurs*",
        "la": "Piegādes adrese*",
        "pn": "Jānis Bērziņš",
        "pp": "+371 2123 4567",
        "pa": "Brīvības iela 10, LV-1010 Rīga",
    },
    "lt": {
        "ln": "Vardas ir pavardė*",
        "lp": "Telefono numeris*",
        "la": "Pristatymo adresas*",
        "pn": "Jonas Jonaitis",
        "pp": "+370 612 34567",
        "pa": "Gedimino pr. 10, LT-01103 Vilnius",
    },
    "bg": {
        "ln": "Име и фамилия*",
        "lp": "Телефонен номер*",
        "la": "Адрес за доставка*",
        "pn": "Иван Иванов",
        "pp": "+359 88 123 4567",
        "pa": "ул. Витоша 10, 1000 София",
    },
    "gr": {
        "ln": "Όνομα και επώνυμο*",
        "lp": "Αριθμός τηλεφώνου*",
        "la": "Διεύθυνση παράδοσης*",
        "pn": "Γιάννης Παπαδόπουλος",
        "pp": "+30 691 234 5678",
        "pa": "Οδός Ερμού 10, 105 63 Αθήνα",
    },
    "en": {
        "ln": "Full name*",
        "lp": "Phone number*",
        "la": "Delivery address*",
        "pn": "John Smith",
        "pp": "+44 7700 900123",
        "pa": "10 High Street, London SW1A 1AA",
    },
    "fr": {
        "ln": "Nom et prénom*",
        "lp": "Numéro de téléphone*",
        "la": "Adresse de livraison*",
        "pn": "Jean Dupont",
        "pp": "+33 6 12 34 56 78",
        "pa": "10 rue de Rivoli, 75001 Paris",
    },
}


def tm_order_fields_html(geo: str, indent: str = "        ") -> str:
    c = FIELDS[geo]
    i = indent
    return (
        f'{i}<label for="name">{c["ln"]}</label>\n'
        f'{i}<input id="name" type="text" name="name" autocomplete="name" '
        f'placeholder="{c["pn"]}" required><br>\n'
        f'{i}<label for="tel">{c["lp"]}</label>\n'
        f'{i}<input id="tel" type="tel" name="tel" autocomplete="tel" '
        f'placeholder="{c["pp"]}" required><br>\n'
        f'{i}<label for="street-address">{c["la"]}</label>\n'
        f'{i}<input id="street-address" type="text" name="street-address" '
        f'autocomplete="street-address" placeholder="{c["pa"]}" required><br>'
    )


def geo_from_rel(rel: str) -> str:
    return rel.split("/", 1)[0]
