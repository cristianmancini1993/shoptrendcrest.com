# -*- coding: utf-8 -*-
"""Footer chrome + hero/review patches for LUNO geo landings."""

H1 = {
    "de": '<span class="hl">Tragbarer 3-in-1-Wäschetrockner</span>, der Kleidung in 20 Minuten trocknet, desodorisiert und hygienisiert',
    "hu": '<span class="hl">Hordozható 3 az 1-ben szárító</span>, amely 20 perc alatt szárít, semlegesíti a szagokat és higiénizál',
    "pt": '<span class="hl">Secadora portátil 3 em 1</span> que seca, desodoriza e higieniza a roupa em 20 minutos',
    "es": '<span class="hl">Secadora portátil 3 en 1</span> que seca, desodoriza e higieniza la ropa en 20 minutos',
    "pl": '<span class="hl">Przenośna suszarka 3 w 1</span>, która suszy, usuwa zapachy i higienizuje ubrania w 20 minut',
    "cs": '<span class="hl">Přenosná sušička 3 v 1</span>, která za 20 minut suší, deodorizuje a hygienizuje oblečení',
    "lv": '<span class="hl">Pārnēsājams žāvētājs “3 vienā”</span>, kas 20 minūtēs žāvē, deodorizē un higienizē apģērbu',
    "sk": '<span class="hl">Prenosná sušička 3 v 1</span>, ktorá za 20 minút suší, deodorizuje a hygienizuje oblečenie',
}

REVIEW_ALTS = {
    "de": (
        "LUNO™ im Schlafzimmer mit hängender Wäsche im Innenraum",
        "LUNO™ in der Waschküche mit hängendem Hemd",
    ),
    "hu": (
        "LUNO™ hálószobában, ruhák a belső térben",
        "LUNO™ mosókonyhában, ing a tartóban",
    ),
    "pt": (
        "LUNO™ no quarto com roupa pendurada no interior",
        "LUNO™ na lavandaria com camisa pendurada",
    ),
    "es": (
        "LUNO™ en el dormitorio con ropa colgada en el interior",
        "LUNO™ en la lavandería con camisa colgada",
    ),
    "pl": (
        "LUNO™ w sypialni z ubraniami wewnątrz komory",
        "LUNO™ w pralni z koszulą na wieszaku",
    ),
    "cs": (
        "LUNO™ v ložnici s oblečením uvnitř komory",
        "LUNO™ v prádelně s košilí na věšáku",
    ),
    "lv": (
        "LUNO™ guļamistabā ar apģērbu iekšpusē",
        "LUNO™ veļas telpā ar kreklu uz pakaramā",
    ),
    "sk": (
        "LUNO™ v spálni s oblečením vo vnútri",
        "LUNO™ v práčovni s košeľou na vešiaku",
    ),
}

REVIEW3 = {
    "de": {
        "alt": "LUNO™ zusammengeklappt auf einem Regal in der Waschküche",
        "h4": "Sofort verstaut: ideal bei wenig Platz.",
        "quote": "«Die Waschküche ist klein und der Ständer störte immer. Nach dem Zyklus klappe ich LUNO™ zu und stelle es ins Regal: wenig Platz und immer griffbereit.»",
    },
    "hu": {
        "alt": "LUNO™ összecsukva egy polcon a mosókonyhában",
        "h4": "Azonnal eltehető: tökéletes kis helyre.",
        "quote": "«Kicsi a mosókonyhám, és utáltam az állványt. A ciklus után becsukom a LUNO™-t és a polcra teszem: kevés helyet foglal, mindig kéznél van.»",
    },
    "pt": {
        "alt": "LUNO™ dobrada numa prateleira na lavandaria",
        "h4": "Guarda-se de imediato: perfeita com pouco espaço.",
        "quote": "«A lavandaria é pequena e detestava o estendal sempre à vista. No fim do ciclo fecho a LUNO™ e coloco-a na prateleira: ocupa pouco e fica pronta para a próxima vez.»",
    },
    "es": {
        "alt": "LUNO™ plegada en un estante de la lavandería",
        "h4": "Se guarda al momento: perfecta si tienes poco espacio.",
        "quote": "«La lavandería es pequeña y odiaba el tendedero siempre a la vista. Al terminar el ciclo cierro LUNO™ y la dejo en el estante: ocupa poco y queda lista para la próxima vez.»",
    },
    "pl": {
        "alt": "LUNO™ złożona na półce w pralni",
        "h4": "Od razu schować: idealna przy małej przestrzeni.",
        "quote": "«Mam małą pralnię i irytował mnie stojak. Po cyklu zamykam LUNO™ i odkładam na półkę: zajmuje mało miejsca i jest zawsze pod ręką.»",
    },
    "cs": {
        "alt": "LUNO™ složená na polici v prádelně",
        "h4": "Hned se schová: skvělá, když máte málo místa.",
        "quote": "«Prádelna je malá a sušák mi vadil. Po cyklu LUNO™ zavřu a dám na polici: zabere málo místa a je připravená na příště.»",
    },
    "lv": {
        "alt": "LUNO™ salikta uz plaukta veļas telpā",
        "h4": "Uzreiz noņemama: ideāla, ja maz vietas.",
        "quote": "«Veļas telpa ir maza, un žāvēšanas statīvs vienmēr traucēja. Pēc cikla aizveru LUNO™ un nolieku uz plaukta: aizņem maz vietas un vienmēr ir gatava.»",
    },
    "sk": {
        "alt": "LUNO™ zložená na polici v práčovni",
        "h4": "Hneď ju schováte: ideálna pri malom priestore.",
        "quote": "«Práčovňa je malá a sušiak ma obťažoval. Po cykle LUNO™ zatvorím a dám na poličku: zaberá málo miesta a je pripravená na ďalšie použitie.»",
    },
}

