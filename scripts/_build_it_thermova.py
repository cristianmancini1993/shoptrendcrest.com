#!/usr/bin/env python3
"""Thermova IT landing helpers.

Edit it/flamora/index.html directly (source of truth for IT).
Multi-geo fireplace LPs: run scripts/gen_flamora_fireplace_geos.py
This script only regenerates thank-you.html from the trimex template.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "it/flamora"
OUT.mkdir(parents=True, exist_ok=True)

ty = (ROOT / "it/trimex-3209/thank-you.html").read_text(encoding="utf-8")
for a, b in [
    ("trimex-3209", "flamora"),
    ("TRIMEX™", "FLAMORA™"),
    ("TRIMEX", "FLAMORA"),
    ("3209", "2635"),
    ("79.99", "96"),
    ("trackPurchase(79.99", "trackPurchase(96"),
    ("Decespugliatore", "Camino elettrico"),
]:
    ty = ty.replace(a, b)
(OUT / "thank-you.html").write_text(ty, encoding="utf-8")
print("Built", OUT / "thank-you.html")
