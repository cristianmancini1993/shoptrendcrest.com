# -*- coding: utf-8 -*-
"""Natural-language polish for Noventis smartwatch body HTML (post-fetch)."""

from __future__ import annotations

import re

# Applied to every locale after locale-specific patches.
GLOBAL_FIXES: list[tuple[str, str]] = [
    ("SmartwatchNoventis™", "Smartwatch Noventis™"),
    ("smartwatchNoventis™", "smartwatch Noventis™"),
    ("ρολόιNoventis™", "ρολόι Noventis™"),
    ("έξυπνο ρολόιNoventis™", "έξυπνο ρολόι Noventis™"),
    ("reloj inteligenteNoventis™", "reloj inteligente Noventis™"),
    ("complete smartwatchNoventis™", "complete smartwatch Noventis™"),
    ("popolna smartwatchNoventis™", "popoln paket smartwatch Noventis™"),
    ("completoNoventis™", "completo Noventis™"),
    ("completa smartwatchNoventis™", "completa smartwatch Noventis™"),
    ("useNoventis™", "use Noventis™"),
    ("you useNoventis™", "you use Noventis™"),
    ("uporabljateNoventis™", "uporabljate Noventis™"),
    ("verwenden\"Noventis™", "verwenden Noventis™"),
    ("verwenden„Noventis™", "verwenden Noventis™"),
    ("SmartwatchNoventis™с", "Smartwatch Noventis™ с"),
    ("Noventis™с ", "Noventis™ с "),
    ("Noventis™Σ", "Noventis™ Σ"),
    ("Noventis™М", "Noventis™ М"),
    ("Noventis™ Es ", "Noventis™ es "),
    ("Noventis™ Está ", "Noventis™ está "),
    ("Noventis™ É ", "Noventis™ é "),
    ("Noventis™ Ist ", "Noventis™ ist "),
    ("Noventis™¿", "Noventis™ ¿"),
    ("Sim.Noventis™", "Sim. Noventis™"),
    ("Sí.Noventis™", "Sí. Noventis™"),
    ("Ja.Noventis™", "Ja. Noventis™"),
    ("Da.Noventis™", "Da. Noventis™"),
    (" -Ja, ja.", " Da."),
    (" »</p>", "»</p>"),
    ('."»</p>', '."</p>'),
    (' »</p>', '</p>'),
    (' »"', '"'),
]

