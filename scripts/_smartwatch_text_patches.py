# -*- coding: utf-8 -*-
"""Post-process smartwatch body HTML per locale (applied after fetch/render)."""

from __future__ import annotations

BODY_PATCHES: dict[str, list[tuple[str, str]]] = {
    "hr": [
        ("izravno s zapešća", "izravno sa zapešća"),
        ("ojačano stiklo", "ojačano staklo"),
        ("bez vadjenja", "bez vađenja"),
    ],
    "sl": [
        ("Prepustnice in kalorije", "Koraki in kalorije"),
        (
            "Pass, šport in spanje v preprost pametni watch za uporabo",
            "Koraki, šport in spanec v preprosti pametni uri",
        ),
        (
            "Noventis™ To se misli za dni, ko ne želite potegniti ven telefon vsaki dve minuti. Predočite opozorila, klice in sporočila v realnem času, preverite najbolj uporabljene aplikacije in lahko ostanete dostopni med delom, vožnjo, hojo ali vlakom.",
            "Noventis™ je zasnovan za dni, ko ne želite ven jemati telefona vsake dve minuti. Na zaslonu vidite opozorila, klice in sporočila v realnem času, preverite najpogosteje uporabljene aplikacije in ostanete dosegljivi med delom, vožnjo, hojo ali vadbo.",
        ),
        ("<h2>Dragi pametni uri vs. Noventis™</h2>", "<h2>Dražje pametne ure v primerjavi z Noventis™</h2>"),
        (
            '"Mislil sem, da je to osnovna smartwatch, vendar ima vse, kar potrebujem: obvestila, klice, korake in spremljanje spanja. Hitro se poveže in prikazen se dobro bere. »',
            '"Mislil sem, da je preprost pametni ura, a ima vse, kar potrebujem: obvestila, klice, korake in spremljanje spanja. Hitro se poveže in zaslon je dobro berljiv."',
        ),
        (
            "<p>-Ja, ja.Noventis™ povezuje z glavnim Android in iPhone pametne telefone preko aplikacije, tako da lahko prejema obvestila in nadzor pametnih funkcij iz vašega zapestja.</p>",
            "<p>Da. Noventis™ se prek aplikacije poveže z glavnimi pametnimi telefoni Android in iPhone, zato prejemate obvestila in upravljate pametne funkcije na zapestju.</p>",
        ),
        (
            "<p>-Ja, ja. Trdna lupina, udoben trak in ojačano steklo so namenjeni delu, sprehodom, lahkim vajam in vsakdanji uporabi.</p>",
            "<p>Da. Trdno ohišje, udoben trak in ojačano steklo so primerno za delo, sprehode, lažje vadbe in vsakodnevno uporabo.</p>",
        ),
        (
            "Za vsak dvom o zdravju vašega zdravnika.",
            "Za vsakršne zdravstvene pomisle se obrnite na zdravnika.",
        ),
    ],
    "pt": [
        ("Passagens e calorias", "Passos e calorias"),
        ("Passes, esportes e dormir em um smartwatch simples para usar", "Passos, desporto e sono num smartwatch simples de utilizar"),
        ("Concha sólida", "Caixa resistente"),
        ("Quando chegará a minha ordem?", "Quando chegará a minha encomenda?"),
        ("você não quer puxar seu telefone", "não quer tirar o telemóvel"),
        ("os aplicativos mais usados", "as aplicações mais usadas"),
        ("você pode permanecer", "pode permanecer"),
        ("academia e rotina", "ginásio e rotina"),
        ("a alça é confortável", "a bracelete é confortável"),
        ("Para qualquer dúvida sobre a saúde do seu médico.", "Para qualquer dúvida de saúde, consulte o seu médico."),
        ("monitoramento do sono", "monitorização do sono"),
        ("Ele se conecta rapidamente e o display lê bem", "Liga-se rapidamente e o ecrã é legível"),
        ("Sim, você pode escolher", "Pode escolher"),
        ("Você não tem que inserir", "Não precisa de introduzir"),
        ("via app, para que você possa", "através da aplicação, para poder"),
        ("conecta-se", "liga-se"),
        ("do seu pulso", "do pulso"),
        ("Você pode falar", "Pode falar"),
        ("casca resistente, a alça confortável", "caixa resistente, bracelete confortável"),
        ("são projetados", "foram concebidos"),
        ("exercícios leves", "treino leve"),
        ("03 — Seu movimento diário", "03 — O seu movimento diário"),
        ("do seu pulso", "do pulso"),
        ("Tens tudo", "Tem tudo"),
        ("Precinta ajustável", "Bracelete ajustável"),
        ("filme protetor para a tela", "película protetora do ecrã"),
        ("SmartwatchNoventis™", "Smartwatch Noventis™"),
        ("utilizaNoventis™", "utiliza Noventis™"),
        (
            'alt="Cliente que utilizaNoventis™ com iPhone>',
            'alt="Cliente que utiliza Noventis™ com iPhone"',
        ),
        ("Sim.Noventis™", "Sim. Noventis™"),
        (
            "O corpo compacto e vidro reforçado torná-lo adequado para a vida real:",
            "O corpo compacto e o vidro reforçado tornam-no adequado à vida real:",
        ),
        ("tanto com o escritório quanto com o lazer", "tanto no escritório como no lazer"),
        ("grave suas atividades esportivas", "registe as suas atividades desportivas"),
        ("esportes, passos", "desportos, passos"),
        ("na tela, embora você não é prático com a tecnologia", "no ecrã, mesmo que não seja experiente em tecnologia"),
        ("alça confortável", "bracelete confortável"),
        ("não tenho que puxar", "não preciso de tirar"),
    ],
    "lt": [
        ("Ojačano staklo", "Sustiprintas stiklas"),
        ("Sportska aktivnost", "Sportinė veikla"),
        ("Što dobivate", "Ką gaunate"),
        ("verificirana kupnja", "patvirtintas pirkimas"),
        ("Pagaliau ne tikrinu", "Pagaliau netikrinu"),
        (
            "«Koristim ga na poslu i u pokretu. Pozivi i obavijesti stižu odmah, sve vidim na prvi pogled bez vadjenja telefona iz torbe.»",
            "«Naudoju darbe ir keliaudamas. Skambučiai ir pranešimai ateina iš karto — viską matau vienu žvilgsniu, be telefono traukimo iš krepšio.»",
        ),
        (
            "«Mislio sam da je osnovni sat, ali ima sve što trebam: obavijesti, pozive, korake i san. Brzo se spaja, zaslon je čitljiv.»",
            "«Maniau, kad tai paprastas laikrodis, bet turi viską: pranešimus, skambučius, žingsnius ir miego stebėjimą. Greitai prisijungia, ekranas aiškus.»",
        ),
        ("Luca R. — Zagreb", "Jonas K. — Vilnius"),
        ("Marko K. — Split", "Marius P. — Kaunas"),
        ("Marta F. — Rijeka", "Greta L. — Klaipėda"),
        (
            "«Kupila sam ga za majku. Jednostavan izbornik, udoban remen i baterija traje cijeli dan. Nakon potvrdnog poziva stigao je bez problema.»",
            "«Nusipirkau jį mamai. Paprastas meniu, patogi apyrankė, baterija užtenka visai dienai. Po patvirtinimo skambučio atėjo be problemų.»",
        ),
        ("Trapūs materialai ar brangios dalys", "Trapios medžiagos ar brangios dalys"),
        ("<td>Savijauga</td>", "<td>Savijauta</td>"),
    ],
    "el": [
        ("<span class=\"tag\">Καλεί ο καρπός.</span>", "<span class=\"tag\">Κλήσεις από τον καρπό</span>"),
        (
            "Περάσματα, αθλήματα και ύπνος σε ένα απλό smartwatch για χρήση",
            "Βήματα, αθλήματα και ύπνος σε ένα απλό smartwatch για χρήση",
        ),
        ("Πάσες και θερμίδες", "Βήματα και θερμίδες"),
        (
            "Για κάθε αμφιβολία σχετικά με την υγεία του γιατρού σας.",
            "Για οποιαδήποτε αμφιβολία σχετικά με την υγεία σας, απευθυνθείτε στον γιατρό σας.",
        ),
    ],
    "bg": [
        (
            "01  год., съобщения и приложения без телефон в ръка",
            "01 — Обаждания, съобщения и приложения без телефон в ръка",
        ),
        (
            "02  гола, елегантна и готова за всеки ден",
            "02 — Здрава, елегантна и готова за всеки ден",
        ),
        ("03  год.", "03 — Вашето ежедневно движение на китката"),
        ("Пропуски, спорт и сън", "Крачки, спорт и сън"),
        ("Пропуски и калории", "Крачки и калории"),
        ("<span class=\"tag\">Китката ме зове.</span>", "<span class=\"tag\">Обаждания от китката</span>"),
        ("<span class=\"tag\">Незабавно уведомления</span>", "<span class=\"tag\">Незабавни известия</span>"),
        ("ходене или влак.", "ходене или тренировка."),
        ("Noventis™Мисли се", "Noventis™ Мисли се"),
        (
            "За всяко съмнение за здравето на Вашия лекар.",
            "При всякакви съмнения относно здравето ви се обърнете към лекар.",
        ),
    ],
    "ro": [
        ("<div class=\"num-eyebrow\">01 </div>", "<div class=\"num-eyebrow\">01 — Apeluri, mesaje și aplicații fără telefon în mână</div>"),
        ("<div class=\"num-eyebrow\">02 </div>", "<div class=\"num-eyebrow\">02 — Robust, elegant și pregătit pentru fiecare zi</div>"),
        (
            "<div class=\"num-eyebrow\">03 </div>",
            "<div class=\"num-eyebrow\">03 — Mișcarea ta zilnică, la încheietură</div>",
        ),
        ("Pase, sport și somn", "Pași, sport și somn"),
        ("Pase și calorii", "Pași și calorii"),
        ("mergeți pe jos sau tren.", "mergeți pe jos sau vă antrenați."),
        ("Încheietura cheamă", "Apeluri la încheietură"),
        (
            "Pentru orice îndoială cu privire la sănătatea medicului dumneavoastră.",
            "Pentru orice îndoială legată de sănătate, adresați-vă medicului dumneavoastră.",
        ),
        ("mici umflaturi zilnice", "mici lovituri cotidiene"),
        (
            "deși nu sunt practice cu tehnologia.",
            "chiar dacă nu sunteți familiarizați cu tehnologia.",
        ),
    ],
    "es": [
        ("Wrist calls", "Llamadas desde la muñeca"),
        ("Concha sólida", "Carcasa resistente"),
        ("la pantalla lee bien", "la pantalla se lee bien"),
        (
            "Noventis™ Se piensa por los días en que no quieres sacar tu teléfono cada dos minutos.",
            "Noventis™ Está pensado para los días en que no quieres sacar el teléfono cada dos minutos.",
        ),
        ("Horas de dormir", "Horas de sueño"),
        (
            "Por cualquier duda sobre la salud de su médico.",
            "Si tiene dudas sobre su salud, consulte a su médico.",
        ),
    ],
    "de": [
        ("Handgelenk ruft", "Anrufe am Handgelenk"),
        ("Pässe, Sport und Schlaf", "Schritte, Sport und Schlaf"),
        ("Pässe und Kalorien", "Schritte und Kalorien"),
        ("des Gehens oder des Zugs zugänglich bleiben", "des Gehens oder des Trainings erreichbar bleiben"),
        ("mit Händen frei", "mit freien Händen"),
        ("kleine tägliche Beulen", "kleine Stöße im Alltag"),
        ("<li>1 Verstellband</li>", "<li>1 Verstellbares Armband</li>"),
        (
            "Für jeden Zweifel an der Gesundheit Ihres Arztes.",
            "Bei gesundheitlichen Fragen wenden Sie sich an Ihren Arzt.",
        ),
    ],
    "pl": [
        ("Kiedy przybędzie mój rozkaz?", "Kiedy dotrze moje zamówienie?"),
        ("utleniania", "natlenienia krwi"),
        (
            "choć nie są praktyczne z technologii.",
            "nawet jeśli nie czujesz się biegły w technologii.",
        ),
        ("wyświetlacz dobrze czyta", "ekran jest czytelny"),
        (
            "Brak jakichkolwiek wątpliwości co do zdrowia lekarza.",
            "W razie wątpliwości dotyczących zdrowia skonsultuj się z lekarzem.",
        ),
    ],
    "cs": [
        ("přímo z zápěstí", "přímo ze zápěstí"),
        ("funkce z zápěstí", "funkce ze zápěstí"),
        ("Koupil jsem ho pro maminku", "Koupila jsem ho pro maminku"),
        ("1.999 Kč", "1 999 Kč"),
        ("3.998 Kč", "3 998 Kč"),
        ("1999 Kč", "1 999 Kč"),
        ("3998 Kč", "3 998 Kč"),
    ],
    "lv": [
        ("JĀ, ES VĒLU", "JĀ, ES VĒLOS"),
        ("Android e iPhone", "Android un iPhone"),
        (
            "Piegāde parasti notiek 2-4 darba dienu laikā",
            "Piegāde parasti notiek 24–48 stundu laikā",
        ),
    ],
}


def apply_body_patches(html: str, locale: str) -> str:
    for old, new in BODY_PATCHES.get(locale, []):
        html = html.replace(old, new)
    from _smartwatch_body_polish import polish_body  # noqa: WPS433

    return polish_body(html, locale)
