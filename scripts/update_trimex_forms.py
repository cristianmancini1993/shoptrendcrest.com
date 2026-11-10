#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject Adrice network forms into TRIMEX geo landings."""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _trimex_network_forms import FORM_META, WEBHOOK, build_forms

ROOT = Path(__file__).resolve().parents[1]
FORM_RE = re.compile(
    r'<form class="tm-order-form order-form"[^>]*>.*?</form>',
    re.DOTALL,
)
NOTE_RE = re.compile(
    r'<form class="tm-order-form order-form"[^>]*>.*?<p class="form-note">(.*?)</p>\s*</form>',
    re.DOTALL,
)


def update_site_config(text: str, meta: dict) -> str:
    text = re.sub(r"  FORM_OFFER: '[^']*',", f"  FORM_OFFER: '{meta['offer']}',", text, count=1)
    text = re.sub(r"  FORM_LP: '[^']*',", f"  FORM_LP: '{meta['lp']}',", text, count=1)
    text = re.sub(r"  FORM_WEBHOOK: '[^']*',", f"  FORM_WEBHOOK: '{WEBHOOK}',", text, count=1)
    text = re.sub(r"  FORM_KEY: '[^']*',", f"  FORM_KEY: '{meta['key']}',", text, count=1)
    return text


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    notes: dict[str, str] = {}
    for rel in FORM_META:
        path = ROOT / rel / "index.html"
        text = path.read_text(encoding="utf-8")
        m = NOTE_RE.search(text)
        if not m:
            raise RuntimeError(f"No form-note in {path}")
        notes[rel] = m.group(1)

    forms = build_forms(notes)

    for rel, form_html in forms.items():
        path = ROOT / rel / "index.html"
        text = path.read_text(encoding="utf-8")
        if not FORM_RE.search(text):
            raise RuntimeError(f"No order form in {path}")
        text = FORM_RE.sub(form_html, text, count=1)
        text = update_site_config(text, FORM_META[rel])
        path.write_text(text, encoding="utf-8")
        print(f"updated {rel}  offer={FORM_META[rel]['offer']}  lp={FORM_META[rel]['lp']}")

    print("done")


if __name__ == "__main__":
    main()
