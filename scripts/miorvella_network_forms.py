#!/usr/bin/env python3
"""Adrice Network form HTML per Miorvella geo offer."""
from __future__ import annotations

UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
WEBHOOK = "https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"
SIZE_PH = "140x200 / 160x200 / 180x200"


def _form(
    *,
    labels: tuple[str, str, str],
    placeholders: tuple[str, str, str],
    size_label: str,
    form_note: str,
    offer: str,
    lp: str,
    thankyou: str,
    key: str,
    submit: str,
) -> str:
    name_l, addr_l, tel_l = labels
    name_p, addr_p, tel_p = placeholders
    return f"""      <form class="tm-order-form order-form" action="{ACTION}" method="post">
        <label for="name">{name_l}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{name_p}" required><br>
        <label for="street-address">{addr_l}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{addr_p}" required><br>
        <label for="tel">{tel_l}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{tel_p}" required><br>
        <label for="size">{size_label}</label>
        <select id="size" name="size" required>
          <option value="" disabled selected>{SIZE_PH}</option>
          <option value="140x200">140x200</option>
          <option value="160x200">160x200</option>
          <option value="180x200">180x200</option>
        </select><br>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="{thankyou}"/>
        <input name="webhook" type="hidden" value="{WEBHOOK}"/>
        <input name="_key" type="hidden" value="{key}" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{submit}</button>
        </div>
        <p class="form-note">{form_note}</p>
        <script src="{SCRIPT}" async></script>
      </form>"""


def _form_no_size(
    *,
    labels: tuple[str, str, str],
    placeholders: tuple[str, str, str],
    form_note: str,
    offer: str,
    lp: str,
    thankyou: str,
    key: str,
    submit: str,
) -> str:
    name_l, addr_l, tel_l = labels
    name_p, addr_p, tel_p = placeholders
    return f"""      <form class="tm-order-form order-form" action="{ACTION}" method="post">
        <label for="name">{name_l}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{name_p}" required><br>
        <label for="street-address">{addr_l}</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{addr_p}" required><br>
        <label for="tel">{tel_l}</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{tel_p}" required><br>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="{thankyou}"/>
        <input name="webhook" type="hidden" value="{WEBHOOK}"/>
        <input name="_key" type="hidden" value="{key}" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{submit}</button>
        </div>
        <p class="form-note">{form_note}</p>
        <script src="{SCRIPT}" async></script>
      </form>"""


def _it_form(
    *,
    name_label: str,
    name_placeholder: str,
    offer: str,
    lp: str,
    thankyou: str,
    key: str,
    submit: str,
) -> str:
    return f"""      <form class="tm-order-form" action="{ACTION}" method="post">
        <label for="name">{name_label}</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="{name_placeholder}" required><br>
        <label for="tel">Telefono*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefono" required><br>
        <label for="street-address">Indirizzo completo*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Indirizzo completo" required><br>
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{lp}" />
        <input name="thankyoupage" type="hidden" value="{thankyou}"/>
        <input name="webhook" type="hidden" value="//hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx"/>
        <input name="_key" type="hidden" value="{key}" />

        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{submit}</button>
        </div>
        <script src="{SCRIPT}" async></script>
      </form>"""


FORMS: dict[str, str] = {
    "3038": _form_no_size(
        labels=("Nombre Apellido*", "Dirección*", "Teléfono*"),
        placeholders=("Nombre Apellido", "Dirección", "Teléfono"),
        form_note="🔒 Cero anticipo · Cero tarjeta · Pagas solo cuando lo recibes",
        offer="3038",
        lp="3072",
        thankyou="https://shoptrendcrest.com/es/miorvella/thank-you.html",
        key="edf712c73dc53af6ed1a8675164892b97c1d353d",
        submit="Haz tu pedido",
    ),
    "3039": _form_no_size(
        labels=("Nome Sobrenome*", "Endereço*", "Telefone de contacto*"),
        placeholders=("Nome Sobrenome", "Endereço", "Telefone de contacto"),
        form_note="🔒 Zero adiantamento · Zero cartão · Paga só quando recebe",
        offer="3039",
        lp="3073",
        thankyou="https://shoptrendcrest.com/pt/miorvella/thank-you.html",
        key="41895c821114d8613281b868a3be62073d3421f1",
        submit="Encomendar agora",
    ),
    "3040": _form_no_size(
        labels=("Vorname Nachname*", "Anschrift*", "Telefon*"),
        placeholders=("Vorname Nachname", "Anschrift", "Telefon"),
        form_note="🔒 Keine Vorauszahlung · Keine Karte · Sie zahlen erst bei Erhalt",
        offer="3040",
        lp="3074",
        thankyou="https://shoptrendcrest.com/de/miorvella/thank-you.html",
        key="863aee27a49a3ced43d398d73cc10a9a60ef1ab8",
        submit="Jetzt bestellen",
    ),
    "3041": _form_no_size(
        labels=("Vardas Pavardė*", "Adresas*", "Telefonas*"),
        placeholders=("Vardas Pavardė", "Adresas", "Telefonas"),
        form_note="🔒 Jokio avanso · Jokios kortelės · Mokate tik gavę",
        offer="3041",
        lp="3075",
        thankyou="https://shoptrendcrest.com/lt/miorvella/thank-you.html",
        key="a6e7173a7d99f8a66aef7294d0efa323f7d16a36",
        submit="Užsisakykite dabar",
    ),
    "3042": _form_no_size(
        labels=("Imię Nazwisko*", "Adres*", "Telefon*"),
        placeholders=("Imię Nazwisko", "Adres", "Telefon"),
        form_note="🔒 Zero zaliczki · Bez karty · Płacisz dopiero po odbiorze",
        offer="3042",
        lp="3076",
        thankyou="https://shoptrendcrest.com/pl/miorvella/thank-you.html",
        key="922b197109f4d93a27c5de44e4c7bd058a73737e",
        submit="Zamów teraz",
    ),
    "3044": _form_no_size(
        labels=("Jméno Příjmení*", "Adresa*", "Telefon*"),
        placeholders=("Jméno Příjmení", "Adresa", "Telefon"),
        form_note="🔒 Bez zálohy · Bez karty · Platíte až po převzetí",
        offer="3044",
        lp="3078",
        thankyou="https://shoptrendcrest.com/cz/miorvella/thank-you.html",
        key="cecef87c6281c91b755f5ebd74502586caf3383a",
        submit="Objednat nyní",
    ),
    "2189": _it_form(
        name_label="Nome e cognome*",
        name_placeholder="Nome e cognome",
        offer="2189",
        lp="2212",
        thankyou="https://shoptrendcrest.com/it/miorvella/thank-you.html",
        key="971ca2b0af355f377812909693783a9752b48610",
        submit="Paga alla consegna",
    ),
}
