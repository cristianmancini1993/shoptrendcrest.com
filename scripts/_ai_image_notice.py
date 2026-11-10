# -*- coding: utf-8 -*-
"""Localized paragraph for AI-generated or AI-modified product imagery (footer)."""

from __future__ import annotations

# Keys match HTML `lang` where possible (el/gr, et/ee, sl/si).
_AI_IMAGE_NOTICE: dict[str, str] = {
    "en": (
        "Some images on this page have been generated or modified using artificial "
        "intelligence and are intended for illustrative purposes only. They may not "
        "accurately represent the product's actual appearance, size, colors, "
        "features, or performance."
    ),
    "it": (
        "Alcune delle immagini presenti in questa pagina sono state create o "
        "modificate con l’ausilio dell’intelligenza artificiale e hanno uno scopo "
        "puramente illustrativo e comunicativo. Potrebbero non rappresentare fedelmente "
        "l’aspetto reale, le dimensioni, i colori, le caratteristiche o le prestazioni "
        "del prodotto, che possono differire da quanto raffigurato."
    ),
    "de": (
        "Einige Bilder auf dieser Seite wurden mit Künstlicher Intelligenz erstellt "
        "oder bearbeitet und dienen nur zur Veranschaulichung. Sie geben möglicherweise "
        "nicht genau wieder, wie das Produkt in Wirklichkeit aussieht, welche Größe "
        "oder Farben es hat, welche Funktionen es bietet oder wie es sich in der "
        "Anwendung verhält."
    ),
    "fr": (
        "Certaines images de cette page ont été générées ou modifiées à l’aide de "
        "l’intelligence artificielle et sont fournies à titre illustratif uniquement. "
        "Elles peuvent ne pas refléter fidèlement l’apparence réelle du produit, sa "
        "taille, ses couleurs, ses caractéristiques ou ses performances."
    ),
    "es": (
        "Algunas imágenes de esta página se han generado o modificado con "
        "inteligencia artificial y tienen solo fines ilustrativos. Es posible que no "
        "reflejen con exactitud el aspecto real del producto, su tamaño, colores, "
        "características o rendimiento."
    ),
    "pt": (
        "Algumas imagens nesta página foram geradas ou alteradas com recurso à "
        "inteligência artificial e destinam-se apenas a fins ilustrativos. Podem não "
        "corresponder com exatidão à aparência real do produto, às dimensões, às "
        "cores, às características ou ao desempenho."
    ),
    "pl": (
        "Niektóre zdjęcia na tej stronie zostały wygenerowane lub zmodyfikowane przy "
        "użyciu sztucznej inteligencji i służą wyłącznie celom poglądowym. Mogą nie "
        "oddawać wiernie rzeczywistego wyglądu produktu, jego rozmiaru, kolorów, cech "
        "lub wydajności."
    ),
    "cs": (
        "Některé obrázky na této stránce byly vytvořeny nebo upraveny pomocí umělé "
        "inteligence a slouží pouze jako ilustrace. Nemusí přesně odpovídat skutečnému "
        "vzhledu výrobku, jeho rozměrům, barvám, vlastnostem nebo výkonu."
    ),
    "sk": (
        "Niektoré obrázky na tejto stránke boli vytvorené alebo upravené pomocou "
        "umelej inteligencie a slúžia len na ilustráciu. Nemusia presne zodpovedať "
        "skutočnému vzhľadu výrobku, jeho rozmerom, farbám, vlastnostiam ani výkonu."
    ),
    "hu": (
        "Az oldalon szereplő egyes képek mesterséges intelligenciával készültek vagy "
        "módosultak, és csak szemléltetési célt szolgálnak. Előfordulhat, hogy nem "
        "tükrözik pontosan a termék valódi megjelenését, méretét, színeit, "
        "jellemzőit vagy teljesítményét."
    ),
    "ro": (
        "Unele imagini de pe această pagină au fost generate sau modificate cu "
        "inteligență artificială și au doar scop ilustrativ. Este posibil să nu "
        "reflecte cu exactitate aspectul real al produsului, dimensiunile, culorile, "
        "caracteristicile sau performanța."
    ),
    "lt": (
        "Kai kurie šio puslapio vaizdai buvo sukurti arba redaguoti naudojant "
        "dirbtinį intelektą ir skirti tik iliustracijai. Jie gali tiksliai neatitikti "
        "tikrosios prekės išvaizdos, dydžio, spalvų, savybių ar veikimo."
    ),
    "lv": (
        "Dažas šīs lapas attēli ir izveidoti vai rediģēti, izmantojot mākslīgo "
        "intelektu, un paredzēti tikai ilustratīviem mērķiem. Tie var precīzi "
        "neatspoguļot produkta faktisko izskatu, izmērus, krāsas, īpašības vai "
        "veiktspēju."
    ),
    "hr": (
        "Neke slike na ovoj stranici generirane su ili izmijenjene pomoću umjetne "
        "inteligencije i služe isključivo ilustrativnoj svrsi. Mogu točno ne "
        "odražavati stvarni izgled proizvoda, veličinu, boje, značajke ili performanse."
    ),
    "sl": (
        "Nekatere slike na tej strani so bile ustvarjene ali spremenjene z umetno "
        "inteligenco in so namenjene le kot ilustracija. Morda ne odražajo natančno "
        "dejanskega videza izdelka, velikosti, barv, lastnosti ali zmogljivosti."
    ),
    "bg": (
        "Някои изображения на тази страница са генерирани или променени с изкуствен "
        "интелект и са само с илюстративна цел. Може да не отразяват точно реалния "
        "вид на продукта, размера, цветовете, характеристиките или представянето му."
    ),
    "el": (
        "Ορισμένες εικόνες σε αυτή τη σελίδα έχουν δημιουργηθεί ή τροποποιηθεί με "
        "τεχνητή νοημοσύνη και προορίζονται μόνο για εικονογραφικούς σκοπούς. "
        "Ενδέχεται να μην αποτυπώνουν με ακρίβεια την πραγματική εμφάνιση του "
        "προϊόντος, το μέγεθος, τα χρώματα, τα χαρακτηριστικά ή τις επιδόσεις του."
    ),
    "et": (
        "Mõned selle lehe pildid on loodud või muudetud tehisintellekti abil ja on "
        "mõeldud ainult illustreerimiseks. Need ei pruugi täpselt vastata toote "
        "tegelikule välimusele, suurusele, värvidele, omadustele või jõudlusele."
    ),
}


def ai_image_notice_html(lang: str) -> str:
    """Return escaped HTML paragraph for the given page language code."""
    text = _AI_IMAGE_NOTICE.get(lang) or _AI_IMAGE_NOTICE["en"]
    esc = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    return f'<p class="site-footer__ai-image-notice">{esc}</p>'


def footer_blurb_column_html(blurb: str, lang: str, *, show_ai_notice: bool) -> str:
    """First grid column: logo + blurb + optional AI image notice."""
    notice = f"\n        {ai_image_notice_html(lang)}" if show_ai_notice else ""
    return f"""      <div>
        <a href="/" class="site-logo" aria-label="homeshopspot.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">{blurb}</p>{notice}
      </div>"""


def strip_ai_notice(html: str) -> str:
    """Remove existing AI notice paragraphs (idempotent rebuilds)."""
    import re

    return re.sub(
        r'\s*<p class="site-footer__ai-image-notice">[\s\S]*?</p>',
        "",
        html,
    )

