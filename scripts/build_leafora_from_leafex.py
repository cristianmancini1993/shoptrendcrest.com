#!/usr/bin/env python3
"""Build LEAFORA IT landing from shopterva LEAFEX clone."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "it/leafora"


def brand(html: str) -> str:
    html = html.replace("LEAFEX™", "LEAFORA™")
    html = html.replace("LEAFEX", "LEAFORA")
    html = html.replace("leafex-1650", "leafora")
    html = html.replace("PRODUCT_SLUG: 'leafex-1650'", "PRODUCT_SLUG: 'leafora'")
    html = html.replace("/assets/img/products/leafex/", "/assets/img/products/leafora/")
    html = html.replace("shopterva.com", "shoptrendcrest.com")
    html = html.replace("info@shopterva.com", "info@shoptrendcrest.com")
    html = html.replace("shopterva", "shoptrendcrest")
    html = html.replace("AW-18420045673", "AW-18510622150")
    html = html.replace(
        "https://gadgetvistapro.com/wp-content/uploads/2026/07/reviewer-2.webp",
        "/assets/img/products/leafora/avatar-2.webp",
    )
    html = html.replace("LP_ID: 'it-1650'", "LP_ID: 'it-leafora'")
    html = html.replace(
        "Soluzioni pratiche per casa e giardino, spedite rapidamente con pagamento alla consegna.",
        "Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.",
    )
    html = html.replace(
        "AW-18510622150/Ylq6CM78vOscEOmurs9E",
        "AW-18510622150/rPVUCJ-RiOwcELiM-89E",
    )
    return html


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    landing = brand((ROOT / "preview/leafex-source.html").read_text(encoding="utf-8"))
    ty = brand((ROOT / "preview/leafex-ty-source.html").read_text(encoding="utf-8"))
    ty = ty.replace(
        "Perfetto — il tuo ordine è in elaborazione. Per completarlo e avviare la spedizione manca solo la <strong>conferma telefonica</strong>.",
        "Perfetto — il tuo ordine LEAFORA™ è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
    )
    ty = ty.replace(
        'content="Il tuo ordine LEAFORA™ è stato registrato. Manca solo un passo: rispondi alla chiamata del nostro operatore per confermare i dati."',
        'content="Il tuo ordine LEAFORA™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore."',
    )

    (OUT / "landing.html").write_text(landing, encoding="utf-8")
    (OUT / "thank-you.html").write_text(ty, encoding="utf-8")
    (OUT / "index.html").write_text(
        """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {
  var path = '/it/leafora/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
})();
</script>
<meta http-equiv="refresh" content="0;url=/it/leafora/landing.html">
<link rel="canonical" href="https://shoptrendcrest.com/it/leafora/landing.html">
</head>
<body>
<p><a href="/it/leafora/landing.html">LEAFORA™</a></p>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
