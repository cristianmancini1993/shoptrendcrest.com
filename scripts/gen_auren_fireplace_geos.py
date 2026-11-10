#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate AUREN electric fireplace landings + TYP for campaign geos (from it/italy)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer
IT_INDEX = ROOT / "it/italy/index.html"
IT_TY = ROOT / "it/italy/thank-you.html"

OFFERS = [
    {"geo": "pl", "lang": "pl", "offer_id": "1987", "currency": "PLN", "price": 399, "cpa": 19},
    {"geo": "cz", "lang": "cs", "offer_id": "2400", "currency": "CZK", "price": 2290, "cpa": 18},
    {"geo": "es", "lang": "es", "offer_id": "2635", "currency": "EUR", "price": 96, "cpa": 18},
    {"geo": "pt", "lang": "pt", "offer_id": "2636", "currency": "EUR", "price": 112, "cpa": 18},
    {"geo": "de", "lang": "de", "offer_id": "2665", "currency": "EUR", "price": 89, "cpa": 18},
    {"geo": "hu", "lang": "hu", "offer_id": "2668", "currency": "HUF", "price": 29999, "cpa": 16},
    {"geo": "sk", "lang": "sk", "offer_id": "4357", "currency": "EUR", "price": 97, "cpa": 20},
    {"geo": "lv", "lang": "lv", "offer_id": "4358", "currency": "EUR", "price": 99, "cpa": 15},
]

try:
    from _auren_network_forms import FORM_META as _FORM_META
except ImportError:
    _FORM_META = {}

LP_BY_OFFER = {meta["offer"]: meta["lp"] for meta in _FORM_META.values()}


