# -*- coding: utf-8 -*-
"""Rigid case (maletín) — consistent kit/FAQ wording per locale."""

KIT_LI4: dict[str, str] = {
    "es": "Maletín rígido de transporte",
    "pt": "Mala rígida de transporte",
    "pl": "Twarda walizka transportowa",
    "cs": "Pevný transportní kufr",
    "ro": "Geantă rigidă de transport",
    "sk": "Pevný transportný kufor",
    "si": "Trda transportna torba",
    "hr": "Tvrdi transportni kofer",
    "hu": "Merev szállítókoffer",
    "de": "Harter Transportkoffer",
    "lv": "Ciets transporta koferis",
    "lt": "Standus transportavimo lagaminas",
    "it": "Valigetta rigida da trasporto",
}

# Phrases that may still contain “funda/bolsa” from TAIGOR seed.
FUNDa_PATCHES: dict[str, tuple[str, str]] = {
    "es": ("funda", "maletín rígido"),
    "pt": ("funda", "mala rígida"),
    "pl": ("funda", "twarda walizka"),
    "cs": ("funda", "pevný kufr"),
    "ro": ("funda", "geantă rigidă"),
    "sk": ("funda", "pevný kufor"),
    "si": ("funda", "trda torba"),
    "hr": ("funda", "tvrdi kofer"),
    "hu": ("funda", "merev koffer"),
    "de": ("funda", "harter Koffer"),
    "lv": ("funda", "ciets koferis"),
    "lt": ("funda", "standus lagaminas"),
    "it": ("funda", "valigetta rigida"),
}


def apply_kit_case(bundle: dict, code: str) -> dict:
    out = dict(bundle)
    if code in KIT_LI4:
        out["kit_li4"] = KIT_LI4[code]
    import re

    if code in FUNDa_PATCHES:
        _old, new = FUNDa_PATCHES[code]
        for key, val in list(out.items()):
            if not isinstance(val, str):
                continue
            if "Funda/bolsa" in val:
                out[key] = val.replace("Funda/bolsa de transporte", KIT_LI4.get(code, val))
            # Word-boundary only — avoid breaking e.g. Czech „refundace“.
            out[key] = re.sub(r"\bfunda\b", new, out[key], flags=re.IGNORECASE)
    if isinstance(out.get("kit_li4"), str) and "Funda/bolsa" in out["kit_li4"]:
        out["kit_li4"] = KIT_LI4.get(code, out["kit_li4"])
    return out
