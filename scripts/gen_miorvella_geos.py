#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Miorvella™ topper landings + thank-you pages for campaign geos."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "miorvella_network_forms",
        Path(__file__).with_name("miorvella_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


GEOS = {
    "3038": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "price": 69.00,
        "currency": "EUR",
        "slug": "miorvella",
        "cpa": 19.0,
    },
    "3039": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "price": 69.00,
        "currency": "EUR",
        "slug": "miorvella",
        "cpa": 19.0,
    },
    "3040": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "price": 99.00,
        "currency": "EUR",
        "slug": "miorvella",
        "cpa": 18.0,
    },
    "3041": {
        "geo": "lt",
        "lang": "lt",
        "tr": "lt",
        "price": 89.00,
        "currency": "EUR",
        "slug": "miorvella",
        "cpa": 21.0,
    },
    "3042": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 299.00,
        "currency": "PLN",
        "slug": "miorvella",
        "cpa": 17.0,
    },
    "3044": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cz",
        "price": 2099.00,
        "currency": "CZK",
        "slug": "miorvella",
        "cpa": 18.0,
    },
    "2189": {
        "geo": "it",
        "lang": "it",
        "tr": "it",
        "price": 79.99,
        "currency": "EUR",
        "slug": "miorvella",
        "cpa": 18.0,
    },
}

SIZES = ("140x200", "160x200", "180x200")

