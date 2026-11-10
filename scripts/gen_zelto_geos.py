#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ZELTO™ landings + thank-you pages for campaign geos (skip IT #3990 overwrite)."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer

DOMAIN = "gadgetshifthub.com"
SKIP_OVERWRITE_OFFERS = frozenset({"3990"})

IT_LANDING = ROOT / "it" / "zelto-3990" / "index.html"
IT_THANKYOU = ROOT / "it" / "zelto-3990" / "thank-you.html"

IT_PRICE_NOW = "69 €"
IT_PRICE_WAS = "138 €"
IT_CTA_LITERAL = "ORDINA ZELTO™ →"
IT_FAQ2_A = (
    "Alla consegna: 69 € in contanti al corriere quando ritiri il pacco."
)


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "zelto_network_forms",
        Path(__file__).with_name("zelto_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


def load_it_by_key() -> dict:
    spec = importlib.util.spec_from_file_location(
        "_zelto_it_strings",
        Path(__file__).with_name("_zelto_it_strings.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.IT_STRINGS


def build_it_replace_map(it_by_key: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    skip = {"cta", "cta_inline"}
    for key, val in it_by_key.items():
        if isinstance(val, str) and key not in skip:
            out[val] = key
    return out


GEOS = {
    "762": {
        "geo": "hu",
        "lang": "hu",
        "tr": "hu",
        "price": 39999.00,
        "currency": "HUF",
        "cpa": 16.0,
    },
    "763": {
        "geo": "ro",
        "lang": "ro",
        "tr": "ro",
        "price": 379.00,
        "currency": "RON",
        "cpa": 16.0,
    },
    "765": {
        "geo": "si",
        "lang": "sl",
        "tr": "si",
        "price": 79.00,
        "currency": "EUR",
        "cpa": 16.0,
    },
    "1673": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "price": 89.00,
        "currency": "EUR",
        "cpa": 17.0,
    },
    "1851": {
        "geo": "hr",
        "lang": "hr",
        "tr": "hr",
        "price": 99.00,
        "currency": "EUR",
        "cpa": 16.0,
    },
    "2283": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "price": 89.00,
        "currency": "EUR",
        "cpa": 17.0,
    },
    "2285": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "price": 89.00,
        "currency": "EUR",
        "cpa": 20.0,
    },
    "2287": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 299.00,
        "currency": "PLN",
        "cpa": 21.0,
    },
    "2289": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cs",
        "price": 1999.00,
        "currency": "CZK",
        "cpa": 18.0,
    },
    "3426": {
        "geo": "lv",
        "lang": "lv",
        "tr": "lv",
        "price": 99.00,
        "currency": "EUR",
        "cpa": 18.0,
    },
    "3990": {
        "geo": "it",
        "lang": "it",
        "tr": "it",
        "price": 69.00,
        "currency": "EUR",
        "cpa": 17.0,
    },
    "4067": {
        "geo": "sk",
        "lang": "sk",
        "tr": "sk",
        "price": 99.00,
        "currency": "EUR",
        "cpa": 16.0,
    },
    "4276": {
        "geo": "lt",
        "lang": "lt",
        "tr": "lt",
        "price": 99.00,
        "currency": "EUR",
        "cpa": 18.0,
    },
}

OFFER_PATH_SYNC = """
<script>
(function () {
  var m = location.pathname.match(/\\/zelto-(\\d+)(?:\\/|$)/);
  if (!m) return;
  var id = m[1];
  document.querySelectorAll('input[name="offer"]').forEach(function (el) { el.value = id; });
  if (window.SITE_CONFIG) {
    window.SITE_CONFIG.FORM_OFFER = id;
    window.SITE_CONFIG.OFFER_NAME = 'ZELTO ' + id;
  }
})();
</script>
"""


def offer_folder(offer: str) -> str:
    return f"zelto-{offer}"


def public_base_path(geo: str, offer: str) -> str:
    return f"/{geo}/{offer_folder(offer)}"


def public_landing_url(geo: str, offer: str) -> str:
    return f"https://{DOMAIN}{public_base_path(geo, offer)}/"


