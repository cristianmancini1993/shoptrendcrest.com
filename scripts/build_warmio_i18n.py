#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble scripts/_warmio_i18n.py from UI strings + WARMIO product copy."""
from __future__ import annotations

import importlib.util
import pprint
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_mod(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


COPY_UI_KEYS = {
    "submitting",
    "cookie_text",
    "cookie_accept",
    "cookie_learn",
    "info",
    "about",
    "contact",
    "contacts",
    "privacy",
    "terms",
    "cookie",
    "ship",
    "refund",
    "rights",
    "footer_blurb",
    "footer_tagline",
    "footer_powered_top",
    "footer_powered_bottom",
    "ty_title",
    "ty_desc",
    "ty_h1",
    "ty_sub",
    "ty_alt",
    "ty_eyebrow",
    "ty_action_title",
    "ty_action_body",
    "ty_action_warn",
    "ty_hours_h",
    "ty_hours",
    "ty_next_h",
    "ty_badges",
    "hours",
    "mins",
    "secs",
    "countdown",
    "stock_l",
    "stock_r",
    "live",
    "live0",
    "label_name",
    "label_tel",
    "label_addr",
    "ph_name",
    "ph_tel",
    "ph_addr",
}

UI_ALIASES = {
    "label_phone": "label_tel",
    "ph_phone": "ph_tel",
    "btn": "submit_btn",
}

WARMIO_COUNTDOWN: dict[str, str] = {
    "it": "⏰ La promozione scade tra",
    "lt": "⏰ Akcija baigiasi po",
    "es": "⏰ La promoción termina en",
    "pt": "⏰ A promoção termina em",
    "pl": "⏰ Promocja kończy się za",
    "cs": "⏰ Akce končí za",
    "ro": "⏰ Promoția se încheie în",
    "sk": "⏰ Akcia končí o",
    "si": "⏰ Promocija se konča v",
    "hr": "⏰ Promocija završava za",
    "hu": "⏰ Az akció vége:",
    "de": "⏰ Das Angebot endet in",
    "lv": "⏰ Akcija beidzas pēc",
}

def _warmio_brand(s: str) -> str:
    return (
        s.replace("LEAFORA™", "WARMIO™")
        .replace("LEAFORA", "WARMIO")
        .replace("GlacierAir™", "WARMIO™")
        .replace("GlacierAir", "WARMIO")
    )


# Local form labels + placeholders (name → tel → address), aligned with taigor geos.
WARMIO_FORM_UI: dict[str, dict[str, str]] = {
    "hu": {
        "label_name": "Teljes név*",
        "label_tel": "Telefonszám*",
        "label_addr": "Teljes cím*",
        "ph_name": "Nagy Péter",
        "ph_tel": "+36 30 123 4567",
        "ph_addr": "Andrássy út 10., 1061 Budapest",
    },
    "ro": {
        "label_name": "Nume și prenume*",
        "label_tel": "Telefon*",
        "label_addr": "Adresă completă*",
        "ph_name": "Ion Popescu",
        "ph_tel": "+40 721 234 567",
        "ph_addr": "Str. Victoriei 10, 010096 București",
    },
    "si": {
        "label_name": "Ime in priimek*",
        "label_tel": "Telefonska številka*",
        "label_addr": "Naslov*",
        "ph_name": "Luka Novak",
        "ph_tel": "+386 41 123 456",
        "ph_addr": "Slovenska cesta 10, 1000 Ljubljana",
    },
    "pt": {
        "label_name": "Nome completo*",
        "label_tel": "Telefone*",
        "label_addr": "Morada*",
        "ph_name": "Ana Silva",
        "ph_tel": "+351 912 345 678",
        "ph_addr": "Rua da Liberdade 45, 1250-096 Lisboa",
    },
    "hr": {
        "label_name": "Ime i prezime*",
        "label_tel": "Broj mobitela*",
        "label_addr": "Adresa*",
        "ph_name": "Ivan Horvat",
        "ph_tel": "+385 91 123 4567",
        "ph_addr": "Ilica 10, 10000 Zagreb",
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
    "it": {
        "label_name": "Nome e cognome*",
        "label_tel": "Telefono*",
        "label_addr": "Indirizzo completo per la consegna*",
        "ph_name": "Mario Rossi",
        "ph_tel": "+39 333 123 4567",
        "ph_addr": "Via Roma 15, 20121 Milano",
    },
    "sk": {
        "label_name": "Meno a priezvisko*",
        "label_tel": "Telefón*",
        "label_addr": "Adresa*",
        "ph_name": "Peter Horváth",
        "ph_tel": "+421 912 345 678",
        "ph_addr": "Hlavná 15, 811 01 Bratislava",
    },
    "lt": {
        "label_name": "Vardas ir pavardė*",
        "label_tel": "Telefonas*",
        "label_addr": "Adresas*",
        "ph_name": "Jonas Petraitis",
        "ph_tel": "+370 612 34567",
        "ph_addr": "Gedimino pr. 10-5, 01103 Vilnius",
    },
}

WARMIO_TY_BADGES: dict[str, tuple[str, str, str]] = {
    "it": ("🔒 Contrassegno", "🛡️ Garanzia 4 anni", "🔐 Protezione SSL"),
    "de": ("🔒 Zahlung per Nachnahme", "🛡️ 4 Jahre Garantie", "🔐 SSL-Schutz"),
    "es": ("🔒 Contra reembolso", "🛡️ Garantía de 4 años", "🔐 Protección SSL"),
    "pt": ("🔒 Pagamento à cobrança", "🛡️ Garantia de 4 anos", "🔐 Proteção SSL"),
    "pl": ("🔒 Płatność przy odbiorze", "🛡️ 4-letnia gwarancja", "🔐 Ochrona SSL"),
    "cs": ("🔒 Platba na dobírku", "🛡️ 4 roky záruky", "🔐 SSL ochrana"),
    "ro": ("🔒 Plată la livrare", "🛡️ Garanție 4 ani", "🔐 Protecție SSL"),
    "sk": ("🔒 Platba na dobierku", "🛡️ 4 roky záruky", "🔐 SSL ochrana"),
    "si": ("🔒 Plačilo po povzetju", "🛡️ 4 leta garancije", "🔐 Zaščita SSL"),
    "hr": ("🔒 Plaćanje pouzećem", "🛡️ Jamstvo 4 godine", "🔐 SSL zaštita"),
    "hu": ("🔒 Utánvét", "🛡️ 4 év garancia", "🔐 SSL védelem"),
    "lv": ("🔒 Maksa pēc saņemšanas", "🛡️ 4 gadu garantija", "🔐 SSL aizsardzība"),
    "lt": ("🔒 Apmokėjimas pristatymo metu", "🛡️ 4 metų garantija", "🔐 SSL apsauga"),
}

WARMIO_FOOTER_POWERED: dict[str, dict[str, str]] = {
    "it": {
        "footer_powered_top": "shoptrendcrest.com — Offerto da WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Offerto da WHATECH MOBILE CO., LIMITED. Tutti i diritti riservati.",
        "footer_tagline": "Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.",
    },
    "de": {
        "footer_powered_top": "shoptrendcrest.com — Bereitgestellt von WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Bereitgestellt von WHATECH MOBILE CO., LIMITED. Alle Rechte vorbehalten.",
        "footer_tagline": "Ausgewählte Produkte für Haus, Garten und Alltag. Zahlung per Nachnahme in 18 europäischen Ländern.",
    },
    "es": {
        "footer_powered_top": "shoptrendcrest.com — Desarrollado por WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Desarrollado por WHATECH MOBILE CO., LIMITED. Todos los derechos reservados.",
        "footer_tagline": "Productos seleccionados para el hogar, el jardín y la vida diaria. Pago contra reembolso en 18 países europeos.",
    },
    "pt": {
        "footer_powered_top": "shoptrendcrest.com — Desenvolvido por WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Desenvolvido por WHATECH MOBILE CO., LIMITED. Todos os direitos reservados.",
        "footer_tagline": "Produtos selecionados para casa, jardim e dia a dia. Pagamento à cobrança em 18 países europeus.",
    },
    "pl": {
        "footer_powered_top": "shoptrendcrest.com — Obsługiwane przez WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Obsługiwane przez WHATECH MOBILE CO., LIMITED. Wszelkie prawa zastrzeżone.",
        "footer_tagline": "Wybrane produkty do domu, ogrodu i codzienności. Płatność przy odbiorze w 18 krajach Europy.",
    },
    "cs": {
        "footer_powered_top": "shoptrendcrest.com — Provozuje WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Provozuje WHATECH MOBILE CO., LIMITED. Všechna práva vyhrazena.",
        "footer_tagline": "Vybrané produkty pro domov, zahradu a každodenní život. Platba na dobírku v 18 evropských zemích.",
    },
    "ro": {
        "footer_powered_top": "shoptrendcrest.com — Oferit de WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Oferit de WHATECH MOBILE CO., LIMITED. Toate drepturile rezervate.",
        "footer_tagline": "Produse alese pentru casă, grădină și viața de zi cu zi. Plată la livrare în 18 țări europene.",
    },
    "sk": {
        "footer_powered_top": "shoptrendcrest.com — Prevádzka WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Prevádzka WHATECH MOBILE CO., LIMITED. Všetky práva vyhradené.",
        "footer_tagline": "Vybrané produkty pre domov, záhradu a každodenný život. Platba na dobierku v 18 európskych krajinách.",
    },
    "si": {
        "footer_powered_top": "shoptrendcrest.com — Omogoča WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Omogoča WHATECH MOBILE CO., LIMITED. Vse pravice pridržane.",
        "footer_tagline": "Izbrani izdelki za dom, vrt in vsakdan. Plačilo po povzetju v 18 evropskih državah.",
    },
    "hr": {
        "footer_powered_top": "shoptrendcrest.com — Pokreće WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Pokreće WHATECH MOBILE CO., LIMITED. Sva prava pridržana.",
        "footer_tagline": "Odabrani proizvodi za dom, vrt i svakodnevicu. Plaćanje pouzećem u 18 europskih zemalja.",
    },
    "hu": {
        "footer_powered_top": "shoptrendcrest.com — Üzemelteti: WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Üzemelteti: WHATECH MOBILE CO., LIMITED. Minden jog fenntartva.",
        "footer_tagline": "Válogatott termékek otthonra, kertre és mindennapokra. Utánvétes fizetés 18 európai országban.",
    },
    "lv": {
        "footer_powered_top": "shoptrendcrest.com — Nodrošina WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Nodrošina WHATECH MOBILE CO., LIMITED. Visas tiesības aizsargātas.",
        "footer_tagline": "Izvēlēti produkti mājai, dārzam un ikdienai. Apmaksa saņemšanas brīdī 18 Eiropas valstīs.",
    },
    "lt": {
        "footer_powered_top": "shoptrendcrest.com — Teikia WHATECH MOBILE CO., LIMITED",
        "footer_powered_bottom": "shoptrendcrest.com — Teikia WHATECH MOBILE CO., LIMITED. Visos teisės saugomos.",
        "footer_tagline": "Atrinkti produktai namams, sodui ir kasdienai. Apmokėjimas pristatymo metu 18 Europos šalių.",
    },
}

WARMIO_UI_OVERRIDES: dict[str, dict[str, str]] = {
    "si": {
        "ty_sub": "Odlično — pošiljka je v pripravi. Ostaja le še <strong>zadnji korak</strong>: telefonska potrditev.",
    },
}

WARMIO_LIVE0: dict[str, str] = {
    "ro": "<strong>41 de persoane</strong> evaluează WARMIO™ acum",
    "si": "<strong>34 oseb</strong> trenutno razmišlja o WARMIO™",
    "hr": "<strong>34 osobe</strong> trenutno razmatraju WARMIO™",
    "lv": "<strong>34 cilvēki</strong> šobrīd izvērtē WARMIO™",
}


def load_ui_translations() -> dict[str, dict]:
    leafora = _load_mod("_leafora_i18n", "_leafora_i18n.py").TRANSLATIONS
    ga2 = _load_mod("_ga_i18n_part2", "_ga_i18n_part2.py").TRANSLATIONS
    ga3 = _load_mod("_ga_i18n_part3", "_ga_i18n_part3.py").TRANSLATIONS
    ro = _load_mod("_leafora_ro_strings", "_leafora_ro_strings.py").RO_STRINGS
    ui: dict[str, dict] = {k: dict(v) for k, v in leafora.items()}
    ui["ro"] = dict(ro)
    ui["si"] = dict(ga2["si"])
    ui["hr"] = dict(ga2["hr"])
    ui["lv"] = dict(ga3["lv"])
    for lang, table in ui.items():
        for src, dst in UI_ALIASES.items():
            if src in table and dst not in table:
                table[dst] = table[src]
    return ui


def load_warmio_core() -> dict[str, dict]:
    from _warmio_assemble import build_locale
    from _warmio_locale_patches import LOCALE_PATCH

    return {code: build_locale(bundle) for code, bundle in LOCALE_PATCH.items()}


def build() -> dict:
    ui_all = load_ui_translations()
    core_all = load_warmio_core()
    it_defaults = _load_mod("_warmio_it_strings", "_warmio_it_strings.py").IT_STRINGS
    out: dict = {}
    for lang, core in core_all.items():
        leaf = ui_all.get(lang, ui_all.get("it", {}))
        merged: dict = {}
        for k in COPY_UI_KEYS:
            if k in leaf:
                v = leaf[k]
                if isinstance(v, str):
                    merged[k] = _warmio_brand(v)
                else:
                    merged[k] = v
            elif k in it_defaults and isinstance(it_defaults[k], str):
                merged[k] = it_defaults[k]
            elif k == "ty_badges" and isinstance(it_defaults.get("ty_badges"), tuple):
                merged[k] = it_defaults["ty_badges"]
        merged.update(core)
        if lang == "it":
            for k in COPY_UI_KEYS:
                if k in it_defaults:
                    v = it_defaults[k]
                    if isinstance(v, str):
                        merged[k] = v
                    elif k == "ty_badges":
                        merged[k] = v
            merged["ty_steps"] = list(it_defaults["ty_steps"])
        if lang in WARMIO_COUNTDOWN:
            merged["countdown"] = WARMIO_COUNTDOWN[lang]
        if lang in WARMIO_LIVE0:
            merged["live0"] = WARMIO_LIVE0[lang]
        if lang in WARMIO_FORM_UI:
            merged.update(WARMIO_FORM_UI[lang])
        if lang in WARMIO_TY_BADGES:
            merged["ty_badges"] = WARMIO_TY_BADGES[lang]
        if lang in WARMIO_FOOTER_POWERED:
            merged.update(WARMIO_FOOTER_POWERED[lang])
        if lang in WARMIO_UI_OVERRIDES:
            merged.update(WARMIO_UI_OVERRIDES[lang])
        if "live" in merged:
            merged["live"] = _warmio_brand(merged["live"])
        if "live0" in merged:
            merged["live0"] = _warmio_brand(merged["live0"])
        if "cta" in merged and "{price}" not in merged["cta"]:
            merged["cta"] = merged.get("cta_inline", merged.get("cta", "ORDINA WARMIO™ →"))
        for k, v in list(merged.items()):
            if isinstance(v, str):
                merged[k] = _warmio_brand(v)
            elif isinstance(v, tuple):
                merged[k] = tuple(_warmio_brand(x) for x in v)
            elif isinstance(v, list):
                merged[k] = [_warmio_brand(x) for x in v]
        out[lang] = merged
    return out


def main() -> None:
    tr = build()
    target = ROOT / "_warmio_i18n.py"
    body = (
        "# -*- coding: utf-8 -*-\n"
        '"""WARMIO™ wall unit landing + thank-you translations."""\n\n'
        "TRANSLATIONS = "
        + pprint.pformat(tr, width=120, sort_dicts=False)
        + "\n"
    )
    target.write_text(body, encoding="utf-8")
    print(f"Wrote {target} ({len(tr)} locales)")


if __name__ == "__main__":
    main()
