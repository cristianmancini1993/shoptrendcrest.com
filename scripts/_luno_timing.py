# -*- coding: utf-8 -*-
"""FAQ/footer/TYP timing — shipment 24–48h after confirm vs delivery 1–2 business days."""

import re

# Footer: both stages (matches IT intent: spedizione vs consegna).
FOOTER_BLURB = {
    "de": (
        "Nützliche Produkte für den Alltag: Versand innerhalb von 24–48 Stunden nach "
        "telefonischer Bestätigung, Lieferung in 1–2 Werktagen, Zahlung per Nachnahme."
    ),
    "hu": (
        "Hasznos termékek a mindennapokhoz: feladás 24–48 órán belül a telefonos "
        "megerősítés után, házhozszállítás 1–2 munkanapon, utánvétes fizetés."
    ),
    "pt": (
        "Produtos úteis para o dia a dia: envio em 24–48 horas após confirmação "
        "telefónica, entrega em 1–2 dias úteis, pagamento à cobrança."
    ),
    "es": (
        "Productos útiles para el día a día: envío en 24–48 horas tras la confirmación "
        "telefónica, entrega en 1–2 días laborables, pago contra reembolso."
    ),
    "pl": (
        "Przydatne produkty na co dzień: wysyłka w 24–48 godzin po potwierdzeniu "
        "telefonicznym, dostawa w 1–2 dni robocze, płatność przy odbiorze."
    ),
    "cs": (
        "Užitečné produkty pro každodenní život: odeslání do 24–48 hodin po telefonickém "
        "potvrzení, doručení do 1–2 pracovních dnů, platba na dobírku."
    ),
    "lv": (
        "Noderīgi produkti ikdienai: sūtīšana 24–48 stundu laikā pēc telefona apstiprinājuma, "
        "piegāde 1–2 darba dienu laikā, apmaksa pie saņemšanas."
    ),
    "sk": (
        "Užitočné produkty pre každodenný život: odoslanie do 24–48 hodín po telefonickom "
        "potvrdení, doručenie do 1–2 pracovných dní, platba na dobierku."
    ),
}

# Thank-you step 3: delivery window + COD (price inserted by caller).
TY_STEP3 = {
    "de": (
        "Lieferung nach Hause in <strong>1–2 Werktagen</strong> und "
        "<strong>Zahlung per Nachnahme</strong> ({price})"
    ),
    "hu": (
        "Házhozszállítás <strong>1–2 munkanapon</strong> belül, "
        "<strong>utánvét</strong> ({price})"
    ),
    "pt": (
        "Entrega ao domicílio em <strong>1–2 dias úteis</strong> e "
        "<strong>pagamento à entrega</strong> ({price})"
    ),
    "es": (
        "Entrega a domicilio en <strong>1–2 días laborables</strong> y "
        "<strong>pago contra reembolso</strong> ({price})"
    ),
    "pl": (
        "Dostawa w <strong>1–2 dni robocze</strong> i "
        "<strong>płatność przy odbiorze</strong> ({price})"
    ),
    "cs": (
        "Doručení do <strong>1–2 pracovních dnů</strong> a "
        "<strong>dobírka</strong> ({price})"
    ),
    "lv": (
        "Piegāde <strong>1–2 darba dienu</strong> laikā un "
        "<strong>apmaksa pie saņemšanas</strong> ({price})"
    ),
    "sk": (
        "Doručenie do <strong>1–2 pracovných dní</strong> a "
        "<strong>dobierka</strong> ({price})"
    ),
}

TY_STEP3_RE = re.compile(
    r"(<ol class=\"ty-steps-list\">\s*<li>[\s\S]*?</li>\s*<li>[\s\S]*?</li>\s*)<li>[\s\S]*?</li>",
    re.MULTILINE,
)


def patch_footer_blurb(html: str, lang: str) -> str:
    blurb = FOOTER_BLURB[lang]
    return re.sub(
        r'<p class="site-footer__blurb">[^<]*</p>',
        f'<p class="site-footer__blurb">{blurb}</p>',
        html,
    )


def patch_ty_step3(html: str, lang: str, price_s: str) -> str:
    step3 = TY_STEP3[lang].format(price=price_s)
    return TY_STEP3_RE.sub(rf"\1<li>{step3}</li>", html, count=1)
