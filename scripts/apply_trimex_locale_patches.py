#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply COPY_PATCHES to scripts/_trimex_copy_data.py."""
from __future__ import annotations

import importlib.util
import pprint
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COPY_PATH = ROOT / "_trimex_copy_data.py"
PATCHES_PATH = ROOT / "_trimex_locale_patches.py"

LANG_ORDER = ("de", "pl", "es", "pt", "ro", "sl", "hr", "cs", "hu", "sk", "lv")
PATCH_LANGS = ("cs", "hu", "lv", "sl", "hr", "sk")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def write_copy_data(copy: dict) -> None:
    ordered = {lang: copy[lang] for lang in LANG_ORDER}
    header = (
        "# -*- coding: utf-8 -*-\n"
        '"""TRIMEX grass trimmer landing + thank-you copy for 11 locales."""\n\n'
    )
    body = pprint.pformat(ordered, width=120, sort_dicts=False)
    COPY_PATH.write_text(header + "COPY = " + body + "\n", encoding="utf-8")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    copy_mod = load_module(COPY_PATH, "_trimex_copy_data")
    patches_mod = load_module(PATCHES_PATH, "_trimex_locale_patches")
    copy = copy_mod.COPY
    patches = patches_mod.COPY_PATCHES

    pl_keys = list(copy["pl"].keys())
    for lang in PATCH_LANGS:
        if lang not in patches:
            raise KeyError(f"Missing COPY_PATCHES[{lang!r}]")
        patch = patches[lang]
        missing = [k for k in pl_keys if k not in patch]
        extra = [k for k in patch if k not in pl_keys]
        if missing:
            raise KeyError(f"{lang}: missing keys {missing[:5]}... ({len(missing)} total)")
        if extra:
            raise KeyError(f"{lang}: extra keys {extra[:5]}...")
        copy[lang] = {k: patch[k] for k in pl_keys}

    write_copy_data(copy)
    print(f"Updated {', '.join(PATCH_LANGS)} in {COPY_PATH.name}")


if __name__ == "__main__":
    main()
