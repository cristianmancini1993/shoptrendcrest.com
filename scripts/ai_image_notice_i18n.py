# -*- coding: utf-8 -*-
"""Localized paragraph for AI-generated/modified images (thank-you + rebuildable landings).

Used by generators and batch tools; keep in sync when adding locales.
"""

from __future__ import annotations

import html as html_lib
import re

# Map HTML ``lang`` (first segment) or internal geo/tr keys → notice text.
BY_LANG: dict[str, str] = {
    "it": "Alcune immagini in questa pagina sono state generate o modificate con intelligenza artificiale e hanno solo scopo illustrativo. Potrebbero non corrispondere fedelmente all’aspetto reale del prodotto, alle dimensioni, ai colori, alle caratteristiche o alle prestazioni.",
    "en": "Some images on this page have been generated or modified using artificial intelligence and are intended for illustrative purposes only. They may not accurately represent the product's actual appearance, size, colors, features, or performance.",
    "de": "Einige Bilder auf dieser Seite wurden mit Künstlicher Intelligenz erzeugt oder bearbeitet und dienen nur zur Veranschaulichung. Sie entsprechen möglicherweise nicht genau dem tatsächlichen Aussehen, der Größe, den Farben, den Merkmalen oder der Leistung des Produkts.",
    "es": "Algunas imágenes de esta página han sido generadas o modificadas con inteligencia artificial y solo tienen fines ilustrativos. Pueden no reflejar con exactitud el aspecto real del producto, su tamaño, colores, características o rendimiento.",
    "pt": "Algumas imagens nesta página foram geradas ou alteradas com recurso a inteligência artificial e destinam‑se apenas a fins ilustrativos. Podem não corresponder com exatidão ao aspeto real do produto, às dimensões, às cores, às caraterísticas ou ao desempenho.",
    "ro": "Unele imagini de pe această pagină au fost generate sau modificate cu inteligență artificială și au doar rol ilustrativ. Este posibil să nu reflecte cu acuratețe aspectul real al produsului, dimensiunile, culorile, caracteristicile sau performanța.",
    "sk": "Niektoré obrázky na tejto stránke boli vytvorené alebo upravené umelou inteligenciou a slúžia len na ilustračné účely. Nemusia presne zodpovedať skutočnému vzhľadu produktu, jeho rozmerom, farbám, vlastnostiam alebo výkonu.",
    "sl": "Nekatere slike na tej strani so bile ustvarjene ali spremenjene z umetno inteligenco in so namenjene le za ponazoritev. Morda ne odražajo natančno dejanskega videza izdelka, velikosti, barv, lastnosti ali zmogljivosti.",
    "hr": "Neke slike na ovoj stranici generirane su ili izmijenjene umjetnom inteligencijom i služe isključivo za ilustraciju. Možda ne odgovaraju stvarnom izgledu proizvoda, veličini, bojama, značajkama ili učinkovitosti.",
    "hu": "Az oldalon szereplő egyes képeket mesterséges intelligencia hozta létre vagy módosította, és csak szemléltető céljuk van. Előfordulhat, hogy nem tükrözik pontosan a termék tényleges megjelenését, méretét, színeit, jellemzőit vagy teljesítményét.",
    "cs": "Některé obrázky na této stránce byly vytvořeny nebo upraveny pomocí umělé inteligence a slouží pouze pro ilustraci. Nemusí přesně odpovídat skutečnému vzhledu výrobku, jeho rozměrům, barvám, vlastnostem nebo výkonu.",
    "lv": "Dažas šīs lapas attēlus ir ģenerējusi vai labojusi mākslīgais intelekts, un tie paredzēti tikai ilustratīviem mērķiem. Tie var neatbilst precīzi preces faktiskajam izskatam, izmēriem, krāsām, īpašībām vai veiktspējai.",
    "lt": "Kai kurie šio puslapio vaizdai buvo sugeneruoti arba pakeisti naudojant dirbtinį intelektą ir skirti tik iliustracijai. Jie gali ne tiksliai atspindėti tikrąją produkto išvaizdą, dydį, spalvas, savybes ar našumą.",
    "pl": "Niektóre obrazy na tej stronie zostały wygenerowane lub zmodyfikowane przy użyciu sztucznej inteligencji i służą wyłącznie celom ilustracyjnym. Mogą nie oddawać dokładnie rzeczywistego wyglądu produktu, rozmiaru, kolorów, cech lub wydajności.",
    "fr": "Certaines images de cette page ont été générées ou modifiées à l’aide de l’intelligence artificielle et sont uniquement destinées à l’illustration. Elles peuvent ne pas refléter fidèlement l’apparence réelle du produit, sa taille, ses couleurs, ses caractéristiques ou ses performances.",
    "bg": "Някои изображения на тази страница са генерирани или променени с изкуствен интелект и са само с илюстративна цел. Може да не отразяват точно реалния вид на продукта, размера, цветовете, характеристиките или производителността.",
    "el": "Ορισμένες εικόνες σε αυτήν τη σελίδα έχουν δημιουργηθεί ή τροποποιηθεί με τεχνητή νοημοσύνη και προορίζονται μόνο για ενδεικτικούς σκοπούς. Ενδέχεται να μην απεικονίζουν με ακρίβεια την πραγματική εμφάνιση του προϊόντος, το μέγεθος, τα χρώματα, τα χαρακτηριστικά ή την απόδοση.",
    "et": "Mõned selle lehe pildid on loodud või muudetud tehisintellekti abil ja on mõeldud ainult illustreerimiseks. Need ei pruugi täpselt vastata toote tegelikule välimusele, mõõtudele, värvidele, omadustele või jõudlusele.",
    "gr": "Ορισμένες εικόνες σε αυτή τη σελίδα έχουν δημιουργηθεί ή τροποποιηθεί με τεχνητή νοημοσύνη και προορίζονται μόνο για ενδεικτικούς σκοπούς. Ενδέχεται να μην απεικονίζουν με ακρίβεια την πραγματική εμφάνιση του προϊόντος, το μέγεθος, τα χρώματα, τα χαρακτηριστικά ή την απόδοση.",
    "ee": "Mõned selle lehe pildid on loodud või muudetud tehisintellekti abil ja on mõeldud ainult illustreerimiseks. Need ei pruugi täpselt vastata toote tegelikule välimusele, mõõtudele, värvidele, omadustele või jõudlusele.",
}

