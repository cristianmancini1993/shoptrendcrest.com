#!/usr/bin/env python3
"""Build locale strings by aligning shopgearspot ferrox geo pages to IT CENDORA keys."""
from __future__ import annotations

import difflib
import pprint
import re
from pathlib import Path
from typing import Any

from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"

FERROX = {
    "ro": ("ro", "ferrox-539"),
    "pt": ("pt", "ferrox-1476"),
    "sk": ("sk", "ferrox-536"),
    "si": ("si", "ferrox-535"),
    "hr": ("hr", "ferrox-537"),
    "hu": ("hu", "ferrox-534"),
    "cs": ("cz", "ferrox-538"),
    "pl": ("pl", "ferrox-540"),
}

# ES/DE/LT/PL/LV: no ferrox folder in seed map — filled from RO + manual overrides below.
MANUAL_GEO: dict[str, dict[str, Any]] = {}

FORM = {
    "pt": {
        "label_name": "Nome completo*",
        "label_tel": "Telefone*",
        "label_addr": "Morada*",
        "ph_name": "Ana Silva",
        "ph_tel": "+351 912 345 678",
        "ph_addr": "Rua da Liberdade 45, 1250-096 Lisboa",
    },
    "sk": {
        "label_name": "Meno a priezvisko*",
        "label_tel": "Telefón*",
        "label_addr": "Adresa*",
        "ph_name": "Peter Horváth",
        "ph_tel": "+421 912 345 678",
        "ph_addr": "Hlavná 15, 811 01 Bratislava",
    },
    "si": {
        "label_name": "Ime in priimek*",
        "label_tel": "Telefonska številka*",
        "label_addr": "Naslov*",
        "ph_name": "Luka Novak",
        "ph_tel": "+386 41 123 456",
        "ph_addr": "Slovenska cesta 10, 1000 Ljubljana",
    },
    "hr": {
        "label_name": "Ime i prezime*",
        "label_tel": "Broj mobitela*",
        "label_addr": "Adresa*",
        "ph_name": "Ivan Horvat",
        "ph_tel": "+385 91 123 4567",
        "ph_addr": "Ilica 10, 10000 Zagreb",
    },
    "hu": {
        "label_name": "Teljes név*",
        "label_tel": "Telefonszám*",
        "label_addr": "Teljes cím*",
        "ph_name": "Nagy Péter",
        "ph_tel": "+36 30 123 4567",
        "ph_addr": "Andrássy út 10., 1061 Budapest",
    },
    "es": {
        "label_name": "Nombre completo*",
        "label_tel": "Número de teléfono*",
        "label_addr": "Dirección completa*",
        "ph_name": "María García López",
        "ph_tel": "+34 612 34 56 78",
        "ph_addr": "Calle Mayor 12, 28013 Madrid",
    },
    "de": {
        "label_name": "Vor- und Nachname*",
        "label_tel": "Telefon*",
        "label_addr": "Vollständige Anschrift*",
        "ph_name": "Thomas Müller",
        "ph_tel": "+49 151 23456789",
        "ph_addr": "Hauptstraße 10, 10115 Berlin",
    },
    "lt": {
        "label_name": "Vardas ir pavardė*",
        "label_tel": "Telefonas*",
        "label_addr": "Adresas*",
        "ph_name": "Jonas Petraitis",
        "ph_tel": "+370 612 34567",
        "ph_addr": "Gedimino pr. 10-5, 01103 Vilnius",
    },
    "pl": {
        "label_name": "Imię i nazwisko*",
        "label_tel": "Telefon*",
        "label_addr": "Adres*",
        "ph_name": "Jan Kowalski",
        "ph_tel": "+48 512 345 678",
        "ph_addr": "ul. Marszałkowska 10/5, 00-590 Warszawa",
    },
    "cs": {
        "label_name": "Jméno a příjmení*",
        "label_tel": "Telefon*",
        "label_addr": "Adresa*",
        "ph_name": "Jan Novák",
        "ph_tel": "+420 601 123 456",
        "ph_addr": "Václavské nám. 1, 110 00 Praha",
    },
    "lv": {
        "label_name": "Vārds un uzvārds*",
        "label_tel": "Tālrunis*",
        "label_addr": "Pilna adrese*",
        "ph_name": "Jānis Bērziņš",
        "ph_tel": "+371 21 234 567",
        "ph_addr": "Brīvības iela 10, LV-1010 Rīga",
    },
    "el": {
        "label_name": "Ονομα και επίθετο*",
        "label_tel": "Τηλέφωνο*",
        "label_addr": "Διεύθυνση*",
        "ph_name": "Γιώργος Παπαδόπουλος",
        "ph_tel": "+30 691 234 5678",
        "ph_addr": "Οδός Αθηνάς 10, 105 51 Αθήνα",
    },
}

