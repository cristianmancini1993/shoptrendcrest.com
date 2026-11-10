#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("gen_warmio_geos.py")
t = p.read_text(encoding="utf-8")
repls = [
    ("Generate TAIGOR™ mini chainsaw", "Generate WARMIO™ wall unit heater landings"),
    ('IT_PRICE_WAS = "140€"', 'IT_PRICE_WAS = "138€"'),
    ("taigor_network_forms", "warmio_network_forms"),
    ("_taigor_it_strings", "_warmio_it_strings"),
    ("_taigor_i18n", "_warmio_i18n"),
    ('IT_CTA_LITERAL = "ACQUISTA TAIGOR™ A 69€ →"', 'IT_CTA_LITERAL = "ORDINA WARMIO™ →"'),
    (
        'IT_FAQ2_A = "No. 69€ in contanti al corriere quando ti consegna TAIGOR™."',
        'IT_FAQ2_A = "Alla consegna: 69€ in contanti al corriere quando ricevi il pacco."',
    ),
    ('"slug": "taigor"', '"slug": "warmio"'),
    ("taigor-", "warmio-"),
    ("TAIGOR™", "WARMIO™"),
    ("TAIGOR ", "WARMIO "),
    ("/it/taigor/", "/it/warmio/"),
    (
        "https://shoptrendcrest.com/it/taigor/thank-you.html",
        "https://shoptrendcrest.com/it/warmio/thank-you/",
    ),
    ("LP_ID: 'it-taigor-v1'", "LP_ID: 'it-warmio-hgs'"),
    ("OFFER_NAME: 'TAIGOR IT'", "OFFER_NAME: 'WARMIO IT'"),
]
for a, b in repls:
    t = t.replace(a, b)
p.write_text(t, encoding="utf-8")
print("patched")
