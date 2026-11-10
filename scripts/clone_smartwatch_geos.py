#!/usr/bin/env python3
"""Clone shoproomdock smartwatch-{offer} landings into homeshopspot.com."""

from __future__ import annotations

import importlib.util
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import footer_blurb_column_html

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://shoproomdock.com"

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
    "586": {"geo": "hr", "lang": "hr", "tr": "hr", "brand": "Noventis"},
    "642": {"geo": "cz", "lang": "cs", "tr": "cz", "brand": "Noventis"},
    "779": {"geo": "si", "lang": "sl", "tr": "si", "brand": "Noventis"},
    "1633": {"geo": "pt", "lang": "pt", "tr": "pt", "brand": "Noventis"},
    "1636": {"geo": "lt", "lang": "lt", "tr": "lt", "brand": "Noventis"},
    "1842": {"geo": "gr", "lang": "el", "tr": "el", "brand": "Noventis"},
    "1843": {"geo": "bg", "lang": "bg", "tr": "bg", "brand": "Noventis"},
    "1844": {"geo": "ro", "lang": "ro", "tr": "ro", "brand": "Noventis"},
    "2297": {"geo": "es", "lang": "es", "tr": "es", "brand": "Noventis"},
    "2934": {"geo": "de", "lang": "de", "tr": "de", "brand": "Noventis"},
    "3141": {"geo": "pl", "lang": "pl", "tr": "pl", "brand": "Noventis"},
    "3143": {
        "geo": "cz",
        "lang": "cs",
        "tr": "cz",
        "brand": "Noventis",
        "price_replace": [
            ("1.499 Kč", "1.999 Kč"),
            ("2.998 Kč", "3.998 Kč"),
            ("1499", "1999"),
            ("2998", "3998"),
        ],
    },
    "3834": {"geo": "lv", "lang": "lv", "tr": "lv", "brand": "Noventis"},
}

FALLBACK_FOOTER = {
    "footer_blurb": "Useful products for everyday life, fast delivery and cash on delivery.",
    "info": "Information",
    "about": "About us",
    "contact": "Contact",
    "privacy": "Privacy Policy",
    "terms": "Terms & Conditions",
    "cookie": "Cookie Policy",
    "ship": "Shipping",
    "refund": "Returns",
    "contacts": "Contact",
    "rights": "All rights reserved.",
}


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_footer_tr(tr_key: str) -> dict:
    ym = load_mod("gen_yardmax_geos", Path(__file__).with_name("gen_yardmax_geos.py"))
    chrome = ym.load_chrome()
    if tr_key in chrome and chrome[tr_key].get("footer_blurb"):
        return chrome[tr_key]
    return FALLBACK_FOOTER


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-clone/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def slug_for(offer_id: str) -> str:
    return f"smartwatch-{offer_id}"


def strip_gtag(html: str) -> str:
    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"<!-- Event snippet for Purchase.*?<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<script async src="https://www.googletagmanager.com/gtag/js[^"]*"></script>\s*<script>[\s\S]*?</script>\s*',
        "",
        html,
        count=1,
    )
    html = re.sub(
        r"GOOGLE_ADS_CONVERSION_SEND_TO: '[^']*',\s*",
        "",
        html,
        count=1,
    )
    html = re.sub(
        r"  META_PIXEL_ID: '',\s*GOOGLE_TAG_ID: '',\s*GOOGLE_ADS_CONVERSION_ID: '',\s*TY_CONVERSION_LABEL: '',\s*",
        "",
        html,
        count=1,
    )
    return html


