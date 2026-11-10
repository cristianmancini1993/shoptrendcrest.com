#!/usr/bin/env python3
"""One-off: replace Google gtag blocks in generator scripts with Meta Pixel."""

import importlib.util
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("_meta_pixel_head", SCRIPT_DIR / "_meta_pixel_head.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

RE_GOOGLE_HEAD = re.compile(
    r"<!-- Google tag \(gtag\.js\) -->\s*"
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
    r"<script>.*?</script>\s*",
    re.DOTALL,
)

RE_GTAG_PURCHASE = re.compile(
    r"<script>\s*"
    r"\(function \(\) \{\{?\s*"
    r"var p = new URLSearchParams\(window\.location\.search\);\s*"
    r"gtag\('event', 'conversion',[\s\S]*?\}\)\(\);\s*"
    r"</script>",
    re.MULTILINE,
)


def escape_for_format(snippet: str) -> str:
    return snippet.replace("{", "{{").replace("}", "}}")


def purchase_replacement(match: re.Match) -> str:
    block = match.group(0)
    value_m = re.search(r"'value':\s*(\{cpa\}|[0-9]+(?:\.[0-9]+)?)", block)
    if value_m and value_m.group(1) == "{cpa}":
        return escape_for_format(
            mod.meta_purchase_script(0).replace("0", "{cpa}")
        )
    value = value_m.group(1) if value_m else "1.0"
    currency_m = re.search(r"'currency':\s*'([A-Z]{3})'", block)
    currency = currency_m.group(1) if currency_m else "USD"
    return escape_for_format(mod.meta_purchase_script(float(value), currency))


def main() -> None:
    for path in sorted(SCRIPT_DIR.glob("*.py")):
        if path.name in ("_meta_pixel_head.py", "replace_google_with_meta_pixel.py", "patch_generators_meta_pixel.py"):
            continue
        text = path.read_text(encoding="utf-8")
        if "googletagmanager" not in text and "gtag('event'" not in text:
            continue
        new = RE_GOOGLE_HEAD.sub(mod.META_PIXEL_HEAD_ESCAPED + "\n", text)
        new = RE_GTAG_PURCHASE.sub(purchase_replacement, new)
        if "normalize_gtag" in new:
            new = new.replace(
                "def normalize_gtag(html: str) -> str:",
                "def normalize_meta_pixel(html: str) -> str:",
            )
            new = re.sub(
                r"def normalize_meta_pixel\(html: str\) -> str:\s*"
                r'html = re\.sub\(\s*'
                r'r\'<script async src="https://www\.googletagmanager\.com/gtag/js[^"]*"></script>\\s*<script>\[\\s\\S\]\*?</script>\\s*\',\s*'
                r"\"\",\s*"
                r"html,\s*"
                r"count=1,\s*"
                r"\)\s*"
                r"return html",
                "def normalize_meta_pixel(html: str) -> str:\n    return html",
                new,
                flags=re.DOTALL,
            )
            new = new.replace("normalize_gtag(html)", "normalize_meta_pixel(html)")
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            print(f"patched {path.name}")


if __name__ == "__main__":
    main()
