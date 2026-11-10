#!/usr/bin/env python3
import re
import urllib.request

OFFERS = [
    ("586", "hr"),
    ("779", "si"),
    ("1633", "pt"),
    ("1636", "lt"),
    ("1842", "gr"),
    ("1843", "bg"),
    ("1844", "ro"),
    ("2297", "es"),
    ("2934", "de"),
    ("3141", "pl"),
    ("3143", "cz"),
    ("3834", "lv"),
]
for oid, geo in OFFERS:
    b = urllib.request.urlopen(
        f"https://shoproomdock.com/{geo}/smartwatch-{oid}/",
        timeout=25,
    ).read().decode("utf-8", "replace")
    bad = []
    if "družbenimi" in b or "zapestju" in b and geo == "hr":
        bad.append("sl")
    if "TRANSLATOR" in b or "PRIEDAS" in b:
        bad.append("lt-artifact")
    if re.search(r'class="lbl">Ore</div>', b):
        bad.append("it-timer")
    if "All rights reserved" in b and geo not in ("en",):
        bad.append("en-footer")
    if "♪" in b or 'alt="Smartwatch' not in b and "noventis/hero" in b:
        if "alt=" not in b[b.find("noventis/hero"): b.find("noventis/hero") + 120]:
            bad.append("broken-alt")
    print(oid, geo, "bad" if bad else "ok", bad or "")
