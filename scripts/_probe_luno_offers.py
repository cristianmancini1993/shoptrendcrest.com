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
BASES = [
    "https://shoproomdock.com",
    "https://homeshopspot.com",
    "https://shoptrendcrest.com",
]


def probe(url: str) -> None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "probe/1"})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as exc:
        print("FAIL", url, exc)
        return
    if len(html) < 1500:
        return
    offer = re.search(r'name="offer"[^>]*value="(\d+)"', html)
    lp = re.search(r'name="lp"[^>]*value="(\d+)"', html)
    key = re.search(r'name="_key"[^>]*value="([^"]+)"', html)
    uid = re.search(r'name="uid"[^>]*value="([^"]+)"', html)
    if offer or lp or "LUNO" in html or "Driovo" in html or "luno" in html:
        print(
            "OK",
            url,
            "offer=" + (offer.group(1) if offer else "?"),
            "lp=" + (lp.group(1) if lp else "?"),
            "key=" + ((key.group(1)[:16] + "...") if key else "?"),
            "uid=" + ((uid.group(1)[:8] + "...") if uid else "?"),
            "len=" + str(len(html)),
        )


for geo, oid in OFFERS:
    slug = f"luno-{oid}"
    for base in BASES:
        for path in (
            f"{base}/{geo}/{slug}/landing.html",
            f"{base}/{geo}/{slug}/",
            f"{base}/{geo}/driovo-{oid}/",
            f"{base}/{geo}/driovo-{oid}/landing.html",
        ):
            probe(path)
