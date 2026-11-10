#!/usr/bin/env python3
"""Static checks: Granvia geo forms keep local placeholder examples in HTML + SITE_CONFIG."""
from __future__ import annotations

import json
import re
from pathlib import Path

from _granvia_form_examples import FIELD_ORDER, GRANVIA_FORM_EXAMPLES

ROOT = Path(__file__).resolve().parents[1]
OFFERS = json.loads((ROOT / "content/granvia/offers.json").read_text(encoding="utf-8"))

OFFER_PATHS = {
    str(o["id"]): (o["geo"], f"{o['geo']}/granvia-{o['id']}/index.html") for o in OFFERS
}

_FIELD_PH_KEYS = {
    "name": "ph_name",
    "tel": "ph_tel",
    "street-address": "ph_addr",
}


def _extract_site_config_placeholders(html: str) -> dict[str, str] | None:
    m = re.search(r"FORM_PLACEHOLDERS:\s*\{([^}]+)\}", html)
    if not m:
        return None
    block = m.group(1)
    out: dict[str, str] = {}
    for field in FIELD_ORDER:
        key = field if field != "street-address" else "'street-address'"
        fm = re.search(rf"{key}:\s*'((?:\\'|[^'])*)'", block)
        if fm:
            out[field] = fm.group(1).replace("\\'", "'")
    return out if len(out) == 3 else None


def _input_placeholder(html: str, name: str) -> str | None:
    m = re.search(
        rf'<input[^>]+name="{name}"[^>]*placeholder="([^"]*)"',
        html,
        re.IGNORECASE,
    )
    return m.group(1) if m else None


def _data_placeholder(html: str, name: str) -> str | None:
    m = re.search(
        rf'<input[^>]+name="{name}"[^>]*data-cendora-placeholder="([^"]*)"',
        html,
        re.IGNORECASE,
    )
    return m.group(1) if m else None


def verify_generated_html() -> list[str]:
    errors: list[str] = []
    for offer_id, (geo, rel) in sorted(OFFER_PATHS.items()):
        lang = next(o["lang"] for o in OFFERS if str(o["id"]) == offer_id)
        if lang not in GRANVIA_FORM_EXAMPLES:
            continue
        expected = GRANVIA_FORM_EXAMPLES[lang]
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"#{offer_id}: missing {rel}")
            continue
        html = path.read_text(encoding="utf-8")
        cfg_ph = _extract_site_config_placeholders(html)
        if not cfg_ph:
            errors.append(f"#{offer_id}: missing FORM_PLACEHOLDERS in SITE_CONFIG")
        else:
            for field in FIELD_ORDER:
                key = _FIELD_PH_KEYS[field]
                if cfg_ph.get(field) != expected[key]:
                    errors.append(
                        f"#{offer_id}: SITE_CONFIG {field} {cfg_ph.get(field)!r} != {expected[key]!r}"
                    )
        for field in FIELD_ORDER:
            key = _FIELD_PH_KEYS[field]
            ph = _input_placeholder(html, field)
            data_ph = _data_placeholder(html, field)
            exp = expected[key]
            if ph != exp:
                errors.append(f"#{offer_id}: HTML placeholder {field} {ph!r} != {exp!r}")
            if data_ph != exp:
                errors.append(f"#{offer_id}: data-cendora-placeholder {field} {data_ph!r} != {exp!r}")
        labels = re.findall(
            r'<label for="(name|tel|street-address)">([^<]+)</label>',
            html,
        )
        order = [a for a, _ in labels]
        if order != list(FIELD_ORDER):
            errors.append(f"#{offer_id}: label order {order} != {list(FIELD_ORDER)}")
    return errors


def main() -> int:
    errs = verify_generated_html()
    if errs:
        print("Granvia form placeholder verification FAILED:")
        for e in errs:
            print(" ", e)
        return 1
    print("Granvia form placeholder verification OK (6 geo landings).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
