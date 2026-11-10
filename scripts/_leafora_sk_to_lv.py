# -*- coding: utf-8 -*-
"""SK → LV for LEAFORA (shoptrendcrest has no lv/leafora; SK page is the source)."""

REPLACEMENTS: list[tuple[str, str]] = [
    (
        "LEAFORA™ — Akumulátorový fúkač-vysávač-drvič 3 v 1, 82 V | -50%",
        "LEAFORA™ — Akumulatora pūtējs-sūcējs-smalcinātājs 3 vienā, 82 V | -50%",
    ),
    (
        "LEAFORA™: akumulátorový fúkač-vysávač-drvič 3 v 1, 82 V. Až 200 minút výdrže, bezkefový motor a rýchlosť vzduchu až 90 m/s. Dnes -50%, platba na dobierku.",
        "LEAFORA™: akumulatora pūtējs-sūcējs-smalcinātājs 3 vienā, 82 V. Līdz 200 min darba laikam, bezkontaktu motors un gaisa ātrums līdz 90 m/s. Šodien -50%, apmaksa pēc saņemšanas.",
    ),
    (
        "⚡ ŠPECIÁLNA ZĽAVA -50% · DORUČENIE DO 3 PRACOVNÝCH DNÍ · PLATBA NA DOBIERKU",
        "⚡ ĪPAŠA -50% ATLAIDE · PIEGĀDE 3 DARBA DIENU LAIKĀ · APMAKSA PĒC SAŅEMŠANAS",
    ),
    (
        "<strong>4,8/5</strong> — na základe viac než <strong>11 000</strong> overených hodnotení",
        "<strong>4,8/5</strong> — balstoties uz vairāk nekā <strong>11 000</strong> verificētām atsauksmēm",
    ),
    (
        "💨 3 v 1 · Dvojitá batéria 82 V · Bez benzínu",
        "💨 3 vienā · Dubulta 82 V baterija · Bez benzīna",
    ),
    (
        "3 v 1: vysávač, fúkač a drvič — bez benzínu a neustálej údržby",
        "3 vienā: sūcējs, pūtējs un smalcinātājs — bez benzīna un pastāvīgas apkopes",
    ),
    (
        "S <strong>LEAFORA™</strong> sa staráte o záhradu s profesionálnym akumulátorovým výkonom: až <strong>200 minút výdrže</strong>, dve batérie <strong>82 V</strong> v balení, bezkefový motor a rýchlosť vzduchu až <strong>90 m/s</strong> na presun mokrého lístia a ťažkých zvyškov bez námahy.",
        "Ar <strong>LEAFORA™</strong> jūs koptējat dārzu ar profesionālu akumulatora jaudu: līdz <strong>200 minūtēm darba</strong>, divas <strong>82 V</strong> baterijas komplektā, bezkontaktu motors un gaisa ātrums līdz <strong>90 m/s</strong>, lai bez piepūles pārvietotu mitras lapas un smagus gružus.",
    ),
    (
        "alt=\"LEAFORA akumulátorový fúkač vysávač\"",
        "alt=\"LEAFORA akumulatora lapu pūtējs un sūcējs\"",
    ),
    (
        "OBJEDNAŤ LEAFORA™ ZA 79 € →",
        "PASŪTĪT LEAFORA™ PAR 79 € →",
    ),
    (
        "🔒 Bez zálohy · Bez karty · Platíte až po prevzatí",
        "🔒 Bez priekšapmaksas · Bez kartes · Maksājat tikai saņemot",
    ),
    (
        "<h4>Doručenie do 3 pracovných dní</h4><p>Po telefonickom potvrdení na celom Slovensku</p>",
        "<h4>Piegāde 3 darba dienu laikā</h4><p>Pēc telefona apstiprinājuma visā Latvijā</p>",
    ),
    (
        "<h4>Platba na dobierku</h4><p>Bez karty, platíte kuriérovi</p>",
        "<h4>Maksa pēc saņemšanas</h4><p>Bez kartes, maksājat kurjeram</p>",
    ),
    (
        "<h4>200 min + 82 V</h4><p>Dvojitá batéria vysokej kapacity</p>",
        "<h4>200 min + 82 V</h4><p>Dubulta augstas ietilpības baterija</p>",
    ),
    (
        "<h4>Spokojnosť alebo vrátenie peňazí</h4><p>2 roky záruky v cene</p>",
        "<h4>Apmierināti vai naudas atmaksa</h4><p>2 gadu garantija iekļauta</p>",
    ),
    ("⏰ Zľava -50% končí za", "⏰ -50% atlaide beidzas pēc"),
    ("<div class=\"lbl\">Hod</div>", "<div class=\"lbl\">St</div>"),
    ("<span class=\"left\">Dostupnosť</span>", "<span class=\"left\">Pieejamība</span>"),
    ("<span class=\"right\">Zostáva len 13 kusov</span>", "<span class=\"right\">Atlikušas tikai 13 vienības</span>"),
    (
        "data-live=\"<strong>{n} ľudí</strong> si práve pozerá LEAFORA™\"",
        "data-live=\"<strong>{n} cilvēki</strong> pašlaik skatās LEAFORA™\"",
    ),
    (
        "<strong>41 ľudí</strong> si práve pozerá LEAFORA™",
        "<strong>41 cilvēks</strong> pašlaik skatās LEAFORA™",
    ),
    (
        "<h2>Dokončite objednávku — LEAFORA™ za 79 €</h2>",
        "<h2>Pabeidziet pasūtījumu — LEAFORA™ par 79 €</h2>",
    ),
    (
        "Zadajte meno, telefón a adresu: zavoláme a potvrdíme detaily pred odoslaním.",
        "Ievadiet vārdu, tālruni un adresi: piezvanīsim, lai apstiprinātu detaļas pirms nosūtīšanas.",
    ),
    ("<label for=\"name\">Meno Priezvisko*</label>", "<label for=\"name\">Vārds Uzvārds*</label>"),
    ('placeholder="Meno Priezvisko"', 'placeholder="Vārds Uzvārds"'),
    ('placeholder="Adresa"', 'placeholder="Adrese"'),
    ("Objednajte si teraz", "Pasūtīt tagad"),
    (
        "Používame technické cookies a cookies tretích strán na zlepšenie vášho zážitku a na analytiku.",
        "Mēs izmantojam tehniskās un trešo pušu sīkdatnes, lai uzlabotu jūsu pieredzi un analītikai.",
    ),
    ("Prijať", "Pieņemt"),
    ("Zistiť viac", "Uzzināt vairāk"),
    ("Odosielanie...", "Nosūta..."),
    ("GEO: 'sk'", "GEO: 'lv'"),
    ("PRODUCT_SLUG: 'leafora-4065'", "PRODUCT_SLUG: 'leafora-4066'"),
    ("OFFER_NAME: 'LEAFORA 4065'", "OFFER_NAME: 'LEAFORA 4066'"),
    ("LP_ID: 'sk-leafora-4065'", "LP_ID: 'lv-leafora-4066'"),
    ('lang="sk"', 'lang="lv"'),
    ("na celom Slovensku", "visā Latvijā"),
    ("Slovensku", "Latvijā"),
    ("Bratislava", "Rīga"),
    ("Košice", "Liepāja"),
    ("Žilina", "Daugavpils"),
    ("overený nákup", "verificēts pirkums"),
    (
        "01 — Profesionálny výkon bez benzínu",
        "01 — Profesionāla jauda bez benzīna",
    ),
    (
        "Výkon ako pri benzínových modeloch, s pohodlím batérie",
        "Jauda kā benzīna modeļiem, ar akumulatora ērtumu",
    ),
    (
        "<span class=\"tag\">Systém 82 V</span>",
        "<span class=\"tag\">82 V sistēma</span>",
    ),
    ("<span class=\"tag\">Bezkefový motor</span>", "<span class=\"tag\">Bezkontaktu motors</span>"),
    ("<span class=\"tag\">Až 90 m/s</span>", "<span class=\"tag\">Līdz 90 m/s</span>"),
    (
        "Záhrada potrebuje <strong>skutočný výkon</strong>. LEAFORA™ má bezkefový motor s vysokým krútiacim momentom — účinnejší a odolnejší. S rýchlosťou vzduchu až <strong>90 m/s</strong> presúvate mokré lístie, hutné zvyšky a ťažké nečistoty bez námahy.",
        "Dārzam vajag <strong>īstu jaudu</strong>. LEAFORA™ ir bezkontaktu motors ar augstu griezes momentu — efektīvāks un izturīgāks. Ar gaisa ātrumu līdz <strong>90 m/s</strong> jūs pārvietojat mitras lapas, blīvus gružus un smagus netīrumus bez piepūles.",
    ),
    (
        "Dve dodané batérie poskytujú až <strong>200 minút výdrže</strong> na dlhé súvislé práce — bez zmesí a dymu.",
        "Divas komplektā esošās baterijas nodrošina līdz <strong>200 minūtēm darba</strong> ilgām nepārtrauktām sesijām — bez maisījumiem un dūmiem.",
    ),
    (
        "02 — Maximálna efektivita, minimum úsilia",
        "02 — Maksimāla efektivitāte, minimāla piepūle",
    ),
    (
        "Za pár sekúnd prepnete z fúkania na vysávanie a drvenie",
        "Dažās sekundēs pārslēdzaties no pūšanas uz sūkšanu un smalcināšanu",
    ),
    (
        "<span class=\"tag\">3 funkcie v 1</span>",
        "<span class=\"tag\">3 funkcijas vienā</span>",
    ),
    ("<span class=\"tag\">Vak 50 L</span>", "<span class=\"tag\">50 L mais</span>"),
    (
        "<span class=\"tag\">Integrované drvenie</span>",
        "<span class=\"tag\">Integrēta smalcināšana</span>",
    ),
    (
        "Systém <strong>3 v 1</strong> umožňuje fúkať, vysávať a drviť bez výmeny nástroja. Drvenie znižuje objem lístia — zbierate viac a menej často vyprázdňujete vak. Extra veľký <strong>50litrový</strong> vak vydrží dlhú prácu bez neustálych pauz.",
        "<strong>3 vienā</strong> sistēma ļauj pūst, sūkt un smalcināt bez instrumenta maiņas. Smalcināšana samazina lapu tilpumu — savācat vairāk un retāk tukšojat maisu. Īpaši liels <strong>50 litru</strong> mais iztur ilgu darbu bez nepārtrauktām pauzēm.",
    ),
    (
        "Bez zmesí a zložitej údržby: zapnete, vyberiete režim a pracujete s konštantnou kontrolou a výkonom.",
        "Bez maisījumiem un sarežģītas apkopes: ieslēdzat, izvēlaties režīmu un strādājat ar stabilu kontroli un jaudu.",
    ),
    (
        "03 — Ľahký, praktický, vždy pripravený",
        "03 — Viegls, praktisks, vienmēr gatavs",
    ),
    (
        "Používate jednou rukou na záhrade, terase, v garáži aj pri aute",
        "Lietojat ar vienu roku dārzā, terasē, garāžā un pie automašīnas",
    ),
    (
        "<span class=\"tag\">Ergonomická rukoväť</span>",
        "<span class=\"tag\">Ergonomiska rokturi</span>",
    ),
    (
        "<span class=\"tag\">Viacúčelové použitie</span>",
        "<span class=\"tag\">Daudzfunkcionāla lietošana</span>",
    ),
    (
        "<span class=\"tag\">Štart počas sekúnd</span>",
        "<span class=\"tag\">Startēšana sekundēs</span>",
    ),
    (
        "<strong>Kompaktná vyvážená</strong> konštrukcia šetrí paže a chrbát. Zapnete, vyberiete režim a idete na to: trávnik, garáž, terasa alebo auto — s oveľa menšou námahou.",
        "<strong>Kompakta, līdzsvarota</strong> konstrukcija samazina slodzi uz rokām un muguras. Ieslēdzat, izvēlaties režīmu un sākat: zāliens, garāža, terase vai auto — ar daudz mazāku piepūli.",
    ),
    (
        "Jeden nástroj na každodenné vonkajšie upratovanie — bez zaplnenia garáže doplnkami.",
        "Viens instruments ikdienas āra uzkopšanai — bez garāžas pildīšanas ar piederumiem.",
    ),
    ("REZERVOVAŤ LEAFORA™ TERAZ →", "REZERVĒT LEAFORA™ TAGAD →"),
    ("Najmúdrejšia voľba", "Gudrākā izvēle"),
    ("Základný fúkač vs LEAFORA™", "Pamata pūtējs pret LEAFORA™"),
    ("Lacný fúkač", "Budžeta pūtējs"),
    ("Funkcie", "Funkcijas"),
    ("Len fúka", "Tikai pūšana"),
    ("Fúka, vysáva a drví (3 v 1)", "Pūšana, sūkšana un smalcināšana (3 vienā)"),
    ("Výdrž", "Darba laiks"),
    ("Jedna batéria, pár minút", "Viena baterija, dažas minūtes"),
    ("Až 200 min s dvojitou 82 V", "Līdz 200 min ar dubultu 82 V"),
    ("Výkon", "Jauda"),
    ("Slabý prúd na mokrom lístí", "Vāja plūsma mitrām lapām"),
    ("Až 90 m/s, bezkefový motor", "Līdz 90 m/s, bezkontaktu motors"),
    ("Zber", "Savākšana"),
    ("Hrable zvlášť", "Grābeklis atsevišķi"),
    ("Vak 50 L + drvenie", "50 L mais + smalcināšana"),
    ("Pohodlie", "Komforts"),
    ("Hmotnosť na pažiach", "Svars uz rokām"),
    ("Ergonomické popruhy v cene", "Ergonomiskās siksnas komplektā"),
    ("Ponuka", "Piedāvājums"),
    ("Plná cena bez sady", "Pilna cena bez komplekta"),
    ("79 € dnes s kompletnou sadou", "79 € šodien ar pilnu komplektu"),
    (
        "Zákazníci, ktorí ho používajú každý týždeň, odporúčajú",
        "Klienti, kas lieto katru nedēļu, iesaka",
    ),
    ("Čo ponuka obsahuje", "Ko ietver piedāvājums"),
    (
        "Kompletná sada LEAFORA™, pripravená na použitie",
        "Pilns LEAFORA™ komplekts, gatavs lietošanai",
    ),
    ("Najdôležitejšie odpovede", "Svarīgākās atbildes"),
    ("Aká je doba doručenia?", "Cik ilgs ir piegādes laiks?"),
    (
        "Po telefonickom potvrdení je doručenie zvyčajne do 3 pracovných dní.",
        "Pēc telefona apstiprinājuma piegāde parasti 3 darba dienu laikā.",
    ),
    ("Môžem platiť na dobierku?", "Vai varu maksāt pēc saņemšanas?"),
    (
        "Áno. Platíte hotovosťou alebo kartou kuriérovi pri doručení, bez online zálohy.",
        "Jā. Maksājat skaidrā naudā vai ar karti kurjeram piegādes brīdī, bez priekšapmaksas internetā.",
    ),
    ("Čo ak nebudem spokojný?", "Ko darīt, ja nebūšu apmierināts?"),
    (
        "Máte záruku spokojnosti s vrátením peňazí a 2 roky záruky na produkt podľa podmienok webu.",
        "Jums ir apmierinātības garantija ar naudas atmaksu un 2 gadu produkta garantija saskaņā ar vietnes noteikumiem.",
    ),
    ("Stačí to na mokré lístie?", "Vai pietiek ar mitrām lapām?"),
    (
        "Áno. Rýchlosť vzduchu až 90 m/s a bezkefový motor s vysokým krútiacim momentom pomáhajú s vlhkým lístím a hutnými zvyškami.",
        "Jā. Gaisa ātrums līdz 90 m/s un bezkontaktu motors ar augstu griezes momentu palīdz ar mitrām lapām un blīviem gružiem.",
    ),
    ("Čo je v balení?", "Kas ir komplektā?"),
    (
        "Stroj 3 v 1, dve batérie 82 V, nabíjačka, vak 50 L, popruhy a manuál — všetko pripravené na prvé použitie.",
        "3 vienā ierīce, divas 82 V baterijas, lādētājs, 50 L mais, siksnas un rokasgrāmata — viss gatavs pirmajai lietošanai.",
    ),
    ("Ako dlho vydrží batéria?", "Cik ilgi darbojas baterija?"),
    (
        "S dvoma dodanými batériami môžete dosiahnuť až <strong>200 minút</strong> výdrže v kombinovanom režime podľa módu a povrchu.",
        "Ar divām komplektā esošajām baterijām varat sasniegt līdz <strong>200 minūtēm</strong> darba kombinētajā režīmā atkarībā no režīma un virsmas.",
    ),
]
