#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clone it/trimex -> it/trimex-3209 with offer #3209 and price 79.99 EUR."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "it/trimex"
OUT = ROOT / "it/trimex-3209"
OFFER_ID = "3209"
BASE = f"https://gadgetshifthub.com/it/trimex-{OFFER_ID}/"
TY = f"{BASE}thank-you.html"


def patch(html: str) -> str:
    html = html.replace(
        "https://gadgetshifthub.com/it/trimex/thank-you.html",
        TY,
    )
    html = html.replace("https://gadgetshifthub.com/it/trimex/", BASE)
    html = html.replace("PRODUCT_SLUG: 'trimex',", f"PRODUCT_SLUG: 'trimex-{OFFER_ID}',")
    html = html.replace("PRICE: 74.0,", "PRICE: 79.99,")
    html = html.replace("OFFER_NAME: 'TRIMEX IT',", f"OFFER_NAME: 'TRIMEX IT #{OFFER_ID}',")
    html = html.replace("LP_ID: 'it-trimex-v1',", f"LP_ID: 'it-{OFFER_ID}',")
    html = html.replace("FORM_OFFER: '',", f"FORM_OFFER: '{OFFER_ID}',")
    html = html.replace(
        '<input name="offer" type="hidden" value="">',
        f'<input name="offer" type="hidden" value="{OFFER_ID}">',
    )
    html = html.replace(
        'value="https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh"',
        'value=""',
    )
    html = html.replace(
        '<span class="was">148€</span><span class="now">74€</span>',
        '<span class="was">159,98€</span><span class="now">79,99€</span>',
    )
    html = html.replace("trackPurchase(74.0, 'EUR')", "trackPurchase(79.99, 'EUR')")
    if 'name="offer-id"' not in html:
        html = html.replace(
            "<meta charset",
            f'<meta name="offer-id" content="{OFFER_ID}">\n<meta charset',
            1,
        )
    marker = f"<!-- Offer #{OFFER_ID} -->"
    if marker not in html:
        html = html.replace("<body", f"{marker}\n<body", 1)
    return html


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "thank-you.html"):
        text = patch((SRC / name).read_text(encoding="utf-8"))
        (OUT / name).write_text(text, encoding="utf-8")
    print(f"Created {OUT}/index.html and thank-you.html")


if __name__ == "__main__":
    main()
