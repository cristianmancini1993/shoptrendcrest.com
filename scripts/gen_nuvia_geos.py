#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Nuvia smartwatch landing + thank-you pages for 11 geos."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer
IT_INDEX = ROOT / "it/nuvia/index.html"
IT_TY = ROOT / "it/nuvia/thank-you.html"

OFFERS = [
    {"geo": "pt", "lang": "pt", "slug": "nuvia", "product": "Nuvia™", "currency": "EUR", "price": 66, "cpa": 16, "offer_id": "1633", "phone": "+351 912 345 678"},
    {"geo": "gr", "lang": "el", "slug": "nuvia", "product": "Nuvia™", "currency": "EUR", "price": 69, "cpa": 20, "offer_id": "1842", "phone": "+30 691 234 5678"},
    {"geo": "bg", "lang": "bg", "slug": "nuvia", "product": "Nuvia™", "currency": "EUR", "price": 69, "cpa": 20, "offer_id": "1843", "phone": "+359 888 123 456"},
    {"geo": "ro", "lang": "ro", "slug": "nuvia", "product": "Nuvia™", "currency": "RON", "price": 339, "cpa": 20, "offer_id": "1844", "phone": "+40 721 123 456"},
    {"geo": "lt", "lang": "lt", "slug": "nuvia-v17", "product": "Nuvia V17™", "currency": "EUR", "price": 69, "cpa": 17, "offer_id": "2136", "phone": "+370 612 34567"},
    {"geo": "es", "lang": "es", "slug": "nuvia", "product": "Nuvia™", "currency": "EUR", "price": 59, "cpa": 18, "offer_id": "2297", "phone": "+34 612 345 678"},
    {"geo": "hu", "lang": "hu", "slug": "nuvia-v17", "product": "Nuvia V17™", "currency": "HUF", "price": 21999, "display": "21 999 Ft", "cpa": 16, "offer_id": "2881", "phone": "+36 30 123 4567"},
    {"geo": "de", "lang": "de", "slug": "nuvia", "product": "Nuvia™", "currency": "EUR", "price": 69, "cpa": 17, "offer_id": "2934", "phone": "+49 170 1234567"},
    {"geo": "cz", "lang": "cs", "slug": "nuvia", "product": "Nuvia™", "currency": "CZK", "price": 1499, "display": "1 499 Kč", "cpa": 16, "offer_id": "3143", "phone": "+420 601 123 456"},
    {"geo": "sk", "lang": "sk", "slug": "nuvia-v17", "product": "Nuvia V17™", "currency": "EUR", "price": 64, "cpa": 17, "offer_id": "3844", "phone": "+421 901 123 456"},
    {"geo": "lv", "lang": "lv", "slug": "nuvia-v17", "product": "Nuvia V17™", "currency": "EUR", "price": 74, "cpa": 15, "offer_id": "3845", "phone": "+371 2123 4567"},
]

