import urllib.request, re, sys
url = sys.argv[1]
h = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
print("len", len(h))
for pat, label in [
    (r'name="offer"[^>]*value="([^"]+)"', "offer"),
    (r'name="lp"[^>]*value="([^"]+)"', "lp"),
    (r'name="key"[^>]*value="([^"]+)"', "key"),
    (r'thankyoupage[^>]*value="([^"]+)"', "ty"),
    (r"PRICE:\s*([0-9.]+)", "PRICE"),
    (r"CONVERSION_VALUE:\s*([0-9.]+)", "CPA"),
]:
    m = re.search(pat, h)
    print(label, m.group(1) if m else "?")
print("title", re.search(r"<title>([^<]+)", h).group(1)[:80] if re.search(r"<title>", h) else "?")
