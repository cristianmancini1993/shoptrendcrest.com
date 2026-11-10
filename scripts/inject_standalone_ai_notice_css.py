# -*- coding: utf-8 -*-
"""Inject minimal CSS so ``.site-footer__ai-notice`` reads well inside standalone footers."""

from __future__ import annotations

import argparse
from pathlib import Path

GSH_BLOCK = """
.gsh-standalone-footer .site-footer__ai-notice {
  max-width: 360px;
  margin: 14px 0 0;
  color: #e2e8f0;
  font-size: 13px;
  line-height: 1.7;
}
""".strip()

HUB_BLOCK = """
.hubaura-standalone-footer .site-footer__ai-notice {
  max-width: 360px;
  margin: 10px 0 0;
  color: #cbd5e1;
  font-size: 13px;
  line-height: 1.7;
}
""".strip()


def ensure_css(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False
    if "gsh-standalone-footer" in text and ".gsh-standalone-footer .site-footer__ai-notice" not in text:
        needle = ".gsh-standalone-footer__heading {"
        if needle in text:
            text = text.replace(needle, GSH_BLOCK + "\n" + needle, 1)
            changed = True
    if "hubaura-standalone-footer" in text and ".hubaura-standalone-footer .site-footer__ai-notice" not in text:
        needle = ".hubaura-standalone-footer__heading {"
        if needle in text:
            text = text.replace(needle, HUB_BLOCK + "\n" + needle, 1)
            changed = True
    if changed:
        path.write_text(text, encoding="utf-8", newline="\n")
    return changed


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, required=True)
    args = p.parse_args()
    root = args.root.resolve()
    n = 0
    for path in sorted(root.rglob("*.html")):
        if "thank-you" in path.parts:
            continue
        if ensure_css(path):
            print(path.relative_to(root))
            n += 1
    print(f"Updated {n} file(s).")


if __name__ == "__main__":
    main()
