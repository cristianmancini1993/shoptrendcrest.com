#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errs: list[str] = []
for p in sorted(ROOT.glob("**/forvex-*/index.html")):
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
    nat = labs == ["name", "street-address", "tel"]
    nta = labs == ["name", "tel", "street-address"]
    if not (nat or nta):
        errs.append(f"{p.relative_to(ROOT)}: order {labs}")
    if "data-forvex-blocked" in f and "offers.adricenetwork.com" in f:
        errs.append(f"{p.relative_to(ROOT)}: blocked form must not post to network")
    folder = p.parent.name
    oid = folder.replace("forvex-", "")
    offer = re.search(r'name="offer"[^>]*value="(\d+)"', f)
    if not offer or offer.group(1) != oid:
        errs.append(f"{p.relative_to(ROOT)}: offer mismatch {offer}")

ty = list(ROOT.glob("**/forvex-*/thank-you/index.html"))
lp = [p for p in ROOT.glob("**/forvex-*/index.html") if "thank-you" not in p.parts]
print(f"Landings: {len(lp)} TYP: {len(ty)}")
print("OK" if not errs else "\n".join(errs))
