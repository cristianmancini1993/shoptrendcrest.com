#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off: build native-ish locale patches from ES master via batched translation + country fixes."""
from __future__ import annotations

import time
from pathlib import Path

from _taigor_langs.es import PATCH as ES_PATCH

ROOT = Path(__file__).resolve().parent / "_taigor_langs"
SEP = "\n⟦TAIGOR⟧\n"

TARGETS = {
    "lt": "lt",
    "pt": "pt",
    "cs": "cs",
    "ro": "ro",
    "sk": "sk",
    "si": "sl",
    "hr": "hr",
    "hu": "hu",
    "lv": "lv",
}

COUNTRY_FIX = {
    "lt": {
        "rating": "<strong>Pristatymas 24–48 val.</strong> Lietuvoje · <strong>Apmokėjimas pristatymo metu</strong>",
        "f1_p": "Pristatymas į namus Lietuvoje",
        "og_description": "Medieną ir šakas iki 45 cm be benzino: brushless 1600 W, 2 akumuliatoriai, iki 12 val. Apmokėjimas pristatymo metu visoje Lietuvoje.",
    },
    "pt": {
        "rating": "<strong>Envio 24–48 h</strong> em Portugal · <strong>Pagamento na entrega</strong>",
        "f1_p": "Entrega ao domicílio em Portugal",
        "og_description": "Corte lenha e ramos até 45 cm sem gasolina: brushless 1600 W, 2 baterias, até 12 h. Pagamento na entrega em Portugal.",
    },
    "cs": {
        "rating": "<strong>Doručení 24–48 h</strong> v Česku · <strong>Dobírka</strong>",
        "f1_p": "Doručení domů v Česku",
        "og_description": "Dřevo a větve do 45 cm bez benzínu: brushless 1600 W, 2 baterie, až 12 h. Dobírka v celé ČR.",
    },
    "ro": {
        "rating": "<strong>Livrare 24–48 h</strong> în România · <strong>Plată la livrare</strong>",
        "f1_p": "Livrare la domiciliu în România",
        "og_description": "Lemne și crengi până la 45 cm fără benzină: brushless 1600 W, 2 baterii, până la 12 h. Plată la livrare în România.",
    },
    "sk": {
        "rating": "<strong>Doručenie 24–48 h</strong> na Slovensku · <strong>Dobierka</strong>",
        "f1_p": "Doručenie domov na Slovensku",
        "og_description": "Drevo a konáre do 45 cm bez benzínu: brushless 1600 W, 2 batérie, až 12 h. Dobierka na celom Slovensku.",
    },
    "si": {
        "rating": "<strong>Dostava 24–48 h</strong> v Sloveniji · <strong>Plačilo po povzetju</strong>",
        "f1_p": "Dostava na dom v Sloveniji",
        "og_description": "Drva in veje do 45 cm brez bencina: brushless 1600 W, 2 bateriji, do 12 h. Plačilo po povzetju po Sloveniji.",
    },
    "hr": {
        "rating": "<strong>Dostava 24–48 h</strong> u Hrvatskoj · <strong>Plaćanje pouzećem</strong>",
        "f1_p": "Dostava na kućnu adresu u Hrvatskoj",
        "og_description": "Drva i grane do 45 cm bez benzina: brushless 1600 W, 2 baterije, do 12 h. Plaćanje pouzećem u Hrvatskoj.",
    },
    "hu": {
        "rating": "<strong>Szállítás 24–48 óra</strong> Magyarországon · <strong>Utánvét</strong>",
        "f1_p": "Házhoz szállítás Magyarországon",
        "og_description": "Fa és ágak 45 cm-ig benzin nélkül: brushless 1600 W, 2 akkumulátor, akár 12 óra. Utánvét egész Magyarországon.",
    },
    "lv": {
        "rating": "<strong>Piegāde 24–48 h</strong> Latvijā · <strong>Apmaksa piegādē</strong>",
        "f1_p": "Piegāde uz mājām Latvijā",
        "og_description": "Kokmateriāli un zari līdz 45 cm bez benzīna: brushless 1600 W, 2 akumulatori, līdz 12 h. Apmaksa piegādē visā Latvijā.",
    },
}


def main() -> None:
    from deep_translator import GoogleTranslator

    keys = list(ES_PATCH.keys())
    batch_size = 20

    for code, target in TARGETS.items():
        out_path = ROOT / f"{code}.py"
        if out_path.exists() and code in ("es", "pl"):
            continue
        print(f"Translating {code} ({target})...")
        translator = GoogleTranslator(source="es", target=target)
        patch: dict[str, str] = {}
        for i in range(0, len(keys), batch_size):
            chunk_keys = keys[i : i + batch_size]
            blob = SEP.join(ES_PATCH[k] for k in chunk_keys)
            time.sleep(12)
            try:
                translated = translator.translate(blob)
            except Exception as exc:
                raise SystemExit(f"Translation failed for {code} batch {i}: {exc}") from exc
            parts = translated.split(SEP)
            if len(parts) != len(chunk_keys):
                raise SystemExit(
                    f"{code} batch {i}: expected {len(chunk_keys)} parts, got {len(parts)}"
                )
            patch.update(dict(zip(chunk_keys, parts)))
        patch.update(COUNTRY_FIX[code])
        # Preserve brand/spec tokens that translators sometimes break
        for k, v in list(patch.items()):
            v = v.replace("TAIGOR ™", "TAIGOR™").replace("1600 Wt", "1600 W")
            patch[k] = v
        body = "# -*- coding: utf-8 -*-\nPATCH = " + repr(patch) + "\n"
        out_path.write_text(body, encoding="utf-8")
        print(f"  Wrote {out_path} ({len(patch)} keys)")


if __name__ == "__main__":
    main()
