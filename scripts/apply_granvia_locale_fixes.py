#!/usr/bin/env python3
"""Apply buyer QA fixes to content/granvia/locales and IT strings."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "content/granvia/locales"

from _granvia_form_examples import GRANVIA_FORM_EXAMPLES, GRANVIA_NAME_LABEL_OVERRIDES

PLACEHOLDERS = GRANVIA_FORM_EXAMPLES

TY_BADGE_24 = {
    "es": "🛡️ Garantía de 24 meses",
    "pt": "🛡️ Garantia de 24 meses",
    "de": "🛡️ 24 Monate Garantie",
    "lt": "🛡️ 24 mėnesių garantija",
    "hu": "🛡️ 24 hónap garancia",
    "cs": "🛡️ Záruka 24 měsíců",
}

F1_P = {
    "es": "Hasta 5 kg de carne",
    "pt": "Até 5 kg de carne",
    "de": "Bis zu 5 kg Fleisch",
    "lt": "Iki 5 kg mėsos",
    "hu": "Akár 5 kg hús",
    "cs": "Až 5 kg masa",
    "it": "Fino a 5 kg di carne",
}

KIT_LI6 = {
    "it": "Set di tamburi per grattugiare e affettare verdure",
    "es": "Juego de tambores para rallar y cortar verduras",
    "pt": "Conjunto de tambores para ralar e fatiar legumes",
    "de": "Trommelset zum Reiben und Schneiden von Gemüse",
    "lt": "Būgnelių rinkinys daržovių trinimui ir skutimui",
    "hu": "Dobkészlet zöldségreszeléshez és szeleteléshez",
    "cs": "Sada bubnů na strouhání a krájení zeleniny",
}

KIT_LI7 = {
    "it": "Accessorio per kibbe",
    "es": "Accesorio para kibbe",
    "pt": "Acessório para kibbe",
    "de": "Kibbe-Aufsatz",
    "lt": "Kibės gaminimo priedas",
    "hu": "Kibbe tartozék",
    "cs": "Příslušenství pro kibbe",
}


def load(code: str) -> dict:
    return json.loads((LOCALES / f"{code}.json").read_text(encoding="utf-8"))


def save(code: str, data: dict) -> None:
    (LOCALES / f"{code}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_lt(d: dict) -> None:
    repl = {
        "Elektrinis mėsmale": "Elektrinė mėsmalė",
        "elektrinis mėsmale": "elektrinė mėsmalė",
        "Senas mėsmale": "Sena mėsmalė",
        "senas mėsmale": "sena mėsmalė",
        "SENAS MĖSMALE": "SENA MĖSMALĖ",
        "Paprastas mėsmale": "Paprasta mėsmalė",
        "paprasto mėsmalio": "paprastos mėsmalės",
        "Šviežiai malti mėsa": "Šviežiai malta mėsa",
        "šviežiai malti mėsa": "šviežiai malta mėsa",
        "Pagaliau malti mėsa kaip mums patinka": "Pagaliau malta mėsa tokia, kokią mėgstame",
        "Malia greitai": "Mala greitai",
        "malia be problemų": "mala be problemų",
        "prieskoniais, kurių mėgsta vaikai": "prieskoniais, kuriuos mėgsta vaikai",
        "neišardydami viso mėsmalio": "neišardydami visos mėsmalės",
        "Dešrų pildymo priedas į komplektą": "Dešrų kimšimo priedas įtrauktas į komplektą",
        "dešrų pildymo priedas": "dešrų kimšimo priedas",
        "Dešrų pildymo priedas": "Dešrų kimšimo priedas",
        "DEŠRŲ PILDYMO PRIEDAS": "DEŠRŲ KIMŠIMO PRIEDAS",
        "Trauktuvė": "Padavimo lovelis",
        "trauktuvė": "padavimo lovelis",
        "Ramunė malia": "Ramunė mala",
        "MĖSMALEI": "MĖSMALĖS",
        "mėsmalio komplektas": "mėsmalės komplektas",
    }
    for k, v in list(d.items()):
        if isinstance(v, str):
            s = v
            for a, b in repl.items():
                s = s.replace(a, b)
            d[k] = s
        elif isinstance(v, list):
            d[k] = [x.replace("mėsmale", "mėsmalė").replace("mėsmalio", "mėsmalės") if isinstance(x, str) else x for x in v]


def patch_hu(d: dict) -> None:
    d["why1_p1"] = d["why1_p1"].replace(
        "A 2600 W-os motor nagy húsmennyiséget is könnyen megbirkózik.",
        "A 2600 W-os motor nagy mennyiségű hússal is könnyen megbirkózik.",
    )
    d["rev1_p"] = d["rev1_p"].replace("hamburgeret", "hamburgert")
    if "ragu-ba" in d.get("why1_p1", ""):
        d["why1_p1"] = d["why1_p1"].replace("ragu-ba", "raguba")
    for k in d:
        if isinstance(d[k], str):
            d[k] = (
                d[k]
                .replace("Írjon a info@shoptrendcrest.com címre", "Írjon az info@shoptrendcrest.com címre")
                .replace("Toló", "Tömőrúd")
                .replace("toló", "tömőrúd")
                .replace("Reverse funkció", "Visszaforgató funkció")
                .replace("reverse funkció", "visszaforgató funkció")
                .replace("reverse funkciót", "visszaforgató funkciót")
            )


def patch_cs(d: dict) -> None:
    d["why3_eye"] = "03 — Granvia™: pohodlné používání a snadná údržba"
    for k in d:
        if isinstance(d[k], str):
            d[k] = (
                d[k]
                .replace("Melo rychle", "Mele rychle")
                .replace("melo bez problémů", "mele bez problémů")
                .replace("kompletní sada, připraveno k použití", "kompletní sada, připravená k použití")
            )
    d["why3_t2"] = "Pěchovadlo"
    d["why3_p1"] = d["why3_p1"].replace("píst", "pěchovadlo").replace("Píst", "Pěchovadlo")
    d["kit_li4"] = d["kit_li4"].replace("píst", "pěchovadlo")
    d["cmp_win_block"] = "Zpětný chod"
    d["why3_t1"] = "Zpětný chod"
    d["faq4_a"] = "Použijte zpětný chod a uvolněte mechanismus bez rozebrání celého mlýnku."
    for k in d:
        if isinstance(d[k], str):
            d[k] = (
                d[k]
                .replace("Funkce reverse", "Zpětný chod")
                .replace("funkci reverse", "zpětný chod")
                .replace("funkce reverse", "zpětný chod")
                .replace("Plnící nástavec", "Plnicí nástavec")
                .replace("plnící nástavec", "plnicí nástavec")
                .replace("Platíte kurýru", "Platíte kurýrovi")
                .replace("zaplatíte kurýru", "zaplatíte kurýrovi")
            )


def patch_de(d: dict) -> None:
    for k in d:
        if isinstance(d[k], str):
            d[k] = (
                d[k]
                .replace("wolfert", "verarbeitet")
                .replace("Wolfarten", "Mahlgrade")
                .replace("Schwacher oder manueller Motor", "Schwacher Motor oder Handbetrieb")
                .replace("löst die Reverse-Funktion den Mechanismus", "hilft die Rücklauffunktion, die Blockade zu lösen")
                .replace("Reverse-Funktion", "Rücklauffunktion")
                .replace("Reverse-Funktion,", "Rücklauffunktion,")
            )


def patch_pt(d: dict) -> None:
    d["rev2_p"] = d["rev2_p"].replace(
        "as especiarias que os meus filhos gostam",
        "as especiarias de que os meus filhos gostam",
    )
    for k in d:
        if isinstance(d[k], str):
            d[k] = d[k].replace("função reverse", "função de marcha-atrás").replace("Função reverse", "Função de marcha-atrás")


def patch_es(d: dict) -> None:
    for k in d:
        if isinstance(d[k], str):
            d[k] = d[k].replace("función reverse", "función de marcha atrás").replace("Función reverse", "Función de marcha atrás")


def main() -> None:
    for code in ("es", "pt", "de", "lt", "hu", "cs", "it"):
        d = load(code)
        if code in F1_P:
            d["f1_p"] = F1_P[code]
        if code in TY_BADGE_24:
            badges = list(d["ty_badges"])
            badges[1] = TY_BADGE_24[code]
            d["ty_badges"] = badges
        if code in KIT_LI6:
            d["kit_li6"] = KIT_LI6[code]
            d["kit_li7"] = KIT_LI7[code]
        if code in PLACEHOLDERS:
            d.update(PLACEHOLDERS[code])
        if code in GRANVIA_NAME_LABEL_OVERRIDES:
            d["label_name"] = GRANVIA_NAME_LABEL_OVERRIDES[code]
        if code == "lt":
            patch_lt(d)
        if code == "hu":
            patch_hu(d)
        if code == "cs":
            patch_cs(d)
        if code == "de":
            patch_de(d)
        if code == "pt":
            patch_pt(d)
        if code == "es":
            patch_es(d)
        save(code, d)
        print("updated", code)

    # Sync _granvia_it_strings ty_badges middle item for template match
    it_strings = ROOT / "scripts" / "_granvia_it_strings.py"
    text = it_strings.read_text(encoding="utf-8")
    text = text.replace("🛡️ Garanzia produttore", "🛡️ Garanzia 24 mesi")
    text = text.replace('"f1_p": "Fino a 5 kg di carne per sessione"', '"f1_p": "Fino a 5 kg di carne"')
    if "kit_li6" not in text:
        text = text.replace(
            '"kit_li5": "Manuale di istruzioni e garanzia del produttore",',
            '"kit_li5": "Manuale di istruzioni e garanzia del produttore",\n'
            '    "kit_li6": "Set di tamburi per grattugiare e affettare verdure",\n'
            '    "kit_li7": "Accessorio per kibbe",',
        )
    it_strings.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
