# -*- coding: utf-8 -*-
"""Build it/calvor-3990/ from it/calvor/ (read-only) with campaign URLs and prices."""
from __future__ import annotations

import re
from pathlib import Path

from calvor_campaign_prices import IT_PRICE_NOW, IT_PRICE_WAS
from calvor_network_forms import FORMS

ROOT = Path(__file__).resolve().parents[1]
IT_TY_URL = "https://shoptrendcrest.com/it/calvor-3990/thank-you/"
SRC_LP = ROOT / "it/calvor/index.html"
SRC_TY = ROOT / "it/calvor/thank-you/index.html"
OUT_LP = ROOT / "it/calvor-3990/index.html"
OUT_TY = ROOT / "it/calvor-3990/thank-you/index.html"


def apply_prices(html: str) -> str:
    html = re.sub(r'<span class="was">[^<]*</span>', f'<span class="was">{IT_PRICE_WAS}</span>', html)
    html = re.sub(r'<span class="now">[^<]*</span>', f'<span class="now">{IT_PRICE_NOW}</span>', html)
    html = re.sub(
        r'<span class="ty-price-was">[^<]*</span>',
        f'<span class="ty-price-was">{IT_PRICE_WAS}</span>',
        html,
    )
    html = re.sub(
        r'<span class="ty-price-now">[^<]*</span>',
        f'<span class="ty-price-now">{IT_PRICE_NOW}</span>',
        html,
    )
    html = html.replace("138 €", IT_PRICE_WAS)
    html = html.replace("69 €", IT_PRICE_NOW)
    html = html.replace("138\u00a0€", IT_PRICE_WAS)
    html = html.replace("69\u00a0€", IT_PRICE_NOW)
    return html


def patch_campaign(html: str) -> str:
    html = html.replace("/it/calvor/", "/it/calvor-3990/")
    html = html.replace("https://shoptrendcrest.com/it/calvor/", "https://shoptrendcrest.com/it/calvor-3990/")
    html = html.replace("PRODUCT_SLUG: 'calvor'", "PRODUCT_SLUG: 'calvor-3990'")
    html = html.replace("LP_ID: 'it-calvor'", "LP_ID: 'it-calvor-3990'")
    html = html.replace("OFFER_NAME: 'Calvor IT'", "OFFER_NAME: 'Calvor IT 3990'")
    return html


def apply_order_form(html: str) -> str:
    html = re.sub(
        r'<form class="tm-order-form.*?</form>',
        FORMS["3990"],
        html,
        count=1,
        flags=re.DOTALL,
    )
    return re.sub(
        r'(<input name="thankyoupage" type="hidden" value=")[^"]*(")',
        rf"\1{IT_TY_URL}\2",
        html,
        count=1,
    )


def main() -> None:
    lp = apply_order_form(apply_prices(patch_campaign(SRC_LP.read_text(encoding="utf-8"))))
    ty = apply_prices(patch_campaign(SRC_TY.read_text(encoding="utf-8")))
    ty = re.sub(
        r'<div class="ty-summary-pay">[^<]+</div>',
        f'<div class="ty-summary-pay">Contrassegno alla consegna: {IT_PRICE_NOW}</div>',
        ty,
        count=1,
    )
    OUT_LP.parent.mkdir(parents=True, exist_ok=True)
    OUT_TY.parent.mkdir(parents=True, exist_ok=True)
    OUT_LP.write_text(lp, encoding="utf-8")
    OUT_TY.write_text(ty, encoding="utf-8")
    redirect = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0;url=/it/calvor-3990/">
<link rel="canonical" href="https://shoptrendcrest.com/it/calvor-3990/">
<title>Reindirizzamento a Calvor™</title>
<script>location.replace('/it/calvor-3990/');</script>
</head>
<body>
<p><a href="/it/calvor-3990/">Calvor™</a></p>
</body>
</html>
"""
    leg_lp = ROOT / "it/warmio-3990/index.html"
    leg_ty = ROOT / "it/warmio-3990/thank-you/index.html"
    leg_lp.parent.mkdir(parents=True, exist_ok=True)
    leg_ty.parent.mkdir(parents=True, exist_ok=True)
    red_ty = redirect.replace("/it/calvor-3990/", "/it/calvor-3990/thank-you/").replace(
        "url=/it/calvor-3990/thank-you/",
        "url=/it/calvor-3990/thank-you/",
    )
    red_ty = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0;url=/it/calvor-3990/thank-you/">
<link rel="canonical" href="https://shoptrendcrest.com/it/calvor-3990/thank-you/">
<meta name="robots" content="noindex, nofollow">
<title>Reindirizzamento</title>
<script>location.replace('/it/calvor-3990/thank-you/');</script>
</head>
<body><p><a href="/it/calvor-3990/thank-you/">Continua</a></p>
</body>
</html>
"""
    leg_lp.write_text(redirect, encoding="utf-8")
    leg_ty.write_text(red_ty, encoding="utf-8")
    print("Wrote", OUT_LP, "and", OUT_TY)


if __name__ == "__main__":
    main()