#!/usr/bin/env python3
"""Insert Adrice Network forms into Dochura geo landings."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dochura_network_forms", ROOT / "scripts/dochura_network_forms.py"
)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

GEOS = {
    "1912": "de/dochura",
    "1915": "hu/dochura",
    "3163": "es/dochura",
    "3164": "pt/dochura",
    "3167": "pl/dochura",
    "3169": "cz/dochura",
    "3910": "lv/dochura",
    "4321": "sk/dochura",
}

FORM_RE = re.compile(r'<form class="tm-order-form.*?</form>', re.DOTALL)


def patch_landing(path: Path, offer: str) -> None:
    html = path.read_text(encoding="utf-8")
    html = FORM_RE.sub(mod.FORMS[offer], html, count=1)
    path.write_text(html, encoding="utf-8")
    print(f"patched {path.relative_to(ROOT)}")


def main() -> None:
    for offer, rel in GEOS.items():
        patch_landing(ROOT / rel / "landing.html", offer)


if __name__ == "__main__":
    main()
