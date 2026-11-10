#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Dochura laundry cabinet landings + thank-you pages for campaign geos."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "dochura_network_forms",
        Path(__file__).with_name("dochura_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


GEOS = {
    "1912": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "price": 92.00,
        "currency": "EUR",
        "slug": "dochura",
        "cpa": 21.0,
    },
    "1915": {
        "geo": "hu",
        "lang": "hu",
        "tr": "hu",
        "price": 29999.00,
        "currency": "HUF",
        "slug": "dochura",
        "cpa": 17.0,
    },
    "3163": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "price": 79.00,
        "currency": "EUR",
        "slug": "dochura",
        "cpa": 17.0,
    },
    "3164": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "price": 99.00,
        "currency": "EUR",
        "slug": "dochura",
        "cpa": 17.0,
    },
    "3167": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 339.00,
        "currency": "PLN",
        "slug": "dochura",
        "cpa": 18.0,
    },
    "3169": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cz",
        "price": 1899.00,
        "currency": "CZK",
        "slug": "dochura",
        "cpa": 17.0,
    },
    "3910": {
        "geo": "lv",
        "lang": "lv",
        "tr": "lv",
        "price": 85.00,
        "currency": "EUR",
        "slug": "dochura",
        "cpa": 16.0,
    },
    "4321": {
        "geo": "sk",
        "lang": "sk",
        "tr": "sk",
        "price": 74.00,
        "currency": "EUR",
        "slug": "dochura",
        "cpa": 15.0,
    },
}

