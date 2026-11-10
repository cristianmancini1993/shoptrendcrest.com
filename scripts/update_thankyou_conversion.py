#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install Google Ads purchase conversion snippet on all thank-you pages."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEND_TO = "AW-18510622150/xfhbCIrl7bUdEMbbxvpE"

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
FB_PURCHASE_VALUE_RE = re.compile(
    r"fbq\('track',\s*'Purchase',\s*\{[^}]*value:\s*([0-9.]+)",
    re.IGNORECASE | re.DOTALL,
)

GOOGLE_ADS_ID = "AW-18510622150"
GTAG_HEAD = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ADS_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GOOGLE_ADS_ID}');
</script>
"""


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
        "<!-- Event snippet for Purchase - 862 ACC conversion page -->\n"
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


SLUG_CPA_FALLBACK = {
    "hypertrimmer": 21.0,
    "vacuza": 13.0,
    "dreamora": 13.0,
    "yardmax": 13.0,
    "glacierair": 15.0,
    "fold360": 129.0,
    "verdola": 17.0,
    "treemax": 21.0,
}


def product_dir(ty_path: Path) -> Path:
    if ty_path.name == "index.html" and ty_path.parent.name == "thank-you":
        return ty_path.parent.parent
    return ty_path.parent


def resolve_cpa(ty_path: Path, content: str) -> float:
    conv = CONVERSION_VALUE_RE.search(content)
    if conv:
        return float(conv.group(1))

    pdir = product_dir(ty_path)
    slug = pdir.name

    if slug.startswith("glacierair-"):
        offer = slug.split("-", 1)[1]
        if offer in GLACIERAIR_CPA:
            return GLACIERAIR_CPA[offer]

    if slug.startswith("kemppi-"):
        return KEMPPI_CPA

    base_slug = slug.split("-")[0]
    if base_slug in {"kemppi", "orvyn", "signalix", "sprayvex", "steamix"}:
        return IT_EN_BASE_CPA

    for landing_name in ("landing.html", "index.html"):
        landing = pdir / landing_name
        if landing.exists() and landing.resolve() != ty_path.resolve():
            landing_text = landing.read_text(encoding="utf-8")
            landing_match = CONVERSION_VALUE_RE.search(landing_text)
            if landing_match:
                return float(landing_match.group(1))

    for key, cpa in SLUG_CPA_FALLBACK.items():
        if key in slug:
            return cpa

    fb_match = FB_PURCHASE_VALUE_RE.search(content)
    if fb_match:
        return float(fb_match.group(1))

    existing_match = VALUE_RE.search(content)
    if existing_match:
        existing = float(existing_match.group(1))
        if existing > 1.0:
            return existing

    return 15.0


LOAD_LISTENER_CONVERSION = re.compile(
    r"<!--[^\n]*(?:Purchase|conversion)[^\n]*-->\s*"
    r"<script>\s*window\.addEventListener\('load'[\s\S]*?gtag\(\s*['\"]event['\"]\s*,\s*['\"]conversion['\"][\s\S]*?</script>\s*",
    re.IGNORECASE,
)


def strip_conversion_snippets(content: str) -> str:
    previous = None
    updated = content
    while updated != previous:
        previous = updated
        updated = CONVERSION_BLOCK.sub("", updated)
        updated = IIFE_CONVERSION_BLOCK.sub("", updated)
        updated = GTAG_CONVERSION_SCRIPT.sub("", updated)
        updated = LOAD_LISTENER_CONVERSION.sub("", updated)
    return updated


def is_redirect_thank_you(text: str) -> bool:
    return "window.location.replace" in text


def is_real_thank_you(text: str) -> bool:
    if is_redirect_thank_you(text):
        return False
    return (
        "ty-page" in text
        or "CONVERSION_VALUE" in text
        or FB_PURCHASE_VALUE_RE.search(text) is not None
    )


def update_thank_you(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    if not is_real_thank_you(original):
        return False

    cpa = resolve_cpa(path, original)
    cleaned = strip_conversion_snippets(original)
    snippet = make_snippet(cpa)

    if "gtag" not in cleaned and "<head>" in cleaned:
        cleaned = cleaned.replace("<head>", "<head>\n" + GTAG_HEAD, 1)

    if "</body>" in cleaned:
        updated = cleaned.replace("</body>", snippet + "</body>", 1)
    else:
        updated = cleaned.rstrip() + "\n\n" + snippet

    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def iter_thank_you_pages() -> list[Path]:
    pages: list[Path] = []
    for path in ROOT.rglob("*"):
        if "archive" in path.parts:
            continue
        if "sync-conflict" in path.name:
            continue
        if path.name == "thank-you.html":
            pages.append(path)
        elif path.name == "index.html" and path.parent.name == "thank-you":
            pages.append(path)
    return sorted(pages)


def main() -> None:
    changed: list[Path] = []
    skipped: list[Path] = []
    for path in iter_thank_you_pages():
        text = path.read_text(encoding="utf-8")
        if not is_real_thank_you(text):
            skipped.append(path)
            continue
        if update_thank_you(path):
            changed.append(path)

    tracking = ROOT / "assets" / "js" / "tracking.js"
    text = tracking.read_text(encoding="utf-8")
    new_text = text.replace(
        "AW-18510622150/rPVUCJ-RiOwcELiM-89E",
        SEND_TO,
    )
    new_text = new_text.replace(
        "AW-18510622150/piRMCJP23tkcEOiR9rJE",
        SEND_TO,
    )
    if new_text != text:
        tracking.write_text(new_text, encoding="utf-8", newline="\n")
        changed.append(tracking)

    print(f"Updated {len(changed)} files")
    print(f"Skipped {len(skipped)} redirect thank-you stubs")
    missing = [
        p
        for p in iter_thank_you_pages()
        if is_real_thank_you(p.read_text(encoding="utf-8"))
        and SEND_TO not in p.read_text(encoding="utf-8")
    ]
    print(f"Thank-you pages missing new send_to: {len(missing)}")
    for path in missing[:10]:
        print(f"  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
