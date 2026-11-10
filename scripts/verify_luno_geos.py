#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFERS = {
    "1912": ("de", 92.0, "EUR"),
    "1915": ("hu", 29999.0, "HUF"),
    "2480": ("pt", 79.0, "EUR"),
    "3163": ("es", 79.0, "EUR"),
    "3167": ("pl", 339.0, "PLN"),
    "3169": ("cz", 1899.0, "CZK"),
    "3910": ("lv", 85.0, "EUR"),
    "4321": ("sk", 74.0, "EUR"),
}
BAD = ("Driovo", "driovo", "shoproomdock", "desc-3.webp", "Pagamento alla consegna", "Cliente verificata", "In circa 20 minuti")
ITALIAN = ("Ordina LUNO", "Nessun anticipo", "Domande frequenti", "Stendino classico")


def check_file(path: Path, offer_id: str) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8")
    for b in BAD:
        if b in text:
            issues.append(f"contains {b!r}")
    if path.name == "landing.html":
        if text.count("why-block wrap") != 3:
            issues.append(f"why-blocks={text.count('why-block wrap')} expected 3")
        if f'value="{offer_id}"' not in text:
            issues.append("missing offer id in form")
        if "forms/html/js-v2/" not in text:
            issues.append("missing adrice js-v2")
        if "name=\"subid\"" in text:
            issues.append("unexpected subid field")
    if path.name == "thank-you.html":
        if "CONVERSION_VALUE" not in text:
            issues.append("missing CONVERSION_VALUE")
    return issues


def main() -> None:
    ok = True
    for oid, (geo, _price, _cur) in OFFERS.items():
        slug = f"luno-{oid}"
        for name in ("index.html", "landing.html", "thank-you.html"):
            p = ROOT / geo / slug / name
            if not p.exists():
                print("MISSING", p)
                ok = False
                continue
            issues = check_file(p, oid)
            if issues:
                ok = False
                print(f"FAIL {geo}/{slug}/{name}:", "; ".join(issues))
            else:
                print(f"OK   {geo}/{slug}/{name}")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
