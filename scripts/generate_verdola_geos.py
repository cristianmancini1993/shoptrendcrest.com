# -*- coding: utf-8 -*-
"""Generate Verdola landings + thank-you for RO/CZ/HU/SK/PL/DE with product codes."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import ai_image_notice_html, footer_blurb_column_html

ROOT = Path(__file__).resolve().parents[1]

GEOS = [
    dict(code="151", geo="ro", lang="ro", currency="RON", price=419.0, schema="419.00", now="419 lei", was="838 lei", cpa=17.0),
    dict(code="152", geo="cz", lang="cs", currency="CZK", price=1999.0, schema="1999", now="1.999 Kč", was="3.998 Kč", cpa=16.0),
    dict(code="153", geo="hu", lang="hu", currency="HUF", price=29999.0, schema="29999", now="29.999 Ft", was="59.998 Ft", cpa=16.0),
    dict(code="154", geo="sk", lang="sk", currency="EUR", price=79.99, schema="79.99", now="79,99 €", was="159,98 €", cpa=16.0),
    dict(code="155", geo="pl", lang="pl", currency="PLN", price=349.0, schema="349.00", now="349 zł", was="698 zł", cpa=16.0),
    dict(code="326", geo="de", lang="de", currency="EUR", price=79.90, schema="79.90", now="79,90 €", was="159,80 €", cpa=18.5),
]

# Compact UI packs — keys must match for all geos
PACKS = {}

PACKS["ro"] = {
    "title": "Verdola™ Cositoare 3000W — Baterie 48V, 1,4 kg | Kit Complet -50%",
    "desc": "Verdola™: cositoare cu baterie 48V de 3000W, doar 1,4 kg. Kit complet inclus, încărcare 4–5 ore. Ramburs la livrare, livrare gratuită 24/48h.",
    "og_title": "Verdola™ Cositoare 3000W 48V — Kit Complet -50%",
    "og_desc": "3000W, baterii 48V, 1,4 kg. Kit complet inclus. Ramburs la livrare.",
    "pname": "Verdola™ Cositoare cu Baterie 48V 3000W",
    "pdesc": "Cositoare 48V 3000W, 1,4 kg. Kit complet cu baterii, încărcător (4–5 ore), curea și protecție plante.",
    "offer": "Verdola Cositoare RO",
    "submit": "Se trimite...",
    "ck_t": "Folosim cookie-uri tehnice și de terți pentru a îmbunătăți experiența ta și pentru analiză.",
    "ck_a": "Acceptă", "ck_l": "Află mai multe",
    "topbar": "🔥 OFERTĂ DE SEZON -50% + LIVRARE GRATUITĂ — RAMBURS LA LIVRARE 🔥",
    "rating": "<strong>4,8/5</strong> — Peste <strong>3.842</strong> clienți mulțumiți · <strong>170+</strong> recenzii verificate",
    "gift": "📦 Kit complet inclus · Garanție 24 luni · Livrare 24/48h",
    "h1": 'Taie iarba fără efort și <span class="hl">fără dureri de spate</span> — 3000W, doar 1,4 kg',
    "lead": "<strong>Verdola™</strong> este cositoarea cu baterie <strong>48V de 3000W</strong> ultraușoară — doar <strong>1,4 kg</strong> — cu <strong>curea de suport integrată</strong> și <strong>kit complet inclus</strong>. Finisează borduri și zone dificile fără cabluri, benzină și stres.",
    "alt": "Verdola™ cositoare 3000W baterie 48V 1,4 kg kit complet",
    "cta": "✓ CONFIRMĂ COMANDA — {price} →",
    "cta_b": "✓ CONFIRMĂ COMANDA — {price}",
    "note": "🔒 Fără avans · Fără card · Plătești doar la livrare",
    "f1h": "3000 W putere", "f1p": "Taie iarbă înaltă și tufișuri",
    "f2h": "Baterii 48 V", "f2p": "Performanță constantă, fără scăderi",
    "f3h": "Doar 1,4 kg", "f3p": "Ultraușoară, zero oboseală",
    "f4h": "4–5 ore încărcare", "f4p": "Gata pentru următoarea lucrare",
    "cd": "⏰ Oferta -50% expiră în", "lh": "Ore", "lm": "Min", "ls": "Sec",
    "sl": "Disponibilitate", "sr": "Au mai rămas doar 9 bucăți la acest preț",
    "live": "<strong>{n} persoane</strong> se uită acum la Verdola",
    "live0": "<strong>42 persoane</strong> se uită acum la Verdola",
    "fh2": "Completează formularul pentru a finaliza comanda",
    "fp": "Comandă azi și <strong>livrarea de mâine este gratuită.</strong> Un operator te sună în maxim 1 oră.",
    "ln": "Nume și prenume*", "pn": "Nume și prenume",
    "lp": "Număr de telefon*", "pp": "Număr de telefon",
    "la": "Adresa de livrare*", "pa": "Adresa de livrare",
    "w1e": "01 — Tăiere precisă și rapidă",
    "w1h": "Finisează borduri, straturi și zone dificile în câteva minute",
    "w1t": ("Precizie", "Borduri", "Straturi"),
    "w1p": "Verdola™ elimină iarba înaltă și bordurile neregulate cu <strong>precizie ridicată</strong>, chiar și în punctele înguste. Grădină curată de la prima trecere.",
    "w1i": "Perfectă de-a lungul zidurilor, gardurilor și colțurilor unde cositoarea normală nu ajunge.",
    "w1a": "Verdola tăiere precisă borduri",
    "w2e": "02 — 3000 W și baterii 48 V",
    "w2h": "Putere profesională fără cabluri, benzină sau mentenanță costisitoare",
    "w2t": ("3000 W", "48 V", "4–5 h încărcare"),
    "w2p": "Motorul de <strong>3000 W</strong> cu <strong>baterii 48 V</strong> menține performanțe constante pe iarbă înaltă. În <strong>kitul complet</strong>, bateriile se încarcă în <strong>4–5 ore</strong>.",
    "w2i": "Iarbă înaltă, mărăcini și borduri dificile — aceeași putere de la început până la sfârșit.",
    "w2a": "Verdola 3000W baterii 48V",
    "w3e": "03 — Doar 1,4 kg, ergonomică și sigură",
    "w3h": "Ultraușoară + cap reglabil + curea de suport",
    "w3t": ("1,4 kg", "Curea", "Kit complet"),
    "w3p": "Doar <strong>1,4 kg</strong>. <strong>Cap reglabil</strong> pentru colțuri fără aplecare. <strong>Curea integrată</strong> pentru spate și brațe. Totul în <strong>kitul complet</strong>.",
    "w3i": "Protecție plante integrată lângă straturi și flori.",
    "w3a": "Verdola cap reglabil și curea",
    "cl": "Comparație",
    "ch": "Cositoare cu fir vs motocoasă pe benzină vs Verdola™",
    "cc": "Cu fir / pe benzină",
    "rows": [
        ("Putere", "Limitată", "3000 W — taie iarbă înaltă și tufișuri"),
        ("Greutate", "Greu, dureri după 20 min", "Doar 1,4 kg + curea ergonomică"),
        ("Cabluri/benzină", "Fire sau benzină scumpă", "100% baterie 48 V — zero cabluri"),
        ("Precizie", "Greu în colțuri", "Cap reglabil — borduri și straturi"),
        ("Încărcare", "Benzină/fir limitativ", "Baterii 48 V — 4–5 ore"),
        ("Zgomot", "95+ dB", "Silentioasă — orice oră"),
        ("Protecție", "Risc pentru flori", "Protecție plante inclusă"),
        ("Cost", "200–400€ + benzină", "Doar {price} kit complet"),
        ("Garanție", "1 an sau mai puțin", "24 luni + retur 30 zile"),
    ],
    "th2": "Mii de oameni aleg Verdola™ — iată ce spun",
    "teye": "★ 4,8/5 · Achiziție verificată · Recenzii autentice",
    "ver": "✔ Achiziție verificată",
    "reviews": [
        ("Andrei M. — București, România", "În sfârșit grădină fără dureri de spate!", "Cu cositoarea clasică mă durea spatele. Cu Verdola™, cureaua face treaba grea — recomand!"),
        ("Mihai P. — Cluj-Napoca, România", "Foarte puternică pe iarbă înaltă", "3000W, 1,4 kg, baterii 48V. Treabă curată în jumătate din timp."),
        ("Ionel D. — Timișoara, România", "Ușor de folosit", "Pornește imediat. Plata ramburs fără probleme."),
    ],
    "ke": "Ce găsești în pachet",
    "kh": "Kit complet inclus — gata de utilizare",
    "ka": "Pachet Verdola™ cositoare",
    "kit": [
        "<strong>1× Verdola™ cositoare pe baterie</strong> — 3000 W, 1,4 kg",
        "<strong>2× baterii litiu 48 V</strong> — în kitul complet",
        "<strong>1× încărcător</strong> — 4–5 ore",
        "<strong>1× bobină fir nailon</strong>",
        "<strong>1× protecție plante</strong>",
        "<strong>1× curea ergonomică</strong>",
        "<strong>1× manual</strong> în română",
        "<strong>Livrare gratuită</strong> 24/48h",
        "<strong>Ramburs la livrare</strong>",
        "<strong>Retur gratuit 30 zile</strong>",
        "<strong>Garanție 24 luni</strong>",
    ],
    "faqh": "Întrebări frecvente",
    "faqs": [
        ("Pot plăti ramburs, fără card?", "Da — plătești cash la curier. Fără avans, fără card."),
        ("Primesc asistență la comandă?", "Da — un consultant te sună în maxim 1 oră."),
        ("Cât durează încărcarea?", "Bateriile <strong>48 V</strong> se încarcă în <strong>4–5 ore</strong>."),
        ("Merge pe iarbă înaltă?", "Da — <strong>3000 W</strong> și baterii <strong>48 V</strong>."),
        ("Cât cântărește?", "Doar <strong>1,4 kg</strong> + curea de suport."),
        ("Ce include kitul?", "Cositoare 3000W, 2 baterii 48V, încărcător, fir, protecție, curea, manual."),
        ("Cum returnez?", "30 de zile, retur gratuit dacă e în stare perfectă."),
        ("Cum e garanția?", "24 luni — reparație sau înlocuire gratuită."),
        ("Datele sunt în siguranță?", 'Da — SSL și GDPR. Vezi <a href="/ro/privacy-policy.html">Politica de confidențialitate</a>.'),
        ("Cum confirm acum?", '<a href="#order-form">Completează formularul</a> — te sunăm în 1 oră.'),
    ],
    "fblurb": "Produse utile pentru viața de zi cu zi, livrare 24–48h și ramburs.",
    "finfo": "Informaţii", "fcon": "Contact",
    "flinks": [("Despre noi","about-us.html"),("Contactaţi-ne","contact-us.html"),("Politica de confidențialitate","privacy-policy.html"),("Termeni și condiții","terms-conditions.html"),("Politica cookie","cookie-policy.html"),("Politica de livrare","shipping-policy.html"),("Politica de rambursare","refund-policy.html")],
    "rights": "Toate drepturile rezervate.",
    "ty_title": "Comandă primită — Așteaptă apelul | Verdola™",
    "ty_desc": "Comanda Verdola™ a fost înregistrată. Răspunde la apelul de confirmare.",
    "ty_h1": "Comanda ta a fost înregistrată cu succes!",
    "ty_sub": "Comanda ta Verdola™ este în procesare. Mai rămâne <strong>un ultim pas</strong>.",
    "ty_eye": "👇 Ce trebuie să faci acum",
    "ty_at": "📞 Răspunde la apelul de confirmare",
    "ty_ab": "Te contactăm <strong>în următoarele ore</strong> pentru confirmare.",
    "ty_w": "Dacă nu răspunzi, comanda se anulează automat.",
    "ty_hh": "🕒 Program de contact",
    "ty_h": "<strong>Luni – Sâmbătă</strong> · 9:00 – 18:00",
    "ty_nh": "📋 Ce se întâmplă după",
    "ty_s": ["Răspunde și <strong>confirmă datele</strong>", "Expediere în <strong>24–48 ore</strong>", "Livrare și <strong>ramburs</strong>"],
    "ty_b": ("🔒 Ramburs la livrare", "🛡️ Garanție 24 luni", "🔐 Protecție SSL"),
    "ty_alt": "Echipa homeshopspot — call center și ramburs",
}

PACKS["cz"] = {
    "title": "Verdola™ Vyžínač 3000W — Baterie 48V, 1,4 kg | Kompletní sada -50%",
    "desc": "Verdola™: akumulátorový vyžínač 48V 3000W, jen 1,4 kg. Kompletní sada, nabíjení 4–5 hodin. Dobírka, doprava zdarma 24/48h.",
    "og_title": "Verdola™ Vyžínač 3000W 48V — Kompletní sada -50%",
    "og_desc": "3000W, baterie 48V, 1,4 kg. Kompletní sada. Platba na dobírku.",
    "pname": "Verdola™ Akumulátorový vyžínač 48V 3000W",
    "pdesc": "Vyžínač 48V 3000W, 1,4 kg. Kompletní sada s bateriemi, nabíječkou (4–5 h), popruhem a ochranou rostlin.",
    "offer": "Verdola Vyžínač CZ",
    "submit": "Odesílám...",
    "ck_t": "Používáme technické a cookies třetích stran ke zlepšení zážitku a pro analytiku.",
    "ck_a": "Přijmout", "ck_l": "Zjistit více",
    "topbar": "🔥 SEZÓNNÍ NABÍDKA -50% + DOPRAVA ZDARMA — PLATBA NA DOBÍRKU 🔥",
    "rating": "<strong>4,8/5</strong> — Více než <strong>3.842</strong> spokojených zákazníků · <strong>170+</strong> ověřených recenzí",
    "gift": "📦 Kompletní sada v balení · Záruka 24 měsíců · Doprava 24/48h",
    "h1": 'Sečte trávu bez námahy a <span class="hl">bez bolesti zad</span> — 3000W, jen 1,4 kg',
    "lead": "<strong>Verdola™</strong> je ultralehký akumulátorový vyžínač <strong>48V 3000W</strong> — váží jen <strong>1,4 kg</strong> — s <strong>integrovaným popruhem</strong> a <strong>kompletní sadou</strong>. Bez kabelů, benzínu a stresu.",
    "alt": "Verdola™ vyžínač 3000W baterie 48V 1,4 kg",
    "cta": "✓ POTVRDIT OBJEDNÁVKU — {price} →",
    "cta_b": "✓ POTVRDIT OBJEDNÁVKU — {price}",
    "note": "🔒 Bez zálohy · Bez karty · Platíte až při doručení",
    "f1h": "Výkon 3000 W", "f1p": "Seká vysokou trávu i keře",
    "f2h": "Baterie 48 V", "f2p": "Stabilní výkon bez poklesů",
    "f3h": "Jen 1,4 kg", "f3p": "Ultralehký, bez únavy",
    "f4h": "Nabíjení 4–5 h", "f4p": "Připraveno na další práci",
    "cd": "⏰ Nabídka -50% končí za", "lh": "Hod", "lm": "Min", "ls": "Sek",
    "sl": "Dostupnost", "sr": "Zbývá jen 9 kusů za tuto cenu",
    "live": "<strong>{n} lidí</strong> právě prohlíží Verdola",
    "live0": "<strong>42 lidí</strong> právě prohlíží Verdola",
    "fh2": "Vyplňte formulář a dokončete objednávku",
    "fp": "Objednejte dnes a <strong>zítřejší doručení je zdarma.</strong> Operátor zavolá do 1 hodiny.",
    "ln": "Jméno a příjmení*", "pn": "Jméno a příjmení",
    "lp": "Telefon*", "pp": "Telefon",
    "la": "Dodací adresa*", "pa": "Dodací adresa",
    "w1e": "01 — Přesné a rychlé sekání",
    "w1h": "Upravte okraje, záhony a těžká místa za pár minut",
    "w1t": ("Přesnost", "Okraje", "Záhony"),
    "w1p": "Verdola™ zvládne vysokou trávu a nerovné okraje s <strong>vysokou přesností</strong> i v úzkých místech.",
    "w1i": "Ideální podél zdí, plotů a rohů, kam klasická sekačka nedosáhne.",
    "w1a": "Verdola přesné sekání okrajů",
    "w2e": "02 — 3000 W a baterie 48 V",
    "w2h": "Profesionální výkon bez kabelů, benzínu a drahé údržby",
    "w2t": ("3000 W", "48 V", "4–5 h nabíjení"),
    "w2p": "Motor <strong>3000 W</strong> a baterie <strong>48 V</strong> drží výkon. V <strong>kompletní sadě</strong> se nabíjí za <strong>4–5 hodin</strong>.",
    "w2i": "Vysoká tráva i hustá vegetace — stejný výkon od začátku do konce.",
    "w2a": "Verdola 3000W baterie 48V",
    "w3e": "03 — Jen 1,4 kg, ergonomický a bezpečný",
    "w3h": "Ultralehký + nastavitelná hlava + popruh",
    "w3t": ("1,4 kg", "Popruh", "Kompletní sada"),
    "w3p": "Jen <strong>1,4 kg</strong>. <strong>Nastavitelná hlava</strong> a <strong>popruh</strong> šetří záda. Vše v <strong>kompletní sadě</strong>.",
    "w3i": "Integrovaná ochrana rostlin u záhonů.",
    "w3a": "Verdola nastavitelná hlava a popruh",
    "cl": "Srovnání",
    "ch": "Elektrický vyžínač s kabelem vs benzínový vs Verdola™",
    "cc": "Kabel / benzín",
    "rows": [
        ("Výkon", "Omezený", "3000 W — vysoká tráva i keře"),
        ("Hmotnost", "Těžký, bolest zad", "Jen 1,4 kg + popruh"),
        ("Kabely/benzín", "Kabely nebo drahý benzín", "100% baterie 48 V"),
        ("Přesnost", "Špatné v rozích", "Nastavitelná hlava"),
        ("Nabíjení", "Benzín/kabel", "Baterie 48 V — 4–5 h"),
        ("Hluk", "95+ dB", "Tichý — kdykoli"),
        ("Ochrana", "Riziko květin", "Ochrana rostlin v balení"),
        ("Cena", "200–400€ + benzín", "Jen {price} kompletní sada"),
        ("Záruka", "1 rok nebo méně", "24 měsíců + vrácení 30 dní"),
    ],
    "th2": "Tisíce lidí volí Verdola™ — co říkají",
    "teye": "★ 4,8/5 · Ověřený nákup · Autentické recenze",
    "ver": "✔ Ověřený nákup",
    "reviews": [
        ("Martin K. — Praha, Česko", "Konečně zahrada bez bolesti zad!", "S klasickým vyžínačem mě bolela záda. Verdola™ s popruhem je úplně jiná — doporučuji!"),
        ("Petr N. — Brno, Česko", "Velmi výkonná na vysokou trávu", "3000W, 1,4 kg, baterie 48V. Hotovo za polovinu času."),
        ("Jakub S. — Ostrava, Česko", "Snadné použití", "Nastartuje hned. Platba na dobírku bez problémů."),
    ],
    "ke": "Co je v balení",
    "kh": "Kompletní sada — připraveno k použití",
    "ka": "Balení Verdola™ vyžínač",
    "kit": [
        "<strong>1× Verdola™ akumulátorový vyžínač</strong> — 3000 W, 1,4 kg",
        "<strong>2× lithium baterie 48 V</strong>",
        "<strong>1× nabíječka</strong> — 4–5 hodin",
        "<strong>1× cívka s nylonovou strunou</strong>",
        "<strong>1× ochrana rostlin</strong>",
        "<strong>1× ergonomický popruh</strong>",
        "<strong>1× návod</strong> v češtině",
        "<strong>Doprava zdarma</strong> 24/48h",
        "<strong>Platba na dobírku</strong>",
        "<strong>Vrácení zdarma 30 dní</strong>",
        "<strong>Záruka 24 měsíců</strong>",
    ],
    "faqh": "Často kladené otázky",
    "faqs": [
        ("Mohu platit na dobírku bez karty?", "Ano — platíte hotově kurýrovi. Bez zálohy, bez karty."),
        ("Dostanu pomoc s objednávkou?", "Ano — zavoláme do 1 hodiny."),
        ("Jak dlouho trvá nabíjení?", "Baterie <strong>48 V</strong> se nabíjí <strong>4–5 hodin</strong>."),
        ("Zvládne vysokou trávu?", "Ano — <strong>3000 W</strong> a baterie <strong>48 V</strong>."),
        ("Kolik váží?", "Jen <strong>1,4 kg</strong> + popruh."),
        ("Co je v sadě?", "Vyžínač 3000W, 2 baterie 48V, nabíječka, struna, ochrana, popruh, návod."),
        ("Jak vrátit?", "Do 30 dnů, zdarma při perfektním stavu."),
        ("Jak funguje záruka?", "24 měsíců — oprava nebo výměna zdarma."),
        ("Jsou data v bezpečí?", 'Ano — SSL a GDPR. Viz <a href="/cz/privacy-policy.html">Zásady ochrany osobních údajů</a>.'),
        ("Jak objednat teď?", '<a href="#order-form">Vyplňte formulář</a> — zavoláme do 1 hodiny.'),
    ],
    "fblurb": "Užitečné produkty pro každodenní život, doprava 24–48h a dobírka.",
    "finfo": "Informace", "fcon": "Kontakt",
    "flinks": [("O nás","about-us.html"),("Kontaktujte nás","contact-us.html"),("Zásady ochrany osobních údajů","privacy-policy.html"),("Obchodní podmínky","terms-conditions.html"),("Zásady cookies","cookie-policy.html"),("Zásady dopravy","shipping-policy.html"),("Zásady reklamací","refund-policy.html")],
    "rights": "Všechna práva vyhrazena.",
    "ty_title": "Objednávka přijata — Čekejte na hovor | Verdola™",
    "ty_desc": "Objednávka Verdola™ byla zaznamenána. Přijměte potvrzovací hovor.",
    "ty_h1": "Vaše objednávka byla úspěšně zaznamenána!",
    "ty_sub": "Objednávka Verdola™ se zpracovává. Zbývá <strong>poslední krok</strong>.",
    "ty_eye": "👇 Co teď udělat",
    "ty_at": "📞 Přijměte potvrzovací hovor",
    "ty_ab": "Zavoláme vám <strong>v následujících hodinách</strong>.",
    "ty_w": "Pokud neodpovíte, objednávka bude automaticky zrušena.",
    "ty_hh": "🕒 Kontaktní hodiny",
    "ty_h": "<strong>Pondělí – Sobota</strong> · 9:00 – 18:00",
    "ty_nh": "📋 Co bude dál",
    "ty_s": ["Přijměte hovor a <strong>potvrďte údaje</strong>", "Odeslání do <strong>24–48 hodin</strong>", "Doručení a <strong>platba na dobírku</strong>"],
    "ty_b": ("🔒 Platba na dobírku", "🛡️ Záruka 24 měsíců", "🔐 Ochrana SSL"),
    "ty_alt": "Tým homeshopspot — call centrum a dobírka",
}

# Continue with hu, sk, pl, de in same structure — loaded from companion below
exec(Path(__file__).with_name("generate_verdola_packs2.py").read_text(encoding="utf-8"), globals())


def tags(xs):
    return "".join(f'<span class="tag">{x}</span>' for x in xs)


def landing(g, t):
    slug = f"verdola-{g['code']}"
    base = f"https://homeshopspot.com/{g['geo']}/{slug}"
    price, was = g["now"], g["was"]
    cta, ctab = t["cta"].format(price=price), t["cta_b"].format(price=price)
    rows = "\n".join(
        f'    <tr><td>{a}</td><td>{b}</td><td class="win">{c.format(price=price)}</td></tr>'
        for a, b, c in t["rows"]
    )
    revs = ""
    for i, (author, title, quote) in enumerate(t["reviews"], 1):
        revs += f"""      <div class="testimonial">
        <img decoding="async" class="t-photo" src="/assets/img/reviews/verdola/review-{i}.webp" alt="{author}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
        <div class="t-body">
          <div class="stars">★★★★★</div>
          <h4>{title}</h4>
          <p>«{quote}»</p>
          <div class="author-row"><img class="avatar" src="/assets/img/reviews/verdola/pfp-{i}.webp" alt="" loading="lazy" onerror="this.style.display='none'"><div class="author">{author} {t['ver']}</div></div>
        </div>
      </div>
