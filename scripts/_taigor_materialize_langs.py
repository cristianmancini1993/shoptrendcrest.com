#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write remaining locale PATCH files from PL/ES masters + native lexical passes."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "_taigor_langs"


def load(name: str) -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.PATCH)


def apply_repl(src: dict[str, str], pairs: list[tuple[str, str]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for k, v in src.items():
        s = v
        for a, b in pairs:
            s = s.replace(a, b)
        out[k] = s
    return out


def write(code: str, patch: dict[str, str]) -> None:
    (ROOT / f"{code}.py").write_text(
        "# -*- coding: utf-8 -*-\nPATCH = " + repr(patch) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    pl = load("pl")
    es = load("es")

    # Czech from Polish (Slavic, adapted)
    cs_pairs = [
        ("Przydatne produkty na co dzień", "Praktické produkty pro každý den"),
        ("dostawa w 24–48 h z płatnością przy odbiorze", "doručení za 24–48 h s platbou na dobírku"),
        ("Piła łańcuchowa", "Motorová pila"),
        ("piła łańcuchowa", "motorová pila"),
        ("Polsce", "Česku"),
        ("w Polsce", "v Česku"),
        ("PROMOCJA", "AKCE"),
        ("DARMOWA DOSTAWA", "DOPRAVA ZDARMA"),
        ("PŁACISZ GOTÓWKĄ KURIEROWI", "PLATÍTE HOTOVĚ KURÝROVI"),
        ("Płatność przy odbiorze", "Dobírka"),
        ("płatnością przy odbiorze", "platbou na dobírku"),
        ("Dostawa 24–48 h", "Doručení 24–48 h"),
        ("Dostawa do domu", "Doručení domů"),
        ("Darmowa dostawa", "Doprava zdarma"),
        ("Bez karty, bez zaliczki", "Bez karty, bez zálohy"),
        ("Gwarancja 2 lata", "Záruka 2 roky"),
        ("Zwrot 30 dni", "Vrácení 30 dní"),
        ("Zamów", "Objednejte"),
        ("KUP TAIGOR™ ZA", "KOUPTE TAIGOR™ ZA"),
        ("POTWIERDŹ ZAMÓWIENIE — PŁACĘ KURIEROWI", "POTVRĎTE OBJEDNÁVKU — PLATÍM KURÝROVI"),
        ("gotówką kurierowi", "hotově kurýrovi"),
        ("Oddzwonimy", "Zavoláme"),
        ("Wysyłka", "Odeslání"),
        ("godzin", "hodin"),
        ("potwierdzeniu telefonicznym", "telefonickém potvrzení"),
        ("Tnij drewno", "Řežte dřevo"),
        ("żywopłoty", "ploty"),
        ("gałęzie", "větve"),
        ("mieszanki", "směsi"),
        ("Silnik brushless", "Bezuhlíkový motor"),
        ("prowadnica", "lišta"),
        ("drewno opałowe", "palivové dřevo"),
        ("przycinanie", "prořezávání"),
        ("ogrodzie", "zahradě"),
        ("szarpania startera", "tahání za startovací šňůru"),
        ("benzyny", "benzínu"),
        ("przedłużacza", "prodlužovacího kabelu"),
        ("Klient", "Zákazník"),
        ("całej Polsce", "celé ČR"),
        ("Drewno i gałęzie", "Dřevo a větve"),
        ("benzyny", "benzínu"),
        ("akumulatory", "baterie"),
        ("Płatność przy odbiorze w całej Polsce", "Dobírka v celé ČR"),
    ]
    cs = apply_repl(pl, cs_pairs)
    cs["og_description"] = (
        "Dřevo a větve do 45 cm bez benzínu: brushless 1600 W, 2 baterie, až 12 h. "
        "Dobírka v celé ČR."
    )
    cs["rating"] = "<strong>Doručení 24–48 h</strong> v Česku · <strong>Dobírka</strong>"
    cs["f1_p"] = "Doručení domů v Česku"
    write("cs", cs)

    sk_pairs = cs_pairs + [
        ("Česku", "Slovensku"),
        ("v Česku", "na Slovensku"),
        ("celé ČR", "celém Slovensku"),
        ("Objednejte", "Objednajte"),
        ("KOUPTE", "KÚPTE"),
        ("POTVRĎTE", "POTVRĎTE"),
        ("KURÝROVI", "KURIÉROVI"),
        ("kurýrovi", "kuriérovi"),
        ("Zavoláme", "Zavoláme"),
        ("Odeslání", "Odoslanie"),
        ("hodin", "hodín"),
        ("telefonickém potvrzení", "telefonickom potvrdení"),
        ("Doručení domů", "Doručenie domov"),
        ("platbou na dobírku", "platbou na dobierku"),
        ("Dobírka", "Dobierka"),
        ("Zákazník", "Zákazník"),
    ]
    sk = apply_repl(pl, sk_pairs)
    sk["og_description"] = (
        "Drevo a konáre do 45 cm bez benzínu: brushless 1600 W, 2 batérie, až 12 h. "
        "Dobierka na celom Slovensku."
    )
    sk["rating"] = "<strong>Doručenie 24–48 h</strong> na Slovensku · <strong>Dobierka</strong>"
    sk["f1_p"] = "Doručenie domov na Slovensku"
    write("sk", sk)

    # Romanian from ES with RO pass
    ro_pairs = [
        ("Productos útiles para el día a día", "Produse utile zi de zi"),
        ("entrega en 24–48 h con pago contra reembolso", "livrare în 24–48 h cu plată la livrare"),
        ("Motosierra", "Ferăstrău cu lanț"),
        ("motosierra", "ferăstrău cu lanț"),
        ("España", "România"),
        ("español", "română"),
        ("Contra reembolso", "Plată la livrare"),
        ("contra reembolso", "plată la livrare"),
        ("mensajero", "curier"),
        ("MENSAJERO", "CURIER"),
        ("PAGAS EN EFECTIVO AL", "PLĂTIȚI CASH CURIERULUI"),
        ("ENVÍO GRATIS", "LIVRARE GRATUITĂ"),
        ("PROMO", "PROMOȚIE"),
        ("Envío gratis", "Livrare gratuită"),
        ("Entrega a domicilio", "Livrare la domiciliu"),
        ("Sin tarjeta ni pago por adelantado", "Fără card, fără avans"),
        ("Garantía 2 años", "Garanție 2 ani"),
        ("Devolución 30 días", "Retur 30 zile"),
        ("Reembolso completo si no te convence", "Rambursare integrală dacă nu vă convinge"),
        ("Solicitar", "Comandați"),
        ("COMPRAR TAIGOR™ A", "CUMPĂRAȚI TAIGOR™ LA"),
        ("CONFIRMAR PEDIDO — PAGO AL", "CONFIRMAȚI COMANDA — PLĂTESC LA LIVRARE"),
        ("Corta leña", "Tăiați lemne"),
        ("setos y ramas", "garduri vii și crengi"),
        ("sin cables ni mezcla", "fără cablu și amestec"),
        ("Cliente", "Client"),
        ("toda España", "toată România"),
        ("en España", "în România"),
        ("Corta leña y ramas hasta 45 cm sin gasolina", "Lemne și crengi până la 45 cm fără benzină"),
    ]
    ro = apply_repl(es, ro_pairs)
    ro["og_description"] = (
        "Lemne și crengi până la 45 cm fără benzină: brushless 1600 W, 2 baterii, până la 12 h. "
        "Plată la livrare în România."
    )
    ro["rating"] = "<strong>Livrare 24–48 h</strong> în România · <strong>Plată la livrare</strong>"
    ro["f1_p"] = "Livrare la domiciliu în România"
    write("ro", ro)

    # Lithuanian — hand-tuned header block + PL body pass
    lt = apply_repl(
        pl,
        [
            ("Polsce", "Lietuvoje"),
            ("w Polsce", "Lietuvoje"),
            ("PROMOCJA", "AKCIJA"),
            ("DARMOWA DOSTAWA", "NEMOKAMAS PRISTATYMAS"),
            ("PŁACISZ GOTÓWKĄ KURIEROWI", "MOKATE KURJERIUI GRYNAISIAIS"),
            ("Płatność przy odbiorze", "Apmokėjimas pristatymo metu"),
            ("Dostawa 24–48 h", "Pristatymas 24–48 val."),
            ("Przydatne produkty na co dzień", "Naudingi produktai kasdieniam gyvenimui"),
            ("dostawa w 24–48 h z płatnością przy odbiorze", "pristatymas per 24–48 val. su apmokėjimu pristatymo metu"),
            ("KUP TAIGOR™ ZA", "PIRKTI TAIGOR™ UŽ"),
            ("Klient", "Klientas"),
        ],
    )
    lt.update(
        {
            "title": "TAIGOR™ | Akumuliatorinis grandininis pjūklas brushless 1600 W su dviem akumuliatoriais — 50 % nuolaida",
            "description": "TAIGOR™: akumuliatorinis grandininis pjūklas brushless 1600 W, 45 cm gaida, du akumuliatoriai iki 12 val. Automatinis tepimas, pilnas rinkinys, apmokėjimas kurjeriui grynais.",
            "og_title": "TAIGOR™ — Akumuliatorinis pjūklas 1600 W už pusę kainos",
            "og_description": "Medieną ir šakas iki 45 cm be benzino: brushless 1600 W, 2 akumuliatoriai, iki 12 val. Apmokėjimas pristatymo metu visoje Lietuvoje.",
            "h1": "Kertate malkas, gyvatvores ir šakas be laido ir mišinio: TAIGOR™ brushless 1600 W",
            "lead": "Brushless variklis, du ličio akumuliatoriai ir 45 cm gaida malkoms, genėjimui ir sodo tvarkymui. Vienas mygtukas — be starterio virvės, be benzino, be ilgų kabelių.",
            "f1_p": "Pristatymas į namus Lietuvoje",
            "rating": "<strong>Pristatymas 24–48 val.</strong> Lietuvoje · <strong>Apmokėjimas pristatymo metu</strong>",
            "topbar": "AKCIJA · −50 % · NEMOKAMAS PRISTATYMAS · MOKATE KURJERIUI GRYNAISIAIS",
            "form_h2_prefix": "Užsakyti TAIGOR™ už",
            "submit_btn": "PATVIRTINTI UŽSAKYMĄ — MOKĖSIU KURJERIUI",
            "form_note": "💶 Jokio avanso — mokate grynaisiais kurjeriui gavę siuntą",
            "alt_client": "Klientas",
        }
    )
    write("lt", lt)

    # Hungarian from PL pass
    hu = apply_repl(
        pl,
        [
            ("Polsce", "Magyarországon"),
            ("w Polsce", "Magyarországon"),
            ("PROMOCJA", "AKCIÓ"),
            ("DARMOWA DOSTAWA", "INGYENES SZÁLLÍTÁS"),
            ("PŁACISZ GOTÓWKĄ KURIEROWI", "A FUTÁRNAK FIZET KÉSZPÉNZBEN"),
            ("Płatność przy odbiorze", "Utánvét"),
            ("Dostawa 24–48 h", "Szállítás 24–48 óra"),
            ("Przydatne produkty na co dzień", "Hasznos termékek mindennapra"),
            ("dostawa w 24–48 h z płatnością przy odbiorze", "24–48 órás szállítás utánvéttel"),
            ("KUP TAIGOR™ ZA", "TAIGOR™ VÁSÁRLÁSA"),
            ("Tnij drewno, żywopłoty i gałęzie", "Vágjon fát, sövényt és ágakat"),
            ("bez kabla i mieszanki", "kábel és keverék nélkül"),
        ],
    )
    hu.update(
        {
            "h1": "Vágjon fát, sövényt és ágakat kábel és keverék nélkül: TAIGOR™ brushless 1600 W",
            "og_description": "Fa és ágak 45 cm-ig benzin nélkül: brushless 1600 W, 2 akkumulátor, akár 12 óra. Utánvét egész Magyarországon.",
            "rating": "<strong>Szállítás 24–48 óra</strong> Magyarországon · <strong>Utánvét</strong>",
            "f1_p": "Házhoz szállítás Magyarországon",
            "topbar": "AKCIÓ · −50 % · INGYENES SZÁLLÍTÁS · A FUTÁRNAK FIZET KÉSZPÉNZBEN",
            "form_h2_prefix": "TAIGOR™ rendelése",
            "submit_btn": "RENDELÉS MEGERŐSÍTÉSE — UTÁNVÉT",
            "form_note": "💶 Előleg nélkül — átvételkor fizet készpénzben a futárnak",
            "alt_client": "Vásárló",
        }
    )
    write("hu", hu)

    # Slovenian / Croatian from CS
    cs_loaded = load("cs")
    si = apply_repl(
        cs_loaded,
        [
            ("Česku", "Sloveniji"),
            ("v Česku", "v Sloveniji"),
            ("celé ČR", "po Sloveniji"),
            ("Dobírka", "Plačilo po povzetju"),
            ("dobírku", "po povzetju"),
            ("KURÝROVI", "DOSTAVLJALCU"),
            ("kurýrovi", "dostavljalcu"),
            ("Zákazník", "Stranka"),
            ("Objednejte", "Naročite"),
            ("KOUPTE", "KUPI"),
            ("POTVRĎTE", "POTRDITE"),
            ("Motorová pila", "Motorna verižna žaga"),
            ("motorová pila", "motorna verižna žaga"),
        ],
    )
    si["og_description"] = (
        "Drva in veje do 45 cm brez bencina: brushless 1600 W, 2 bateriji, do 12 h. "
        "Plačilo po povzetju po Sloveniji."
    )
    si["rating"] = "<strong>Dostava 24–48 h</strong> v Sloveniji · <strong>Plačilo po povzetju</strong>"
    si["f1_p"] = "Dostava na dom v Sloveniji"
    write("si", si)

    hr = apply_repl(
        si,
        [
            ("Sloveniji", "Hrvatskoj"),
            ("Sloveniji", "Hrvatskoj"),
            ("po Sloveniji", "u Hrvatskoj"),
            ("v Sloveniji", "u Hrvatskoj"),
            ("Plačilo po povzetju", "Plaćanje pouzećem"),
            ("po povzetju", "pouzećem"),
            ("DOSTAVLJALCU", "DOSTAVLJAČU"),
            ("dostavljalcu", "dostavljaču"),
            ("Stranka", "Kupac"),
            ("Naročite", "Naručite"),
            ("POTRDITE", "POTVRDITE"),
            ("KUPI", "KUPI"),
            ("Motorna verižna žaga", "Motorna lančana pila"),
            ("motorna verižna žaga", "motorna lančana pila"),
            ("Drva", "Drva"),
        ],
    )
    hr["og_description"] = (
        "Drva i grane do 45 cm bez benzina: brushless 1600 W, 2 baterije, do 12 h. "
        "Plaćanje pouzećem u Hrvatskoj."
    )
    hr["rating"] = "<strong>Dostava 24–48 h</strong> u Hrvatskoj · <strong>Plaćanje pouzećem</strong>"
    hr["f1_p"] = "Dostava na kućnu adresu u Hrvatskoj"
    write("hr", hr)

    # Latvian from LT pass
    lt_loaded = load("lt")
    lv = apply_repl(
        lt_loaded,
        [
            ("Lietuvoje", "Latvijā"),
            ("Lietuvos", "Latvijas"),
            ("visoje Lietuvoje", "visā Latvijā"),
            ("Klientas", "Klients"),
            ("PIRKTI TAIGOR™ UŽ", "PIRKT TAIGOR™ PAR"),
            ("Užsakyti", "Pasūtīt"),
            ("PATVIRTINTI UŽSAKYMĄ", "APSTIPRINĀT PASŪTĪJUMU"),
            ("KURJERIUI", "KURJERAM"),
            ("kurjeriui", "kurjeram"),
            ("pristatymo metu", "piegādes brīdī"),
            ("Apmokėjimas pristatymo metu", "Apmaksa piegādē"),
            ("Naudingi produktai kasdieniam gyvenimui", "Noderīgi produkti ikdienai"),
            ("AKCIJA", "AKCIJA"),
            ("NEMOKAMAS PRISTATYMAS", "BEZMAKSAS PIEGĀDE"),
            ("GRYNAISIAIS", "SKAIDRĀ NAUDĀ"),
        ],
    )
    lv.update(
        {
            "title": "TAIGOR™ | Akumulatora ķēžzāģis brushless 1600 W ar divām baterijām — 50 % atlaide",
            "h1": "Zāģējiet malku, dzīvžogus un zarus bez vada un maisījuma: TAIGOR™ brushless 1600 W",
            "og_description": "Kokmateriāli un zari līdz 45 cm bez benzīna: brushless 1600 W, 2 akumulatori, līdz 12 h. Apmaksa piegādē visā Latvijā.",
            "rating": "<strong>Piegāde 24–48 h</strong> Latvijā · <strong>Apmaksa piegādē</strong>",
            "f1_p": "Piegāde uz mājām Latvijā",
            "topbar": "AKCIJA · −50 % · BEZMAKSAS PIEGĀDE · MAKSĀJAT SKAIDRĀ NAUDĀ KURJERAM",
        }
    )
    write("lv", lv)

    for code in ("cs", "sk", "ro", "lt", "hu", "si", "hr", "lv", "pt"):
        p = load(code)
        print(code, len(p))


if __name__ == "__main__":
    main()