LOCALE_FIXES: dict[str, list[tuple[str, str]]] = {
    "sl": [
        ("preprost pametni ura", "preprosta pametna ura"),
        ("zažgane kalorije", "porabljene kalorije"),
        ("Trdna ohišja, udoben trak", "Trdno ohišje, udoben trak"),
        ("Vse imaš pod nadzorom, brez rok in manj motenj.", "Vse imate pod nadzorom, roke so proste in manj je motenj."),
        ("telovadnica in vsakodnevna rutina", "telovadba in vsakodnevna rutina"),
        ("Prikazuje ti, koliko si spal ponoči.", "Prikazuje, koliko ste spali ponoči."),
        ("čeprav s tehnologijo niste praktični.", "tudi če niste vešči tehnologije."),
        ("vse vidim s pogledom in ni mi treba", "vse vidim na prvi pogled in ni mi treba"),
        (
            "Dobil sem jo za mamo. Preprost meni, udoben pas in baterija več kot dovolj za vsakdanjo uporabo. Po potrditvi klic prišel gladko.",
            "Dobila sem jo za mamo. Preprost meni, udoben pas in baterija zadostuje za vsakodnevno uporabo. Po potrditvenem klicu je prispela brez težav.",
        ),
        ("Odgovor, ki ga uporabljate Noventis™", "Stranka, ki uporablja Noventis™"),
        ('alt="Odgovor, ki ga uporabljateNoventis™ z iPhone>', 'alt="Stranka z Noventis™ in iPhoneom"'),
        ("<span>Noventis™ Je kompatibilen", "<span>Noventis™ je kompatibilen"),
        ("majhne dnevne izbokline", "majhne dnevne odrgnine"),
        ("Dobro urejen vidik", "Urejen videz"),
        ("so primerno za delo", "so primerni za delo"),
        ("Ojačeno steklo", "Ojačano steklo"),
        ("Sporočila in socialna sporočila", "Sporočila in družbena omrežja"),
    ],
    "pt": [
        ("Mostra o quanto dormiste à noite.", "Mostra quanto dormiu durante a noite."),
        ("O carregamento é preparado rapidamente", "A encomenda é preparada rapidamente"),
        ("assistência e retorno.", "assistência e devolução."),
        ("grave suas atividades", "registe as suas atividades"),
        ("na tela,", "no ecrã,"),
        ("esportes, passos", "desportos, passos"),
        ("Actividades desportivas", "Atividades desportivas"),
        ("quanto com o lazer", "tanto no escritório como no lazer"),
        ('alt="Cliente que utiliza Noventis™ com iPhone>', 'alt="Cliente que utiliza Noventis™ com iPhone"'),
        ("não tenho que puxar", "não preciso de tirar"),
        ("alça confortável", "bracelete confortável"),
        ("Milão", "Milão"),
        ("Nápoles", "Nápoles"),
        ("Um aspecto bem guardado", "Um aspeto cuidado"),
        ("Mensagens e sociais", "Mensagens e redes sociais"),
        (
            "Design premium, proteção durável de vidro e chuva, ginásio e rotina diária",
            "Design premium, vidro resistente e proteção contra a chuva, ginásio e rotina diária",
        ),
    ],
    "el": [
        ("Οραματιστείτε ειδοποιήσεις", "Δείτε ειδοποιήσεις"),
        ("Σκέφτεστε για τις μέρες", "είναι σχεδιασμένο για τις μέρες"),
        ("να τραβάτε το τηλέφωνό σας", "να βγάζετε το τηλέφωνο"),
        ("προσβάσιμες ενώ εργάζεστε", "προσβάσιμοι στη δουλειά"),
        ("οδηγείτε, περπατάτε ή εκπαιδεύετε", "στο αμάξι, στο περπάτημα ή στο γυμναστήριο"),
        ("η οθόνη διαβάζει καλά.", "η οθόνη είναι ευανάγνωστη."),
        ("Περάσματα, αθλήματα", "Βήματα, αθλήματα"),
        ("μικρά καθημερινά εξογκώματα", "μικρά καθημερινά χτυπήματα"),
        ("Απάντηση, διαβάστε", "Απαντήστε, διαβάστε"),
        ("Τα έχεις όλα υπό έλεγχο", "Έχετε τα πάντα υπό έλεγχο"),
        ("Σου δείχνει πόσο κοιμόσουν τα βράδια", "Σας δείχνει πόσο κοιμηθήκατε τα βράδια"),
        (
            "δεν έχω να τραβήξει το τηλέφωνο από την τσάντα κάθε φορά.",
            "δεν χρειάζεται να βγάζω το τηλέφωνο από την τσάντα κάθε φορά.",
        ),
    ],
    "bg": [
        ("Отговор, прочетете", "Отговорете, прочетете"),
        (
            "Noventis™ Мисли се за дните, когато не искаш да си вдигаш телефона на всеки две минути. Визуализиране на сигнали, повикване и съобщения в реално време, проверка на най-използваните приложения и можете да останете достъпни, докато работите, шофиране, ходене или тренировка.",
            "Noventis™ е създаден за дни, в които не искате да вадите телефона на всеки две минути. Виждате известия, обаждания и съобщения в реално време, проверявате най-често използваните приложения и оставате на разположение по време на работа, шофиране, разходка или тренировка.",
        ),
        ("с свободни ръце", "със свободни ръце"),
        ("малки ежедневни подутини", "малки ежедневни удари"),
        ("оценява изгорени калории", "оценете изгорените калории"),
        (
            "Показва колко си спал през нощта. Той също така показва",
            "Показва колко сте спали през нощта. Показва и",
        ),
        ("въпреки че не сте практични с технологията.", "дори ако не сте напреднали с технологиите."),
        ("Съобщения и социални</span>", "Съобщения и социални мрежи</span>"),
        (
            "Premium дизайн, трайно стъкло и дъжд защита, фитнес и ежедневна рутина",
            "Premium дизайн, трайно стъкло, защита от дъжд, фитнес и ежедневна рутина",
        ),
        ("Твърда черупка", "Здрав корпус"),
        ("Здравата черупка", "Здрав корпус"),
        ("Luca R.  год. Рим, потвърдена покупка", "Luca R. — Рим, потвърдена покупка"),
        ("дисплеят чете добре.", "дисплеят е лесен за четене."),
        (
            "След потвърждението обаждането пристигна гладко.",
            "След обаждането за потвърждение поръчката пристигна без проблеми.",
        ),
    ],
    "ro": [
        (
            "Design premium, protecție durabilă a sticlei și ploii, sală de gimnastică și rutină zilnică",
            "Design premium, sticlă rezistentă, protecție la ploaie — sală și rutină zilnică",
        ),
        (
            "Pași, sport și somn într-un simplu smartwatch pentru a utiliza",
            "Pași, sport și somn într-un smartwatch simplu, ușor de folosit",
        ),
        ("mici umflaturi zilnice", "mici lovituri cotidiene"),
        (
            "deși nu sunt practice cu tehnologia.",
            "chiar dacă nu sunteți familiarizați cu tehnologia.",
        ),
        (
            "Am luat-o pentru mama. Meniu simplu, curea confortabil și baterie mai mult decât suficient pentru utilizarea de zi cu zi. După ce apelul de confirmare a sosit fără probleme.",
            "Am luat-o pentru mama. Meniu simplu, curea confortabilă și baterie mai mult decât suficientă pentru utilizarea zilnică. După apelul de confirmare, comanda a ajuns fără probleme.",
        ),
        ("asistență și întoarcere.", "asistență și returnare."),
        ("Ai totul sub control", "Aveți totul sub control"),
        (
            "Corpul compact si sticla armata il fac potrivit pentru viata reala: schimburi, lucrari, antrenamente, ploaie usoara si mici lovituri cotidiene.",
            "Corpul compact și sticla armată îl fac potrivit pentru viața reală: schimburi, lucrări, antrenamente, ploaie ușoară și mici lovituri cotidiene.",
        ),
        (
            "Îţi arată cât de mult ai dormit noaptea.",
            "Vă arată cât de mult ați dormit noaptea.",
        ),
        ("ecranul citește bine.", "ecranul este ușor de citit."),
        ("nu trebuie să scoateți telefonul", "nu trebuie să scot telefonul"),
    ],
    "es": [
        ("cuánto dormiste por la noche", "cuánto durmió por la noche"),
        (
            "Tienes todo bajo control, con manos libres y menos distracciones.",
            "Tiene todo bajo control, con las manos libres y menos distracciones.",
        ),
        ("no quieres sacar el teléfono", "no quiere sacar el teléfono"),
        ("Visualiza alertas", "Visualice alertas"),
        ("revisa las aplicaciones", "revise las aplicaciones"),
        ("puedes mantenerte accesible mientras trabajas, conduces, caminas o entrenas", "puede mantenerse accesible mientras trabaja, conduce, camina o entrena"),
        ("Te muestra cuánto durmió", "Le muestra cuánto durmió"),
        ("03 — Tu movimiento cotidiano", "03 — Su movimiento cotidiano"),
        ("Mensajes y sociales</span>", "Mensajes y redes sociales</span>"),
        (
            "Pasos, deportes y dormir en un simple reloj inteligente para usar",
            "Pasos, deporte y sueño en un reloj inteligente fácil de usar",
        ),
        ("Cuenta los pasos, estima calorías quemadas y registra tus actividades deportivas.", "Cuente los pasos, estime las calorías quemadas y registre sus actividades deportivas."),
        ("La robusta cáscara,", "La resistente carcasa,"),
        ("entrar tarjetas", "introducir los datos de la tarjeta"),
        ("y el regreso.", "y la devolución."),
        ("aunque no es práctico con la tecnología.", "aunque no se sienta cómodo con la tecnología."),
        ("puedes elegir", "puede elegir"),
        ("monitoreo del sueño", "seguimiento del sueño"),
        ("la pantalla se lee bien", "la pantalla es fácil de leer"),
        (
            "Usted no tiene que introducir los datos de la tarjeta o pagar los anticipos en el sitio.",
            "No tiene que introducir los datos de la tarjeta ni pagar por adelantado en la web.",
        ),
        (
            "Finalmente no comprobé mi teléfono cada minuto.",
            "Por fin no tengo que mirar el móvil cada minuto.",
        ),
        ("Pagas también el logo", "Paga también el logo"),
    ],
    "de": [
        ("Nachrichten und soziale</span>", "Nachrichten und soziale Netzwerke</span>"),
        (
            "Noventis™ Es wird für die Tage gedacht, an denen Sie Ihr Telefon nicht alle zwei Minuten herausziehen möchten. Visualisieren Sie Benachrichtigungen, Anrufe und Echtzeitnachrichten, überprüfen Sie die am häufigsten verwendeten Apps und Sie können während der Arbeit, des Fahrens, des Gehens oder des Trainings erreichbar bleiben.",
            "Noventis™ ist für Tage gedacht, an denen Sie Ihr Smartphone nicht ständig herausholen möchten. Sehen Sie Benachrichtigungen, Anrufe und Nachrichten in Echtzeit, prüfen Sie Ihre wichtigsten Apps und bleiben Sie bei Arbeit, Fahrt, Spaziergang oder Training erreichbar.",
        ),
        (
            "Schritte, Sport und Schlaf in einer einfachen Smartwatch zu verwenden",
            "Schritte, Sport und Schlaf – in einer einfachen Smartwatch",
        ),
        (
            "obwohl Sie mit Technologie nicht praktisch sind.",
            "auch wenn Sie technisch nicht versiert sind.",
        ),
        (
            '"Ich dachte, es wäre eine grundlegende Smartwatch, aber sie hat alles, was ich brauche: Benachrichtigungen, Anrufe, Schritte und Schlafüberwachung." Es verbindet sich schnell und das Display liest sich gut.',
            '"Ich dachte, es wäre eine einfache Smartwatch, aber sie hat alles, was ich brauche: Benachrichtigungen, Anrufe, Schritte und Schlaftracking. Sie verbindet sich schnell und das Display ist gut lesbar."',
        ),
        (
            "Ich habe es für meine Mutter bekommen. Einfaches Menü, bequemes Band und Batterie mehr als genug für den täglichen Gebrauch. Nachdem der Bestätigungsruf reibungslos eingetroffen war.",
            "Ich habe sie für meine Mutter gekauft. Einfaches Menü, bequemes Armband und die Akku-Laufzeit reicht für den ganzen Tag. Nach dem Bestätigungsanruf kam sie problemlos an.",
        ),
        (
            '"Ich benutze es bei der Arbeit und wenn ich da bin." Anrufe und Benachrichtigungen kommen sofort, ich sehe alles mit einem Blick und muss nicht jedes Mal das Telefon aus der Tasche ziehen.',
            '"Ich nutze sie bei der Arbeit und unterwegs. Anrufe und Benachrichtigungen kommen sofort, ich sehe alles auf einen Blick und muss das Handy nicht jedes Mal aus der Tasche holen."',
        ),
        ("Premium Design, langlebiger Glas- und Regenschutz, Fitnessstudio und Tagesablauf", "Premium-Design, robustes Glas, Regenschutz – fürs Fitnessstudio und den Alltag"),
        ("Ein gepflegter Aspekt, aber ohne den Zuschlag der großen Marken.", "Gepflegte Optik – ohne den Aufpreis für große Marken."),
        ("Ja.Noventis™ Verbindet", "Ja. Noventis™ verbindet"),
        (
            "<span>Noventis™ Ist es mit meinem Telefon kompatibel?</span>",
            "<span>Ist Noventis™ mit meinem Smartphone kompatibel?</span>",
        ),
        ('alt="Client, den Sie verwenden Noventis™ für das Rennen>', 'alt="Kunde mit Noventis™ beim Laufen"'),
        ('alt="Kit komplette Smartwatch"Noventis™„>', 'alt="Komplettes Noventis™ Smartwatch-Kit"'),
        ("<span class=\"tag\">Vollschale</span>", "<span class=\"tag\">Robustes Gehäuse</span>"),
        (
            "Für den Preis, den er hat, hat er mich überrascht.",
            "Für diesen Preis hat sie mich überrascht.",
        ),
    ],
    "pl": [
        ("Często trzeba wyciągać telefon", "Często trzeba wyciągać telefonu"),
        ("Widzę wszystko z spojrzeniem i nie muszę wyciągać telefon z torby", "Widzę wszystko na pierwszy rzut oka i nie muszę wyciągać telefonu z torby"),
        ("1 Regulowana taśma", "1 Regulowany pasek"),
        ("pomocy i powrotu.", "pomocy i zwrotu."),
        ("choć nie są praktyczne z technologii.", "nawet jeśli nie czujesz się biegły w technologii."),
        ("wyświetlacz dobrze czyta", "ekran jest czytelny"),
        ("Dobrze utrzymany aspekt", "Estetyczny wygląd"),
        (
            "Po potwierdzeniu połączenie przyszło gładko \".",
            "Po rozmowie potwierdzającej zamówienie dotarło bez problemów.",
        ),
        (
            'Po potwierdzeniu połączenie przyszło gładko ".',
            "Po rozmowie potwierdzającej zamówienie dotarło bez problemów.",
        ),
        (
            "Po rozmowie potwierdzającej zamówienie dotarło bez problemów.\"",
            "Po rozmowie potwierdzającej zamówienie dotarło bez problemów.",
        ),
    ],
    "cs": [
        ("Koupil jsem ho pro maminku", "Koupila jsem ho pro maminku"),
    ],
    "lv": [],
    "hr": [],
    "lt": [],
}

