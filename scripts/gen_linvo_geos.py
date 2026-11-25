#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate LINVO™ localized landings from it/linvo/ templates."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF_NOW = 89.0
REF_WAS = 178.0
DISCOUNT = 50

OFFERS: dict[str, dict] = {
    "1912": {"geo": "de", "lang": "de", "price": 92.0, "currency": "EUR"},
    "1915": {"geo": "hu", "lang": "hu", "price": 29999.0, "currency": "HUF"},
    "2480": {"geo": "pt", "lang": "pt", "price": 79.0, "currency": "EUR"},
    "3163": {"geo": "es", "lang": "es", "price": 79.0, "currency": "EUR"},
    "3167": {"geo": "pl", "lang": "pl", "price": 339.0, "currency": "PLN"},
    "3169": {"geo": "cz", "lang": "cs", "price": 1899.0, "currency": "CZK"},
    "3910": {"geo": "lv", "lang": "lv", "price": 85.0, "currency": "EUR"},
    "4321": {"geo": "sk", "lang": "sk", "price": 74.0, "currency": "EUR"},
    "1897": {"geo": "it", "lang": "it", "price": 79.99, "currency": "EUR"},
}

LANG_MAP = {
    "de": "de",
    "hu": "hu",
    "pt": "pt",
    "es": "es",
    "pl": "pl",
    "cz": "cs",
    "lv": "lv",
    "sk": "sk",
    "it": "it",
}

SKIP_REPLACE_KEYS = frozenset({
    "label_name",
    "label_tel",
    "label_addr",
    "ph_name",
    "ph_tel",
    "ph_addr",
    "err_name",
    "err_tel",
    "err_addr",
    "submit_btn",
    "author1_name",
    "author1_city",
    "author1_suffix",
    "author2_name",
    "author2_city",
    "author2_suffix",
    "author3_name",
    "author3_city",
    "author3_suffix",
})


