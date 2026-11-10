#!/usr/bin/env python3
"""Insert Adrice Network forms into Miorvella geo landings."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "miorvella_network_forms", ROOT / "scripts/miorvella_network_forms.py"
)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

GEOS = {
    "3038": "es/miorvella",
    "3039": "pt/miorvella",
    "3040": "de/miorvella",
    "3041": "lt/miorvella",
    "3042": "pl/miorvella",
    "3044": "cz/miorvella",
    "2189": "it/miorvella",
}

FORM_RE = re.compile(r'<form class="tm-order-form.*?</form>', re.DOTALL)


def patch_landing(path: Path, offer: str) -> None:
    html = path.read_text(encoding="utf-8")
    html = FORM_RE.sub(mod.FORMS[offer], html, count=1)
    html = html.replace(
        '<script src="/assets/js/form-handler.js" defer></script>\n', ""
    )
    html = re.sub(r"\n  FORM_ENDPOINT: '[^']*',", "", html)
    html = re.sub(r"\n  SUBMITTING_LABEL: '[^']*',", "", html)
    html = re.sub(r"\n  RELAXED_FORM_VALIDATION: true,", "", html)
    path.write_text(html, encoding="utf-8")
    print(f"patched {path.relative_to(ROOT)}")


def main() -> None:
    for offer, rel in GEOS.items():
        patch_landing(ROOT / rel / "landing.html", offer)


if __name__ == "__main__":
    main()
