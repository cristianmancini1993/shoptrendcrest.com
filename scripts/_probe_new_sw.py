#!/usr/bin/env python3
import re
import urllib.request

NEW = [
    ("779", "si"),
    ("1636", "lt"),
    ("3143", "cz"),
    ("3834", "lv"),
]
for oid, geo in NEW:
    url = f"https://shoproomdock.com/{geo}/smartwatch-{oid}/"
    try:
        b = urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "x"}), timeout=20
        ).read().decode("utf-8")
        def g(name):
            m = re.search(rf'name="{name}"[^>]*value="([^"]*)"', b)
            return m.group(1) if m else ""
        was = re.search(r'class="was"[^>]*>([^<]+)<', b)
        now = re.search(r'class="now"[^>]*>([^<]+)<', b)
        print(
            "OK",
            oid,
            geo,
            len(b),
            "was",
            (was.group(1).strip() if was else "?"),
            "now",
            (now.group(1).strip() if now else "?"),
            "lp",
            g("lp"),
            "key",
            g("_key"),
        )
    except Exception as e:
        print("FAIL", oid, geo, e)
