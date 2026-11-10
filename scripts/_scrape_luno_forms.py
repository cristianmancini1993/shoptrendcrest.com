#!/usr/bin/env python3
import re
import urllib.request

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


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "probe/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


for geo, oid in OFFERS:
    landing = fetch(f"https://shoproomdock.com/{geo}/driovo-{oid}/")
    ty = fetch(f"https://shoproomdock.com/{geo}/driovo-{oid}/thank-you.html")
    lp = re.search(r'name="lp"[^>]*value="(\d+)"', landing)
    key = re.search(r'name="_key"[^>]*value="([^"]+)"', landing)
    cpa = re.search(r"CONVERSION_VALUE:\s*([0-9.]+)", ty)
    print(
        oid,
        geo,
        "lp=" + lp.group(1),
        "key=" + key.group(1),
        "cpa=" + (cpa.group(1) if cpa else "?"),
    )