def public_thankyou_url(geo: str, offer: str) -> str:
    return f"https://{DOMAIN}{public_base_path(geo, offer)}/thank-you/"


def load_translations() -> dict:
    path = Path(__file__).with_name("_zelto_i18n.py")
    spec = importlib.util.spec_from_file_location("_zelto_i18n", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.TRANSLATIONS)


def was_price(now: float) -> float:
    return float(now * 2)


def list_was_price(cfg: dict) -> float:
    if "was" in cfg:
        return float(cfg["was"])
    return was_price(cfg["price"])


def fmt_price(amount: float, currency: str) -> str:
    if currency == "CZK":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s} Kč"
    if currency == "PLN":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s} zł"
    if currency == "HUF":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s} Ft"
    if currency == "RON":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        if amount == int(amount) or abs(amount - whole) < 0.01:
            return f"{whole_s} lei"
        frac = int(round((amount - whole) * 100))
        return f"{whole_s},{frac:02d} lei"
    if amount == int(amount):
        return f"{int(amount)} €"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s} €"


def normalize_euro_spacing(html: str) -> str:
    return re.sub(r"(?<=\d)€", " €", html)


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def apply_price_remants(html: str, now: str, was: str) -> str:
    html = html.replace(IT_PRICE_NOW, now)
    html = html.replace(IT_PRICE_WAS, was)
    return html


def apply_testimonial_alts(html: str, tr: dict, it_by_key: dict | None = None) -> str:
    if it_by_key is None:
        it_by_key = {}
    for fragment, key in (
        ("review-2.webp", "alt_t1"),
        ("review-1.webp", "alt_t2"),
        ("review-3.webp", "alt_t3"),
    ):
        if key not in tr:
            continue
        alt = tr[key].replace("\\", "\\\\").replace('"', "&quot;")
        html = re.sub(
            rf'(<img class="t-photo" src="[^"]*{fragment}[^"]*" alt=")[^"]*(")',
            rf"\1{alt}\2",
            html,
            count=1,
        )
    # Fallback: replace leftover Italian template alts from IT source
    for key in ("alt_t1", "alt_t2", "alt_t3"):
        if key in tr and key in it_by_key:
            it_alt = it_by_key[key]
            loc_alt = tr[key].replace("\\", "\\\\").replace('"', "&quot;")
            if it_alt in html:
                html = html.replace(f'alt="{it_alt}"', f'alt="{loc_alt}"', 1)
    return html


def apply_footer(html: str, tr: dict, geo: str) -> str:
    blurb = tr.get("footer_blurb", "")
    html = html.replace(
        "Soluzioni per la casa, spedizione veloce e pagamento in contrassegno.",
        blurb,
    )
    # Remove legacy AI paragraph if present (canonical = site-footer__ai-notice via injector).
    html = re.sub(
        r'<p class="site-footer__ai-disclosure">.*?</p>\s*',
        "",
        html,
        flags=re.DOTALL,
    )
    loc_info = (
        f'<h4 class="site-footer__heading">{tr["info"]}</h4>\n'
        f'<ul class="site-footer__list">\n'
        f'<li><a href="/{geo}/about-us.html">{tr["about"]}</a></li>\n'
        f'<li><a href="/{geo}/contact-us.html">{tr["contact"]}</a></li>\n'
        f'<li><a href="/{geo}/privacy-policy.html">{tr["privacy"]}</a></li>\n'
        f'<li><a href="/{geo}/terms-conditions.html">{tr["terms"]}</a></li>\n'
        f'<li><a href="/{geo}/cookie-policy.html">{tr["cookie"]}</a></li>\n'
        f'<li><a href="/{geo}/shipping-policy.html">{tr["ship"]}</a></li>\n'
        f'<li><a href="/{geo}/refund-policy.html">{tr["refund"]}</a></li>\n'
        f"</ul>"
    )
    html = re.sub(
        r'<h4 class="site-footer__heading">Informazioni</h4>\s*'
        r'<ul class="site-footer__list">\s*'
        r"(?:\s*<li><a href=\"[^\"]+\">.*?</li>\s*)+"
        r"</ul>",
        loc_info,
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        '<h4 class="site-footer__heading">Contatti</h4>',
        f'<h4 class="site-footer__heading">{tr["contacts"]}</h4>',
    )
    if tr.get("footer_country"):
        html = html.replace("Stati Uniti", tr["footer_country"])
    if tr.get("footer_managed"):
        html = html.replace("Gestito da", tr["footer_managed"])
    powered_top = tr.get(
        "footer_powered_top",
        "gadgetshifthub.com — Gestito da <strong>Netmart LLC</strong>",
    )
    html = html.replace(
        "gadgetshifthub.com — Gestito da <strong>Netmart LLC</strong></p>",
        f"{powered_top}</p>",
        1,
    )
    powered_bottom = tr.get(
        "footer_powered_bottom",
        "gadgetshifthub.com — Gestito da <strong>Netmart LLC</strong>",
    )
    html = re.sub(
        r'<div class="site-footer__bottom">© <span data-year="">\d+</span> [^<]+</div>',
        f'<div class="site-footer__bottom">© <span data-year="">2026</span> {powered_bottom}</div>',
        html,
        count=1,
    )
    return html


