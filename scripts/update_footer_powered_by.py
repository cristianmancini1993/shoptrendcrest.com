#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add powered-by header, company block, and update footer copyright site-wide."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMPANY = "WHATECH MOBILE CO., LIMITED"
DOMAIN = "shoptrendcrest.com"

ADDRESS_LINES = [
    "Room 505, 5th floor, Beverley Commercial Centre",
    "87-105 Chatham Road South",
    "Tsim Sha Tsui",
    "Kowloon",
]

LOCALE = {
    "bg": {"powered": "Задвижвано от", "hong_kong": "Хонконг", "rights": "Всички права запазени."},
    "cz": {"powered": "Provozuje", "hong_kong": "Hongkong", "rights": "Všechna práva vyhrazena."},
    "de": {"powered": "Bereitgestellt von", "hong_kong": "Hongkong", "rights": "Alle Rechte vorbehalten."},
    "ee": {"powered": "Powered by", "hong_kong": "Hongkong", "rights": "Kõik õigused kaitstud."},
    "en": {"powered": "Powered by", "hong_kong": "Hong Kong", "rights": "All rights reserved."},
    "es": {"powered": "Operado por", "hong_kong": "Hong Kong", "rights": "Todos los derechos reservados."},
    "fr": {"powered": "Propulsé par", "hong_kong": "Hong Kong", "rights": "Tous droits réservés."},
    "gr": {"powered": "Powered by", "hong_kong": "Χονγκ Κονγκ", "rights": "All rights reserved."},
    "hr": {"powered": "Pokreće", "hong_kong": "Hong Kong", "rights": "Sva prava pridržana."},
    "hu": {"powered": "Üzemelteti", "hong_kong": "Hongkong", "rights": "Minden jog fenntartva."},
    "it": {"powered": "Gestito da", "hong_kong": "Hong Kong", "rights": "Tutti i diritti riservati."},
    "lt": {"powered": "Prižiūri", "hong_kong": "Honkongas", "rights": "Visos teisės saugomos."},
    "lv": {"powered": "Nodrošina", "hong_kong": "Honkonga", "rights": "Visas tiesības aizsargātas."},
    "pl": {"powered": "Obsługiwane przez", "hong_kong": "Hongkong", "rights": "Wszelkie prawa zastrzeżone."},
    "pt": {"powered": "Operado por", "hong_kong": "Hong Kong", "rights": "Todos os direitos reservados."},
    "ro": {"powered": "Operat de", "hong_kong": "Hong Kong", "rights": "Toate drepturile rezervate."},
    "si": {"powered": "Poganja", "hong_kong": "Hongkong", "rights": "Vse pravice pridržane."},
    "sk": {"powered": "Prevádzka", "hong_kong": "Hongkong", "rights": "Všetky práva vyhradené."},
}

HONG_KONG_VARIANTS = {"Hong Kong", "Hongkong", "Hongkongis", "Honkongas", "Honkonga", "Χονγκ Κονγκ", "Хонконг"}

COMPANY_LI_RE = re.compile(
    r"\s*<li>(?:<strong>)?WHATECH MOBILE CO\., LIMITED(?:</strong>)?</li>\s*",
    re.IGNORECASE,
)
SINGLE_ADDRESS_LI_RE = re.compile(
    r"\s*<li>Room 505, 5th floor, Beverley Commercial Centre, "
    r"87-105 Chatham Road South, Tsim Sha Tsui, Kowloon, Hong Kong</li>\s*",
    re.IGNORECASE,
)
FOOTER_RE = re.compile(r"<footer class=\"site-footer\"[^>]*>.*?</footer>", re.DOTALL | re.IGNORECASE)
LANG_RE = re.compile(r"<html[^>]+lang=[\"']([a-z]{2})", re.IGNORECASE)
RIGHTS_RE = re.compile(
    r"—\s*(.+?)(?:\s*<a\s+href=[\"']/[\"']>.*?</a>)?\s*</div>",
    re.DOTALL | re.IGNORECASE,
)


def detect_geo(path: Path, html: str) -> str:
    parts = path.parts
    for part in parts:
        if part in LOCALE:
            return part
    m = LANG_RE.search(html)
    if m and m.group(1) in LOCALE:
        return m.group(1)
    return "en"


def strip_company_from_contact(footer: str) -> str:
    footer = COMPANY_LI_RE.sub("", footer)
    footer = SINGLE_ADDRESS_LI_RE.sub("", footer)
    for line in ADDRESS_LINES:
        footer = re.sub(rf"\s*<li>{re.escape(line)}</li>\s*", "", footer, flags=re.IGNORECASE)
    for hk in HONG_KONG_VARIANTS:
        footer = re.sub(rf"\s*<li>{re.escape(hk)}</li>\s*", "", footer, flags=re.IGNORECASE)
    return footer


