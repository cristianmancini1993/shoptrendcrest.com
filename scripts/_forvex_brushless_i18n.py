# -*- coding: utf-8 -*-
"""Post-process brushless → locale-appropriate motor wording on key phrases."""

# Applied to full translation dict values after ES master merge.
PHRASE_PATCHES: dict[str, list[tuple[str, str]]] = {
    "es": [
        ("brushless 2000 W", "motor sin escobillas de 2000 W"),
        ("brushless de alto par", "motor sin escobillas de alto par"),
        ("El brushless de 2000 W", "El motor sin escobillas de 2000 W"),
        ("Brushless 2000 W", "Motor sin escobillas 2000 W"),
        ("brushless", "sin escobillas"),
        ("Cadenas spare", "Cadenas de repuesto"),
        ("cadenas spare", "cadenas de repuesto"),
        ("Funda/bolsa de transporte", "Malettín rígido de transporte"),
        ("funda, guantes", "maletín rígido, guantes"),
        ("funda,", "maletín rígido,"),
    ],
    "de": [
        ("Brushless 2000 W", "Bürstenloser Motor 2000 W"),
        ("brushless 2000 W", "bürstenloser Motor 2000 W"),
        ("Brushless", "Bürstenlos"),
        ("brushless", "bürstenlos"),
    ],
    "pt": [
        ("brushless 2000 W", "motor sem escovas de 2000 W"),
        ("Brushless 2000 W", "Motor sem escovas 2000 W"),
        ("brushless", "sem escovas"),
        ("Brushless", "Sem escovas"),
    ],
    "pl": [
        ("brushless 2000 W", "silnik bezszczotkowy 2000 W"),
        ("Brushless 2000 W", "Silnik bezszczotkowy 2000 W"),
        ("brushless", "bezszczotkowy"),
        ("Brushless", "Bezszczotkowy"),
    ],
    "cs": [
        ("brushless 2000 W", "bezkartáčový motor 2000 W"),
        ("Brushless 2000 W", "Bezkartáčový motor 2000 W"),
        ("brushless", "bezkartáčový"),
        ("Brushless", "Bezkartáčový"),
    ],
    "ro": [
        ("brushless 2000 W", "motor fără perii 2000 W"),
        ("Brushless 2000 W", "Motor fără perii 2000 W"),
        ("brushless", "fără perii"),
        ("Brushless", "Fără perii"),
    ],
    "sk": [
        ("brushless 2000 W", "bezkartáčový motor 2000 W"),
        ("Brushless 2000 W", "Bezkartáčový motor 2000 W"),
        ("brushless", "bezkartáčový"),
        ("Brushless", "Bezkartáčový"),
    ],
    "si": [
        ("brushless 2000 W", "brezčetnični motor 2000 W"),
        ("Brushless 2000 W", "Brezčetnični motor 2000 W"),
        ("brushless", "brezčetnični"),
        ("Brushless", "Brezčetnični"),
    ],
    "hr": [
        ("brushless 2000 W", "motor bez četkica 2000 W"),
        ("Brushless 2000 W", "Motor bez četkica 2000 W"),
        ("brushless", "bez četkica"),
        ("Brushless", "Bez četkica"),
    ],
    "hu": [
        ("brushless 2000 W", "kefe nélküli motor 2000 W"),
        ("Brushless 2000 W", "Kefe nélküli motor 2000 W"),
        ("brushless", "kefe nélküli"),
        ("Brushless", "Kefe nélküli"),
    ],
    "lt": [
        ("brushless 2000 W", "bekontaktis variklis 2000 W"),
        ("Brushless 2000 W", "Bekontaktis variklis 2000 W"),
        ("brushless", "bekontaktis"),
        ("Brushless", "Bekontaktis"),
    ],
    "lv": [
        ("brushless 2000 W", "bezkontaktu motors 2000 W"),
        ("Brushless 2000 W", "Bezkontaktu motors 2000 W"),
        ("brushless", "bezkontaktu"),
        ("Brushless", "Bezkontaktu"),
    ],
    "it": [
        ("brushless 2000 W", "motore brushless 2000 W"),
        ("Brushless 2000 W", "Motore brushless 2000 W"),
    ],
}

KIT_CASE_PATCHES: dict[str, list[tuple[str, str]]] = {
    "es": [
        ("Funda/bolsa de transporte", "Malettín rígido de transporte"),
    ],
}


def apply_patches(text: str, code: str) -> str:
    for old, new in PHRASE_PATCHES.get(code, []):
        text = text.replace(old, new)
    for old, new in KIT_CASE_PATCHES.get(code, []):
        text = text.replace(old, new)
    return text


def patch_bundle(bundle: dict, code: str) -> dict:
    out = {}
    for k, v in bundle.items():
        if isinstance(v, str):
            out[k] = apply_patches(v, code)
        elif isinstance(v, tuple):
            out[k] = tuple(apply_patches(x, code) for x in v)
        elif isinstance(v, list):
            out[k] = [apply_patches(x, code) for x in v]
        else:
            out[k] = v
    return out
