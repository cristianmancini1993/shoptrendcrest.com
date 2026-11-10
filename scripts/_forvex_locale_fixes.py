# -*- coding: utf-8 -*-
"""Manual copy fixes per locale (reviews, leads, PT forms labels, etc.)."""

LOCALE_FIXES: dict[str, dict[str, str]] = {
    "pt": {
        "label_name": "Nome completo*",
        "ph_name": "Nome completo",
        "label_addr": "Morada*",
        "ph_addr": "Morada",
        "submit_btn": "Encomendar agora",
    },
    "de": {
        "rev1_h": "Auf dem Sägebock starke Stämme ohne Mühe.",
        "rev2_p": "«Zwischen Laub und Holzstapel säge ich Stämme auf dem Sägebock: konstante Kraft, Späne fliegen, kein Benzingeruch.»",
        "why1_p1": "Der bürstenlose 2000-W-Motor startet sofort und hält die Kraft: FORVEX™ bleibt auch bei dickem Holz durchzugsstark.",
    },
    "sk": {
        "rev1_h": "Na koze zvládne aj hrubé klady.",
        "rev2_p": "«Medzi lístím a kôpkou dreva režem klady na koze: stály výkon, triesky lietajú, žiadny benzín.»",
    },
    "hr": {
        "lead": "Motor bez četkica, dvije litij-baterije i vodilica 50 cm za drva, obrezivanje i vrt. Jedan klik — bez vučenja startera, bez benzina, bez produžnog kabela.",
    },
    "hu": {
        "testimonials_h": "Élmények az udvaron, az erdőben és a doboz kinyitásakor",
        "rev1_p": "«Az udvaron sisakkal és kesztyűvel készítek tűzifát: egyenesen megy a rönkbe, tiszta vágás vastag darabokon is.»",
    },
    "lv": {
        "rev2_h": "Rudenī malka bez maisījuma.",
        "rev1_p": "«Pagalmā ar ķiveri un cimdiem gatavoju malku: iet taisni kokā, tīrs griezums arī biezos gabalos.»",
    },
}


def apply_locale_fixes(bundle: dict, code: str) -> dict:
    fixes = LOCALE_FIXES.get(code, {})
    out = dict(bundle)
    for k, v in fixes.items():
        if v:
            out[k] = v
    return out
