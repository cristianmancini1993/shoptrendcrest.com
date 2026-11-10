#!/usr/bin/env python3
"""Generate LUNO™ localized landings + thank-you pages from shoproomdock driovo sources."""

from __future__ import annotations

import importlib.util
import re
import urllib.request
import sys
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

OFFERS = {
    "1912": {"geo": "de", "lang": "de", "price": 92.0, "currency": "EUR"},
    "1915": {"geo": "hu", "lang": "hu", "price": 29999.0, "currency": "HUF"},
    "2480": {"geo": "pt", "lang": "pt", "price": 79.0, "currency": "EUR"},
    "3163": {"geo": "es", "lang": "es", "price": 79.0, "currency": "EUR"},
    "3167": {"geo": "pl", "lang": "pl", "price": 339.0, "currency": "PLN"},
    "3169": {"geo": "cz", "lang": "cs", "price": 1899.0, "currency": "CZK"},
    "3910": {"geo": "lv", "lang": "lv", "price": 85.0, "currency": "EUR"},
    "4321": {"geo": "sk", "lang": "sk", "price": 74.0, "currency": "EUR"},
}

def remove_desc3_block(html: str) -> str:
    parts = re.split(r"(?=<section class=\"why-block wrap\")", html)
    out: list[str] = []
    for part in parts:
        if "desc-3.webp" in part.lower():
            continue
        out.append(part)
    return "".join(out)


