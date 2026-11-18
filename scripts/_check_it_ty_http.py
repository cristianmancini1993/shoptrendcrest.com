#!/usr/bin/env python3
import re
import ssl
import urllib.error
import urllib.request

CTX = ssl.create_default_context()
CHECKS = [
    ("IT LP", "https://shoptrendcrest.com/it/calvor-3990/"),
    ("IT TY (target)", "https://shoptrendcrest.com/it/calvor-3990/thank-you/"),
    ("IT old path (expect 404)", "https://shoptrendcrest.com/it/3990/thank-you/"),
]
for label, url in CHECKS:
    req = urllib.request.Request(url, headers={"User-Agent": "check/1"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as resp:
            code = resp.status
            body = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        code = exc.code
        body = ""
    extra = ""
    if label.startswith("IT LP") and code == 200:
        m = re.search(r'name="thankyoupage"[^>]*value="([^"]+)"', body)
        if m:
            extra = f" | thankyoupage={m.group(1)}"
    print(f"{label}: HTTP {code}{extra}")