#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("gen_granvia_geos.py")
t = p.read_text(encoding="utf-8")
repl = [
    ('"""Generate CENDORA™', '"""Generate Granvia™'),
    ("IT_PRICE_NOW = \"74€\"", "IT_PRICE_NOW = \"89€\""),
    ("IT_PRICE_WAS = \"148€\"", "IT_PRICE_WAS = \"178€\""),
    ('IT_CTA_LITERAL = "VOGLIO CENDORA™ →"', 'IT_CTA_LITERAL = "VOGLIO GRANVIA™ →"'),
    ("cendora_network_forms", "granvia_network_forms"),
    ("_cendora_it_strings", "_granvia_it_strings"),
    ("content/cendora", "content/granvia"),
    ('return f"cendora-{offer}"', 'return f"granvia-{offer}"'),
    ("def public_landing_url(geo: str, offer: str) -> str:\n    return f\"https://shoptrendcrest.com{public_base_path(geo, offer)}/\"", ""),
]
for a, b in repl:
    if a not in t:
        raise SystemExit(f"missing: {a[:60]}")
    t = t.replace(a, b)

t = t.replace(
    'def public_landing_url(geo: str, offer: str) -> str:\n    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/"\n\n\ndef public_thankyou_url',
    'def public_landing_url(geo: str, offer: str) -> str:\n    site = json.loads((ROOT / "content/granvia/site.json").read_text(encoding="utf-8"))\n    domain = site["domain"]\n    return f"https://{domain}{public_base_path(geo, offer)}/"\n\n\ndef public_thankyou_url',
)
t = t.replace(
    'def public_thankyou_url(geo: str, offer: str) -> str:\n    return f"https://shoptrendcrest.com{public_base_path(geo, offer)}/thank-you/"',
    'def public_thankyou_url(geo: str, offer: str) -> str:\n    site = json.loads((ROOT / "content/granvia/site.json").read_text(encoding="utf-8"))\n    domain = site["domain"]\n    return f"https://{domain}{public_base_path(geo, offer)}/thank-you/"',
)
t = t.replace("cendora_it_landing.html", "granvia_it_landing.html")
t = t.replace("cendora_it_thank_you.html", "granvia_it_thank_you.html")
t = t.replace("/cendora-(\\d+)", "/granvia-(\\\\d+)")
t = t.replace("OFFER_NAME = 'CENDORA ' + id", "OFFER_NAME = 'GRANVIA ' + id")
t = t.replace("https://shoptrendcrest.com/it/cendora/", "https://shoptrendcrest.com/it/granvia/")
t = t.replace("it/cendora/thank-you.html", "it/granvia/thank-you.html")
t = t.replace("PRODUCT_SLUG: 'cendora'", "PRODUCT_SLUG: 'granvia'")
t = t.replace("OFFER_NAME: 'CENDORA IT'", "OFFER_NAME: 'GRANVIA IT'")
t = t.replace("LP_ID: 'it-cendora-v1'", "LP_ID: 'it-granvia-v1'")
t = t.replace('html.replace("OFFER_NAME: \'CENDORA IT\'", f"OFFER_NAME: \'CENDORA {offer}\'")',
                'html.replace("OFFER_NAME: \'GRANVIA IT\'", f"OFFER_NAME: \'GRANVIA {offer}\'")')
t = t.replace("gen_cendora_geos.py", "gen_granvia_geos.py")
# remove OFFER_ID line if present
t = t.replace(
    """    html = re.sub(
        r"OFFER_ID:\\s*'[^']*'",
        f"OFFER_ID: '{offer}'",
        html,
        count=1,
    )
""",
    "",
)
t = t.replace("re.sub(r\"74€\", now, html)", "re.sub(r\"89€\", now, html)")
t = t.replace("re.sub(r\"148€\", was, html)", "re.sub(r\"178€\", was, html)")
p.write_text(t, encoding="utf-8")
print("patched gen_granvia_geos.py")
