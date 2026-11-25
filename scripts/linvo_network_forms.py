# -*- coding: utf-8 -*-
"""LINVO™ — Adrice Network forms (cod-form UI) for shoptrendcrest.com."""
from __future__ import annotations

BASE = "https://shoptrendcrest.com"
UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/srey7bhi9b1qapk46soc1q9jpb6iwexk"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

from _luno_form_snippets import _FORM_META  # noqa: E402

OFFER_GEO: dict[str, str] = {
    "1912": "de",
    "1915": "hu",
    "2480": "pt",
    "3163": "es",
    "3167": "pl",
    "3169": "cz",
    "3910": "lv",
    "4321": "sk",
    "1897": "it",
}

SPECIAL_LP_KEY = {"1897": ("1917", "61826e8e613c4e5436baadf88ddf662246fb0210")}

# Italian defaults for offer 1897 (reference landing labels)
_IT_FORM = {
    "labels": ("Nome e cognome*", "Indirizzo di consegna*", "Telefono*"),
    "placeholders": ("Giulia Rossi", "Via Roma 10, 00100 Roma", "+39 312 345 6789"),
    "submit": "Ordina ora",
}


def _esc_attr(s: str) -> str:
    return s.replace("&", "&amp;").replace('"', "&quot;")


def thankyou_url(geo: str, offer: str) -> str:
    return f"{BASE}/{geo}/linvo-{offer}/thank-you.html"


def _lp_key(offer: str) -> tuple[str, str]:
    if offer in SPECIAL_LP_KEY:
        return SPECIAL_LP_KEY[offer]
    meta = _FORM_META[offer]
    return meta["lp"], meta["key"]


def _ui(offer: str, tr: dict) -> dict[str, str]:
    if offer == "1897":
        labels = _IT_FORM["labels"]
        placeholders = _IT_FORM["placeholders"]
        submit = tr.get("submit_btn", _IT_FORM["submit"])
    else:
        meta = _FORM_META[offer]
        # _FORM_META order: name, tel, address — display: name → street-address → tel
        labels = (meta["labels"][0], meta["labels"][2], meta["labels"][1])
        placeholders = (meta["placeholders"][0], meta["placeholders"][2], meta["placeholders"][1])
        submit = meta["submit"]
    return {
        "name_l": labels[0],
        "addr_l": labels[1],
        "tel_l": labels[2],
        "name_p": placeholders[0],
        "addr_p": placeholders[1],
        "tel_p": placeholders[2],
        "submit": submit,
    }


def form_html(offer: str, tr: dict | None = None) -> str:
    tr = tr or {}
    geo = OFFER_GEO[offer]
    ui = _ui(offer, tr)
    lp, key = _lp_key(offer)
    ty = thankyou_url(geo, offer)
    nl, al, tl = ui["name_l"], ui["addr_l"], ui["tel_l"]
    np, ap, tp = map(_esc_attr, (ui["name_p"], ui["addr_p"], ui["tel_p"]))
    submit = ui["submit"]

    return f"""      <form class="tm-order-form order-form" action="{ACTION}" method="post">
<label for="name">{nl}</label>
<input id="name" type="text" name="name" autocomplete="name" placeholder="{np}" required><br>
<label for="street-address">{al}</label>
<input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{ap}" required><br>
<label for="tel">{tl}</label>
<input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{tp}" required><br>
<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit">{submit}</button>
</div>
<script src="{SCRIPT}" async></script>
</form>"""


def build_forms(tr_by_offer: dict[str, dict] | None = None) -> dict[str, str]:
    tr_by_offer = tr_by_offer or {}
    out: dict[str, str] = {}
    for offer in OFFER_GEO:
        out[offer] = form_html(offer, tr_by_offer.get(offer, {}))
    return out


MISSING_ADRICE: list[str] = [
    oid for oid in OFFER_GEO if oid != "1897" and oid not in _FORM_META
]