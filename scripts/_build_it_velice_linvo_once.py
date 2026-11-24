# -*- coding: utf-8 -*-
"""Copy IT VELICE BF landing from devicevaultspot template into shoptrendcrest.com."""
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(r"e:\WORK\Landings\devicevaultspot.com")
DST = Path(__file__).resolve().parents[1]
OLD_DOM = "devicevaultspot.com"
NEW_DOM = "shoptrendcrest.com"
OLD_EMAIL = "info@devicevaultspot.com"
NEW_EMAIL = "info@shoptrendcrest.com"

FOOTER_BLOCK = """<footer class="site-footer">
  <div class="container">
    <div class="site-footer__top">
      <p class="site-footer__top-meta">shoptrendcrest.com — Offerto da CAPITALADV S.R.L.</p>
    </div>
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="shoptrendcrest.com home">
          <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">shoptrendcrest</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.</p>
        <p class="site-footer__ai-notice" data-ai-disclosure="1">Alcune immagini in questa pagina sono state generate o modificate con intelligenza artificiale e hanno solo scopo illustrativo. Potrebbero non corrispondere fedelmente all’aspetto reale del prodotto, alle dimensioni, ai colori, alle caratteristiche o alle prestazioni.</p>
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
        <ul class="site-footer__list"><li><a href="mailto:info@shoptrendcrest.com">info@shoptrendcrest.com</a></li></ul>
      </div>
    </div>
    <div class="site-footer__company">
      <p class="site-footer__company-name"><strong>CAPITALADV S.R.L.</strong></p>
      <p class="site-footer__company-line">CORSO BUENOS AIRES 64</p>
      <p class="site-footer__company-line">20124 Milano</p>
      <p class="site-footer__company-line">Italy</p>
    </div>
    <div class="site-footer__bottom">© <span data-year>2026</span> shoptrendcrest.com — Offerto da CAPITALADV S.R.L.. Tutti i diritti riservati.</div>
  </div>
</footer>"""


def transform_landing(text: str) -> str:
    text = text.replace(f"https://{OLD_DOM}", f"https://{NEW_DOM}")
    text = text.replace(OLD_DOM, NEW_DOM)
    text = text.replace(OLD_EMAIL, NEW_EMAIL)
    text = text.replace("AW-18544572311", "AW-18510622150")
    text = text.replace("OFFER_NAME: 'Velice IT Impasti Casa'", "OFFER_NAME: 'VELICE IT'")
    text = text.replace(
        "/assets/css/orbimix-landing-alt.css?v=20261123kit2",
        "/assets/css/orbimix-landing-alt-velice.css?v=20261123kit2",
    )
    text = re.sub(r'<footer class="site-footer">.*?</footer>', FOOTER_BLOCK, text, count=1, flags=re.DOTALL)
    return text


def transform_ty(text: str) -> str:
    text = text.replace(f"https://{OLD_DOM}", f"https://{NEW_DOM}")
    text = text.replace(OLD_DOM, NEW_DOM)
    text = text.replace(OLD_EMAIL, NEW_EMAIL)
    text = text.replace("AW-18544572311", "AW-18510622150")
    text = text.replace("Il team devicevaultspot", "Team shoptrendcrest")
    text = text.replace("Equipo devicevaultspot", "Team shoptrendcrest")
    text = text.replace(
        'aria-label="devicevaultspot.com home"',
        'aria-label="shoptrendcrest.com home"',
    )
    text = re.sub(
        r'<span class="site-logo__text"><span class="site-logo__text-primary">devicevaultspot</span>'
        r'<span class="site-logo__text-accent">\.com</span></span>',
        '<span class="site-logo__text"><span class="site-logo__text-primary">shoptrendcrest</span>'
        r'<span class="site-logo__text-accent">.com</span></span>',
        text,
    )
    text = re.sub(
        r'<span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">devicevaultspot</span>'
        r'<span class="site-logo__text-accent">\.com</span></span>',
        '<span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">shoptrendcrest</span>'
        r'<span class="site-logo__text-accent">.com</span></span>',
        text,
    )
    text = text.replace(
        'site-footer__powered">devicevaultspot.com — Gestito da',
        'site-footer__top-meta">shoptrendcrest.com — Offerto da',
    )
    text = text.replace("devicevaultspot.com — Gestito da", "shoptrendcrest.com — Offerto da")
    text = text.replace("Gestito da", "Offerto da")
    text = re.sub(
        r"<script>\s*gtag\('event', 'conversion'.*?</script>\s*",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )
    return text


def main() -> None:
    out_dir = DST / "it" / "velice"
    out_dir.mkdir(parents=True, exist_ok=True)

    landing = transform_landing((SRC / "it/velice/landing.html").read_text(encoding="utf-8"))
    (out_dir / "landing.html").write_text(landing, encoding="utf-8")

    ty = transform_ty((SRC / "it/velice/thank-you.html").read_text(encoding="utf-8"))
    (out_dir / "thank-you.html").write_text(ty, encoding="utf-8")

    index = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/it/velice/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/it/velice/landing.html">
<link rel="canonical" href="https://{NEW_DOM}/it/velice/landing.html">
</head>
<body>
<p><a href="/it/velice/landing.html">VELICE™</a></p>
</body>
</html>
"""
    (out_dir / "index.html").write_text(index, encoding="utf-8")
    print("OK:", out_dir)


if __name__ == "__main__":
    main()