DEFAULT_LANG = "en"

_LEGACY_AI_CLASSES = (
    "site-footer__ai-disclosure",
    "site-footer__ai-media-notice",
    "gsh-standalone-footer__ai-disclosure",
    "hubaura-standalone-footer__ai-media-notice",
)

# Remove any legacy-variant AI disclosure paragraphs (non-canonical classes).
_STRIP_LEGACY_AI_PARA = re.compile(
    r"<p\b[^>]*\bclass=\"[^\"]*\b(?:"
    + "|".join(re.escape(c) for c in _LEGACY_AI_CLASSES)
    + r")\b[^\"]*\"[^>]*>[\s\S]*?</p>\s*",
    re.IGNORECASE,
)

# Remove canonical blocks (for replace / dedupe).
_STRIP_CANONICAL_AI_PARA = re.compile(
    r'<p class="site-footer__ai-notice" data-ai-disclosure="1">[\s\S]*?</p>\s*',
    re.IGNORECASE,
)

_CANONICAL_AI_P = re.compile(
    r'<p class="site-footer__ai-notice" data-ai-disclosure="1">([\s\S]*?)</p>',
    re.IGNORECASE,
)

_PARAGRAPH = '<p class="site-footer__ai-notice" data-ai-disclosure="1">{text}</p>'
_MARKER_BLOCK = "<!-- AI_IMAGE_DISCLOSURE_PLACEHOLDER -->"

_AFTER_SITE_HEADING = r'(\s*</div>\s*\n\s*<div>\s*\n\s*<h4 class="site-footer__heading">)'

_RE_GSH_LOGO_COL = re.compile(
    r"(<div class=\"gsh-standalone-footer__grid\">\s*<div>\s*"
    r'<a class="gsh-standalone-footer__logo"[^>]*>[\s\S]*?</a>[\s\S]*?)'
    r'(\s*</div>\s*<div>\s*<h4 class="gsh-standalone-footer__heading">)',
    re.IGNORECASE,
)

