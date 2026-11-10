#!/usr/bin/env python3
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OFFERS = [
    ("de", "1912"),
    ("hu", "1915"),
    ("pt", "2480"),
    ("es", "3163"),
    ("pl", "3167"),
    ("cz", "3169"),
    ("lv", "3910"),
    ("sk", "4321"),
]
for geo, oid in OFFERS:
    for kind in ("index", "landing", "thank-you"):
        url = f"https://shoproomdock.com/{geo}/driovo-{oid}/"
        if kind == "thank-you":
            url = f"https://shoproomdock.com/{geo}/driovo-{oid}/thank-you.html"
        elif kind == "landing":
            url = f"https://shoproomdock.com/{geo}/driovo-{oid}/"
        data = urllib.request.urlopen(url, timeout=30).read()
        out = ROOT / "scripts" / f"_src_{geo}_{oid}_{kind}.html"
        out.write_bytes(data)
        print("wrote", out.name, len(data))
