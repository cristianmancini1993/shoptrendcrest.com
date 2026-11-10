#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate VALMORA cookware landing + thank-you pages for campaign geos."""
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
IT_INDEX = ROOT / "it/valmora/index.html"
IT_TY = ROOT / "it/valmora/thank-you.html"

OFFERS = [
    {"geo": "ro", "lang": "ro", "offer_id": "1387", "currency": "RON", "price": 389, "cpa": 16, "phone": "+40 721 234 567"},
    {"geo": "pt", "lang": "pt", "offer_id": "1476", "currency": "EUR", "price": 99, "cpa": 16, "phone": "+351 912 345 678"},
    {"geo": "si", "lang": "sl", "offer_id": "1875", "currency": "EUR", "price": 89, "cpa": 14, "phone": "+386 31 234 567"},
    {"geo": "hr", "lang": "hr", "offer_id": "1876", "currency": "EUR", "price": 89, "cpa": 15, "phone": "+385 91 234 5678"},
    {"geo": "hu", "lang": "hu", "offer_id": "2409", "currency": "HUF", "price": 31999, "cpa": 18, "phone": "+36 30 123 4567"},
    {"geo": "es", "lang": "es", "offer_id": "3176", "currency": "EUR", "price": 89, "cpa": 17, "phone": "+34 612 345 678"},
    {"geo": "de", "lang": "de", "offer_id": "3177", "currency": "EUR", "price": 109, "cpa": 22, "phone": "+49 170 1234567"},
    {"geo": "lt", "lang": "lt", "offer_id": "3178", "currency": "EUR", "price": 89, "cpa": 17, "phone": "+370 612 34567"},
    {"geo": "pl", "lang": "pl", "offer_id": "3179", "currency": "PLN", "price": 399, "cpa": 19, "phone": "+48 512 345 678"},
    {"geo": "cz", "lang": "cs", "offer_id": "3180", "currency": "CZK", "price": 2199, "cpa": 17, "phone": "+420 601 123 456"},
    {"geo": "sk", "lang": "sk", "offer_id": "3702", "currency": "EUR", "price": 89, "cpa": 16, "phone": "+421 901 123 456"},
    {"geo": "lv", "lang": "lv", "offer_id": "4095", "currency": "EUR", "price": 99, "cpa": 19, "phone": "+371 2123 4567"},
]

FORM_UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"


