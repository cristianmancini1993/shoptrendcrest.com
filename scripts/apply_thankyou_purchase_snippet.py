#!/usr/bin/env python3
"""Normalize Meta Purchase snippet on every thank-you page (CPA from CONVERSION_VALUE)."""

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
    "verdola": 17.0,
}

RE_CONVERSION_VALUE = re.compile(r"CONVERSION_VALUE:\s*([0-9]+(?:\.[0-9]+)?)")
RE_FB_VALUE = re.compile(
    r"fbq\('track',\s*'Purchase',\s*\{[^}]*value:\s*([0-9]+(?:\.[0-9]+)?)",
    re.S,
)
RE_PRODUCT_SLUG = re.compile(r"PRODUCT_SLUG:\s*'([^']+)'")
RE_EXISTING_SNIPPET = re.compile(
    r"\n?<!-- Meta Pixel Purchase event -->\s*<script>[\s\S]*?</script>"
    r"|"
    r"\n?<script>\s*"
    r"(?:\(function\s*\(\)\s*\{[\s\S]*?)?fbq\('track',\s*'Purchase'[\s\S]*?</script>",
    re.MULTILINE,
)


def format_value(cpa: float) -> str:
    if abs(cpa - round(cpa)) < 1e-9:
        return f"{int(round(cpa)):.2f}"
    return f"{cpa:.2f}"


def slug_from_path(path: Path) -> str:
    for part in reversed(path.parts[:-1]):
        if part in {
            "en", "de", "es", "fr", "it", "pl", "pt", "ro", "bg", "cz", "sk", "si",
            "hu", "hr", "gr", "ee", "lt", "lv",
        }:
            continue
        base = part.split("-")[0]
        if base in SLUG_CPA_FALLBACK:
            return base
        return part
    return ""


def detect_cpa(text: str, path: Path) -> float:
    m = RE_CONVERSION_VALUE.search(text)
    if m:
        return float(m.group(1))
    m = RE_FB_VALUE.search(text)
    if m:
        return float(m.group(1))
    slug_m = RE_PRODUCT_SLUG.search(text)
    slug = slug_m.group(1) if slug_m else slug_from_path(path)
    for key, cpa in SLUG_CPA_FALLBACK.items():
        if key in slug:
            return cpa
    raise ValueError(f"Could not detect CPA for {path}")


def build_snippet(cpa: float) -> str:
    value = format_value(cpa)
    return f"""
<script>
fbq('track', 'Purchase', {{
value: {value},
currency: '{CURRENCY}'
}});
</script>"""


def ensure_site_config_cpa(text: str, cpa: float) -> str:
    if "window.SITE_CONFIG" not in text:
        return text
    if RE_CONVERSION_VALUE.search(text):
        text = re.sub(
            r"CONVERSION_VALUE:\s*[0-9]+(?:\.[0-9]+)?",
            f"CONVERSION_VALUE: {cpa}",
            text,
            count=1,
        )
    else:
        text = text.replace(
            "window.SITE_CONFIG = {",
            f"window.SITE_CONFIG = {{\n  CONVERSION_VALUE: {cpa},",
            1,
        )
    if "CONVERSION_CURRENCY:" in text:
        text = re.sub(
            r"CONVERSION_CURRENCY:\s*'[A-Z]{3}'",
            f"CONVERSION_CURRENCY: '{CURRENCY}'",
            text,
            count=1,
        )
    elif "CONVERSION_VALUE:" in text:
        text = text.replace(
            f"CONVERSION_VALUE: {cpa},",
            f"CONVERSION_VALUE: {cpa},\n  CONVERSION_CURRENCY: '{CURRENCY}',",
            1,
        )
    return text


def update_file(path: Path) -> float:
    text = path.read_text(encoding="utf-8")
    cpa = detect_cpa(text, path)
    text = ensure_site_config_cpa(text, cpa)
    snippet = build_snippet(cpa)
    if RE_EXISTING_SNIPPET.search(text):
        text = RE_EXISTING_SNIPPET.sub(snippet, text, count=1)
    elif "</body>" in text:
        text = text.replace("</body>", snippet + "\n</body>", 1)
    else:
        raise ValueError(f"No </body> in {path}")
    path.write_text(text, encoding="utf-8", newline="\n")
    return cpa


def main() -> None:
    for path in sorted(ROOT.glob("**/thank-you.html")):
        cpa = update_file(path)
        print(f"OK {path.relative_to(ROOT)} -> €{format_value(cpa)}")
    print("Done.")


if __name__ == "__main__":
    main()
