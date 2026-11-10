# -*- coding: utf-8 -*-
"""Add localized AI image disclosure to home ``/`` and product landings.

Processes root ``index.html``, ``**/landing.html``, and product ``**/index.html``
(not ``thank-you/``). Skips redirect stubs without ``<footer``. Does **not** use
image-path heuristics: every real landing gets one footer paragraph.

Run from repo root::

  python scripts/patch_landing_ai_notice.py
  python scripts/patch_landing_ai_notice.py --root /path/to/other-site.com

"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Site root directory (default: parent of scripts/)",
    )
    return p.parse_args(argv)


def _resolve_root(arg_root: Path | None) -> Path:
    script_dir = Path(__file__).resolve().parent
    return (arg_root or script_dir.parent).resolve()


def main(argv: list[str] | None = None) -> None:
    args = _parse_args(argv)
    root = _resolve_root(args.root)
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    from scripts.ai_image_notice_i18n import (  # noqa: E402
        footer_ai_notice_complete,
        insert_ai_notice_in_site_footer,
    )

    LANG_RE = re.compile(r"<html[^>]*\blang\s*=\s*[\"']([^\"']+)[\"']", re.I)

    def html_lang(path: Path, html: str) -> str:
        m = LANG_RE.search(html)
        if m:
            return m.group(1)
        parts = path.parts
        rel = path.relative_to(root).parts
        # .../{geo}/{slug}/file.html → geo
        if len(rel) >= 2 and rel[1] not in ("thank-you",):
            return rel[0]
        return "en"

    _NON_PRODUCT_DIRS = frozenset(
        {
            "thank-you",
            "assets",
            ".github",
            "about-us",
            "contact-us",
            "privacy-policy",
            "terms-conditions",
            "cookie-policy",
            "shipping-policy",
            "refund-policy",
        }
    )

    def is_product_index(path: Path) -> bool:
        if path.name != "index.html":
            return False
        if path.parent.name in _NON_PRODUCT_DIRS:
            return False
        rel = path.relative_to(root).parts
        if not rel:
            return False
        if any(p in _NON_PRODUCT_DIRS for p in rel):
            return False
        if rel[0] in ("scripts", "content", "node_modules"):
            return False
        return True

    def is_redirect_stub(html: str) -> bool:
        return "window.location.replace" in html and "<footer" not in html.lower()

    updated: list[Path] = []
    candidates: set[Path] = set()
    root_index = root / "index.html"
    if root_index.is_file():
        candidates.add(root_index)
    candidates.update(root.glob("**/landing.html"))
    for p in root.glob("**/index.html"):
        if is_product_index(p):
            candidates.add(p)

    for path in sorted(candidates):
        rel = path.relative_to(root)
        if "thank-you" in rel.parts:
            continue
        if any(p in ("archive", "backup", "scripts", "node_modules") for p in rel.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if path.name == "index.html" and is_redirect_stub(text):
            continue
        if "<footer" not in text.lower():
            continue
        lang = html_lang(path, text)
        if footer_ai_notice_complete(text, lang):
            continue
        new = insert_ai_notice_in_site_footer(text, lang)
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            updated.append(path.relative_to(root))
    print(f"Patched {len(updated)} landing/index file(s).")
    for p in updated:
        print(p)


if __name__ == "__main__":
    main()