def _load_copy() -> dict[str, dict]:
    path = Path(__file__).with_name("_nuvia_copy_data.py")
    spec = importlib.util.spec_from_file_location("_nuvia_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


COPY = _load_copy()


def was_price(now: float) -> int:
    return round(now / 0.3)


def fmt_price(amount: float, currency: str, display: str | None = None) -> str:
    if display:
        return display
    if currency == "EUR":
        if float(amount).is_integer():
            return f"{int(amount)} €"
        return f"{amount:.2f}".replace(".", ",") + " €"
    if currency == "RON":
        return f"{int(amount)} lei"
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Ft"
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Kč"
    if currency == "PLN":
        whole = int(round(amount))
        return f"{whole} zł"
    return str(amount)


def apply_product(text: str, product: str) -> str:
    return text.replace("{product}", product)


def offer_name(offer: dict) -> str:
    geo = offer["geo"].upper()
    if "v17" in offer["slug"]:
        return f"Nuvia V17 {geo}"
    return f"Nuvia {geo}"


def lp_id(offer: dict) -> str:
    return f"{offer['geo']}-{offer['offer_id']}"


def inject_offer_markers(html: str, offer_id: str) -> str:
    if 'name="offer-id"' not in html:
        html = html.replace(
            '<meta charset="utf-8">',
            f'<meta charset="utf-8">\n<meta name="offer-id" content="{offer_id}">',
            1,
        )
    else:
        html = re.sub(
            r'<meta name="offer-id" content="[^"]*">',
            f'<meta name="offer-id" content="{offer_id}">',
            html,
            count=1,
        )
    marker = f"<!-- Offer #{offer_id} -->"
    if marker not in html:
        html = html.replace("<body>", f"<body>\n\n  {marker}", 1)
    if 'name="offer_id"' not in html:
        html = html.replace(
            '<form class="cod-form order-form" novalidate>',
            (
                '<form class="cod-form order-form" novalidate>\n'
                f'          <input type="hidden" name="offer_id" value="{offer_id}">'
            ),
            1,
        )
    else:
        html = re.sub(
            r'<input type="hidden" name="offer_id" value="[^"]*">',
            f'<input type="hidden" name="offer_id" value="{offer_id}">',
            html,
            count=1,
        )
    return html


def text(c: dict, key: str, product: str) -> str:
    return apply_product(c[key], product)


def index_replacements(c: dict, product: str) -> list[tuple[str, str]]:
    pairs = [
        ("Nuvia™ — Smartwatch di nuova generazione", text(c, "title", product)),
        (
            'Nuvia™: lo smartwatch di nuova generazione con notifiche in tempo reale, vetro temperato anti-graffio e coach AI per la corsa. Compatibile con Android e iPhone. -70% oggi, pagamento alla consegna.',
            text(c, "description", product),
        ),
        ("🔥 SOLO OGGI: -70% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA 🔥", c["topbar"]),
        ("<strong>4,8/5</strong> — oltre <strong>6.200</strong> polsi già connessi", c["rating"]),
        ("🚚 Spedizione gratuita + Garanzia 2 anni inclusa", c["gift"]),
        (
            'Lo smartwatch <span class="hl">🔥 di nuova generazione</span> che rende il telefono quasi superfluo',
            c["h1_mobile"],
        ),
        (
            'Lo smartwatch <span class="hl">di nuova generazione</span> che rende il telefono quasi superfluo',
            c["h1_desktop"],
        ),
        (
            "<strong>Nuvia™</strong> — tecnologia completa a un prezzo onesto: le stesse funzioni dei modelli top di gamma, senza pagare il logo. Compatibile con Android e iPhone.",
            text(c, "lead", product),
        ),
        ("Nuvia smartwatch di nuova generazione", text(c, "alt_hero", product)),
        ("SÌ, VOGLIO NUVIA™ →", text(c, "cta", product)),
        ("🔒 Zero anticipo · Zero carta · Paghi solo quando la ricevi", c["form_note_hero"]),
        ("<h4>Spedizione rapida</h4><p>Consegna in tutta Italia</p>", f'<h4>{c["f1_h"]}</h4><p>{c["f1_p"]}</p>'),
        ("<h4>Ordine sicuro</h4><p>Pagamento alla consegna</p>", f'<h4>{c["f2_h"]}</h4><p>{c["f2_p"]}</p>'),
        ("<h4>Garanzia 2 anni</h4><p>Materiali e lavorazione controllati</p>", f'<h4>{c["f3_h"]}</h4><p>{c["f3_p"]}</p>'),
        ("<h4>Reso 30 giorni</h4><p>Rimborso semplice</p>", f'<h4>{c["f4_h"]}</h4><p>{c["f4_p"]}</p>'),
        ("⏰ Lo sconto del -70% termina tra", c["countdown"]),
        ('<div class="lbl">Ore</div>', f'<div class="lbl">{c["hours"]}</div>'),
        ('<div class="lbl">Min</div>', f'<div class="lbl">{c["mins"]}</div>'),
        ('<div class="lbl">Sec</div>', f'<div class="lbl">{c["secs"]}</div>'),
        ('<span class="left">Disponibilità</span>', f'<span class="left">{c["stock_l"]}</span>'),
        ('<span class="right">Solo pochi pezzi rimasti</span>', f'<span class="right">{c["stock_r"]}</span>'),
        (
            '<span id="liveCount"><strong>23 persone</strong> stanno guardando questo prodotto ora</span>',
            f'<span id="liveCount">{c["live_tpl"].format(n=23)}</span>',
        ),
        ("Completa il tuo ordine", c["form_h2"]),
        (
            "Compila il modulo — il nostro team ti contatterà per confermare tutti i dettagli.",
            c["form_p"],
        ),
        ('placeholder="Nome e cognome"', f'placeholder="{c["ph_name"]}"'),
        ('placeholder="+39 333 1234567"', f'placeholder="{c["ph_phone"]}"'),
        ('placeholder="Via, numero civico, CAP, città"', f'placeholder="{c["ph_addr"]}"'),
        ("Inserisci nome e cognome valido", c["err_name"]),
        ("Inserisci un numero valido", c["err_phone"]),
        ("Inserisci indirizzo completo", c["err_addr"]),
        ("CONFERMA ORDINE", c["btn"]),
        ("🔒 Pagamento alla consegna · Zero anticipo · Reso 30 giorni", c["form_note"]),
        ("01 — Tutto il telefono, sul polso", c["ey1"]),
        ("Ricevi e gestisci ogni notifica senza mai tirare fuori lo smartphone", c["h3_1"]),
        ("<span class=\"tag\">Notifiche in tempo reale</span>", f'<span class="tag">{c["tag1a"]}</span>'),
        ("<span class=\"tag\">Controllo app e social</span>", f'<span class="tag">{c["tag1b"]}</span>'),
        ("<span class=\"tag\">Android e iPhone</span>", f'<span class="tag">{c["tag1c"]}</span>'),
        (
            "Con Nuvia™ chiamate, messaggi e social arrivano direttamente sul polso, in tempo reale. Puoi leggere, rispondere e gestire le tue app preferite senza perdere nulla, anche quando il telefono è lontano o in tasca.",
            text(c, "p1", product),
        ),
        (
            "Il risultato: resti sempre connesso, senza restare incollato allo schermo del telefono.",
            c["i1"],
        ),
        (
            "Nuvia smartwatch con notifiche social in tempo reale",
            text(c, "alt_d1", product),
        ),
        ("02 — Costruito per resistere alla vita vera", c["ey2"]),
        (
            "Vetro temperato anti-graffio e corpo robusto, pensati per l'uso quotidiano",
            c["h3_2"],
        ),
        ('<span class="tag">Vetro temperato</span>', f'<span class="tag">{c["tag2a"]}</span>'),
        ('<span class="tag">Cassa resistente agli urti</span>', f'<span class="tag">{c["tag2b"]}</span>'),
        ('<span class="tag">Protezione dai liquidi</span>', f'<span class="tag">{c["tag2c"]}</span>'),
        (
            "Nuvia™ monta un vetro temperato anti-graffio e una cassa robusta, realizzata con materiali pensati per resistere a urti, cadute accidentali e contatto con l'acqua. Lo indossi ogni giorno senza doverlo trattare come un oggetto fragile.",
            text(c, "p2", product),
        ),
        (
            "Tecnologia completa che dura nel tempo, non solo alla prima settimana.",
            c["i2"],
        ),
        (
            "Nuvia smartwatch con vetro temperato anti-graffio",
            text(c, "alt_d2", product),
        ),
        ("03 — Un allenatore che ti conosce davvero", c["ey3"]),
        ("Il tuo coach di corsa personale, basato su intelligenza artificiale", c["h3_3"]),
        ('<span class="tag">Frequenza cardiaca</span>', f'<span class="tag">{c["tag3a"]}</span>'),
        ('<span class="tag">Ossigenazione del sangue</span>', f'<span class="tag">{c["tag3b"]}</span>'),
        ('<span class="tag">Ritmo del passo</span>', f'<span class="tag">{c["tag3c"]}</span>'),
        (
            "Il coach AI integrato in Nuvia™ analizza in tempo reale frequenza cardiaca, livello di ossigenazione e ritmo del passo durante la corsa, per aiutarti a capire quando spingere e quando rallentare, allenamento dopo allenamento.",
            text(c, "p3", product),
        ),
        ("Non un semplice contapassi: un allenatore che si adatta a te.", c["i3"]),
        ("Coach AI Nuvia per la corsa e lo sport", text(c, "alt_d3", product)),
        ("Confronto diretto", c["cmp_label"]),
        ("Smartwatch generico vs. Nuvia™", text(c, "cmp_h2", product)),
        ("<th>Generico</th>", f'<th>{c["th_generic"]}</th>'),
        ('<th class="highlight">Nuvia™</th>', f'<th class="highlight">{text(c, "th_nuvia", product)}</th>'),
        ("Compatibilità", c["r1a"]),
        ("Spesso un solo sistema", c["r1b"]),
        ('<td class="win">Android e iPhone</td>', f'<td class="win">{c["r1c"]}</td>'),
        ("Notifiche", c["r2a"]),
        ("Base o in ritardo", c["r2b"]),
        ('<td class="win">Social e app in tempo reale</td>', f'<td class="win">{c["r2c"]}</td>'),
        ("Resistenza", c["r3a"]),
        ("Vetro e cassa fragili", c["r3b"]),
        ('<td class="win">Vetro temperato + cassa robusta</td>', f'<td class="win">{c["r3c"]}</td>'),
        ("Coach sportivo", c["r4a"]),
        ("Assente o limitato", c["r4b"]),
        ('<td class="win">AI: battito, ossigeno, passo</td>', f'<td class="win">{c["r4c"]}</td>'),
        ("Prezzo", c["r5a"]),
        ("Alto per le stesse funzioni", c["r5b"]),
        ('<td class="win">Fino al -70% oggi</td>', f'<td class="win">{c["r5c"]}</td>'),
        ("Garanzia", c["r6a"]),
        ("Limitata o assente", c["r6b"]),
        ('<td class="win">2 anni di garanzia inclusa</td>', f'<td class="win">{c["r6c"]}</td>'),
        (
            "Migliaia di clienti soddisfatti. Ecco cosa dicono di Nuvia™.",
            text(c, "rev_h2", product),
        ),
        ("Cliente che usa Nuvia per la corsa", text(c, "alt_rev1", product)),
        ("Ora esco a correre senza portarmi dietro il telefono.", c["rev1_h"]),
        (
            "„Il coach AI mi dice in tempo reale come sto andando, e le notifiche importanti arrivano comunque sul polso. Non pensavo che uno smartwatch potesse cambiare così tanto la mia routine.\"",
            c["rev1_p"],
        ),
        ("Luca R. — Milano, acquisto verificato", c["rev1_a"]),
        ("Cliente che usa Nuvia con vetro resistente", text(c, "alt_rev2", product)),
        ("L'ho fatto cadere due volte e non ha un graffio.", c["rev2_h"]),
        (
            "„Lavoro in cantiere e temevo lo rovinassi in una settimana. Il vetro temperato ha retto benissimo agli urti, e continua a funzionare come il primo giorno.\"",
            c["rev2_p"],
        ),
        ("Marco R. — Bologna, acquisto verificato", c["rev2_a"]),
        ("Cliente che usa Nuvia con iPhone", text(c, "alt_rev3", product)),
        ("Perfetta compatibilità con il mio iPhone.", c["rev3_h"]),
        (
            "„Avevo paura che, essendo economico, funzionasse male con iPhone. Invece notifiche, chiamate e app di messaggistica arrivano tutte senza problemi.\"",
            c["rev3_p"],
        ),
        ("Marta F. — Torino, acquisto verificato", c["rev3_a"]),
        ("Nella confezione", c["kit_eye"]),
        ("Il set completo Nuvia™, pronto all'uso da subito", text(c, "kit_h2", product)),
        ("Set completo Nuvia smartwatch", text(c, "alt_kit", product)),
        ("Domande frequenti", c["faq_h2"]),
        ("Quando arriva il mio ordine?", c["fq1"]),
        (
            "La consegna avviene generalmente entro 2-4 giorni lavorativi. Riceverai una conferma con tutti i dettagli di spedizione dopo l'ordine.",
            c["fa1"],
        ),
        ("Come posso pagare?", c["fq2"]),
        (
            "Puoi pagare comodamente alla consegna: zero anticipo e zero carta al momento dell'ordine.",
            c["fa2"],
        ),
        ("Nuvia™ è compatibile con il mio telefono?", text(c, "fq3", product)),
        (
            "Sì. Nuvia™ è compatibile sia con dispositivi Android che con iPhone, tramite la relativa app dedicata.",
            text(c, "fa3", product),
        ),
        ("Il vetro resiste davvero agli urti?", c["fq4"]),
        (
            "Sì, il vetro temperato anti-graffio e la cassa robusta sono progettati per proteggere l'orologio da urti, cadute accidentali e contatto con i liquidi nell'uso quotidiano.",
            c["fa4"],
        ),
        ("Cosa succede se non sono soddisfatto?", c["fq5"]),
        (
            "Hai 30 giorni di tempo per restituire il prodotto gratuitamente e ricevere il rimborso completo.",
            c["fa5"],
        ),
        ("Informazioni", c["info"]),
        ("Chi siamo", c["about"]),
        ("Contattaci", c["contact"]),
        ("Privacy Policy", c["privacy"]),
        ("Termini e Condizioni", c["terms"]),
        ("Cookie Policy", c["cookie"]),
        ("Politica di Spedizione", c["ship"]),
        ("Politica di Rimborso", c["refund"]),
        ("Contatti", c["contacts"]),
        ("Stati Uniti", c["country_us"]),
        ("Tutti i diritti riservati.", f'{c["rights"]}.'),
    ]
    kit_it = [
        "1 Smartwatch Nuvia™ con vetro temperato",
        "1 Cinturino di ricambio",
        "1 Caricabatterie magnetico",
        "1 Pellicola protettiva aggiuntiva",
        "Compatibilità Android e iPhone",
        "Coach AI di corsa incluso",
        "Manuale d'uso e certificato di garanzia",
        "2 anni di garanzia inclusa",
    ]
    for it_li, loc_li in zip(kit_it, c["kit_li"]):
        pairs.append((f"<li>{it_li}</li>", f"<li>{apply_product(loc_li, product)}</li>"))
    return pairs


def transform_index(html: str, offer: dict, c: dict) -> str:
    geo, slug = offer["geo"], offer["slug"]
    lang, product = offer["lang"], offer["product"]
    price, currency = offer["price"], offer["currency"]
    display = offer.get("display")
    now_s = fmt_price(price, currency, display)
    was_s = fmt_price(was_price(price), currency)

    out = html.replace('lang="it"', f'lang="{lang}"')
    out = out.replace(
        "https://gadgetshifthub.com/it/nuvia/",
        f"https://gadgetshifthub.com/{geo}/{slug}/",
    )
    out = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            f"  PRODUCT_SLUG: '{slug}',\n"
            f"  OFFER_ID: '{offer['offer_id']}',\n"
            f"  CURRENCY: '{currency}',\n"
            f"  PRICE: {price},\n"
            f"  OFFER_NAME: '{offer_name(offer)}',\n"
            f"  LP_ID: '{lp_id(offer)}',\n"
            f"  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',\n"
            f"  SUBMITTING_LABEL: '{c['submitting']}',\n"
            f"  COOKIE_TEXT: '{c['cookie_text']}',\n"
            f"  COOKIE_ACCEPT: '{c['cookie_accept']}',\n"
            f"  COOKIE_LEARN: '{c['cookie_learn']}'\n"
            "};"
        ),
        out,
        count=1,
        flags=re.S,
    )
    out = out.replace("<span class=\"was\">166 €</span>", f'<span class="was">{was_s}</span>')
    out = out.replace("<span class=\"now\">50 €</span>", f'<span class="now">{now_s}</span>')
    for old, new in index_replacements(c, product):
        out = out.replace(old, new)
    live_js = c["live_tpl"].format(n="${count}")
    out = out.replace(
        "el.innerHTML = `<strong>${count} persone</strong> stanno guardando questo prodotto ora`;",
        f"el.innerHTML = `{live_js}`;",
    )
    out = out.replace("/it/", f"/{geo}/")
    if product != "Nuvia™":
        out = out.replace("Nuvia™", product)
    out = inject_offer_markers(out, offer["offer_id"])
    return out