_TESTIMONIAL_QUOTE_LOCALES = frozenset({"sl", "pt", "el", "bg", "ro", "es"})


def _normalize_testimonial_quotes(html: str) -> str:
    """Wrap testimonial body paragraphs in matching «…» quotes."""

    def _repl(m: re.Match[str]) -> str:
        prefix, text, suffix = m.group(1), m.group(2), m.group(3)
        t = text.strip()
        if t.startswith('"'):
            t = t[1:].lstrip()
        t = t.rstrip('"').strip()
        if t.startswith("«"):
            t = t[1:].lstrip()
        if t.endswith("»"):
            t = t[:-1].rstrip()
        return f"{prefix}«{t}»{suffix}"

    return re.sub(
        r'(<div class="t-body">[\s\S]*?<p>)([^<]+)(</p>)',
        _repl,
        html,
    )


def _fix_broken_img_alts(html: str) -> str:
    html = html.replace('onerror=" this.onerror', 'onerror="this.onerror')
    html = re.sub(r'alt="([^"]*?)Noventis™ ([^"]*?)(?<!")>', r'alt="\1Noventis™ \2">', html)
    html = re.sub(r'([^«"])\»</p>', r"\1</p>", html)
    return html


def polish_body(html: str, locale: str) -> str:
    for old, new in LOCALE_FIXES.get(locale, []):
        html = html.replace(old, new)
    for old, new in GLOBAL_FIXES:
        html = html.replace(old, new)
    html = re.sub(r"Noventis™([α-ωΑ-ΩΆ-ώa-z])", r"Noventis™ \1", html)
    html = _fix_broken_img_alts(html)
    if locale in _TESTIMONIAL_QUOTE_LOCALES:
        html = _normalize_testimonial_quotes(html)
    return html