"""
    kit = "\n".join(f"        <li>{x}</li>" for x in t["kit"])
    faqs = "".join(
        f'  <div class="faq-item"><button class="faq-q" type="button"><span>{q}</span><span class="arrow">▾</span></button>\n    <div class="faq-a"><p>{a}</p></div></div>\n'
        for q, a in t["faqs"]
    )
    flinks = "\n".join(f'          <li><a href="/{g["geo"]}/{h}">{lab}</a></li>' for lab, h in t["flinks"])
    footer_first_col = footer_blurb_column_html(
        t["fblurb"], g["lang"], show_ai_notice=True
    )
    return f"""<!DOCTYPE html>
<html lang="{g['lang']}">
<head>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="contact" content="info@homeshopspot.com">
<meta name="theme-color" content="#14181f">
<link rel="canonical" href="{base}/landing.html">
<link rel="alternate" hreflang="{g['lang']}" href="{base}/landing.html">
<link rel="alternate" hreflang="x-default" href="/">
<meta property="og:type" content="product">
<meta property="og:title" content="{t['og_title']}">
<meta property="og:description" content="{t['og_desc']}">
<meta property="og:image" content="https://homeshopspot.com/assets/img/products/verdola/hero.webp">
<meta property="og:url" content="{base}/landing.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/glacierair-landing.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{t['pname']}",
  "image": "https://homeshopspot.com/assets/img/products/verdola/hero.webp",
  "description": "{t['pdesc']}",
  "brand": {{ "@type": "Brand", "name": "Verdola" }},
  "offers": {{
    "@type": "Offer",
    "price": "{g['schema']}",
    "priceCurrency": "{g['currency']}",
    "availability": "https://schema.org/InStock",
    "url": "{base}/landing.html"
  }},
  "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "3842" }}
}}
</script>
<script>
window.SITE_CONFIG = {{
  GEO: '{g['geo']}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{g['currency']}',
  PRICE: {g['price']},
  OFFER_NAME: '{t['offer']}',
  LP_ID: '{g['geo']}-verdola-{g['code']}',
  FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead',
  SUBMITTING_LABEL: '{t['submit']}',
  COOKIE_TEXT: '{t['ck_t']}',
  COOKIE_ACCEPT: '{t['ck_a']}',
  COOKIE_LEARN: '{t['ck_l']}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/form-handler.js" defer></script>
</head>
<body>
<div class="topbar">{t['topbar']}</div>
<div class="rating-strip wrap">
  <div class="stars">★★★★★</div>
  <div class="rating-text">{t['rating']}</div>
</div>
<section class="hero wrap">
  <div class="hero-copy">
    <span class="gift-strip">{t['gift']}</span>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="/assets/img/products/verdola/hero.webp" alt="{t['alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
    </div>
    <div class="price-block">
      <span class="was">{was}</span>
      <span class="now">{price}</span>
      <span class="pct">-50%</span>
    </div>
    <a href="#order-form" class="cta-btn">{cta}</a>
    <p class="form-note">{t['note']}</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="/assets/img/products/verdola/hero.webp" alt="{t['alt']}" width="560" height="560" loading="eager" fetchpriority="high" onerror="this.src='/assets/img/placeholder.svg'">
  </div>
</section>
<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">⚡</div><h4>{t['f1h']}</h4><p>{t['f1p']}</p></div>
    <div class="feature-item"><div class="ico">🔋</div><h4>{t['f2h']}</h4><p>{t['f2p']}</p></div>
    <div class="feature-item"><div class="ico">🪶</div><h4>{t['f3h']}</h4><p>{t['f3p']}</p></div>
    <div class="feature-item"><div class="ico">⏱️</div><h4>{t['f4h']}</h4><p>{t['f4p']}</p></div>
  </div>
</div>
<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="countdown-row">
        <div class="countdown-label">{t['cd']}</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">{t['lh']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">{t['lm']}</div></div>
          <div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">{t['ls']}</div></div>
        </div>
      </div>
      <div class="stock-row">
        <div class="stock-label"><span class="left">{t['sl']}</span><span class="right">{t['sr']}</span></div>
        <div class="stock-bar"><div class="stock-bar-fill"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount" data-live="{t['live']}">{t['live0']}</span>
      </div>
    </div>
    <div class="order-card">
      <h2>{t['fh2']}</h2>
      <p>{t['fp']}</p>
      <form class="tm-order-form order-form cod-form" novalidate>
        <div class="cod-form__field">
          <label for="name">{t['ln']}</label>
          <input class="cod-form__input" id="name" type="text" name="name" autocomplete="name" placeholder="{t['pn']}" required minlength="3">
        </div>
        <div class="cod-form__field">
          <label for="phone">{t['lp']}</label>
          <input class="cod-form__input" id="phone" type="tel" name="phone" autocomplete="tel" placeholder="{t['pp']}" required>
        </div>
        <div class="cod-form__field">
          <label for="address">{t['la']}</label>
          <input class="cod-form__input" id="address" type="text" name="address" autocomplete="street-address" placeholder="{t['pa']}" required minlength="10">
        </div>
        <input name="subid" type="hidden" value="">
        <input name="thankyoupage" type="hidden" value="{base}/thank-you.html">
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">{ctab}</button>
        </div>
        <p class="form-note">{t['note']}</p>
      </form>
    </div>
  </div>
</section>
<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/verdola/feature-1.webp" alt="{t['w1a']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{t['w1e']}</div>
      <h3>{t['w1h']}</h3>
      <div class="tag-row">{tags(t['w1t'])}</div>
      <p>{t['w1p']}</p>
      <p class="italic">{t['w1i']}</p>
    </div>
  </div>
</section>
<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/verdola/feature-2.webp" alt="{t['w2a']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{t['w2e']}</div>
      <h3>{t['w2h']}</h3>
      <div class="tag-row">{tags(t['w2t'])}</div>
      <p>{t['w2p']}</p>
      <p class="italic">{t['w2i']}</p>
    </div>
  </div>
</section>
<section class="why-block wrap" style="border-bottom:none;">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="/assets/img/products/verdola/feature-3.webp" alt="{t['w3a']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'"></div>
    <div>
      <div class="num-eyebrow">{t['w3e']}</div>
      <h3>{t['w3h']}</h3>
      <div class="tag-row">{tags(t['w3t'])}</div>
      <p>{t['w3p']}</p>
      <p class="italic">{t['w3i']}</p>
    </div>
  </div>
</section>
<div class="wrap" style="text-align:center;padding:0 0 32px;">
  <a href="#order-form" class="cta-btn">{cta}</a>
</div>
<section class="compare wrap">
  <div class="section-label">{t['cl']}</div>
  <h2>{t['ch']}</h2>
  <table>
    <tr><th></th><th>{t['cc']}</th><th class="highlight">Verdola™ 3000W</th></tr>
{rows}
  </table>
</section>
<section class="testimonials">
  <div class="wrap">
    <div class="section-heading">
      <h2>{t['th2']}</h2>
      <span class="eyebrow" style="display:block;margin-top:8px;color:#5b6472;font-weight:600;text-transform:none;letter-spacing:0;font-size:14px;">{t['teye']}</span>
    </div>
    <div class="t-grid">
{revs}    </div>
  </div>
</section>
<div class="wrap" style="text-align:center;padding:0 0 32px;">
  <a href="#order-form" class="cta-btn">{cta}</a>
</div>
<section class="kit-section wrap">
  <div class="section-heading">
    <span class="eyebrow">{t['ke']}</span>
    <h2>{t['kh']}</h2>
  </div>
  <div class="kit-box">
    <img decoding="async" src="/assets/img/products/verdola/package.webp" alt="{t['ka']}" loading="lazy" onerror="this.src='/assets/img/placeholder.svg'">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;">
        <span class="was">{was}</span>
        <span class="now">{price}</span>
        <span class="pct">-50%</span>
      </div>
      <ul>
{kit}
      </ul>
      <a href="#order-form" class="cta-btn">{cta}</a>
    </div>
  </div>
</section>
<section class="faq wrap" id="faq">
  <div class="section-heading"><h2>{t['faqh']}</h2></div>
{faqs}</section>
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
{footer_first_col}
      <div>
        <h4 class="site-footer__heading">{t['finfo']}</h4>
        <ul class="site-footer__list">
{flinks}
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">{t['fcon']}</h4>
        <ul class="site-footer__list">
          <li><strong>Northstar Digital Growth LLC</strong></li>
          <li>32 N Gould St.</li>
          <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
          <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — {t['rights']}
      <a href="/">homeshopspot.com</a>
    </div>
  </div>
</footer>
<script src="/assets/js/glacierair-landing.js" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {{
    el.textContent = String(new Date().getFullYear());
  }});
</script>
</body>
</html>
"""


def thankyou(g, t):
    slug = f"verdola-{g['code']}"
    cpa = g["cpa"]
    flinks = "\n".join(f'        <li><a href="/{g["geo"]}/{h}">{lab}</a></li>' for lab, h in t["flinks"])
    ty_ai_notice = ai_image_notice_html(g["lang"])
    return f"""<!DOCTYPE html>
<html lang="{g['lang']}">
<head>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t['ty_title']}</title>
<meta name="description" content="{t['ty_desc']}">
<meta name="contact" content="info@homeshopspot.com">
<meta name="theme-color" content="#16a34a">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
body {{ background: #f8fafc; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-check {{ width: 64px; height: 64px; border-radius: 9999px; background: #fff; border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; margin: 1rem auto 1.5rem; font-size: 2rem; color: var(--color-primary); font-weight: 800; box-shadow: 0 4px 12px -4px rgba(22,163,74,0.25); }}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: 0.875rem; letter-spacing: -0.02em; }}
.ty-subhead {{ text-align: center; color: var(--color-text-muted); font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
@media (min-width: 480px) {{ .ty-headline {{ font-size: 1.875rem; }} }}
.ty-hero {{ border-radius: 0.75rem; overflow: hidden; aspect-ratio: 2848 / 1331; background: var(--color-bg-alt); margin-bottom: 1.5rem; box-shadow: 0 4px 16px -8px rgba(0,0,0,0.15); }}
.ty-hero img {{ width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }}
.ty-action {{ background: #fef9e7; border: 1.5px solid #f5d07a; border-radius: 0.75rem; padding: 1.25rem 1.25rem 1.5rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: 0.7rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #92400e; margin-bottom: 0.625rem; text-align: center; }}
.ty-action__title {{ font-size: 1.25rem; font-weight: 800; text-align: center; margin-bottom: 0.625rem; color: var(--color-text); }}
.ty-action__body {{ text-align: center; color: var(--color-text-muted); font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; }}
.ty-action__warning {{ text-align: center; color: var(--color-urgency); font-weight: 700; font-size: 0.9rem; line-height: 1.45; }}
.ty-box {{ background: #fff; border: 1px solid var(--color-border); border-radius: 0.5rem; margin-bottom: 0.75rem; overflow: hidden; }}
.ty-box__header {{ padding: 0.625rem 1rem; background: #f8fafc; border-bottom: 1px solid var(--color-border); font-size: 0.7rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; color: var(--color-text-muted); }}
.ty-box__body {{ padding: 0.75rem 1rem; font-size: 0.95rem; }}
.ty-hours-line strong {{ font-weight: 700; }}
.ty-steps-list {{ list-style: none; padding: 0; margin: 0; counter-reset: ty-step; }}
.ty-steps-list li {{ display: flex; gap: 0.625rem; padding: 0.625rem 0; border-bottom: 1px solid var(--color-border); font-size: 0.9rem; line-height: 1.45; counter-increment: ty-step; }}
.ty-steps-list li:last-child {{ border-bottom: none; padding-bottom: 0; }}
.ty-steps-list li::before {{ content: counter(ty-step) "."; font-weight: 800; color: var(--color-primary); flex-shrink: 0; min-width: 1.25rem; }}
.ty-trust {{ display: flex; gap: 0.5rem; flex-wrap: wrap; justify-content: center; margin-top: 1.25rem; }}
.ty-trust__badge {{ background: #fff; border: 1px solid var(--color-border); border-radius: 9999px; padding: 0.4rem 0.875rem; font-size: 0.75rem; font-weight: 600; color: var(--color-text-muted); white-space: nowrap; }}
</style>
<script>
window.SITE_CONFIG = {{
  GEO: '{g['geo']}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{g['currency']}',
  PRICE: {g['price']},
  GOOGLE_ADS_CONVERSION_SEND_TO: 'AW-18441580932/gc9ACMvhrvQcEITj0NlE',
  CONVERSION_VALUE: {cpa},
  CONVERSION_CURRENCY: 'EUR',
  COOKIE_TEXT: '{t['ck_t']}',
  COOKIE_ACCEPT: '{t['ck_a']}',
  COOKIE_LEARN: '{t['ck_l']}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
<script src="/assets/js/main.js" defer></script>
</head>
<body>
<header class="site-header">
  <div class="site-header__inner">
    <a href="/" class="site-logo" aria-label="homeshopspot.com home">
      <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
    </a>
  </div>
</header>
<main class="ty-page">
  <div class="ty-check" aria-hidden="true">✓</div>
  <h1 class="ty-headline">{t['ty_h1']}</h1>
  <p class="ty-subhead">{t['ty_sub']}</p>
  <figure class="ty-hero">
    <img src="/assets/img/site/thank_you_draftin.png" alt="{t['ty_alt']}" width="2848" height="1331" loading="lazy" decoding="async">
  </figure>
  <section class="ty-action">
    <div class="ty-action__eyebrow">{t['ty_eye']}</div>
    <h2 class="ty-action__title">{t['ty_at']}</h2>
    <p class="ty-action__body">{t['ty_ab']}</p>
    <p class="ty-action__warning">{t['ty_w']}</p>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{t['ty_hh']}</div>
    <div class="ty-box__body"><div class="ty-hours-line">{t['ty_h']}</div></div>
  </section>
  <section class="ty-box">
    <div class="ty-box__header">{t['ty_nh']}</div>
    <div class="ty-box__body">
      <ol class="ty-steps-list">
        <li>{t['ty_s'][0]}</li>
        <li>{t['ty_s'][1]}</li>
        <li>{t['ty_s'][2]}</li>
      </ol>
    </div>
  </section>
  <div class="ty-trust">
    <span class="ty-trust__badge">{t['ty_b'][0]}</span>
    <span class="ty-trust__badge">{t['ty_b'][1]}</span>
    <span class="ty-trust__badge">{t['ty_b'][2]}</span>
  </div>
</main>
<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div><a href="/" class="site-logo"><span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span></a></div>
    <div>
      <h4 class="site-footer__heading">{t['finfo']}</h4>
      <ul class="site-footer__list">
{flinks}
      </ul>
    </div>
    <div>
      <h4 class="site-footer__heading">{t['fcon']}</h4>
      <ul class="site-footer__list">
        <li><strong>Northstar Digital Growth LLC</strong></li>
        <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
        <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
      </ul>
    </div>
  </div>
  {ty_ai_notice}
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — {t['rights']} <a href="/">homeshopspot.com</a></div>
</div></footer>
<!-- Meta Pixel Purchase event -->
<script>
  (function () {{
    if (!window.fbq) return;
    var p = new URLSearchParams(window.location.search);
    fbq('track', 'Purchase', {{
      value: {{cpa}},
      currency: 'USD',
      order_id: p.get('order_id') || p.get('transaction_id') || p.get('tid') || ''
    }});
  }})();
</script>
</body>
</html>
"""


def index(g):
    slug = f"verdola-{g['code']}"
    path = f"/{g['geo']}/{slug}/landing.html"
    return f"""<!DOCTYPE html>
<html lang="{g['lang']}">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '{path}';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url={path}">
<link rel="canonical" href="https://homeshopspot.com{path}">
</head>
<body>
<p><a href="{path}">Verdola™</a></p>
</body>
</html>
"""


def main():
    for g in GEOS:
        t = PACKS[g["geo"]]
        out = ROOT / g["geo"] / f"verdola-{g['code']}"
        out.mkdir(parents=True, exist_ok=True)
        (out / "landing.html").write_text(landing(g, t), encoding="utf-8")
        (out / "thank-you.html").write_text(thankyou(g, t), encoding="utf-8")
        (out / "index.html").write_text(index(g), encoding="utf-8")
        print("OK", out)


if __name__ == "__main__":
    main()
