#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Calvor™ campaign landings + thank-you pages for 13 GEO (from it/calvor/)."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from calvor_campaign_prices import (  # noqa: E402
    GEOS,
    IT_PRICE_NOW,
    IT_PRICE_WAS,
    fmt_price,
    list_was_price,
    offer_folder as calvor_offer_folder,
)

IT_CTA_LITERAL = "ORDINA Calvor™ →"
IT_FAQ2_A = "Alla consegna: 69 € in contanti al corriere quando ritiri il pacco."


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "calvor_network_forms",
        Path(__file__).with_name("calvor_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


def load_it_by_key() -> dict:
    spec = importlib.util.spec_from_file_location(
        "_calvor_it_strings",
        Path(__file__).with_name("_calvor_it_strings.py"),
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
<p><a href="{target}">Calvor™</a></p>
</body>
</html>
"""

OFFER_PATH_SYNC = """
<script>
(function () {
  var m = location.pathname.match(/\\/(?:warmio|calvor)-(\\d+)(?:\\/|$)/);
  if (!m) return;
  var id = m[1];
  document.querySelectorAll('input[name="offer"]').forEach(function (el) { el.value = id; });
  if (window.SITE_CONFIG) {
    window.SITE_CONFIG.OFFER_ID = id;
    window.SITE_CONFIG.OFFER_NAME = 'Calvor ' + id;
  }
})();
</script>
"""


def offer_folder(offer: str) -> str:
    return calvor_offer_folder(offer)


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
    path = Path(__file__).with_name("_calvor_i18n.py")
    spec = importlib.util.spec_from_file_location("_calvor_i18n", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return dict(mod.TRANSLATIONS)


def normalize_euro_spacing(html: str) -> str:
    from calvor_campaign_prices import NBSP

    html = re.sub(r"(?<=\d)€", f"{NBSP}€", html)
    html = re.sub(r"(?<=\d)\s+€", f"{NBSP}€", html)
    return html


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def apply_price_remants(html: str, now: str, was: str) -> str:
    from calvor_campaign_prices import NBSP

    html = html.replace(IT_PRICE_NOW, now)
    html = html.replace(IT_PRICE_WAS, was)
    for legacy_now, legacy_was in (
        ("69€", "138€"),
        ("69 €", "138 €"),
        (f"69{NBSP}€", f"138{NBSP}€"),
    ):
        html = html.replace(legacy_was, was)
        html = html.replace(legacy_now, now)
    return html


def apply_testimonial_alts(html: str, tr: dict) -> str:
    """Bind each review photo to alt_t1..alt_t3 by filename (stable if copy order changes)."""
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
    return html


FOOTER_IT_TOP = "shoptrendcrest.com — Offerto da CAPITALADV S.R.L."
FOOTER_IT_BLURB = (
    "Prodotti selezionati per casa, giardino e vita quotidiana. "
    "Pagamento alla consegna in 18 paesi europei."
)


def apply_footer(html: str, tr: dict, geo: str, lang: str | None = None) -> str:
    tagline = tr.get("footer_tagline") or tr.get("footer_blurb", "")
    html = html.replace(
        "Curated products for home, garden, and everyday life. Cash on delivery across 18 European countries.",
        tagline,
    )
    html = html.replace(FOOTER_IT_BLURB, tagline)
    html = html.replace(
        f'<p class="site-footer__blurb">{FOOTER_IT_BLURB}</p>',
        f'<p class="site-footer__blurb">{tagline}</p>',
        1,
    )
    html = html.replace(
        f'<p style="margin-top:1rem;max-width:340px">{FOOTER_IT_BLURB}</p>',
        f'<p style="margin-top:1rem;max-width:340px">{tagline}</p>',
        1,
    )
    loc_info = (
        f'        <h4 class="site-footer__heading">{tr["info"]}</h4>\n'
        f'        <ul class="site-footer__list">\n'
        f'          <li><a href="/{geo}/about-us.html">{tr["about"]}</a></li>\n'
        f'          <li><a href="/{geo}/contact-us.html">{tr["contact"]}</a></li>\n'
        f'          <li><a href="/{geo}/privacy-policy.html">{tr["privacy"]}</a></li>\n'
        f'          <li><a href="/{geo}/terms-conditions.html">{tr["terms"]}</a></li>\n'
        f'          <li><a href="/{geo}/cookie-policy.html">{tr["cookie"]}</a></li>\n'
        f'          <li><a href="/{geo}/shipping-policy.html">{tr["ship"]}</a></li>\n'
        f'          <li><a href="/{geo}/refund-policy.html">{tr["refund"]}</a></li>\n'
        f"        </ul>"
    )
    html = re.sub(
        r"        <h4 class=\"site-footer__heading\">[^<]+</h4>\s*"
        r"<ul class=\"site-footer__list\">\s*"
        r"(?:\s*<li><a href=\"[^\"]*(?:about-us|privacy-policy)[^\"]*\">.*?</li>\s*)+"
        r"</ul>",
        loc_info,
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<h4 class="site-footer__heading">)[^<]+(</h4>\s*<ul class="site-footer__list"><li><a href="mailto:)',
        rf'\1{tr["contacts"]}\2',
        html,
        count=1,
    )
    powered_top = tr.get(
        "footer_powered_top",
        FOOTER_IT_TOP,
    )
    html = html.replace(FOOTER_IT_TOP, powered_top)
    html = html.replace(
        "shoptrendcrest.com — Powered by WHATECH MOBILE CO., LIMITED</p>",
        f"{powered_top}</p>",
        1,
    )
    powered_bottom = tr.get(
        "footer_powered_bottom",
        f"{FOOTER_IT_TOP}. {tr.get('rights', 'Tutti i diritti riservati')}.",
    )
    html = re.sub(
        r'<div class="site-footer__bottom">© <span data-year>\d+</span> [^<]+</div>',
        f'<div class="site-footer__bottom">© <span data-year>2026</span> {powered_bottom}</div>',
        html,
        count=1,
    )
    locale = lang or geo
    try:
        from foot_ai_media import patch_footer_ai_notice
    except ImportError:
        from scripts.foot_ai_media import patch_footer_ai_notice  # type: ignore
    html = patch_footer_ai_notice(html, locale)
    return html


def apply_cta_and_faq_price(html: str, tr: dict, now: str, it_by_key: dict) -> str:
    cta = tr.get("cta_inline", tr.get("cta", IT_CTA_LITERAL))
    if "{price}" in cta:
        cta = cta.format(price=now)
    html = html.replace(IT_CTA_LITERAL, cta)
    html = html.replace("ORDINA Calvor™ →", cta)
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
                r"Alla consegna: [^<]+quando ricevi il pacco\.",
                loc_val,
                html,
                count=1,
            )
    html = re.sub(
        r"SUBMITTING_LABEL:\s*'[^']*'",
        f"SUBMITTING_LABEL: '{esc_js(tr['submitting'])}'",
        html,
        count=1,
    )
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
    slug = cfg["slug"]
    folder = offer_folder(offer)
    landing_url = public_landing_url(geo, offer)
    ty_url = public_thankyou_url(geo, offer)
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    now = fmt_price(cfg["price"], cfg["currency"])

    html = it_html
    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = html.replace(
        "https://shoptrendcrest.com/it/calvor/",
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
    html = re.sub(r"PRODUCT_SLUG:\s*'calvor'", f"PRODUCT_SLUG: '{folder}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = html.replace("OFFER_NAME: 'Calvor IT'", f"OFFER_NAME: 'Calvor {offer}'")
    html = re.sub(r"OFFER_ID:\s*'[^']*'", f"OFFER_ID: '{offer}'", html, count=0)
    html = html.replace("LP_ID: 'it-calvor'", f"LP_ID: '{geo}-{folder}'")

    html = re.sub(
        r'thankyoupage" type="hidden" value="[^"]+"',
        f'thankyoupage" type="hidden" value="{ty_url}"',
        html,
        count=1,
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
        r"<h2>Prenota Calvor™ ora, prima che finisca la promozione</h2>",
        f"<h2>{tr['form_h2']}</h2>",
        html,
        count=1,
    )

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
        val = tr[key]
        if isinstance(val, str) and "{price}" in val:
            val = val.format(price=now)
        html = html.replace(it_text, val)

    html = apply_price_remants(html, now, was)
    for key in (
        "f1_h",
        "f1_p",
        "f2_h",
        "f2_p",
        "f3_h",
        "f3_p",
        "f4_h",
        "f4_p",
    ):
        if key in tr and key in it_by_key and it_by_key[key] in html:
            html = html.replace(it_by_key[key], tr[key])
    if geo != "it":
        f4_fmt = tr.get("f4_p", "")
        if "{price}" in f4_fmt:
            html = re.sub(
                r"(<div class=\"feature-item\"><div class=\"ico\">💵</div><h4>)[^<]+(</h4><p>)[^<]+(</p></div>)",
                rf"\1{tr.get('f4_h', 'Contrassegno')}\2{f4_fmt.format(price=now)}\3",
                html,
                count=1,
            )
    html = apply_cta_and_faq_price(html, tr, now, it_by_key)
    html = re.sub(
        r'(<p class="form-note form-note--hero">)[^<]+(</p>)',
        rf'\1{tr["form_note_hero"]}\2',
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="form-note form-note--form">)[^<]+(</p>)',
        rf'\1{tr["form_note_form"]}\2',
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

    for i in range(1, 7):
        key = f"kit_li{i}"
        if key in tr and key in it_by_key and it_by_key[key] in html:
            html = html.replace(f"<li>{it_by_key[key]}</li>", f"<li>{tr[key]}</li>")
    for n in range(1, 4):
        for part in ("h", "p"):
            key = f"rev{n}_{part}"
            if key in tr and key in it_by_key and it_by_key[key] in html:
                html = html.replace(it_by_key[key], tr[key])
        auth = f"author{n}"
        if auth in tr and auth in it_by_key and it_by_key[auth] in html:
            html = html.replace(it_by_key[auth], tr[auth])
    for n in range(1, 6):
        for part in ("q", "a"):
            key = f"faq{n}_{part}"
            if key not in tr or key not in it_by_key:
                continue
            it_val = it_by_key[key]
            loc_val = tr[key]
            if "{price}" in loc_val:
                loc_val = loc_val.format(price=now)
            if part == "q" and it_val in html:
                html = html.replace(f"<span>{it_val}</span>", f"<span>{loc_val}</span>", 1)
            elif part == "a" and it_val in html:
                html = html.replace(f"<p>{it_val}</p>", f"<p>{loc_val}</p>", 1)

    if geo == "lt":
        html = html.replace(
            'id="liveCount"',
            'id="liveCount" data-live-locale="lt"',
            1,
        )

    html = html.replace("/it/", f"/{geo}/")
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

    html = apply_testimonial_alts(html, tr)
    html = apply_footer(html, tr, geo, cfg["lang"])

    if "</body>" in html:
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
    html = re.sub(r"PRODUCT_SLUG:\s*'calvor'", f"PRODUCT_SLUG: '{folder}'", html)
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
    html = html.replace(it_by_key["ty_h1"], tr["ty_h1"])
    html = html.replace(it_by_key["ty_sub"], tr["ty_sub"])
    html = html.replace(it_by_key["ty_alt"], tr["ty_alt"])
    html = html.replace(it_by_key["ty_eyebrow"], tr["ty_eyebrow"])
    html = html.replace(it_by_key["ty_action_title"], tr["ty_action_title"])
    html = html.replace(it_by_key["ty_action_body"], tr["ty_action_body"])
    html = html.replace(it_by_key["ty_action_warn"], tr["ty_action_warn"])
    html = html.replace(it_by_key["ty_hours_h"], tr["ty_hours_h"])
    html = html.replace(it_by_key["ty_hours"], tr["ty_hours"])
    html = html.replace(it_by_key["ty_next_h"], tr["ty_next_h"])

    ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
    steps_html = "\n".join(f"        <li>{s}</li>" for s in ty_steps)
    html = re.sub(
        r'<ol class="ty-steps-list">.*?</ol>',
        f"<ol class=\"ty-steps-list\">\n{steps_html}\n      </ol>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    it_badges = it_by_key["ty_badges"]
    for ib, lb in zip(it_badges, tr["ty_badges"]):
        html = html.replace(ib, lb)

    html = html.replace(it_by_key["ty_order_header"], tr["ty_order_header"])
    html = html.replace(it_by_key["ty_product"], tr["ty_product"])
    html = re.sub(
        r'<div class="ty-summary-pay">[^<]+</div>',
        f'<div class="ty-summary-pay">{tr["ty_pay"].format(price=now)}</div>',
        html,
        count=1,
    )
    was = fmt_price(list_was_price(cfg), cfg["currency"])
    html = apply_price_remants(html, now, was)
    html = html.replace(
        "https://shoptrendcrest.com/it/calvor/thank-you/",
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
    html = apply_footer(html, tr, geo, cfg["lang"])
    return html


def main(only: set[str] | None = None) -> None:
    tr_all = load_translations()
    it_by_key = load_it_by_key()
    it_replace = build_it_replace_map(it_by_key)
    it_landing = (ROOT / "it/calvor/index.html").read_text(encoding="utf-8")
    it_ty = (ROOT / "it/calvor/thank-you/index.html").read_text(encoding="utf-8")

    urls: list[str] = []
    for offer, cfg in GEOS.items():
        if offer == "3990":
            continue  # it/calvor-3990/ via build_it_calvor_3990.py
        if only is not None and offer not in only:
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
            render_landing(offer, cfg, tr, it_landing, it_replace, it_by_key),
            encoding="utf-8",
        )
        ty_dir = out_dir / "thank-you"
        ty_dir.mkdir(parents=True, exist_ok=True)
        (ty_dir / "index.html").write_text(
            render_thank_you(offer, cfg, tr, it_ty, it_by_key),
            encoding="utf-8",
        )

        legacy = ROOT / geo / slug
        write_legacy_redirect(legacy / "index.html", lang, lp_path)
        write_legacy_redirect(legacy / "landing.html", lang, lp_path)
        write_legacy_redirect(legacy / "thank-you.html", lang, ty_path)

        write_legacy_redirect(ROOT / offer / "index.html", lang, lp_path)
        write_legacy_redirect(ROOT / offer / "t.html", lang, ty_path)

        warmio_legacy = ROOT / geo / f"warmio-{offer}"
        write_legacy_redirect(warmio_legacy / "index.html", lang, lp_path)
        write_legacy_redirect(warmio_legacy / "thank-you/index.html", lang, ty_path)

        lp_url = public_landing_url(geo, offer)
        ty_url = public_thankyou_url(geo, offer)
        urls.extend([lp_url, ty_url])
        print(
            f"Wrote {geo}/{folder}/ (#{offer}) - "
            f"now={cfg['price']} {cfg['currency']} "
            f"was={list_was_price(cfg)} CPA/CPL={cfg['cpa']}"
        )

    print("\n--- Summary URLs ---")
    for url in urls:
        print(url)


if __name__ == "__main__":
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(only)
