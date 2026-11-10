#!/usr/bin/env python3
import re
import urllib.request

for oid, geo in [("586", "hr"), ("642", "cz"), ("3141", "pl"), ("1844", "ro")]:
    url = f"https://shoproomdock.com/{geo}/smartwatch-{oid}/"
    b = urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "x"}), timeout=20
    ).read().decode("utf-8")
    print("===", oid, geo, len(b))
    m = re.search(r'name="offer"[^>]*value="([^"]+)"', b)
    print("offer", m.group(1) if m else "?")
    m = re.search(r'name="lp"[^>]*value="([^"]+)"', b)
    print("lp", m.group(1) if m else "?")
    for cls in ("old", "new", "price-old", "price-new", "was", "now"):
        m = re.search(rf'class="{cls}"[^>]*>([^<]+)<', b)
        if m:
            print(cls, m.group(1).strip())
    # generic price blocks
    for m in re.finditer(r'<span class="[^"]*price[^"]*"[^>]*>([^<]+)</span>', b):
        print("span", m.group(1).strip())
    imgs = sorted(set(re.findall(r"/assets/img/products/[^\"'\s>]+", b)))
    print("imgs", imgs[:5], "count", len(imgs))
    print("Ultrawatch", "Ultrawatch" in b, "Noventis", "Noventis" in b)
