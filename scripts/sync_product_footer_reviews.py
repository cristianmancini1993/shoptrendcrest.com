#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add reviews-summary + standardized site footer blurb on product landings."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = frozenset(
    {
        "bg",
        "cz",
        "de",
        "ee",
        "en",
        "es",
        "fr",
        "gr",
        "hr",
        "hu",
        "it",
        "lt",
        "lv",
        "pl",
        "pt",
        "ro",
        "si",
        "sk",
    }
)

POLICY_PAGES = frozenset(
    {
        "about-us.html",
        "contact-us.html",
        "privacy-policy.html",
        "terms-conditions.html",
        "cookie-policy.html",
        "shipping-policy.html",
        "refund-policy.html",
    }
)

FOOTER_BLURB: dict[str, str] = {
    "en": "Curated products for home, garden, and everyday life. Cash on delivery across 18 European countries.",
    "it": "Prodotti selezionati per casa, giardino e vita quotidiana. Pagamento alla consegna in 18 paesi europei.",
    "de": "Ausgewählte Produkte für Haus, Garten und Alltag. Zahlung per Nachnahme in 18 europäischen Ländern.",
    "es": "Productos seleccionados para el hogar, el jardín y la vida diaria. Pago contra reembolso en 18 países europeos.",
    "fr": "Produits sélectionnés pour la maison, le jardin et le quotidien. Paiement à la livraison dans 18 pays européens.",
    "pt": "Produtos selecionados para casa, jardim e dia a dia. Pagamento à cobrança em 18 países europeus.",
    "pl": "Wybrane produkty do domu, ogrodu i codzienności. Płatność przy odbiorze w 18 krajach Europy.",
    "cz": "Vybrané produkty pro domov, zahradu a každodenní život. Platba na dobírku v 18 evropských zemích.",
    "sk": "Vybrané produkty pre domov, záhradu a každodenný život. Platba na dobierku v 18 európskych krajinách.",
    "hu": "Válogatott termékek otthonra, kertre és mindennapokra. Utánvétes fizetés 18 európai országban.",
    "ro": "Produse alese pentru casă, grădină și viața de zi cu zi. Plată la livrare în 18 țări europene.",
    "hr": "Odabrani proizvodi za dom, vrt i svakodnevicu. Plaćanje pouzećem u 18 europskih zemalja.",
    "si": "Izbrani izdelki za dom, vrt in vsakdan. Plačilo po povzetju v 18 evropskih državah.",
    "lt": "Atrinkti produktai namams, sodui ir kasdienai. Apmokėjimas pristatymo metu 18 Europos šalių.",
    "lv": "Izvēlēti produkti mājai, dārzam un ikdienai. Apmaksa saņemšanas brīdī 18 Eiropas valstīs.",
    "bg": "Подбрани продукти за дома, градината и ежедневието. Плащане при доставка в 18 европейски държави.",
    "gr": "Επιλεγμένα προϊόντα για το σπίτι, τον κήπο και την καθημερινότητα. Αντικαταβολή σε 18 ευρωπαϊκές χώρες.",
    "ee": "Valitud tooted koju, aeda ja igapäevaseks kasutamiseks. Sularaha kohaletoimetamisel 18 Euroopa riigis.",
}

REVIEWS_SCORE: dict[str, str] = {
    "en": "4.8",
    "ee": "4.8",
    "hr": "4.8",
    "lv": "4.8",
}

REVIEWS_COUNT: dict[str, str] = {
    "en": "Based on 3,842 verified customer reviews",
    "it": "Basato su 3.842 recensioni verificate dei clienti",
    "de": "Basierend auf 3.842 verifizierten Kundenbewertungen",
    "es": "Basado en 3.842 opiniones verificadas de clientes",
    "fr": "Basé sur 3 842 avis clients vérifiés",
    "pt": "Com base em 3.842 avaliações verificadas de clientes",
    "pl": "Na podstawie 3.842 zweryfikowanych opinii klientów",
    "cz": "Na základě 3.842 ověřených recenzí zákazníků",
    "sk": "Na základe 3.842 overených recenzií zákazníkov",
    "hu": "3.842 ellenőrzött vásárlói értékelés alapján",
    "ro": "Pe baza a 3.842 de recenzii verificate ale clienților",
    "hr": "Na temelju 3.842 provjerenih recenzija kupaca",
    "si": "Na podlagi 3.842 preverjenih ocen strank",
    "lt": "Remiantis 3.842 patikrintais klientų atsiliepimais",
    "lv": "Balstoties uz 3.842 pārbaudītām klientu atsauksmēm",
    "bg": "Въз основа на 3.842 проверени отзива на клиенти",
    "gr": "Με βάση 3.842 επαληθευμένες κριτικές πελατών",
    "ee": "Based on 3,842 verified customer reviews",
}

