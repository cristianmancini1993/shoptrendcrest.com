#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate FORVEX™ cordless chainsaw landings + thank-you pages for campaign geos."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from _forvex_es_overlay import TY_OVERLAY  # noqa: E402

ES_PRICE_NOW = "69 €"
ES_PRICE_WAS = "138 €"
ES_CTA_LITERAL = "PEDIR FORVEX™ AHORA →"
ES_FAQ2_A = "No: {price} en efectivo al mensajero cuando recibes FORVEX™."


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "forvex_network_forms",
        Path(__file__).with_name("forvex_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


def load_es_by_key() -> dict:
    import ast

    text = (Path(__file__).with_name("_forvex_es_strings.py")).read_text(encoding="utf-8")
    start = text.index("ES_STRINGS")
    start = text.index("{", start)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return ast.literal_eval(text[start : i + 1])
    raise ValueError("ES_STRINGS not found")


def build_es_replace_map(es_by_key: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    skip = {"cta"}
    for key, val in es_by_key.items():
        if isinstance(val, str) and key not in skip:
            out[val] = key
    return out


GEOS = {
    "752": {
        "geo": "lt",
        "lang": "lt",
        "tr": "lt",
        "price": 89.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 18.0,
    },
    "1013": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "price": 69.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 17.0,
    },
    "1014": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "price": 79.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 17.0,
    },
    "1429": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 349.00,
        "currency": "PLN",
        "slug": "forvex",
        "cpa": 21.0,
        "form_blocked": True,
    },
    "1797": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "price": 329.00,
        "currency": "PLN",
        "slug": "forvex",
        "cpa": 21.0,
    },
    "1945": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cs",
        "price": 1799.00,
        "currency": "CZK",
        "slug": "forvex",
        "cpa": 18.0,
    },
    "3225": {
        "geo": "ro",
        "lang": "ro",
        "tr": "ro",
        "price": 397.00,
        "currency": "RON",
        "slug": "forvex",
        "cpa": 16.0,
    },
    "3228": {
        "geo": "sk",
        "lang": "sk",
        "tr": "sk",
        "price": 79.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 16.0,
    },
    "3229": {
        "geo": "si",
        "lang": "sl",
        "tr": "si",
        "price": 79.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 16.0,
    },
    "3230": {
        "geo": "hr",
        "lang": "hr",
        "tr": "hr",
        "price": 79.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 16.0,
    },
    "3232": {
        "geo": "hu",
        "lang": "hu",
        "tr": "hu",
        "price": 29999.00,
        "currency": "HUF",
        "slug": "forvex",
        "cpa": 16.0,
    },
    "3248": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "price": 89.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 20.0,
    },
    "3518": {
        "geo": "lv",
        "lang": "lv",
        "tr": "lv",
        "price": 79.00,
        "currency": "EUR",
        "slug": "forvex",
        "cpa": 18.0,
    },
}

