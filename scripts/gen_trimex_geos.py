#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate TRIMEX grass trimmer landing + thank-you pages for campaign geos."""
from __future__ import annotations

import html
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer
IT_INDEX = ROOT / "it/trimex/index.html"
IT_TY = ROOT / "it/trimex/thank-you.html"

OFFERS = [
    {"geo": "de", "lang": "de", "offer_id": "23", "currency": "EUR", "price": 79, "phone": "+49 170 1234567"},
    {"geo": "pl", "lang": "pl", "offer_id": "24", "currency": "PLN", "price": 299, "phone": "+48 512 345 678"},
    {"geo": "es", "lang": "es", "offer_id": "1815", "currency": "EUR", "price": 74, "phone": "+34 612 345 678"},
    {"geo": "pt", "lang": "pt", "offer_id": "1816", "currency": "EUR", "price": 79, "phone": "+351 912 345 678"},
    {"geo": "ro", "lang": "ro", "offer_id": "2637", "currency": "RON", "price": 399, "phone": "+40 721 234 567"},
    {"geo": "si", "lang": "sl", "offer_id": "2642", "currency": "EUR", "price": 79.90, "phone": "+386 31 234 567"},
    {"geo": "hr", "lang": "hr", "offer_id": "2643", "currency": "EUR", "price": 79.90, "phone": "+385 91 234 5678"},
    {"geo": "cz", "lang": "cs", "offer_id": "2645", "currency": "CZK", "price": 1899, "phone": "+420 601 123 456"},
    {"geo": "hu", "lang": "hu", "offer_id": "2918", "currency": "HUF", "price": 31999, "phone": "+36 30 123 4567"},
    {"geo": "sk", "lang": "sk", "offer_id": "4042", "currency": "EUR", "price": 79, "phone": "+421 901 123 456"},
    {"geo": "lv", "lang": "lv", "offer_id": "4043", "currency": "EUR", "price": 99, "phone": "+371 2123 4567"},
]

FORM_UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"


