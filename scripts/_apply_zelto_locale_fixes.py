#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off patches to locale_*.py STRINGS — run from repo root if keys drift."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

PATCHES: dict[str, dict[str, str]] = {
    "locale_ro.py": {
        '"why1_eye": "01 · CÂTORVA BANI PE ZI"': '"why1_eye": "01 · CÂȚIVA BANI PE ZI"',
        '"cmp_old_air": "Uscacă și ridică praful"': '"cmp_old_air": "Usucă și ridică praful"',
        '"faq4_a": "Da. Dezumidificarea elimină excesul de abur: mai puțină condens, mai puțin miros de încăpere închisă, rufe care se usucă mai repede."':
        '"faq4_a": "Da. Dezumidificarea elimină excesul de abur: mai puțin condens, mai puțin miros de încăpere închisă, rufe care se usucă mai repede."',
        '"ph_tel": "+40 722 123 456"': '"ph_tel": "+40 721 234 567"',
        '"ph_addr": "Str. Victoriei 10, 010091 București"': '"ph_addr": "Str. Victoriei 10, 010096 București"',
    },
    "locale_si.py": {
        '"f4_p": "Brez predhodnega bremenitve"': '"f4_p": "Brez predhodne bremenitve"',
        '"cmp_win_air": "Trifazni filter HEPA H13"': '"cmp_win_air": "Tristopenjski filter HEPA H13"',
        '"why2_p2": "Komfort vam posluša."': '"why2_p2": "Udobje po vaših željah."',
        '"ph_name": "Janez Novak"': '"ph_name": "Luka Novak"',
        '"ph_tel": "+386 41 123 456"': '"ph_tel": "+386 41 123 456"',
    },
    "locale_hr.py": {
        '"why1_eye": "01 · PAR LIPE DNEVNO"': '"why1_eye": "01 · NEKOLIKO CENTI DNEVNO"',
        "drži temperaturu koja vam odgovara.": "održava temperaturu koja vam odgovara.",
        "drži zadanu temperaturu.": "održava zadanu temperaturu.",
        '"rev2_p": "«Ja sam montirao na zid. Kabel ravno u utičnicu, bez cijevi. Upalim i na zaslonu 28, odmah se osjeti. Zadovoljna zlatnom bojom kao na slikama»"':
        '"rev2_p": "«Sama sam ga montirala na zid. Kabel ide ravno u utičnicu, bez cijevi. Upalim i na zaslonu piše 28 — odmah se osjeća. Zadovoljna sam zlatnom bojom, kao na slikama.»"',
        '"faq4_a": "Da. Odvlaživanje uklanja višak pare: manje kondenzacije, manje mirisa zatvorenog prostora, brže suše se rublje."':
        '"faq4_a": "Da. Odvlaživanje uklanja višak pare: manje kondenzacije, manje mirisa zatvorenog prostora, rublje se brže suši."',
        '"form_h2": "Pošaljite upit sada, prije nego ponestane promotivni stock"':
        '"form_h2": "Pošaljite upit sada, prije nego ponestane promotivna zaliha"',
        '"ph_tel": "+385 91 123 4567"': '"ph_tel": "+385 91 234 5678"',
    },
    "locale_cs.py": {
        '"form_h2": "Odešlete poptávku teď, než dojde promo sklad"':
        '"form_h2": "Odešlete poptávku teď, než dojde promo zásoba"',
        '"faq4_q": "Pomáhá proti vlhkosti a plísní?"': '"faq4_q": "Pomáhá proti vlhkosti a plísni?"',
        "pálí peníze každou hodinu, i v prázdných místnostech":
        "spaluje peníze každou hodinu, i v prázdných místnostech",
    },
    "locale_sk.py": {
        '"form_h2": "Odošlite dopyt teraz, kým nedôjde promo sklad"':
        '"form_h2": "Odošlite dopyt teraz, kým nedôjde promo zásoba"',
        "pálí peniaze každú hodinu, aj v prázdných izbách":
        "spaluje peniaze každú hodinu, aj v prázdnych izbách",
        '"ph_name": "Ján Novák"': '"ph_name": "Peter Horváth"',
    },
    "locale_pl.py": {
        '"stock_l": "Ograniczony stock"': '"stock_l": "Ograniczona ilość"',
        '"form_h2": "Wyślij zapytanie teraz, zanim skończy się stock promocyjny"':
        '"form_h2": "Wyślij zapytanie teraz, zanim skończy się zapas promocyjny"',
        '"ph_addr": "ul. Marszałkowska 15, 00-626 Warszawa"':
        '"ph_addr": "ul. Marszałkowska 10, 00-590 Warszawa"',
    },
    "locale_lv.py": {
        "APMAKSA PIEGĀDES · BEZMAKSAS PIEGĀDE":
        "APMAKSA SAŅEMOT · BEZMAKSAS PIEGĀDE",
        '"why2_eye": "02 · VADĀT AR BALSS"': '"why2_eye": "02 · VADĪBA AR BALSI"',
        "bez salstēšanas": "nesalstot",
        '"ph_tel": "+371 21 234 567"': '"ph_tel": "+371 2123 4567"',
    },
    "locale_lt.py": {
        '"h1_mobile": "Mokate už viso namo šildymą, bet gyvenate viename kambaryje? Nuo šios vakaro galite sutaupyti nešalant."':
        '"h1_mobile": "Mokate už viso namo šildymą, bet gyvenate viename kambaryje? Nuo šio vakaro galite sutaupyti nešalant."',
        "perteklinę garą": "perteklinę drėgmę",
        "iš sofa": "nuo sofos",
    },
    "locale_hu.py": {
        '"why1_p2": "A meleg még sosem került ennyibe."':
        '"why1_p2": "A meleg még sosem került ilyen kevésbe."',
        '"ph_name": "Nagy Péter"': '"ph_name": "Nagy Péter"',
    },
    "locale_es.py": {
        '"why2_p1": "Sin mandos, sin levantarte de la cama. ZELTO™ se controla con voz, app o mando y mantiene la temperatura que te gusta."':
        '"why2_p1": "Sin mandos giratorios, sin levantarte de la cama. ZELTO™ se controla con voz, app o mando y mantiene la temperatura que te gusta."',
        '"ph_tel": "+34 612 34 56 78"': '"ph_tel": "+34 612 345 678"',
    },
    "locale_de.py": {
        '"rev1_p": "«Alles vom Set dabei, nichts fehlte. Im Wohnzimmer Stecker rein, sofort warm. Vom Sofa mit dem Handy»"':
        '"rev1_p": "«Alles vom Set war dabei, nichts fehlte. Im Wohnzimmer in die Steckdose — und es wird sofort warm. Vom Sofa steuere ich alles mit dem Handy.»"',
        '"rev2_p": "«Ich habe es selbst an die Wand montiert. Das Kabel geht direkt in die Steckdose, ohne sichtbare Leitungen. Einschalten — das Display zeigt 28 °C, und man spürt es sofort. Die goldene Farbe entspricht den Fotos.»"':
        '"rev2_p": "«Ich habe es selbst an die Wand montiert. Das Kabel geht direkt in die Steckdose, ohne sichtbare Leitungen. Einschalten — das Display zeigt 28 °C, und man spürt es sofort. Ich bin zufrieden mit der goldenen Farbe, genau wie auf den Fotos.»"',
        '"rev3_p": "«Im Schlafzimmer morgens immer kalt. Über die Tür, Steckdose seitlich. Thermometer an der Wand: 28 Grad, Raum ist warm»"':
        '"rev3_p": "«Im Schlafzimmer war es morgens immer kalt. Ich habe es über der Tür montiert, die Steckdose sitzt seitlich. Am Thermometer an der Wand stehen 28 Grad — der Raum ist angenehm warm.»"',
        '"ph_name": "Thomas Müller"': '"ph_name": "Anna Müller"',
        '"ph_addr": "Hauptstraße 10, 10115 Berlin"': '"ph_addr": "Hauptstraße 10, 80331 München"',
    },
    "locale_pt.py": {
        '"ph_addr": "Rua da Liberdade 45, 1250-096 Lisboa"':
        '"ph_addr": "Rua Augusta 10, 1100-053 Lisboa"',
    },
}


def main() -> None:
    for fname, reps in PATCHES.items():
        path = ROOT / fname
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in reps.items():
            if old not in text:
                print(f"WARN missing in {fname}: {old[:60]}...")
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"Updated {fname}")


if __name__ == "__main__":
    main()
