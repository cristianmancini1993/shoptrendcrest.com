#!/usr/bin/env python3
"""Add Meta Pixel Purchase snippet to every thank-you page."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRENCY = "EUR"

SLUG_CPA_FALLBACK = {
    "hypertrimmer": 21.0,
    "vacuza": 13.0,
    "dreamora": 13.0,
    "yardmax": 13.0,
    "glacierair": 15.0,
    "fold360": 129.0,
}

RE_CONVERSION_VALUE = re.compile(r"CONVERSION_VALUE:\s*([0-9]+(?:\.[0-9]+)?)")
RE_FIRE_VALUE = re.compile(r"fireMeersmartThankYouConversion\(\{[^}]*value:\s*([0-9]+(?:\.[0-9]+)?)", re.S)
RE_TRACK_PURCHASE = re.compile(r"trackPurchase\(\s*([0-9]+(?:\.[0-9]+)?)\s*,\s*'([A-Z]{3})'\s*\)")
RE_PRODUCT_SLUG = re.compile(r"PRODUCT_SLUG:\s*'([^']+)'")
RE_OLD_SNIPPET = re.compile(
    r"\n?<!-- Event snippet for Purchase[^>]*-->\s*"
    r"<script>\s*"
    r"(?:window\.addEventListener\('load'[\s\S]*?</script>|"
    r"\(function\s*\(\)[\s\S]*?</script>)",
    re.I,
)
RE_HEAD_TRACK = re.compile(
    r"\n<script>\s*window\.addEventListener\('load',\s*function\s*\(\)\s*\{\s*"
    r"if\s*\(window\.trackPurchase\)[\s\S]*?</script>",
)
RE_FOOTER_TRACK = re.compile(
    r"\n<script>\s*window\.addEventListener\('load',\s*function\s*\(\)\s*\{\s*"
    r"(?:if\s*\(window\.fireMeersmartThankYouConversion\)[\s\S]*?|"
    r"if\s*\(window\.trackPurchase\)[\s\S]*?)"
    r"\}\);\s*</script>",
)
RE_BROKEN_FOOTER = re.compile(
    r"\n<script>\s*\(function\s*\(\)\s*\{[\s\S]*?<script>[\s\S]*?</script>\s*(?=</body>)",
)
RE_HEAD_PLACEHOLDER = re.compile(r"\n<!-- Event snippet for Purchase conversion page -->\s*\n?")


def slug_from_path(path: Path) -> str:
    parts = path.parts
    for part in reversed(parts[:-1]):
        if part not in {"en", "de", "es", "fr", "it", "pl", "pt", "ro", "bg", "cz", "sk", "si", "hu", "hr", "gr", "ee", "lt", "lv"}:
            base = part.split("-")[0]
            if base in SLUG_CPA_FALLBACK:
                return base
            return part
    return ""


def detect_cpa(text: str, path: Path) -> float:
    m = RE_CONVERSION_VALUE.search(text)
    if m:
        return float(m.group(1))

    m = RE_FIRE_VALUE.search(text)
    if m:
        return float(m.group(1))

    purchases = [(float(v), cur) for v, cur in RE_TRACK_PURCHASE.findall(text)]
    eur_cpas = [v for v, cur in purchases if cur == "EUR" and v <= 30]
    if eur_cpas:
        return min(eur_cpas)

    slug_m = RE_PRODUCT_SLUG.search(text)
    slug = slug_m.group(1) if slug_m else slug_from_path(path)
    for key, cpa in SLUG_CPA_FALLBACK.items():
        if key in slug:
            return cpa

    if purchases:
        return min(v for v, _ in purchases)

    raise ValueError(f"Could not detect CPA for {path}")


def build_snippet(cpa: float) -> str:
    value = f"{cpa:.2f}" if abs(cpa - round(cpa)) > 1e-9 else f"{int(round(cpa)):.2f}"
    return f"""
<script>
fbq('track', 'Purchase', {{
value: {value},
currency: '{CURRENCY}'
}});
</script>
"""


def update_file(path: Path) -> float:
    text = path.read_text(encoding="utf-8")
    cpa = detect_cpa(text, path)

    text = RE_HEAD_PLACEHOLDER.sub("\n", text)
    text = RE_BROKEN_FOOTER.sub("", text)
    text = RE_OLD_SNIPPET.sub("", text)
    text = RE_HEAD_TRACK.sub("", text)
    text = RE_FOOTER_TRACK.sub("", text)

    if "fbq('track', 'Purchase'" not in text:
        if "</body>" not in text:
            raise ValueError(f"No </body> in {path}")
        text = text.replace("</body>", build_snippet(cpa) + "\n</body>", 1)

    if "CONVERSION_VALUE:" not in text and "window.SITE_CONFIG" in text:
        text = text.replace(
            "  PRICE:",
            f"  CONVERSION_VALUE: {cpa},\n  CONVERSION_CURRENCY: '{CURRENCY}',\n  PRICE:",
            1,
        )

    path.write_text(text, encoding="utf-8", newline="\n")
    return cpa


def main():
    paths = sorted(ROOT.glob("**/thank-you.html"))
    updated = []
    for path in paths:
        cpa = update_file(path)
        updated.append((str(path.relative_to(ROOT)), cpa))
        print(f"OK {path.relative_to(ROOT)} -> CPA {cpa}")

    print(f"Done: {len(updated)} thank-you pages")


if __name__ == "__main__":
    main()
