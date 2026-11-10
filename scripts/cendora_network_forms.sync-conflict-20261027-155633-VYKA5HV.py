#!/usr/bin/env python3
"""Adrice form HTML for CENDORA™ — confirmed lp/_key only; others blocked."""
from __future__ import annotations

from _cendora_form_ui import FORM_UI, OFFER_GEO, OFFER_LP_KEY

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/et3u9cckjin3j6cl6quzp6dp306xptjh"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"


def thankyou_url(geo: str, offer: str) -> str:
    return f"https://shoptrendcrest.com/{geo}/cendora-{offer}/thank-you/"


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


def _blocked(offer: str, geo: str, ui: dict[str, str]) -> str:
    msg = ui.get("blocked_msg", ui.get("form_blocked_msg", ""))
    btn = ui.get("blocked_btn", ui.get("form_blocked_btn", "—"))
    return f"""<form class="tm-order-form order-form order-form--blocked" method="post" lang="{geo}" data-cendora-blocked="1" onsubmit="event.preventDefault();var e=this.querySelector('.form-blocked-msg');if(e)e.hidden=false;return false;">
{_fields(ui)}<input name="offer" type="hidden" value="{offer}" />
<p class="form-blocked-msg" role="alert" hidden style="color:#b91c1c;text-align:center;margin-top:12px;font-weight:600;line-height:1.45;">{msg}</p>
<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn" aria-disabled="true">{btn}</button>
</div>
</form>"""


def _live(offer: str, geo: str, ui: dict[str, str]) -> str:
    lp, key = OFFER_LP_KEY[offer]
    ty = thankyou_url(geo, offer)
    note = ui.get("form_note", ui.get("form_note_form", ""))
    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post" lang="{geo}">
{_fields(ui)}<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn">{ui["submit"]}</button>
</div>
<p class="form-note">{note}</p>
<script src="{SCRIPT}" async></script>
</form>"""


def form_html(offer: str) -> str:
    ui = FORM_UI[offer]
    geo = OFFER_GEO[offer]
    if offer not in OFFER_LP_KEY:
        return _blocked(offer, geo, ui)
    return _live(offer, geo, ui)


def all_forms() -> dict[str, str]:
    return {oid: form_html(oid) for oid in FORM_UI}


FORMS: dict[str, str] = all_forms()