def load_mod(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-luno-gen/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8", "replace")


def fmt_price(amount: float, currency: str) -> str:
    wholeish = abs(amount - round(amount)) < 0.001
    if currency == "HUF":
        whole = int(round(amount))
        s = f"{whole:,}".replace(",", " ")
        return f"{s} Ft"
    if currency == "CZK":
        whole = int(round(amount))
        s = f"{whole:,}".replace(",", " ")
        return f"{s} Kč"
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
    return round(now * 2) if abs(now - round(now)) < 0.001 else round(now * 2, 2)


def build_footer(geo: str, lang: str, chrome) -> str:
    t = chrome.FOOTER[lang]
    first_col = footer_blurb_column_html(t["blurb"], lang, show_ai_notice=True)
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

<script src="/assets/js/glacierair-landing.js" defer></script>
<script>document.querySelectorAll('[data-year]').forEach(function (el) {{ el.textContent = String(new Date().getFullYear()); }});</script>"""


def patch_prices(html: str, now: float, currency: str) -> str:
    was = was_price(now)
    was_s = fmt_price(was, currency)
    now_s = fmt_price(now, currency)
    html = re.sub(r'<span class="was">[^<]+</span>', f'<span class="was">{was_s}</span>', html)
    html = re.sub(r'<span class="now">[^<]+</span>', f'<span class="now">{now_s}</span>', html)
    return html


def patch_review_alts(html: str, lang: str, chrome) -> str:
    a1, a2 = chrome.REVIEW_ALTS[lang]
    html = re.sub(
        r'(<img class="t-photo" src="/assets/img/reviews/luno/review-1\.webp[^"]*" alt=")[^"]+(")',
        rf"\1{a1}\2",
        html,
        count=1,
    )
    html = re.sub(
        r'(<img class="t-photo" src="/assets/img/reviews/luno/review-2\.webp[^"]*" alt=")[^"]+(")',
        rf"\1{a2}\2",
        html,
        count=1,
    )
    return html


def patch_review3(html: str, lang: str, chrome) -> str:
    r3 = chrome.REVIEW3[lang]
    chunks = html.split('<div class="testimonial">')
    if len(chunks) < 4:
        return html
    t3 = chunks[3]
    t3 = re.sub(
        r'<img class="t-photo" src="[^"]+" alt="[^"]+"',
        f'<img class="t-photo" src="/assets/img/reviews/luno/review-3.jpg?v=5" alt="{r3["alt"]}"',
        t3,
        count=1,
    )
    t3 = re.sub(r"<h4>[^<]+</h4>", f"<h4>{r3['h4']}</h4>", t3, count=1)
    t3 = re.sub(r"<p>«[^»]+»</p>", f"<p>{r3['quote']}</p>", t3, count=1)
    chunks[3] = t3
    return '<div class="testimonial">'.join(chunks)


def process_landing(html: str, offer_id: str, cfg: dict, net, chrome) -> str:
    src_html = html
    geo, lang = cfg["geo"], cfg["lang"]
    slug = f"luno-{offer_id}"
    src_slug = f"driovo-{offer_id}"
    price, currency = cfg["price"], cfg["currency"]
    forms = net.FORMS[offer_id]
    ty_url = f"https://homeshopspot.com/{geo}/{slug}/thank-you.html"

    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)

    html = remove_desc3_block(html)
    html = re.sub(r"04 —", "03 —", html)
    html = re.sub(r">04 —", ">03 —", html)

    html = html.replace("Driovo™", "LUNO™").replace("Driovo", "LUNO").replace("DRIOVO™", "LUNO™")
    html = html.replace("driovo-video", "luno-video")
    html = html.replace("/assets/img/products/driovo/", "/assets/img/products/luno/")
    html = html.replace("/assets/img/reviews/driovo/", "/assets/img/reviews/luno/")
    html = html.replace("/assets/video/driovo/", "/assets/video/luno/")
    html = html.replace("funzionamento.mp4", "funzionamento.mp4?v=2")
    html = html.replace("hero.webp?v=7", "hero.webp?v=8")
    html = html.replace("desc-2.webp?v=3", "desc-2.webp?v=4")
    html = html.replace("desc-4.webp?v=5", "desc-4.webp?v=6")
    html = html.replace("kit.webp?v=3", "kit.webp?v=5")
    html = re.sub(r"review-([12])\.webp\?v=3", r"review-\1.webp?v=4", html)
    html = html.replace("review-3.webp?v=3", "review-3.jpg?v=5")

    html = html.replace("shoproomdock.com", "homeshopspot.com")
    html = html.replace("shoproomdock", "homeshopspot")
    html = html.replace(f"/{geo}/{src_slug}/", f"/{geo}/{slug}/")
    html = html.replace(f"driovo-{offer_id}", slug)
    html = html.replace(f"luno-{offer_id}/thank-you/", ty_url)

    html = re.sub(
        r'<link rel="canonical" href="[^"]+">',
        f'<link rel="canonical" href="https://homeshopspot.com/{geo}/{slug}/landing.html">',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]+">',
        f'<meta property="og:url" content="https://homeshopspot.com/{geo}/{slug}/landing.html">',
        html,
        count=1,
    )
    html = re.sub(r'lang="[a-z]{2}"', f'lang="{lang}"', html, count=1)

    html = re.sub(r"<h1[^>]*>.*?</h1>", f"<h1>{chrome.H1[lang]}</h1>", html, count=1, flags=re.DOTALL)
    html = patch_prices(html, price, currency)
    html = patch_review_alts(html, lang, chrome)
    html = patch_review3(html, lang, chrome)

    html = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{currency}',
  PRICE: {price},
  OFFER_NAME: 'LUNO {offer_id}',
  OFFER_ID: '{offer_id}',
  LP_ID: '{geo}-luno-{offer_id}',
  FORM_ENDPOINT: '{net.ACTION}',
  SUBMITTING_LABEL: '…',
  COOKIE_TEXT: '…',
  COOKIE_ACCEPT: '…',
  COOKIE_LEARN: '…'
}};""",
        html,
        count=1,
    )

    src_cookie = re.search(
        r"COOKIE_TEXT: '([^']*)',\s*COOKIE_ACCEPT: '([^']*)',\s*COOKIE_LEARN: '([^']*)'",
        src_html,
    )
    submit = re.search(r"SUBMITTING_LABEL: '([^']*)'", src_html)
    if src_cookie and submit:
        html = re.sub(
            r"  SUBMITTING_LABEL: '[^']*',\s*COOKIE_TEXT: '[^']*',\s*COOKIE_ACCEPT: '[^']*',\s*COOKIE_LEARN: '[^']*'",
            (
                f"  SUBMITTING_LABEL: '{submit.group(1)}',\n"
                f"  COOKIE_TEXT: '{src_cookie.group(1)}',\n"
                f"  COOKIE_ACCEPT: '{src_cookie.group(2)}',\n"
                f"  COOKIE_LEARN: '{src_cookie.group(3)}'"
            ),
            html,
            count=1,
        )

    html = re.sub(r'<input name="uid"[^>]*>', f'<input name="uid" type="hidden" value="{net.UID}">', html)
    html = re.sub(
        r'<input name="offer"[^>]*>',
        f'<input name="offer" type="hidden" value="{offer_id}">',
        html,
    )
    html = re.sub(r'<input name="lp"[^>]*>', f'<input name="lp" type="hidden" value="{forms["lp"]}">', html)
    html = re.sub(
        r'<input name="_key"[^>]*>',
        f'<input name="_key" type="hidden" value="{forms["key"]}">',
        html,
    )
    html = re.sub(
        r'<input name="webhook"[^>]*>',
        f'<input name="webhook" type="hidden" value="{net.WEBHOOK}">',
        html,
    )
    html = re.sub(
        r'<input name="thankyoupage"[^>]*>',
        f'<input name="thankyoupage" type="hidden" value="{ty_url}">',
        html,
    )
    if 'class="tm-order-form' not in html:
        html = html.replace('class="cod-form tm-order-form order-form"', 'class="tm-order-form order-form"')
    if "forms/html/js-v2/" not in html:
        html = html.replace(
            "</form>",
            '          <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>\n        </form>',
            1,
        )

    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>\s*"
        r"(?:<script src=\"/assets/js/glacierair-landing.js\" defer></script>\s*)?"
        r"(?:<script>document\.querySelectorAll\('\[data-year\]'\).*?</script>\s*)?",
        build_footer(geo, lang, chrome),
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace("The Lead Empire L.L.C-FZ", "Northstar Digital Growth LLC")
    return html