def load_copy() -> dict:
    path = Path(__file__).with_name("_auren_fireplace_copy_data.py")
    spec = importlib.util.spec_from_file_location("_auren_fireplace_copy_data", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.COPY


def slug_for(offer: dict) -> str:
    return f"auren-{offer['offer_id']}"


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


def sub(c: dict, key: str, **kwargs: str) -> str:
    text = c[key]
    for k, v in kwargs.items():
        text = text.replace("{" + k + "}", v)
    return text


def apply_pairs(html: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        if old not in html:
            raise KeyError(f"Missing template fragment: {old[:120]}...")
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
    slug = slug_for(offer)
    geo = offer["geo"]
    base = base_url(offer)
    ty = ty_url(offer)
    oid = offer["offer_id"]
    lp = lp_for(oid)

    live = sub(c, "live_tpl", n="15")

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ('content="2635"', f'content="{oid}"'),
        (
            "AUREN™ | Camino elettrico LED 3D, fino a 80 m² | -50% | Italia",
            sub(c, "title", price=now),
        ),
        (
            "AUREN™: caminetto elettrico con effetto fiamma LED 3D, calore rapido fino a 80 m². App, telecomando e comandi sul pannello. Nessuna installazione. Spedizione 24–48 h dopo conferma telefonica e contrassegno a 96 €.",
            sub(c, "meta_desc", price=now),
        ),
        (
            '<link rel="canonical" href="https://gadgetshifthub.com/it/italy/">',
            f'<link rel="canonical" href="{base}">',
        ),
        (
            '<meta property="og:title" content="AUREN™ | Camino elettrico LED 3D | -50%">',
            f'<meta property="og:title" content="{c["og_title"]}">',
        ),
        (
            '<meta property="og:description" content="Riscaldamento veloce, effetto camino e gestione da smartphone. 96 € in contrassegno.">',
            f'<meta property="og:description" content="{sub(c, "og_desc", price=now)}">',
        ),
        (
            '<meta property="og:url" content="https://gadgetshifthub.com/it/italy/">',
            f'<meta property="og:url" content="{base}">',
        ),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'italy',", f"  PRODUCT_SLUG: '{slug}',"),
        ("  CURRENCY: 'EUR',", f"  CURRENCY: '{offer['currency']}',"),
        ("  PRICE: 96,", f"  PRICE: {offer['price']},"),
        ("  OFFER_NAME: 'AUREN IT',", f"  OFFER_NAME: 'AUREN {geo.upper()} #{oid}',"),
        ("  LP_ID: 'it-italy',", f"  LP_ID: '{geo}-{oid}',"),
        ("  FORM_OFFER: '2635',", f"  FORM_OFFER: '{oid}',"),
        ("  FORM_LP: '2662',", f"  FORM_LP: '{lp}',"),
        (
            "  THANKYOU_URL: 'https://gadgetshifthub.com/it/italy/thank-you.html',",
            f"  THANKYOU_URL: '{ty}',",
        ),
        ("Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.", c["cookie_text"]),
        ("COOKIE_ACCEPT: 'Accetta',", f"COOKIE_ACCEPT: '{c['cookie_accept']}',"),
        ("COOKIE_LEARN: 'Scopri di più'", f"COOKIE_LEARN: '{c['cookie_learn']}'"),
        (
            "🔥 SOLO OGGI: −50% + SPEDIZIONE GRATUITA · PAGAMENTO ALLA CONSEGNA 🔥",
            c["topbar"],
        ),
        (
            "<strong>4,8/5</strong> · Oltre <strong>8.700</strong> clienti hanno già scelto un camino elettrico per il living",
            c["rating"],
        ),
        (
            "🎁 INCLUSI: TELECOMANDO + APP PER COMANDARE IL CAMINO DALLO SMARTPHONE",
            c["gift"],
        ),
        (
            '<h1 class="h1-mobile-only"><span class="hl">Living più caldo e accogliente</span>, calore veloce senza caldaia né cantieri.</h1>',
            c["h1_mobile"],
        ),
        (
            '<h1 class="h1-desktop-only"><span class="hl">Living più caldo e accogliente</span>, calore veloce senza caldaia né cantieri.</h1>',
            c["h1_desktop"],
        ),
        (
            "<strong>AUREN™</strong> unisce l'atmosfera di un fuoco vero al comfort elettrico: 2000 W di potenza, calore fino a 80 m², 3 livelli (800 / 1500 / 2000 W) e classe energetica A+++. Fiamma LED 3D da circa 0,20 € al giorno, timer, app WiFi e telecomando. Niente tecnico né pellet: inserisci la spina e il living si scalda in pochi minuti.",
            c["lead"],
        ),
        (
            'alt="Camino elettrico con fiamma LED 3D, app e telecomando"',
            f'alt="{c["alt_hero"]}"',
        ),
        (
            '<span class="was">192 €</span><span class="now">96 €</span><span class="disc">-50%</span>',
            price_block,
        ),
        ('<span class="ship">contrassegno</span>', ship),
        ("ORDINA ORA E PAGA ALLA CONSEGNA →", c["cta_order"]),
        (
            "🔒 Nessun anticipo · Nessuna carta · Paghi solo quando ricevi il pacco",
            c["form_note_hero"],
        ),
        (
            "<h4>Calore fino a 80 m²</h4><p>Sensazione di caldo in pochi minuti, senza attese lunghe</p>",
            f'<h4>{c["f1_h"]}</h4><p>{c["f1_p"]}</p>',
        ),
        (
            "<h4>Plug & play</h4><p>Collega e usa subito, senza tecnico</p>",
            f'<h4>{c["f2_h"]}</h4><p>{c["f2_p"]}</p>',
        ),
        (
            "<h4>App · WiFi · telecomando</h4><p>Imposta temperatura e timer da remoto</p>",
            f'<h4>{c["f3_h"]}</h4><p>{c["f3_p"]}</p>',
        ),
        (
            "<h4>Sicurezza integrata</h4><p>Auto spegnimento anti surriscaldamento</p>",
            f'<h4>{c["f4_h"]}</h4><p>{c["f4_p"]}</p>',
        ),
        (
            "⏰ Lo sconto del 50% vale fino a esaurimento scorte promozionali",
            c["countdown"],
        ),
        ('<div class="lbl">Ore</div>', f'<div class="lbl">{c["hours"]}</div>'),
        ('<div class="lbl">Min</div>', f'<div class="lbl">{c["mins"]}</div>'),
        ('<div class="lbl">Sec</div>', f'<div class="lbl">{c["secs"]}</div>'),
        (
            '          <span class="left">Disponibilità</span>\n          <span class="right">Restano 3 pezzi a prezzo promo</span>',
            f'          <span class="left">{c["stock_l"]}</span>\n          <span class="right">{c["stock_r"]}</span>',
        ),
        (
            'data-live="<strong>{n} persone</strong> stanno valutando questa promo ora"><strong>15 persone</strong> stanno valutando questa promo ora',
            f'data-live="{c["live_tpl"]}">{live}',
        ),
        ("<h2>Invia la richiesta: AUREN™ a 96 €</h2>", f"<h2>{sub(c, 'form_h2', price=now)}</h2>"),
        (
            "<p>Compila nome, telefono e indirizzo: ti contattiamo per confermare la consegna, zero pagamenti anticipati.</p>",
            f"<p>{c['form_p']}</p>",
        ),
        ("<label for=\"name\">Nome e cognome*</label>", f'<label for="name">{c["label_name"]}</label>'),
        ('placeholder="Maria Rossi"', f'placeholder="{c["ph_name"]}"'),
        ("<label for=\"tel\">Telefono*</label>", f'<label for="tel">{c["label_tel"]}</label>'),
        ('placeholder="+39 333 123 4567"', f'placeholder="{c["ph_tel"]}"'),
        (
            "<label for=\"street-address\">Indirizzo*</label>",
            f'<label for="street-address">{c["label_addr"]}</label>',
        ),
        ('placeholder="Via Roma 10, 20121 Milano"', f'placeholder="{c["ph_addr"]}"'),
        ('<input name="offer" type="hidden" value="2635">', f'<input name="offer" type="hidden" value="{oid}">'),
        ('<input name="lp" type="hidden" value="2662">', f'<input name="lp" type="hidden" value="{lp}">'),
        (
            'value="https://gadgetshifthub.com/it/italy/thank-you.html"',
            f'value="{ty}"',
        ),
        ("CONFERMA ORDINE", c["btn_submit"]),
        (
            "🔒 Nessun anticipo · Nessuna carta · Paghi solo alla consegna",
            c["form_note"],
        ),
        ('alt="Camino nel soggiorno: calore e atmosfera"', f'alt="{c["alt_w1"]}"'),
        ("01 · Calore immediato", c["w1_eye"]),
        ("Calore percepibile in pochi minuti, superficie fino a 80 m²", c["w1_h"]),
        (
            '<span class="tag">Minuti</span><span class="tag">Fino a 80 m²</span><span class="tag">Senza tubature</span>',
            f'<span class="tag">{c["w1_t1"]}</span><span class="tag">{c["w1_t2"]}</span><span class="tag">{c["w1_t3"]}</span>',
        ),
        (
            "I radiatori spesso impiegano <strong>1–2 ore</strong>. <strong>AUREN™</strong> riscalda in <strong>pochi minuti</strong> su <strong>fino a 80 m²</strong>, senza dispersioni della rete idraulica.",
            c["w1_p"],
        ),
        (
            "Appartamento o casa mal isolata: un unico elemento compatto per più benessere.",
            c["w1_i"],
        ),
        ('alt="Collegamento alla presa in pochi secondi"', f'alt="{c["alt_w2"]}"'),
        ("02 · Senza lavori", c["w2_eye"]),
        ("Presa e via, nessun installatore", c["w2_h"]),
        (
            '<span class="tag">Solo presa</span><span class="tag">Portatile</span><span class="tag">Senza canna fumaria</span>',
            f'<span class="tag">{c["w2_t1"]}</span><span class="tag">{c["w2_t2"]}</span><span class="tag">{c["w2_t3"]}</span>',
        ),
        (
            "Senza caldaia, tubi o canna fumaria: <strong>apri, collega e accendi</strong>. Spostalo dove ti serve.",
            c["w2_p"],
        ),
        (
            "Con <strong>AUREN™</strong> alleggerisci spese di gas e montaggio, con l'effetto camino in salotto.",
            c["w2_i"],
        ),
        (
            'alt="Fiamma LED 3D e controllo con telecomando"',
            f'alt="{c["alt_w3"]}"',
        ),
        ("03 · Fiamma e controllo", c["w3_eye"]),
        ("2000 W reali, fiamma LED 3D di fascia alta", c["w3_h"]),
        (
            '<span class="tag">2000 W</span><span class="tag">App · WiFi</span><span class="tag">Telecomando IR</span>',
            f'<span class="tag">{c["w3_t1"]}</span><span class="tag">{c["w3_t2"]}</span><span class="tag">{c["w3_t3"]}</span>',
        ),
        (
            "Potenza fino a <strong>2000 W</strong> per grandi ambienti in sicurezza. <strong>Fiamma LED 3D</strong> anche senza riscaldamento: zero fumo, cenere o scorta di legna. Timer, modalità e temperatura da app o telecomando IR.",
            c["w3_p"],
        ),
        (
            "Effetto fiamma e calore separati: atmosfera camino tutto l'anno.",
            c["w3_i"],
        ),
        ("SÌ, VOGLIO L'OFFERTA →", c["cta_offer"]),
        (
            "Perché AUREN™ ha senso rispetto a caldaia e pellet",
            c["cmp_label"],
        ),
        ("Centralina e radiatori vs AUREN™", c["cmp_h2"]),
        (
            'aria-label="Confronto riscaldamento tradizionale e camino elettrico AUREN"',
            f'aria-label="{c["cmp_aria"]}"',
        ),
        (
            "<th></th><th>Centralina e radiatori</th><th class=\"highlight\">AUREN™</th></tr>",
            f'<th></th><th>{c["th_trad"]}</th><th class="highlight">{c["th_auren"]}</th></tr>',
        ),
        (
            "<td>Tempo per sentire calore</td><td>❌ 1–2 ore</td><td class=\"win\">✅ Pochi minuti</td>",
            f'<td>{c["cmp_r1_l"]}</td><td>{c["cmp_r1_a"]}</td><td class="win">{c["cmp_r1_b"]}</td>',
        ),
        (
            "<td>Installazione</td><td>❌ Migliaia di € e lavori</td><td class=\"win\">✅ Solo una presa</td>",
            f'<td>{c["cmp_r2_l"]}</td><td>{c["cmp_r2_a"]}</td><td class="win">{c["cmp_r2_b"]}</td>',
        ),
        (
            "<td>Gas e manutenzione</td><td>❌ Bollette alte e revisioni</td><td class=\"win\">✅ Elettrico efficiente A+++</td>",
            f'<td>{c["cmp_r3_l"]}</td><td>{c["cmp_r3_a"]}</td><td class="win">{c["cmp_r3_b"]}</td>',
        ),
        (
            "<td>Atmosfera camino</td><td>❌ Non la offre</td><td class=\"win\">✅ Fiamma LED 3D regolabile</td>",
            f'<td>{c["cmp_r4_l"]}</td><td>{c["cmp_r4_a"]}</td><td class="win">{c["cmp_r4_b"]}</td>',
        ),
        (
            "<td>Controllo</td><td>❌ Termosifoni manuali</td><td class=\"win\">✅ App · WiFi · telecomando IR</td>",
            f'<td>{c["cmp_r5_l"]}</td><td>{c["cmp_r5_a"]}</td><td class="win">{c["cmp_r5_b"]}</td>',
        ),
        (
            '      <span class="eyebrow">★ 4,8/5 · Acquisto verificato · Recensioni moderate</span>',
            f'      <span class="eyebrow">{c["test_eye"]}</span>',
        ),
        (
            "<h2>Decine di famiglie hanno scelto AUREN™. Le loro impressioni:</h2>",
            f"<h2>{c['test_h2']}</h2>",
        ),
        ('alt="Unboxing con telecomando"', f'alt="{c["alt_t1"]}"'),
        ("Confezione completa, tutto a posto", c["t1_h"]),
        (
            "«Ho scartato il pacco e dentro c'erano camino, telecomando e istruzioni in italiano. In un minuto era operativo; ho saldato solo al corriere, zero anticipi. A 96 € il set completo è un'occasione che non volevo lasciarmi sfuggire.»",
            sub(c, "t1_p", price=now),
        ),
        (
            "Elena W., Torino, Acquisto verificato",
            c["t1_auth"],
        ),
        ('alt="Lucia con telecomando"', f'alt="{c["alt_t2"]}"'),
        ("Niente preventivi a cinque cifre", c["t2_h"]),
        (
            "«Pellet e camino tradizionale erano fuori budget. Riscalda tutta la zona living a un prezzo accessibile; lo accendo dall'app prima di rientrare. Niente preventivi da migliaia di euro, l'ho ordinato subito perché tornava.»",
            c["t2_p"],
        ),
        ("Lucia M., Milano, Acquisto verificato", c["t2_auth"]),
        ('alt="Marco in soggiorno"', f'alt="{c["alt_t3"]}"'),
        ("Meno gas in bolletta", c["t3_h"]),
        (
            "«85 m² e radiatori lentissimi, il gas pesava troppo in bolletta. Con 96 € invece di 192 €, scalda in pochi minuti e l'effetto fiamma è bellissimo. Pagato al corriere, consegnato in due giorni: per me è stata una scelta azzeccata.»",
            sub(c, "t3_p", price=now, was_price=was),
        ),
        ("Marco R., Roma, Acquisto verificato", c["t3_auth"]),
        ('    <span class="eyebrow">Nel pacco</span>', f'    <span class="eyebrow">{c["kit_eye"]}</span>'),
        (
            "<h2>📦 Set completo AUREN™: accendi al primo utilizzo</h2>",
            f"<h2>{c['kit_h2']}</h2>",
        ),
        (
            'alt="Camino elettrico con app e telecomando"',
            f'alt="{c["alt_kit"]}"',
        ),
        (
            "<li><strong>1× AUREN™</strong> camino elettrico 2000 W, classe energetica A+++</li>",
            f"<li>{c['kit_i1']}</li>",
        ),
        (
            "<li>Telecomando IR in dotazione: fiamma e calore comodamente dal divano</li>",
            f"<li>{c['kit_i2']}</li>",
        ),
        (
            "<li>App con WiFi: comandi dallo smartphone</li>",
            f"<li>{c['kit_i3']}</li>",
        ),
        (
            "<li>3 livelli di potenza: 800 / 1500 / 2000 W</li>",
            f"<li>{c['kit_i4']}</li>",
        ),
        (
            "<li>Effetto fiamma LED 3D regolabile, calore attivabile a piacere</li>",
            f"<li>{c['kit_i5']}</li>",
        ),
        (
            "<li>Sistema anti surriscaldamento integrato</li>",
            f"<li>{c['kit_i6']}</li>",
        ),
        (
            "<li>Manuale utente in italiano</li>",
            f"<li>{c['kit_i7']}</li>",
        ),
        (
            "<li>Spedizione gratuita 24–48 h lavorative dopo conferma telefonica · Contrassegno · 30 giorni soddisfatti o rimborsati</li>",
            f"<li>{c['kit_ship']}</li>",
        ),
        ("ORDINA ORA →", c["cta_kit"]),
        ("<h2>Domande frequenti</h2>", f"<h2>{c['faq_h2']}</h2>"),
        ("<span>Come si effettua l'ordine?</span>", f"<span>{c['faq1_q']}</span>"),
        (
            "<p>Inserisci i dati nel modulo: ti richiamiamo per fissare la consegna.</p>",
            f"<p>{c['faq1_a']}</p>",
        ),
        ("<span>Posso pagare alla consegna?</span>", f"<span>{c['faq2_q']}</span>"),
        (
            "<p>Sì. Saldare 96 € al corriere alla consegna, pratico e sicuro, senza anticipo.</p>",
            f"<p>{sub(c, 'faq2_a', price=now)}</p>",
        ),
        (
            "<span>Quanto tempo richiede la spedizione?</span>",
            f"<span>{c['faq3_q']}</span>",
        ),
        (
            "<p>La spedizione express impiega di solito <strong>24–48 ore lavorative</strong> dopo la <strong>conferma telefonica</strong> dell'ordine.</p>",
            f"<p>{c['faq3_a']}</p>",
        ),
        ("<span>Quanti m² copre AUREN™?</span>", f"<span>{c['faq4_q']}</span>"),
        (
            "<p>Fino a <strong>80 m²</strong> in pochi minuti, in base a isolamento e altezza dei soffitti.</p>",
            f"<p>{c['faq4_a']}</p>",
        ),
        ("<span>Serve un installatore?</span>", f"<span>{c['faq5_q']}</span>"),
        (
            "<p>No. Presa standard 230 V, senza tubature, condotto o forature.</p>",
            f"<p>{c['faq5_a']}</p>",
        ),
        (
            "<span>Posso usare solo la fiamma, senza calore?</span>",
            f"<span>{c['faq6_q']}</span>",
        ),
        (
            "<p>Sì. <strong>La fiamma LED 3D e il riscaldamento sono indipendenti</strong>, atmosfera tutto l'anno.</p>",
            f"<p>{c['faq6_a']}</p>",
        ),
        ("<span>I miei dati sono protetti?</span>", f"<span>{c['faq7_q']}</span>"),
        (
            "<p>Sì. I dati sono trattati secondo l'informativa privacy del sito e condivisi solo con il corriere.</p>",
            f"<p>{c['faq7_a']}</p>",
        ),
        (
            "<span>Cosa succede se non sono soddisfatto?</span>",
            f"<span>{c['faq8_q']}</span>",
        ),
        (
            "<p>Hai <strong>30 giorni</strong> dalla consegna per il rimborso completo, oltre alla garanzia su difetti di fabbricazione.</p>",
            f"<p>{c['faq8_a']}</p>",
        ),
        (
            "Soluzioni per la casa, spedizione veloce e pagamento in contrassegno.",
            c["footer_blurb"],
        ),
        ("Gestito da", c.get("footer_managed", "Gestito da")),
        ("Informazioni", c["footer_info"]),
        ("Chi siamo", c["footer_about"]),
        ("Contattaci", c["footer_contact"]),
        ("Informativa sulla privacy", c["footer_privacy"]),
        ("Termini e condizioni", c["footer_terms"]),
        ("Politica sui cookie", c["footer_cookie"]),
        ("Politica di spedizione", c["footer_shipping"]),
        ("Politica di reso", c["footer_refund"]),
        (
            '<h4 class="site-footer__heading">Contatti</h4>',
            f'<h4 class="site-footer__heading">{c["footer_contacts"]}</h4>',
        ),
        ("Stati Uniti", c["footer_us"]),
        ('href="/it/', f'href="/{geo}/'),
        ("<!-- Offer #2635", f"<!-- Offer #{oid}"),
    ]


def ty_pairs(c: dict, offer: dict) -> list[tuple[str, str]]:
    geo = offer["geo"]
    slug = slug_for(offer)
    oid = offer["offer_id"]
    ty = ty_url(offer)
    cur = offer["currency"]
    price = offer["price"]
    cpa = offer["cpa"]

    return [
        ('lang="it"', f'lang="{offer["lang"]}"'),
        ('content="2635"', f'content="{oid}"'),
        (
            "Ordine ricevuto — Attendi la chiamata di conferma | AUREN™",
            c["ty_title"],
        ),
        (
            "Il tuo ordine AUREN™ è stato ricevuto. Resta solo un passaggio: rispondere alla chiamata del nostro operatore per confermare i dati.",
            c["ty_meta"],
        ),
        ("https://gadgetshifthub.com/it/italy/thank-you.html", ty),
        ("  GEO: 'it',", f"  GEO: '{geo}',"),
        ("  PRODUCT_SLUG: 'italy',", f"  PRODUCT_SLUG: '{slug}',"),
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
        (
            'alt="Il team gadgetshifthub al lavoro: call center e logistica COD"',
            f'alt="{c["ty_img_alt"]}"',
        ),
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
        (
            "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
            c["ty_s1"],
        ),
        (
            "Il tuo ordine verrà preparato entro <strong>24–48 ore</strong>",
            c["ty_s2"],
        ),
        (
            "Ricevi il pacco a domicilio e <strong>paghi alla consegna</strong>",
            c["ty_s3"],
        ),
        ("🔒 Pagamento alla consegna", c["ty_b1"]),
        ("🛡️ Garanzia 24 mesi", c["ty_b2"]),
        ("🔐 Protezione SSL", c["ty_b3"]),
        ("Informazioni", c["footer_info"]),
        ("Chi siamo", c["footer_about"]),
        ("Contattaci", c["footer_contact"]),
        ("Privacy Policy", c["footer_privacy_ty"]),
        ("Termini e Condizioni", c["footer_terms_ty"]),
        ("Cookie Policy", c["footer_cookie_ty"]),
        ("Politica di Spedizione", c["footer_shipping_ty"]),
        ("Politica di Rimborso", c["footer_refund_ty"]),
        (
            '<h4 class="site-footer__heading">Contatti</h4>',
            f'<h4 class="site-footer__heading">{c["footer_contacts"]}</h4>',
        ),
        ("Stati Uniti", c["footer_us"]),
        ('href="/it/', f'href="/{geo}/'),
        ("Gestito da", c.get("footer_managed", "Gestito da")),
        ("<!-- Offer #2635", f"<!-- Offer #{oid}"),
    ]


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    copy = load_copy()
    it_index = IT_INDEX.read_text(encoding="utf-8")
    it_ty = IT_TY.read_text(encoding="utf-8")

    errors: list[str] = []

    for offer in OFFERS:
        lang = offer["lang"]
        if lang not in copy:
            errors.append(f"Missing COPY for lang={lang}")
            continue
        c = copy[lang]
        rel = f"{offer['geo']}/{slug_for(offer)}"
        out_dir = ROOT / rel
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            idx = apply_pairs(it_index, index_pairs(c, offer))
            idx = insert_ai_notice_in_site_footer(idx, offer["lang"])
            (out_dir / "index.html").write_text(idx, encoding="utf-8")
            ty = apply_pairs(it_ty, ty_pairs(c, offer))
            (out_dir / "thank-you.html").write_text(ty, encoding="utf-8")
            print(f"Wrote {rel}/index.html + thank-you.html")
        except KeyError as exc:
            errors.append(f"{rel}: {exc}")

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)

    import update_auren_fireplace_forms as _patch_forms

    _patch_forms.main()
    print("done")


if __name__ == "__main__":
    main()
