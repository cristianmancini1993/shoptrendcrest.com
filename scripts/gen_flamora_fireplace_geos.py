#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate FLAMORA electric fireplace landings + TYP for campaign geos (from it/flamora)."""
from __future__ import annotations

import html
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer
IT_INDEX = ROOT / "it/flamora/index.html"
IT_TY = ROOT / "it/flamora/thank-you.html"

FORM_UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
FORM_WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
FORM_KEY = "a8f3f892387f175bf6e35938d46afdb47069fd18"

OFFERS = [
    {"geo": "pl", "lang": "pl", "offer_id": "1987", "currency": "PLN", "price": 399, "cpa": 19, "phone": "+48 512 345 678"},
    {"geo": "cz", "lang": "cs", "offer_id": "2400", "currency": "CZK", "price": 2290, "cpa": 18, "phone": "+420 601 123 456"},
    {"geo": "es", "lang": "es", "offer_id": "2635", "currency": "EUR", "price": 96, "cpa": 18, "phone": "+34 612 345 678"},
    {"geo": "pt", "lang": "pt", "offer_id": "2636", "currency": "EUR", "price": 112, "cpa": 18, "phone": "+351 912 345 678"},
    {"geo": "de", "lang": "de", "offer_id": "2665", "currency": "EUR", "price": 89, "cpa": 18, "phone": "+49 170 1234567"},
    {"geo": "hu", "lang": "hu", "offer_id": "2668", "currency": "HUF", "price": 29999, "cpa": 16, "phone": "+36 30 123 4567"},
    {"geo": "sk", "lang": "sk", "offer_id": "4357", "currency": "EUR", "price": 97, "cpa": 20, "phone": "+421 901 123 456"},
    {"geo": "lv", "lang": "lv", "offer_id": "4358", "currency": "EUR", "price": 99, "cpa": 15, "phone": "+371 2123 4567"},
]

try:
    from _flamora_network_forms import FORM_META as _FORM_META
except ImportError:
    _FORM_META = {}

LP_BY_OFFER = {meta["offer"]: meta["lp"] for meta in _FORM_META.values()}


