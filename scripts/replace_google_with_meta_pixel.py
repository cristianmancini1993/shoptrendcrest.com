#!/usr/bin/env python3
"""Replace Google gtag head snippets with Meta Pixel across HTML files."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIXEL_ID = "1405442415117529"

META_PIXEL = f"""<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

RE_GOOGLE_HEAD = re.compile(
    r"<!-- Google tag \(gtag\.js\) -->\s*"
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
    r"<script>\s*"
    r"window\.dataLayer = window\.dataLayer \|\| \[\];\s*"
    r"function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*"
    r"gtag\('js', new Date\(\)\);\s*"
    r"\s*"
    r"gtag\('config', '[^']+'\);\s*"
    r"</script>",
    re.MULTILINE,
)

RE_PURCHASE_SNIPPET = re.compile(
    r"\n?<!-- Event snippet for Purchase[^>]*-->\s*"
    r"<script>\s*"
    r"\(function \(\) \{[\s\S]*?gtag\('event', 'conversion'[\s\S]*?\}\)\(\);\s*"
    r"</script>",
    re.MULTILINE,
)

RE_PURCHASE_SNIPPET_ALT = re.compile(
    r"\n<script>\s*"
    r"\(function \(\) \{\s*"
    r"var p = new URLSearchParams\(window\.location\.search\);\s*"
    r"gtag\('event', 'conversion',[\s\S]*?\}\)\(\);\s*"
    r"</script>",
    re.MULTILINE,
)

RE_VALUE = re.compile(r"'value':\s*([0-9]+(?:\.[0-9]+)?)")
RE_CURRENCY = re.compile(r"'currency':\s*'([A-Z]{3})'")

SITE_CONFIG_GOOGLE_LINES = [
    re.compile(r"\n\s*GOOGLE_TAG_ID:\s*'[^']*',?"),
    re.compile(r"\n\s*GOOGLE_ADS_CONVERSION_ID:\s*'[^']*',?"),
    re.compile(r"\n\s*GOOGLE_ADS_CONVERSION_LABEL:\s*'[^']*',?"),
    re.compile(r"\n\s*TY_CONVERSION_LABEL:\s*'[^']*',?"),
    re.compile(r"\n\s*GOOGLE_ADS_CONVERSION_SEND_TO:\s*'[^']*',?"),
    re.compile(r"\n\s*META_PIXEL_ID:\s*'',?"),
]


def fb_purchase_snippet(block: str) -> str:
    value_m = RE_VALUE.search(block)
    currency_m = RE_CURRENCY.search(block)
    value = value_m.group(1) if value_m else "1.0"
    currency = currency_m.group(1) if currency_m else "EUR"
    return f"""
<!-- Meta Pixel Purchase event -->
<script>
  (function () {{
    if (!window.fbq) return;
    var p = new URLSearchParams(window.location.search);
    fbq('track', 'Purchase', {{
      value: {value},
      currency: '{currency}',
      order_id: p.get('order_id') || p.get('transaction_id') || p.get('tid') || ''
    }});
  }})();
</script>"""


def process_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if RE_GOOGLE_HEAD.search(text):
        text = RE_GOOGLE_HEAD.sub(META_PIXEL, text, count=1)

    def replace_purchase(m: re.Match) -> str:
        return fb_purchase_snippet(m.group(0))

    text = RE_PURCHASE_SNIPPET.sub(replace_purchase, text)
    text = RE_PURCHASE_SNIPPET_ALT.sub(replace_purchase, text)

    for pat in SITE_CONFIG_GOOGLE_LINES:
        text = pat.sub("", text)

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    updated = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        if process_html(path):
            updated += 1
            print(f"OK {path.relative_to(ROOT)}")
    print(f"Done: {updated} HTML files updated")


if __name__ == "__main__":
    main()
