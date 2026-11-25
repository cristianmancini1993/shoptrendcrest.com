# -*- coding: utf-8 -*-
"""LINVO™ — Adrice Network forms (cod-form UI) for shoptrendcrest.com."""
from __future__ import annotations

BASE = "https://shoptrendcrest.com"
UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
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
    "labels": ("Nome e cognome*", "Telefono*", "Indirizzo di consegna*"),
    "placeholders": ("Giulia Rossi", "+39 312 345 6789", "Via Roma 10, 00100 Roma"),
    "submit": "Ordina ora",
    "errors": (
        "Inserisci nome e cognome (almeno 3 caratteri)",
        "Inserisci un numero di telefono valido",
        "Inserisci un indirizzo di consegna completo",
    ),
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
        errors = _IT_FORM["errors"]
    else:
        meta = _FORM_META[offer]
        labels = meta["labels"]
        placeholders = meta["placeholders"]
        submit = meta["submit"]
        errors = (
            tr.get("err_name", "Inserisci nome e cognome (almeno 3 caratteri)"),
            tr.get("err_tel", "Inserisci un numero di telefono valido"),
            tr.get("err_addr", "Inserisci un indirizzo di consegna completo"),
        )
    return {
        "name_l": labels[0],
        "tel_l": labels[1],
        "addr_l": labels[2],
        "name_p": placeholders[0],
        "tel_p": placeholders[1],
        "addr_p": placeholders[2],
        "submit": submit,
        "err_name": errors[0],
        "err_tel": errors[1],
        "err_addr": errors[2],
        "form_note": tr.get("form_note", ""),
    }


def form_html(offer: str, tr: dict | None = None) -> str:
    tr = tr or {}
    geo = OFFER_GEO[offer]
    ui = _ui(offer, tr)
    lp, key = _lp_key(offer)
    ty = thankyou_url(geo, offer)
    nl, tl, al = ui["name_l"], ui["tel_l"], ui["addr_l"]
    np, tp, ap = map(_esc_attr, (ui["name_p"], ui["tel_p"], ui["addr_p"]))
    en, et, ea = map(_esc_attr, (ui["err_name"], ui["err_tel"], ui["err_addr"]))
    submit = ui["submit"]
    note = _esc_attr(ui.get("form_note", ""))

    return f"""      <form class="tm-order-form order-form cod-form" action="{ACTION}" method="post" novalidate>
        <div class="cod-form__field">
          <label class="cod-form__label" for="name">{nl}</label>
          <input id="name" class="cod-form__input" type="text" name="name" autocomplete="name" placeholder="{np}" required>
          <span class="cod-form__error">{en}</span>
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="tel">{tl}</label>
          <input id="tel" class="cod-form__input" type="tel" name="tel" autocomplete="tel" placeholder="{tp}" required>
          <span class="cod-form__error">{et}</span>
        </div>
        <div class="cod-form__field">
          <label class="cod-form__label" for="street-address">{al}</label>
          <input id="street-address" class="cod-form__input" type="text" name="street-address" autocomplete="street-address" placeholder="{ap}" required>
          <span class="cod-form__error">{ea}</span>
        </div>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="{ty}"/>
        <input name="webhook" type="hidden" value="{WEBHOOK}"/>
        <input name="_key" type="hidden" value="{key}" />
        <div class="order-form__submit">
          <button name="submit" type="submit" class="cta-btn">{submit}</button>
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