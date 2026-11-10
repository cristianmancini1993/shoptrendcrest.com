#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Seed TAIGOR phrase bundles and write _taigor_phrases_all.py.

LOCALE_PATCH (128 keys per geo, native copy) lives in _taigor_locale_patches.py,
sourced from scripts/_taigor_langs/{lt,es,pt,pl,cs,ro,sk,si,hr,hu,lv}.py.
DE uses the in-file DE master; all other geos use the full patch only (no IT fallback).
"""
from __future__ import annotations

import pprint
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _build_it_master() -> dict:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "_taigor_it_strings", ROOT / "_taigor_it_strings.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    s = mod.IT_STRINGS
    ty = s["ty_steps"]
    return {
        "footer": s["footer_blurb"],
        "title": s["title"],
        "description": s["description"],
        "og_title": s["og_title"],
        "og_description": s["og_description"],
        "topbar": s["topbar"],
        "rating": s["rating"],
        "gift": s["gift"],
        "h1": s["h1"],
        "lead": s["lead"],
        "alt_hero": s["alt_hero"],
        "cta": s["cta"],
        "f1_h": s["f1_h"],
        "f1_p": s["f1_p"],
        "f2_h": s["f2_h"],
        "f2_p": s["f2_p"],
        "f3_h": s["f3_h"],
        "f3_p": s["f3_p"],
        "f4_h": s["f4_h"],
        "f4_p": s["f4_p"],
        "form_h2_prefix": s["form_h2_prefix"],
        "form_p": s["form_p"],
        "submit_btn": s["submit_btn"],
        "form_note": s["form_note"],
        "ty1": ty[0],
        "ty2": ty[1],
        "ty3": ty[2],
        "why1_eye": s["why1_eye"],
        "why1_h": s["why1_h"],
        "why1_t3": s["why1_t3"],
        "why1_p1": s["why1_p1"],
        "why1_p2": s["why1_p2"],
        "why2_eye": s["why2_eye"],
        "why2_h": s["why2_h"],
        "why2_t2": s["why2_t2"],
        "why2_t3": s["why2_t3"],
        "why2_p1": s["why2_p1"],
        "why2_p2": s["why2_p2"],
        "why3_eye": s["why3_eye"],
        "why3_h": s["why3_h"],
        "why3_t1": s["why3_t1"],
        "why3_t2": s["why3_t2"],
        "why3_t3": s["why3_t3"],
        "why3_p1": s["why3_p1"],
        "why3_p2": s["why3_p2"],
        "why4_eye": s["why4_eye"],
        "why4_h": s["why4_h"],
        "why4_t1": s["why4_t1"],
        "why4_t2": s["why4_t2"],
        "why4_t3": s["why4_t3"],
        "why4_p1": s["why4_p1"],
        "why4_p2": s["why4_p2"],
        "compare_label": s["compare_label"],
        "compare_h": s["compare_h"],
        "cmp_th_gas": s["cmp_th_gas"],
        "cmp_row_start": s["cmp_row_start"],
        "cmp_gas_start": s["cmp_gas_start"],
        "cmp_win_start": s["cmp_win_start"],
        "cmp_row_power": s["cmp_row_power"],
        "cmp_gas_power": s["cmp_gas_power"],
        "cmp_win_power": s["cmp_win_power"],
        "cmp_row_weight": s["cmp_row_weight"],
        "cmp_gas_weight": s["cmp_gas_weight"],
        "cmp_win_weight": s["cmp_win_weight"],
        "cmp_row_perf": s["cmp_row_perf"],
        "cmp_gas_perf": s["cmp_gas_perf"],
        "cmp_win_perf": s["cmp_win_perf"],
        "cmp_row_cut": s["cmp_row_cut"],
        "cmp_gas_cut": s["cmp_gas_cut"],
        "cmp_win_cut": s["cmp_win_cut"],
        "cmp_row_auto": s["cmp_row_auto"],
        "cmp_gas_auto": s["cmp_gas_auto"],
        "cmp_win_auto": s["cmp_win_auto"],
        "cmp_row_oil": s["cmp_row_oil"],
        "cmp_gas_oil": s["cmp_gas_oil"],
        "cmp_win_oil": s["cmp_win_oil"],
        "cmp_row_kit": s["cmp_row_kit"],
        "cmp_gas_kit": s["cmp_gas_kit"],
        "cmp_win_kit": s["cmp_win_kit"],
        "testimonials_h": s["testimonials_h"],
        "rev1_h": s["rev1_h"],
        "rev1_p": s["rev1_p"],
        "rev2_h": s["rev2_h"],
        "rev2_p": s["rev2_p"],
        "rev3_h": s["rev3_h"],
        "rev3_p": s["rev3_p"],
        "kit_eye": s["kit_eye"],
        "kit_h": s["kit_h"],
        "kit_li1": s["kit_li1"],
        "kit_li2": s["kit_li2"],
        "kit_li3": s["kit_li3"],
        "kit_li4": s["kit_li4"],
        "kit_li5": s["kit_li5"],
        "kit_li6": s["kit_li6"],
        "kit_li7": s["kit_li7"],
        "kit_li8": s["kit_li8"],
        "faq_h": s["faq_h"],
        "faq1_q": s["faq1_q"],
        "faq1_a": s["faq1_a"],
        "faq2_q": s["faq2_q"],
        "faq2_a": s["faq2_a"],
        "faq3_q": s["faq3_q"],
        "faq3_a": s["faq3_a"],
        "faq4_q": s["faq4_q"],
        "faq4_a": s["faq4_a"],
        "faq5_q": s["faq5_q"],
        "faq5_a": s["faq5_a"],
        "faq6_q": s["faq6_q"],
        "faq6_a": s["faq6_a"],
        "faq7_q": s["faq7_q"],
        "faq7_a": s["faq7_a"],
        "faq8_q": s["faq8_q"],
        "faq8_a": s["faq8_a"],
        "faq9_q": s["faq9_q"],
        "faq9_a": s["faq9_a"],
        "faq10_q": s["faq10_q"],
        "faq10_a": s["faq10_a"],
        "faq11_q": s["faq11_q"],
        "faq11_a": s["faq11_a"],
        "alt_b1": s["alt_b1"],
        "alt_b2": s["alt_b2"],
        "alt_b3": s["alt_b3"],
        "alt_b4": s["alt_b4"],
        "alt_r1": s["alt_r1"],
        "alt_r2": s["alt_r2"],
        "alt_r3": s["alt_r3"],
        "alt_kit": s["alt_kit"],
        "alt_client": s["alt_client"],
    }


IT = _build_it_master()

# German master copy — human-written product strings.
DE = {
    "footer": "Nützliche Produkte für den Alltag, Lieferung in 24–48 Stunden mit Zahlung per Nachnahme.",
    "title": "TAIGOR™ | Akku-Kettensäge Brushless 1600 W mit Doppelakku — 50 % Rabatt",
    "description": "TAIGOR™: Akku-Kettensäge brushless 1600 W, 45 cm Schwert, zwei Akkus für bis zu 12 Stunden Laufzeit. Automatische Ölung, Komplettset, Barzahlung beim Kurier.",
    "og_title": "TAIGOR™ — Akku-Kettensäge 1600 W zum halben Preis",
    "og_description": "Holz und Äste bis 45 cm ohne Benzin: brushless 1600 W, 2 Akkus, bis zu 12 h. Nachnahme in ganz Deutschland.",
    "topbar": "AKTION · −50 % · KOSTENLOSER VERSAND · BARZAHLUNG BEIM KURIER",
    "rating": "<strong>Lieferung 24–48 h</strong> in Deutschland · <strong>Nachnahme</strong> bei Zustellung",
    "gift": "🎁 Inklusive: 2 Akkus, Schnellladegerät und Zubehör im Set",
    "h1": "Holz, Hecken und Äste ohne Kabel und Mischung schneiden: TAIGOR™ brushless mit 1600 W",
    "lead": "Brushless-Motor, zwei Lithium-Akkus und 45 cm Schwert für Brennholz, Baumschnitt und Gartenpflege. Ein Knopf — kein Starterseil, kein Benzintank, kein Verlängerungskabel.",
    "alt_hero": "TAIGOR™ Akku-Kettensäge mit Doppelakku, Ladegerät, Ketten, Handschuhen und Tasche",
    "cta": "TAIGOR™ FÜR {price} KAUFEN →",
    "f1_h": "Kostenloser Versand",
    "f1_p": "Lieferung nach Hause in Deutschland",
    "f2_h": "Nachnahme",
    "f2_p": "Keine Karte, keine Vorauszahlung",
    "f3_h": "2 Jahre Garantie",
    "f3_p": "Offizielle Herstellergarantie inklusive",
    "f4_h": "30 Tage Rückgabe",
    "f4_p": "Volle Erstattung, wenn es nicht passt",
    "form_h2_prefix": "TAIGOR™ anfragen für",
    "form_p": "Name, Telefon und Adresse eintragen. Wir rufen innerhalb von 24 Stunden an und planen die Lieferung — bezahlt wird nur bar beim Kurier.",
    "submit_btn": "BESTELLUNG BESTÄTIGEN — ZAHLE BEIM KURIER",
    "form_note": "💶 Keine Vorauszahlung: Sie zahlen bar beim Kurier bei Erhalt",
    "ty1": "Nehmen Sie den Anruf entgegen und <strong>bestätigen Sie Ihre Daten</strong>",
    "ty2": "Versand innerhalb von <strong>24–48 Stunden</strong> nach telefonischer Bestätigung",
    "ty3": "Lieferung nach Hause und <strong>Zahlung per Nachnahme</strong> ({price})",
    "why1_eye": "01 · Brushless 1600 W",
    "why1_h": "Stabile Leistung auch bei dichtem Holz, mit weniger Vibration",
    "why1_t3": "Konstantes Drehmoment",
    "why1_p1": "Der 1600-W-Brushless hält die Kraft, wenn der Durchmesser wächst: TAIGOR™ geht in den Stamm und fällt nicht in der Mitte des Schnitts ab.",
    "why1_p2": "Weniger Überhitzung, wenig Wartung — ein Gerät für Holz, Schnitt und Sturmäste.",
    "why2_eye": "02 · Doppelakku, bis zu 12 Stunden",
    "why2_h": "Lange Einsätze ohne ständiges Nachfüllen",
    "why2_t2": "Bis zu 12 Stunden",
    "why2_t3": "Schneller Akkuwechsel",
    "why2_p1": "Zwei leistungsstarke Lithium-Akkus liefern bis zu 12 Stunden Gesamtlaufzeit: Holz stapeln, Garten erledigen — ohne Dauerpause am Ladegerät.",
    "why2_p2": "Akkutausch in Sekunden. Schluss mit Mischung, Kanistern und Verlängerungskabeln.",
    "why3_eye": "03 · 45 cm Schwert · ca. 2 kg",
    "why3_h": "Leichtes Gewicht, präzise Schnittführung",
    "why3_t1": "Gehärtete Stahlschiene",
    "why3_t2": "Ca. 2 kg",
    "why3_t3": "Sauberer Schnitt",
    "why3_p1": "Mit 45 cm Schwert schneiden Sie Stämme und dicke Äste bis 45 cm Durchmesser. Etwa 2 kg in der Hand — weniger Ermüdung auch nach einer Stunde.",
    "why3_p2": "Start per Knopf wie eine Bohrmaschine: auch Einsteiger sind in Minuten sicher unterwegs.",
    "why4_eye": "04 · Auto-Ölung · Komplettset",
    "why4_h": "Kette immer geölt, Karton sofort einsatzbereit",
    "why4_t1": "Automatische Schmierung",
    "why4_t2": "Ersatzketten",
    "why4_t3": "Alles dabei",
    "why4_p1": "Der integrierte Tank ölt die Kette beim Arbeiten: ruhiger Lauf, weniger Verschleiß. Im Karton: Schnelllader, Ersatzketten, Handschuhe und Pflegezubehör.",
    "why4_p2": "Akkus laden, Öl einfüllen, loslegen.",
    "compare_label": "Schnellvergleich",
    "compare_h": "Benzin oder Akku? TAIGOR™ vs klassische Kettensäge",
    "cmp_th_gas": "Benzin-Kettensäge",
    "cmp_row_start": "Start",
    "cmp_gas_start": "Starterseil immer wieder ziehen",
    "cmp_win_start": "Ein Knopf",
    "cmp_row_power": "Antrieb",
    "cmp_gas_power": "Mischung, Abgase, Lärm",
    "cmp_win_power": "Lithium, null Emissionen",
    "cmp_row_weight": "Gewicht",
    "cmp_gas_weight": "Belastet Arme und Schultern",
    "cmp_win_weight": "Ca. 2 kg",
    "cmp_row_perf": "Leistung",
    "cmp_gas_perf": "Schwächelt bei Hartholz",
    "cmp_win_perf": "Brushless 1600 W, konstantes Drehmoment",
    "cmp_row_cut": "Schnittkapazität",
    "cmp_gas_cut": "Schwierig bei dicken Stücken",
    "cmp_win_cut": "Bis 45 cm Durchmesser",
    "cmp_row_auto": "Laufzeit",
    "cmp_gas_auto": "Pausen zum Betanken",
    "cmp_win_auto": "2 Akkus, bis zu 12 h",
    "cmp_row_oil": "Schmierung",
    "cmp_gas_oil": "Manuelle Einstellung",
    "cmp_win_oil": "Automatisch aus Tank",
    "cmp_row_kit": "Zubehör",
    "cmp_gas_kit": "Oft extra kostenpflichtig",
    "cmp_win_kit": "Akkus, Ladegerät, Tasche, Handschuhe, Ketten",
    "testimonials_h": "Das sagen Käufer nach dem Test",
    "rev1_h": "Gibt bei harten Stämmen nicht nach.",
    "rev1_p": "«Für Brennholz und Gartenarbeit. Geht tief rein, der Motor hält auch bei dicken Stücken die Leistung.»",
    "rev2_h": "Zwei Akkus machen den Tag.",
    "rev2_p": "«Ich wechsle die Akkus und schaffe mehr, ohne Benzinstopps oder Steckdose am Ende des Gartens.»",
    "rev3_h": "Komplett geliefert, nichts fehlt.",
    "rev3_p": "«Akkus, Ladegerät, Ketten und Handschuhe drin. Sofort an dicke Äste — handlich und präzise.»",
    "kit_eye": "Lieferumfang",
    "kit_h": "Komplettes TAIGOR™-Set zum Festpreis",
    "kit_li1": "TAIGOR™ Akku-Kettensäge — brushless 1600 W, 45 cm Schwert",
    "kit_li2": "2 Hochleistungs-Lithium-Akkus (bis zu 12 h gesamt)",
    "kit_li3": "Schnellladegerät",
    "kit_li4": "Hartschalen-Tasche für Lagerung und Transport",
    "kit_li5": "Ersatzketten",
    "kit_li6": "Arbeitshandschuhe und Pflegeset",
    "kit_li7": "Integrierte automatische Kettenschmierung",
    "kit_li8": "Offizielle 2-Jahres-Garantie",
    "faq_h": "Häufige Fragen",
    "faq1_q": "Wie lange dauert die Lieferung?",
    "faq1_a": "In der Regel 24–48 Stunden. Innerhalb von 24 Stunden nach Bestellung rufen wir an und vereinbaren den Termin.",
    "faq2_q": "Muss ich online zahlen?",
    "faq2_a": "Nein. {price} bar beim Kurier, wenn TAIGOR™ geliefert wird.",
    "faq3_q": "Geeignet ohne Kettensägen-Erfahrung?",
    "faq3_a": "Ja: Start per Knopf, kein Seil, keine Mischung. Handschuhe und Schutzbrille tragen, Anleitung lesen — in wenigen Minuten sicher.",
    "faq4_q": "Wie schwer? Auch für Frauen oder Senioren?",
    "faq4_a": "Ca. 2 kg — deutlich leichter als Benzinsägen, gut für längere Schnittarbeiten.",
    "faq5_q": "Für Obstgarten und Hecken?",
    "faq5_a": "Ja. Leicht und kabellos, kommt zwischen Ästen durch; schneidet bis ca. 45 cm Stärke.",
    "faq6_q": "Maximaler Schnittdurchmesser?",
    "faq6_a": "Äste und Stämme bis ca. 45 cm, je nach Holz und Technik.",
    "faq7_q": "Wie lange halten beide Akkus?",
    "faq7_a": "Bis zu 12 Stunden kombiniert, abhängig von Holzhärte und Einsatz.",
    "faq8_q": "Welches Kettenöl?",
    "faq8_a": "Standard-Kettensägenöl aus dem Fachhandel. In den Tank füllen — Schmierung läuft automatisch.",
    "faq9_q": "Kette verschlissen?",
    "faq9_a": "Ersatzkette aus dem Set montieren — wenige Minuten, ohne Spezialwerkzeug.",
    "faq10_q": "Was ist in der Box?",
    "faq10_a": "TAIGOR™, 2 Akkus, Schnelllader, Tasche, Ersatzketten, Handschuhe und Pflegezubehör.",
    "faq11_q": "Nicht überzeugt — Rückgabe?",
    "faq11_a": "30 Tage kostenlose Rückgabe mit voller Erstattung.",
    "alt_b1": "TAIGOR™ beim Stamm-Schnitt",
    "alt_b2": "Doppel-Akku für TAIGOR™",
    "alt_b3": "45 cm Schwert TAIGOR™ im Einsatz",
    "alt_b4": "Automatische Kettenschmierung TAIGOR™",
    "alt_r1": "TAIGOR™ an dickem Stamm",
    "alt_r2": "TAIGOR™ mit Brennholz",
    "alt_r3": "TAIGOR™ Set-Inhalt",
    "alt_kit": "TAIGOR™ Komplettset",
    "alt_client": "Kunde",
}

# Full native phrase bundles (128 keys each) — see _taigor_langs/*.py
from _taigor_locale_patches import LOCALE_PATCH  # noqa: E402

LANGS = ["it", "lt", "es", "pt", "pl", "cs", "ro", "sk", "si", "hr", "hu", "de", "lv"]


def merge_lang(code: str) -> dict:
    if code == "de":
        return dict(DE)
    if code not in LOCALE_PATCH:
        raise KeyError(f"No LOCALE_PATCH for {code}")
    patch = dict(LOCALE_PATCH[code])
    missing = set(IT.keys()) - set(patch.keys())
    if missing:
        raise KeyError(
            f"{code} LOCALE_PATCH missing {len(missing)} keys, e.g. {sorted(missing)[:5]}"
        )
    return patch


def main() -> None:
    phrases = {code: merge_lang(code) for code in LANGS}
    out = ROOT / "_taigor_phrases_all.py"
    text = (
        "# -*- coding: utf-8 -*-\n"
        '"""TAIGOR phrase bundles per locale (merged from DE master + patches)."""\n\n'
        "PHRASES = "
        + pprint.pformat(phrases, width=100, sort_dicts=False)
        + "\n"
    )
    out.write_text(text, encoding="utf-8")
    core = ROOT / "_taigor_locale_core.py"
    core.write_text(
        "# -*- coding: utf-8 -*-\n"
        'from _taigor_assemble import build_locale\n'
        "from _taigor_phrases_all import PHRASES\n\n"
        "TAIGOR_CORE = {code: build_locale(PHRASES[code]) for code in PHRASES}\n",
        encoding="utf-8",
    )
    print(f"Wrote {out} and {core}")


if __name__ == "__main__":
    main()
