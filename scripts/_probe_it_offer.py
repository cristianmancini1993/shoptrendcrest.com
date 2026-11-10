import urllib.request
import re

for p in ("it/leafora-4188/", "it/leafora-4183/", "it/leafora-1650/", "it/leafora/"):
    u = "https://shoptrendcrest.com/" + p
    try:
        b = urllib.request.urlopen(u, timeout=20).read(12000).decode("utf-8", errors="replace")
        o = re.search(r'name="offer"[^>]*value="([^"]+)"', b)
        print(p, "len", len(b), "offer", o.group(1) if o else "-", "4188" in b, "4183" in b)
    except Exception as e:
        print(p, "FAIL", getattr(e, "code", e))
