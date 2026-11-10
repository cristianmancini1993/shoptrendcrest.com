#!/usr/bin/env python3
"""Clone shoptrendcrest LEAFORA landings into homeshopspot.com (native copy per geo)."""

from __future__ import annotations

import importlib.util
import re
import urllib.request
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import footer_blurb_column_html

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://shoptrendcrest.com"

META_PIXEL = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

OFFERS: dict[str, dict] = {
    "1745": {
        "geo": "pl",
        "lang": "pl",
        "tr": "pl",
        "slug": "leafora-1745",
        "src": "pl/leafora-1745",
        "price": 359.0,
        "currency": "PLN",
        "cpa": 16.0,
    },
    "2653": {
        "geo": "hu",
        "lang": "hu",
        "tr": "hu",
        "slug": "leafora-2653",
        "src": "hu/leafora-1746",
        "price": 32990.0,
        "currency": "HUF",
        "cpa": 17.0,
        "price_find": (("32 999", "32 990"), ("32999", "32990"), ("32.999", "32.990")),
    },
    "2657": {
        "geo": "ro",
        "lang": "ro",
        "tr": "ro",
        "slug": "leafora-2657",
        "src": "ro/leafora-2657",
        "price": 397.0,
        "currency": "RON",
        "cpa": 16.0,
    },
    "3188": {
        "geo": "de",
        "lang": "de",
        "tr": "de",
        "slug": "leafora-3188",
        "src": "de/leafora-3188",
        "price": 86.0,
        "currency": "EUR",
        "cpa": 16.0,
    },
    "3189": {
        "geo": "lt",
        "lang": "lt",
        "tr": "lt",
        "slug": "leafora-3189",
        "src": "lt/leafora-3189",
        "price": 69.0,
        "currency": "EUR",
        "cpa": 13.0,
    },
    "3190": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cz",
        "slug": "leafora-3190",
        "src": "cz/leafora-3190",
        "price": 1499.0,
        "currency": "CZK",
        "cpa": 16.0,
    },
    "3191": {
        "geo": "pt",
        "lang": "pt",
        "tr": "pt",
        "slug": "leafora-3191",
        "src": "pt/leafora-3191",
        "price": 69.0,
        "currency": "EUR",
        "cpa": 15.0,
    },
    "3192": {
        "geo": "es",
        "lang": "es",
        "tr": "es",
        "slug": "leafora-3192",
        "src": "es/leafora-3192",
        "price": 69.0,
        "currency": "EUR",
        "cpa": 15.0,
    },
    "4065": {
        "geo": "sk",
        "lang": "sk",
        "tr": "sk",
        "slug": "leafora-4065",
        "src": "sk/leafora-4065",
        "price": 79.0,
        "currency": "EUR",
        "cpa": 17.0,
    },
    "4066": {
        "geo": "lv",
        "lang": "lv",
        "tr": "lv",
        "slug": "leafora-4066",
        "src": "sk/leafora-4065",
        "price": 79.0,
        "currency": "EUR",
        "cpa": 14.0,
        "lv_from_sk": True,
    },
    "4188": {
        "geo": "it",
        "lang": "it",
        "tr": "it",
        "slug": "leafora-4188",
        "src": "it/leafora-1650",
        "price": 69.99,
        "currency": "EUR",
        "cpa": 12.0,
        "price_find": (("79,99", "69,99"), ("79.99", "69.99"), ("79 €", "69,99 €")),
    },
}


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_chrome(tr_key: str) -> dict:
    ym = load_mod("gen_yardmax_geos", Path(__file__).with_name("gen_yardmax_geos.py"))
    product = ym.load_product()
    chrome = ym.load_chrome()
    return ym.merge_tr(tr_key, product, chrome)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-clone/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def build_footer(geo: str, t: dict) -> str:
    lang = t.get("__lang__") or ""
    if not lang:
        raise ValueError("build_footer requires t['__lang__'] (html lang)")
    first_col = footer_blurb_column_html(
        t["footer_blurb"], lang, show_ai_notice=True
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
{first_col}
      <div>
        <h4 class="site-footer__heading">{t["info"]}</h4>
        <ul class="site-footer__list">
          <li><a href="/{geo}/about-us.html">{t["about"]}</a></li>
          <li><a href="/{geo}/contact-us.html">{t["contact"]}</a></li>
          <li><a href="/{geo}/privacy-policy.html">{t["privacy"]}</a></li>
          <li><a href="/{geo}/terms-conditions.html">{t["terms"]}</a></li>
          <li><a href="/{geo}/cookie-policy.html">{t["cookie"]}</a></li>
          <li><a href="/{geo}/shipping-policy.html">{t["ship"]}</a></li>
          <li><a href="/{geo}/refund-policy.html">{t["refund"]}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{t["contacts"]}</h4>
        <ul class="site-footer__list">
          <li><strong>Northstar Digital Growth LLC</strong></li>
          <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
          <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — {t["rights"]}
      <a href="/">homeshopspot.com</a>
    </div>
  </div>
</footer>
<script src="/assets/js/glacierair-landing.js" defer></script>
<script>document.querySelectorAll('[data-year]').forEach(function(el){{el.textContent=String(new Date().getFullYear());}});</script>"""


def patch_site_config(html: str, cfg: dict) -> str:
    offer_id = cfg["offer_id"]
    slug = cfg["slug"]
    geo = cfg["geo"]
    price = cfg["price"]
    currency = cfg["currency"]
    cpa = cfg["cpa"]
    html = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{currency}',
  PRICE: {price},
  OFFER_NAME: 'LEAFORA {offer_id}',
  OFFER_ID: '{offer_id}',
  LP_ID: '{geo}-leafora-{offer_id}',
  FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/',
  SUBMITTING_LABEL: '…',
  COOKIE_TEXT: '…',
  COOKIE_ACCEPT: '…',
  COOKIE_LEARN: '…',
}};""",
        html,
        count=1,
    )
    t = load_chrome(cfg["tr"])
    cookie_block = (
        f"  COOKIE_TEXT: '{t['cookie_text'].replace(chr(39), chr(92)+chr(39))}',\n"
        f"  COOKIE_ACCEPT: '{t['cookie_accept']}',\n"
        f"  COOKIE_LEARN: '{t['cookie_learn']}'"
    )
    html = re.sub(
        r"  SUBMITTING_LABEL: '[^']*',\s*COOKIE_TEXT: '[^']*',\s*COOKIE_ACCEPT: '[^']*',\s*COOKIE_LEARN: '[^']*'",
        f"  SUBMITTING_LABEL: '{t['submitting']}',\n{cookie_block}",
        html,
        count=1,
    )
    return html