# Italian source strings → translation keys (longest-first replacement order).
IT_STRINGS: dict[str, str] = {
    "Miorvella™ — Topper ortopedico in memory foam 10cm con gel termoregolante | Pagamento alla consegna": "title",
    "Miorvella™: topper ortopedico in memory foam 10cm con gel termoregolante. 93% degli utenti nota riduzione del dolore articolare dopo 15 notti. Pagamento alla consegna.": "description",
    "SOLO OGGI: -70% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA": "topbar",
    "<strong>4,9/5</strong> — Oltre <strong>9.480</strong> persone dormono meglio ogni notte": "rating",
    "🚚 Spedizione gratuita + Garanzia 2 anni inclusa": "gift",
    "Il 93% nota meno dolore articolare già dopo 15 notti.": "h1",
    "<strong>Miorvella™</strong> — Non è un materasso nuovo. È 10 cm di memory foam ortopedico che si adatta al tuo corpo, scarica la pressione da schiena, spalle e fianchi, e trasforma un materasso vecchio o troppo rigido in una superficie che finalmente ti lascia dormire.": "lead",
    "Miorvella™ topper ortopedico in memory foam 10 cm con gel termoregolante": "alt_hero",
    "SÌ, VOGLIO MIORVELLA™ →": "cta",
    "🔒 Zero anticipo · Zero carta · Paghi solo quando lo ricevi": "form_note",
    "Spedizione gratuita": "f1_h",
    "Consegna in tutta Italia": "f1_p",
    "Paghi alla consegna": "f2_h",
    "Nessuna carta richiesta": "f2_p",
    "Garanzia 2 anni": "f3_h",
    "Copertura completa inclusa": "f3_p",
    "Reso 30 giorni": "f4_h",
    "Rimborso pieno, senza domande": "f4_p",
    "⏰ Prezzo -70% bloccato ancora per": "countdown",
    "Ore": "hours",
    "Min": "mins",
    "Sec": "secs",
    "Disponibilità magazzino": "stock_l",
    "Solo 4 pezzi rimasti": "stock_r",
    '<strong>{n} persone</strong> stanno guardando Miorvella™ ora': "live",
    "<strong>38 persone</strong> stanno guardando Miorvella™ ora": "live0",
    "Compila i campi qui sotto. Ti chiamiamo entro 24h per confermare la consegna — nessun addebito prima.": "form_p",
    "Nome e Cognome*": "label_name",
    "Mario Rossi": "ph_name",
    "Numero di telefono*": "label_phone",
    "+39 333 123 4567": "ph_phone",
    "Indirizzo di consegna*": "label_addr",
    "Via Roma 10, 00100 Roma": "ph_addr",
    "Misura*": "label_size",
    "140x200 / 160x200 / 180x200": "size_ph",
    "Inserisci nome e cognome": "err_name",
    "Inserisci il numero di telefono": "err_phone",
    "Inserisci l'indirizzo di consegna": "err_addr",
    "Seleziona una misura": "err_size",
    "Controlla i campi evidenziati e riprova.": "submit_err",
    "SÌ, ORDINO MIORVELLA™": "btn_submit",
    "01 — Miorvella™: sollievo vero, misurato": "w1_ey",
    "10 cm di memory foam ortopedico: il 93% degli utenti nota meno dolore già dopo 15 notti": "w1_h",
    "Memory foam 10cm": "w1_t1",
    "Sollievo articolare": "w1_t2",
    "Risultati in 15 notti": "w1_t3",
    "Un materasso troppo rigido scarica tutto il peso su spalle e fianchi: ti giri, ti risvegli, ti alzi indolenzito. Il memory foam di Miorvella™ si modella sul tuo corpo e distribuisce la pressione in modo uniforme, invece di concentrarla nei punti che fanno più male.": "w1_p1",
    "Non è una promessa vaga: nei nostri test interni, 93 persone su 100 hanno riferito meno dolore a schiena, spalle e fianchi entro due settimane d'uso.": "w1_p2",
    "02 — Miorvella™: Fresco d'estate, caldo d'inverno, sempre lo stesso comfort": "w2_ey",
    "Gel termoregolante integrato: la temperatura giusta in ogni stagione": "w2_h",
    "Gel termoregolante": "w2_t1",
    "Comfort tutto l'anno": "w2_t2",
    "Nessuna svolta a metà notte": "w2_t3",
    "Il memory foam tradizionale trattiene calore e ti fa svegliare accaldato in estate. Il gel termoregolante integrato in Miorvella™ disperde il calore in eccesso quando fa caldo e mantiene il tepore quando le temperature scendono.": "w2_p1",
    "Il risultato: la stessa qualità del sonno a gennaio come a luglio, senza girare il cuscino o buttare via le coperte a metà notte.": "w2_p2",
    "03 — Miorvella™: Igiene garantita, notte dopo notte": "w3_ey",
    "Fodera sfoderabile e lavabile in lavatrice, fissata con 4 bande elastiche resistenti": "w3_h",
    "Fodera lavabile": "w3_t1",
    "4 bande elastiche": "w3_t2",
    "Anti-acaro": "w3_t3",
    "Le 4 bande elastiche tengono Miorvella™ ancorato al materasso: non scivola, non si sposta durante la notte. La fodera si sfila in pochi secondi e va in lavatrice come qualsiasi lenzuolo, mantenendo il letto fresco e pulito.": "w3_p1",
    "Trattata contro acari e batteri: ideale anche per chi soffre di allergie o ha la pelle sensibile.": "w3_p2",
    "04 — Miorvella™: Funziona ovunque dormi, anche sul divano letto": "w4_ey",
    "Rinnova il tuo materasso — o il divano letto — senza comprarne uno nuovo": "w4_h",
    "Compatibile divano letto": "w4_t1",
    "Si piega per riporlo": "w4_t2",
    "Prolunga la vita del materasso": "w4_t3",
    "Il tuo materasso è vecchio o troppo duro? Miorvella™ lo trasforma in una superficie più morbida e accogliente, ne allunga la vita utile e ti risparmia il costo di uno nuovo.": "w4_p1",
    "Funziona altrettanto bene su un divano letto: dà spessore, stabilità e la sensazione di un vero materasso, e si piega facilmente per essere riposto quando non serve.": "w4_p2",
    "Confronto diretto": "cmp_label",
    "Materasso normale vs Miorvella™": "cmp_h2",
    "Senza Miorvella™": "cmp_th_without",
    "Con Miorvella™": "cmp_th_with",
    "Dolore articolare": "cmp_r1_label",
    "Pressione concentrata su schiena, spalle, fianchi": "cmp_r1_without",
    "Memory foam distribuisce il peso, meno pressione": "cmp_r1_with",
    "Temperatura": "cmp_r2_label",
    "Caldo in estate, freddo in inverno": "cmp_r2_without",
    "Gel termoregolante, comfort tutto l'anno": "cmp_r2_with",
    "Igiene": "cmp_r3_label",
    "Difficile da pulire in profondità": "cmp_r3_without",
    "Fodera sfoderabile e lavabile in lavatrice": "cmp_r3_with",
    "Durata materasso": "cmp_r4_label",
    "Si consuma e va sostituito": "cmp_r4_without",
    "Protegge e allunga la vita del materasso": "cmp_r4_with",
    "Divano letto": "cmp_r5_label",
    "Scomodo, sottile": "cmp_r5_without",
    "Stesso comfort di un vero materasso": "cmp_r5_with",
    "Oltre 9.480 persone dormono meglio. Ecco perché hanno scelto Miorvella™.": "test_h2",
    "Dopo due settimane il dolore alla schiena è quasi sparito.": "rev1_h",
    "«Avevo il materasso troppo rigido da anni e mi svegliavo sempre indolenzita. Con Miorvella™ il cambiamento si è sentito già dopo pochi giorni.»": "rev1_p",
    "Roberto G. — Cliente verificato": "rev1_author",
    "Qualità ottima, si sente subito la differenza.": "rev2_h",
    "«L'ho ordinato per me e mio marito: dopo un mese dormiamo entrambi molto meglio. Il tessuto è morbido, la fodera si lava facilmente e fa esattamente quello che promette.»": "rev2_p",
    "Elena R. — Cliente verificata": "rev2_author",
    "L'ho preso per il divano letto degli ospiti, ora sembra un vero letto.": "rev3_h",
    "«Ho ordinato la misura 140x200 per il divano letto degli ospiti. Non pensavo facesse così tanta differenza: ora dormono comodi come a casa loro.»": "rev3_p",
    "Marta T. — Cliente verificata": "rev3_author",
    "Nella confezione": "kit_ey",
    "Kit completo Miorvella™, pronto da stendere e usare": "kit_h2",
    "1× Miorvella™ — topper ortopedico in memory foam 10 cm con gel termoregolante": "kit_li1",
    "1× Fodera sfoderabile e lavabile in lavatrice": "kit_li2",
    "4× Bande elastiche di fissaggio": "kit_li3",
    "Disponibile in 3 misure: 140x200 · 160x200 · 180x200": "kit_li4",
    "Garanzia ufficiale di 2 anni": "kit_li5",
    "Domande frequenti": "faq_h2",
    "Quanto ci mette ad arrivare?": "fq1",
    "1-2 giorni lavorativi. Ti chiamiamo entro 24 ore per confermare l'ordine e l'orario di consegna.": "fa1",
    "Devo pagare in anticipo?": "fq2",
    "No. Paghi in contanti direttamente al corriere quando Miorvella™ è già a casa tua.": "fa2",
    "Va bene su qualsiasi materasso?": "fq3",
    "Sì. Le 4 bande elastiche si adattano alla maggior parte dei materassi standard nelle misure disponibili.": "fa3",
    "Come si lava?": "fq4",
    "La fodera è completamente sfoderabile e si lava in lavatrice. Miorvella™ in memory foam non va lavato in acqua, basta arieggiarlo.": "fa4",
    "È adatto anche a chi ha allergie?": "fq5",
    "Sì, la fodera è trattata contro acari e batteri, indicata anche per pelli sensibili.": "fa5",
    "E se non mi convince?": "fq6",
    "Hai 30 giorni per restituirlo gratuitamente e ricevere il rimborso completo, senza domande.": "fa6",
    "Ok, sono convinto. Come lo ordino?": "fq7",
    "Compila il modulo qui sopra con nome, telefono e indirizzo. Ti chiamiamo entro 24h per confermare, e Miorvella™ arriva a casa tua in 1-2 giorni. Paghi solo alla consegna.": "fa7",
    "Miorvella™ memory foam 10 cm con gel: strati interni del topper": "alt_w1",
    "Miorvella™ gel termoregolante: comfort d'estate e d'inverno": "alt_w2",
    "Miorvella™ fodera sfoderabile e lavabile in lavatrice": "alt_w3",
    "Miorvella™ fissato con bande elastiche su materasso e divano letto": "alt_w4",
    "Kit completo Miorvella™": "alt_kit",
    "Coppia che installa Miorvella™ sul letto": "alt_rev1",
    "Coppia che dorme su Miorvella™": "alt_rev2",
    "Cliente soddisfatta di Miorvella™ 140x200 sul divano letto": "alt_rev3",
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
    "Invio in corso...": "submitting",
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
<p><a href="/{geo}/{slug}/landing.html">Miorvella™</a></p>
</body>
</html>
"""


def load_translations() -> dict:
    path = Path(__file__).with_name("_miorvella_i18n.py")
    spec = importlib.util.spec_from_file_location("_miorvella_i18n", path)
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
        "https://shoptrendcrest.com/it/treemax/landing.html",
        f"https://shoptrendcrest.com/{geo}/{slug}/landing.html",
    )
    html = html.replace('hreflang="it"', f'hreflang="{cfg["lang"]}"')

    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'treemax'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = html.replace("OFFER_NAME: 'Miorvella IT'", f"OFFER_NAME: 'Miorvella {offer}'")
    html = html.replace("LP_ID: 'it-treemax'", f"LP_ID: '{geo}-{slug}'")

    html = re.sub(r'\s*data-typ="[^"]*"', "", html)

    if cfg["tr"] != "it":
        html = re.sub(
            r"SUBMITTING_LABEL:\s*'[^']*'",
            f"SUBMITTING_LABEL: '{esc_js(tr['submitting'])}'",
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

    html = re.sub(r'<span class="was">[^<]*</span>', f'<span class="was">{was}</span>', html)
    html = re.sub(r'<span class="now">[^<]*</span>', f'<span class="now">{now}</span>', html)
    if cfg["tr"] == "it":
        html = re.sub(
            r"<h2>Blocca il tuo Miorvella™ a [^<]+</h2>",
            f"<h2>Blocca il tuo Miorvella™ a {now}</h2>",
            html,
        )
    else:
        html = html.replace(
            "<h2>Blocca il tuo Miorvella™ a 49€</h2>",
            f"<h2>{tr['form_h2_prefix']} {now}</h2>",
        )
        html = html.replace("49€", now)

    if cfg["tr"] != "it":
        for it_text, key in sorted(IT_STRINGS.items(), key=lambda x: -len(x[0])):
            if key in tr:
                val = tr[key] + "." if key == "rights" else tr[key]
                html = html.replace(it_text, val)

    html = html.replace("/it/", f"/{geo}/")
    html = html.replace(
        f"https://shoptrendcrest.com/{geo}/treemax/",
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
        html = html.replace(
            '<script src="/assets/js/form-handler.js" defer></script>\n', ""
        )
        html = re.sub(r"\n  FORM_ENDPOINT: '[^']*',", "", html)
        html = re.sub(r"\n  SUBMITTING_LABEL: '[^']*',", "", html)
        html = re.sub(r"\n  RELAXED_FORM_VALIDATION: true,", "", html)

    return html


def render_thank_you(
    offer: str, cfg: dict, tr: dict, it_ty: str, size: str | None = None
) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    now = fmt_price(cfg["price"], cfg["currency"])
    html = it_ty

    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'treemax'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = re.sub(
        r"trackPurchase\([\d.]+,\s*'EUR'\)",
        f"trackPurchase({cfg['price']}, '{cfg['currency']}')",
        html,
    )
    if cfg["tr"] != "it":
        html = re.sub(
            r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
            (
                f"COOKIE_TEXT: '{esc_js(tr['cookie_text'])}',\n"
                f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
                f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}'"
            ),
            html,
        )

    if cfg["tr"] != "it":
        if size:
            it_title = (
                f"Ordine ricevuto — Miorvella™ {size} — "
                "Attendi la chiamata di conferma | Miorvella™"
            )
            it_desc = (
                f"Il tuo ordine Miorvella™ {size} è stato registrato. "
                "Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore."
            )
            loc_title = tr["ty_title_size"].format(size=size)
            loc_desc = tr["ty_desc_size"].format(size=size)
            html = html.replace(f"<title>{it_title}</title>", f"<title>{loc_title}</title>")
            html = re.sub(
                rf'<meta name="description" content="{re.escape(it_desc)}"\s*/?>',
                f'<meta name="description" content="{loc_desc}">',
                html,
                count=1,
            )
        else:
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
            "Perfetto — il tuo ordine Miorvella™ è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
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
            f"Consegna a domicilio e <strong>pagamento alla consegna</strong> ({fmt_price(49.0, 'EUR')})",
        ]
        ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
        for it_li, loc_li in zip(it_steps, ty_steps):
            html = html.replace(f"<li>{it_li}</li>", f"<li>{loc_li}</li>")

        it_badges = (
            "🔒 Pagamento alla consegna",
            "🛡️ Garanzia 2 anni",
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
    else:
        html = re.sub(
            r"Consegna a domicilio e <strong>pagamento alla consegna</strong> \([^)]+\)",
            f"Consegna a domicilio e <strong>pagamento alla consegna</strong> ({now})",
            html,
        )

    html = html.replace("/it/", f"/{geo}/")

    html = re.sub(r"'value':\s*[0-9.]+", f"'value': {cfg['cpa']}", html)
    html = re.sub(
        r"<!-- Google Ads Purchase conversion[^>]*>",
        f"<!-- Google Ads Purchase conversion — value = CPA/CPL EUR for offer #{offer} -->",
        html,
    )
    return html


def main(only: set[str] | None = None) -> None:
    tr_all = load_translations()
    it_landing = (ROOT / "it/treemax/landing.html").read_text(encoding="utf-8")
    it_ty = (ROOT / "it/treemax/thank-you.html").read_text(encoding="utf-8")

    urls: list[str] = []
    for offer, cfg in GEOS.items():
        if only is not None and offer not in only:
            continue
        tr = tr_all.get(cfg["tr"], {})
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
        for size in SIZES:
            size_ty = out_dir / f"thank-you-{size}.html"
            if size_ty.exists():
                size_ty.unlink()

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
    import sys

    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
