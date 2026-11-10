#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "scripts" / "AI_NOTICE_VERIFIED_URLS.txt"
lines = ["https://gadgetshifthub.com/"]
for p in sorted(ROOT.rglob("*.html")):
    rel = p.relative_to(ROOT).as_posix()
    if "thank-you" in rel:
        continue
    if p.name not in ("index.html", "landing.html"):
        continue
    raw = p.read_text(encoding="utf-8")
    if "assets/img/products" not in raw:
        continue
    if 'data-ai-disclosure="1"' not in raw:
        continue
    path = "/" + rel.replace("index.html", "").replace("landing.html", "")
    if not path.endswith("/"):
        path += "/"
    lines.append(f"https://gadgetshifthub.com{path}")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {len(lines)} URLs to {out}")
