#!/usr/bin/env python3
from pathlib import Path

b = Path(__file__).resolve().parents[1] / "it" / "noventis" / "landing.html"
html = b.read_text(encoding="utf-8")
s = html.index("<!-- ===== WHY BLOCKS")
e = html.index('<footer class="site-footer">')
Path(__file__).with_name("_body_it_ref.html").write_text(html[s:e], encoding="utf-8")
print(len(html[s:e]))
