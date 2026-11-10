#!/usr/bin/env python3
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "warmio_network_forms",
    Path(__file__).with_name("warmio_network_forms.py"),
)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

errs: list[str] = []
landings = [p for p in ROOT.glob("**/warmio-*/index.html") if "thank-you" not in p.parts]
for p in sorted(landings):
    h = p.read_text(encoding="utf-8")
    m = re.search(r'<form class="tm-order-form.*?</form>', h, re.S)
    if not m:
        errs.append(f"{p.relative_to(ROOT)}: no form")
        continue
    f = m.group(0)
    offer_m = re.search(r'name="offer"[^>]*value="([^"]*)"', f)
    offer = offer_m.group(1) if offer_m else ""
    if not offer:
        errs.append(f"{p.relative_to(ROOT)}: empty offer")
    ty_m = re.search(r'name="thankyoupage"[^>]*value="([^"]*)"', f)
    if not ty_m or "/thank-you/" not in ty_m.group(1):
        errs.append(f"{p.relative_to(ROOT)}: bad thankyoupage")
    if offer not in mod.FORMS:
        errs.append(f"{p.relative_to(ROOT)}: no network form for offer {offer}")
        continue
    exp = mod.FORMS[offer]
    for field in ("lp", "_key", "webhook"):
        vm = re.search(rf'name="{field}"[^>]*value="([^"]*)"', exp)
        if not vm:
            continue
        hm = re.search(rf'name="{field}"[^>]*value="([^"]*)"', f)
        if not hm or hm.group(1) != vm.group(1):
            errs.append(f"{p.relative_to(ROOT)}: {field} mismatch")
    if mod.WEBHOOK not in f:
        errs.append(f"{p.relative_to(ROOT)}: webhook")
    expected = mod.FIELD_ORDER.get(offer, ["name", "tel", "street-address"])
    labs = re.findall(
        r'for="(name|tel|street-address|postal-code|address-level2)"',
        f,
    )
    if labs != expected:
        errs.append(f"{p.relative_to(ROOT)}: order {labs} expected {expected}")

ty = list(ROOT.glob("**/warmio-*/thank-you/index.html"))
print(f"Landings: {len(landings)} TYP: {len(ty)} MISSING forms: {len(mod.MISSING_OFFERS)}")
print("OK" if not errs else "\n".join(errs))
