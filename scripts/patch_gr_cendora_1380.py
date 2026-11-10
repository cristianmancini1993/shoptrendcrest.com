#!/usr/bin/env python3
"""Regenerate GR cendora-1380 on shoptrendcrest.com (see homeshopspot scripts/gen_cendora_gr_1380.py)."""
from pathlib import Path
import runpy

SRC = Path(__file__).resolve().parents[1].parent / "homeshopspot.com-1" / "scripts" / "gen_cendora_gr_1380.py"
if not SRC.is_file():
    raise SystemExit(f"Missing generator: {SRC}")
runpy.run_path(str(SRC), run_name="__main__")
