#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace company legal entity and address across the site."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_COMPANY = "Vicequattrostrade Srl"
NEW_COMPANY = "WHATECH MOBILE CO., LIMITED"

OLD_ADDRESS_SINGLE = "Via Giosuè Carducci, 30, 28838 Stresa, Italy"
NEW_ADDRESS_SINGLE = (
    "Room 505, 5th floor, Beverley Commercial Centre, "
    "87-105 Chatham Road South, Tsim Sha Tsui, Kowloon, Hong Kong"
)

ADDRESS_LINES = [
    "Room 505, 5th floor, Beverley Commercial Centre",
    "87-105 Chatham Road South",
    "Tsim Sha Tsui",
    "Kowloon",
    "Hong Kong",
]

FOOTER_TWO_LINE = re.compile(
    r"<li>Via Giosuè Carducci, 30</li>\s*<li>28838 Stresa, Italy</li>",
    re.MULTILINE,
)

BR_ADDRESS = re.compile(
    r"Via Giosuè Carducci, 30<br>\s*28838 Stresa<br>\s*Italy(?:<br>|</p>)",
    re.MULTILINE,
)

JSON_COMPANY_INFO = re.compile(
    r'("<strong>Vicequattrostrade Srl</strong>",\s*)'
    r'"Via Giosuè Carducci, 30",\s*'
    r'"28838 Stresa, Italy"\s*',
    re.MULTILINE,
)

LOCATION_REPLACEMENTS = [
    ("Via Giosuè Carducci, 30 — 28838 Stresa, Italy", NEW_ADDRESS_SINGLE),
    ("Via Giosuè Carducci, 30, 28838 Stresa, Italyłochy", NEW_ADDRESS_SINGLE),
    ("Via Giosuè Carducci, 30, 28838 Stresa, Italyālija", NEW_ADDRESS_SINGLE),
    (OLD_ADDRESS_SINGLE, NEW_ADDRESS_SINGLE),
    ("Stresa (Italie)", "Hong Kong"),
    ("Stresa (Italia)", "Hong Kong"),
    ("Stresa (Itálie)", "Hong Kong"),
    ("Stresa (Włochy)", "Hong Kong"),
    ("Stresa, Italia", "Hong Kong"),
    ("Stresa, Itália", "Hong Kong"),
    ("Stresa, Itālija", "Hong Kong"),
    ("Stresa, Italy", "Hong Kong"),
    ("Stresa, Olaszország", "Hong Kong"),
    ("Stresa (Taliansko)", "Hong Kong"),
    ("Stresa (Italija)", "Hong Kong"),
    ("Stresa (Italien)", "Hong Kong"),
    ("Stresa, Italien", "Hong Kong"),
    ("Stresa, Italie", "Hong Kong"),
    ("Stresa, Itálie", "Hong Kong"),
    ("Stresa, Włochy", "Hong Kong"),
    ("Stresa, Taliansko", "Hong Kong"),
    ("Stresa, Italija", "Hong Kong"),
    ("Stresa, Ιταλία", "Hong Kong"),
    ("Stresas, Itaalias", "Hongkongis"),
    ("28838 Stresa, Italy", "Hong Kong"),
    ("28838 Stresa<br>", "Hong Kong<br>"),
    ("28838 Hong Kong", "Hong Kong"),
    ("(Via Giosuè Carducci, 30)", ""),
    ("Via Giosuè Carducci, 30", "Room 505, 5th floor, Beverley Commercial Centre, 87-105 Chatham Road South"),
    ("talijanske tvrtke", "tvrtke sa sjedištem u Hong Kongu"),
    ("itāļu uzņēmums", "uzņēmums ar mītni Hongkongā"),
    ("itāļu uzņēmuma", "uzņēmuma ar mītni Hongkongā"),
    ("headquarters in 28838 Stresa, Italy", "headquarters in Hong Kong"),
    ("sede a Stresa, Italia", "sede a Hong Kong"),
    ("sede em Stresa, Itália", "sede em Hong Kong"),
    ("galvenā mītne Stresa, Itālija", "galvenā mītne Hong Kong"),
    ("székhely Stresa, Olaszország", "székhely Hong Kong"),
]


def footer_replacement(match: re.Match[str]) -> str:
    indent = " " * 10
    return "\n".join(f"{indent}<li>{line}</li>" for line in ADDRESS_LINES)


def br_replacement(match: re.Match[str]) -> str:
    suffix = "</p>" if match.group(0).endswith("</p>") else "<br>"
    return "<br>\n".join(ADDRESS_LINES) + suffix


def json_company_info_replacement(_: re.Match[str]) -> str:
    lines = ",\n      ".join(f'"{line}"' for line in ADDRESS_LINES)
    return f'"<strong>{NEW_COMPANY}</strong>",\n      {lines}\n    '


def transform(content: str) -> str:
    content = FOOTER_TWO_LINE.sub(footer_replacement, content)
    content = BR_ADDRESS.sub(br_replacement, content)
    content = JSON_COMPANY_INFO.sub(json_company_info_replacement, content)
    content = content.replace(OLD_COMPANY, NEW_COMPANY)
    for old, new in LOCATION_REPLACEMENTS:
        content = content.replace(old, new)
    return content


def main() -> None:
    patterns = ["**/*.html", "content/**/*.json", "scripts/gen_kemppi_geos.py", "scripts/gen_glacierair_geos.py", "README.md"]
    changed: list[Path] = []

    for pattern in patterns:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            original = path.read_text(encoding="utf-8")
            updated = transform(original)
            if updated != original:
                path.write_text(updated, encoding="utf-8", newline="\n")
                changed.append(path)

    print(f"Updated {len(changed)} files")
    for path in sorted(changed):
        print(f"  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
