#!/usr/bin/env python3
from pathlib import Path

src = Path(__file__).with_name("gen_warmio_geos.py").read_text(encoding="utf-8")
text = src.replace("WARMIO", "CENDORA").replace("warmio", "cendora")
text = text.replace("CENDORA™ wall unit heater landings landings", "CENDORA™ cookware landings")
text = text.replace('IT_PRICE_NOW = "69€"', 'IT_PRICE_NOW = "74€"')
text = text.replace('IT_PRICE_WAS = "138€"', 'IT_PRICE_WAS = "148€"')
text = text.replace('IT_CTA_LITERAL = "ORDINA CENDORA™ →"', 'IT_CTA_LITERAL = "VOGLIO CENDORA™ →"')
text = text.replace("_warmio_it_strings", "_cendora_it_strings")
text = text.replace("_warmio_i18n.py", "build_cendora_i18n.py")
text = text.replace("_warmio_i18n", "build_cendora_i18n")
text = text.replace("cendora_network_forms", "cendora_network_forms")
text = text.replace("cendora_it_landing.html", "cendora_it_landing.html")
text = text.replace(
    "https://shoptrendcrest.com/it/cendora/",
    "https://shoptrendcrest.com/it/cendora/",
)
text = text.replace(
    '<h2>Invia l\'ordine ora, prima che finisca lo stock promozionale</h2>',
    '<h2>Finalizza la richiesta</h2>',
)
text = text.replace("it-cendora-hgs", "it-cendora-v1")
text = text.replace(
    "Curated products for home, garden, and everyday life. Cash on delivery across 18 European countries.",
    "Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.",
)
text = text.replace(
    "shoptrendcrest.com — Powered by WHATECH MOBILE CO., LIMITED",
    "shoptrendcrest.com — Offerto da WHATECH MOBILE CO., LIMITED",
)
insert = '''
import json

DOMAIN = "shoptrendcrest.com"


def load_offers() -> dict[str, dict]:
    root = Path(__file__).resolve().parents[1]
    rows = json.loads((root / "content/cendora/offers.json").read_text(encoding="utf-8"))
    out = {}
    for row in rows:
        oid = str(row["id"])
        out[oid] = {
            "geo": row["geo"],
            "lang": row["lang"],
            "tr": row.get("tr", row["lang"]),
            "price": float(row["price"]),
            "currency": row["currency"],
            "slug": "cendora",
        }
    return out


GEOS = load_offers()
'''
# Replace GEOS = { ... }; block
import re

text = re.sub(r"GEOS = \{.*?\n\}\n\nLEGACY", insert + "\nLEGACY", text, count=1, flags=re.DOTALL)
text = text.replace("https://shoptrendcrest.com/it/cendora/thank-you.html", "https://shoptrendcrest.com/it/cendora/thank-you.html")
text = text.replace(
    'html.replace("ORDINA CENDORA™ →", cta)',
    'html.replace("VOGLIO CENDORA™ →", cta)',
)
# thank-you path
text = text.replace(
    "https://shoptrendcrest.com/it/cendora/thank-you.html",
    "https://shoptrendcrest.com/it/cendora/thank-you.html",
)
Path(__file__).with_name("gen_cendora_geos.py").write_text(text, encoding="utf-8")
print("ok")