def load_copy() -> dict:
    path = Path(__file__).with_name("_flamora_fireplace_copy_data.py")
    spec = importlib.util.spec_from_file_location("_flamora_fireplace_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


COPY = load_copy()


def slug_for(offer: dict) -> str:
    return f"flamora-{offer['offer_id']}"


def lp_for(offer_id: str) -> str:
    return LP_BY_OFFER.get(offer_id, offer_id)


def was_price(now: float) -> float:
    return now * 2


def fmt_price(amount: float, currency: str) -> str:
    if currency == "HUF":
        whole = int(round(amount))
        s = f"{whole:,}".replace(",", " ")
        return f"{s} Ft"
    if currency == "CZK":
        whole = int(round(amount))
        s = f"{whole:,}".replace(",", " ")
        return f"{s} Kč"
    if currency == "PLN":
        return f"{int(amount)} zł"
    if float(amount).is_integer():
        return f"{int(amount)} €"
    return f"{amount:.2f}".replace(".", ",") + " €"


def base_url(offer: dict) -> str:
    return f"https://gadgetshifthub.com/{offer['geo']}/{slug_for(offer)}/"


def ty_url(offer: dict) -> str:
    return f"{base_url(offer)}thank-you.html"


def apply_pairs(html: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        if old not in html:
            raise KeyError(f"Missing template fragment: {old[:100]}...")
        html = html.replace(old, new)
    return html


def index_pairs(c: dict, offer: dict) -> list[tuple[str, str]]:
    was = fmt_price(was_price(offer["price"]), offer["currency"])
    now = fmt_price(offer["price"], offer["currency"])
    price_block = (
        f'<span class="was">{was}</span><span class="now">{now}</span>'
        f'<span class="disc">-50%</span>'
    )
    ship = f'<span class="ship">{c["ship_cod"]}</span>'
    price_block_ship = price_block + ship
    slug = slug_for(offer)
    geo = offer["geo"]
    base = base_url(offer)
    ty = ty_url(offer)
    oid = offer["offer_id"]
    lp = lp_for(oid)

    faq2_a = c["faq2_a"].replace("{price}", now)
    cmp_buy = c["cmp_buy"].replace("{price}", now)
    form_h2 = c["form_h2"].replace("{price}", now)
    kit_ship = c["kit_i6"].replace("{price}", now)

    live = c["live_tpl"].replace("{n}", "38")

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ('content="2635"', f'content="{oid}"'),
        ("FLAMORA™ — Camino elettrico con app e telecomando | 96 €", c["title"].replace("{price}", now)),
        (
            "Caminetto elettrico a colonna con fiamma LED, app e telecomando. 96 €, pagamento alla consegna in Italia.",
            c["meta_desc"].replace("{price}", now),
        ),
        (
            '<link href="https://gadgetshifthub.com/it/flamora/" rel="canonical"/>',
            f'<link href="{base}" rel="canonical"/>',
        ),
        (
            '<meta content="https://gadgetshifthub.com/it/flamora/" property="og:url"/>',
            f'<meta content="{base}" property="og:url"/>',
        ),
        ("FLAMORA™ — Camino elettrico con app e telecomando", c["og_title"]),
        (
            "Effetto fiamma senza legna né fumi. 96 € con pagamento alla consegna.",
            c["og_desc"].replace("{price}", now),
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'flamora',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 96,", f"  PRICE: {offer['price']},"),
        ("  OFFER_NAME: 'FLAMORA IT #2635',", f"  OFFER_NAME: 'FLAMORA {geo.upper()} #{oid}',"),
        ("  LP_ID: 'it-2635',", f"  LP_ID: '{geo}-{oid}',"),
        ("  FORM_OFFER: '2635',", f"  FORM_OFFER: '{oid}',"),
        ("  FORM_LP: '2662',", f"  FORM_LP: '{lp}',"),
        (
            "  THANKYOU_URL: 'https://gadgetshifthub.com/it/flamora/thank-you.html',",
            f"  THANKYOU_URL: '{ty}',",
        ),
        ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", c["cookie_text"]),
        ("COOKIE_ACCEPT: 'Accetta',", f"COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("COOKIE_LEARN: 'Scopri di più'", f"COOKIE_LEARN: '{c['cookie_learn']}'"),
        ("🔥 SOLO OGGI: -50% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA 🔥", c["topbar"]),
        (
            "<strong>4,8/5</strong> — Oltre <strong>8.730</strong> persone hanno già scelto un camino elettrico per il proprio soggiorno",
            c["rating"],
        ),
        ("🎁 IN OMAGGIO: TELECOMANDO + APP DI CONTROLLO", c["gift"]),
        (
            "Camino senza legna, fumo né cenere. <span class=\"hl\">Controlla FLAMORA™ dallo smartphone!</span>",
            c["h1"],
        ),
        (
            "Fiamma viva senza legna né fuliggine! Imposta temperatura e timer dall'app, blocca i tasti con il telecomando e goditi il calore. Basta una presa e il camino è pronto!",
            c["lead"],
        ),
        (
            'alt="Camino elettrico FLAMORA con app e telecomando"',
            f'alt="{c["alt_hero"]}"',
        ),
        (
            '<span class="was">192 €</span><span class="now">96 €</span><span class="disc">-50%</span>',
            price_block,
        ),
        ('<span class="ship">contrassegno</span>', ship),
        ("ORDINA ORA →", c["cta_order"]),
        ("🔒 Contrassegno · Zero anticipi · Paghi quando ricevi il pacco", c["form_note_hero"]),
        ("<h4>App dedicata</h4><p>Regoli temperatura, effetto fiamma, modalità e timer dal telefono</p>", f'<h4>{c["f1_h"]}</h4><p>{c["f1_p"]}</p>'),
        (
            "<h4>Telecomando in dotazione</h4><p>On/off, fiamma, timer, ventola, blocco bambini e temperatura</p>",
            f'<h4>{c["f2_h"]}</h4><p>{c["f2_p"]}</p>',
        ),
        ("<h4>Fiamma realistica</h4><p>LED con ceppi decorativi, zero combustione</p>", f'<h4>{c["f3_h"]}</h4><p>{c["f3_p"]}</p>'),
        ("<h4>Contrassegno</h4><p>Saldi il corriere al momento della consegna</p>", f'<h4>{c["f4_h"]}</h4><p>{c["f4_p"]}</p>'),
        ("⏰ Lo sconto del 50% resta attivo ancora per", c["countdown"]),
        ('<div class="lbl">Ore</div>', f'<div class="lbl">{c["hours"]}</div>'),
        ('<div class="lbl">Min</div>', f'<div class="lbl">{c["mins"]}</div>'),
        ('<div class="lbl">Sec</div>', f'<div class="lbl">{c["secs"]}</div>'),
        (
            '<span class="left">Stock disponibile</span>\n<span class="right">Scorte limitate</span>',
            f'<span class="left">{c["stock_l"]}</span>\n<span class="right">{c["stock_r"]}</span>',
        ),
        (
            'data-live="&lt;strong&gt;{n} persone&lt;/strong&gt; stanno valutando questa offerta in questo momento" id="liveCount"><strong>38 persone</strong> stanno valutando questa offerta in questo momento',
            f'data-live="{html.escape(c["live_tpl"])}" id="liveCount">{live}',
        ),
        ("<h2>Richiedi il camino a 96 €</h2>", f"<h2>{form_h2}</h2>"),
        (
            "<p>Inserisci i tre dati richiesti: ti richiamiamo entro 24 ore per fissare la consegna, senza pagare nulla ora.</p>",
            f"<p>{c['form_p']}</p>",
        ),
        ("<label for=\"name\">Nome e cognome*</label>", f'<label for="name">{c["label_name"]}</label>'),
        ('placeholder="Mario Rossi"', f'placeholder="{c["ph_name"]}"'),
        ("<label for=\"tel\">Numero di telefono*</label>", f'<label for="tel">{c["label_tel"]}</label>'),
        ('placeholder="+39 333 123 4567"', f'placeholder="{offer["phone"]}"'),
        ("<label for=\"street-address\">Indirizzo di consegna*</label>", f'<label for="street-address">{c["label_addr"]}</label>'),
        ('placeholder="Via Roma 10, 00100 Roma"', f'placeholder="{c["ph_addr"]}"'),
        ('<input name="offer" type="hidden" value="2635"/>', f'<input name="offer" type="hidden" value="{oid}"/>'),
        ('<input name="lp" type="hidden" value="2662">', f'<input name="lp" type="hidden" value="{lp}">'),
        (
            'value="https://gadgetshifthub.com/it/flamora/thank-you.html"',
            f'value="{ty}"',
        ),
        ("Invia ordine", c["btn_submit"]),
        ("🔒 Nessun anticipo · Nessuna carta · Paghi solo alla consegna", c["form_note"]),
        ("01 — Come lo comandi", c["w1_eye"]),
        ("Smartphone, telecomando o pulsanti sul piano superiore", c["w1_h"]),
        ('<span class="tag">App</span><span class="tag">Telecomando</span><span class="tag">Tasti touch</span>', f'<span class="tag">{c["w1_t1"]}</span><span class="tag">{c["w1_t2"]}</span><span class="tag">{c["w1_t3"]}</span>'),
        (
            "Con l'app dedicata controlli setpoint e temperatura ambiente, oltre all'accensione, effetto fiamma, modalità operativa e timer. Il telecomando replica le funzioni e aggiunge il blocco dei tasti.",
            c["w1_p"],
        ),
        (
            "Puoi accendere solo la fiamma per l'atmosfera, oppure anche il riscaldamento quando ti serve.",
            c["w1_i"],
        ),
        ('alt="Camino con effetto fiamma LED e ceppi"', f'alt="{c["alt_w2"]}"'),
        ("02 — Effetto fiamma", c["w2_eye"]),
        ("L'aspetto del fuoco, zero canna fumaria", c["w2_h"]),
        ('<span class="tag">Niente legna</span><span class="tag">Niente fumi</span><span class="tag">Niente cenere</span>', f'<span class="tag">{c["w2_t1"]}</span><span class="tag">{c["w2_t2"]}</span><span class="tag">{c["w2_t3"]}</span>'),
        (
            "La struttura bianca espone la fiamma LED dietro il vetro, con ceppi e prese d'aria sotto la vetrina. Niente opere murarie, deposito legna o fuliggine in casa.",
            c["w2_p"],
        ),
        (
            "Lo posizioni dove vuoi, lo attacchi e lo usi: tieni sgombra la griglia di ventilazione sul retro.",
            c["w2_i"],
        ),
        ('alt="App, telecomando e pannello del camino"', f'alt="{c["alt_w3"]}"'),
        ("03 — Uso quotidiano", c["w3_eye"]),
        ("Programmi l'orario e la temperatura, senza lasciarlo sempre acceso", c["w3_h"]),
        ('<span class="tag">Timer</span><span class="tag">Termostato</span><span class="tag">Blocco tasti</span>', f'<span class="tag">{c["w3_t1"]}</span><span class="tag">{c["w3_t2"]}</span><span class="tag">{c["w3_t3"]}</span>'),
        (
            "Sul display dell'app leggi valore impostato e temperatura reale della stanza. Il timer definisce la durata; il blocco sul telecomando impedisce tocchi involontari.",
            c["w3_p"],
        ),
        (
            "Wattaggio, metratura consigliata e fasce del timer sono nel manuale tecnico: non li pubblichiamo finché non sono validati.",
            c["w3_i"],
        ),
        ("SÌ, VOGLIO L'OFFERTA →", c["cta_offer"]),
        ("A colonna elettrico, non a combustibile", c["cmp_label"]),
        ("Camino a legna o elettrico a colonna?", c["cmp_h2"]),
        ('aria-label="Confronto camino a legna e modello elettrico"', f'aria-label="{c["cmp_aria"]}"'),
        ("<th>Camino a legna</th><th class=\"highlight\">Elettrico</th>", f'<th>{c["th_wood"]}</th><th class="highlight">{c["th_elec"]}</th>'),
        ("<td>Alimentazione</td><td>Legna, ripostiglio e rifornimenti</td><td class=\"win\">Solo presa di corrente</td>", f'<td>{c["cmp_r1_l"]}</td><td>{c["cmp_r1_a"]}</td><td class="win">{c["cmp_r1_b"]}</td>'),
        ("<td>Emissioni</td><td>Fumi, cenere e sporco</td><td class=\"win\">Nessuna combustione</td>", f'<td>{c["cmp_r2_l"]}</td><td>{c["cmp_r2_a"]}</td><td class="win">{c["cmp_r2_b"]}</td>'),
        ("<td>Montaggio</td><td>Spesso canna fumaria</td><td class=\"win\">Libero da terra, spostabile</td>", f'<td>{c["cmp_r3_l"]}</td><td>{c["cmp_r3_a"]}</td><td class="win">{c["cmp_r3_b"]}</td>'),
        ("<td>Gestione</td><td>Sul posto</td><td class=\"win\">App, telecomando e tasti in alto</td>", f'<td>{c["cmp_r4_l"]}</td><td>{c["cmp_r4_a"]}</td><td class="win">{c["cmp_r4_b"]}</td>'),
        ("<td>Solo effetto fiamma</td><td>Non disponibile</td><td class=\"win\">Fiamma e calore indipendenti</td>", f'<td>{c["cmp_r5_l"]}</td><td>{c["cmp_r5_a"]}</td><td class="win">{c["cmp_r5_b"]}</td>'),
        ("<td>Acquisto</td><td>Spesso pagamento anticipato</td><td class=\"win\">96 € in contrassegno</td>", f'<td>{c["cmp_r6_l"]}</td><td>{c["cmp_r6_a"]}</td><td class="win">{cmp_buy}</td>'),
        ("Tante famiglie lo hanno già scelto: ecco cosa dicono i clienti.", c["test_h2"]),
        ('alt="Cliente con telecomando e confezione FLAMORA"', f'alt="{c["alt_t1"]}"'),
        ("Dalla scatola alla fiamma in pochi minuti.", c["t1_h"]),
        (
            "«Come in foto: l'ho tolto dall'imballo, collegato e acceso subito l'effetto fuoco. Niente canna fumaria, niente legna da comprare.»",
            c["t1_p"],
        ),
        ("Marco B. — Milano, Cliente verificato", c["t1_auth"]),
        ('alt="Kit con scatola, telecomando e manuale"', f'alt="{c["alt_t2"]}"'),
        ("Tutto nel pacco, niente pezzi mancanti.", c["t2_h"]),
        (
            "«Camino bianco, telecomando e manuale tutti insieme. Dopo l'unboxing l'ho messo in soggiorno: il telecomando è già pronto per accendere fiamma e calore.»",
            c["t2_p"],
        ),
        ("Giulia R. — Roma, Cliente verificata", c["t2_auth"]),
        ('alt="Camino da terra in soggiorno, vista frontale"', f'alt="{c["alt_t3"]}"'),
        ("In salotto fa davvero atmosfera.", c["t3_h"]),
        (
            "«Accesa la fiamma LED sembra un camino vero: gli ospiti restano a guardarla. La colonna bianca sta bene nel soggiorno e non serve alcun lavoro al muro.»",
            c["t3_p"],
        ),
        ("Elena F. — Napoli, Cliente verificata", c["t3_auth"]),
        (
            '    <span class="eyebrow">Nel pacco</span>\n    <h2>Tutto il kit pronto all\'uso</h2>',
            f'    <span class="eyebrow">{c["kit_eye"]}</span>\n    <h2>{c["kit_h2"]}</h2>',
        ),
        ('alt="Camino elettrico con app e telecomando"', f'alt="{c["alt_kit"]}"'),
        ("Caminetto elettrico a colonna bianco, finitura liscia", c["kit_i1"]),
        ("Simulazione fiamma LED con ceppi decorativi", c["kit_i2"]),
        ("Telecomando con funzione blocco", c["kit_i3"]),
        ("App per temperatura, fiamma, modalità e timer", c["kit_i4"]),
        ("Comandi rapidi sui tasti superiori", c["kit_i5"]),
        ("Spedizione · contrassegno a 96 €", kit_ship),
        ("<h2>Domande frequenti</h2>", f"<h2>{c['faq_h2']}</h2>"),
        ("<span>Qual è la procedura d'ordine?</span>", f"<span>{c['faq1_q']}</span>"),
        (
            "<p>Lascia nome, telefono e indirizzo nel modulo: ti richiamiamo per confermare spedizione e dettagli.</p>",
            f"<p>{c['faq1_a']}</p>",
        ),
        ("<span>Accettate il contrassegno?</span>", f"<span>{c['faq2_q']}</span>"),
        ("<p>Sì, paghi 96 € in contanti al corriere quando ritiri il pacco.</p>", f"<p>{faq2_a}</p>"),
        ("<span>Come ottengo assistenza?</span>", f"<span>{c['faq3_q']}</span>"),
        (
            "<p>Usa il form oppure scrivi a info@gadgetshifthub.com: un operatore ti risponde su prodotto e offerta.</p>",
            f"<p>{c['faq3_a']}</p>",
        ),
        ("<span>Come vengono trattati i miei dati?</span>", f"<span>{c['faq4_q']}</span>"),
        (
            "<p>Le regole su privacy e consegna sono descritte nelle pagine legali del sito, inclusa l'informativa privacy.</p>",
            f"<p>{c['faq4_a']}</p>",
        ),
        ("<span>Posso restituire il prodotto?</span>", f"<span>{c['faq5_q']}</span>"),
        (
            "<p>Vale la policy resi pubblicata su gadgetshifthub.com, con tempi e condizioni indicati lì.</p>",
            f"<p>{c['faq5_a']}</p>",
        ),
        ("Soluzioni per la casa, spedizione veloce e pagamento in contrassegno.", c["footer_blurb"]),
        ("Informazioni", c["footer_info"]),
        ("Chi siamo", c["footer_about"]),
        ("Contattaci", c["footer_contact"]),
        ("Informativa sulla privacy", c["footer_privacy"]),
        ("Termini e condizioni", c["footer_terms"]),
        ("Politica sui cookie", c["footer_cookie"]),
        ("Politica di spedizione", c["footer_shipping"]),
        ("Politica di reso", c["footer_refund"]),
        ('<h4 class="site-footer__heading">Contatti</h4>', f'<h4 class="site-footer__heading">{c["footer_contacts"]}</h4>'),
        ("Stati Uniti", c["footer_us"]),
        ("Tutti i diritti riservati.", c["footer_rights"]),
        ('href="/it/', f'href="/{geo}/'),
        ("<!-- Offer #2635", f"<!-- Offer #{oid}"),
    ]


def ty_pairs(c: dict, offer: dict) -> list[tuple[str, str]]:
    geo = offer["geo"]
    slug = slug_for(offer)
    oid = offer["offer_id"]
    base = base_url(offer)
    ty = ty_url(offer)
    cur = offer["currency"]
    price = offer["price"]
    cpa = offer["cpa"]

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ('content="2635"', f'content="{oid}"'),
        ("Ordine ricevuto — Attendi la chiamata di conferma | FLAMORA™", c["ty_title"]),
        ("Il tuo ordine FLAMORA™ è stato ricevuto. Resta solo un passaggio: rispondere alla chiamata del nostro operatore per confermare i dati.", c["ty_meta"]),
        ("https://gadgetshifthub.com/it/flamora/thank-you.html", ty),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'flamora',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{cur}',"),
        ("  PRICE: 96,", f"  PRICE: {price},"),
        ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", c["cookie_text"]),
        ("COOKIE_ACCEPT: 'Accetta',", f"COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("COOKIE_LEARN: 'Scopri di più'", f"COOKIE_LEARN: '{c['cookie_learn']}'"),
        ("window.trackPurchase(96, 'EUR');", f"window.trackPurchase({cpa}, '{cur}');"),
        ("Il tuo ordine è stato registrato correttamente!", c["ty_h1"]),
        (
            "Perfetto — il tuo ordine è in lavorazione. Per completarlo e avviare la spedizione manca solo <strong>la conferma telefonica</strong>.",
            c["ty_sub"],
        ),
        ('alt="Il team gadgetshifthub al lavoro: call center e logistica COD"', f'alt="{c["ty_img_alt"]}"'),
        ("👇 Cosa fare adesso", c["ty_act_eye"]),
        ("📞 Rispondi alla chiamata di conferma", c["ty_act_title"]),
        (
            "Un nostro operatore ti chiamerà <strong>nelle prossime ore</strong> per confermare il tuo ordine e i dettagli di consegna.",
            c["ty_act_body"],
        ),
        (
            "Se non rispondi, l'ordine non potrà essere confermato e verrà annullato.",
            c["ty_act_warn"],
        ),
        ("🕒 Orari di contatto", c["ty_hours_h"]),
        ("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", c["ty_hours"]),
        ("📋 Cosa succede dopo", c["ty_steps_h"]),
        ("Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>", c["ty_s1"]),
        ("Il tuo ordine verrà preparato entro <strong>24–48 ore</strong>", c["ty_s2"]),
        ("Ricevi il pacco a domicilio e <strong>paghi alla consegna</strong>", c["ty_s3"]),
        ("🔒 Pagamento alla consegna", c["ty_b1"]),
        ("🛡️ Garanzia 24 mesi", c["ty_b2"]),
        ("🔐 Protezione SSL", c["ty_b3"]),
        ("Informazioni", c["footer_info"]),
        ("Chi siamo", c["footer_about"]),
        ("Contattaci", c["footer_contact"]),
        ("Privacy Policy", c["footer_privacy"]),
        ("Termini e Condizioni", c["footer_terms"]),
        ("Cookie Policy", c["footer_cookie"]),
        ("Politica di Spedizione", c["footer_shipping"]),
        ("Politica di Rimborso", c["footer_refund"]),
        ('<h4 class="site-footer__heading">Contatti</h4>', f'<h4 class="site-footer__heading">{c["footer_contacts"]}</h4>'),
        ("Stati Uniti", c["footer_us"]),
        ("Tutti i diritti riservati.", c["footer_rights"]),
        ('href="/it/', f'href="/{geo}/'),
        ("<!-- Offer #2635", f"<!-- Offer #{oid}"),
    ]


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    import _patch_flamora_locales as _loc

    _loc.patch_all()
    copy = load_copy()

    it_index = IT_INDEX.read_text(encoding="utf-8")
    it_ty = IT_TY.read_text(encoding="utf-8")

    for offer in OFFERS:
        lang = offer["lang"]
        if lang not in copy:
            raise KeyError(f"Missing COPY for lang={lang}")
        c = copy[lang]
        rel = f"{offer['geo']}/{slug_for(offer)}"
        out_dir = ROOT / rel
        out_dir.mkdir(parents=True, exist_ok=True)

        idx = apply_pairs(it_index, index_pairs(c, offer))
        idx = insert_ai_notice_in_site_footer(idx, offer["lang"])
        (out_dir / "index.html").write_text(idx, encoding="utf-8")

        ty = apply_pairs(it_ty, ty_pairs(c, offer))
        (out_dir / "thank-you.html").write_text(ty, encoding="utf-8")
        print(f"Wrote {rel}/index.html + thank-you.html")

    import update_flamora_fireplace_forms as _patch_forms

    _patch_forms.main()
    print("done")


if __name__ == "__main__":
    main()
