#!/usr/bin/env python3
"""Update gadgetshifthub.com footers — account 932 (Netmart LLC) signature format."""

from __future__ import annotations

import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "gadgetshifthub.com"
COMPANY = "Netmart LLC"

LOCALE = {
    "en": {"powered": "Powered by", "country": "United States"},
    "it": {"powered": "Gestito da", "country": "Stati Uniti"},
    "es": {"powered": "Impulsado por", "country": "Estados Unidos"},
    "de": {"powered": "Betrieben von", "country": "Vereinigte Staaten"},
    "fr": {"powered": "Propulsé par", "country": "États-Unis"},
    "pt": {"powered": "Desenvolvido por", "country": "Estados Unidos"},
    "pl": {"powered": "Obsługiwane przez", "country": "Stany Zjednoczone"},
    "cz": {"powered": "Provozováno společností", "country": "Spojené státy americké"},
    "sk": {"powered": "Prevádzané spoločnosťou", "country": "Spojené štáty americké"},
    "hu": {"powered": "Üzemelteti", "country": "Egyesült Államok"},
    "ro": {"powered": "Oferit de", "country": "Statele Unite"},
    "bg": {"powered": "Предоставено от", "country": "Съединени щати"},
    "gr": {"powered": "Υποστηρίζεται από", "country": "Ηνωμένες Πολιτείες"},
    "hr": {"powered": "Pokreće", "country": "Sjedinjene Države"},
    "si": {"powered": "Poganja", "country": "Združene države Amerike"},
    "lv": {"powered": "Nodrošina", "country": "Amerikas Savienotās Valstis"},
    "lt": {"powered": "Teikia", "country": "Jungtinės Valstijos"},
    "ee": {"powered": "Toetab", "country": "Ameerika Ühendriigid"},
}

GSH_FOOTER_CSS = """
.gsh-standalone-footer__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  width: 100%;
  max-width: 1320px;
  margin: 0 auto 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(148,163,184,.28);
}
.gsh-standalone-footer__powered {
  margin: 0;
  font-size: 11px;
  color: #94a3b8;
  text-align: right;
  line-height: 1.45;
}
.gsh-standalone-footer__powered strong { color: #cbd5e1; }
.gsh-standalone-footer__entity {
  width: 100%;
  max-width: 1320px;
  margin: 0 auto 12px;
  padding: 12px 0 12px 12px;
  border-top: 1px solid rgba(148,163,184,.28);
  border-left: 3px solid #f97316;
  font-size: 12px;
  line-height: 1.5;
  color: #94a3b8;
}
.gsh-standalone-footer__entity-name {
  margin: 0 0 6px;
  color: #fff;
}
.gsh-standalone-footer__entity-address { margin: 0; }
"""

ADDRESS_MARKERS = (
    "county of sussex",
    "16192 coastal",
    "lewes, de",
    "19958-3608",
    "stati uniti",
    "united states",
    "estados unidos",
    "vereinigte staaten",
    "états-unis",
    "stany zjednoczone",
    "spojené státy",
    "spojené štáty",
    "egyesült államok",
    "statele unite",
    "съединени",
    "ηνωμένες",
    "sjedinjene",
    "združene",
    "amerikas savienotās",
    "jungtinės",
    "ameerika ühendriigid",
)


def detect_geo(path: Path, soup: BeautifulSoup) -> str:
    parts = path.parts
    for i, part in enumerate(parts):
        if part in LOCALE and i > 0:
            return part
    html = soup.find("html")
    if html and html.get("lang"):
        lang = html["lang"].lower().split("-")[0]
        if lang in LOCALE:
            return lang
    return "en"


def is_address_line(text: str) -> bool:
    t = " ".join(text.split()).lower()
    if COMPANY.lower() in t and len(t) < 40:
        return True
    return any(m in t for m in ADDRESS_MARKERS)


def clean_contact_lists(footer) -> None:
    for ul in footer.find_all("ul"):
        parent = ul.parent
        if not parent:
            continue
        heading = parent.find(["h4", "h3", "h2"])
        if not heading:
            continue
        htext = heading.get_text(" ", strip=True).lower()
        if not any(
            k in htext
            for k in (
                "contact",
                "contatt",
                "kontakt",
                "kapcsolat",
                "επαφ",
                "контакт",
                "sazinā",
                "susisiek",
                "võtke",
                "elérhetőség",
            )
        ):
            continue
        for li in list(ul.find_all("li", recursive=False)):
            txt = li.get_text(" ", strip=True)
            if is_address_line(txt):
                li.decompose()


def powered_html(geo: str, prefix_class: str) -> str:
    loc = LOCALE[geo]
    return (
        f'<p class="{prefix_class}">{DOMAIN} — {loc["powered"]} '
        f"<strong>{COMPANY}</strong></p>"
    )


def entity_html(geo: str, prefix_class: str) -> str:
    loc = LOCALE[geo]
    return (
        f'<div class="{prefix_class}">'
        f'<p class="{prefix_class}-name"><strong>{COMPANY}</strong></p>'
        f'<p class="{prefix_class}-address">County of Sussex 16192 Coastal Hwy<br>'
        f"Lewes, DE 19958-3608, {loc['country']}</p>"
        "</div>"
    )


def bottom_html(geo: str, bottom_class: str) -> str:
    loc = LOCALE[geo]
    return (
        f'<div class="{bottom_class}">© <span data-year>2026</span> {DOMAIN} — '
        f"{loc['powered']} <strong>{COMPANY}</strong></div>"
    )


