#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert AI image disclosure in footers of HTML pages that use /assets/img/products/.

Idempotent: skips pages that already contain the disclosure. Run from repo root:
  python scripts/apply_ai_footer_disclosure.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from scripts.ai_image_notice_i18n import notice_text_for_lang  # noqa: E402

GSH_STYLE = (
    ' class="gsh-standalone-footer__ai-disclosure" '
    'style="margin-top:1rem;max-width:36rem;color:#e2e8f0;line-height:1.55;font-size:inherit"'
)


def _lang_from_html(raw: str) -> str:
    m = re.search(r'<html[^>]*\blang=["\']([^"\']+)["\']', raw, re.I)
    if not m:
        return "en"
    return m.group(1).strip()


def _has_disclosure(raw: str) -> bool:
    return (
        'data-ai-disclosure="1"' in raw
        or "site-footer__ai-notice" in raw
        or "site-footer__ai-disclosure" in raw
        or "gsh-standalone-footer__ai-disclosure" in raw
    )


def _escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _insert_gsh(raw: str, text: str) -> str | None:
    esc = _escape_html(text)
    block = f"<p{GSH_STYLE}>{esc}</p>"
    if _has_disclosure(raw):
        return None
    m = re.search(
        r'(<a class="gsh-standalone-footer__logo"[^>]*>.*?</a>)',
        raw,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return None
    return raw[: m.end()] + "\n" + block + raw[m.end() :]


def _insert_site_blurb(raw: str, text: str) -> str | None:
    if _has_disclosure(raw):
        return None
    esc = _escape_html(text)
    insert = f'<p class="site-footer__ai-notice" data-ai-disclosure="1">{esc}</p>'
    m = re.search(
        r'<p class="site-footer__blurb">.*?</p>',
        raw,
        flags=re.DOTALL,
    )
    if not m:
        return None
    return raw[: m.end()] + "\n" + insert + raw[m.end() :]


def _insert_inline_blurb(raw: str, text: str) -> str | None:
    if _has_disclosure(raw):
        return None
    esc = _escape_html(text)
    insert = f'<p class="site-footer__ai-notice" data-ai-disclosure="1">{esc}</p>'
    m = re.search(
        r'<p style="margin-top:1rem;max-width:340px">.*?</p>',
        raw,
        flags=re.DOTALL,
    )
    if not m:
        return None
    return raw[: m.end()] + "\n" + insert + raw[m.end() :]


def patch_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if "thank-you" in rel or rel.endswith("thank-you.html"):
        return False
    raw = path.read_text(encoding="utf-8")
    if "assets/img/products" not in raw:
        return False
    if _has_disclosure(raw):
        return False
    lang = _lang_from_html(raw)
    text = notice_text_for_lang(lang)
    new: str | None = None
    if "gsh-standalone-footer" in raw:
        new = _insert_gsh(raw, text)
    if new is None:
        new = _insert_site_blurb(raw, text)
    if new is None:
        new = _insert_inline_blurb(raw, text)
    if new is None or new == raw:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts and rel.parts[0] in (".git", "node_modules"):
            continue
        if patch_file(p):
            print(f"Patched {rel}")
            n += 1
    print(f"Done. Patched {n} file(s).")


if __name__ == "__main__":
    main()
