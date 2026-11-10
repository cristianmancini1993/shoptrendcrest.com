#!/usr/bin/env python3
"""Build homeshopspot IT LUNO offer #1897 landing + thank-you from it/luno templates."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from luno_network_forms import (  # noqa: E402
    ACTION,
    CPA,
    FORMS,
    OFFER_ID,
    PRICE_EUR,
    SCRIPT,
    SLUG,
    UID,
    WAS_EUR,
    WEBHOOK,
)

GEO = "it"
SRC_LANDING = ROOT / GEO / "luno" / "landing.html"
SRC_TY = ROOT / GEO / "luno" / "thank-you.html"
OUT_DIR = ROOT / GEO / SLUG
BASE = "https://homeshopspot.com"


def form_block(ty_url: str) -> str:
    net = FORMS[OFFER_ID]
    return f"""        <form class="tm-order-form order-form" action="{ACTION}" method="post">
          <label for="name">Nome e cognome*</label>
          <input id="name" type="text" name="name" autocomplete="name" placeholder="Mario Rossi" required><br>
          <label for="tel">Numero di telefono*</label>
          <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+39 333 123 4567" required><br>
          <label for="street-address">Indirizzo di consegna*</label>
          <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Via Roma 10, 00100 Roma" required><br>
          <input name="uid" type="hidden" value="{UID}" />
          <input name="offer" type="hidden" value="{OFFER_ID}" />
          <input name="lp" type="hidden" value="{net['lp']}" />
          <input name="thankyoupage" type="hidden" value="{ty_url}" />
          <input name="webhook" type="hidden" value="{WEBHOOK}" />
          <input name="_key" type="hidden" value="{net['key']}" />
          <div style="margin-top:10px;text-align:center">
            <button name="submit" type="submit">INVIA LA RICHIESTA</button>
          </div>
          <p class="form-note">🔒 Nessun anticipo · Nessuna carta · Paghi al corriere</p>
          <script src="{SCRIPT}" async></script>
        </form>"""


def patch_landing(html: str) -> str:
    ty = f"{BASE}/{GEO}/{SLUG}/thank-you.html"
    landing = f"{BASE}/{GEO}/{SLUG}/landing.html"

    html = html.replace("/it/luno/", f"/{GEO}/{SLUG}/")
    html = html.replace("it/luno/", f"{GEO}/{SLUG}/")
    html = re.sub(r"<meta charset=\"UTF-8\">", '<meta charset="UTF-8">\n<meta name="offer-id" content="1897">', html, count=1)

    html = re.sub(
        r"window\.SITE_CONFIG = \{[\s\S]*?\};",
        f"""window.SITE_CONFIG = {{
  GEO: '{GEO}',
  PRODUCT_SLUG: '{SLUG}',
  OFFER_ID: '{OFFER_ID}',
  CURRENCY: 'EUR',
  PRICE: {PRICE_EUR},
  OFFER_NAME: 'LUNO {OFFER_ID}',
  LP_ID: '{GEO}-{SLUG}',
  FORM_ENDPOINT: '{ACTION}',
  SUBMITTING_LABEL: 'Invio in corso...',
  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',
  COOKIE_ACCEPT: 'Accetta',
  COOKIE_REJECT: 'Rifiuta',
  COOKIE_LEARN: 'Scopri di più'
}};""",
        html,
        count=1,
    )

    html = html.replace("<script src=\"/assets/js/form-handler.js\" defer></script>\n", "")
    if "main.js" not in html:
        html = html.replace(
            "<script src=\"/assets/js/tracking.js\" defer></script>",
            "<script src=\"/assets/js/tracking.js\" defer></script>\n<script src=\"/assets/js/main.js\" defer></script>",
        )

    html = re.sub(r"<span class=\"was\">[^<]+</span>", f'<span class="was">{WAS_EUR:.2f} €</span>'.replace(".", ","), html)
    html = re.sub(r"<span class=\"now\">[^<]+</span>", '<span class="now">79,99 €</span>', html)
    html = re.sub(r"a 74€", "a 79,99 €", html)
    html = re.sub(r">74€<", ">79,99 €<", html)
    html = re.sub(r">148€<", ">159,98 €<", html)

    html = html.replace("placeholder=\"+39 312 345 6789\"", 'placeholder="+39 333 123 4567"')
    html = html.replace("placeholder=\"Via Roma 45, Interno 12, 00100 Roma\"", 'placeholder="Via Roma 10, 00100 Roma"')
    html = html.replace("«Sul stendino", "«Sullo stendino")

    form_pat = re.compile(
        r"<form class=\"cod-form tm-order-form order-form\">[\s\S]*?</form>",
        re.MULTILINE,
    )
    html = form_pat.sub(form_block(ty), html, count=1)

    html = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{landing}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]+">', f'<meta property="og:url" content="{landing}">', html)

    tail = f"""
<script>
(function () {{
  var m = location.pathname.match(/\\/luno-(\\d+)(?:\\/|$)/);
  if (!m) return;
  var id = m[1];
  document.querySelectorAll('input[name="offer"]').forEach(function (el) {{ el.value = id; }});
  if (window.SITE_CONFIG) {{
    window.SITE_CONFIG.OFFER_ID = id;
    window.SITE_CONFIG.OFFER_NAME = 'LUNO ' + id;
  }}
}})();
</script>
"""
    if "luno-(\\d+)" not in html:
        html = html.replace("</body>", tail + "\n</body>")

    return html


def patch_thankyou(html: str) -> str:
    price = "79,99 €"
    html = html.replace("PRODUCT_SLUG: 'luno'", f"PRODUCT_SLUG: '{SLUG}'")
    html = html.replace("PRICE: 74,", f"PRICE: {PRICE_EUR},")
    html = re.sub(r"CONVERSION_VALUE: [\d.]+", f"CONVERSION_VALUE: {PRICE_EUR}", html)
    html = re.sub(r"value: [\d.]+,\s*\n\s*currency: 'EUR'", f"value: {PRICE_EUR},\n  currency: 'EUR'", html)
    html = html.replace("(74 €)", f"({price})")
    html = html.replace("🛡️ Garanzia 3 anni", "↩️ Reso entro 30 giorni")
    return html


def write_index_redirect() -> None:
    idx = f"""<!DOCTYPE html>
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
<link rel="canonical" href="{BASE}/{GEO}/{SLUG}/landing.html">
</head>
<body>
<p><a href="/{GEO}/{SLUG}/landing.html">LUNO™</a></p>
</body>
</html>
"""
    (OUT_DIR / "index.html").write_text(idx, encoding="utf-8")


def main() -> None:
    if not SRC_LANDING.is_file():
        raise SystemExit(f"Missing template: {SRC_LANDING}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    landing = patch_landing(SRC_LANDING.read_text(encoding="utf-8"))
    (OUT_DIR / "landing.html").write_text(landing, encoding="utf-8")

    if SRC_TY.is_file():
        ty = patch_thankyou(SRC_TY.read_text(encoding="utf-8"))
        (OUT_DIR / "thank-you.html").write_text(ty, encoding="utf-8")

    write_index_redirect()
    print(f"OK {GEO}/{SLUG}/  offer #{OFFER_ID}  €{PRICE_EUR}  CPA €{CPA[OFFER_ID]:g} (not shown on page)")


if __name__ == "__main__":
    main()
