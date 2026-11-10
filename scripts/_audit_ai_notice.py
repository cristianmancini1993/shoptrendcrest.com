# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
NON = frozenset(
    {
        "thank-you",
        "assets",
        ".github",
        "about-us",
        "contact-us",
        "privacy-policy",
        "terms-conditions",
        "cookie-policy",
        "shipping-policy",
        "refund-policy",
        "scripts",
        "content",
        "node_modules",
        "archive",
        "backup",
    }
)


def is_product_index(p: Path) -> bool:
    if p.name != "index.html":
        return False
    parts = p.relative_to(root).parts
    if not parts or parts[0] in ("scripts", "content"):
        return False
    if any(x in NON for x in parts):
        return False
    return True


missing = []
for p in sorted(root.rglob("*.html")):
    rel = p.relative_to(root)
    if "thank-you" in rel.parts:
        continue
    if any(x in rel.parts for x in ("archive", "backup", "content")):
        continue
    is_home = rel == Path("index.html")
    is_landing = p.name == "landing.html"
    is_offer = is_product_index(p)
    if not (is_home or is_landing or is_offer):
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "window.location.replace" in t and "<footer" not in t.lower():
        continue
    if "<footer" not in t.lower():
        continue
    if 'data-ai-disclosure="1"' not in t:
        missing.append(str(rel).replace("\\", "/"))

print("missing count", len(missing))
for m in missing:
    print(m)
