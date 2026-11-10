#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Seed _warmio_json/*.json from es master + per-country native fixups."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSON_DIR = ROOT / "_warmio_json"

FIXUPS: dict[str, dict[str, str]] = {
    "de": {
        "rating": "<strong>4,9/5</strong> — Über <strong>6.500</strong> Haushalte in Deutschland heizen bereits mit WARMIO™",
        "f1_p": "In ganz Deutschland in 24–48 Stunden",
        "kit_li5": "Anleitung auf Deutsch",
        "author1": "Giulia M. — Milano, verifizierter Kauf",
        "author2": "Francesca L. — Torino, verifizierter Kauf",
        "author3": "Giuseppe R. — Napoli, verifizierter Kauf",
    },
    "pt": {
        "rating": "<strong>4,9/5</strong> — Mais de <strong>6.500</strong> famílias em Portugal já aquecem com WARMIO™",
        "f1_p": "Em todo Portugal em 24–48 horas",
        "kit_li5": "Instruções em português",
        "author1": "Giulia M. — Milano, compra verificada",
        "author2": "Francesca L. — Torino, compra verificada",
        "author3": "Giuseppe R. — Napoli, compra verificada",
    },
    "pl": {
        "rating": "<strong>4,9/5</strong> — Ponad <strong>6 500</strong> gospodarstw w Polsce już ogrzewa się z WARMIO™",
        "f1_p": "W całej Polsce w 24–48 godzin",
        "kit_li5": "Instrukcja po polsku",
        "author1": "Giulia M. — Milano, zweryfikowany zakup",
        "author2": "Francesca L. — Torino, zweryfikowany zakup",
        "author3": "Giuseppe R. — Napoli, zweryfikowany zakup",
    },
    "ro": {
        "rating": "<strong>4,9/5</strong> — Peste <strong>6.500</strong> de familii din România se încălzesc deja cu WARMIO™",
        "f1_p": "În toată România în 24–48 de ore",
        "kit_li5": "Instrucțiuni în română",
        "author1": "Giulia M. — Milano, achiziție verificată",
        "author2": "Francesca L. — Torino, achiziție verificată",
        "author3": "Giuseppe R. — Napoli, achiziție verificată",
    },
    "cs": {
        "rating": "<strong>4,9/5</strong> — Více než <strong>6 500</strong> domácností v Česku už topí s WARMIO™",
        "f1_p": "V celé ČR do 24–48 hodin",
        "kit_li5": "Návod v češtině",
        "author1": "Giulia M. — Milano, ověřený nákup",
        "author2": "Francesca L. — Torino, ověřený nákup",
        "author3": "Giuseppe R. — Napoli, ověřený nákup",
    },
    "sk": {
        "rating": "<strong>4,9/5</strong> — Viac ako <strong>6 500</strong> domácností na Slovensku už kúri s WARMIO™",
        "f1_p": "Na celom Slovensku do 24–48 hodín",
        "kit_li5": "Návod v slovenčine",
        "author1": "Giulia M. — Milano, overený nákup",
        "author2": "Francesca L. — Torino, overený nákup",
        "author3": "Giuseppe R. — Napoli, overený nákup",
    },
    "hu": {
        "rating": "<strong>4,9/5</strong> — Több mint <strong>6 500</strong> magyar háztartás már WARMIO™-val fűt",
        "f1_p": "Magyarországon 24–48 órán belül",
        "kit_li5": "Magyar nyelvű útmutató",
        "author1": "Giulia M. — Milano, ellenőrzött vásárlás",
        "author2": "Francesca L. — Torino, ellenőrzött vásárlás",
        "author3": "Giuseppe R. — Napoli, ellenőrzött vásárlás",
    },
    "hr": {
        "rating": "<strong>4,9/5</strong> — Više od <strong>6.500</strong> kućanstava u Hrvatskoj već se grije s WARMIO™",
        "f1_p": "U cijeloj Hrvatskoj za 24–48 sati",
        "kit_li5": "Upute na hrvatskom",
        "author1": "Giulia M. — Milano, potvrđena kupnja",
        "author2": "Francesca L. — Torino, potvrđena kupnja",
        "author3": "Giuseppe R. — Napoli, potvrđena kupnja",
    },
    "si": {
        "rating": "<strong>4,9/5</strong> — Več kot <strong>6.500</strong> gospodinjstev v Sloveniji se že ogreva s WARMIO™",
        "f1_p": "Po vsej Sloveniji v 24–48 urah",
        "kit_li5": "Navodila v slovenščini",
        "author1": "Giulia M. — Milano, preverjen nakup",
        "author2": "Francesca L. — Torino, preverjen nakup",
        "author3": "Giuseppe R. — Napoli, preverjen nakup",
    },
    "lv": {
        "rating": "<strong>4,9/5</strong> — Vairāk nekā <strong>6 500</strong> mājsaimniecību Latvijā jau silda ar WARMIO™",
        "f1_p": "Visā Latvijā 24–48 stundu laikā",
        "kit_li5": "Instrukcijas latviešu valodā",
        "author1": "Giulia M. — Milano, verificēts pirkums",
        "author2": "Francesca L. — Torino, verificēts pirkums",
        "author3": "Giuseppe R. — Napoli, verificēts pirkums",
    },
    "lt": {
        "rating": "<strong>4,9/5</strong> — Daugiau nei <strong>6 500</strong> namų Lietuvoje jau šildosi su WARMIO™",
        "f1_p": "Visoje Lietuvoje per 24–48 val.",
        "kit_li5": "Instrukcijos lietuvių kalba",
        "author1": "Giulia M. — Milano, patvirtintas pirkimas",
        "author2": "Francesca L. — Torino, patvirtintas pirkimas",
        "author3": "Giuseppe R. — Napoli, patvirtintas pirkimas",
    },
}


def main() -> None:
    es = json.loads((JSON_DIR / "es.json").read_text(encoding="utf-8"))
    for code in [
        "hu",
        "ro",
        "si",
        "pt",
        "hr",
        "de",
        "pl",
        "cs",
        "lv",
        "sk",
        "lt",
    ]:
        bundle = copy.deepcopy(es)
        bundle.update(FIXUPS.get(code, {}))
        (JSON_DIR / f"{code}.json").write_text(
            json.dumps(bundle, ensure_ascii=False, indent=0) + "\n",
            encoding="utf-8",
        )
        print(code)


if __name__ == "__main__":
    main()