def transform_thank_you(html: str, offer: dict, c: dict) -> str:
    geo, slug = offer["geo"], offer["slug"]
    lang, product = offer["lang"], offer["product"]
    price, currency, cpa = offer["price"], offer["currency"], offer["cpa"]

    out = html.replace('lang="it"', f'lang="{lang}"')
    price_val = float(price)
    out = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        (
            "window.SITE_CONFIG = {\n"
            f"  GEO: '{geo}',\n"
            f"  PRODUCT_SLUG: '{slug}',\n"
            f"  OFFER_ID: '{offer['offer_id']}',\n"
            f"  CURRENCY: '{currency}',\n"
            f"  PRICE: {price_val},\n"
            "  META_PIXEL_ID: '',\n"
            "  GOOGLE_TAG_ID: '',\n"
            "  GOOGLE_ADS_CONVERSION_ID: '',\n"
            "  TY_CONVERSION_LABEL: '',\n"
            f"  COOKIE_TEXT: '{c['cookie_text']}',\n"
            f"  COOKIE_ACCEPT: '{c['cookie_accept']}',\n"
            f"  COOKIE_LEARN: '{c['cookie_learn']}'\n"
            "};"
        ),
        out,
        count=1,
        flags=re.S,
    )
    out = out.replace("trackPurchase(50.00, 'EUR')", f"trackPurchase({price}, '{currency}')")
    out = out.replace("'value': 15.0,", f"'value': {cpa},")
    out = out.replace(
        "Ordine ricevuto — Attendi la chiamata di conferma | Nuvia™",
        text(c, "ty_title", product),
    )
    out = out.replace(
        "Il tuo ordine Nuvia™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.",
        text(c, "ty_desc", product),
    )
    out = out.replace("Il tuo ordine è stato registrato con successo!", c["ty_h1"])
    out = out.replace(
        "Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
        c["ty_sub"],
    )
    out = out.replace(
        "Il team gadgetshifthub al lavoro: call center e logistica COD",
        c["ty_alt"],
    )
    out = out.replace("👇 Cosa devi fare adesso", c["ty_eyebrow"])
    out = out.replace("📞 Rispondi alla chiamata di conferma", c["ty_action_title"])
    out = out.replace(
        "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
        c["ty_action_body"],
    )
    out = out.replace(
        "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        c["ty_action_warn"],
    )
    out = out.replace("🕒 Orari di contatto", c["ty_hours_h"])
    out = out.replace("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", c["ty_hours"])
    out = out.replace("📋 Cosa succede dopo", c["ty_next_h"])
    it_steps = [
        "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
        "Il tuo ordine verrà spedito entro <strong>24–48 ore</strong>",
        "Consegna a domicilio e <strong>pagamento alla consegna</strong>",
    ]
    for it_s, loc_s in zip(it_steps, c["ty_steps"]):
        out = out.replace(f"<li>{it_s}</li>", f"<li>{loc_s}</li>")
    it_badges = ("🔒 Pagamento alla consegna", "🛡️ Garanzia 24 mesi", "🔐 Protezione SSL")
    for it_b, loc_b in zip(it_badges, c["ty_badges"]):
        out = out.replace(it_b, loc_b)
    out = out.replace("Informazioni", c["info"])
    out = out.replace("Chi siamo", c["about"])
    out = out.replace("Contattaci", c["contact"])
    out = out.replace("Privacy Policy", c["privacy"])
    out = out.replace("Termini e Condizioni", c["terms"])
    out = out.replace("Cookie Policy", c["cookie"])
    out = out.replace("Politica di Spedizione", c["ship"])
    out = out.replace("Politica di Rimborso", c["refund"])
    out = out.replace('<h4 class="site-footer__heading">Contatti</h4>', f'<h4 class="site-footer__heading">{c["contacts"]}</h4>')
    out = out.replace("Stati Uniti", c["country_us"])
    out = out.replace("Tutti i diritti riservati.", f'{c["rights"]}.')
    out = out.replace("/it/", f"/{geo}/")
    if product != "Nuvia™":
        out = out.replace("Nuvia™", product)
    marker = f"<!-- Google Ads Purchase conversion — value = CPA/CPL EUR for offer #{offer['offer_id']} -->"
    if marker not in out:
        out = out.replace(
            "<!-- Event snippet for Acquisto conversion page -->",
            f"{marker}\n<!-- Event snippet for Acquisto conversion page -->",
        )
    ty_marker = f"<!-- Offer #{offer['offer_id']} -->"
    if ty_marker not in out:
        out = out.replace("<body>", f"<body>\n\n  {ty_marker}", 1)
    return out


