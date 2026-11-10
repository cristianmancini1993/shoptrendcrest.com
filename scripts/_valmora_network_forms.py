# -*- coding: utf-8 -*-
"""Adrice Network form HTML per VALMORA offer."""
from __future__ import annotations

from _order_form_fields_i18n import geo_from_rel, tm_order_fields_html

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh"
ACTION = "https://offers.adricenetwork.com/forms/html/"

FORM_META = {
    "lv/valmora-4095": {"offer": "4095", "lp": "4135", "key": "846167920ffa5186bf49e51c085dd25da88ee156"},
    "sk/valmora-3702": {"offer": "3702", "lp": "3742", "key": "95b96e3e466e3180a5fc5117499394b150f135bf"},
    "cz/valmora-3180": {"offer": "3180", "lp": "3214", "key": "2c99b5833682b7e8dad6eb52038d2560d25708a4"},
    "pl/valmora-3179": {"offer": "3179", "lp": "3213", "key": "9284f944be23b667b5f083f1c256ac6773e78073"},
    "lt/valmora-3178": {"offer": "3178", "lp": "3212", "key": "554b43383d85970a492667f31cd6bdb35030ae11"},
    "de/valmora-3177": {"offer": "3177", "lp": "3211", "key": "feaaf365b3bfd853b4fc9b265145b08a57bafe55"},
    "es/valmora-3176": {"offer": "3176", "lp": "3210", "key": "ef1eecc2ab3ddc7b01bdc1ecee2c9a5c76a0400b"},
    "ro/valmora-1387": {"offer": "1387", "lp": "1406", "key": "bfaf8a8d8f3f5285fbf87c3616581b86f6886e9b"},
    "pt/valmora-1476": {"offer": "1476", "lp": "1496", "key": "31e9407b5c50cced10662c864645101050908a07"},
    "si/valmora-1875": {"offer": "1875", "lp": "1895", "key": "d16aa4ee0aa82cb50fccbf992a6cf6447a237290"},
    "hr/valmora-1876": {"offer": "1876", "lp": "1896", "key": "aff24016433518c2a9c8192afe693f24d9c817c8"},
    "hu/valmora-2409": {"offer": "2409", "lp": "2434", "key": "ba45ebc620cdf881f6b555ebf345c213e544ae0b"},
}

SUBMIT_LABELS: dict[str, str] = {
    "lv/valmora-4095": "Pasūtiet tagad",
    "sk/valmora-3702": "Objednajte si teraz",
    "cz/valmora-3180": "Objednat nyní",
    "pl/valmora-3179": "Zamów teraz",
    "lt/valmora-3178": "Užsisakykite dabar",
    "de/valmora-3177": "Jetzt bestellen",
    "es/valmora-3176": "Haz tu pedido",
    "ro/valmora-1387": "Cumpără acum",
    "pt/valmora-1476": "Enviar o pedido",
    "si/valmora-1875": "Kupite zdaj",
    "hr/valmora-1876": "Kupi sada",
    "hu/valmora-2409": "Rendeljen most",
}

FORM_NOTES: dict[str, str] = {
    "lv/valmora-4095": "🔒 Apmaksa pie saņemšanas · Atgriešana 30 dienu laikā",
    "sk/valmora-3702": "🔒 Platba pri doručení · Vrátenie do 30 dní",
    "cz/valmora-3180": "🔒 Platba při doručení · Vrácení do 30 dnů",
    "pl/valmora-3179": "🔒 Płatność przy odbiorze · Zwrot do 30 dni",
    "lt/valmora-3178": "🔒 Mokėjimas pristatymo metu · Grąžinimas per 30 dienų",
    "de/valmora-3177": "🔒 Zahlung bei Lieferung · Rückgabe innerhalb von 30 Tagen",
    "es/valmora-3176": "🔒 Pago contra reembolso · Devolución en 30 días",
    "ro/valmora-1387": "🔒 Plată la livrare · Retur în 30 de zile",
    "pt/valmora-1476": "🔒 Pagamento na entrega · Devolução em 30 dias",
    "si/valmora-1875": "🔒 Plačilo ob prevzemu · Vračilo v 30 dneh",
    "hr/valmora-1876": "🔒 Plaćanje pri dostavi · Povrat u 30 dana",
    "hu/valmora-2409": "🔒 Fizetés átvételkor · 30 napos visszaküldés",
}


def _build_form(rel: str) -> str:
    meta = FORM_META[rel]
    fields = tm_order_fields_html(geo_from_rel(rel))
    ty = f"https://gadgetshifthub.com/{rel}/thank-you.html"
    btn = SUBMIT_LABELS[rel]
    note = FORM_NOTES[rel]
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post">
{fields}
        <input name="uid" type="hidden" value="{UID}">
        <input name="offer" type="hidden" value="{meta['offer']}">
        <input name="lp" type="hidden" value="{meta['lp']}">
        <input name="subid" id="subid" type="hidden" value="">
        <input name="thankyoupage" type="hidden" value="{ty}">
        <input name="webhook" type="hidden" value="{WEBHOOK}">
        <input name="_key" type="hidden" value="{meta['key']}">
        <button type="submit" class="cta-btn">{btn}</button>
        <p class="form-note">{note}</p>
      </form>"""


FORMS = {rel: _build_form(rel) for rel in FORM_META}