LEGACY_REDIRECT_TMPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var target = '{target}';
  window.location.replace(target + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url={target}">
</head>
<body>
<p><a href="{target}">FORVEX™</a></p>
</body>
</html>
"""

OFFER_PATH_SYNC = """
<script>
(function () {
  var m = location.pathname.match(/\\/forvex-(\\d+)(?:\\/|$)/);
  if (!m) return;
  var id = m[1];
  document.querySelectorAll('input[name="offer"]').forEach(function (el) { el.value = id; });
  if (window.SITE_CONFIG) {
    window.SITE_CONFIG.OFFER_ID = id;
    window.SITE_CONFIG.OFFER_NAME = 'FORVEX ' + id;
  }
})();
</script>
"""


def offer_folder(offer: str) -> str:
    return f"forvex-{offer}"


def public_base_path(geo: str, offer: str) -> str:
    return f"/{geo}/{offer_folder(offer)}"


def public_landing_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/"


def public_thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/thank-you/"


def write_legacy_redirect(path: Path, lang: str, target_path: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        LEGACY_REDIRECT_TMPL.format(lang=lang, target=target_path),
        encoding="utf-8",
    )


def load_translations() -> dict:
    path = Path(__file__).with_name("_forvex_i18n.py")
    spec = importlib.util.spec_from_file_location("_forvex_i18n", path)
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
        return f"{whole_s},00 Kč"
    if currency == "PLN":
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s},{frac:02d} zł"
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
    html = html.replace(ES_PRICE_NOW, now)
    html = html.replace(ES_PRICE_WAS, was)
    return html


def patch_urgency_and_live(html: str, tr: dict, geo: str) -> str:
    if tr.get("countdown"):
        html = re.sub(
            r'<div class="countdown-label">[^<]*</div>',
            f'<div class="countdown-label">{tr["countdown"]}</div>',
            html,
            count=1,
        )
    for key in ("hours", "mins", "secs"):
        if key in tr and tr.get(key):
            es_lbl = {"hours": "Horas", "mins": "Min", "secs": "Seg"}[key]
            html = html.replace(
                f'<div class="lbl">{es_lbl}</div>',
                f'<div class="lbl">{tr[key]}</div>',
            )
    if tr.get("stock_l") and tr.get("stock_r"):
        html = re.sub(
            r'(<div class="stock-label">\s*)<span class="left">[^<]*</span>\s*'
            r'<span class="right">[^<]*</span>',
            f'\\1<span class="left">{tr["stock_l"]}</span>\n          '
            f'<span class="right">{tr["stock_r"]}</span>',
            html,
            count=1,
            flags=re.DOTALL,
        )
    if tr.get("live") and tr.get("live0"):
        live_attr = tr["live"].replace('"', "&quot;")
        locale_attr = ' data-live-locale="lt"' if geo == "lt" else ""
        html = re.sub(
            r'<span id="liveCount"[^>]*>.*?</span>',
            f'<span id="liveCount"{locale_attr} data-live="{live_attr}">'
            f'{tr["live0"]}</span>',
            html,
            count=1,
            flags=re.DOTALL,
        )
    if tr.get("rating"):
        html = re.sub(
            r'<div class="rating-text">.*?</div>',
            f'<div class="rating-text">{tr["rating"]}</div>',
            html,
            count=1,
            flags=re.DOTALL,
        )
    return html


def apply_cta_and_faq_price(html: str, tr: dict, now: str, es_by_key: dict) -> str:
    cta = tr["cta"] if "{price}" not in tr["cta"] else tr["cta"].format(price=now)
    html = html.replace(ES_CTA_LITERAL, cta)
    html = re.sub(
        r"PEDIR FORVEX™ AHORA →",
        cta,
        html,
    )
    for key in (f"faq{n}_a" for n in range(1, 12)):
        if key not in tr or key not in es_by_key:
            continue
        loc_val = tr[key]
        if "{price}" in loc_val:
            loc_val = loc_val.format(price=now)
        it_val = es_by_key[key]
        if it_val in html:
            html = html.replace(it_val, loc_val)
        elif key == "faq2_a":
            html = re.sub(
                r"No:\s[^<]*al mensajero cuando recibes FORVEX™\.",
                loc_val,
                html,
                count=1,
            )
    form_note = tr["form_note"].format(price=now) if "{price}" in tr["form_note"] else tr["form_note"]
    html = re.sub(
        r'<p class="form-note">[^<]*</p>',
        f'<p class="form-note">{form_note}</p>',
        html,
        count=1,
    )
    return html


def render_landing(
    offer: str,
    cfg: dict,
    tr: dict,
    es_html: str,
    es_replace: dict[str, str],
    es_by_key: dict,
) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    folder = offer_folder(offer)
    landing_url = public_landing_url(geo, offer)
    ty_url = public_thankyou_url(geo, offer)
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    now = fmt_price(cfg["price"], cfg["currency"])

    html = es_html
    html = html.replace('lang="es"', f'lang="{cfg["lang"]}"', 1)
    html = html.replace(
        "https://shoptrendcrest.com/es/forvex-1013/",
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

    html = re.sub(r"GEO:\s*'es'", f"GEO: '{geo}'", html)
    html = re.sub(
        r"PRODUCT_SLUG:\s*'forvex-\d+'",
        f"PRODUCT_SLUG: '{folder}'",
        html,
    )
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = html.replace("OFFER_NAME: 'FORVEX 1013'", f"OFFER_NAME: 'FORVEX {offer}'")
    html = html.replace("LP_ID: 'es-forvex-1013'", f"LP_ID: '{geo}-{folder}'")

    html = re.sub(
        r'thankyoupage" type="hidden" value="https://shoptrendcrest.com/es/forvex-1013/thank-you/"',
        f'thankyoupage" type="hidden" value="{ty_url}"',
        html,
    )
    html = re.sub(
        r'<input name="offer" type="hidden" value="[^"]*"\s*/?>',
        f'<input name="offer" type="hidden" value="{offer}" />',
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
    html = re.sub(
        r"<h2>Reserva FORVEX™ por [^<]+</h2>",
        f"<h2>{tr['form_h2_prefix']} {now}</h2>",
        html,
    )

    countdown_label_keys = {"hours", "mins", "secs"}
    form_field_keys = {
        "label_name",
        "label_tel",
        "label_addr",
        "ph_name",
        "ph_tel",
        "ph_addr",
        "submit_btn",
        "form_note",
    }
    for es_text, key in sorted(es_replace.items(), key=lambda x: -len(x[0])):
        if key in form_field_keys or key not in tr:
            continue
        if key in countdown_label_keys:
            html = html.replace(
                f'<div class="lbl">{es_text}</div>',
                f'<div class="lbl">{tr[key]}</div>',
            )
            continue
        if key in tr and isinstance(tr[key], str):
            html = html.replace(es_text, tr[key])

    html = apply_price_remants(html, now, was)
    html = apply_cta_and_faq_price(html, tr, now, es_by_key)
    html = patch_urgency_and_live(html, tr, geo)
    if tr.get("footer_blurb"):
        html = re.sub(
            r'<p class="site-footer__blurb">[^<]*</p>',
            f'<p class="site-footer__blurb">{tr["footer_blurb"]}</p>',
            html,
            count=1,
        )

    html = html.replace("/es/", f"/{geo}/")
    html = html.replace(f"https://shoptrendcrest.com/{geo}/{slug}/", landing_url)
    html = html.replace(f"/{geo}/{slug}/", f"{public_base_path(geo, offer)}/")

    forms = load_network_forms()
    if offer in forms:
        html = re.sub(
            r'<form class="tm-order-form.*?</form>',
            forms[offer],
            html,
            count=1,
            flags=re.DOTALL,
        )

    if cfg["currency"] == "EUR":
        html = normalize_euro_spacing(html)

    if "</body>" in html:
        html = html.replace("</body>", OFFER_PATH_SYNC + "\n</body>", 1)

    return html


def render_thank_you(
    offer: str,
    cfg: dict,
    tr: dict,
    es_ty: str,
    es_by_key: dict,
) -> str:
    geo = cfg["geo"]
    folder = offer_folder(offer)
    ty_url = public_thankyou_url(geo, offer)
    now = fmt_price(cfg["price"], cfg["currency"])
    html = es_ty

    html = html.replace('lang="es"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'es'", f"GEO: '{geo}'", html)
    html = re.sub(
        r"PRODUCT_SLUG:\s*'forvex-\d+'",
        f"PRODUCT_SLUG: '{folder}'",
        html,
    )
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{ty_url}">',
        html,
        count=1,
    )
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = re.sub(
        r"CONVERSION_CURRENCY:\s*'EUR'",
        f"CONVERSION_CURRENCY: '{cfg['currency']}'",
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
    html = html.replace(es_by_key["ty_h1"], tr["ty_h1"])
    html = html.replace(es_by_key["ty_sub"], tr["ty_sub"])
    html = html.replace(es_by_key["ty_alt"], tr["ty_alt"])
    html = html.replace(es_by_key["ty_eyebrow"], tr["ty_eyebrow"])
    html = html.replace(es_by_key["ty_action_title"], tr["ty_action_title"])
    html = html.replace(es_by_key["ty_action_body"], tr["ty_action_body"])
    html = html.replace(es_by_key["ty_action_warn"], tr["ty_action_warn"])
    html = html.replace(es_by_key["ty_hours_h"], tr["ty_hours_h"])
    html = html.replace(es_by_key["ty_hours"], tr["ty_hours"])
    html = html.replace(es_by_key["ty_next_h"], tr["ty_next_h"])

    ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
    steps_html = "\n".join(f"        <li>{s}</li>" for s in ty_steps)
    html = re.sub(
        r'<ol class="ty-steps-list">.*?</ol>',
        f"<ol class=\"ty-steps-list\">\n{steps_html}\n      </ol>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    es_badges = TY_OVERLAY["ty_badges"]
    for ib, lb in zip(es_badges, tr["ty_badges"]):
        html = html.replace(ib, lb)

    footer_it = (
        "    <div>\n"
        '      <h4 class="site-footer__heading">Información</h4>\n'
        '      <ul class="site-footer__list">\n'
        '        <li><a href="/es/about-us.html">Quiénes somos</a></li>\n'
        '        <li><a href="/es/contact-us.html">Contacto</a></li>\n'
        '        <li><a href="/es/privacy-policy.html">Política de privacidad</a></li>\n'
        '        <li><a href="/es/terms-conditions.html">Términos y condiciones</a></li>\n'
        '        <li><a href="/es/cookie-policy.html">Política de cookies</a></li>\n'
        '        <li><a href="/es/shipping-policy.html">Política de envío</a></li>\n'
        '        <li><a href="/es/refund-policy.html">Política de devolución</a></li>\n'
        "      </ul>\n"
        "    </div>\n"
        "    <div>\n"
        '      <h4 class="site-footer__heading">Contacto</h4>'
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
    html = html.replace(
        es_by_key["footer_blurb"],
        tr["footer_blurb"],
    )
    html = html.replace(
        f"{es_by_key['rights']}.",
        tr["rights"] + ".",
    )
    html = html.replace("/es/", f"/{geo}/")
    html = html.replace(
        "https://shoptrendcrest.com/es/forvex-1013/thank-you/",
        ty_url,
    )
    html = html.replace(f"/{cfg['slug']}/", f"/{folder}/")

    html = re.sub(r"'value':\s*[0-9.]+", f"'value': {cfg['cpa']}", html)
    html = re.sub(
        r"CONVERSION_VALUE:\s*[0-9.]+",
        f"CONVERSION_VALUE: {cfg['cpa']}",
        html,
    )
    if cfg["currency"] == "EUR":
        html = normalize_euro_spacing(html)
    return html


def main(only: set[str] | None = None) -> None:
    tr_all = load_translations()
    es_by_key = load_es_by_key()
    es_replace = build_es_replace_map(es_by_key)
    tpl_dir = Path(__file__).with_name("templates")
    es_landing = (tpl_dir / "forvex_es_landing.html").read_text(encoding="utf-8")
    es_ty = (tpl_dir / "forvex_es_thank_you.html").read_text(encoding="utf-8")
    forms = load_network_forms()

    urls: list[str] = []
    skipped: list[str] = []
    for offer, cfg in GEOS.items():
        if only is not None and offer not in only:
            continue
        if offer not in forms and not cfg.get("form_blocked"):
            skipped.append(offer)
            continue
        tr = tr_all[cfg["tr"]]
        geo = cfg["geo"]
        slug = cfg["slug"]
        folder = offer_folder(offer)
        lang = cfg["lang"]
        lp_path = f"{public_base_path(geo, offer)}/"
        ty_path = f"{public_base_path(geo, offer)}/thank-you/"

        out_dir = ROOT / geo / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            render_landing(offer, cfg, tr, es_landing, es_replace, es_by_key),
            encoding="utf-8",
        )
        ty_dir = out_dir / "thank-you"
        ty_dir.mkdir(parents=True, exist_ok=True)
        (ty_dir / "index.html").write_text(
            render_thank_you(offer, cfg, tr, es_ty, es_by_key),
            encoding="utf-8",
        )

        legacy = ROOT / geo / slug
        write_legacy_redirect(legacy / "index.html", lang, lp_path)
        write_legacy_redirect(legacy / "landing.html", lang, lp_path)
        write_legacy_redirect(legacy / "thank-you.html", lang, ty_path)

        write_legacy_redirect(ROOT / offer / "index.html", lang, lp_path)
        write_legacy_redirect(ROOT / offer / "t.html", lang, ty_path)

        lp_url = public_landing_url(geo, offer)
        ty_url = public_thankyou_url(geo, offer)
        urls.extend([lp_url, ty_url])
        print(
            f"Wrote {geo}/{folder}/ (#{offer}) - "
            f"now={cfg['price']} {cfg['currency']} was={list_was_price(cfg)}"
        )

    if skipped:
        print("\nSkipped (missing form settings):", ", ".join(skipped))

    print("\n--- Summary URLs ---")
    for url in urls:
        print(url)


if __name__ == "__main__":
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