def patch_form(html: str, cfg: dict, net) -> str:
    offer_id = cfg["offer_id"]
    geo = cfg["geo"]
    slug = cfg["slug"]
    forms = net.FORMS[offer_id]
    ty_url = f"https://homeshopspot.com/{geo}/{slug}/thank-you.html"
    html = re.sub(r'<input name="uid"[^>]*>', f'<input name="uid" type="hidden" value="{net.UID}" />', html)
    html = re.sub(
        r'<input name="offer"[^>]*>',
        f'<input name="offer" type="hidden" value="{offer_id}" />',
        html,
    )
    html = re.sub(r'<input name="lp"[^>]*>', f'<input name="lp" type="hidden" value="{forms["lp"]}" />', html)
    html = re.sub(
        r'<input name="_key"[^>]*>',
        f'<input name="_key" type="hidden" value="{forms["key"]}" />',
        html,
    )
    html = re.sub(
        r'<input name="webhook"[^>]*>',
        f'<input name="webhook" type="hidden" value="{net.WEBHOOK}" />',
        html,
    )
    html = re.sub(
        r'<input name="thankyoupage"[^>]*>',
        f'<input name="thankyoupage" type="hidden" value="{ty_url}"/>',
        html,
    )
    return html


def apply_lv_from_sk(html: str) -> str:
    overlay = load_mod("_leafora_sk_to_lv", Path(__file__).with_name("_leafora_sk_to_lv.py"))
    for old, new in sorted(overlay.REPLACEMENTS, key=lambda p: -len(p[0])):
        html = html.replace(old, new)
    return html


