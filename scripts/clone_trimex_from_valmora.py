#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clone Italian VALMORA (cookware) landing to TRIMEX."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "it/valmora"
DST_DIR = ROOT / "it/trimex"
IMG_SRC = ROOT / "assets/img/products/valmora"
IMG_DST = ROOT / "assets/img/products/trimex"
CACHE = "20260923"


def transform(text: str) -> str:
    text = text.replace("/it/valmora/", "/it/trimex/")
    text = text.replace("/products/valmora/", "/products/trimex/")
    text = text.replace("PRODUCT_SLUG: 'valmora'", "PRODUCT_SLUG: 'trimex'")
    text = text.replace("it-valmora-v1", "it-trimex-v1")
    text = text.replace("OFFER_NAME: 'VALMORA IT'", "OFFER_NAME: 'TRIMEX IT'")
    text = text.replace(
        "FORM_WEBHOOK: 'https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh',",
        "FORM_WEBHOOK: '',",
    )
    text = text.replace("VALMORA", "TRIMEX")
    text = re.sub(r"\?v=[^\"']+", f"?v={CACHE}", text)
    return text


def main() -> None:
    DST_DIR.mkdir(parents=True, exist_ok=True)
    if IMG_DST.exists():
        shutil.rmtree(IMG_DST)
    shutil.copytree(IMG_SRC, IMG_DST)

    for name in ("index.html", "thank-you.html", "landing.html"):
        out = transform((SRC_DIR / name).read_text(encoding="utf-8"))
        (DST_DIR / name).write_text(out, encoding="utf-8")
        print(f"wrote it/trimex/{name}")

    print(f"images: assets/img/products/trimex/ ({len(list(IMG_DST.iterdir()))} files)")


if __name__ == "__main__":
    main()
