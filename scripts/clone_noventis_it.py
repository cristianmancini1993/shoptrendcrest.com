#!/usr/bin/env python3
"""Clone shoproomdock.com IT Noventis landing into homeshopspot.com."""

import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import ai_image_notice_html

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://shoproomdock.com"
GEO = "it"
SLUG = "noventis"
OUT = ROOT / GEO / SLUG
ASSET_DIR = ROOT / "assets" / "img" / "products" / "noventis"

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

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="homeshopspot.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">Prodotti utili per la vita quotidiana, consegna in 24–48 ore e pagamento alla consegna.</p>
{ai_image_notice_html("it")}
      </div>
      <div>
        <h4 class="site-footer__heading">Informazioni</h4>
        <ul class="site-footer__list">
          <li><a href="/it/about-us.html">Chi siamo</a></li>
          <li><a href="/it/contact-us.html">Contatti</a></li>
          <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/it/terms-conditions.html">Termini e condizioni</a></li>
          <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>
          <li><a href="/it/shipping-policy.html">Spedizione</a></li>
          <li><a href="/it/refund-policy.html">Resi e rimborsi</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">Contatti</h4>
        <ul class="site-footer__list">
          <li><strong>Northstar Digital Growth LLC</strong></li>
          <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
          <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — Tutti i diritti riservati.
      <a href="/">homeshopspot.com</a>
    </div>
  </div>
</footer>"""

TY_FOOTER = f"""<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div>
      <a href="/" class="site-logo">
        <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
      </a>
{ai_image_notice_html("it")}
    </div>
    <div>
      <h4 class="site-footer__heading">Informazioni</h4>
      <ul class="site-footer__list">
        <li><a href="/it/about-us.html">Chi siamo</a></li>
        <li><a href="/it/contact-us.html">Contattaci</a></li>
        <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>
        <li><a href="/it/terms-conditions.html">Termini e Condizioni</a></li>
        <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>
        <li><a href="/it/shipping-policy.html">Politica di spedizione</a></li>
        <li><a href="/it/refund-policy.html">Politica di reso</a></li>
      </ul>
    </div>
    <div>
      <h4 class="site-footer__heading">Contatti</h4>
      <ul class="site-footer__list">
        <li><strong>Northstar Digital Growth LLC</strong></li>
        <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
        <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — Tutti i diritti riservati. <a href="/">homeshopspot.com</a></div>
</div></footer>"""


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-clone/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


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
    return html


def homeshopspotify(html: str) -> str:
    html = html.replace("shoproomdock.com", "homeshopspot.com")
    html = html.replace("info@shoproomdock.com", "info@homeshopspot.com")
    html = html.replace("shoproomdock", "homeshopspot")
    html = html.replace("The Lead Empire L.L.C-FZ", "Northstar Digital Growth LLC")
    html = html.replace(
        "Meydan Grandstand, 6th floor, Meydan Road, Dubai, Emiratos Árabes Unidos",
        "32 N Gould St., Sheridan, WY 82801, Statele Unite",
    )
    ty_url = f"https://homeshopspot.com/{GEO}/{SLUG}/thank-you.html"
    html = re.sub(
        r'value="https://homeshopspot\.com/it/noventis/thank-you\.html"',
        f'value="{ty_url}"',
        html,
    )
    html = html.replace(
        f"https://homeshopspot.com/it/{SLUG}/thank-you.html",
        ty_url,
    )
    html = re.sub(
        r'<link rel="canonical" href="https://homeshopspot\.com/it/noventis/">',
        f'<link rel="canonical" href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">',
        html,
        count=1,
    )
    html = re.sub(
        r"  COOKIE_TEXT: '[^']*',\s*COOKIE_ACCEPT: '[^']*',\s*COOKIE_LEARN: '[^']*'",
        "  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',\n"
        "  COOKIE_ACCEPT: 'Accetta',\n"
        "  COOKIE_LEARN: 'Scopri di più'",
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


def download_assets(html: str) -> None:
    paths = sorted(set(re.findall(r"/assets/img/products/noventis/[^\"'\\s>]+", html)))
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    for rel in paths:
        dest = ROOT / rel.lstrip("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            print("GET", rel)
            dest.write_bytes(fetch(SRC + rel))


def process_landing(html: str) -> str:
    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = homeshopspotify(html)
    if "glacierair-landing.css" not in html:
        html = html.replace(
            "</style>",
            "</style>\n<link rel=\"stylesheet\" href=\"/assets/css/glacierair-landing.css\">",
            1,
        )
    html = re.sub(
        r'<footer class="gsh-standalone-footer">.*?</footer>',
        FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )
    html += '\n<script>document.querySelectorAll(\'[data-year]\').forEach(function(el){el.textContent=String(new Date().getFullYear());});</script>\n'
    return html


def process_thank_you(html: str) -> str:
    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = homeshopspotify(html)
    html = re.sub(
        r'<a href="/" class="site-logo" aria-label="homeshopspot\.com home">.*?</a>',
        '<a href="/" class="site-logo" aria-label="homeshopspot.com home">\n'
        '      <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span>'
        '<span class="site-logo__text-accent">.com</span></span>\n    </a>',
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        'alt="Il team homeshopspot al lavoro: call center e logistica COD"',
        'alt="Il team homeshopspot al lavoro: call center e logistica COD"',
    )
    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        TY_FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )
    cpa = 15.0
    html = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", html, count=1)
    html = html + f"""

<script>
fbq('track', 'Purchase', {{
  value: {cpa:.2f},
  currency: 'EUR'
}});
</script>
"""
    return html


def main() -> None:
    landing = fetch(f"{SRC}/{GEO}/{SLUG}/").decode("utf-8")
    download_assets(landing)
    landing = process_landing(landing)

    ty = fetch(f"{SRC}/{GEO}/{SLUG}/thank-you.html").decode("utf-8")
    ty = process_thank_you(ty)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "landing.html").write_text(landing, encoding="utf-8", newline="\n")
    (OUT / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
    index = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{GEO}/{SLUG}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{GEO}/{SLUG}/landing.html">
<link rel="canonical" href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">
</head>
<body>
<p><a href="/{GEO}/{SLUG}/landing.html">Noventis™</a></p>
</body>
</html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
