# -*- coding: utf-8 -*-
"""One-off content fixes for FLAMORA fireplace locale JSON files."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "locales" / "flamora_fireplace"

W1_P = {
    "pl": "W dedykowanej aplikacji ustawiasz żądaną temperaturę, a bieżącą temperaturę pokoju widzisz na ekranie. Sterujesz też włączeniem, efektem płomienia, trybem pracy i timerem. Pilot powiela funkcje i dodaje blokadę przycisków.",
    "cs": "Ve vlastní aplikaci nastavíte požadovanou teplotu a na displeji vidíte aktuální teplotu v místnosti. Ovládáte také zapnutí, efekt plamene, režim a časovač. Ovladač kopíruje funkce a přidává zámek tlačítek.",
    "es": "En la app dedicada ajustas la temperatura deseada y ves la temperatura actual de la habitación en pantalla. También controlas el encendido, el efecto llama, el modo y el temporizador. El mando repite las funciones y añade el bloqueo de botones.",
    "pt": "Na app dedicada define a temperatura pretendida e vê no ecrã a temperatura atual da divisão. Também controla o ligar/desligar, o efeito chama, o modo e o temporizador. O comando repete as funções e acrescenta o bloqueio de botões.",
    "de": "In der App stellen Sie die gewünschte Temperatur ein und sehen die aktuelle Raumtemperatur auf dem Display. Außerdem steuern Sie Ein/Aus, Flammeneffekt, Betriebsmodus und Timer. Die Fernbedienung bietet dieselben Funktionen plus Tastensperre.",
    "hu": "A dedikált alkalmazásban beállítja a kívánt hőmérsékletet, és a kijelzőn látja a szoba aktuális hőmérsékletét. Kezeli a be/kikapcsolást, a lángeffektet, az üzemmódot és az időzítőt. A távirányító ugyanezeket adja, plusz gombzárat.",
    "sk": "Vo vlastnej aplikácii nastavíte požadovanú teplotu a na displeji vidíte aktuálnu teplotu v miestnosti. Ovládate aj zapnutie, efekt plameňa, režim a časovač. Ovládač kopíruje funkcie a pridáva zámok tlačidiel.",
    "lv": "Īpašajā lietotnē iestatāt vēlamo temperatūru un ekrānā redzat faktisko istabas temperatūru. Vadāt arī ieslēgšanu, liesmas efektu, darba režīmu un taimeri. Tālvadība atkārto funkcijas un pievieno pogu bloķēšanu.",
}

W3_I = {
    "pl": "Szczegóły techniczne znajdziesz w instrukcji obsługi.",
    "cs": "Technické podrobnosti najdete v návodu k použití.",
    "es": "Los detalles técnicos están en el manual de uso.",
    "pt": "Os detalhes técnicos estão no manual de utilização.",
    "de": "Technische Details finden Sie in der Bedienungsanleitung.",
    "hu": "A technikai részleteket a használati útmutató tartalmazza.",
    "sk": "Technické podrobnosti nájdete v návode na použitie.",
    "lv": "Tehniskās detaļas ir lietošanas rokasgrāmatā.",
}


def load(lang: str) -> dict:
    path = ROOT / f"{lang}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def save(lang: str, data: dict) -> None:
    path = ROOT / f"{lang}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_all() -> None:
    for lang in W1_P:
        d = load(lang)
        d["w1_p"] = W1_P[lang]
        d["w3_i"] = W3_I[lang]
        save(lang, d)

    pl = load("pl")
    pl["gift"] = "🎁 W PREZENCIE: PILOT + APLIKACJA STERUJĄCA"
    pl["w3_p"] = (
        "Na ekranie aplikacji widzisz ustawioną wartość i rzeczywistą temperaturę w pokoju. "
        "Timer określa czas pracy; blokada na pilocie chroni przed przypadkowymi naciśnięciami."
    )
    pl["cmp_label"] = "Wolnostojący kominek elektryczny, nie na paliwo"
    pl["cmp_r3_b"] = "Wolnostojący, przenośny"
    pl["w3_h"] = "Ustaw godzinę i temperaturę bez konieczności pozostawiania kominka stale włączonego"
    pl["ty_s2"] = "Zamówienie zostanie przygotowane w ciągu <strong>24–48 godzin</strong>"
    save("pl", pl)

    de = load("de")
    de["rating"] = "<strong>4,8/5</strong> — Über <strong>8.730</strong> Menschen haben sich bereits für einen Elektrokamin fürs Wohnzimmer entschieden"
    de["w2_i"] = de["w2_i"].replace("die hintere Lüftungsgitter", "das hintere Lüftungsgitter")
    de["w3_h"] = "Zeit und Temperatur programmieren, ohne den Kamin ständig eingeschaltet zu lassen"
    save("de", de)

    hu = load("hu")
    hu["w3_p"] = "Az alkalmazás képernyőjén látja a beállított értéket és a szoba valós hőmérsékletét. Az időzítő a futásidőt határozza meg; a távirányító gombzárja megakadályozza a véletlen gombnyomásokat."
    hu["w2_p"] = hu["w2_p"].replace("a vitrin alatt", "az ott található vitrin alatt")
    hu["alt_w2"] = hu["alt_w2"].replace("láng effekt", "lángeffekt")
    hu["w2_eye"] = hu["w2_eye"].replace("Láng effekt", "Lángeffekt")
    hu["faq5_a"] = hu["faq5_a"].replace("a ott", "az ott")
    hu["og_desc"] = hu["og_desc"].replace("Láng effekt", "Lángeffekt")
    hu["f1_p"] = hu["f1_p"].replace("láng effektet", "lángeffektet")
    hu["cmp_r5_l"] = "Csak lángeffekt"
    hu["t3_p"] = hu["t3_p"].replace("fal munka nélkül", "falátalakítás nélkül")
    hu["w2_h"] = "Valósághű lánghatás, égés nélkül"
    hu["kit_i2"] = "LED-es lángszimuláció dekoratív fahasábokkal"
    save("hu", hu)

    cs = load("cs")
    cs["f4_p"] = "Platíte kurýrovi při doručení"
    cs["faq2_a"] = cs["faq2_a"].replace("kurýru", "kurýrovi")
    cs["w3_h"] = "Nastavte čas a teplotu bez nutnosti nechávat krb stále zapnutý"
    cs["cmp_label"] = "Volně stojící elektrický krb bez spalování"
    save("cs", cs)

    sk = load("sk")
    sk["f4_p"] = "Platíte kuriérovi pri doručení"
    sk["faq2_a"] = sk["faq2_a"].replace("kuriéru", "kuriérovi")
    sk["faq4_a"] = sk["faq4_a"].replace("právných", "právnych")
    sk["w2_i"] = "Postavíte ho, kde chcete, zapojíte a používate — nie sú potrebné úpravy steny, nechajte voľnú zadnú ventilačnú mriežku."
    sk["t3_p"] = (
        "«So zapnutým LED plameňom vyzerá ako skutočný krb — hostia sa naň pozerajú. "
        "Biely stĺp sa hodí do obývačky a nie sú potrebné úpravy steny.»"
    )
    save("sk", sk)

    es = load("es")
    es["f2_p"] = "Encendido/apagado, llama, temporizador, ventilador, bloqueo infantil y temperatura"
    es["cmp_r3_b"] = "De pie, portátil"
    save("es", es)

    pt = load("pt")
    pt["w2_p"] = pt["w2_p"].replace("sob a vitrine", "sob o vidro")
    pt["label_name"] = "Nome completo*"
    pt["label_addr"] = "Morada*"
    pt["ph_name"] = "Ana Silva"
    pt["ph_addr"] = "Rua Augusta 10, 1100-053 Lisboa"
    pt["cmp_label"] = "Lareira elétrica de instalação livre, sem combustão"
    pt["cmp_r3_b"] = "De instalação livre, portátil"
    save("pt", pt)

    lv = load("lv")
    text = json.dumps(lv, ensure_ascii=False)
    text = text.replace("kamīnzāle", "kamīns")
    text = text.replace("kamīnzāli", "kamīnu")
    text = text.replace("Kamīnzāle", "Kamīns")
    text = text.replace("kamīnzāles", "kamīna")
    text = text.replace("TĀLVADĪBAS PULS", "TĀLVADĪBAS PULTS")
    text = text.replace("gluds apdares", "gluda apdare")
    text = text.replace("formularā", "veidlapā")
    text = text.replace("Elektriskā kamīns", "Elektriskais kamīns")
    text = text.replace("elektriskā kamīns", "elektriskais kamīns")
    text = text.replace("Balta kamīns", "Balts kamīns")
    text = text.replace("Stāvoša kamīns", "Stāvošs kamīns")
    text = text.replace("Pasūtiet kamīns", "Pasūtiet kamīnu")
    lv = json.loads(text)
    lv["title"] = "FLAMORA™ — Elektriskais kamīns ar lietotni un tālvadību | {price}"
    lv["meta_desc"] = "Brīvi stāvošs elektriskais kamīns ar LED liesmu, lietotni un tālvadības pulti. {price}, apmaksa pie piegādes Latvijā."
    lv["og_title"] = "FLAMORA™ — Elektriskais kamīns ar lietotni un tālvadību"
    lv["alt_hero"] = "FLAMORA elektriskais kamīns ar lietotni un tālvadību"
    lv["form_h2"] = "Pasūtiet kamīnu par {price}"
    lv["rating"] = "<strong>4,8/5</strong> — Vairāk nekā <strong>8 730</strong> cilvēku jau izvēlējušies elektrisko kamīnu viesistabai"
    lv["lead"] = lv["lead"].replace("kamīns ir gatava", "kamīns ir gatavs")
    lv["alt_kit"] = "Elektriskais kamīns ar lietotni un tālvadību"
    lv["kit_i1"] = "Balts brīvi stāvošs elektriskais kamīns, gluda apdare"
    lv["alt_t3"] = "Brīvi stāvošs kamīns viesistabā, priekšskats"
    lv["t2_p"] = "«Balts kamīns, tālvadība un rokasgrāmata kopā. Pēc kastes atvēršanas novietoju viesistabā: tālvadība jau gatava liesmai un siltumam.»"
    lv["alt_w3"] = lv["alt_w3"].replace("kamīnss", "kamīna")
    lv["cmp_label"] = "Brīvi stāvošs elektriskais kamīns bez degšanas"
    lv["cmp_h2"] = "Malkas kamīns vai brīvi stāvošs elektriskais kamīns?"
    lv["th_elec"] = "Elektriskais"
    lv["cmp_r3_b"] = "Brīvi uz grīdas, pārvietojams"
    save("lv", lv)


if __name__ == "__main__":
    patch_all()
    print("patched locale JSON files")
