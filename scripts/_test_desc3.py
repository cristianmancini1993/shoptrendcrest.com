import re
from pathlib import Path

html = Path(__file__).with_name("_src_de_1912.html").read_text(encoding="utf-8")


def remove_desc3_block(s: str) -> str:
    parts = re.split(r"(?=<section class=\"why-block wrap\")", s)
    out = []
    for part in parts:
        if "desc-3.webp" in part.lower():
            continue
        out.append(part)
    return "".join(out)


print("before", html.count("why-block wrap"))
out = remove_desc3_block(html)
print("after", out.count("why-block wrap"))
