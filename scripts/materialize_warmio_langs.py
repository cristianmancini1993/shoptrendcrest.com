#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write _warmio_langs/*.py from JSON bundles in _warmio_json/."""
from __future__ import annotations

import importlib.util
import json
import pprint
from pathlib import Path

ROOT = Path(__file__).resolve().parent
JSON_DIR = ROOT / "_warmio_json"
LANG_DIR = ROOT / "_warmio_langs"


def it_phrase() -> dict[str, str]:
    spec = importlib.util.spec_from_file_location(
        "seed", ROOT / "seed_warmio_phrases.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.it_to_phrase(mod.load_it())


def main() -> None:
    from _warmio_patch_common import validate_bundle

    LANG_DIR.mkdir(exist_ok=True)
    bundles: dict[str, dict[str, str]] = {"it": it_phrase()}
    for path in sorted(JSON_DIR.glob("*.json")):
        if path.stem == "it":
            continue
        bundles[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "hu",
        "ro",
        "si",
        "pt",
        "hr",
        "es",
        "de",
        "pl",
        "cs",
        "lv",
        "sk",
        "lt",
    }
    missing = required - set(bundles)
    if missing:
        raise SystemExit(f"Missing JSON locales: {sorted(missing)}")
    for code, patch in bundles.items():
        validate_bundle(code, patch)
        (LANG_DIR / f"{code}.py").write_text(
            "# -*- coding: utf-8 -*-\nPATCH = "
            + pprint.pformat(patch, width=120, sort_dicts=False)
            + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {code}.py")


if __name__ == "__main__":
    main()
