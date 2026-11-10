# -*- coding: utf-8 -*-
"""LT → LV copy for LEAFORA (shoptrendcrest has no lv/leafora; LT page is the Baltic source)."""
# Longest strings first when applying via clone_leafora_geos.apply_replacements.

REPLACEMENTS: list[tuple[str, str]] = [
    (
        "Akumuliatorinis lapų pūstuvas-smulkintuvas-siurblys 3 viename, 82 V",
        "Akumulatora lapu pūtējs-sūcējs-smalcinātājs 3 vienā, 82 V",
    ),
    (
        "⚡ SPECIALI -50% AKCIJA · PRISTATYMAS PER 3 D. D. · APMOKĖJIMAS PRISTATYMO METU",
        "⚡ ĪPAŠA -50% AKCIJA · PIEGĀDE 3 DARBA DIENU LAIKĀ · APMAKSAS PĒC SAŅEMŠANAS",
    ),
    (
        "<strong>4,8/5</strong> — pagal daugiau nei <strong>11 000</strong> patvirtintų atsiliepimų",
        "<strong>4,8/5</strong> — balstoties uz vairāk nekā <strong>11 000</strong> verificētu atsauksmēm",
    ),
    (
        "💨 3 viename · Dviguba 82 V baterija · Be benzino",
        "💨 3 vienā · Dubulta 82 V baterija · Bez benzīna",
    ),
    (
        "3 viename: siurblys, pūstuvas ir smulkintuvas — be benzino ir nuolatinės priežiūros",
        "3 vienā: sūcējs, pūtējs un smalcinātājs — bez benzīna un pastāvīgas apkopes",
    ),
    (
        "Su <strong>LEAFORA™</strong> prižiūrite sodą su profesionalia akumuliatorine galia: iki <strong>200 minučių veikimo</strong>, dvi <strong>82 V</strong> baterijos komplekte, bešepetėlinis variklis ir oro greitis iki <strong>90 m/s</strong>, kad be pastangų judintumėte drėgnus lapus ir sunkias liekanas.",
        "Ar <strong>LEAFORA™</strong> jūs koptējat dārzu ar profesionālu akumulatora jaudu: līdz <strong>200 minūtēm darba</strong>, divas <strong>82 V</strong> baterijas komplektā, bezkontaktu motors un gaisa ātrums līdz <strong>90 m/s</strong>, lai bez piepūles pārvietotu mitras lapas un smagus gružus.",
    ),
    (
        "alt=\"LEAFORA akumuliatorinis lapų pūstuvas siurblys\"",
        "alt=\"LEAFORA akumulatora lapu pūtējs un sūcējs\"",
    ),
    (
        "UŽSAKYTI LEAFORA™ UŽ 69 € →",
        "PASŪTĪT LEAFORA™ PAR 79 € →",
    ),
    (
        "🔒 Jokio avanso · Jokios kortelės · Mokate tik gavę",
        "🔒 Bez priekšapmaksas · Bez kartes · Maksājat tikai saņemot",
    ),
    (
        "<h4>Pristatymas per 3 d. d.</h4><p>Po telefoninio patvirtinimo visoje Lietuvoje</p>",
        "<h4>Piegāde 3 darba dienu laikā</h4><p>Pēc telefona apstiprinājuma visā Latvijā</p>",
    ),
    (
        "<h4>Mokate pristatymo metu</h4><p>Kortelė nereikalinga, mokate kurjeriui</p>",
        "<h4>Maksa pēc saņemšanas</h4><p>Karte nav vajadzīga, maksājat kurjeram</p>",
    ),
    (
        "<h4>200 min + 82 V</h4><p>Dviguba didelės talpos baterija</p>",
        "<h4>200 min + 82 V</h4><p>Dubulta augstas ietilpības baterija</p>",
    ),
    (
        "<h4>Patenkinti arba grąžinami pinigai</h4><p>2 metų garantija įskaičiuota</p>",
        "<h4>Apmierināti vai naudas atmaksa</h4><p>2 gadu garantija iekļauta</p>",
    ),
    (
        "⏰ -50% baigiasi po",
        "⏰ -50% beidzas pēc",
    ),
    ("<div class=\"lbl\">Val</div>", "<div class=\"lbl\">St</div>"),
    ("<div class=\"lbl\">Min</div>", "<div class=\"lbl\">Min</div>"),
    ("<div class=\"lbl\">Sek</div>", "<div class=\"lbl\">Sek</div>"),
    ("<span class=\"left\">Likutis</span>", "<span class=\"left\">Pieejamība</span>"),
    ("<span class=\"right\">Liko tik 13 vnt.</span>", "<span class=\"right\">Atlikušas tikai 13 vienības</span>"),
    (
        "data-live-locale=\"lt\" data-live=\"<strong>{n} {word}</strong> dabar žiūri LEAFORA™\"",
        "data-live-locale=\"lv\" data-live=\"<strong>{n} cilvēki</strong> pašlaik skatās LEAFORA™\"",
    ),
    (
        "<strong>41 žmogus</strong> dabar žiūri LEAFORA™",
        "<strong>41 cilvēks</strong> pašlaik skatās LEAFORA™",
    ),
    (
        "<h2>Užbaikite užsakymą — LEAFORA™ už 69 €</h2>",
        "<h2>Pabeidziet pasūtījumu — LEAFORA™ par 79 €</h2>",
    ),
    (
        "Įrašykite vardą, telefoną ir adresą: paskambinsime patvirtinti detalių prieš siuntimą.",
        "Ievadiet vārdu, tālruni un adresi: piezvanīsim, lai apstiprinātu detaļas pirms nosūtīšanas.",
    ),
    ("<label for=\"name\">Vardas Pavardė*</label>", "<label for=\"name\">Vārds Uzvārds*</label>"),
    ('placeholder="Vardas Pavardė"', 'placeholder="Vārds Uzvārds"'),
    ("<label for=\"street-address\">Adresas*</label>", "<label for=\"street-address\">Adrese*</label>"),
    ('placeholder="Adresas"', 'placeholder="Adrese"'),
    ("<label for=\"tel\">Telefonas*</label>", "<label for=\"tel\">Tālrunis*</label>"),
    ('placeholder="Telefonas"', 'placeholder="Tālrunis"'),
    ("Užsisakykite dabar", "Pasūtīt tagad"),
    (
        "Odosielanie...",
        "Nosūta...",
    ),
    (
        "Používame technické cookies a cookies tretích strán na zlepšenie vášho zážitku a na analytiku.",
        "Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu jūsu pieredzi un analītikai.",
    ),
    (
        "Prijať",
        "Pieņemt",
    ),
    (
        "Zistiť viac",
        "Uzzināt vairāk",
    ),
    ("<span class=\"now\">69 €</span>", "<span class=\"now\">79 €</span>"),
    ("<span class=\"was\">138 €</span>", "<span class=\"was\">158 €</span>"),
    ("už 69 €", "par 79 €"),
    ("UŽ 69 €", "PAR 79 €"),
    ("69 €", "79 €"),
    ("138 €", "158 €"),
    ("GEO: 'lt'", "GEO: 'lv'"),
    ("PRODUCT_SLUG: 'leafora-3189'", "PRODUCT_SLUG: 'leafora-4066'"),
    ("OFFER_NAME: 'LEAFORA 3189'", "OFFER_NAME: 'LEAFORA 4066'"),
    ("LP_ID: 'lt-leafora-3189'", "LP_ID: 'lv-leafora-4066'"),
    ("lang=\"lt\"", "lang=\"lv\""),
    ("visoje Lietuvoje", "visā Latvijā"),
    ("Lietuvoje", "Latvijā"),
]
