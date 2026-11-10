#!/usr/bin/env python3
"""One-off helper: rebuild scripts/templates/leafora_it_*.html from it/leafora-1650/."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TPL = Path(__file__).resolve().parent / "templates"


def main() -> None:
    landing = (ROOT / "it/leafora-1650/index.html").read_text(encoding="utf-8")
    ty = (ROOT / "it/leafora-1650/thank-you/index.html").read_text(encoding="utf-8")

    landing = landing.replace(
        "https://shoptrendcrest.com/it/leafora-1650/",
        "https://shoptrendcrest.com/it/leafora/landing.html",
    )
    landing = landing.replace("PRODUCT_SLUG: 'leafora-1650'", "PRODUCT_SLUG: 'leafora'")
    landing = landing.replace("LP_ID: 'it-leafora-1650'", "LP_ID: 'it-leafora'")
    landing = landing.replace(
        'thankyoupage" type="hidden" value="https://shoptrendcrest.com/it/leafora-1650/thank-you/"',
        'thankyoupage" type="hidden" value="https://shoptrendcrest.com/it/leafora/thank-you.html"',
    )
    landing = landing.replace("79,99 €", "79,99€")
    landing = landing.replace("159,98 €", "159,98€")
    landing = landing.replace(
        "⚡ PROMO SPECIALE -50% · SPEDIZIONE 48H · PAGAMENTO ALLA CONSEGNA",
        "⚡ PROMO SPECIALE -50% · CONSEGNA IN CIRCA 3 GIORNI LAVORATIVI · PAGAMENTO ALLA CONSEGNA",
    )
    landing = landing.replace(
        "<h4>Consegna 48h</h4><p>Spedizione rapida in tutta Italia</p>",
        "<h4>Consegna in 3 giorni lavorativi</h4><p>Dopo conferma telefonica in tutta Italia</p>",
    )
    landing = landing.replace(
        "<li>Spedizione 48h e pagamento alla consegna</li>",
        "<li>Spedizione in circa 3 giorni lavorativi e pagamento alla consegna</li>",
    )
    landing = landing.replace(
        "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.",
        "Prodotti utili per la vita quotidiana, consegna in circa 3 giorni lavorativi con pagamento alla consegna.",
    )
    landing = re.sub(
        r"<script>\s*\(function \(\) \{.*?leafora-\(\\d\+\).*?\}\)\(\);\s*</script>\s*",
        "",
        landing,
        flags=re.DOTALL,
    )

    ty = ty.replace(
        "https://shoptrendcrest.com/it/leafora-1650/thank-you/",
        "https://shoptrendcrest.com/it/leafora/thank-you.html",
    )
    ty = ty.replace("PRODUCT_SLUG: 'leafora-1650'", "PRODUCT_SLUG: 'leafora'")
    ty = ty.replace(
        "<li>Il tuo ordine sarà preparato in <strong>24–48 ore</strong></li>",
        "<li>Il tuo ordine sarà spedito entro <strong>3 giorni lavorativi</strong> dalla conferma telefonica</li>",
    )
    ty = ty.replace(
        "<li>Ricevi a casa e <strong>paghi alla consegna</strong></li>",
        "<li>Ricevi a casa e <strong>paghi alla consegna</strong> (79,99€)</li>",
    )
    if 'rel="canonical"' not in ty:
        ty = ty.replace(
            '<meta name="robots"',
            '<link rel="canonical" href="https://shoptrendcrest.com/it/leafora/thank-you.html">\n<meta name="robots"',
            1,
        )

    TPL.mkdir(parents=True, exist_ok=True)
    (TPL / "leafora_it_landing.html").write_text(landing, encoding="utf-8")
    (TPL / "leafora_it_thank_you.html").write_text(ty, encoding="utf-8")
    print("Wrote", TPL / "leafora_it_landing.html")
    print("Wrote", TPL / "leafora_it_thank_you.html")


if __name__ == "__main__":
    main()