def load_copy() -> dict:
    path = Path(__file__).with_name("_valmora_copy_data.py")
    spec = importlib.util.spec_from_file_location("_valmora_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


COPY = load_copy()


def slug_for(offer: dict) -> str:
    return f"valmora-{offer['offer_id']}"


def was_price(now: float) -> float:
    return now * 2


def fmt_price(amount: float, currency: str) -> str:
    if currency == "RON":
        return f"{int(amount)} lei"
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", ".") + " Ft"
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Kč"
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
            raise KeyError(f"Missing template fragment: {old[:80]}...")
        html = html.replace(old, new)
    return html


def index_pairs(c: dict, offer: dict) -> list[tuple[str, str]]:
    was = fmt_price(was_price(offer["price"]), offer["currency"])
    now = fmt_price(offer["price"], offer["currency"])
    price_block = f'<span class="was">{was}</span><span class="now">{now}</span><span class="pct">-50%</span>'
    faq2_a = c["faq2_a"].replace("{price}", now)
    slug = slug_for(offer)
    geo = offer["geo"]
    base = base_url(offer)
    ty = ty_url(offer)

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ("VALMORA™ — Set di pentole in acciaio inox a 3 strati", c["title"]),
        (
            'Scopri VALMORA™: il set completo in acciaio inox a 3 strati che aiuta a distribuire il calore in modo omogeneo. Adatto anche a induzione e lavastoviglie.',
            c["description"],
        ),
        ("VALMORA™ — Cottura uniforme su ogni piano", c["title"]),
        (
            "Un set completo in acciaio inox a 3 strati: calore distribuito meglio, pulizia semplice e compatibilità con l'induzione.",
            c["og_description"],
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'valmora',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 74.0,", f"  PRICE: {offer['price']},"),
        ("  OFFER_NAME: 'VALMORA IT',", f"  OFFER_NAME: 'VALMORA {geo.upper()} #{offer['offer_id']}',"),
        ("  LP_ID: 'it-valmora-v1',", f"  LP_ID: '{geo}-{offer['offer_id']}',"),
        ("  FORM_OFFER: '',", f"  FORM_OFFER: '{offer['offer_id']}',"),
        ("  FORM_LP: '',", "  FORM_LP: '',"),
        (
            "  FORM_WEBHOOK: 'https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh',",
            "  FORM_WEBHOOK: '',",
        ),
        ("  FORM_KEY: '',", "  FORM_KEY: '',"),
        ("  THANKYOU_URL: 'https://gadgetshifthub.com/it/valmora/thank-you.html',", f"  THANKYOU_URL: '{ty}',"),
        ("https://gadgetshifthub.com/it/valmora/", base),
        ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", c["cookie_text"]),
        ("COOKIE_ACCEPT: 'Accetta',", f"COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("COOKIE_LEARN: 'Scopri di più'", f"COOKIE_LEARN: '{c['cookie_learn']}'"),
        ("🔥 SOLO OGGI: -50% SUL SET COMPLETO VALMORA™ 🔥", c["topbar"]),
        ("<strong>4,8/5</strong> — Più di <strong>6.200</strong> clienti soddisfatti", c["rating"]),
        ("🛡️ Reso entro 30 giorni + consegna rapida", c["gift"]),
        (
            'Attenzione: fino a <span class="hl">9.000 microplastiche</span> possono finire nel cibo. Proteggi la tua cucina oggi.',
            c["h1_m"],
        ),
        (
            'Attenzione: le padelle antiaderenti in teflon possono rilasciare fino a <span class="hl">9.000 particelle di microplastica</span> nel cibo. Proteggi la tua cucina oggi.',
            c["h1_d"],
        ),
        (
            "<strong>VALMORA™</strong> — acciaio inox a 3 strati con anima in alluminio, senza PTFE e PFOA. Nessun rivestimento che si consuma, calore distribuito su tutta la base e resistenza pensata per durare. Garanzia ufficiale di 2 anni.",
            c["lead"],
        ),
        ('alt="Set completo VALMORA™ con coperchi in vetro e manici in legno"', f'alt="{c["alt_hero"]}"'),
        ('<span class="was">148€</span><span class="now">74€</span><span class="pct">-50%</span>', price_block),
        ("SÌ, VOGLIO VALMORA™ →", c["cta"]),
        ("🔒 Consegna rapida · Pagamento alla consegna · Reso entro 30 giorni", c["form_note_hero"]),
        ("<h4>Consegna rapida</h4><p>Spedizione in tutta Italia</p>", f'<h4>{c["f1_h"]}</h4><p>{c["f1_p"]}</p>'),
        ("<h4>Ordine sicuro</h4><p>Dati protetti durante l'acquisto</p>", f'<h4>{c["f2_h"]}</h4><p>{c["f2_p"]}</p>'),
        ("<h4>Qualità verificata</h4><p>Materiali solidi e durevoli</p>", f'<h4>{c["f3_h"]}</h4><p>{c["f3_p"]}</p>'),
        ("<h4>30 giorni per il reso</h4><p>Procedura semplice e veloce</p>", f'<h4>{c["f4_h"]}</h4><p>{c["f4_p"]}</p>'),
        ("⏰ L'offerta -50% scade tra", c["countdown"]),
        ('<div class="lbl">Ore</div>', f'<div class="lbl">{c["hours"]}</div>'),
        ('<div class="lbl">Min</div>', f'<div class="lbl">{c["mins"]}</div>'),
        ('<div class="lbl">Sec</div>', f'<div class="lbl">{c["secs"]}</div>'),
        ('<span class="left">Disponibilità</span><span class="right">Restano pochi set in magazzino</span>', f'<span class="left">{c["stock_l"]}</span><span class="right">{c["stock_r"]}</span>'),
        (
            'data-live="&lt;strong&gt;{n} persone&lt;/strong&gt; stanno guardando VALMORA™ adesso" id="liveCount"><strong>34 persone</strong> stanno guardando VALMORA™ adesso',
            f'data-live="{html.escape(c["live_tpl"])}" id="liveCount">{c["live_tpl"].replace("{n}", "34")}',
        ),
        ("<h2>Completa il tuo ordine</h2>", f"<h2>{c['form_h2']}</h2>"),
        (
            "<p>Inserisci i tuoi dati: il nostro team ti chiamerà per verificare l'ordine e concordare la consegna.</p>",
            f"<p>{c['form_p']}</p>",
        ),
        ("<label for=\"name\">Nome e cognome*</label>", f'<label for="name">{c["label_name"]}</label>'),
        ('placeholder="Mario Rossi"', f'placeholder="{c["ph_name"]}"'),
        ("<label for=\"tel\">Numero di telefono*</label>", f'<label for="tel">{c["label_tel"]}</label>'),
        ('placeholder="+39 333 123 4567"', f'placeholder="{offer["phone"]}"'),
        ("<label for=\"street-address\">Indirizzo di consegna*</label>", f'<label for="street-address">{c["label_addr"]}</label>'),
        ('placeholder="Via Roma 15, Milano"', f'placeholder="{c["ph_addr"]}"'),
        ('<input name="offer" type="hidden" value=""/>', f'<input name="offer" type="hidden" value="{offer["offer_id"]}"/>'),
        ('value="https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh"', 'value=""'),
        ("CONFERMA L'ORDINE", c["btn_submit"]),
        ("🔒 Pagamento alla consegna · Reso entro 30 giorni", c["form_note"]),
        ("01 — VALMORA™: Cottura uniforme dal centro ai bordi", c["w1_eye"]),
        ("Il calore si diffonde su tutta la base, senza zone che si surriscaldano", c["w1_h"]),
        ("<span class=\"tag\">Struttura a 3 strati</span><span class=\"tag\">Anima in alluminio</span><span class=\"tag\">Calore ben distribuito</span>", f'<span class="tag">{c["w1_t1"]}</span><span class="tag">{c["w1_t2"]}</span><span class="tag">{c["w1_t3"]}</span>'),
        (
            "Con VALMORA™ non devi mescolare di continuo per evitare che il cibo si bruci in alcuni punti. Il nucleo in alluminio aiuta a diffondere il calore in modo omogeneo, mentre l'acciaio inox offre una superficie resistente per cucinare ogni giorno.",
            c["w1_p"],
        ),
        ("Cottura più regolare e meno tempo passato a controllare i fornelli.", c["w1_i"]),
        ('alt="Set di pentole VALMORA con fondo trilaminato"', f'alt="{c["alt_w1"]}"'),
        ("02 — VALMORA™: Lo stesso set per ogni tipo di cucina", c["w2_eye"]),
        ("Un solo set per gas, elettrico, vetroceramica e induzione", c["w2_h"]),
        ("<span class=\"tag\">Adatto all'induzione</span><span class=\"tag\">Forno fino a 230°C</span><span class=\"tag\">Manici confortevoli</span>", f'<span class="tag">{c["w2_t1"]}</span><span class="tag">{c["w2_t2"]}</span><span class="tag">{c["w2_t3"]}</span>'),
        (
            "La base multistrato è compatibile con i principali piani cottura, inclusa l'induzione. Se la ricetta lo richiede, puoi spostare la pentola dal fornello al forno fino a 230°C senza cambiare recipiente.",
            c["w2_p"],
        ),
        ("Cucina con più libertà, riducendo passaggi e stoviglie da lavare.", c["w2_i"]),
        ('alt="Set VALMORA compatibile con piano a induzione"', f'alt="{c["alt_w2"]}"'),
        ("03 — VALMORA™: Pulizia veloce e brillantezza duratura", c["w3_eye"]),
        ("Una superficie liscia che non trattiene aromi né odori", c["w3_h"]),
        ("<span class=\"tag\">Acciaio lucidato</span><span class=\"tag\">Neutro sui sapori</span><span class=\"tag\">Adatto alla lavastoviglie</span>", f'<span class="tag">{c["w3_t1"]}</span><span class="tag">{c["w3_t2"]}</span><span class="tag">{c["w3_t3"]}</span>'),
        (
            "L'acciaio inox si pulisce facilmente e non conserva gli odori delle ricette precedenti. Tutti i componenti possono andare in lavastoviglie, rendendo VALMORA™ pratico anche con un uso intenso e quotidiano.",
            c["w3_p"],
        ),
        ("Meno tempo per riordinare e pentole che mantengono più a lungo la loro brillantezza.", c["w3_i"]),
        ('alt="Set VALMORA lavabile in lavastoviglie"', f'alt="{c["alt_w3"]}"'),
        ("Confronto diretto", c["cmp_label"]),
        ("Pentole comuni o VALMORA™? Guarda cosa cambia", c["cmp_h2"]),
        ('aria-label="Confronto tra pentole comuni e VALMORA"', f'aria-label="{c["cmp_aria"]}"'),
        ("<th>Comuni</th>", f"<th>{c['th_common']}</th>"),
        ("<td>Distribuzione del calore</td><td>Possibili punti troppo caldi</td><td class=\"win\">Base a 3 strati, calore uniforme</td>", f'<td>{c["cmp_r1_l"]}</td><td>{c["cmp_r1_a"]}</td><td class="win">{c["cmp_r1_b"]}</td>'),
        ("<td>Piani cottura</td><td>Compatibilità variabile</td><td class=\"win\">Gas, elettrico, vetroceramica e induzione</td>", f'<td>{c["cmp_r2_l"]}</td><td>{c["cmp_r2_a"]}</td><td class="win">{c["cmp_r2_b"]}</td>'),
        ("<td>Uso in forno</td><td>Spesso non indicato</td><td class=\"win\">Adatto fino a 230°C</td>", f'<td>{c["cmp_r3_l"]}</td><td>{c["cmp_r3_a"]}</td><td class="win">{c["cmp_r3_b"]}</td>'),
        ("<td>Manici</td><td>Presa spesso scomoda</td><td class=\"win\">Solidi e facili da impugnare</td>", f'<td>{c["cmp_r4_l"]}</td><td>{c["cmp_r4_a"]}</td><td class="win">{c["cmp_r4_b"]}</td>'),
        ("<td>Pulizia</td><td>Può opacizzarsi nel tempo</td><td class=\"win\">Acciaio lucidato, lavabile in lavastoviglie</td>", f'<td>{c["cmp_r5_l"]}</td><td>{c["cmp_r5_a"]}</td><td class="win">{c["cmp_r5_b"]}</td>'),
        ("<td>Contenuto</td><td>Spesso pochi elementi</td><td class=\"win\">Set completo da 12 pezzi</td>", f'<td>{c["cmp_r6_l"]}</td><td>{c["cmp_r6_a"]}</td><td class="win">{c["cmp_r6_b"]}</td>'),
        ("<td>Acquisto</td><td>Tutele non sempre chiare</td><td class=\"win\">30 giorni per richiedere il reso</td>", f'<td>{c["cmp_r7_l"]}</td><td>{c["cmp_r7_a"]}</td><td class="win">{c["cmp_r7_b"]}</td>'),
        ("Migliaia di clienti hanno già scelto VALMORA™ per la cucina di tutti i giorni", c["test_h2"]),
        ("Il riso cuoce bene e non resta incollato al fondo.", c["t1_h"]),
        ("«Preparo da mangiare ogni giorno per la famiglia e questo set si nota subito. Il calore si distribuisce meglio, i piatti cuociono in modo più uniforme e i coperchi chiudono bene.»", c["t1_p"]),
        ("Chiara B. — Torino, acquisto verificato", c["t1_auth"]),
        ("Mia moglie ha preso VALMORA™ per la nostra famiglia numerosa: ormai lo usiamo quasi sempre.", c["t2_h"]),
        ("«Lo utilizziamo ogni giorno per carne, sughi e primi piatti. Non si attacca tutto come prima, il calore è ben distribuito e la pulizia è molto semplice.»", c["t2_p"]),
        ("Davide M. — Bologna, acquisto verificato", c["t2_auth"]),
        ("Restano brillanti anche dopo tanti lavaggi.", c["t3_h"]),
        ("«Le uso spesso e finiscono regolarmente in lavastoviglie. L'acciaio torna pulito con poco sforzo e non trattiene odori o macchie difficili.»", c["t3_p"]),
        ("Elena R. — Bari, acquisto verificato", c["t3_auth"]),
        ('alt="Set completo VALMORA™ da 12 pezzi appena ricevuto"', f'alt="{c["alt_t1"]}"'),
        ('alt="Set VALMORA su un piano a induzione"', f'alt="{c["alt_t2"]}"'),
        ('alt="Superficie lucida del set VALMORA dopo il lavaggio"', f'alt="{c["alt_t3"]}"'),
        ('<span class="eyebrow">Cosa ricevi</span><h2>Il set completo VALMORA™ da 12 pezzi, pronto per la tua cucina</h2>', f'<span class="eyebrow">{c["kit_eye"]}</span><h2>{c["kit_h2"]}</h2>'),
        ('alt="Kit completo VALMORA™"', f'alt="{c["alt_kit"]}"'),
        ("Pentola alta 7L con coperchio — per zuppe e porzioni abbondanti", c["kit_i1"]),
        ("Pentola media 3L con coperchio — per sughi e uso quotidiano", c["kit_i2"]),
        ("Casseruola 1,5L con coperchio — per ricette e porzioni più piccole", c["kit_i3"]),
        ("Pentola per brasare 3,5L con manico ausiliario", c["kit_i4"]),
        ("Padella 20cm e padella 28cm", c["kit_i5"]),
        ("Cestello per cottura al vapore con coperchio", c["kit_i6"]),
        ("Manici saldati, comodi durante la cottura", c["kit_i7"]),
        ("Manuale d'uso e scheda di garanzia", c["kit_i8"]),
        ("Garanzia ufficiale di 2 anni", c["kit_i9"]),
        ("<h2>Domande frequenti</h2>", f"<h2>{c['faq_h2']}</h2>"),
        ("<span>Quanto tempo richiede la consegna?</span>", f"<span>{c['faq1_q']}</span>"),
        ("<p>La consegna avviene normalmente entro 2-4 giorni lavorativi. Dopo la richiesta ti contatteremo per verificare i dati e confermare la spedizione.</p>", f"<p>{c['faq1_a']}</p>"),
        ("<span>Come avviene il pagamento?</span>", f"<span>{c['faq2_q']}</span>"),
        ("<p>Puoi pagare 74€ direttamente alla consegna, quando ricevi il pacco dal corriere.</p>", f"<p>{faq2_a}</p>"),
        ("<span>Il set è compatibile con l'induzione?</span>", f"<span>{c['faq3_q']}</span>"),
        (
            "<p>Sì. La base multistrato con anima in alluminio è adatta ai piani a gas, elettrici, in vetroceramica e a induzione.</p>",
            f"<p>{c['faq3_a']}</p>",
        ),
        ("<span>Le pentole possono andare in forno?</span>", f"<span>{c['faq4_q']}</span>"),
        (
            "<p>Sì, il set può essere utilizzato in forno fino a 230°C: ideale per iniziare una ricetta sul piano cottura e completarla in forno.</p>",
            f"<p>{c['faq4_a']}</p>",
        ),
        ("<span>Cosa succede se il set non fa per me?</span>", f"<span>{c['faq5_q']}</span>"),
        (
            "<p>Hai 30 giorni dalla consegna per richiedere il reso e ottenere il rimborso secondo le condizioni della nostra politica di rimborso.</p>",
            f"<p>{c['faq5_a']}</p>",
        ),
        ("Prodotti utili per la vita quotidiana, consegna rapida e pagamento alla consegna.", c["footer_blurb"]),
        ("Informazioni", c["info"]),
        ("Chi siamo", c["about"]),
        ("Contattaci", c["contact"]),
        ("Privacy Policy", c["privacy"]),
        ("Termini e Condizioni", c["terms"]),
        ("Cookie Policy", c["cookie_pol"]),
        ("Politica di Spedizione", c["ship"]),
        ("Politica di Rimborso", c["refund"]),
        ('<h4 class="site-footer__heading">Contatti</h4>', f'<h4 class="site-footer__heading">{c["contacts"]}</h4>'),
        ("Stati Uniti", c["country_us"]),
        ("Tutti i diritti riservati.", f'{c["rights"]}.'),
        ('href="/it/', f'href="/{geo}/'),
    ]


def ty_pairs(c: dict, offer: dict) -> list[tuple[str, str]]:
    geo = offer["geo"]
    slug = slug_for(offer)
    ty = ty_url(offer)
    now = fmt_price(offer["price"], offer["currency"])

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ("https://gadgetshifthub.com/it/valmora/thank-you.html", ty),
        ("Ordine ricevuto — Attendi la chiamata di conferma | VALMORA™", c["ty_title"]),
        (
            "Il tuo ordine VALMORA™ è stato ricevuto. Resta solo un passaggio: rispondere alla chiamata del nostro operatore per confermare i dati.",
            c["ty_desc"],
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'valmora',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 74.0,", f"  PRICE: {offer['price']},"),
        ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", c["cookie_text"]),
        ("COOKIE_ACCEPT: 'Accetta',", f"COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("COOKIE_LEARN: 'Scopri di più'", f"COOKIE_LEARN: '{c['cookie_learn']}'"),
        ("trackPurchase(74.0, 'EUR')", f"trackPurchase({offer['price']}, '{offer['currency']}')"),
        ("Il tuo ordine è stato registrato correttamente!", c["ty_h1"]),
        (
            "Perfetto — il tuo ordine è in lavorazione. Per completarlo e avviare la spedizione manca solo <strong>la conferma telefonica</strong>.",
            c["ty_sub"],
        ),
        ("Il team gadgetshifthub al lavoro: call center e logistica COD", c["ty_alt"]),
        ("👇 Cosa fare adesso", c["ty_eyebrow"]),
        ("📞 Rispondi alla chiamata di conferma", c["ty_action_title"]),
        (
            "Un nostro operatore ti chiamerà <strong>nelle prossime ore</strong> per confermare il tuo ordine e i dettagli di consegna.",
            c["ty_action_body"],
        ),
        ("Se non rispondi, l'ordine non potrà essere confermato e verrà annullato.", c["ty_action_warn"]),
        ("🕒 Orari di contatto", c["ty_hours_h"]),
        ("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", c["ty_hours"]),
        ("📋 Cosa succede dopo", c["ty_next_h"]),
        ("Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>", c["ty_step1"]),
        ("Il tuo ordine verrà preparato entro <strong>24–48 ore</strong>", c["ty_step2"]),
        ("Ricevi il pacco a domicilio e <strong>paghi alla consegna</strong>", c["ty_step3"]),
        ("🔒 Pagamento alla consegna", c["ty_badge1"]),
        ("🛡️ Garanzia 24 mesi", c["ty_badge2"]),
        ("🔐 Protezione SSL", c["ty_badge3"]),
        ("Informazioni", c["info"]),
        ("Chi siamo", c["about"]),
        ("Contattaci", c["contact"]),
        ("Privacy Policy", c["privacy"]),
        ("Termini e Condizioni", c["terms"]),
        ("Cookie Policy", c["cookie_pol"]),
        ("Politica di Spedizione", c["ship"]),
        ("Politica di Rimborso", c["refund"]),
        ('<h4 class="site-footer__heading">Contatti</h4>', f'<h4 class="site-footer__heading">{c["contacts"]}</h4>'),
        ("Stati Uniti", c["country_us"]),
        ("Tutti i diritti riservati.", f'{c["rights"]}.'),
        ('href="/it/', f'href="/{geo}/'),
    ]


def inject_markers(html: str, offer_id: str) -> str:
    marker = f'<!-- Offer #{offer_id} -->'
    if marker not in html:
        html = html.replace("<body", f"{marker}\n<body", 1)
    meta = f'<meta name="offer-id" content="{offer_id}">'
    if 'name="offer-id"' not in html:
        html = html.replace("<meta charset=", f"{meta}\n<meta charset=", 1)
    return html


def main() -> list[str]:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    it_index = IT_INDEX.read_text(encoding="utf-8")
    it_ty = IT_TY.read_text(encoding="utf-8")
    urls: list[str] = []

    for offer in OFFERS:
        lang = offer["lang"]
        if lang not in COPY:
            raise KeyError(f"Missing COPY for {lang}")
        c = COPY[lang]
        slug = slug_for(offer)
        out_dir = ROOT / offer["geo"] / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        index_html = apply_pairs(it_index, index_pairs(c, offer))
        index_html = insert_ai_notice_in_site_footer(index_html, offer["lang"])
        ty_html = apply_pairs(it_ty, ty_pairs(c, offer))
        index_html = inject_markers(index_html, offer["offer_id"])
        ty_html = inject_markers(ty_html, offer["offer_id"])

        (out_dir / "index.html").write_text(index_html, encoding="utf-8")
        (out_dir / "thank-you.html").write_text(ty_html, encoding="utf-8")

        url = base_url(offer)
        urls.append(url)
        print(
            f"OK {offer['geo']}/{slug}/  offer=#{offer['offer_id']}  "
            f"price={fmt_price(offer['price'], offer['currency'])}  "
            f"was={fmt_price(was_price(offer['price']), offer['currency'])}",
            flush=True,
        )

    print(f"\nCreated {len(OFFERS) * 2} files for {len(OFFERS)} geos")
    return urls


if __name__ == "__main__":
    main()