_RE_HUBAURA_AFTER_DESC = re.compile(
    r"(<p class=\"hubaura-standalone-footer__description\">[\s\S]*?</p>[\s\S]*?)"
    r'(\s*</div>\s*<div>\s*<h4 class="hubaura-standalone-footer__heading">)',
    re.IGNORECASE,
)

_RE_HUBAURA_LOGO_COL = re.compile(
    r"(<div class=\"hubaura-standalone-footer__grid\">\s*<div>\s*"
    r'<a[^>]*class="hubaura-standalone-footer__logo"[^>]*>[\s\S]*?</a>[\s\S]*?)'
    r'(\s*</div>\s*<div>\s*<h4 class="hubaura-standalone-footer__heading">)',
    re.IGNORECASE,
)


def notice_text_for_lang(lang: str | None) -> str:
    if not lang:
        return BY_LANG[DEFAULT_LANG]
    raw = lang.strip().lower().replace("_", "-")
    segments = raw.split("-")
    # HTML ``lang``: pt-PT → PT-PT copy; generic pt → same bucket.
    if segments[0] == "pt":
        return BY_LANG["pt"]
    key = segments[0]
    if key == "cz":
        key = "cs"
    return BY_LANG.get(key, BY_LANG[DEFAULT_LANG])


def notice_paragraph_html(lang: str | None) -> str:
    text = html_lib.escape(notice_text_for_lang(lang))
    return _PARAGRAPH.format(text=text)


def _normalize_notice_text(s: str) -> str:
    s = html_lib.unescape(s).replace("\xa0", " ").strip()
    for ch in ("\u2011", "\u2010", "\u2013", "\u2014"):
        s = s.replace(ch, "-")
    return s.replace("'", "'")


def _inner_text_matches_expected(inner: str, lang: str | None) -> bool:
    """Compare decoded paragraph text to expected notice (apostrophe / entity tolerant)."""
    inner_clean = _normalize_notice_text(inner)
    expected = _normalize_notice_text(notice_text_for_lang(lang))
    return inner_clean == expected


def strip_ai_notice_paragraphs(html: str) -> str:
    """Remove every AI disclosure paragraph (legacy + canonical)."""
    cur = html
    prev = None
    while prev != cur:
        prev = cur
        cur = _STRIP_LEGACY_AI_PARA.sub("", cur)
        cur = _STRIP_CANONICAL_AI_PARA.sub("", cur)
    return cur


def has_ai_notice(html: str) -> bool:
    """True if HTML already has any footer AI disclosure (canonical, legacy, or marker)."""
    if _MARKER_BLOCK in html:
        return True
    if _CANONICAL_AI_P.search(html):
        return True
    return bool(_STRIP_LEGACY_AI_PARA.search(html))


def footer_ai_notice_complete(html: str, lang: str | None) -> bool:
    """Valid layout: one canonical paragraph sitewide with correct text; no legacy."""
    if _MARKER_BLOCK in html:
        return False
    if _STRIP_LEGACY_AI_PARA.search(html):
        return False
    matches = list(_CANONICAL_AI_P.finditer(html))
    if len(matches) != 1:
        return False
    if not _inner_text_matches_expected(matches[0].group(1), lang):
        return False
    return True


def _segment_has_notice(segment: str) -> bool:
    return "site-footer__ai-notice" in segment and 'data-ai-disclosure="1"' in segment


def _segment_text_ok(segment: str, lang: str | None) -> bool:
    m = _CANONICAL_AI_P.search(segment)
    if not m:
        return False
    return _inner_text_matches_expected(m.group(1), lang)


def _patch_gsh_standalone(html: str, para: str) -> str:
    if _RE_GSH_LOGO_COL.search(html) is None:
        return html

    def repl(m: re.Match[str]) -> str:
        seg = m.group(0)
        if _segment_has_notice(seg):
            return seg
        return m.group(1) + "\n" + para + m.group(2)

    return _RE_GSH_LOGO_COL.sub(repl, html, count=1)


