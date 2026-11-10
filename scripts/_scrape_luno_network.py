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

for geo, oid in OFFERS:
    landing = urllib.request.urlopen(
        f"https://shoproomdock.com/{geo}/driovo-{oid}/", timeout=30
    ).read().decode("utf-8", "replace")
    ty = urllib.request.urlopen(
        f"https://shoproomdock.com/{geo}/driovo-{oid}/thank-you/", timeout=30
    ).read().decode("utf-8", "replace")
    lp = re.search(r'name="lp"[^>]*value="(\d+)"', landing).group(1)
    key = re.search(r'name="_key"[^>]*value="([^"]+)"', landing).group(1)
    uid = re.search(r'name="uid"[^>]*value="([^"]+)"', landing).group(1)
    wh = re.search(r'name="webhook"[^>]*value="([^"]+)"', landing).group(1)
    cpa = re.search(r"CONVERSION_VALUE:\s*([0-9.]+)", ty)
    print(oid, geo, "lp", lp, "cpa", cpa.group(1) if cpa else "?")
    print("  uid", uid)
    print("  webhook", wh)
    print("  key", key)