BLOCKED = {
    "pt": (
        "Os pedidos online para esta oferta estão temporariamente desativados (integração em configuração). "
        "Escreva para info@shoptrendcrest.com — ligamos de volta.",
        "Envio temporariamente indisponível",
    ),
    "sk": (
        "Online požiadavky na túto ponuku sú dočasne vypnuté (integrácia v konfigurácii). "
        "Napíšte na info@shoptrendcrest.com — ozveme sa vám.",
        "Odoslanie je dočasne nedostupné",
    ),
    "si": (
        "Spletne zahteve za to ponudbo so začasno onemogočene (integracija v nastavitvah). "
        "Pišite na info@shoptrendcrest.com — poklicali vas bomo.",
        "Pošiljanje začasno ni na voljo",
    ),
    "hr": (
        "Online zahtjevi za ovu ponudu privremeno su onemogućeni (integracija u konfiguraciji). "
        "Pišite na info@shoptrendcrest.com — javit ćemo vam se.",
        "Slanje privremeno nije dostupno",
    ),
    "hu": (
        "Az online igénylés ehhez az ajánlathoz átmenetileg szünetel (beállítás alatt). "
        "Írjon az info@shoptrendcrest.com címre — visszahívjuk.",
        "Küldés átmenetileg nem elérhető",
    ),
    "es": (
        "Las solicitudes online de esta oferta están desactivadas temporalmente (integración en configuración). "
        "Escriba a info@shoptrendcrest.com — le llamaremos.",
        "Envío temporalmente no disponible",
    ),
    "de": (
        "Online-Anfragen für dieses Angebot sind vorübergehend deaktiviert (Integration in Konfiguration). "
        "Schreiben Sie an info@shoptrendcrest.com — wir rufen zurück.",
        "Senden vorübergehend nicht verfügbar",
    ),
    "lt": (
        "Šios akcijos užklausos internetu laikinai išjungtos (integracija konfigūruojama). "
        "Rašykite info@shoptrendcrest.com — perskambinsime.",
        "Siuntimas laikinai nepasiekiamas",
    ),
    "pl": (
        "Zgłoszenia online dla tej oferty są tymczasowo wyłączone (integracja w konfiguracji). "
        "Napisz na info@shoptrendcrest.com — oddzwonimy.",
        "Wysyłka tymczasowo niedostępna",
    ),
    "cs": (
        "Online žádosti pro tuto nabídku jsou dočasně vypnuté (integrace v konfiguraci). "
        "Napište na info@shoptrendcrest.com — ozveme se.",
        "Odeslání je dočasně nedostupné",
    ),
    "lv": (
        "Šī piedāvājuma pieteikumi tiešsaistē uz laiku ir atspējoti (integrācija konfigurācijā). "
        "Rakstiet uz info@shoptrendcrest.com — pārzvanīsim.",
        "Iesniegšana īslaicīgi nav pieejama",
    ),
    "ro": (
        "Cererile online pentru această ofertă sunt temporar dezactivate (integrare în configurare). "
        "Scrieți la info@shoptrendcrest.com — vă sunăm noi.",
        "Trimitere temporar indisponibilă",
    ),
    "el": (
        "Οι online αιτήσεις για αυτή την προσφορά είναι προσωρινά απενεργοποιημένες (ρύθμιση ενσωμάτωσης). "
        "Γράψτε στο info@shoptrendcrest.com — θα σας καλέσουμε.",
        "Η αποστολή είναι προσωρινά μη διαθέσιμη",
    ),
}