def apply_cta_and_faq_price(html: str, tr: dict, now: str, it_by_key: dict) -> str:
    cta = tr.get("cta_inline", tr.get("cta", IT_CTA_LITERAL))
    if "{price}" in cta:
        cta = cta.format(price=now)
    html = html.replace(IT_CTA_LITERAL, cta)
    for key in (f"faq{n}_a" for n in range(1, 6)):
        if key not in tr or key not in it_by_key:
            continue
        loc_val = tr[key]
        if "{price}" in loc_val:
            loc_val = loc_val.format(price=now)
        it_val = it_by_key[key]
        if it_val in html:
            html = html.replace(it_val, loc_val)
        elif key == "faq2_a":
            html = re.sub(
                r"Alla consegna: [^<]+quando ritiri il pacco\.",
                loc_val,
                html,
                count=1,
            )
    return html


def apply_why_alts(html: str, tr: dict, it_by_key: dict) -> str:
    pairs = (
        ("desc-1.webp", "alt_w1"),
        ("desc-3.webp", "alt_w2"),
        ("desc-2.webp", "alt_w3"),
    )
    for fragment, key in pairs:
        if key not in tr or key not in it_by_key:
            continue
        it_alt = it_by_key[key]
        loc_alt = tr[key].replace("\\", "\\\\").replace('"', "&quot;")
        html = html.replace(f'alt="{it_alt}"', f'alt="{loc_alt}"', 1)
    if "alt_kit" in tr and "alt_kit" in it_by_key:
        html = html.replace(it_by_key["alt_kit"], tr["alt_kit"])
    return html


