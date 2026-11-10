#!/usr/bin/env python3
"""Adrice form HTML for CENDORA™ — exactly 3 visible fields (name, tel, full address)."""
from __future__ import annotations

from _cendora_form_ui import FORM_UI, OFFER_GEO, OFFER_LANG, OFFER_LP_KEY, SITE_DOMAIN, PRODUCT_SLUG

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

MISSING_OFFERS: list[str] = [oid for oid in FORM_UI if oid not in OFFER_LP_KEY]

# Visible field order: name → tel → full address (all 13 offers).
FIELD_ORDER: dict[str, list[str]] = {}
_DEFAULT_ORDER = ["name", "tel", "street-address"]

_REQUIRED = frozenset({"name", "tel", "street-address"})

# Network submit button labels from buyer embeds.
NETWORK_SUBMIT: dict[str, str] = {
    "4373": "ORDINA ORA",
    "1476": "Enviar o pedido",
    "1387": "Cumpără acum:",
    "1874": "Kúpte teraz",
    "1875": "Kupite Zdaj",
    "1876": "Kupi sada",
    "2409": "Rendeljen most",
    "3176": "Haz tu pedido",
    "3177": "Jetzt bestellen",
    "3178": "Užsisakykite dabar",
    "3179": "Zamów teraz",
    "3251": "Objednat nyní",
    "4095": "Pasūtiet tagad",
}


def thankyou_url(geo: str, offer: str) -> str:
    if not SITE_DOMAIN or not PRODUCT_SLUG:
        raise ValueError("Set domain and product_slug in content/cendora/site.json")
    return f"https://{SITE_DOMAIN}/{geo}/{PRODUCT_SLUG}-{offer}/thank-you/"


def _field_block(field_id: str, ui: dict[str, str]) -> str:
    if field_id == "name":
        return (
            f'<label for="name">{ui["name_l"]}</label>\n'
            f'<input id="name" type="text" name="name" autocomplete="name" '
            f'placeholder="{ui["name_p"]}" required><br>\n'
        )
    if field_id == "tel":
        return (
            f'<label for="tel">{ui["tel_l"]}</label>\n'
            f'<input id="tel" type="tel" name="tel" autocomplete="tel" '
            f'placeholder="{ui["tel_p"]}" required><br>\n'
        )
    if field_id == "street-address":
        return (
            f'<label for="street-address">{ui["addr_l"]}</label>\n'
            f'<input id="street-address" type="text" name="street-address" '
            f'autocomplete="street-address" placeholder="{ui["addr_p"]}" required><br>\n'
        )
    return ""


def _fields_for_offer(offer: str, ui: dict[str, str]) -> str:
    order = FIELD_ORDER.get(offer, _DEFAULT_ORDER)
    parts: list[str] = []
    for fid in order:
        if fid not in _REQUIRED:
            continue
        parts.append(_field_block(fid, ui))
    return "".join(parts)


def form_html(offer: str) -> str:
    ui = FORM_UI[offer]
    geo = OFFER_GEO[offer]
    lang = OFFER_LANG[offer]
    if offer in MISSING_OFFERS:
        return blocked_form_html(offer, lang, ui)
    lp, key = OFFER_LP_KEY[offer]
    ty = thankyou_url(geo, offer)
    fields = _fields_for_offer(offer, ui)
    submit = NETWORK_SUBMIT.get(offer, ui["submit"])
    blocked_msg = ui.get("blocked_msg", "")

    def _esc_attr(s: str) -> str:
        return s.replace("&", "&amp;").replace('"', "&quot;")

    return f"""<form class="tm-order-form order-form" action="{ACTION}" method="post" lang="{lang}" data-cendora-fields="3" data-cendora-blocked-msg="{_esc_attr(blocked_msg)}">
{fields}<input name="uid" type="hidden" value="{UID}" />
<input name="offer" type="hidden" value="{offer}" />
<input name="lp" type="hidden" value="{lp}" />
<input name="thankyoupage" type="hidden" value="{ty}"/>
<input name="webhook" type="hidden" value="{WEBHOOK}"/>
<input name="_key" type="hidden" value="{key}" />
<p class="form-blocked-msg" role="alert" hidden style="color:#b91c1c;text-align:center;margin-top:12px;font-weight:600;line-height:1.45;">{blocked_msg}</p>

<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn">{submit}</button>
</div>
<p class="form-note">{ui.get("form_note", "")}</p>
<script src="{SCRIPT}" async></script>
</form>"""


def blocked_form_html(offer: str, lang: str, ui: dict[str, str]) -> str:
    msg = ui["blocked_msg"]
    btn = ui["blocked_btn"]
    fields = _fields_for_offer(offer, ui)
    return f"""<form class="tm-order-form order-form order-form--blocked" method="post" lang="{lang}" data-cendora-blocked="1" data-cendora-fields="3" onsubmit="event.preventDefault();var e=this.querySelector('.form-blocked-msg');if(e)e.hidden=false;return false;">
{fields}<input name="offer" type="hidden" value="{offer}" />
<p class="form-blocked-msg" role="alert" hidden style="color:#b91c1c;text-align:center;margin-top:12px;font-weight:600;line-height:1.45;">{msg}</p>
<div style="margin-top: 10px; text-align: center">
    <button name="submit" type="submit" class="cta-btn" aria-disabled="true">{btn}</button>
</div>
<p class="form-note">{ui.get("form_note", "")}</p>
</form>"""


FORMS: dict[str, str] = {oid: form_html(oid) for oid in FORM_UI}