def build_footer(geo: str, t: dict, *, page_lang: str) -> str:
    first_col = footer_blurb_column_html(
        t["footer_blurb"], page_lang, show_ai_notice=True
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
          <li>32 N Gould St., Sheridan, WY 82801, United States</li>
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
<script>document.querySelectorAll('[data-year]').forEach(function(el){{el.textContent=String(new Date().getFullYear());}});</script>"""


def homeshopspotify(html: str, geo: str, offer_id: str) -> str:
    slug = slug_for(offer_id)
    src_prefix = f"shoproomdock.com/{geo}/smartwatch-{offer_id}"
    dst_prefix = f"homeshopspot.com/{geo}/{slug}"
    html = html.replace(src_prefix, dst_prefix)
    html = html.replace("shoproomdock.com", "homeshopspot.com")
    html = html.replace("info@shoproomdock.com", "info@homeshopspot.com")
    html = html.replace("The Lead Empire L.L.C-FZ", "Northstar Digital Growth LLC")
    html = html.replace(
        "Meydan Grandstand, 6th floor, Meydan Road, Dubai, Emiratos Árabes Unidos",
        "32 N Gould St., Sheridan, WY 82801, United States",
    )
    ty = f"https://homeshopspot.com/{geo}/{slug}/thank-you.html"
    html = re.sub(
        r'<input name="thankyoupage"[^>]*>',
        f'<input name="thankyoupage" type="hidden" value="{ty}"/>',
        html,
        count=1,
    )
    html = re.sub(
        rf'<link rel="canonical" href="https://homeshopspot\.com/{geo}/smartwatch-{offer_id}/">',
        f'<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">',
        html,
        count=1,
    )
    return html


def patch_form(html: str, offer_id: str, net) -> str:
    forms = net.FORMS[offer_id]
    html = re.sub(
        r'<input name="uid"[^>]*>',
        f'<input name="uid" type="hidden" value="{net.UID}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<input name="lp"[^>]*>',
        f'<input name="lp" type="hidden" value="{forms["lp"]}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<input name="_key"[^>]*>',
        f'<input name="_key" type="hidden" value="{forms["key"]}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<input name="webhook"[^>]*>',
        f'<input name="webhook" type="hidden" value="{net.WEBHOOK}" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<input name="offer"[^>]*>',
        f'<input name="offer" type="hidden" value="{offer_id}" />',
        html,
        count=1,
    )
    return html


def patch_site_config(html: str, geo: str, offer_id: str, brand: str) -> str:
    slug = slug_for(offer_id)
    html = re.sub(r"PRODUCT_SLUG: '[^']*'", f"PRODUCT_SLUG: '{slug}'", html, count=1)
    html = re.sub(r"OFFER_ID: '\d+'", f"OFFER_ID: '{offer_id}'", html, count=1)
    html = re.sub(r"LP_ID: '[^']*'", f"LP_ID: '{geo}-{slug}'", html, count=1)
    html = re.sub(
        r"OFFER_NAME: '[^']*'",
        f"OFFER_NAME: '{brand} {offer_id}'",
        html,
        count=1,
    )
    html = re.sub(r"GEO: '[^']*'", f"GEO: '{geo}'", html, count=1)
    return html


def download_assets(html: str) -> None:
    paths = sorted(set(re.findall(r"/assets/img/products/noventis/[^\"'\\s>]+", html)))
    for rel in paths:
        dest = ROOT / rel.lstrip("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            print("GET", rel)
            dest.write_bytes(fetch(SRC + rel))


def process_landing(html: str, cfg: dict, net) -> str:
    offer_id = cfg["offer_id"]
    geo = cfg["geo"]
    t = load_footer_tr(cfg["tr"])

    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = homeshopspotify(html, geo, offer_id)
    html = patch_site_config(html, geo, offer_id, cfg["brand"])
    html = patch_form(html, offer_id, net)
    for old, new in cfg.get("price_replace", []):
        html = html.replace(old, new)
    if "glacierair-landing.css" not in html:
        html = html.replace(
            "</style>",
            '</style>\n<link rel="stylesheet" href="/assets/css/glacierair-landing.css">',
            1,
        )
    html = re.sub(
        r'<footer class="gsh-standalone-footer">.*?</footer>',
        build_footer(geo, t, page_lang=cfg["lang"]),
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'<meta name="offer-id" content="\d+">',
        f'<meta name="offer-id" content="{offer_id}">',
        html,
        count=1,
    )
    return html


def process_thank_you(html: str, cfg: dict, cpa: float) -> str:
    offer_id = cfg["offer_id"]
    geo = cfg["geo"]
    brand = cfg["brand"]
    t = load_footer_tr(cfg["tr"])

    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = homeshopspotify(html, geo, offer_id)
    html = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", html, count=1)
    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        build_footer(geo, t, page_lang=cfg["lang"]),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if "fbq('track', 'Purchase'" not in html:
        html += f"""

<script>
fbq('track', 'Purchase', {{
  value: {cpa:.2f},
  currency: 'EUR'
}});
</script>
"""
    else:
        html = re.sub(
            r"fbq\('track', 'Purchase', \{\s*value: [0-9.]+,\s*currency: 'EUR'\s*\}\);",
            f"fbq('track', 'Purchase', {{ value: {cpa:.2f}, currency: 'EUR' }});",
            html,
            count=1,
        )
    return html


def write_index(cfg: dict) -> str:
    geo, lang = cfg["geo"], cfg["lang"]
    slug = slug_for(cfg["offer_id"])
    label = f"{cfg['brand']}™"
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
<p><a href="/{geo}/{slug}/landing.html">{label}</a></p>
</body>
</html>
"""


def main(only: set[str] | None = None) -> None:
    net = load_mod(
        "smartwatch_network_forms",
        Path(__file__).with_name("smartwatch_network_forms.py"),
    )
    for offer_id, base in OFFERS.items():
        if only and offer_id not in only:
            continue
        cfg = dict(base)
        cfg["offer_id"] = offer_id
        geo = cfg["geo"]
        slug = slug_for(offer_id)
        cpa = net.CPA[offer_id]

        landing_url = f"{SRC}/{geo}/smartwatch-{offer_id}/"
        html = fetch(landing_url).decode("utf-8")
        download_assets(html)
        html = process_landing(html, cfg, net)

        ty_url = f"{SRC}/{geo}/smartwatch-{offer_id}/thank-you/"
        ty = fetch(ty_url).decode("utf-8")
        ty = process_thank_you(ty, cfg, cpa)

        out = ROOT / geo / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "landing.html").write_text(html, encoding="utf-8", newline="\n")
        (out / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
        (out / "index.html").write_text(write_index(cfg), encoding="utf-8", newline="\n")
        print(f"OK {geo}/{slug}/  #{offer_id}  CPA EUR {cpa:g}")


if __name__ == "__main__":
    import sys

    sel = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    main(sel)