def _footer_blurbs():
    from pathlib import Path
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "_luno_timing", Path(__file__).with_name("_luno_timing.py")
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod.FOOTER_BLURB


_FOOTER_BLURB = _footer_blurbs()

FOOTER = {
    "de": {
        "blurb": _FOOTER_BLURB["de"],
        "info": "Informationen",
        "about": "Über uns",
        "contact": "Kontakt",
        "privacy": "Datenschutz",
        "terms": "AGB",
        "cookie": "Cookie-Richtlinie",
        "ship": "Versand",
        "refund": "Rückgabe",
        "contacts": "Kontakt",
        "rights": "Alle Rechte vorbehalten.",
    },
    "hu": {
        "blurb": _FOOTER_BLURB["hu"],
        "info": "Információ",
        "about": "Rólunk",
        "contact": "Kapcsolat",
        "privacy": "Adatvédelem",
        "terms": "ÁSZF",
        "cookie": "Cookie szabályzat",
        "ship": "Szállítás",
        "refund": "Visszaküldés",
        "contacts": "Elérhetőség",
        "rights": "Minden jog fenntartva.",
    },
    "pt": {
        "blurb": _FOOTER_BLURB["pt"],
        "info": "Informação",
        "about": "Sobre nós",
        "contact": "Contactos",
        "privacy": "Política de privacidade",
        "terms": "Termos e condições",
        "cookie": "Política de cookies",
        "ship": "Envio",
        "refund": "Devoluções",
        "contacts": "Contactos",
        "rights": "Todos os direitos reservados.",
    },
    "es": {
        "blurb": _FOOTER_BLURB["es"],
        "info": "Información",
        "about": "Sobre nosotros",
        "contact": "Contacto",
        "privacy": "Política de privacidad",
        "terms": "Términos y condiciones",
        "cookie": "Política de cookies",
        "ship": "Envío",
        "refund": "Devoluciones",
        "contacts": "Contacto",
        "rights": "Todos los derechos reservados.",
    },
    "pl": {
        "blurb": _FOOTER_BLURB["pl"],
        "info": "Informacje",
        "about": "O nas",
        "contact": "Kontakt",
        "privacy": "Polityka prywatności",
        "terms": "Regulamin",
        "cookie": "Polityka cookies",
        "ship": "Wysyłka",
        "refund": "Zwroty",
        "contacts": "Kontakt",
        "rights": "Wszelkie prawa zastrzeżone.",
    },
    "cs": {
        "blurb": _FOOTER_BLURB["cs"],
        "info": "Informace",
        "about": "O nás",
        "contact": "Kontakt",
        "privacy": "Zásady ochrany osobních údajů",
        "terms": "Obchodní podmínky",
        "cookie": "Zásady cookies",
        "ship": "Doprava",
        "refund": "Vrácení zboží",
        "contacts": "Kontakt",
        "rights": "Všechna práva vyhrazena.",
    },
    "lv": {
        "blurb": _FOOTER_BLURB["lv"],
        "info": "Informācija",
        "about": "Par mums",
        "contact": "Kontakti",
        "privacy": "Privātuma politika",
        "terms": "Noteikumi",
        "cookie": "Sīkdatņu politika",
        "ship": "Piegāde",
        "refund": "Atgriešana",
        "contacts": "Kontakti",
        "rights": "Visas tiesības aizsargātas.",
    },
    "sk": {
        "blurb": _FOOTER_BLURB["sk"],
        "info": "Informácie",
        "about": "O nás",
        "contact": "Kontakt",
        "privacy": "Zásady ochrany súkromia",
        "terms": "Obchodné podmienky",
        "cookie": "Zásady cookies",
        "ship": "Doprava",
        "refund": "Vrátenie tovaru",
        "contacts": "Kontakt",
        "rights": "Všetky práva vyhradené.",
    },
}
