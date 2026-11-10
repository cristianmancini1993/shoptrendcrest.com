# -*- coding: utf-8 -*-
"""Localized copy for FLAMORA electric fireplace geo landings."""
from __future__ import annotations

import json
from pathlib import Path

_LOC = Path(__file__).resolve().parent / "locales" / "flamora_fireplace"

COPY: dict = {}
for path in sorted(_LOC.glob("*.json")):
    lang = path.stem
    COPY[lang] = json.loads(path.read_text(encoding="utf-8"))
