#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install Google Ads purchase conversion snippet on all thank-you pages."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEND_TO = "AW-18421302840/rPVUCJ-RiOwcELiM-89E"

KEMPPI_CPA = 17.0
IT_EN_BASE_CPA = 13.0

CONVERSION_BLOCK = re.compile(
    r"(?:<!--\s*(?:CPA:[^\n]*|Event snippet for Purchase[^\n]*|Google Ads Purchase conversion[^\n]*)\s*-->\s*)+"
    r"<script>\s*.*?\s*</script>\s*",
    re.DOTALL | re.IGNORECASE,
)

IIFE_CONVERSION_BLOCK = re.compile(
    r"<script>\s*\(function\s*\(\)\s*\{.*?gtag\(\s*['\"]event['\"]\s*,\s*['\"]conversion['\"].*?\}\)\(\);\s*</script>\s*",
    re.DOTALL,
)

GTAG_CONVERSION_SCRIPT = re.compile(
    r"<script>\s*gtag\(\s*['\"]event['\"]\s*,\s*['\"]conversion['\"].*?</script>\s*",
    re.DOTALL,
)

VALUE_RE = re.compile(r"'value':\s*([0-9.]+)")
CONVERSION_VALUE_RE = re.compile(r"CONVERSION_VALUE:\s*([0-9.]+)")


def load_glacierair_cpa() -> dict[str, float]:
    path = ROOT / "scripts" / "glacierair_network_forms.py"
    spec = importlib.util.spec_from_file_location("glacierair_network_forms", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return {str(k): float(v) for k, v in mod.CPA.items()}


GLACIERAIR_CPA = load_glacierair_cpa()


def format_cpa(value: float) -> str:
    return f"{value:.1f}" if float(value).is_integer() else str(value)


def make_snippet(cpa: float) -> str:
    return (
        "<!-- Event snippet for Purchase 1006 - 01.09.2026 conversion page -->\n"
        "<script>\n"
        "  gtag('event', 'conversion', {\n"
        f"      'send_to': '{SEND_TO}',\n"
        f"      'value': {format_cpa(cpa)},\n"
        "      'currency': 'EUR',\n"
        "      'transaction_id': ''\n"
        "      // 'new_customer': true /* calculate dynamically, populate with true/false */,\n"
        "  });\n"
        "</script>\n\n"
    )


def resolve_cpa(ty_path: Path, content: str) -> float:
    slug = ty_path.parent.name

    existing_match = VALUE_RE.search(content)
    existing = float(existing_match.group(1)) if existing_match else None

    if slug.startswith("glacierair-"):
        offer = slug.split("-", 1)[1]
        if offer in GLACIERAIR_CPA:
            return GLACIERAIR_CPA[offer]

    if slug.startswith("kemppi-"):
        return KEMPPI_CPA

    if slug in {"kemppi", "orvyn", "signalix", "sprayvex", "steamix"}:
        return IT_EN_BASE_CPA

    landing = ty_path.parent / "landing.html"
    if not landing.exists() and slug == "fold360":
        landing = ty_path.parent / "index.html"
    if landing.exists():
        landing_match = CONVERSION_VALUE_RE.search(landing.read_text(encoding="utf-8"))
        if landing_match:
            landing_cpa = float(landing_match.group(1))
            if existing is None or existing <= 1.0:
                return landing_cpa

    if existing is not None:
        return existing

    return 15.0


def strip_conversion_snippets(content: str) -> str:
    previous = None
    updated = content
    while updated != previous:
        previous = updated
        updated = CONVERSION_BLOCK.sub("", updated)
        updated = IIFE_CONVERSION_BLOCK.sub("", updated)
        updated = GTAG_CONVERSION_SCRIPT.sub("", updated)
    return updated


def update_thank_you(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    cpa = resolve_cpa(path, original)
    cleaned = strip_conversion_snippets(original)
    snippet = make_snippet(cpa)

    if "</body>" in cleaned:
        updated = cleaned.replace("</body>", snippet + "</body>", 1)
    else:
        updated = cleaned.rstrip() + "\n\n" + snippet

    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    changed: list[Path] = []
    for path in sorted(ROOT.glob("**/thank-you.html")):
        if update_thank_you(path):
            changed.append(path)

    tracking = ROOT / "assets" / "js" / "tracking.js"
    text = tracking.read_text(encoding="utf-8")
    new_text = text.replace(
        "AW-18421302840/piRMCJP23tkcEOiR9rJE",
        SEND_TO,
    )
    if new_text != text:
        tracking.write_text(new_text, encoding="utf-8", newline="\n")
        changed.append(tracking)

    print(f"Updated {len(changed)} files")
    missing = [
        p for p in ROOT.glob("**/thank-you.html")
        if SEND_TO not in p.read_text(encoding="utf-8")
    ]
    print(f"Thank-you pages missing new send_to: {len(missing)}")
    for path in missing[:5]:
        print(f"  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