def load_copy() -> dict:
    path = Path(__file__).with_name("_trimex_copy_data.py")
    spec = importlib.util.spec_from_file_location("_trimex_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


COPY = load_copy()


def slug_for(offer: dict) -> str:
    return f"trimex-{offer['offer_id']}"


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
    slug = slug_for(offer)
    geo = offer["geo"]
    base = base_url(offer)
    ty = ty_url(offer)
    h1 = c["h1_m"]

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        (
            "TRIMEX™ — Decespugliatore a batteria senza benzina | -50% oggi",
            c["title"],
        ),
        (
            "Decespugliatore a batteria TRIMEX™ con motore da 2880 W, 2 batterie da 60 W incluse e solo 2 kg. Niente benzina, fumo o cavi. Pagamento alla consegna.",
            c["description"],
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'trimex',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 74.0,", f"  PRICE: {offer['price']},"),
        ("  OFFER_NAME: 'TRIMEX IT',", f"  OFFER_NAME: 'TRIMEX {geo.upper()} #{offer['offer_id']}',"),
        ("  LP_ID: 'it-trimex-v1',", f"  LP_ID: '{geo}-{offer['offer_id']}',"),
        ("  FORM_OFFER: '',", f"  FORM_OFFER: '{offer['offer_id']}',"),
        ("  FORM_LP: '',", "  FORM_LP: '',"),
        ("  FORM_WEBHOOK: '',", "  FORM_WEBHOOK: '',"),
        ("  FORM_KEY: '',", "  FORM_KEY: '',"),
        (
            "  THANKYOU_URL: 'https://gadgetshifthub.com/it/trimex/thank-you.html',",
            f"  THANKYOU_URL: '{ty}',",
        ),
        (
            "  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',",
            f"  COOKIE_TEXT: '{c['cookie_text']}',",
        ),
        ("  COOKIE_ACCEPT: 'Accetta',", f"  COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("  COOKIE_LEARN: 'Scopri di più'", f"  COOKIE_LEARN: '{c['cookie_learn']}'"),
        (
            'value="https://gadgetshifthub.com/it/trimex/thank-you.html"',
            f'value="{ty}"',
        ),
        (
            'value="https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh"',
            'value=""',
        ),
        ("https://gadgetshifthub.com/it/trimex/", base),
        ("🔥 SOLO OGGI: -50% SU TRIMEX™ + 2 BATTERIE DA 60 W INCLUSE 🔥", c["topbar"]),
        ("<strong>4,8/5</strong> — Più di <strong>6.200</strong> clienti soddisfatti", c["rating"]),
        ("🛡️ Reso entro 30 giorni + consegna rapida", c["gift"]),
        (
            'Pesa come una bottiglia d\'acqua da 2 litri, ma taglia rovi, erbacce e cespugli senza una goccia di benzina.',
            h1,
        ),
        (
            "<strong>TRIMEX™</strong> — motore brushless da 2880 W e 2 batterie da 60 W incluse. Taglia dove il tosaerba non arriva: lungo la recinzione, intorno ad alberi e aiuole. Garanzia 2 anni.",
            c["lead"],
        ),
        (
            'alt="Decespugliatore TRIMEX™ con batterie, lame e accessori inclusi"',
            f'alt="{c["alt_hero"]}"',
        ),
        ('<span class="was">148€</span><span class="now">74€</span><span class="pct">-50%</span>', price_block),
        ("SÌ, VOGLIO TRIMEX™ →", c["cta"]),
        ("🔒 Consegna rapida · Pagamento alla consegna · Reso entro 30 giorni", c["form_note_hero"]),
        (
            "<h4>Consegna rapida</h4><p>Spedizione in tutta Italia</p>",
            f'<h4>{c["f1_h"]}</h4><p>{c["f1_p"]}</p>',
        ),
        (
            "<h4>Ordine sicuro</h4><p>Dati protetti durante l'acquisto</p>",
            f'<h4>{c["f2_h"]}</h4><p>{c["f2_p"]}</p>',
        ),
        (
            "<h4>Qualità verificata</h4><p>Motore potente e materiali robusti</p>",
            f'<h4>{c["f3_h"]}</h4><p>{c["f3_p"]}</p>',
        ),
        (
            "<h4>30 giorni per il reso</h4><p>Procedura semplice e veloce</p>",
            f'<h4>{c["f4_h"]}</h4><p>{c["f4_p"]}</p>',
        ),
        ("⏰ L'offerta -50% scade tra", c["countdown"]),
        ('<div class="lbl">Ore</div>', f'<div class="lbl">{c["hours"]}</div>'),
        ('<div class="lbl">Min</div>', f'<div class="lbl">{c["mins"]}</div>'),
        ('<div class="lbl">Sec</div>', f'<div class="lbl">{c["secs"]}</div>'),
        (
            '<span class="left">Disponibilità</span><span class="right">Restano pochi pezzi in magazzino</span>',
            f'<span class="left">{c["stock_l"]}</span><span class="right">{c["stock_r"]}</span>',
        ),
        (
            'data-live="&lt;strong&gt;{n} persone&lt;/strong&gt; stanno guardando TRIMEX™ adesso" id="liveCount"><strong>53 persone</strong> stanno guardando TRIMEX™ adesso',
            f'data-live="{html.escape(c["live_tpl"])}" id="liveCount">{c["live_tpl"].replace("{n}", "53")}',
        ),
        ("<h2>Completa il tuo ordine</h2>", f"<h2>{c['form_h2']}</h2>"),
        (
            "<p>Inserisci i tuoi dati: il nostro team ti chiamerà per verificare l'ordine e concordare la consegna.</p>",
            f"<p>{c['form_p']}</p>",
        ),
        ('<label for="name">Nome e cognome*</label>', f'<label for="name">{c["label_name"]}</label>'),
        ('placeholder="Mario Rossi"', f'placeholder="{c["ph_name"]}"'),
        ('<label for="tel">Numero di telefono*</label>', f'<label for="tel">{c["label_tel"]}</label>'),
        ('placeholder="+39 333 123 4567"', f'placeholder="{offer["phone"]}"'),
        (
            '<label for="street-address">Indirizzo di consegna*</label>',
            f'<label for="street-address">{c["label_addr"]}</label>',
        ),
        ('placeholder="Via Roma 15, Milano"', f'placeholder="{c["ph_addr"]}"'),
        ('<input name="offer" type="hidden" value=""/>', f'<input name="offer" type="hidden" value="{offer["offer_id"]}"/>'),
        ("CONFERMA L'ORDINE", c["btn_submit"]),
        ("🔒 Pagamento alla consegna · Reso entro 30 giorni", c["form_note"]),
        ("01 — TRIMEX™: La potenza per l'erba più ostinata, senza benzina", c["w1_eye"]),
        ("Erba alta, rovi, erbacce e piccoli rami: tagli tutto senza fatica", c["w1_h"]),
        (
            '<span class="tag">Motore da 2880 W</span><span class="tag">Lame in acciaio incluse</span><span class="tag">Zero benzina e fumo</span>',
            f'<span class="tag">{c["w1_t1"]}</span><span class="tag">{c["w1_t2"]}</span><span class="tag">{c["w1_t3"]}</span>',
        ),
        (
            "Bordi del prato, lungo la recinzione, intorno agli alberi, tra aiuole e vialetti: TRIMEX™ arriva dove il tosaerba non passa. Il motore da 2880 W e le lame in acciaio tagliano anche la vegetazione più fitta, senza miscela da preparare, senza tirare la cordicella e senza odore di benzina sui vestiti.",
            c["w1_p"],
        ),
        ("Il giardino in ordine in meno tempo, senza strappi e senza fumo.", c["w1_i"]),
        (
            'alt="TRIMEX™ taglia erba alta e rovi lungo la recinzione"',
            f'alt="{c["alt_w1"]}"',
        ),
        ("02 — TRIMEX™: Lavori più a lungo, senza fermarti a metà", c["w2_eye"]),
        ("Due batterie e soli 2 kg: finisci il lavoro senza mal di schiena", c["w2_h"]),
        (
            '<span class="tag">2 batterie da 60 W incluse</span><span class="tag">Solo 2 kg</span><span class="tag">Manico regolabile</span>',
            f'<span class="tag">{c["w2_t1"]}</span><span class="tag">{c["w2_t2"]}</span><span class="tag">{c["w2_t3"]}</span>',
        ),
        (
            "Quando una batteria si scarica, la sostituisci in pochi secondi e riprendi subito da dove eri rimasto. TRIMEX™ è leggero e bilanciato, il manico telescopico si regola fino a 2 metri per adattarsi alla tua altezza e l'impugnatura antiscivolo riduce le vibrazioni: braccia, spalle e schiena non ne risentono, nemmeno dopo ore di lavoro.",
            c["w2_p"],
        ),
        (
            "Più lavoro fatto, meno fatica. Perfetto anche per chi non ha più la forza di una volta.",
            c["w2_i"],
        ),
        (
            'alt="Sostituzione rapida della batteria del decespugliatore TRIMEX™"',
            f'alt="{c["alt_w2"]}"',
        ),
        ("03 — TRIMEX™: Silenzioso e pronto all'uso appena arriva", c["w3_eye"]),
        ("Niente rumore assordante, niente accessori da comprare a parte", c["w3_h"]),
        (
            '<span class="tag">Funzionamento silenzioso</span><span class="tag">Kit completo</span><span class="tag">Si monta in pochi minuti</span>',
            f'<span class="tag">{c["w3_t1"]}</span><span class="tag">{c["w3_t2"]}</span><span class="tag">{c["w3_t3"]}</span>',
        ),
        (
            "Puoi sistemare il giardino anche la domenica mattina senza disturbare i vicini. Nella confezione trovi già tutto: batterie, caricabatterie, lame in acciaio, lame in plastica, disco da taglio e attrezzi per il montaggio. Apri la scatola, monti in pochi minuti e sei già in giardino.",
            c["w3_p"],
        ),
        ("Nessuna sorpresa, nessuna spesa extra: solo il giardino in ordine.", c["w3_i"]),
        (
            'alt="Kit completo TRIMEX™ pronto all\'uso appena aperto"',
            f'alt="{c["alt_w3"]}"',
        ),
        ("Confronto diretto", c["cmp_label"]),
        ("Decespugliatore a benzina o TRIMEX™? Guarda cosa cambia", c["cmp_h2"]),
        (
            'aria-label="Confronto tra decespugliatore a benzina e TRIMEX"',
            f'aria-label="{c["cmp_aria"]}"',
        ),
        ("<th>A benzina</th>", f"<th>{c['th_gas']}</th>"),
        (
            "<td>Alimentazione</td><td>Benzina e miscela da comprare</td><td class=\"win\">Batteria, zero carburante</td>",
            f'<td>{c["cmp_r1_l"]}</td><td>{c["cmp_r1_a"]}</td><td class="win">{c["cmp_r1_b"]}</td>',
        ),
        (
            "<td>Peso</td><td>Pesante, affatica spalle e schiena</td><td class=\"win\">Solo 2 kg, leggero e bilanciato</td>",
            f'<td>{c["cmp_r2_l"]}</td><td>{c["cmp_r2_a"]}</td><td class="win">{c["cmp_r2_b"]}</td>',
        ),
        (
            "<td>Rumore</td><td>Assordante, disturba i vicini</td><td class=\"win\">Silenzioso</td>",
            f'<td>{c["cmp_r3_l"]}</td><td>{c["cmp_r3_a"]}</td><td class="win">{c["cmp_r3_b"]}</td>',
        ),
        (
            "<td>Fumo e odore</td><td>Gas di scarico e puzza di benzina</td><td class=\"win\">Nessuna emissione</td>",
            f'<td>{c["cmp_r4_l"]}</td><td>{c["cmp_r4_a"]}</td><td class="win">{c["cmp_r4_b"]}</td>',
        ),
        (
            "<td>Avviamento</td><td>Cordicella da tirare più volte</td><td class=\"win\">Si accende con un pulsante</td>",
            f'<td>{c["cmp_r5_l"]}</td><td>{c["cmp_r5_a"]}</td><td class="win">{c["cmp_r5_b"]}</td>',
        ),
        (
            "<td>Autonomia</td><td>Ti fermi per fare rifornimento</td><td class=\"win\">2 batterie da 60 W, cambio in pochi secondi</td>",
            f'<td>{c["cmp_r6_l"]}</td><td>{c["cmp_r6_a"]}</td><td class="win">{c["cmp_r6_b"]}</td>',
        ),
        (
            "<td>Acquisto</td><td>Accessori spesso venduti a parte</td><td class=\"win\">Kit completo + garanzia 2 anni</td>",
            f'<td>{c["cmp_r7_l"]}</td><td>{c["cmp_r7_a"]}</td><td class="win">{c["cmp_r7_b"]}</td>',
        ),
        (
            "Migliaia di clienti hanno già scelto TRIMEX™ per il loro giardino",
            c["test_h2"],
        ),
        ("Sembrava un giocattolo, poi mi sono dovuto ricredere.", c["t1_h"]),
        (
            "«Aprendo la scatola ero perplesso: così leggero, rispetto al mio vecchio a benzina, sembrava un giocattolo. Poi l'ho provato su rovi e rami di oltre un centimetro e li ha tagliati senza problemi.»",
            c["t1_p"],
        ),
        ("Marco T. — Verona, acquisto verificato", c["t1_auth"]),
        ("La batteria di scorta fa tutta la differenza.", c["t2_h"]),
        (
            "«Ho un terreno grande e l'erba alta lungo la recinzione era un incubo. Quando la prima batteria finisce, metto la seconda in pochi secondi e continuo. Finalmente finisco tutto in una volta sola.»",
            c["t2_p"],
        ),
        ("Giuseppe L. — Perugia, acquisto verificato", c["t2_auth"]),
        ("L'ho regalato ai miei genitori.", c["t3_h"]),
        (
            "«Mio padre ha 72 anni e non volevo più vederlo con il decespugliatore a benzina in spalla. Questo è leggero, si accende subito e il manico si regola bene. Ora lo usa da solo senza problemi.»",
            c["t3_p"],
        ),
        ("Francesca D. — Lecce, acquisto verificato", c["t3_auth"]),
        (
            'alt="Decespugliatore TRIMEX™ dopo il taglio di rovi in giardino"',
            f'alt="{c["alt_t1"]}"',
        ),
        (
            'alt="Erba alta tagliata lungo la recinzione con TRIMEX™"',
            f'alt="{c["alt_t2"]}"',
        ),
        (
            'alt="Uomo anziano usa il decespugliatore TRIMEX™ in giardino"',
            f'alt="{c["alt_t3"]}"',
        ),
        (
            '<span class="eyebrow">Cosa ricevi</span><h2>Il kit completo TRIMEX™, pronto per il tuo giardino</h2>',
            f'<span class="eyebrow">{c["kit_eye"]}</span><h2>{c["kit_h2"]}</h2>',
        ),
        ('alt="Kit completo TRIMEX™"', f'alt="{c["alt_kit"]}"'),
        ("Decespugliatore TRIMEX™ con motore da 2880 W", c["kit_i1"]),
        ("2 batterie da 60 W — per lavorare senza interruzioni", c["kit_i2"]),
        ("Caricabatterie rapido", c["kit_i3"]),
        ("Lame in acciaio — per rovi, cespugli e piccoli rami", c["kit_i4"]),
        ("Lame in plastica — per erba e bordi del prato", c["kit_i5"]),
        ("Disco da taglio — per la vegetazione più fitta", c["kit_i6"]),
        ("Manico telescopico regolabile con impugnatura antiscivolo", c["kit_i7"]),
        ("Attrezzi per il montaggio e manuale d'uso", c["kit_i8"]),
        ("Garanzia ufficiale di 2 anni", c["kit_i9"]),
        ("<h2>Domande frequenti</h2>", f"<h2>{c['faq_h2']}</h2>"),
        ("<span>Quanto tempo richiede la consegna?</span>", f"<span>{c['faq1_q']}</span>"),
        (
            "<p>Dopo la conferma telefonica del tuo ordine, il pacco arriva a casa tua in 24-48 ore lavorative.</p>",
            f"<p>{c['faq1_a']}</p>",
        ),
        ("<span>Come avviene il pagamento?</span>", f"<span>{c['faq2_q']}</span>"),
        (
            "<p>Paghi direttamente al corriere al momento della consegna. Nessun pagamento anticipato e nessun dato della carta richiesto.</p>",
            f"<p>{c['faq2_a']}</p>",
        ),
        ("<span>Quanto dura la batteria?</span>", f"<span>{c['faq3_q']}</span>"),
        (
            "<p>Nel kit trovi 2 batterie da 60 W, con un'autonomia totale fino a 16 ore. Quando una si scarica, la sostituisci in pochi secondi e continui a lavorare.</p>",
            f"<p>{c['faq3_a']}</p>",
        ),
        (
            "<span>Taglia anche rovi ed erbacce resistenti?</span>",
            f"<span>{c['faq4_q']}</span>",
        ),
        (
            "<p>Sì. Grazie al motore da 2880 W e alle lame in acciaio e al disco inclusi, taglia erba alta, rovi, erbacce e piccoli arbusti.</p>",
            f"<p>{c['faq4_a']}</p>",
        ),
        (
            "<span>È pesante? Può usarlo anche una persona anziana?</span>",
            f"<span>{c['faq5_q']}</span>",
        ),
        (
            "<p>Pesa solo 2 kg ed è ben bilanciato. Il manico regolabile e l'impugnatura antiscivolo lo rendono facile da usare anche per chi ha meno forza.</p>",
            f"<p>{c['faq5_a']}</p>",
        ),
        ("<span>Cosa succede se non fa per me?</span>", f"<span>{c['faq6_q']}</span>"),
        (
            "<p>Hai 30 giorni per richiedere il reso. Contatta il nostro servizio clienti e ti guideremo passo dopo passo.</p>",
            f"<p>{c['faq6_a']}</p>",
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

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ("https://gadgetshifthub.com/it/trimex/thank-you.html", ty),
        ("Ordine ricevuto — Attendi la chiamata di conferma | TRIMEX™", c["ty_title"]),
        (
            "Il tuo ordine TRIMEX™ è stato ricevuto. Resta solo un passaggio: rispondere alla chiamata del nostro operatore per confermare i dati.",
            c["ty_desc"],
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'trimex',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 74.0,", f"  PRICE: {offer['price']},"),
        (
            "  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',",
            f"  COOKIE_TEXT: '{c['cookie_text']}',",
        ),
        ("  COOKIE_ACCEPT: 'Accetta',", f"  COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("  COOKIE_LEARN: 'Scopri di più'", f"  COOKIE_LEARN: '{c['cookie_learn']}'"),
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
        (
            "Se non rispondi, l'ordine non potrà essere confermato e verrà annullato.",
            c["ty_action_warn"],
        ),
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
    marker = f"<!-- Offer #{offer_id} -->"
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
