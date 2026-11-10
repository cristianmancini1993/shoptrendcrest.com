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
for oid, geo in OFFERS:
    url = f"https://shoproomdock.com/{geo}/smartwatch-{oid}/"
    b = urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "x"}), timeout=20
    ).read().decode("utf-8")
    def g(name):
        m = re.search(rf'name="{name}"[^>]*value="([^"]*)"', b)
        return m.group(1) if m else ""
    was = re.search(r'class="was"[^>]*>([^<]+)<', b)
    now = re.search(r'class="now"[^>]*>([^<]+)<', b)
    ty_url = f"https://shoproomdock.com/{geo}/smartwatch-{oid}/thank-you.html"
    try:
        ty = urllib.request.urlopen(
            urllib.request.Request(ty_url, headers={"User-Agent": "x"}), timeout=20
        ).read().decode("utf-8")
        cpa = re.search(r"CONVERSION_VALUE:\s*([0-9.]+)", ty)
        cpa_v = cpa.group(1) if cpa else "?"
    except Exception as e:
        ty = ""
        cpa_v = f"err:{e}"
    print(
        oid,
        geo,
        "was",
        was.group(1).strip() if was else "?",
        "now",
        now.group(1).strip() if now else "?",
        "ty_len",
        len(ty),
        "ty_cpa",
        cpa_v,
        "lp",
        g("lp"),
        "key",
        g("_key"),
        "webhook",
        g("webhook")[-20:],
    )