def _patch_hubaura_standalone(html: str, para: str) -> str:
    def repl(m: re.Match[str]) -> str:
        seg = m.group(0)
        if _segment_has_notice(seg):
            return seg
        return m.group(1) + "\n        " + para + m.group(2)

    new = html
    if "hubaura-standalone-footer__description" in new and _RE_HUBAURA_AFTER_DESC.search(new):
        return _RE_HUBAURA_AFTER_DESC.sub(repl, new, count=1)
    return _RE_HUBAURA_LOGO_COL.sub(repl, new, count=1)


def _patch_site_footer_standard(html: str, para: str) -> str:
    _AFTER_BLURB = _AFTER_SITE_HEADING

    m = re.search(
        r'(<p class="site-footer__blurb">.*?</p>)' + _AFTER_BLURB,
        html,
        flags=re.DOTALL,
    )
    if m:
        seg = m.group(0)
        if _segment_has_notice(seg):
            return html
        return html[: m.start()] + m.group(1) + "\n        " + para + m.group(2) + html[m.end() :]

    m_inline = re.search(
        r'(<p[^>]*style="[^"]*max-width:\s*340px[^"]*"[^>]*>.*?</p>)' + _AFTER_BLURB,
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if m_inline:
        seg = m_inline.group(0)
        if _segment_has_notice(seg):
            return html
        return (
            html[: m_inline.start()]
            + m_inline.group(1)
            + "\n        "
            + para
            + m_inline.group(2)
            + html[m_inline.end() :]
        )

    m2 = re.search(
        r'(<div class="site-footer__grid">\s*<div>\s*'
        r'<a href="/" class="site-logo"[^>]*>.*?</a>)'
        + _AFTER_BLURB,
        html,
        flags=re.DOTALL,
    )
    if m2:
        seg = m2.group(0)
        if _segment_has_notice(seg):
            return html
        return html[: m2.start()] + m2.group(1) + "\n        " + para + m2.group(2) + html[m2.end() :]

    if '<div class="site-footer__entity">' in html:
        if "<p class=\"site-footer__ai-notice\"" in html.split("site-footer__entity")[0]:
            return html
        return html.replace(
            '<div class="site-footer__entity">',
            f"{para}\n        <div class=\"site-footer__entity\">",
            1,
        )

    m3 = re.search(r'(\n\s*)<div class="site-footer__bottom">', html)
    if m3:
        insert_at = m3.start()
        indent = m3.group(1) or "\n    "
        before = html[:insert_at]
        if 'data-ai-disclosure="1"' in before[-800:]:
            return html
        return html[:insert_at] + f"{indent}{para}" + html[insert_at:]

    return html


def insert_ai_notice_in_site_footer(html: str, lang: str | None) -> str:
    """Ensure exactly one canonical AI paragraph for the page (one footer family)."""
    if footer_ai_notice_complete(html, lang):
        return html
    html = strip_ai_notice_paragraphs(html)
    para = notice_paragraph_html(lang)
    # Prefer standard site footer when present; avoid double inserts on hybrid pages.
    if re.search(r'<footer[^>]*\bclass="[^"]*\bsite-footer\b', html, re.I):
        return _patch_site_footer_standard(html, para)
    if "gsh-standalone-footer__grid" in html:
        return _patch_gsh_standalone(html, para)
    if "hubaura-standalone-footer__grid" in html:
        return _patch_hubaura_standalone(html, para)
    return _patch_site_footer_standard(html, para)


def footer_insertion_after_blurb(html: str, lang: str | None) -> str:
    """Backward-compatible name: use full footer insertion logic."""
    return insert_ai_notice_in_site_footer(html, lang)


def thank_you_insert_before_entity(html: str, lang: str | None) -> str:
    """For footers without blurb: insert before site-footer__entity or fallback."""
    return insert_ai_notice_in_site_footer(html, lang)


def replace_placeholder(html: str, lang: str | None) -> str:
    if _MARKER_BLOCK not in html:
        return html
    return html.replace(_MARKER_BLOCK, notice_paragraph_html(lang), 1)