IT_STRINGS: dict[str, str] = {
    "Dochura — Asciuugatrice portatile pieghevole | Pagamento alla consegna": "title",
    "Dochura: asciugatrice portatile pieghevole con camera chiusa, aria calda e timer. Asciuga i capi in profondità senza dipendere dal meteo. Pagamento alla consegna in tutta Italia.": "description",
    "SOLO OGGI: -70% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA": "topbar",
    "<strong>4,9/5</strong> — Oltre <strong>9.480</strong> persone in Italia si asciugano i vestiti più velocemente ogni giorno": "rating",
    "Risparmi fino al 60% in bolletta + Garanzia 3 anni": "gift",
    "Asciuga e distende fino a 20 kg di bucato in soli 30 minuti, consumando fino al 60% in meno.": "h1",
    "<strong>Dochura</strong> — Ascugatrice portatile pieghevole con camera chiusa e cerniera: appendi i capi dentro, l'elemento riscaldante e la ventola fanno circolare aria calda, l'umidità esce dalle griglie di ventilazione. Timer integrato, spegnimento automatico.": "lead",
    "Dochura in lavanderia — asciugatrice portatile con camera chiusa": "alt_hero",
    "SÌ, VOGLIO DOCHURA →": "cta",
    "🔒 Zero anticipo · Zero carta · Paghi solo quando lo ricevi": "form_note",
    "Spedizione gratuita": "f1_h",
    "Consegna in tutta Italia": "f1_p",
    "Paghi alla consegna": "f2_h",
    "Nessuna carta richiesta": "f2_p",
    "Garanzia 3 anni": "f3_h",
    "Copertura completa inclusa": "f3_p",
    "Reso 30 giorni": "f4_h",
    "Rimborso pieno, senza domande": "f4_p",
    "⏰ Prezzo -70% bloccato ancora per": "countdown",
    "Ore": "hours",
    "Min": "mins",
    "Sec": "secs",
    "Disponibilità magazzino": "stock_l",
    "Solo 4 pezzi rimasti": "stock_r",
    '<strong>{n} persone</strong> stanno guardando Dochura ora': "live",
    "<strong>38 persone</strong> stanno guardando Dochura ora": "live0",
    "Compila i campi qui sotto. Ti chiamiamo entro 24h per confermare la consegna — nessun addebito prima.": "form_p",
    "Nome e Cognome": "ph_name",
    "Numero di telefono": "ph_phone",
    "Indirizzo di consegna": "ph_addr",
    "SÌ, ORDINO DOCHURA": "btn_submit",
    "01 — Come funziona Dochura: passo dopo passo": "w1_ey",
    "Camera chiusa, aria calda in circolo, umidità fuori — spegnimento automatico col timer": "w1_h",
    "Camera chiusa": "w1_t1",
    "Aria calda": "w1_t2",
    "Timer auto": "w1_t3",
    "Apri la cerniera, appendi i capi all'interno e chiudi la camera. L'elemento riscaldante e la ventola fanno girare aria calda in modo uniforme, l'umidità esce dalle pannelli di ventilazione laterali.": "w1_p1",
    "Imposti il timer e te ne dimentichi: al termine del ciclo Dochura si spegne da sola, senza rischi di capi lasciati troppo a lungo.": "w1_p2",
    "02 — Non è la lavatrice il problema": "w2_ey",
    "Asciugatura completa, non solo in superficie — addio odore di umido": "w2_h",
    "Asciugatura profonda": "w2_t1",
    "Meno odore": "w2_t2",
    "Più igiene": "w2_t3",
    "Stendere i vestiti in casa o sullo stendino spesso li fa sembrare asciutti fuori, ma restano umidi nelle pieghe e nelle cuciture. Con il tempo arrivano l'odore sgradevole e quella sensazione di «non proprio pulito».": "w2_p1",
    "Dochura fa circolare aria calda dentro la camera chiusa e raggiunge anche le zone più difficili, così i capi sono davvero pronti da indossare o da riporre nell'armadio.": "w2_p2",
    "03 — Niente sole, niente balcone": "w3_ey",
    "Funziona con qualsiasi tempo — pioggia, inverno o umidità estiva": "w3_h",
    "Indipendente dal meteo": "w3_t1",
    "Circolazione uniforme": "w3_t2",
    "Sempre disponibile": "w3_t3",
    "Non devi più organizzare la giornata in base al sole o al vento. Dochura asciuga quando vuoi tu: la sera, di notte, con il cielo coperto o quando fuori piove da giorni.": "w3_p1",
    "L'aria calda si muove dentro la camera chiusa in modo costante, così non dipendi dalle condizioni fuori casa e non resti con il bucato fermo per giorni.": "w3_p2",
    "04 — Si piega, si ripara, sparisce": "w4_ey",
    "Compatta per monolocali, viaggi e campeggio — pronta quando serve": "w4_h",
    "Pieghevole": "w4_t1",
    "Poco ingombro": "w4_t2",
    "Portatile": "w4_t3",
    "Quando hai finito, Dochura si piega e la riponi in un armadio, sotto il letto o in un ripostiglio. Non serve uno stendino che occupa mezzo soggiorno né un balcone sempre pieno di bucato.": "w4_p1",
    "Ideale per appartamenti piccoli, seconde case, viaggi lunghi o campeggio: porti con te un modo semplice per avere capi asciutti senza dipendere da spazio esterno.": "w4_p2",
    "Confronto diretto": "cmp_label",
    "Asciugatura tradizionale vs Dochura": "cmp_h2",
    "Senza Dochura": "cmp_th_without",
    "Con Dochura": "cmp_th_with",
    "Tempo di asciugatura": "cmp_r1_label",
    "Giorni, dipende da meteo e spazio": "cmp_r1_without",
    "Ciclo guidato in camera chiusa, più prevedibile": "cmp_r1_with",
    "Dipendenza dal meteo": "cmp_r2_label",
    "Sole, vento e umidità esterna": "cmp_r2_without",
    "Funziona sempre, anche con pioggia o in inverno": "cmp_r2_with",
    "Odore di umidità": "cmp_r3_label",
    "Capo che sembra asciutto ma resta umido dentro": "cmp_r3_without",
    "Circolazione di aria calda, meno odore di chiuso": "cmp_r3_with",
    "Spazio in casa": "cmp_r4_label",
    "Stendini, balcone, sedie piene di bucato": "cmp_r4_without",
    "Camera chiusa compatta, si piega e si ripone": "cmp_r4_with",
    "Oltre 9.480 persone in Italia hanno scelto Dochura. Ecco cosa dicono.": "test_h2",
    "Finalmente niente più odore di umido nei capi.": "rev1_h",
    "«Prima sembravano asciutti sullo stendino, ma restavano umidi nelle pieghe. Con Dochura li appendo dentro, imposto il timer e li trovo davvero pronti da mettere nell'armadio.»": "rev1_p",
    "Roberto G. — Cliente verificato": "rev1_author",
    "Con la pioggia fuori, a casa il bucato non si ferma più.": "rev2_h",
    "«Vivo in un monolocale senza balcone: quando pioveva per giorni restavo bloccata con montagne di vestiti umidi. Ora accendo Dochura la sera e al mattino sono asciutti.»": "rev2_p",
    "Davide M. — Cliente verificato": "rev2_author",
    "Si piega e sparisce — perfetta per un appartamento piccolo.": "rev3_h",
    "«Non volevo uno stendino che occupa mezzo soggiorno. Dochura la uso, la chiudo e la ripongo sotto il letto. In viaggio me la porto dietro senza problemi.»": "rev3_p",
    "Marta T. — Cliente verificata": "rev3_author",
    "Nella confezione": "kit_ey",
    "Kit completo Dochura, pronto da usare subito": "kit_h2",
    "1× Dochura — asciugatrice portatile pieghevole con camera chiusa e timer": "kit_li1",
    "1× Cavo di alimentazione": "kit_li2",
    "1× Set di ganci interni per appendere i capi": "kit_li3",
    "1× Borsa o custodia per riporre il prodotto piegato": "kit_li4",
    "Garanzia ufficiale di 3 anni": "kit_li5",
    "Domande frequenti": "faq_h2",
    "Quanto ci mette ad arrivare?": "fq1",
    "1-2 giorni lavorativi in tutta Italia. Ti chiamiamo entro 24 ore per confermare l'ordine e l'orario di consegna.": "fa1",
    "Devo pagare in anticipo?": "fq2",
    "No. Paghi in contanti direttamente al corriere quando Dochura è già a casa tua. Nessuna carta, nessun addebito prima.": "fa2",
    "Che tipi di tessuto posso asciugare?": "fq3",
    "Dochura è adatta a magliette, felpe, intimo, asciugamani, pigiama e capi del quotidiano. Per lana, seta o materiali molto delicati, controlla sempre l'etichetta del capo e usa cicli brevi.": "fa3",
    "Fa molto rumore?": "fq4",
    "Il rumore è paragonabile a quello di un ventilatore domestico: puoi usarla in lavanderia, bagno o camera da letto senza disturbare eccessivamente.": "fa4",
    "Quanto consuma di elettricità?": "fq5",
    "Dochura è pensata per un uso domestico quotidiano con consumo contenuto. Il timer ti aiuta a evitare cicli più lunghi del necessario.": "fa5",
    "E se non mi convince?": "fq6",
    "Hai 30 giorni per restituirlo gratuitamente e ricevere il rimborso completo, senza domande.": "fa6",
    "Ok, sono convinto. Come lo ordino?": "fq7",
    "Compila il modulo qui sopra con nome, telefono e indirizzo. Ti chiamiamo entro 24h per confermare, e Dochura arriva a casa tua in 1-2 giorni. Paghi solo alla consegna.": "fa7",
    "Dochura — circolazione aria calda 360° per asciugatura completa": "alt_w2",
    "Dochura funziona indipendentemente dal meteo": "alt_w3",
    "Dochura piegata e portatile per viaggi": "alt_w4",
    "Dochura in lavanderia con capi appesi": "alt_rev1",
    "Dochura in monolocale con pioggia fuori": "alt_rev2",
    "Dochura piegata riposta sotto il letto": "alt_rev3",
    "Dochura in uso in lavanderia": "alt_kit",
    "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.": "footer_blurb",
    "Informazioni": "info",
    "Chi siamo": "about",
    "Contattaci": "contact",
    "Privacy Policy": "privacy",
    "Termini e Condizioni": "terms",
    "Cookie Policy": "cookie",
    "Politica di spedizione": "ship",
    "Politica di reso": "refund",
    "Contatti": "contacts",
    "Tutti i diritti riservati": "rights",
    "Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.": "cookie_text",
    "Accetta": "cookie_accept",
    "Scopri di più": "cookie_learn",
}

