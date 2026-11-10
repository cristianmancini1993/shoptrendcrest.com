#!/usr/bin/env python3
import urllib.request

OFFERS = [
    ("pl", "1745"),
    ("hu", "2653"),
    ("ro", "2657"),
    ("de", "3188"),
    ("lt", "3189"),
    ("cz", "3190"),
    ("pt", "3191"),
    ("es", "3192"),
    ("sk", "4065"),
    ("lv", "4066"),
    ("it", "4183"),
    ("it", "1650"),
]
for geo, oid in OFFERS:
    for path in (f"https://shoptrendcrest.com/{geo}/leafora-{oid}/", f"https://shoptrendcrest.com/{geo}/leafora-{oid}/landing.html"):
        try:
            r = urllib.request.urlopen(path, timeout=15)
            html = r.read(500).decode("utf-8", errors="replace")
            ok = "LEAFORA" in html or "leafora" in html or len(r.read()) > 5000
            print(oid, geo, path, r.status, "ok" if "minichainsaw" in html or "hero" in html or r.length else len(html))
        except Exception as e:
            print(oid, geo, path, "FAIL", e)
