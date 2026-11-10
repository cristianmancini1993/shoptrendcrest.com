# -*- coding: utf-8 -*-
"""Post-gen text/kit patches for LUNO geo landings."""

# Two kit lines matching gift-strip (hangers + clips). Bag stays as existing line.
KIT_APPEND = {
    "de": (
        "          <li>1× Premium-Kleiderbügel (Gratis)</li>\n"
        "          <li>1× Multifunktions-Clips (Gratis)</li>"
    ),
    "hu": (
        "          <li>1× Prémium vállfák (ajándék)</li>\n"
        "          <li>1× Multifunkciós csipeszek (ajándék)</li>"
    ),
    "pt": (
        "          <li>1× Cabides reforçados (oferta)</li>\n"
        "          <li>1× Clips multiuso (oferta)</li>"
    ),
    "es": (
        "          <li>1× Perchas reforzadas (regalo)</li>\n"
        "          <li>1× Clips multifunción (regalo)</li>"
    ),
    "pl": (
        "          <li>1× Wzmocnione wieszaki (gratis)</li>\n"
        "          <li>1× Klipsy wielofunkcyjne (gratis)</li>"
    ),
    "cs": (
        "          <li>1× Vyztužená ramínka (zdarma)</li>\n"
        "          <li>1× Multifunkční kolíčky (zdarma)</li>"
    ),
    "lv": (
        "          <li>1× Pastiprināti pakaramie (dāvanā)</li>\n"
        "          <li>1× Daudzfunkcionālie knaģīši (dāvanā)</li>"
    ),
    "sk": (
        "          <li>1× Vystužené vešiaky (darček)</li>\n"
        "          <li>1× Multifunkčné klipy (darček)</li>"
    ),
}

# Per landing path replacements (old, new) — longest first when applying.
LANDING_REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "lv/luno-3910/landing.html": [
        (
            '<span class="hl">Portatīvā 3 vienā žāvētājs</span>',
            '<span class="hl">Pārnēsājams žāvētājs “3 vienā”</span>',
        ),
        (
            "Darbojas arī lietū, salā vai apmācās debesīs",
            "Darbojas arī lietainā, aukstā vai mākoņainā laikā",
        ),
        (
            "«Veļas telpa ir maza un biedēja žāvētājs. Pēc cikla aizveru LUNO™ un nolieku uz plaukta: aizņem maz vietas un vienmēr ir gatava.»",
            "«Veļas telpa ir maza, un žāvēšanas statīvs vienmēr traucēja. Pēc cikla aizveru LUNO™ un nolieku uz plaukta: aizņem maz vietas un vienmēr ir gatava.»",
        ),
    ],
    "cz/luno-3169/landing.html": [
        ("auto vypnutí", "automatické vypnutí"),
        ("zápach zavřenosti", "zatuchlý zápach"),
    ],
    "sk/luno-4321/landing.html": [
        ("02 — Nie len povrch", "02 — Nielen povrch"),
        ("auto vypnutie", "automatické vypnutie"),
        ("Karta online netreba", "Pri online objednávke nepotrebujete kartu"),
    ],
    "hu/luno-1915/landing.html": [
        (
            '<p class="italic">A zárt térben a meleg levegő eléri a nehezebb helyeket is — a mosás gyorsabban hordható vagy eltehető.</p>',
            '<p class="italic">A zárt térben a meleg levegő a nehezebben hozzáférhető részeket is eléri, így a ruhák a ciklus után hamarabb felvehetők vagy elpakolhatók.</p>',
        ),
    ],
}

# Comparison table + hero (regen from shoproomdock may reintroduce old LV weather line).
LANG_WIDE_REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "lv": [
        (
            "Darbojas arī lietū, salā vai apmācās debesīs",
            "Darbojas arī lietainā, aukstā vai mākoņainā laikā",
        ),
    ],
    "cs": [
        ("auto vypnutí", "automatické vypnutí"),
        ("zápach zavřenosti", "zatuchlý zápach"),
    ],
    "sk": [
        ("02 — Nie len povrch", "02 — Nielen povrch"),
        ("auto vypnutie", "automatické vypnutie"),
        ("Karta online netreba", "Pri online objednávke nepotrebujete kartu"),
    ],
}

IT_KIT_APPEND = (
    "          <li>1× Grucce rinforzate (in omaggio)</li>\n"
    "          <li>1× Clip multiuso (in omaggio)</li>"
)