def load_it_ref_strings() -> dict:
    """Italian literals still present in it/linvo/ templates (search side of i18n replace)."""
    spec = importlib.util.spec_from_file_location(
        "_linvo_it_ref_strings",
        Path(__file__).with_name("_linvo_it_ref_strings.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.IT_REF_STRINGS


def load_translations() -> dict[str, dict]:
    loc_dir = ROOT / "content/linvo/locales"
    out: dict[str, dict] = {"it": json.loads((loc_dir / "it.json").read_text(encoding="utf-8"))}
    for path in sorted(loc_dir.glob("*.json")):
        if path.stem == "it":
            continue
        out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return out


def fmt_price(amount: float, currency: str) -> str:
    wholeish = abs(amount - round(amount)) < 0.001
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Ft"
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Kč"
    if currency == "PLN":
        if wholeish:
            return f"{int(round(amount))} zł"
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        return f"{whole},{frac:02d} zł"
    if wholeish:
        return f"{int(round(amount))} €"
    return f"{amount:.2f}".replace(".", ",") + " €"


def was_price(now: float) -> float:
    return round(now * (100 / (100 - DISCOUNT)), 2)


def fmt_ctx(now: float, currency: str) -> dict[str, str]:
    was = was_price(now)
    now_s = fmt_price(now, currency)
    was_s = fmt_price(was, currency)
    save_s = fmt_price(was - now, currency)
    return {"price_now": now_s, "price_was": was_s, "save_amount": save_s}


def fill_template(s: str, ctx: dict[str, str]) -> str:
    if "{" not in s:
        return s
    try:
        return s.format(**ctx)
    except KeyError:
        return s


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def normalize_euro_spacing(html: str) -> str:
    return re.sub(r"(?<=\d)€", " €", html)


def build_it_replace_map(it_by_key: dict, ref_ctx: dict[str, str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, val in it_by_key.items():
        if isinstance(val, str) and key not in SKIP_REPLACE_KEYS:
            lit = fill_template(val, ref_ctx)
            if len(lit) > 2:
                out[lit] = key
    return out


def author_line(tr: dict, n: int) -> str:
    return f"{tr[f'author{n}_name']} — {tr[f'author{n}_city']}, {tr[f'author{n}_suffix']}"


def hero_price_parts(amount: float, currency: str) -> tuple[str, str]:
    """Split formatted price for bf-pn + <small> (full number, currency label)."""
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " "), "Ft"
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " "), "Kč"
    if currency == "PLN":
        if abs(amount - round(amount)) < 0.001:
            return str(int(round(amount))), "zł"
        whole = int(amount)
        frac = int(round((amount - whole) * 100))
        return f"{whole},{frac:02d}", "zł"
    if abs(amount - round(amount)) < 0.001:
        return str(int(round(amount))), "€"
    return f"{amount:.2f}".replace(".", ","), "€"


def patch_price_nodes(html: str, now: float, currency: str) -> str:
    was = was_price(now)
    now_s = fmt_price(now, currency)
    was_s = fmt_price(was, currency)
    save_s = fmt_price(now * 0 + (was - now), currency)

    now_num, curr_suffix = hero_price_parts(now, currency)
    html = re.sub(
        r'<span class="bf-p-new"><span class="bf-pn">[^<]*</span><small>[^<]*</small>',
        f'<span class="bf-p-new"><span class="bf-pn">{now_num}</span><small>{curr_suffix}</small>',
        html,
        count=1,
    )
    html = re.sub(r'<span class="bf-p-old">[^<]*</span>', f'<span class="bf-p-old">{was_s}</span>', html)
    def _disc_repl(m: re.Match[str]) -> str:
        return (
            f'{m.group(1)}BLACK FRIDAY −{DISCOUNT}%'
            f"{m.group(2)}−{save_s}{m.group(3)}"
        )

    html = re.sub(
        r'(<p class="bf-disc"><span>)[^<]+(</span><span>)[^<]+(</span></p>)',
        _disc_repl,
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="bf-grand"><span>[^<]+</span><span>)[^<]+',
        lambda m: f"{m.group(1)}{now_s}",
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="bf-old"><span>[^<]+</span><span>)[^<]+',
        lambda m: f"{m.group(1)}{was_s}",
        html,
        count=1,
    )
    html = re.sub(
        r'<div class="bf-st-pr"><b>[^<]+</b>',
        f'<div class="bf-st-pr"><b>{now_s}</b>',
        html,
        count=1,
    )
    html = re.sub(
        r"<s>[^<]+</s>",
        f"<s>{was_s}</s>",
        html,
        count=1,
    )

    html = html.replace("89 €", now_s)
    html = html.replace("178 €", was_s)
    html = html.replace("−89 €", f"−{save_s}")
    html = html.replace("Risparmi <b class=\"bf-nw\">89 €</b>", f"Risparmi <b class=\"bf-nw\">{save_s}</b>")
    html = re.sub(r"trackPurchase\(89\.0", f"trackPurchase({now}", html)
    html = re.sub(r"PRICE: 89\b", f"PRICE: {now}", html)
    html = re.sub(r"PRICE: 89\.0", f"PRICE: {now}", html)
    if currency == "EUR":
        html = normalize_euro_spacing(html)
    return html


