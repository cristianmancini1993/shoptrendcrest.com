"""One-off: IT CENDORA on shoptrendcrest.com from shopgearspot template + HGS footer."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SG = ROOT.parent / "shopgearspot.com"

HOME_FOOTER_INDEX = Path(ROOT / "it/warmio-3990/index.html").read_text(encoding="utf-8")
m = re.search(r"<footer class=\"site-footer\">.*?</footer>", HOME_FOOTER_INDEX, re.DOTALL)
if not m:
    raise SystemExit("footer not found in warmio-3990")
HOME_FOOTER = m.group(0) + "\n\n<script src=\"/assets/js/noreva-landing.js\" defer></script>\n<script src=\"/assets/js/main.js\" defer></script>"

HOME_FOOTER_TY = Path(ROOT / "it/warmio-3990/thank-you/index.html").read_text(encoding="utf-8")
m2 = re.search(r"<footer class=\"site-footer\">.*?</footer>", HOME_FOOTER_TY, re.DOTALL)
if not m2:
    raise SystemExit("ty footer not found")
HOME_FOOTER_TY_BLOCK = m2.group(0)


def domain_patch(html: str) -> str:
    html = html.replace("AW-18437425584", "AW-18421302840")
    html = html.replace("shopgearspot.com", "shoptrendcrest.com")
    html = html.replace("info@shopgearspot.com", "info@shoptrendcrest.com")
    return html


src = (SG / "it/cendora/index.html").read_text(encoding="utf-8")
idx = domain_patch(src)
idx = re.sub(
    r"<footer class=\"site-footer\">.*?</footer>\s*<script src=\"/assets/js/noreva-landing.js\" defer></script>",
    HOME_FOOTER,
    idx,
    count=1,
    flags=re.DOTALL,
)

ty_src = (SG / "it/cendora/thank-you.html").read_text(encoding="utf-8")
ty = domain_patch(ty_src)
ty = re.sub(
    r"<footer class=\"site-footer\">.*?</footer>",
    HOME_FOOTER_TY_BLOCK,
    ty,
    count=1,
    flags=re.DOTALL,
)
ty = ty.replace(
    'alt="shopgearspot team:',
    'alt="shoptrendcrest team:',
)

out = ROOT / "it/cendora"
(out / "thank-you").mkdir(parents=True, exist_ok=True)
(out / "index.html").write_text(idx, encoding="utf-8", newline="\n")
(out / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")

(out / "landing.html").write_text(
    (SG / "it/cendora/landing.html").read_text(encoding="utf-8").replace("shopgearspot.com", "shoptrendcrest.com"),
    encoding="utf-8",
    newline="\n",
)
(out / "thank-you/index.html").write_text(
    (SG / "it/cendora/thank-you/index.html").read_text(encoding="utf-8").replace(
        "shopgearspot.com", "shoptrendcrest.com"
    ),
    encoding="utf-8",
    newline="\n",
)
print("OK", out)