LANG_RE = re.compile(r'<html[^>]+lang=["\']([a-z]{2})', re.IGNORECASE)
FOOTER_OPEN = '<footer class="site-footer">'
FOOTER_BROKEN = '<footer class=\\"site-footer\\">'

FOOTER_RE = re.compile(r'<footer class="site-footer"[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)
BLURB_RE = re.compile(
    r'<p(?:\s+class="site-footer__blurb"|\s+style="margin-top:1rem;max-width:340px")[^>]*>.*?</p>',
    re.DOTALL | re.IGNORECASE,
)


def detect_geo(path: Path, html: str) -> str:
    for part in path.parts:
        if part in GEOS:
            return part
    m = LANG_RE.search(html)
    if m and m.group(1) in GEOS:
        return m.group(1)
    return "en"


def is_product_page(path: Path, html: str) -> bool:
    if path.name in POLICY_PAGES:
        return False
    if path.parts == ("index.html",):
        return False
    if any(x in path.parts for x in ("archive", "preview", "scripts", "node_modules")):
        return False
    if "site-footer" not in html:
        return False
    if "PRODUCT_SLUG" in html or "rating-strip" in html or "noreva-lp" in html:
        return True
    if any(
        needle in html
        for needle in (
            "/assets/css/landing.css",
            "glacierair-landing.css",
            "noreva-landing.css",
            "cod-form",
            "tm-order-form",
        )
    ):
        return True
    if len(path.parts) >= 2 and path.parts[0] in GEOS:
        if path.name in {"landing.html", "index.html", "thank-you.html", "t.html"}:
            return True
        if len(path.parts) >= 3 and path.parts[-2] == "thank-you" and path.name == "index.html":
            return True
    return False


def reviews_block(locale: str) -> str:
    score = REVIEWS_SCORE.get(locale, "4,8")
    count = REVIEWS_COUNT.get(locale, REVIEWS_COUNT["en"])
    return (
        '\n<section class="reviews-summary" aria-label="Customer reviews">\n'
        f'  <div class="reviews-summary__score">{score}</div>\n'
        '  <div class="reviews-summary__stars" aria-hidden="true">★★★★★</div>\n'
        f'  <div class="reviews-summary__count">{count}</div>\n'
        "</section>\n"
    )


def normalize_footer(footer: str, locale: str) -> str:
    blurb = FOOTER_BLURB.get(locale, FOOTER_BLURB["en"])
    new_blurb = f'<p class="site-footer__blurb">{blurb}</p>'
    if BLURB_RE.search(footer):
        footer = BLURB_RE.sub(new_blurb, footer, count=1)
    else:
        footer = re.sub(
            r"(</a>\s*)",
            r"\1\n        " + new_blurb + "\n",
            footer,
            count=1,
        )
    return footer


def transform_html(html: str, path: Path) -> str:
    html = html.replace(FOOTER_BROKEN, FOOTER_OPEN)
    if not is_product_page(path, html):
        return html
    locale = detect_geo(path, html)

    if "reviews-summary" not in html:
        html = re.sub(
            r'(\s*)<footer class="site-footer"',
            reviews_block(locale) + r'\1<footer class="site-footer"',
            html,
            count=1,
            flags=re.IGNORECASE,
        )

    def repl_footer(match: re.Match[str]) -> str:
        return normalize_footer(match.group(0), locale)

    return FOOTER_RE.sub(repl_footer, html)


def main() -> None:
    changed: list[Path] = []
    for path in ROOT.rglob("*.html"):
        if any(x in path.parts for x in ("archive", "preview", "node_modules", "scripts")):
            continue
        original = path.read_text(encoding="utf-8")
        updated = transform_html(original, path.relative_to(ROOT))
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)
    print(f"Updated {len(changed)} product HTML files")


if __name__ == "__main__":
    main()