def render_landing(
    offer: str,
    cfg: dict,
    tr: dict,
    it_html: str,
    it_replace: dict[str, str],
    it_by_key: dict,
) -> str:
    geo = cfg["geo"]
    folder = offer_folder(offer)
    landing_url = public_landing_url(geo, offer)
    ty_url = public_thankyou_url(geo, offer)
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    now = fmt_price(cfg["price"], cfg["currency"])

    html = it_html
    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = html.replace(
        "https://gadgetshifthub.com/it/zelto-3990/",
        landing_url,
    )
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{landing_url}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]+"\s*/?>',
        f'<meta property="og:url" content="{landing_url}">',
        html,
        count=1,
    )

    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'zelto-3990'", f"PRODUCT_SLUG: '{folder}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html, count=1)
    html = html.replace(
        "OFFER_NAME: 'ZELTO IT #3990'",
        f"OFFER_NAME: 'ZELTO {offer}'",
    )
    html = html.replace("LP_ID: 'it-3990'", f"LP_ID: '{geo}-{offer}'")
    html = re.sub(r"FORM_OFFER:\s*'3990'", f"FORM_OFFER: '{offer}'", html)
    from zelto_network_forms import _offer_key

    lp, form_key = _offer_key(offer)
    html = re.sub(r"FORM_LP:\s*'[^']*'", f"FORM_LP: '{lp}'", html, count=1)
    html = re.sub(r"FORM_KEY:\s*'[^']*'", f"FORM_KEY: '{form_key}'", html, count=1)
    html = re.sub(
        r"THANKYOU_URL:\s*'[^']*'",
        f"THANKYOU_URL: '{ty_url}'",
        html,
        count=1,
    )
    html = re.sub(
        r'thankyoupage" type="hidden" value="[^"]+"',
        f'thankyoupage" type="hidden" value="{ty_url}"',
        html,
        count=1,
    )
    html = re.sub(
        r'<input name="offer" type="hidden" value="[^"]*"\s*/?>',
        f'<input name="offer" type="hidden" value="{offer}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="offer-id" content="[^"]*"\s*/?>',
        f'<meta name="offer-id" content="{offer}">',
        html,
        count=1,
    )
    html = re.sub(
        r"<!-- Offer #\d+ -->",
        f"<!-- Offer #{offer} -->",
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

    html = re.sub(r"<title>.*?</title>", f"<title>{tr['title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*"\s*/?>',
        f'<meta name="description" content="{tr["description"]}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*"\s*/?>',
        f'<meta property="og:title" content="{tr["og_title"]}">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*"\s*/?>',
        f'<meta property="og:description" content="{tr["og_description"]}">',
        html,
        count=1,
    )

    html = re.sub(r'<span class="was">[^<]*</span>', f'<span class="was">{was}</span>', html)
    html = re.sub(r'<span class="now">[^<]*</span>', f'<span class="now">{now}</span>', html)

    countdown_label_keys = {"hours", "mins", "secs"}
    form_field_keys = {
        "label_name",
        "label_tel",
        "label_addr",
        "ph_name",
        "ph_tel",
        "ph_addr",
        "form_note_hero",
        "form_note_form",
    }
    footer_ui_keys = {
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
    }
    for it_text, key in sorted(it_replace.items(), key=lambda x: -len(x[0])):
        if key in form_field_keys or key in footer_ui_keys or key not in tr:
            continue
        if key in countdown_label_keys:
            html = html.replace(
                f'<div class="lbl">{it_text}</div>',
                f'<div class="lbl">{tr[key]}</div>',
            )
            continue
        html = html.replace(it_text, tr[key])

    html = apply_price_remants(html, now, was)
    html = apply_cta_and_faq_price(html, tr, now, it_by_key)
    html = re.sub(
        r'(<p class="form-note form-note--hero">)[^<]+(</p>)',
        rf'\1{tr["form_note_hero"]}\2',
        html,
        count=1,
    )

    form_fields = (
        ("name", "label_name", "ph_name"),
        ("tel", "label_tel", "ph_tel"),
        ("street-address", "label_addr", "ph_addr"),
    )
    for field_id, label_key, ph_key in form_fields:
        if label_key in tr:
            html = re.sub(
                rf'(<label for="{field_id}">)[^<]+(</label>)',
                rf"\1{tr[label_key]}\2",
                html,
                count=1,
            )
        if ph_key in tr:
            html = re.sub(
                rf'(<input id="{field_id}"[^>]*placeholder=")[^"]*(")',
                rf"\1{tr[ph_key]}\2",
                html,
                count=1,
            )
    if "submit_btn" in tr:
        html = re.sub(
            r'(<button name="submit"[^>]*class="cta-btn">)[^<]+(</button>)',
            rf"\1{tr['submit_btn']}\2",
            html,
            count=1,
        )

    if geo == "lt":
        html = html.replace(
            'id="liveCount"',
            'id="liveCount" data-live-locale="lt"',
            1,
        )

    html = html.replace("/it/", f"/{geo}/")
    html = html.replace("zelto-3990", folder)

    forms = load_network_forms()
    if offer in forms:
        html = re.sub(
            r'<form class="tm-order-form.*?</form>',
            forms[offer],
            html,
            count=1,
            flags=re.DOTALL,
        )
        if "form_note_form" in tr:
            html = html.replace(
                "<!--ZELTO_FORM_NOTE-->",
                tr["form_note_form"],
            )

    if cfg["currency"] == "EUR":
        html = normalize_euro_spacing(html)

    html = apply_testimonial_alts(html, tr, it_by_key)
    html = apply_why_alts(html, tr, it_by_key)
    html = apply_footer(html, tr, geo)
    html = insert_ai_notice_in_site_footer(html, cfg["lang"])
    html = html.replace("shoptrendcrest", "gadgetshifthub")

    if OFFER_PATH_SYNC.strip() not in html:
        html = html.replace("</body>", OFFER_PATH_SYNC + "\n</body>", 1)

    return html


def render_thank_you(
    offer: str,
    cfg: dict,
    tr: dict,
    it_ty: str,
    it_by_key: dict,
) -> str:
    geo = cfg["geo"]
    folder = offer_folder(offer)
    ty_url = public_thankyou_url(geo, offer)
    now = fmt_price(cfg["price"], cfg["currency"])
    html = it_ty

    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'zelto-3990'", f"PRODUCT_SLUG: '{folder}'", html)
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{ty_url}">',
        html,
        count=1,
    )
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html, count=1)
    html = re.sub(
        r'<meta name="offer-id" content="[^"]*"\s*/?>',
        f'<meta name="offer-id" content="{offer}">',
        html,
        count=1,
    )
    html = re.sub(
        r"<!-- Offer #\d+ -->",
        f"<!-- Offer #{offer} -->",
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
        r'<meta name="description" content="[^"]*"\s*/?>',
        f'<meta name="description" content="{tr["ty_desc"]}">',
        html,
        count=1,
    )
    for key in (
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
    ):
        html = html.replace(it_by_key[key], tr[key])

    ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
    steps_html = "\n".join(f"<li>{s}</li>" for s in ty_steps)
    html = re.sub(
        r'<ol class="ty-steps-list">.*?</ol>',
        f'<ol class="ty-steps-list">\n{steps_html}\n</ol>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    it_badges = it_by_key["ty_badges"]
    for ib, lb in zip(it_badges, tr["ty_badges"]):
        html = html.replace(ib, lb)

    was = fmt_price(list_was_price(cfg), cfg["currency"])
    html = apply_price_remants(html, now, was)
    html = html.replace(
        "https://gadgetshifthub.com/it/zelto-3990/thank-you.html",
        ty_url,
    )
    html = html.replace("/it/", f"/{geo}/")
    html = html.replace("zelto-3990", folder)

    html = re.sub(
        r"window\.trackPurchase\(\d+(?:\.\d+)?,\s*'EUR'\)",
        f"window.trackPurchase({cfg['price']}, '{cfg['currency']}')",
        html,
        count=1,
    )

    if cfg["currency"] == "EUR":
        html = normalize_euro_spacing(html)
    html = apply_footer(html, tr, geo)
    html = html.replace("shoptrendcrest", "gadgetshifthub")
    return html


def main(only: set[str] | None = None) -> None:
    tr_all = load_translations()
    it_by_key = load_it_by_key()
    it_replace = build_it_replace_map(it_by_key)
    it_landing = IT_LANDING.read_text(encoding="utf-8")
    it_ty = IT_THANKYOU.read_text(encoding="utf-8")

    urls: list[str] = []
    for offer, cfg in GEOS.items():
        if only is not None and offer not in only:
            continue
        tr = tr_all[cfg["tr"]]
        geo = cfg["geo"]
        folder = offer_folder(offer)
        lp_url = public_landing_url(geo, offer)
        ty_url = public_thankyou_url(geo, offer)

        if offer not in SKIP_OVERWRITE_OFFERS:
            out_dir = ROOT / geo / folder
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "index.html").write_text(
                render_landing(offer, cfg, tr, it_landing, it_replace, it_by_key),
                encoding="utf-8",
            )
            ty_dir = out_dir / "thank-you"
            ty_dir.mkdir(parents=True, exist_ok=True)
            (ty_dir / "index.html").write_text(
                render_thank_you(offer, cfg, tr, it_ty, it_by_key),
                encoding="utf-8",
            )
            print(
                f"Wrote {geo}/{folder}/ (#{offer}) — "
                f"now={cfg['price']} {cfg['currency']} was={list_was_price(cfg)}"
            )
        else:
            print(f"Skipped overwrite {geo}/{folder}/ (#{offer})")

        urls.extend([lp_url, ty_url])

    print("\n--- Summary URLs ---")
    for url in urls:
        print(url)


if __name__ == "__main__":
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