def top_block(locale: str) -> str:
    powered = LOCALE[locale]["powered"]
    return (
        f'    <div class="site-footer__top">\n'
        f'      <p class="site-footer__top-meta">{DOMAIN} — {powered} {COMPANY}</p>\n'
        f"    </div>\n"
    )


def company_block(locale: str) -> str:
    hk = LOCALE[locale]["hong_kong"]
    lines = "\n".join(f'      <p class="site-footer__company-line">{line}</p>' for line in ADDRESS_LINES + [hk])
    return (
        f'    <div class="site-footer__company">\n'
        f'      <p class="site-footer__company-name"><strong>{COMPANY}</strong></p>\n'
        f"{lines}\n"
        f"    </div>\n"
    )


def extract_rights(old_bottom: str, locale: str) -> str:
    m = RIGHTS_RE.search(old_bottom)
    if m:
        text = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        text = re.sub(r"\s+", " ", text)
        if text and "WHATECH" not in text.upper():
            if not text.endswith("."):
                text += "."
            return text
    return LOCALE[locale]["rights"]


def bottom_block(locale: str, rights: str) -> str:
    powered = LOCALE[locale]["powered"]
    return (
        f'    <div class="site-footer__bottom">'
        f"© <span data-year>2026</span> {DOMAIN} — {powered} {COMPANY}. {rights}"
        f"</div>"
    )


def transform_footer(footer: str, locale: str) -> str:
    if "site-footer__top-meta" in footer and "site-footer__company-name" in footer:
        powered = LOCALE[locale]["powered"]
        hk = LOCALE[locale]["hong_kong"]
        footer = re.sub(
            r'(<p class="site-footer__top-meta">)[^<]+(</p>)',
            rf"\1{DOMAIN} — {powered} {COMPANY}\2",
            footer,
            count=1,
        )
        footer = strip_company_from_contact(footer)
        old_bottom_m = re.search(r'<div class="site-footer__bottom">.*?</div>', footer, re.DOTALL)
        rights = extract_rights(old_bottom_m.group(0), locale) if old_bottom_m else LOCALE[locale]["rights"]
        footer = re.sub(
            r'<div class="site-footer__bottom">.*?</div>',
            bottom_block(locale, rights),
            footer,
            count=1,
            flags=re.DOTALL,
        )
        for line in ADDRESS_LINES:
            footer = footer.replace(f"<p class=\"site-footer__company-line\">{line}</p>", f'<p class="site-footer__company-line">{line}</p>')
        footer = re.sub(
            r'(<p class="site-footer__company-line">)[^<]+(</p>\s*</div>\s*<div class="site-footer__bottom">)',
            rf"\1{hk}\2",
            footer,
            count=1,
        )
        return footer

    footer = strip_company_from_contact(footer)

    old_bottom_m = re.search(r'<div class="site-footer__bottom">.*?</div>', footer, re.DOTALL)
    rights = extract_rights(old_bottom_m.group(0), locale) if old_bottom_m else LOCALE[locale]["rights"]

    if re.search(r"<div class=\"container\">", footer):
        footer = re.sub(
            r"(<div class=\"container\">)\s*",
            r"\1\n" + top_block(locale),
            footer,
            count=1,
        )
    else:
        footer = re.sub(
            r"(<footer class=\"site-footer\"[^>]*>)\s*",
            r"\1\n  <div class=\"container\">\n" + top_block(locale),
            footer,
            count=1,
        )

    footer = re.sub(
        r'(\s*</div>\s*)(<div class="site-footer__bottom">)',
        r"\1" + company_block(locale) + r"\2",
        footer,
        count=1,
        flags=re.DOTALL,
    )

    footer = re.sub(
        r'<div class="site-footer__bottom">.*?</div>',
        bottom_block(locale, rights),
        footer,
        count=1,
        flags=re.DOTALL,
    )
    return footer


def transform_html(html: str, path: Path) -> str:
    if "site-footer" not in html:
        return html
    locale = detect_geo(path, html)

    def repl(match: re.Match[str]) -> str:
        return transform_footer(match.group(0), locale)

    return FOOTER_RE.sub(repl, html)


def load_domain_from_policies() -> str:
    sample = ROOT / "content" / "it" / "policies.json"
    if sample.is_file():
        data = json.loads(sample.read_text(encoding="utf-8"))
        return data.get("common", {}).get("domain", DOMAIN)
    return DOMAIN


def main() -> None:
    global DOMAIN
    DOMAIN = load_domain_from_policies()

    patterns = ["**/*.html"]
    changed: list[Path] = []
    for pattern in patterns:
        for path in ROOT.glob(pattern):
            if "preview" in path.parts or "node_modules" in path.parts:
                continue
            original = path.read_text(encoding="utf-8")
            updated = transform_html(original, path.relative_to(ROOT))
            if updated != original:
                path.write_text(updated, encoding="utf-8", newline="\n")
                changed.append(path)

    print(f"Updated {len(changed)} HTML files (domain: {DOMAIN})")


if __name__ == "__main__":
    main()