def sync_powered_in_footer(footer, geo: str) -> bool:
    """Update top powered line and copyright powered phrase only."""
    changed = False
    loc = LOCALE.get(geo, LOCALE["en"])
    marker = f"{DOMAIN} — {loc['powered']}"

    for cls in ("site-footer__powered", "gsh-standalone-footer__powered"):
        el = footer.find(class_=cls)
        if not el:
            continue
        if marker in el.get_text(" ", strip=True):
            continue
        new_el = BeautifulSoup(powered_html(geo, cls), "html.parser").p
        el.replace_with(new_el)
        changed = True

    for cls in ("site-footer__bottom", "gsh-standalone-footer__bottom"):
        bottom = footer.find(class_=cls)
        if not bottom:
            continue
        if marker in bottom.get_text(" ", strip=True):
            continue
        new_bottom = BeautifulSoup(bottom_html(geo, cls), "html.parser").div
        bottom.replace_with(new_bottom)
        changed = True
    return changed


def patch_site_footer(footer, geo: str) -> bool:
    changed = False
    container = footer.find(class_="container")
    if not container:
        return False

    if not container.find(class_="site-footer__top"):
        top = BeautifulSoup(
            f'<div class="site-footer__top">{powered_html(geo, "site-footer__powered")}</div>',
            "html.parser",
        ).div
        grid = container.find(class_="site-footer__grid")
        if grid:
            grid.insert_before(top)
            changed = True

    if not container.find(class_="site-footer__entity"):
        entity = BeautifulSoup(
            entity_html(geo, "site-footer__entity"), "html.parser"
        ).div
        bottom = container.find(class_="site-footer__bottom")
        if bottom:
            bottom.insert_before(entity)
            changed = True

    bottom = container.find(class_="site-footer__bottom")
    if bottom:
        expected = f"{DOMAIN} — {LOCALE[geo]['powered']}"
        if expected not in bottom.get_text(" ", strip=True):
            new_bottom = BeautifulSoup(
                bottom_html(geo, "site-footer__bottom"), "html.parser"
            ).div
            bottom.replace_with(new_bottom)
            changed = True

    if sync_powered_in_footer(footer, geo):
        changed = True

    clean_contact_lists(footer)
    return changed


def patch_gsh_footer(footer, geo: str) -> bool:
    changed = False
    if not footer.find(class_="gsh-standalone-footer__top"):
        grid = footer.find(class_="gsh-standalone-footer__grid")
        if grid:
            top = BeautifulSoup(
                f'<div class="gsh-standalone-footer__top">{powered_html(geo, "gsh-standalone-footer__powered")}</div>',
                "html.parser",
            ).div
            grid.insert_before(top)
            changed = True

    if not footer.find(class_="gsh-standalone-footer__entity"):
        entity = BeautifulSoup(
            entity_html(geo, "gsh-standalone-footer__entity"), "html.parser"
        ).div
        bottom = footer.find(class_="gsh-standalone-footer__bottom")
        if bottom:
            bottom.insert_before(entity)
            changed = True

    bottom = footer.find(class_="gsh-standalone-footer__bottom")
    if bottom:
        expected = f"{DOMAIN} — {LOCALE[geo]['powered']}"
        if expected not in bottom.get_text(" ", strip=True):
            new_bottom = BeautifulSoup(
                bottom_html(geo, "gsh-standalone-footer__bottom"), "html.parser"
            ).div
            bottom.replace_with(new_bottom)
            changed = True

    if sync_powered_in_footer(footer, geo):
        changed = True

    clean_contact_lists(footer)
    return changed


def inject_gsh_css(raw: str) -> str:
    if "gsh-standalone-footer__top" in raw and "gsh-standalone-footer__entity" in raw:
        if ".gsh-standalone-footer__top {" in raw:
            return raw
    marker = "@media (max-width:959px)"
    if marker in raw and ".gsh-standalone-footer__top {" not in raw:
        return raw.replace(marker, GSH_FOOTER_CSS + "\n" + marker, 1)
    return raw


def process_file(path: Path, powered_only: bool = False) -> bool:
    raw = path.read_text(encoding="utf-8")
    if "site-footer" not in raw and "gsh-standalone-footer" not in raw:
        return False

    soup = BeautifulSoup(raw, "html.parser")
    geo = detect_geo(path, soup)
    changed = False

    for footer in soup.find_all("footer", class_="site-footer"):
        if powered_only:
            if sync_powered_in_footer(footer, geo):
                changed = True
        elif patch_site_footer(footer, geo):
            changed = True

    for footer in soup.find_all("footer", class_="gsh-standalone-footer"):
        if powered_only:
            if sync_powered_in_footer(footer, geo):
                changed = True
        elif patch_gsh_footer(footer, geo):
            changed = True

    if not changed:
        return False

    out = str(soup)
    if not powered_only and "gsh-standalone-footer" in out:
        out = inject_gsh_css(out)

    if out != raw:
        path.write_text(out, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    powered_only = "--powered-only" in sys.argv
    updated = 0
    skipped = 0
    for html in ROOT.rglob("*.html"):
        if "node_modules" in html.parts:
            continue
        try:
            if process_file(html, powered_only=powered_only):
                updated += 1
                print(html.relative_to(ROOT))
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR {html}: {exc}", file=sys.stderr)
            skipped += 1
    print(f"\nUpdated: {updated}, errors: {skipped}")
    return 0 if skipped == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