def process_thank_you(html: str, offer_id: str, cfg: dict, net, chrome) -> str:
    src_ty = html
    geo, lang = cfg["geo"], cfg["lang"]
    slug = f"luno-{offer_id}"
    price, currency = cfg["price"], cfg["currency"]
    cpa = net.CPA[offer_id]
    price_s = fmt_price(price, currency)

    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)

    html = html.replace("Driovo™", "LUNO™").replace("Driovo", "LUNO")
    html = html.replace("shoproomdock.com", "homeshopspot.com").replace("shoproomdock", "homeshopspot")
    html = re.sub(r'lang="[a-z]{2}"', f'lang="{lang}"', html, count=1)

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

    html = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        f"""window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{currency}',
  PRICE: {price},
  CONVERSION_VALUE: {cpa},
  CONVERSION_CURRENCY: 'EUR',
  COOKIE_TEXT: '…',
  COOKIE_ACCEPT: '…',
  COOKIE_LEARN: '…'
}};""",
        html,
        count=1,
    )

    cookie = re.search(
        r"COOKIE_TEXT: '([^']*)',\s*COOKIE_ACCEPT: '([^']*)',\s*COOKIE_LEARN: '([^']*)'",
        src_ty,
    )
    if cookie:
        html = re.sub(
            r"  COOKIE_TEXT: '[^']*',\s*COOKIE_ACCEPT: '[^']*',\s*COOKIE_LEARN: '[^']*'",
            f"  COOKIE_TEXT: '{cookie.group(1)}',\n  COOKIE_ACCEPT: '{cookie.group(2)}',\n  COOKIE_LEARN: '{cookie.group(3)}'",
            html,
            count=1,
        )

    html = re.sub(r"PRODUCT_SLUG:\s*'[^']*'", f"PRODUCT_SLUG: '{slug}'", html, count=1)
    html = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", html, count=1)
    html = re.sub(r"\(\d+[\d\s.,]*(?:€|Ft|Kč|zł)[^)]*\)", f"({price_s})", html)
    html = re.sub(
        r"fbq\('track', 'Purchase', \{[\s\S]*?\}\);",
        f"fbq('track', 'Purchase', {{ value: {cpa:.2f}, currency: 'EUR' }});",
        html,
        count=1,
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

    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        build_footer(geo, lang, chrome).split("<script src=\"/assets/js/glacierair-landing.js\"")[0].rstrip()
        + "</footer>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    timing = load_mod("_luno_timing", Path(__file__).with_name("_luno_timing.py"))
    html = timing.patch_ty_step3(html, lang, price_s)

    return html


def write_index(cfg: dict, offer_id: str) -> str:
    geo, lang = cfg["geo"], cfg["lang"]
    slug = f"luno-{offer_id}"
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
<p><a href="/{geo}/{slug}/landing.html">LUNO™</a></p>
</body>
</html>
"""


def main() -> None:
    net = load_mod("luno_network_forms", Path(__file__).with_name("luno_network_forms.py"))
    chrome = load_mod("_luno_chrome", Path(__file__).with_name("_luno_chrome.py"))

    for offer_id, cfg in OFFERS.items():
        geo = cfg["geo"]
        slug = f"luno-{offer_id}"
        landing = fetch(f"{SRC}/{geo}/driovo-{offer_id}/")
        ty = fetch(f"{SRC}/{geo}/driovo-{offer_id}/thank-you/")

        landing = process_landing(landing, offer_id, cfg, net, chrome)
        ty = process_thank_you(ty, offer_id, cfg, net, chrome)

        out = ROOT / geo / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / "landing.html").write_text(landing, encoding="utf-8", newline="\n")
        (out / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
        (out / "index.html").write_text(write_index(cfg, offer_id), encoding="utf-8", newline="\n")
        print(f"OK {geo}/{slug}/  #{offer_id}")


if __name__ == "__main__":
    main()
    import subprocess
    import sys

    patch_script = Path(__file__).with_name("patch_luno_geos.py")
    subprocess.run([sys.executable, str(patch_script)], check=True)
