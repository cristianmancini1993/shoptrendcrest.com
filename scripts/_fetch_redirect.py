import urllib.request, re, sys

url = sys.argv[1]
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    final = r.geturl()
    body = r.read().decode("utf-8", errors="replace")
print("final", final)
print("len", len(body))
m = re.search(r'location\.replace\([^)]+\'([^\']+)\'', body)
if m:
    print("js", m.group(1))
m2 = re.search(r'content="0;url=([^"]+)"', body)
if m2:
    print("meta", m2.group(1))
