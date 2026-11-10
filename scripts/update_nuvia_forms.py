#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace Nuvia order-form blocks with 3-field localized forms."""
from __future__ import annotations

import re
from pathlib import Path

from _nuvia_network_forms import FORMS, IT_COD_FORM, TM_FORM_CSS

ROOT = Path(__file__).resolve().parents[1]
FORM_RE = re.compile(
    r'<form class="(?:tm-order-form order-form|cod-form order-form)[^"]*"[^>]*>.*?</form>',
    re.DOTALL,
)


def indent_form(html: str, spaces: int = 8) -> str:
    pad = " " * spaces
    lines = html.strip().splitlines()
    return "\n".join(pad + line if line.strip() else line for line in lines)


def ensure_tm_css(text: str) -> str:
    if ".order-form.tm-order-form label" not in text:
        text = text.replace(
            ".order-form br{ display:none; }",
            ".order-form br{ display:none; }\n" + TM_FORM_CSS.strip(),
        )
    return text


def update_network_file(rel: str, form_html: str) -> None:
    path = ROOT / rel / "index.html"
    text = path.read_text(encoding="utf-8")
    matches = list(FORM_RE.finditer(text))
    if not matches:
        raise RuntimeError(f"No order form found in {path}")

    new_form = indent_form(form_html)
    text = FORM_RE.sub(new_form, text, count=len(matches))
    text = text.replace(
        "FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',",
        "FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/',",
    )
    text = re.sub(r'\n<script src="/assets/js/form-handler\.js" defer></script>', "", text)
    text = ensure_tm_css(text)
    path.write_text(text, encoding="utf-8")
    print(f"updated {rel} ({len(matches)} form(s))")


def update_italian() -> None:
    path = ROOT / "it/nuvia/index.html"
    text = path.read_text(encoding="utf-8")
    matches = list(FORM_RE.finditer(text))
    if not matches:
        raise RuntimeError(f"No order form found in {path}")

    new_form = indent_form(IT_COD_FORM)
    text = FORM_RE.sub(new_form, text, count=len(matches))
    text = ensure_tm_css(text)
    path.write_text(text, encoding="utf-8")
    print(f"updated it/nuvia ({len(matches)} form(s))")


def main() -> None:
    for rel, form_html in FORMS.items():
        update_network_file(rel, form_html)
    update_italian()
    print("done")


if __name__ == "__main__":
    main()
