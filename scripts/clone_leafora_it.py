#!/usr/bin/env python3
"""Clone shoptrendcrest IT LEAFORA landing into homeshopspot."""

import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import ai_image_notice_html

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://shoptrendcrest.com"
GEO = "it"
SLUG = "leafora-4188"
SRC_PATH = f"{GEO}/leafora-1650"
OUT = ROOT / GEO / SLUG
ASSETS = ROOT / "assets" / "img" / "products" / "leafora"

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
</footer>
<script src="/assets/js/glacierair-landing.js" defer></script>
<script>document.querySelectorAll('[data-year]').forEach(function(el){el.textContent=String(new Date().getFullYear());});</script>"""


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-clone/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def main() -> None:
    page_url = f"{SRC}/{SRC_PATH}/"
    html = fetch(page_url).decode("utf-8")

    imgs = sorted(set(re.findall(r"/assets/img/products/leafora/[^\"']+", html)))
    ASSETS.mkdir(parents=True, exist_ok=True)
    for rel in imgs:
        dest = ROOT / rel.lstrip("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            print("GET", rel)
            dest.write_bytes(fetch(SRC + rel))

    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)

    thankyou_src = re.search(
        r'value="(https://shoptrendcrest\.com/[^"]+thank-you[^"]*)"',
        html,
    )
    if thankyou_src:
        old_ty = thankyou_src.group(1)
        new_ty = old_ty.replace(SRC, "https://homeshopspot.com").replace(
            "/thank-you/", "/thank-you.html"
        ).replace("/thank-you", "/thank-you.html")
        if not new_ty.endswith(".html"):
            new_ty = new_ty.rstrip("/") + ".html" if new_ty.endswith("/") else new_ty + ".html"
        new_ty_url = f"https://homeshopspot.com/{GEO}/{SLUG}/thank-you.html"
        html = html.replace(old_ty, new_ty_url)
    html = re.sub(
        rf'value="https://homeshopspot\.com/{GEO}/leafora-1650/thank-you/?"',
        f'value="https://homeshopspot.com/{GEO}/{SLUG}/thank-you.html"',
        html,
    )

    html = html.replace("info@shoptrendcrest.com", "info@homeshopspot.com")
    html = html.replace("https://shoptrendcrest.com", "https://homeshopspot.com")
    html = html.replace(
        f"https://homeshopspot.com/{GEO}/leafora-1650/",
        f"https://homeshopspot.com/{GEO}/{SLUG}/landing.html",
    )
    html = html.replace(
        f'<link rel="canonical" href="https://homeshopspot.com/{GEO}/leafora-1650/">',
        f'<link rel="canonical" href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">',
    )
    html = html.replace(
        f'href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html"',
        f'href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html"',
    )

    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>\s*"
        r"<script src=\"/assets/js/glacierair-landing.js\" defer></script>\s*"
        r"<script>document\.querySelectorAll\('\[data-year\]'\).*?</script>",
        FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )

    cookie_it = (
        "  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',\n"
        "  COOKIE_ACCEPT: 'Accetta',\n"
        "  COOKIE_LEARN: 'Scopri di più'"
    )
    html = re.sub(
        r"  COOKIE_TEXT: '[^']*',\s*COOKIE_ACCEPT: '[^']*',\s*COOKIE_LEARN: '[^']*'",
        cookie_it.strip(),
        html,
        count=1,
    )

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "landing.html").write_text(html, encoding="utf-8", newline="\n")

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
<p><a href="/{GEO}/{SLUG}/landing.html">LEAFORA™</a></p>
</body>
</html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8", newline="\n")

    ty_src = ROOT / GEO / "verdola" / "thank-you.html"
    ty = ty_src.read_text(encoding="utf-8")
    ty = re.sub(r"Verdola™?", "LEAFORA™", ty)
    ty = ty.replace("verdola", SLUG)
    ty = ty.replace("PRODUCT_SLUG: 'verdola'", f"PRODUCT_SLUG: '{SLUG}'")
    ty = ty.replace("OFFER_NAME: 'Verdola Tagliaerba IT'", "OFFER_NAME: 'LEAFORA 1650 IT'")
    ty = ty.replace("LP_ID: 'it-verdola-v1'", "LP_ID: 'it-leafora-v1'")
    m = re.search(r"CONVERSION_VALUE:\s*([0-9.]+)", html)
    cpa = float(m.group(1)) if m else 21.0
    ty = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", ty, count=1)
    ty = re.sub(
        r"value: [0-9.]+,\ncurrency: 'EUR'",
        f"value: {cpa:.2f},\ncurrency: 'EUR'",
        ty,
        count=1,
    )
    (OUT / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")

    print(f"Wrote {OUT.relative_to(ROOT)}/")
    print(f"Images checked: {len(imgs)}")


if __name__ == "__main__":
    main()
