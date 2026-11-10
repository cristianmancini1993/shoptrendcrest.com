#!/usr/bin/env python3
"""Adrice Network form HTML for WARMIO™ — per-offer lp/_key from buyer."""
from __future__ import annotations

from _warmio_form_ui import FORM_UI, OFFER_GEO, OFFER_LP_KEY

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

MISSING_OFFERS: list[str] = []

FIELD_ORDER: dict[str, list[str]] = {
    oid: ["name", "tel", "street-address"] for oid in FORM_UI
}


def thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com/{geo}/warmio-{offer}/thank-you/"


def _fields(ui: dict[str, str]) -> str:
    return (
        f'<label for="name">{ui["name_l"]}</label>\n'
        f'<input id="name" type="text" name="name" autocomplete="name" '
        f'placeholder="{ui["name_p"]}" required><br>\n'
        f'<label for="tel">{ui["tel_l"]}</label>\n'
        f'<input id="tel" type="tel" name="tel" autocomplete="tel" '
        f'placeholder="{ui["tel_p"]}" required><br>\n'
        f'<label for="street-address">{ui["addr_l"]}</label>\n'
        f'<input id="street-address" type="text" name="street-address" '
        f'autocomplete="street-address" placeholder="{ui["addr_p"]}" required><br>\n'
    )


def _form(offer: str) -> str:
    ui = FORM_UI[offer]
    geo = OFFER_GEO[offer]
    lp, key = OFFER_LP_KEY[offer]
    ty = thankyou_url(geo, offer)
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post">
{_fields(ui)}<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn">{ui["submit"]}</button>
</div>
<script src="{SCRIPT}" async></script>
</form>"""


FORMS: dict[str, str] = {oid: _form(oid) for oid in FORM_UI}
