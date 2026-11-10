#!/usr/bin/env python3
"""Replace company name and address across the site."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_COMPANY = "BlueVision Interactive Limited"
NEW_COMPANY = "Northstar Digital Growth LLC"

OLD_ADDRESS_FULL = (
    "Flat/RM07, 19F, Kodak House II, 39 Healthy street East, "
    "North Point, Hong Kong Island, Hong Kong"
)
NEW_ADDRESS_FULL = "32 N Gould St., Sheridan, WY 82801, Statele Unite"

OLD_ADDRESS_SHORT = "39 Healthy street East, North Point, Hong Kong Island, Hong Kong"

REPLACEMENTS = [
    (OLD_COMPANY, NEW_COMPANY),
    (OLD_ADDRESS_FULL, NEW_ADDRESS_FULL),
    (OLD_ADDRESS_SHORT, NEW_ADDRESS_FULL),
    (
        "Flat/RM07, 19F, Kodak House II<br>\n39 Healthy street East, North Point<br>\nHong Kong Island, Hong Kong",
        "32 N Gould St.<br>\nSheridan, WY 82801<br>\nStatele Unite",
    ),
    (
        "Flat/RM07, 19F, Kodak House II<br>\r\n39 Healthy street East, North Point<br>\r\nHong Kong Island, Hong Kong",
        "32 N Gould St.<br>\r\nSheridan, WY 82801<br>\r\nStatele Unite",
    ),
    (
        "Flat/RM07, 19F, Kodak House II<br>\n39 Healthy street East, North Point<br>\nHong Kong Island, Hong Kong<br>",
        "32 N Gould St.<br>\nSheridan, WY 82801<br>\nStatele Unite<br>",
    ),
    (
        '      "Flat/RM07, 19F, Kodak House II",\n      "39 Healthy street East, North Point, Hong Kong Island, Hong Kong"',
        '      "32 N Gould St.",\n      "Sheridan, WY 82801, Statele Unite"',
    ),
    ("North Point, Hong Kong", "Sheridan, WY, Statele Unite"),
    ("North Point, Hong Kong Island, Hong Kong", "Sheridan, WY 82801, Statele Unite"),
    (
        "headquarters in 39 Healthy street East, North Point, Hong Kong Island, Hong Kong",
        "headquarters at 32 N Gould St., Sheridan, WY 82801, Statele Unite",
    ),
    ("Flat/RM07, 19F, Kodak House II", "32 N Gould St."),
    ("39 Healthy street East, North Point", "Sheridan, WY 82801"),
    ("Hong Kong Island, Hong Kong", "Statele Unite"),
]

EXTENSIONS = {".html", ".json", ".py", ".xml", ".sh"}


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def update_sitemap(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = re.sub(
        r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>",
        "<lastmod>2026-09-16</lastmod>",
        text,
    )
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if ".git" in path.parts:
            continue
        if update_file(path):
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    if update_sitemap(ROOT / "sitemap.xml"):
        changed += 1
        print("updated: sitemap.xml (lastmod)")
    print(f"Done. {changed} files changed.")


if __name__ == "__main__":
    main()
