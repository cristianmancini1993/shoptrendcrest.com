from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
src = (ROOT.parent / "shopgearspot.com" / "it" / "varmo" / "index.html").read_text(encoding="utf-8")
ty_src = (ROOT.parent / "shopgearspot.com" / "it" / "varmo" / "thank-you.html").read_text(encoding="utf-8")

WARMIO_FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="https://warmio.com/" class="site-logo" aria-label="warmio.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">warmio</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">Prodotti pratici per la vita quotidiana. Ordine preparato in 24–48 ore; consegna in 2–4 giorni lavorativi con pagamento alla consegna.</p>
      </div>
      <div>
        <h4 class="site-footer__heading">Informazioni</h4>
        <ul class="site-footer__list">
          <li><a href="https://warmio.com/it/about-us.html">Chi siamo</a></li>
          <li><a href="https://warmio.com/it/contact-us.html">Contattaci</a></li>
          <li><a href="https://warmio.com/it/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="https://warmio.com/it/terms-conditions.html">Termini e Condizioni</a></li>
          <li><a href="https://warmio.com/it/cookie-policy.html">Cookie Policy</a></li>
          <li><a href="https://warmio.com/it/shipping-policy.html">Politica di spedizione</a></li>
          <li><a href="https://warmio.com/it/refund-policy.html">Politica di reso</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">Contatti</h4>
        <ul class="site-footer__list">
          <li><strong>GLOBAL INTEGRATED MARKETING COMMUNICATION GROUP HOLDINGS LIMITED</strong></li>
          <li>RM 01, 15/F, GOLDSLAND BUILDING, 22–26 MINDEN AVENUE, TSIM SHA TSUI, KOWLOON, HONG KONG</li>
          <li><a href="mailto:info@warmio.com">info@warmio.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>GLOBAL INTEGRATED MARKETING COMMUNICATION GROUP HOLDINGS LIMITED</strong> — Tutti i diritti riservati.
      <a href="https://warmio.com/">warmio.com</a>
    </div>
  </div>
</footer>"""


def swap_footer(html: str) -> str:
    m = re.search(r"<footer class=\"site-footer\">.*?</footer>", html, re.S)
    if not m:
        raise SystemExit("footer not found")
    return html[: m.start()] + WARMIO_FOOTER + html[m.end() :]


def adapt_landing(html: str) -> str:
    html = html.replace("AW-18437425584", "AW-18510622150")
    html = html.replace("VARMO", "WARMIO")
    html = html.replace("varmo", "warmio")
    html = html.replace("https://shopgearspot.com", "https://shoptrendcrest.com")
    html = html.replace("info@shopgearspot.com", "info@shoptrendcrest.com")
    html = html.replace(
        'value="https://shoptrendcrest.com/it/warmio/thank-you.html"',
        'value="https://warmio.com/it/warmio/thank-you.html"',
    )
    html = html.replace("LP_ID: 'it-warmio-v1'", "LP_ID: 'it-warmio-hgs'")
    return swap_footer(html)


def adapt_ty(html: str) -> str:
    html = html.replace("AW-18437425584", "AW-18510622150")
    html = html.replace("AW-18437425584/iRw_CISgmfIcELCT09dE", "AW-18510622150/rPVUCJ-RiOwcELiM-89E")
    html = html.replace("VARMO", "WARMIO")
    html = html.replace("varmo", "warmio")
    html = html.replace("shopgearspot.com", "warmio.com")
    html = html.replace("shopgearspot", "warmio")
    html = html.replace('content="info@warmio.com"', 'content="info@warmio.com"')
    return swap_footer(html)


base = ROOT / "it" / "warmio"
(base / "thank-you").mkdir(parents=True, exist_ok=True)
(base / "index.html").write_text(adapt_landing(src), encoding="utf-8")
(base / "thank-you" / "index.html").write_text(adapt_ty(ty_src), encoding="utf-8")
(base / "landing.html").write_text(
    """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {
  var path = '/it/warmio/';
  window.location.replace(path + window.location.search + window.location.hash);
})();
</script>
<meta http-equiv="refresh" content="0;url=/it/warmio/">
<link rel="canonical" href="https://shoptrendcrest.com/it/warmio/">
</head>
<body>
<p><a href="/it/warmio/">WARMIO™</a></p>
</body>
</html>
""",
    encoding="utf-8",
)
(base / "thank-you.html").write_text(
    """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<meta http-equiv="refresh" content="0;url=/it/warmio/thank-you/">
<script>location.replace('/it/warmio/thank-you/' + location.search + location.hash);</script>
</head>
<body><p><a href="/it/warmio/thank-you/">Thank you</a></p></body>
</html>
""",
    encoding="utf-8",
)
print("Wrote", base / "index.html")