INDEX_TMPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/{slug}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/{slug}/landing.html">
<link rel="canonical" href="https://shoptrendcrest.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">Dochura™</a></p>
</body>
</html>
"""


def load_translations() -> dict:
    path = Path(__file__).with_name("_dochura_i18n.py")
    spec = importlib.util.spec_from_file_location("_dochura_i18n", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.TRANSLATIONS


def was_price(now: float) -> float:
    return float(round(now / 0.3))


def fmt_price(amount: float, currency: str) -> str:
    if currency == "CZK":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},00 Kč"
    if currency == "PLN":
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},{frac:02d} zł"
    if currency == "HUF":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s} Ft"
    if amount == int(amount):
        return f"{int(amount)}€"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s}€"


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def render_landing(offer: str, cfg: dict, tr: dict, it_html: str) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    was = fmt_price(was_price(cfg["price"]), cfg["currency"])
    now = fmt_price(cfg["price"], cfg["currency"])

    html = it_html
    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = html.replace(
        "https://shoptrendcrest.com/it/dochura/landing.html",
        f"https://shoptrendcrest.com/{geo}/{slug}/landing.html",
    )
    html = html.replace('hreflang="it"', f'hreflang="{cfg["lang"]}"')

    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'dochura'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = html.replace("OFFER_NAME: 'Dochura IT'", f"OFFER_NAME: 'Dochura {offer}'")
    html = html.replace("LP_ID: 'it-dochura'", f"LP_ID: '{geo}-{slug}'")

    html = re.sub(
        r"thankyoupage\" type=\"hidden\" value=\"https://shoptrendcrest.com/it/dochura/thank-you.html\"",
        f'thankyoupage" type="hidden" value="https://shoptrendcrest.com/{geo}/{slug}/thank-you.html"',
        html,
    )

    html = re.sub(r'<span class="was">[^<]*</span>', f'<span class="was">{was}</span>', html)
    html = re.sub(r'<span class="now">[^<]*</span>', f'<span class="now">{now}</span>', html)
    html = re.sub(
        r"<h2>Blocca il tuo Dochura a [^<]+</h2>",
        f"<h2>{tr['form_h2_prefix']} {now}</h2>",
        html,
    )

    for it_text, key in sorted(IT_STRINGS.items(), key=lambda x: -len(x[0])):
        if key in tr:
            val = tr[key] + "." if key == "rights" else tr[key]
            html = html.replace(it_text, val)

    html = html.replace("/it/", f"/{geo}/")
    html = html.replace(
        f"https://shoptrendcrest.com/{geo}/dochura/",
        f"https://shoptrendcrest.com/{geo}/{slug}/",
    )

    forms = load_network_forms()
    if offer in forms:
        html = re.sub(
            r'<form class="tm-order-form.*?</form>',
            forms[offer],
            html,
            count=1,
            flags=re.DOTALL,
        )

    return html


def render_thank_you(offer: str, cfg: dict, tr: dict, it_ty: str) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    now = fmt_price(cfg["price"], cfg["currency"])
    html = it_ty

    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'dochura'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = re.sub(
        r"trackPurchase\([\d.]+,\s*'EUR'\)",
        f"trackPurchase({cfg['price']}, '{cfg['currency']}')",
        html,
    )
    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        (
            f"COOKIE_TEXT: '{esc_js(tr['cookie_text'])}',\n"
            f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
            f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}'"
        ),
        html,
    )

    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{tr['ty_title']}</title>",
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="description" content=".*?"\s*/?>',
        f'<meta name="description" content="{tr["ty_desc"]}">',
        html,
        count=1,
    )
    html = html.replace("Il tuo ordine è stato registrato con successo!", tr["ty_h1"])
    html = html.replace(
        "Perfetto — il tuo ordine Dochura™ è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
        tr["ty_sub"],
    )
    html = html.replace(
        "Il team shoptrendcrest al lavoro: call center e logistica COD",
        tr["ty_alt"],
    )
    html = html.replace("👇 Cosa devi fare adesso", tr["ty_eyebrow"])
    html = html.replace("📞 Rispondi alla chiamata di conferma", tr["ty_action_title"])
    html = html.replace(
        "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine.",
        tr["ty_action_body"],
    )
    html = html.replace(
        "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
        tr["ty_action_warn"],
    )
    html = html.replace("🕒 Orari di contatto", tr["ty_hours_h"])
    html = html.replace("<strong>Lunedì – Sabato</strong> · 9:00 – 18:00", tr["ty_hours"])
    html = html.replace("📋 Cosa succede dopo", tr["ty_next_h"])

    it_steps = [
        "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
        "Il tuo ordine verrà spedito entro <strong>24–48 ore</strong>",
        "Consegna a domicilio e <strong>pagamento alla consegna</strong> (34€)",
    ]
    ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
    for it_li, loc_li in zip(it_steps, ty_steps):
        html = html.replace(f"<li>{it_li}</li>", f"<li>{loc_li}</li>")

    it_badges = (
        "🔒 Pagamento alla consegna",
        "🛡️ Garanzia 3 anni",
        "🔐 Protezione SSL",
    )
    for ib, lb in zip(it_badges, tr["ty_badges"]):
        html = html.replace(ib, lb)

    footer_it = (
        "    <div>\n"
        '      <h4 class="site-footer__heading">Informazioni</h4>\n'
        '      <ul class="site-footer__list">\n'
        '        <li><a href="/it/about-us.html">Chi siamo</a></li>\n'
        '        <li><a href="/it/contact-us.html">Contattaci</a></li>\n'
        '        <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>\n'
        '        <li><a href="/it/terms-conditions.html">Termini e Condizioni</a></li>\n'
        '        <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>\n'
        '        <li><a href="/it/shipping-policy.html">Politica di Spedizione</a></li>\n'
        '        <li><a href="/it/refund-policy.html">Politica di Rimborso</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        '      <h4 class="site-footer__heading">Contatti</h4>'
    )
    footer_geo = (
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{tr["info"]}</h4>\n'
        '      <ul class="site-footer__list">\n'
        f'        <li><a href="/{geo}/about-us.html">{tr["about"]}</a></li>\n'
        f'        <li><a href="/{geo}/contact-us.html">{tr["contact"]}</a></li>\n'
        f'        <li><a href="/{geo}/privacy-policy.html">{tr["privacy"]}</a></li>\n'
        f'        <li><a href="/{geo}/terms-conditions.html">{tr["terms"]}</a></li>\n'
        f'        <li><a href="/{geo}/cookie-policy.html">{tr["cookie"]}</a></li>\n'
        f'        <li><a href="/{geo}/shipping-policy.html">{tr["ship"]}</a></li>\n'
        f'        <li><a href="/{geo}/refund-policy.html">{tr["refund"]}</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        f'      <h4 class="site-footer__heading">{tr["contacts"]}</h4>'
    )
    html = html.replace(footer_it, footer_geo)
    html = html.replace("Tutti i diritti riservati.", tr["rights"] + ".")
    html = html.replace("/it/", f"/{geo}/")

    html = re.sub(r"'value':\s*[0-9.]+", f"'value': {cfg['cpa']}", html)
    return html


def main(only: set[str] | None = None) -> None:
    tr_all = load_translations()
    it_landing = (ROOT / "it/dochura/landing.html").read_text(encoding="utf-8")
    it_ty = (ROOT / "it/dochura/thank-you.html").read_text(encoding="utf-8")

    urls: list[str] = []
    for offer, cfg in GEOS.items():
        if only is not None and offer not in only:
            continue
        tr = tr_all[cfg["tr"]]
        geo = cfg["geo"]
        slug = cfg["slug"]
        out_dir = ROOT / geo / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        (out_dir / "landing.html").write_text(
            render_landing(offer, cfg, tr, it_landing), encoding="utf-8"
        )
        (out_dir / "index.html").write_text(
            INDEX_TMPL.format(lang=cfg["lang"], geo=geo, slug=slug),
            encoding="utf-8",
        )
        (out_dir / "thank-you.html").write_text(
            render_thank_you(offer, cfg, tr, it_ty), encoding="utf-8"
        )

        base = f"https://shoptrendcrest.com/{geo}/{slug}"
        urls.extend(
            [
                f"{base}/",
                f"{base}/landing.html",
                f"{base}/thank-you.html",
            ]
        )
        print(
            f"Wrote {geo}/{slug}/ (#{offer}) - "
            f"now={cfg['price']} {cfg['currency']} "
            f"was={was_price(cfg['price'])} CPA={cfg['cpa']}"
        )

    print("\n--- Summary URLs ---")
    for url in urls:
        print(url)


if __name__ == "__main__":
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
