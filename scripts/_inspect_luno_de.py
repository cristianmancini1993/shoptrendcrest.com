import re
import urllib.request

html = urllib.request.urlopen("https://shoproomdock.com/de/driovo-1912/", timeout=30).read().decode()
print("why-blocks", html.count("why-block wrap"))
h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
print("h1", re.sub(r"\s+", " ", h1.group(1))[:200] if h1 else "?")
for m in re.finditer(r'num-eyebrow">([^<]+)', html):
    print("eyebrow", m.group(1))
lp = re.search(r'name="lp"[^>]*value="(\d+)"', html)
key = re.search(r'name="_key"[^>]*value="([^"]+)"', html)
print("lp", lp.group(1) if lp else None)
print("key", key.group(1) if key else None)
