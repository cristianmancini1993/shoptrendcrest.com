#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate CENDORA™ localized landings + thank-you for content/cendora/offers.json."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IT_PRICE_NOW = "74€"
IT_PRICE_WAS = "148€"
IT_CTA_LITERAL = "VOGLIO CENDORA™ →"
DISCOUNT = 50


def load_network_forms() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "cendora_network_forms",
        Path(__file__).with_name("cendora_network_forms.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FORMS


def load_it_by_key() -> dict:
    spec = importlib.util.spec_from_file_location(
        "_cendora_it_strings",
        Path(__file__).with_name("_cendora_it_strings.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.IT_STRINGS


def load_translations() -> dict[str, dict]:
    loc_dir = ROOT / "content/cendora/locales"
    it = load_it_by_key()
    out: dict[str, dict] = {"it": dict(it)}
    for path in sorted(loc_dir.glob("*.json")):
        stem = path.stem
        if stem == "it" or stem.startswith("_") or ".sync-conflict" in path.name:
            continue
        out[stem] = json.loads(path.read_text(encoding="utf-8"))
    expected = set(it)
    for code, data in out.items():
        keys = set(data)
        if keys != expected:
            missing = expected - keys
            extra = keys - expected
            raise AssertionError(
                f"locale {code}: missing {sorted(missing)[:8]} ({len(missing)}); "
                f"extra {sorted(extra)[:8]} ({len(extra)})"
            )
    return out


def build_it_replace_map(it_by_key: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    skip = {"cta", "cta_inline"}
    for key, val in it_by_key.items():
        if isinstance(val, str) and key not in skip:
            out[val] = key
    return out


def offer_folder(offer: str) -> str:
    return f"cendora-{offer}"


def public_base_path(geo: str, offer: str) -> str:
    return f"/{geo}/{offer_folder(offer)}"


def public_landing_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/"


def public_thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/thank-you/"


def was_price(now: float) -> float:
    return float(int(round(now * (100 / (100 - DISCOUNT)))))


def fmt_price(amount: float, currency: str) -> str:
    if currency == "CZK":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Kč"
    if currency == "PLN":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", " ")
        return f"{whole_s} zł"
    if currency == "HUF":
        whole = int(round(amount))
        return f"{whole:,}".replace(",", " ") + " Ft"
    if currency == "RON":
        whole = int(round(amount))
        whole_s = f"{whole:,}".replace(",", ".")
        return f"{whole_s} lei"
    if abs(amount - round(amount)) < 0.001:
        return f"{int(round(amount))} €"
    s = f"{amount:.2f}".replace(".", ",")
    return f"{s} €"


def normalize_euro_spacing(html: str) -> str:
    return re.sub(r"(?<=\d)€", " €", html)


def esc_js(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def apply_kit_list(html: str, tr: dict) -> str:
    items = "".join(f"        <li>{tr[f'kit_li{i}']}</li>\n" for i in range(1, 13))
    supplement = (tr.get("kit_supplement") or "").strip()
    sup = f'      <p class="kit-count-note">{supplement}</p>\n' if supplement else ""
    block = f"      <ul>\n{items}      </ul>\n{sup}".rstrip()
    return re.sub(
        r"(<div class=\"kit-content\">\s*<div class=\"price-block\"[^>]*>.*?</div>\s*)<ul>.*?</ul>(?:\s*<p class=\"kit-count-note\">[^<]*</p>)?",
        rf"\1{block}",
        html,
        count=1,
        flags=re.DOTALL,
    )


def apply_template_drift(html: str, tr: dict) -> str:
    """Replace legacy IT template snippets that diverged from IT_STRINGS."""
    drift = {
        "01 — CENDORA™: cottura uniforme, zero attacchi": tr.get("why1_eye", ""),
        "«Ho allevato tre bambini e ho cambiato pentole più volte. Con CENDORA™ cuociono in modo uniforme anche a fiamma bassa e si lavano in un attimo. Per quello che ho speso, la qualità mi ha colpito.»": tr.get(
            "rev1_p", ""
        ),
        "Due padelle: 20 cm e 28 cm": tr.get("kit_li10", ""),
        "Batteria CENDORA™ 12 pezzi, pronta da usare": tr.get("kit_h", ""),
    }
    for old, new in drift.items():
        if old and new and old in html:
            html = html.replace(old, new)
    return html


def apply_price_remants(html: str, now: str, was: str) -> str:
    html = html.replace(IT_PRICE_NOW, now)
    html = html.replace(IT_PRICE_WAS, was)
    html = re.sub(r"74€", now, html)
    html = re.sub(r"148€", was, html)
    return html


def apply_testimonial_alts(html: str, tr: dict) -> str:
    for fragment, key in (
        ("review-1.webp", "alt_t1"),
        ("review-2.webp", "alt_t2"),
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


def apply_footer(html: str, tr: dict, geo: str) -> str:
    tagline = tr.get("footer_tagline", "")
    html = html.replace(
        "Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.",
        tagline,
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
        r"<ul class=\"site-footer__list\">.*?</ul>",
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
    powered_top = tr.get("footer_powered_top", "")
    if powered_top:
        html = html.replace(
            "shoptrendcrest.com — Offerto da WHATECH MOBILE CO., LIMITED</p>",
            f"{powered_top}</p>",
            1,
        )
    powered_bottom = tr.get("footer_powered_bottom", "")
    if powered_bottom:
        html = re.sub(
            r'<div class="site-footer__bottom">© <span data-year>\d+</span> [^<]+</div>',
            f'<div class="site-footer__bottom">© <span data-year>2026</span> {powered_bottom}</div>',
            html,
            count=1,
        )
    return html


def apply_cta_and_faq_price(html: str, tr: dict, now: str, it_by_key: dict) -> str:
    cta = tr.get("cta_inline", tr.get("cta", IT_CTA_LITERAL))
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
                r"(?:Alla consegna consegni|Paghi) [^<]+al corriere[^<]*\.",
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


OFFER_PATH_SYNC = """
<script>
(function () {
  var m = location.pathname.match(/\\/cendora-(\\d+)(?:\\/|$)/);
  if (!m) return;
  var id = m[1];
  document.querySelectorAll('input[name="offer"]').forEach(function (el) { el.value = id; });
  if (window.SITE_CONFIG) {
    window.SITE_CONFIG.OFFER_ID = id;
    window.SITE_CONFIG.OFFER_NAME = 'CENDORA ' + id;
  }
})();
</script>
"""


def render_landing(
    offer: str,
    cfg: dict,
    tr: dict,
    it_html: str,
    it_replace: dict[str, str],
    it_by_key: dict,
    forms: dict[str, str],
) -> str:
    geo = cfg["geo"]
    folder = offer_folder(offer)
    landing_url = public_landing_url(geo, offer)
    ty_url = public_thankyou_url(geo, offer)
    was = fmt_price(was_price(cfg["price"]), cfg["currency"])
    now = fmt_price(cfg["price"], cfg["currency"])

    html = it_html
    for note_key in ("form_note_hero", "form_note_form"):
        if note_key in tr and note_key in it_by_key:
            html = html.replace(it_by_key[note_key], tr[note_key])
    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = html.replace("https://shoptrendcrest.com/it/cendora/", landing_url)
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
    html = re.sub(r"PRODUCT_SLUG:\s*'cendora'", f"PRODUCT_SLUG: '{folder}'", html)
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = html.replace("OFFER_NAME: 'CENDORA IT'", f"OFFER_NAME: 'CENDORA {offer}'")
    html = re.sub(
        r"OFFER_ID:\s*'[^']*'",
        f"OFFER_ID: '{offer}'",
        html,
        count=1,
    )
    html = html.replace("LP_ID: 'it-cendora-v1'", f"LP_ID: '{geo}-{folder}'")

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
        count=1,
    )

    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        (
            f"COOKIE_TEXT: '{esc_js(tr['cookie_text'])}',\n"
            f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
            f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}',\n"
            f"  FORM_BLOCKED_MSG: '{esc_js(tr.get('form_blocked_msg', ''))}'"
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
        "submit_btn",
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
    for key in ("f1_h", "f1_p", "f2_h", "f2_p", "f3_h", "f3_p", "f4_h", "f4_p"):
        if key in tr and key in it_by_key and it_by_key[key] in html:
            html = html.replace(it_by_key[key], tr[key])
    html = apply_cta_and_faq_price(html, tr, now, it_by_key)

    html = html.replace("/it/", f"/{geo}/")
    html = html.replace("https://shoptrendcrest.com/it/cendora/thank-you.html", ty_url)

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
    html = apply_kit_list(html, tr)
    html = apply_template_drift(html, tr)
    html = apply_footer(html, tr, geo)
    if "form_note_hero" in tr:
        html = re.sub(
            r'(<p class="form-note">)[^<]+(</p>)',
            rf'\1{tr["form_note_hero"]}\2',
            html,
            count=1,
        )
    if "form_note_form" in tr:
        html = re.sub(
            r'(<form class="tm-order-form.*?<p class="form-note">)[^<]+(</p>)',
            rf'\1{tr["form_note_form"]}\2',
            html,
            count=1,
            flags=re.DOTALL,
        )

    if "cendora-order-form.js" not in html:
        html = html.replace(
            '<script src="/assets/js/noreva-landing.js" defer></script>',
            '<script src="/assets/js/noreva-landing.js" defer></script>\n'
            '<script src="/assets/js/cendora-order-form.js" defer></script>',
            1,
        )

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
    was = fmt_price(was_price(cfg["price"]), cfg["currency"])
    html = it_ty

    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"', 1)
    html = re.sub(r"GEO:\s*'it'", f"GEO: '{geo}'", html)
    html = re.sub(r"PRODUCT_SLUG:\s*'cendora'", f"PRODUCT_SLUG: '{folder}'", html)
    html = re.sub(
        r'<link rel="canonical" href="[^"]+"\s*/?>',
        f'<link rel="canonical" href="{ty_url}">',
        html,
        count=1,
    )
    html = re.sub(r"CURRENCY:\s*'EUR'", f"CURRENCY: '{cfg['currency']}'", html)
    html = re.sub(r"PRICE:\s*[\d.]+", f"PRICE: {cfg['price']}", html)
    html = re.sub(
        r"COOKIE_TEXT:\s*'[^']*',\s*\n\s*COOKIE_ACCEPT:\s*'[^']*',\s*\n\s*COOKIE_LEARN:\s*'[^']*'",
        (
            f"COOKIE_TEXT: '{esc_js(tr['cookie_text'])}',\n"
            f"  COOKIE_ACCEPT: '{esc_js(tr['cookie_accept'])}',\n"
            f"  COOKIE_LEARN: '{esc_js(tr['cookie_learn'])}'"
        ),
        html,
    )

    html = re.sub(r"<title>.*?</title>", f"<title>{tr['ty_title']}</title>", html, count=1)
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
        "ty_order_header",
        "ty_product",
    ):
        if key in it_by_key and key in tr:
            html = html.replace(it_by_key[key], tr[key])

    if "ty_order_header" in tr:
        aria = tr["ty_order_header"].replace("🛒 ", "").strip()
        html = html.replace('aria-label="Il tuo ordine"', f'aria-label="{aria}"')

    ty_steps = [s.format(price=now) for s in tr["ty_steps"]]
    steps_html = "\n".join(f"        <li>{s}</li>" for s in ty_steps)
    html = re.sub(
        r'<ol class="ty-steps-list">.*?</ol>',
        f'<ol class="ty-steps-list">\n{steps_html}\n      </ol>',
        html,
        count=1,
        flags=re.DOTALL,
    )

    it_badges = it_by_key["ty_badges"]
    for ib, lb in zip(it_badges, tr["ty_badges"]):
        html = html.replace(ib, lb)

    pay_it = it_by_key["ty_pay"].format(price=IT_PRICE_NOW)
    html = html.replace(pay_it, tr["ty_pay"].format(price=now))
    html = apply_price_remants(html, now, was)
    html = html.replace("https://shoptrendcrest.com/it/cendora/thank-you.html", ty_url)
    html = html.replace("/it/cendora/", f"/{geo}/{folder}/")

    html = re.sub(
        r"<!-- Event snippet for Purchase.*?/script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )

    if cfg["currency"] == "EUR":
        html = normalize_euro_spacing(html)
    html = apply_footer(html, tr, geo)
    return html


def load_offer_configs() -> dict[str, dict]:
    offers = json.loads((ROOT / "content/cendora/offers.json").read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for o in offers:
        oid = str(o["id"])
        out[oid] = {
            "geo": o["geo"],
            "lang": o["lang"],
            "tr": o["lang"],
            "price": float(o["price"]),
            "currency": o["currency"],
        }
    return out


def preflight() -> list[str]:
    errors: list[str] = []
    site = json.loads((ROOT / "content/cendora/site.json").read_text(encoding="utf-8"))
    if not (site.get("domain") or "").strip():
        errors.append("content/cendora/site.json: domain is empty")
    if not (site.get("product_slug") or "").strip():
        errors.append("content/cendora/site.json: product_slug is empty")
    try:
        load_translations()
    except Exception as exc:
        errors.append(f"locales: {exc}")
    try:
        load_network_forms()
    except Exception as exc:
        errors.append(f"forms: {exc}")
    return errors


def main(only: set[str] | None = None) -> int:
    errors = preflight()
    if errors:
        print("gen_cendora_geos.py: not ready\n", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    tr_all = load_translations()
    it_by_key = load_it_by_key()
    it_replace = build_it_replace_map(it_by_key)
    forms = load_network_forms()
    tpl_dir = Path(__file__).with_name("templates")
    it_landing = (tpl_dir / "cendora_it_landing.html").read_text(encoding="utf-8")
    it_ty = (tpl_dir / "cendora_it_thank_you.html").read_text(encoding="utf-8")
    configs = load_offer_configs()

    urls: list[str] = []
    for offer, cfg in configs.items():
        if only is not None and offer not in only:
            continue
        tr = tr_all[cfg["tr"]]
        geo = cfg["geo"]
        out_dir = ROOT / geo / offer_folder(offer)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            render_landing(offer, cfg, tr, it_landing, it_replace, it_by_key, forms),
            encoding="utf-8",
        )
        ty_dir = out_dir / "thank-you"
        ty_dir.mkdir(parents=True, exist_ok=True)
        (ty_dir / "index.html").write_text(
            render_thank_you(offer, cfg, tr, it_ty, it_by_key),
            encoding="utf-8",
        )
        lp_url = public_landing_url(geo, offer)
        ty_url = public_thankyou_url(geo, offer)
        urls.extend([lp_url, ty_url])
        print(
            f"Wrote {geo}/{offer_folder(offer)}/ (#{offer}) "
            f"now={cfg['price']} {cfg['currency']} was={was_price(cfg['price'])}"
        )

    print("\n--- Summary URLs ---")
    for url in urls:
        print(url)
    return 0


if __name__ == "__main__":
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    raise SystemExit(main(only))