def apply_footer(html: str, tr: dict, geo: str) -> str:
    top = tr.get("footer_powered_top")
    if top:
        html = html.replace(
            "<p class=\"site-footer__top-meta\">shoptrendcrest.com — Offerto da CAPITALADV S.R.L.</p>",
            f'<p class="site-footer__top-meta">{top}</p>',
        )
    html = html.replace(
        "Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.",
        tr.get("footer_tagline", ""),
    )
    ai = tr.get("footer_ai_notice", "")
    if ai:
        html = re.sub(
            r'<p class="site-footer__ai-notice"[^>]*>.*?</p>',
            f'<p class="site-footer__ai-notice" data-ai-disclosure="1">{ai}</p>',
            html,
            count=1,
            flags=re.DOTALL,
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
        r'        <h4 class="site-footer__heading">Informazioni</h4>\s*'
        r'<ul class="site-footer__list">.*?</ul>',
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
    html = re.sub(
        r'<div class="site-footer__bottom">© <span data-year>\d+</span> [^<]+</div>',
        f'<div class="site-footer__bottom">© <span data-year>2026</span> {tr.get("footer_rights", "")}</div>',
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
    form_html: str,
) -> str:
    geo = cfg["geo"]
    lang = cfg["lang"]
    slug = f"linvo-{offer}"
    now = cfg["price"]
    currency = cfg["currency"]
    ctx = fmt_ctx(now, currency)
    ref_ctx = fmt_ctx(REF_NOW, "EUR")

    landing_url = f"https://shoptrendcrest.com/{geo}/{slug}/landing.html"
    ty_url = f"https://shoptrendcrest.com/{geo}/{slug}/thank-you.html"

    html = it_html
    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = html.replace("https://shoptrendcrest.com/it/linvo/landing.html", landing_url)
    html = html.replace("https://shoptrendcrest.com/it/linvo/thank-you.html", ty_url)
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
    html = re.sub(r"PRODUCT_SLUG:\s*'linvo'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{currency}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {now}", html)
    html = html.replace("OFFER_NAME: 'LINVO IT'", f"OFFER_NAME: 'LINVO {offer}'")
    html = html.replace("LP_ID: 'it-linvo'", f"LP_ID: '{geo}-{slug}'")
    html = html.replace("DEFAULT_OFFER_ID: 'linvo'", f"DEFAULT_OFFER_ID: '{offer}'")

    html = re.sub(r"\s*ORDER_DISABLED:\s*true,?\n", "\n", html)
    html = re.sub(r"\s*FORM_ENDPOINT:[^\n]+\n", "", html)

    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        (
            f"COOKIE_TEXT: '{esc_js(fill_template(tr['cookie_text'], ctx))}',\n"
            f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
            f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}'"
        ),
        html,
        count=1,
    )
    html = re.sub(
        r"FORM_ERROR_LABEL:\s*'[^']*'",
        f"FORM_ERROR_LABEL: '{esc_js(tr.get('form_error_label', ''))}'",
        html,
        count=1,
    )
    html = re.sub(
        r"SUBMITTING_LABEL:\s*'[^']*'",
        f"SUBMITTING_LABEL: '{esc_js(tr.get('submitting', ''))}'",
        html,
        count=1,
    )

    kit_keys = {f"kit_li{n}" for n in range(1, 7)}
    for n in range(6, 0, -1):
        key = f"kit_li{n}"
        it_val = it_by_key.get(key)
        if key not in tr or not isinstance(it_val, str):
            continue
        it_text = fill_template(it_val, ref_ctx)
        loc = fill_template(tr[key], ctx)
        if it_text in html:
            html = html.replace(it_text, loc, 1)

    for it_text, key in sorted(it_replace.items(), key=lambda x: -len(x[0])):
        if key in kit_keys or key not in tr:
            continue
        loc = fill_template(tr[key], ctx) if isinstance(tr[key], str) else tr[key]
        if isinstance(loc, str) and it_text in html:
            html = html.replace(it_text, loc)

    for n in (1, 2, 3):
        if not isinstance(it_by_key.get(f"author{n}_name"), str):
            continue
        it_auth = (
            f"{it_by_key[f'author{n}_name']} — "
            f"{it_by_key[f'author{n}_city']}, {it_by_key[f'author{n}_suffix']}"
        )
        html = html.replace(it_auth, author_line(tr, n))

    if manual := it_by_key.get("manual_in_box"):
        if isinstance(manual, str):
            html = html.replace(manual, tr.get("manual_in_box", manual))

    html = patch_price_nodes(html, now, currency)

    html = re.sub(
        r'<form class="tm-order-form.*?</form>',
        form_html.strip(),
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace("/it/about-us.html", f"/{geo}/about-us.html")
    html = html.replace("/it/contact-us.html", f"/{geo}/contact-us.html")
    html = html.replace("/it/privacy-policy.html", f"/{geo}/privacy-policy.html")
    html = html.replace("/it/terms-conditions.html", f"/{geo}/terms-conditions.html")
    html = html.replace("/it/cookie-policy.html", f"/{geo}/cookie-policy.html")
    html = html.replace("/it/shipping-policy.html", f"/{geo}/shipping-policy.html")
    html = html.replace("/it/refund-policy.html", f"/{geo}/refund-policy.html")

    html = apply_footer(html, tr, geo)
    return html


def render_thank_you(offer: str, cfg: dict, tr: dict, it_ty: str, it_by_key: dict, ref_ctx: dict) -> str:
    geo = cfg["geo"]
    lang = cfg["lang"]
    slug = f"linvo-{offer}"
    now = cfg["price"]
    currency = cfg["currency"]
    ctx = fmt_ctx(now, currency)
    ty_url = f"https://shoptrendcrest.com/{geo}/{slug}/thank-you.html"

    html = it_ty
    html = html.replace('lang="it"', f'lang="{lang}"', 1)
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{ty_url}">',
        html,
        count=1,
    )
    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'linvo'", f"PRODUCT_SLUG: '{slug}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{currency}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {now}", html)

    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        (
            f"COOKIE_TEXT: '{esc_js(fill_template(tr['cookie_text'], ctx))}',\n"
            f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
            f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}'"
        ),
        html,
        count=1,
    )

    for key in (
        "ty_title",
        "ty_desc",
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
        if key in it_by_key and key in tr and isinstance(it_by_key[key], str):
            it_val = fill_template(it_by_key[key], ref_ctx) if "{" in it_by_key[key] else it_by_key[key]
            loc_val = fill_template(tr[key], ctx) if isinstance(tr[key], str) and "{" in tr[key] else tr[key]
            html = html.replace(it_val, loc_val)

    ty_steps_it = it_by_key.get("ty_steps", [])
    ty_steps = tr.get("ty_steps", ty_steps_it)
    steps_html = "\n".join(f"<li>{fill_template(s, ctx) if '{' in s else s}</li>" for s in ty_steps)
    html = re.sub(
        r'<ol class="ty-steps-list">.*?</ol>',
        f'<ol class="ty-steps-list">\n{steps_html}\n      </ol>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    badges = tr.get("ty_badges", it_by_key.get("ty_badges", ()))
    badges_html = "\n".join(f'    <span class="ty-trust__badge">{b}</span>' for b in badges)
    html = re.sub(
        r'<div class="ty-trust">\s*.*?\s*</div>',
        f'<div class="ty-trust">\n{badges_html}\n  </div>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = patch_price_nodes(html, now, currency)
    html = html.replace("https://shoptrendcrest.com/it/linvo/thank-you.html", ty_url)
    html = html.replace("/it/about-us.html", f"/{geo}/about-us.html")
    html = apply_footer(html, tr, geo)
    return html


def write_index(geo: str, lang: str, slug: str) -> str:
    lp = f"/{geo}/{slug}/landing.html"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '{lp}';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url={lp}">
<link rel="canonical" href="https://shoptrendcrest.com{lp}">
</head>
<body>
<p><a href="{lp}">LINVO™</a></p>
</body>
</html>
"""


def main() -> int:
    from linvo_network_forms import build_forms

    it_landing = (ROOT / "it/linvo/landing.html").read_text(encoding="utf-8")
    it_ty = (ROOT / "it/linvo/thank-you.html").read_text(encoding="utf-8")
    it_by_key = load_it_ref_strings()
    ref_ctx = fmt_ctx(REF_NOW, "EUR")
    it_replace = build_it_replace_map(dict(it_by_key), ref_ctx)

    try:
        tr_all = load_translations()
    except FileNotFoundError as exc:
        print(f"Missing locales — run seed_linvo_locales.py first: {exc}", file=sys.stderr)
        return 1

    paths: list[str] = []
    for offer, cfg in OFFERS.items():
        lang_key = LANG_MAP.get(cfg["geo"], cfg["lang"])
        tr = tr_all.get(lang_key, tr_all.get(cfg["lang"], {}))
        ctx_tr = {**tr, **{k: fill_template(v, fmt_ctx(cfg["price"], cfg["currency"])) if isinstance(v, str) else v for k, v in tr.items()}}
        forms = build_forms({offer: ctx_tr})
        geo = cfg["geo"]
        slug = f"linvo-{offer}"
        out_dir = ROOT / geo / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        landing = render_landing(offer, cfg, tr, it_landing, it_replace, it_by_key, forms[offer])
        ty = render_thank_you(offer, cfg, tr, it_ty, it_by_key, ref_ctx)

        (out_dir / "landing.html").write_text(landing, encoding="utf-8")
        (out_dir / "thank-you.html").write_text(ty, encoding="utf-8")
        (out_dir / "index.html").write_text(write_index(geo, cfg["lang"], slug), encoding="utf-8")
        ty_sub = out_dir / "thank-you" / "index.html"
        ty_sub.parent.mkdir(parents=True, exist_ok=True)
        ty_sub.write_text(ty, encoding="utf-8")

        paths.extend([
            str(out_dir / "landing.html"),
            str(out_dir / "thank-you.html"),
            str(out_dir / "index.html"),
            str(ty_sub),
        ])
        print(f"OK {geo}/{slug}/ #{offer} now={cfg['price']} {cfg['currency']}")

    print("\n--- Output paths ---")
    for p in paths:
        print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())