def process_landing(html: str, cfg: dict, net, t: dict) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    offer_id = cfg["offer_id"]

    if cfg.get("lv_from_sk"):
        html = apply_lv_from_sk(html)

    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)

    html = html.replace("info@shoptrendcrest.com", "info@homeshopspot.com")
    html = html.replace("https://shoptrendcrest.com", "https://homeshopspot.com")

    src_slug_match = re.search(rf"/{geo}/(leafora[^/\"']+)/", html)
    if src_slug_match:
        old_slug = src_slug_match.group(1)
        html = html.replace(f"/{geo}/{old_slug}/", f"/{geo}/{slug}/")
        html = html.replace(f"/{geo}/{old_slug}", f"/{geo}/{slug}")

    for other_geo in ("pl", "hu", "ro", "de", "lt", "cz", "pt", "es", "sk", "it"):
        html = re.sub(
            rf"https://homeshopspot\.com/{other_geo}/leafora-\d+/thank-you/?",
            f"https://homeshopspot.com/{geo}/{slug}/thank-you.html",
            html,
        )

    html = re.sub(
        r'<link rel="canonical" href="https://homeshopspot\.com/[^"]+">',
        f'<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">',
        html,
        count=1,
    )

    pf = cfg.get("price_find")
    if isinstance(pf, tuple) and len(pf) == 2 and isinstance(pf[0], str):
        html = html.replace(pf[0], pf[1])
    elif isinstance(pf, tuple):
        for a, b in pf:
            html = html.replace(a, b)

    html = patch_site_config(html, cfg)
    html = patch_form(html, cfg, net)

    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>\s*"
        r"<script src=\"/assets/js/glacierair-landing.js\" defer></script>\s*"
        r"<script>document\.querySelectorAll\('\[data-year\]'\).*?</script>",
        build_footer(geo, t),
        html,
        count=1,
        flags=re.DOTALL,
    )

    if cfg.get("lv_from_sk"):
        html = re.sub(r"value=\"4065\"", f'value="{offer_id}"', html)
        html = html.replace("leafora-4065", slug)
        html = html.replace("GEO: 'sk'", f"GEO: '{geo}'")
        html = re.sub(r'lang="sk"', f'lang="{cfg["lang"]}"', html, count=1)

    html = re.sub(
        rf'<input name="offer" type="hidden" value="\d+" />',
        f'<input name="offer" type="hidden" value="{offer_id}" />',
        html,
        count=1,
    )

    return html


def build_thank_you(cfg: dict, t: dict) -> str:
    geo = cfg["geo"]
    slug = cfg["slug"]
    offer_id = cfg["offer_id"]
    cpa = cfg["cpa"]
    ym_path = ROOT / geo / f"yardmax-{offer_id}" / "thank-you.html"
    if not ym_path.exists() and offer_id == "4188":
        ym_path = ROOT / geo / "yardmax-1650" / "thank-you.html"
    if not ym_path.exists():
        ym_path = ROOT / "pl" / f"yardmax-1745" / "thank-you.html"
    ty = ym_path.read_text(encoding="utf-8")
    ty = ty.replace(f"yardmax-{offer_id}", slug)
    if offer_id == "4188":
        ty = ty.replace("yardmax-1650", slug)
    ty = ty.replace("YardMax™", "LEAFORA™").replace("YardMax", "LEAFORA")
    ty = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", ty, count=1)
    ty = re.sub(
        r"fbq\('track', 'Purchase', \{\s*value: [0-9.]+,\s*currency: 'EUR'\s*\}\);",
        f"fbq('track', 'Purchase', {{ value: {cpa:.2f}, currency: 'EUR' }});",
        ty,
        count=1,
    )
    ty = re.sub(r"PRODUCT_SLUG:\s*'[^']*'", f"PRODUCT_SLUG: '{slug}'", ty, count=1)
    return ty


def write_index(cfg: dict) -> str:
    geo, slug, lang = cfg["geo"], cfg["slug"], cfg["lang"]
    return f"""<!DOCTYPE html>
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
<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">
</head>
<body>
<p><a href="/{geo}/{slug}/landing.html">LEAFORA™</a></p>
</body>
</html>
"""


def main(only: set[str] | None = None) -> None:
    net = load_mod("yardmax_network_forms", Path(__file__).with_name("yardmax_network_forms.py"))
    assets = ROOT / "assets" / "img" / "products" / "leafora"
    assets.mkdir(parents=True, exist_ok=True)

    for offer_id, cfg in OFFERS.items():
        if only and offer_id not in only:
            continue
        cfg = dict(cfg)
        cfg["offer_id"] = offer_id
        cfg["cpa"] = net.CPA.get(offer_id, cfg["cpa"])
        geo, slug, src = cfg["geo"], cfg["slug"], cfg["src"]
        t = load_chrome(cfg["tr"])
        t = dict(t)
        t["__lang__"] = cfg["lang"]

        page_url = f"{SRC}/{src}/"
        html = fetch(page_url).decode("utf-8")

        imgs = sorted(set(re.findall(r"/assets/img/products/leafora/[^\"']+", html)))
        for rel in imgs:
            dest = ROOT / rel.lstrip("/")
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                print("GET", rel)
                dest.write_bytes(fetch(SRC + rel))

        html = process_landing(html, cfg, net, t)
        out = ROOT / geo / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "landing.html").write_text(html, encoding="utf-8", newline="\n")
        (out / "index.html").write_text(write_index(cfg), encoding="utf-8", newline="\n")
        (out / "thank-you.html").write_text(build_thank_you(cfg, t), encoding="utf-8", newline="\n")
        print(f"OK {geo}/{slug}/  #{offer_id}  CPA €{cfg['cpa']:g}")


if __name__ == "__main__":
    import sys

    sel = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(sel)
