#!/usr/bin/env python3
import urllib.request
from pathlib import Path

b = urllib.request.urlopen("https://shoproomdock.com/pl/smartwatch-3141/").read().decode()
s = b.index("<!-- ===== WHY BLOCKS")
e = b.index('<footer class="gsh-standalone-footer">')
Path(__file__).with_name("_body_pl_ref.html").write_text(b[s:e], encoding="utf-8")
print("wrote", e - s)
