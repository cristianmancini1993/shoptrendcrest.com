#!/usr/bin/env python3
"""One-off generator for build_cendora_i18n.py (manual RO + machine-assist other langs)."""
from __future__ import annotations

import json
import pprint
import re
import time
from pathlib import Path
from typing import Any

from deep_translator import MyMemoryTranslator

from _cendora_i18n_embed import _ro
from _cendora_it_strings import IT_STRINGS

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
}

TARGET = {
    "pt": "pt-PT",
    "sk": "sk-SK",
    "si": "sl-SI",
    "hr": "hr-HR",
    "hu": "hu-HU",
    "es": "es-ES",
    "de": "de-DE",
    "lt": "lt-LT",
    "pl": "pl-PL",
    "cs": "cs-CZ",
    "lv": "lv-LV",
}

_PROTECT_PATTERNS = (
    r"\{price\}",
    r"\{n\}",
    r"CENDORA™",
    r"<strong>",
    r"</strong>",
    r'<span class="hl">',
    r"</span>",
)


_CACHE_PATH = Path(__file__).with_name("_cendora_tr_cache.json")
_CACHE: dict[str, str] = (
    json.loads(_CACHE_PATH.read_text(encoding="utf-8")) if _CACHE_PATH.exists() else {}
)


def _shield_translate(text: str, tgt: str) -> str:
    ck = f"{tgt}\x1f{text}"
    if ck in _CACHE:
        return _CACHE[ck]

    protected: list[str] = []

    def shield(m: re.Match[str]) -> str:
        protected.append(m.group(0))
        return f"__PH{len(protected) - 1}__"

    s = text
    for pat in _PROTECT_PATTERNS:
        s = re.sub(pat, shield, s)

    for attempt in range(6):
        try:
            out = MyMemoryTranslator(source="it-IT", target=f"{tgt}").translate(s)
            break
        except Exception:
            time.sleep(2.0 * (attempt + 1))
    else:
        raise RuntimeError(f"translate failed: {text[:80]}")

    for i, part in enumerate(protected):
        out = out.replace(f"__PH{i}__", part)
    _CACHE[ck] = out
    _CACHE_PATH.write_text(json.dumps(_CACHE, ensure_ascii=False), encoding="utf-8")
    return out


def _build_locale(code: str, tgt: str) -> dict[str, Any]:
    loc: dict[str, Any] = {}
    for k in IT_STRINGS:
        v = IT_STRINGS[k]
        if k == "ty_steps":
            loc[k] = [_shield_translate(x, tgt) for x in v]
            time.sleep(0.6)
            continue
        if k == "ty_badges":
            loc[k] = tuple(_shield_translate(x, tgt) for x in v)
            time.sleep(0.6)
            continue
        if isinstance(v, str):
            if k in ("ty_alt",):
                loc[k] = v
                continue
            loc[k] = _shield_translate(v, tgt)
            time.sleep(0.6)
        else:
            loc[k] = v
    loc.update(FORM[code])
    loc["form_blocked_msg"], loc["form_blocked_btn"] = BLOCKED[code]
    if "cta" in loc:
        loc["cta_inline"] = loc["cta"]
    return loc


def main() -> None:
    out: dict[str, dict[str, Any]] = {"ro": _ro()}
    for code, tgt in TARGET.items():
        print(f"Translating {code} ({tgt})…", flush=True)
        out[code] = _build_locale(code, tgt)

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
    print("Wrote build_cendora_i18n.py", len(out), "locales")


if __name__ == "__main__":
    main()
