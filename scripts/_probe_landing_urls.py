#!/usr/bin/env python3
"""Probe which URL shape works for landings on a domain."""
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ctx = ssl.create_default_context()
domain = "gadgetshifthub.com"
samples = [
    ROOT / "de" / "yardmax-3188" / "landing.html",
    ROOT / "cz" / "hypertrimmer" / "landing.html",
]


def try_url(url: str) -> tuple[int | None, int]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
            body = r.read().decode("utf-8", errors="replace")
            return r.status, body.count("site-footer__ai-image-notice")
    except Exception as e:
        return None, -1


for p in samples:
    rel = p.relative_to(ROOT).as_posix()
    stem = Path(rel).parent.as_posix()
    bases = [
        f"https://{domain}/{rel}",
        f"https://{domain}/{stem}/",
        f"https://{domain}/{stem}/index.html",
    ]
    print("===", rel, "===")
    for url in bases:
        st, c = try_url(url)
        print(f"  {st!r} notice={c} {url}")
