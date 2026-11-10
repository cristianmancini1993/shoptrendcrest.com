#!/usr/bin/env python3
"""Generate Topper thank-you pages per mattress size."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "it" / "treemax"
base = ROOT.joinpath("thank-you.html").read_text(encoding="utf-8")
base = base.replace("TreeMax™", "Topper")
base = base.replace("ordine TreeMax", "ordine Topper")

for size in ("140x200", "160x200", "180x200"):
    html = base
    html = html.replace(
        "<title>Ordine ricevuto",
        f"<title>Ordine ricevuto — Topper {size}",
    )
    html = html.replace(
        "Il tuo ordine Topper è in elaborazione",
        f"Il tuo ordine Topper {size} è in elaborazione",
    )
    html = html.replace(
        'content="Il tuo ordine Topper è stato registrato',
        f'content="Il tuo ordine Topper {size} è stato registrato',
    )
    out = ROOT / f"thank-you-{size}.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.name}")

ROOT.joinpath("thank-you.html").write_text(base, encoding="utf-8")
print("updated thank-you.html")
