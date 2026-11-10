#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errs: list[str] = []
for p in sorted(ROOT.glob("**/taigor-*/index.html")):
    if "thank-you" in p.parts:
        continue
    h = p.read_text(encoding="utf-8")
    m = re.search(r'<form class="tm-order-form.*?</form>', h, re.S)
    if not m:
        errs.append(f"{p.relative_to(ROOT)}: no form")
        continue
    f = m.group(0)
    if "postal-code" in f or "address-level2" in f:
        errs.append(f"{p.relative_to(ROOT)}: extra fields")
    labs = re.findall(r'for="(name|tel|street-address)"', f)
    if labs != ["name", "tel", "street-address"]:
        errs.append(f"{p.relative_to(ROOT)}: order {labs}")

ty = list(ROOT.glob("**/taigor-*/thank-you/index.html"))
print(f"Landings: {len(list(ROOT.glob('**/taigor-*/index.html'))) - len(ty)} TYP: {len(ty)}")
print("OK" if not errs else "\n".join(errs))
