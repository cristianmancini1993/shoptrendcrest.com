# -*- coding: utf-8 -*-
"""Rebuild _zelto_i18n.py from locale modules + IT source."""
from __future__ import annotations

import importlib
from pathlib import Path

from _zelto_it_strings import IT_STRINGS

LOCALE_MODULES = {
    "hu": "locale_hu",
    "ro": "locale_ro",
    "si": "locale_si",
    "pt": "locale_pt",
    "hr": "locale_hr",
    "es": "locale_es",
    "de": "locale_de",
    "pl": "locale_pl",
    "cs": "locale_cs",
    "lv": "locale_lv",
    "sk": "locale_sk",
    "lt": "locale_lt",
}

ROOT = Path(__file__).resolve().parent


def load_strings(code: str) -> dict:
    mod = importlib.import_module(LOCALE_MODULES[code])
    return dict(mod.STRINGS)


def main() -> None:
    missing = [c for c in LOCALE_MODULES if not (ROOT / f"{LOCALE_MODULES[c]}.py").exists()]
    if missing:
        raise SystemExit(f"Missing locale modules: {missing}")

    translations = {"it": dict(IT_STRINGS)}
    for code in LOCALE_MODULES:
        translations[code] = load_strings(code)

    out = ROOT / "_zelto_i18n.py"
    body = (
        "# -*- coding: utf-8 -*-\n"
        '"""ZELTO landing translations — IT from _zelto_it_strings; geos from locale_*.py."""\n'
        "from __future__ import annotations\n\n"
        "from _zelto_it_strings import IT_STRINGS\n"
        "from _zelto_i18n_data import GEO_TRANSLATIONS\n\n"
        "TRANSLATIONS: dict[str, dict] = {\n"
        '    "it": dict(IT_STRINGS),\n'
        "    **GEO_TRANSLATIONS,\n"
        "}\n"
    )
    data_path = ROOT / "_zelto_i18n_data.py"
    lines = [
        "# -*- coding: utf-8 -*-",
        "from __future__ import annotations",
        "",
        "import importlib",
        "",
        "_LOCALE_MODULES = {",
    ]
    for code, mod in LOCALE_MODULES.items():
        lines.append(f'    "{code}": "{mod}",')
    lines.extend(
        [
            "}",
            "",
            "def _load(code: str) -> dict:",
            "    mod = importlib.import_module(_LOCALE_MODULES[code])",
            "    return dict(mod.STRINGS)",
            "",
            "GEO_TRANSLATIONS: dict[str, dict] = {",
        ]
    )
    for code in LOCALE_MODULES:
        lines.append(f'    "{code}": _load("{code}"),')
    lines.append("}")
    data_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    out.write_text(body, encoding="utf-8")
    print(f"Wrote {out.name} and {data_path.name}")


if __name__ == "__main__":
    main()
