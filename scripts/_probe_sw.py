#!/usr/bin/env python3
import re
import urllib.request

OFFERS = [
    ("586", "hr"),
    ("642", "cz"),
    ("1633", "pt"),
    ("1842", "gr"),
    ("1843", "bg"),
    ("1844", "ro"),
    ("2297", "es"),
    ("2934", "de"),
    ("3141", "pl"),
]
bases = ["https://shoproomdock.com", "https://shoptrendcrest.com"]
names = ["ultrawatch", "smartwatch", "noventis", "watch", "chrono"]

for base in bases:
    for oid, geo in OFFERS:
        geos = [geo]
        if geo == "gr":
            geos = ["gr", "el"]
        for g in geos:
            for name in names:
                for slug in (f"{name}-{oid}", name):
                    url = f"{base}/{g}/{slug}/"
                    try:
                        r = urllib.request.urlopen(
                            urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
                            timeout=12,
                        )
                        b = r.read(20000).decode("utf-8", "replace")
                        if r.status == 200 and len(b) > 3000:
                            off = re.search(r'name="offer"[^>]*value="(\d+)"', b)
                            print("HIT", oid, g, url, "offer", off.group(1) if off else "?")
                    except Exception:
                        pass
