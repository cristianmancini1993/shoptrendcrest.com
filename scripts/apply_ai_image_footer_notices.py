#!/usr/bin/env python3
"""Insert AI image disclosure in product landing + home page footers (idempotent).

Excludes thank-you pages (user request). Applies to every locale landing.html and
root index.html so rebuilt pages keep the notice without duplication.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import ai_image_notice_html, strip_ai_notice

ROOT = Path(__file__).resolve().parents[1]
LOCALE_DIRS = {"bg", "cz", "de", "ee", "en", "es", "fr", "gr", "hr", "hu", "it", "lt", "lv", "pl", "pt", "ro", "si", "sk"}

# Folder name → HTML lang (when <html lang> is missing)
GEO_TO_LANG = {"cz": "cs", "gr": "el", "si": "sl", "ee": "et"}


def _is_redirect_stub_index(path: Path, text: str) -> bool:
    """Skip locale/*/index.html that only redirects to landing.html."""
    if path.name != "index.html":
        return False
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return False
    if len(rel.parts) != 3:
        return False
    if rel.parts[0] not in LOCALE_DIRS:
        return False
    return "window.location.replace" in text and "landing.html" in text


def _lang_from_html(text: str) -> str | None:
    m = re.search(r'<html\s[^>]*\blang\s*=\s*["\']([^"\']+)["\']', text, re.I)
    if not m:
        return None
    lang = m.group(1).strip().lower()
    # BCP47: take primary subtag
    return lang.split("-")[0]


def _lang_from_path(path: Path) -> str | None:
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return None
    if rel.parts == ("index.html",):
        return "en"
    if not rel.parts or rel.parts[0] not in LOCALE_DIRS:
        return None
    geo = rel.parts[0]
    return GEO_TO_LANG.get(geo, geo)


def _insert_after_blurb_column(text: str, notice: str) -> str | None:
    """After site-footer__blurb or first column intro paragraph; return new text or None."""

    blurb_re = re.compile(
        r'(<p class="site-footer__blurb"[^>]*>[\s\S]*?</p>)',
        re.IGNORECASE,
    )
    m = blurb_re.search(text)
    if m:
        end = m.end()
        if 'class="site-footer__ai-image-notice"' not in text[m.start() : end + len(notice) + 5]:
            return text[:end] + "\n" + notice + text[end:]
        return text

    # HyperTrimmer & similar: first column uses plain <p style="margin-top:1rem...
    grid_open = text.find('<div class="site-footer__grid">')
    if grid_open == -1:
        return None
    sub = text[grid_open:]
    col_m = re.search(
        r'<div class="site-footer__grid">\s*<div>\s*'
        r'(?:<a[^>]*\bclass="site-logo"[^>]*>[\s\S]*?</a>\s*)'
        r'(<p[^>]*style="[^"]*margin-top:\s*1rem[^"]*"[^>]*>[\s\S]*?</p>)',
        sub,
        re.IGNORECASE,
    )
    if col_m:
        rel_end = grid_open + col_m.end(1)
        snippet = text[grid_open : rel_end + 120]
        if 'class="site-footer__ai-image-notice"' in snippet:
            return text
        return text[:rel_end] + "\n" + notice + text[rel_end:]
    return None


def _insert_before_footer_bottom(text: str, notice: str) -> str | None:
    """Paragraph immediately above site-footer__bottom inside .container (fallback)."""
    if 'class="site-footer__ai-image-notice"' in text:
        return text
    m = re.search(r'(\s*)(<div class="site-footer__bottom">)', text)
    if not m:
        return None
    return text[: m.start()] + m.group(1) + notice + m.group(1) + m.group(2) + text[m.end() :]


def patch_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    lang = _lang_from_html(raw) or _lang_from_path(path)
    if not lang:
        return False

    rel = path.relative_to(ROOT)
    rel_posix = rel.as_posix().lower()

    if path.name == "thank-you.html" or "thank-you" in rel_posix:
        return False

    if path.name == "index.html" and path.parent != ROOT and _is_redirect_stub_index(path, raw):
        return False

    text = strip_ai_notice(raw)
    notice = ai_image_notice_html(lang)

    out = _insert_after_blurb_column(text, notice)
    if out is None:
        out = _insert_before_footer_bottom(text, notice)

    if out is None or out == raw:
        return False
    for attempt in range(5):
        try:
            path.write_text(out, encoding="utf-8", newline="\n")
            return True
        except OSError:
            if attempt == 4:
                raise
            time.sleep(0.15 * (attempt + 1))
    return False


def main() -> None:
    n = 0
    root_index = ROOT / "index.html"
    if root_index.is_file() and patch_file(root_index):
        print("+", "index.html")
        n += 1

    for geo in sorted(LOCALE_DIRS):
        base = ROOT / geo
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.html")):
            rel = path.relative_to(ROOT)
            if rel.parts[-1] == "landing.html":
                pass
            elif rel.parts[-1] == "index.html" and len(rel.parts) >= 2:
                pass
            else:
                continue
            if patch_file(path):
                print("+", rel.as_posix())
                n += 1
    print(f"Done. Updated {n} file(s).")


if __name__ == "__main__":
    main()
