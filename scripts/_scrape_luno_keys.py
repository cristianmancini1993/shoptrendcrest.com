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

print("FORMS = {")
for geo, oid in OFFERS:
    html = urllib.request.urlopen(
        f"https://shoproomdock.com/{geo}/driovo-{oid}/",
        timeout=30,
    ).read().decode("utf-8", "replace")
    lp = re.search(r'name="lp"[^>]*value="(\d+)"', html).group(1)
    key = re.search(r'name="_key"[^>]*value="([^"]+)"', html).group(1)
    print(f'    "{oid}": {{"lp": "{lp}", "key": "{key}"}},')
print("}")
