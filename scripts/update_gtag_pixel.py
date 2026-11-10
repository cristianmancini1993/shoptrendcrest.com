#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install or update Google Ads gtag pixel (AW-18510622150) across the site."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEW_ID = "AW-18510622150"
OLD_IDS = ("AW-18421302840", "AW-18360728507", "AW-18390079985")
PURCHASE_SEND_TO = f"{NEW_ID}/xfhbCIrl7bUdEMbbxvpE"

OLD_SEND_TO_RE = re.compile(
    rf"(?:{'|'.join(re.escape(x) for x in OLD_IDS)})/[A-Za-z0-9_-]+"
)
OTHER_AW_ID_RE = re.compile(r"AW-\d{8,12}")
LEGACY_LABELS = (
    "rPVUCJ-RiOwcELiM-89E",
    "piRMCJP23tkcEOiR9rJE",
    "iRw_CISgmfIcELCT09dE",
)

GTAG_BLOCK = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={NEW_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{NEW_ID}');
</script>"""

HEAD_INSERT = re.compile(r"(<head[^>]*>)", re.IGNORECASE)
REDIRECT_MARKERS = ("window.location.replace", 'http-equiv="refresh"')


def should_skip_html(path: Path) -> bool:
    if "archive" in path.parts or "preview" in path.parts:
        return True
    if "sync-conflict" in path.name:
        return True
    return False


def is_redirect_stub(text: str) -> bool:
    if len(text) > 2500:
        return False
    return any(m in text for m in REDIRECT_MARKERS)


def update_content(content: str, *, add_if_missing: bool) -> str:
    updated = content
    for old_id in OLD_IDS:
        updated = updated.replace(old_id, NEW_ID)

    updated = OLD_SEND_TO_RE.sub(PURCHASE_SEND_TO, updated)
    for label in LEGACY_LABELS:
        updated = updated.replace(f"{NEW_ID}/{label}", PURCHASE_SEND_TO)

    updated = OTHER_AW_ID_RE.sub(NEW_ID, updated)

    if add_if_missing and "googletagmanager.com/gtag/js" not in updated:
        updated = HEAD_INSERT.sub(r"\1\n" + GTAG_BLOCK, updated, count=1)
    return updated


def iter_targets() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in {"archive", "preview", ".git"}:
            continue
        if "sync-conflict" in path.name:
            continue
        if path.suffix == ".html":
            paths.append(path)
        elif path.suffix == ".js" and rel.parts[0] == "assets":
            paths.append(path)
    return sorted(paths)


def main() -> None:
    changed: list[Path] = []
    skipped_redirect = 0

    for path in iter_targets():
        original = path.read_text(encoding="utf-8")
        add_gtag = path.suffix == ".html" and not is_redirect_stub(original)
        updated = update_content(original, add_if_missing=add_gtag)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(path)
        if path.suffix == ".html" and is_redirect_stub(original):
            skipped_redirect += 1

    html_files = [p for p in ROOT.rglob("*.html") if not should_skip_html(p)]
    missing_gtag = [
        p
        for p in html_files
        if not is_redirect_stub(p.read_text(encoding="utf-8", errors="ignore"))
        and f"gtag/js?id={NEW_ID}" not in p.read_text(encoding="utf-8", errors="ignore")
        and "googletagmanager.com/gtag/js" not in p.read_text(encoding="utf-8", errors="ignore")
    ]
    old_id_left = sum(
        1
        for p in html_files
        for old in OLD_IDS
        if old in p.read_text(encoding="utf-8", errors="ignore")
    )

    print(f"Updated {len(changed)} files")
    print(f"Skipped {skipped_redirect} redirect HTML stubs (no gtag injected)")
    print(f"HTML without any gtag loader: {len(missing_gtag)}")
    print(f"Remaining old AW ID references in HTML: {old_id_left}")
    for path in missing_gtag[:8]:
        print(f"  missing: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