def main() -> list[str]:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    it_index = IT_INDEX.read_text(encoding="utf-8")
    it_ty = IT_TY.read_text(encoding="utf-8")
    urls: list[str] = []
    created = 0

    for offer in OFFERS:
        lang = offer["lang"]
        if lang not in COPY:
            raise KeyError(f"Missing COPY for lang {lang}")
        c = COPY[lang]
        out_dir = ROOT / offer["geo"] / offer["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)

        index_html = transform_index(it_index, offer, c)
        index_html = insert_ai_notice_in_site_footer(index_html, offer["lang"])
        ty_html = transform_thank_you(it_ty, offer, c)

        (out_dir / "index.html").write_text(index_html, encoding="utf-8")
        (out_dir / "thank-you.html").write_text(ty_html, encoding="utf-8")
        created += 2
        urls.append(f"https://gadgetshifthub.com/{offer['geo']}/{offer['slug']}/")
        print(
            f"OK {offer['geo']}/{offer['slug']}/  "
            f"price={fmt_price(offer['price'], offer['currency'], offer.get('display'))}  "
            f"was={fmt_price(was_price(offer['price']), offer['currency'])}  "
            f"offer=#{offer['offer_id']}",
            flush=True,
        )

    print(f"\nCreated {created} files ({len(OFFERS)} index + {len(OFFERS)} thank-you)")
    if created != 22:
        print(f"WARNING: expected 22 files, got {created}")
    return urls


if __name__ == "__main__":
    main()
