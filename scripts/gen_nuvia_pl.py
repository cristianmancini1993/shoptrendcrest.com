#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Nuvia landing + thank-you for Poland offer #3141."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("gen_nuvia_geos", ROOT / "scripts" / "gen_nuvia_geos.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

OFFER = {
    "geo": "pl",
    "lang": "pl",
    "slug": "nuvia",
    "product": "Nuvia™",
    "currency": "PLN",
    "price": 199,
    "cpa": 16,
    "offer_id": "3141",
    "phone": "+48 512 345 678",
}


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    c = mod.COPY["pl"]
    it_index = mod.IT_INDEX.read_text(encoding="utf-8")
    it_ty = mod.IT_TY.read_text(encoding="utf-8")

    out_dir = ROOT / OFFER["geo"] / OFFER["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)

    from scripts.ai_image_notice_i18n import insert_ai_notice_in_site_footer

    index_html = mod.transform_index(it_index, OFFER, c)
    index_html = insert_ai_notice_in_site_footer(index_html, OFFER["lang"])
    ty_html = mod.transform_thank_you(it_ty, OFFER, c)

    (out_dir / "index.html").write_text(index_html, encoding="utf-8")
    (out_dir / "thank-you.html").write_text(ty_html, encoding="utf-8")

    print(
        f"OK pl/nuvia/  price={mod.fmt_price(OFFER['price'], OFFER['currency'])}  "
        f"was={mod.fmt_price(mod.was_price(OFFER['price']), OFFER['currency'])}  "
        f"offer=#{OFFER['offer_id']}"
    )
    print("https://gadgetshifthub.com/pl/nuvia/")
    print("https://gadgetshifthub.com/pl/nuvia/thank-you.html")


if __name__ == "__main__":
    main()