def _read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def _pair_lines(a: list[str], b: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    sm = difflib.SequenceMatcher(None, a, b)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for x, y in zip(a[i1:i2], b[j1:j2]):
                tx = _text(x)
                ty = _text(y)
                if tx and ty and tx != ty:
                    out[tx] = ty
        elif tag == "replace" and (i2 - i1) == (j2 - j1):
            for x, y in zip(a[i1:i2], b[j1:j2]):
                tx = _text(x)
                ty = _text(y)
                if tx and ty and tx != ty:
                    out[tx] = ty
    return out


def _text(line: str) -> str | None:
    m = re.search(r">([^<>]+)<", line)
    if not m:
        return None
    t = m.group(1).strip()
    if not t or t.startswith("http"):
        return None
    return t


def _ferrox_to_cendora_it() -> dict[str, str]:
    it_f = _read_lines(SG / "it/ferrox/index.html")
    it_c = _read_lines(ROOT / "it/cendora/index.html")
    return _pair_lines(it_f, it_c)


def _swap_brand(s: str) -> str:
    s = s.replace("FERROX™", "CENDORA™").replace("FERROX", "CENDORA")
    s = s.replace("oțel inoxidabil", "antiaderent").replace("inox", "antiaderent")
    s = s.replace("acciaio inossidabile", "antiaderente").replace("oțel inoxidabil", "antiaderent")
    s = s.replace("stainless steel", "non-stick").replace("Stahl", "Antihaft")
    return s


def _map_value(it_cendora: str, it_f2c: dict[str, str], it_f2geo: dict[str, str]) -> str:
    """Map Italian CENDORA string to geo via ferrox alignment."""
    if it_cendora in it_f2geo:
        return _swap_brand(it_f2geo[it_cendora])
    for it_f, it_c in it_f2c.items():
        if it_c == it_cendora:
            geo_f = it_f2geo.get(it_f)
            if geo_f:
                return _swap_brand(geo_f)
    for it_f, geo_f in it_f2geo.items():
        if it_f == it_cendora or (len(it_cendora) > 20 and it_cendora[:40] in it_f):
            return _swap_brand(geo_f)
    return it_cendora


def build_geo(code: str) -> dict[str, Any]:
    if code in MANUAL_GEO:
        loc = dict(MANUAL_GEO[code])
    elif code in FERROX:
        geo, folder = FERROX[code]
        it_f = _read_lines(SG / "it/ferrox/index.html")
        geo_f = _read_lines(SG / geo / folder / "index.html")
        it_f2geo = _pair_lines(it_f, geo_f)
        it_f2c = _ferrox_to_cendora_it()
        loc: dict[str, Any] = {}
        for k, it_val in IT_STRINGS.items():
            if k in ("ty_steps",):
                loc[k] = [_map_value(x, it_f2c, it_f2geo) for x in it_val]
            elif k in ("ty_badges",):
                loc[k] = tuple(_map_value(x, it_f2c, it_f2geo) for x in it_val)
            elif isinstance(it_val, str):
                loc[k] = _map_value(it_val, it_f2c, it_f2geo)
            else:
                loc[k] = it_val
    else:
        loc = dict(_ro())

    if code in FORM:
        loc.update(FORM[code])
    if code in BLOCKED:
        loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[code]
    if "cta" in loc:
        loc["cta_inline"] = loc["cta"]
    loc["ty_alt"] = IT_STRINGS["ty_alt"]
    return loc


def main() -> None:
    codes = ["ro", "pt", "sk", "si", "hr", "hu", "es", "de", "lt", "pl", "cs", "lv"]
    out: dict[str, dict[str, Any]] = {}
    out["ro"] = _ro()
    for code in codes:
        if code == "ro":
            continue
        print("align", code)
        out[code] = build_geo(code)

    header = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CENDORA™ 12-piece non-stick landing translations (Italian source excluded).

Used by seed_cendora_locales.py when DeepL is unavailable.
"""
from __future__ import annotations

from typing import Any

from _cendora_it_strings import IT_STRINGS

TRANSLATIONS: dict[str, dict[str, Any]] = '''
    body = pprint.pformat(out, width=120, sort_dicts=False)
    footer = '''

def _validate() -> None:
    expected = set(IT_STRINGS)
    for code, data in TRANSLATIONS.items():
        keys = set(data)
        missing = expected - keys
        extra = keys - expected
        if missing or extra:
            raise AssertionError(
                f"{code}: missing {sorted(missing)[:5]} ({len(missing)}); "
                f"extra {sorted(extra)[:5]} ({len(extra)})"
            )


_validate()
'''
    Path(__file__).with_name("build_cendora_i18n.py").write_text(
        header + body + footer,
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
