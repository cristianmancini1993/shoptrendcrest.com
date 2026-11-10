#!/usr/bin/env python3
"""Update Elementor JSON template HTML with Topper copy."""
import json
from pathlib import Path

JSON_PATH = Path(r"c:\Users\BohVy\Desktop\WORK\Templates\TEMPLATE 4 BENEFITS.json")

REPLACEMENTS = [
    # head title (visible in browser tab)
    (
        "TreeMax\u2122 \u2014 Motosega Telescopica Elettrica, Taglia Fino a 35 cm Senza Benzina",
        "Topper ortopedico in memory foam 3cm con gel termoregolante | Pagamento alla consegna",
    ),
    # rating
    (
        '<div class="rating-text"><strong>4,9/5</strong> \u2014 Oltre <strong>9.480</strong> giardini gi\u00e0 domati</div>',
        '<div class="rating-text"><strong>4,9/5</strong> \u2014 Oltre <strong>[N] persone</strong> dormono meglio ogni notte</div>',
    ),
    # hero
    (
        'Spedizione gratuita + Garanzia 2 anni inclusa',
        'Spedizione gratuita + Garanzia [N] anni inclusa',
    ),
    (
        '<h1 class="h1-mobile-only">Pota rami fino a 5 metri di altezza senza usare una scala e taglia rami e tronchi fino a 35 cm di diametro.</h1>',
        '<h1 class="h1-mobile-only">Il 93% nota meno dolore articolare gi\u00e0 dopo 15 notti.</h1>',
    ),
    (
        '<h1 class="h1-desktop-only">Pota rami fino a 5 metri di altezza senza usare una scala e taglia rami e tronchi fino a 35 cm di diametro.\n</h1>',
        '<h1 class="h1-desktop-only">Il 93% nota meno dolore articolare gi\u00e0 dopo 15 notti.\n</h1>',
    ),
    (
        '<p class="lead">Progettata per lavori in giardino, frutteto e intorno alla casa. Si trasforma rapidamente da mini motosega manuale a motosega telescopica, ideale per tagliare rami alti, lunghi e spessi.</p>',
        '<p class="lead">Non \u00e8 un materasso nuovo. \u00c8 3 cm di memory foam ortopedico che si adatta al tuo corpo, scarica la pressione da schiena, spalle e fianchi, e trasforma un materasso vecchio o troppo rigido in una superficie che finalmente ti lascia dormire.</p>',
    ),
    # features
    (
        '<h4>Garanzia 2 anni</h4>',
        '<h4>Garanzia [N] anni</h4>',
    ),
    # urgency
    (
        '<span class="right">Solo 4 pezzi rimasti</span>',
        '<span class="right">Solo [N] pezzi rimasti</span>',
    ),
    (
        '<span id="liveCount"><strong>38 persone</strong> stanno guardando TreeMax\u2122 ora</span>',
        '<span id="liveCount"><strong>[N] persone</strong> stanno guardando questo topper ora</span>',
    ),
    # order form
    (
        '<h2>Blocca il tuo TreeMax\u2122 a 49\u20ac</h2>',
        '<h2>Blocca il tuo Topper a 49\u20ac</h2>',
    ),
    (
        '<p>Compila i 3 campi qui sotto. Ti chiamiamo entro 24h per confermare la consegna \u2014 nessun addebito prima.</p>',
        '<p>Compila i campi qui sotto. Ti chiamiamo entro 24h per confermare la consegna \u2014 nessun addebito prima.</p>',
    ),
    (
        'S\u00cc, ORDINO TREEMAX\u2122',
        'S\u00cc, ORDINO IL TOPPER',
    ),
    # why 01
    (
        '<div class="num-eyebrow">01 \u2014 Potenza vera, non un giocattolo da giardino</div>\n        <h3>Motore da 3000W e asta telescopica da 5 metri: tagli tronchi a terra e rami in alto senza scala</h3>\n        <div class="tag-row"><span class="tag">Taglio 35 cm</span><span class="tag">3000W</span><span class="tag">Asta 5 metri</span></div>\n        <p>Un decespugliatore si arrende sui rami spessi. TreeMax\u2122 no: la lama rivestita in titanio taglia tronchi e rami fino a 35 cm di diametro, legno verde o secco, senza fatica. In 2 secondi passi dalla modalit\u00e0 impugnatura, per il lavoro vicino a terra, alla modalit\u00e0 asta telescopica, per potare in alto senza salire su nulla.</p>\n        <p class="italic">Rami del melo troppo alti, tronco caduto dopo il temporale, legna da spaccare per l\'inverno: TreeMax\u2122 li taglia tutti, nello stesso pomeriggio.</p>',
        '<div class="num-eyebrow">01 \u2014 Non un topper qualunque: sollievo vero, misurato</div>\n        <h3>3 cm di memory foam ortopedico: il 93% degli utenti nota meno dolore gi\u00e0 dopo 15 notti</h3>\n        <div class="tag-row"><span class="tag">Memory foam 3cm</span><span class="tag">Sollievo articolare</span><span class="tag">Risultati in 15 notti</span></div>\n        <p>Un materasso troppo rigido scarica tutto il peso su spalle e fianchi: ti giri, ti risvegli, ti alzi indolenzito. Il memory foam di questo topper si modella sul tuo corpo e distribuisce la pressione in modo uniforme, invece di concentrarla nei punti che fanno pi\u00f9 male.</p>\n        <p class="italic">Non \u00e8 una promessa vaga: nei nostri test interni, 93 persone su 100 hanno riferito meno dolore a schiena, spalle e fianchi entro due settimane d\'uso.</p>',
    ),
    # why 02
    (
        '<div class="num-eyebrow">02 \u2014 Zero benzina, zero cavo, zero scuse</div>\n        <h3>Due batterie 48V 8000mAh: lavori tutto il giardino senza fermarti mai</h3>\n        <div class="tag-row"><span class="tag">48V 8000mAh</span><span class="tag">Ricarica in 45 min</span><span class="tag">Nessun cavo</span></div>\n        <p>Niente serbatoio, niente miscela, niente prolunghe che ti si attorcigliano tra i piedi. TreeMax\u2122 arriva con 2 batterie da 48V 8000mAh: quando una finisce, monti l\'altra e continui a tagliare mentre la prima si ricarica in circa 45 minuti.</p>\n        <p class="italic">Ti muovi da un capo all\'altro del giardino senza cercare una presa: l\'unico limite \u00e8 quanto vuoi tagliare oggi.</p>',
        '<div class="num-eyebrow">02 \u2014 Fresco d\'estate, caldo d\'inverno, sempre lo stesso comfort</div>\n        <h3>Gel termoregolante integrato: la temperatura giusta in ogni stagione</h3>\n        <div class="tag-row"><span class="tag">Gel termoregolante</span><span class="tag">Comfort tutto l\'anno</span><span class="tag">Nessuna svolta a met\u00e0 notte</span></div>\n        <p>Il memory foam tradizionale trattiene calore e ti fa svegliare accaldato in estate. Il gel termoregolante integrato in questo topper disperde il calore in eccesso quando fa caldo e mantiene il tepore quando le temperature scendono.</p>\n        <p class="italic">Il risultato: la stessa qualit\u00e0 del sonno a gennaio come a luglio, senza girare il cuscino o buttare via le coperte a met\u00e0 notte.</p>',
    ),
    # why 03 - remove CTA from block 03
    (
        '<div class="num-eyebrow">03 \u2014 Leggera, precisa, sicura anche nei punti stretti</div>\n        <h3>700 g di peso: la usi con una mano sola, senza stancarti</h3>\n        <div class="tag-row"><span class="tag">700 g</span><span class="tag">Uso monomano</span><span class="tag">Freno lama rapido</span></div>\n        <p>Una motosega a benzina da 4-5 kg dopo dieci minuti ti brucia le braccia. TreeMax\u2122 pesa 700 g: la controlli con una mano sola, tagli con precisione anche negli angoli stretti, e la protezione contro l\'avviamento accidentale pi\u00f9 il freno lama rapido ti coprono le spalle a ogni taglio.</p>\n        <p class="italic">La usi tu, la usa tua moglie, la usa anche chi non ha mai preso in mano una motosega prima: nessuno si spaventa.</p>\n\n        <!-- CTA aggiunta 1 \u2014 dopo il testo del beneficio 03 -->\n        <a href="#order-form" class="cta-btn cta-inline">S\u00cc, VOGLIO TREEMAX\u2122 \u2192</a>',
        '<div class="num-eyebrow">03 \u2014 Igiene garantita, notte dopo notte</div>\n        <h3>Fodera sfoderabile e lavabile in lavatrice, fissata con 4 bande elastiche resistenti</h3>\n        <div class="tag-row"><span class="tag">Fodera lavabile</span><span class="tag">4 bande elastiche</span><span class="tag">Anti-acaro</span></div>\n        <p>Le 4 bande elastiche tengono il topper ancorato al materasso: non scivola, non si sposta durante la notte. La fodera si sfila in pochi secondi e va in lavatrice come qualsiasi lenzuolo, mantenendo il letto fresco e pulito.</p>\n        <p class="italic">Trattata contro acari e batteri: ideale anche per chi soffre di allergie o ha la pelle sensibile.</p>',
    ),
    # why 04 + add CTA
    (
        '<div class="num-eyebrow">04 \u2014 Lubrificazione e tensione automatiche, zero manutenzione continua</div>\n        <h3>Tecnologia AutoChain X\u2122: lubrifica e tende la catena da sola, mentre tu tagli</h3>\n        <div class="tag-row"><span class="tag">AutoChain X\u2122</span><span class="tag">Taglio stabile</span><span class="tag">Meno regolazioni</span></div>\n        <p>Con una motosega tradizionale ti fermi ogni dieci minuti a controllare tensione e olio. AutoChain X\u2122 ci pensa da sola: lubrificazione continua e tensione automatica della catena, per un taglio stabile senza interruzioni continue per regolare a mano.</p>\n        <p class="italic">Meno fermate, pi\u00f9 tagli fatti. Il pomeriggio che dedichi al giardino torna a essere tuo.</p>\n      </div>',
        '<div class="num-eyebrow">04 \u2014 Funziona ovunque dormi, anche sul divano letto</div>\n        <h3>Rinnova il tuo materasso \u2014 o il divano letto \u2014 senza comprarne uno nuovo</h3>\n        <div class="tag-row"><span class="tag">Compatibile divano letto</span><span class="tag">Si piega per riporlo</span><span class="tag">Prolunga la vita del materasso</span></div>\n        <p>Il tuo materasso \u00e8 vecchio o troppo duro? Questo topper lo trasforma in una superficie pi\u00f9 morbida e accogliente, ne allunga la vita utile e ti risparmia il costo di uno nuovo.</p>\n        <p class="italic">Funziona altrettanto bene su un divano letto: d\u00e0 spessore, stabilit\u00e0 e la sensazione di un vero materasso, e si piega facilmente per essere riposto quando non serve.</p>\n        <a href="#order-form" class="cta-btn cta-inline">S\u00cc, VOGLIO IL MIO TOPPER \u2192</a>\n      </div>',
    ),
    # compare
    (
        '<h2>Motosega tradizionale vs TreeMax\u2122</h2>\n    <table>\n      <tr><th></th><th>Tradizionale</th><th class="highlight">TreeMax\u2122</th></tr>\n      <tr><td>Alimentazione</td><td>Benzina, rumore, fumi di scarico</td><td class="win">Batteria, silenziosa, zero fumi</td></tr>\n      <tr><td>Peso</td><td>4-5 kg, braccia a fuoco in pochi minuti</td><td class="win">700 g, una mano sola</td></tr>\n      <tr><td>Rami in alto</td><td>Serve la scala</td><td class="win">Asta telescopica da 5 metri</td></tr>\n      <tr><td>Manutenzione catena</td><td>Olio e tensione da regolare a mano</td><td class="win">AutoChain X\u2122 automatica</td></tr>\n      <tr><td>Autonomia</td><td>Serbatoio da riempire ogni volta</td><td class="win">2 batterie 48V, ricarica 45 min</td></tr>\n      <tr><td>Sicurezza</td><td>Rischio avviamento accidentale</td><td class="win">Protezione anti-avviamento + freno rapido</td></tr>\n    </table>',
        '<h2>Materasso normale vs Topper</h2>\n    <table>\n      <tr><th></th><th>Senza Topper</th><th class="highlight">Con Topper</th></tr>\n      <tr><td>Dolore articolare</td><td>Pressione concentrata su schiena, spalle, fianchi</td><td class="win">Memory foam distribuisce il peso, meno pressione</td></tr>\n      <tr><td>Temperatura</td><td>Caldo in estate, freddo in inverno</td><td class="win">Gel termoregolante, comfort tutto l\'anno</td></tr>\n      <tr><td>Igiene</td><td>Difficile da pulire in profondit\u00e0</td><td class="win">Fodera sfoderabile e lavabile in lavatrice</td></tr>\n      <tr><td>Durata materasso</td><td>Si consuma e va sostituito</td><td class="win">Protegge e allunga la vita del materasso</td></tr>\n      <tr><td>Divano letto</td><td>Scomodo, sottile</td><td class="win">Stesso comfort di un vero materasso</td></tr>\n    </table>',
    ),
    # testimonials heading
    (
        '<h2>Oltre 9.480 giardini gi\u00e0 domati. Ecco perch\u00e9 scelgono TreeMax\u2122.</h2>',
        '<h2>Oltre [N] persone dormono meglio. Ecco perch\u00e9 hanno scelto questo Topper.</h2>',
    ),
    # review 1 text only
    (
        '<h4>La lama \u00e8 velocissima, taglia anche il legno pi\u00f9 duro senza sforzo.</h4>\n            <p>\u00abSono rimasto colpito dalla velocit\u00e0 e dalla precisione del taglio. La consiglio senza riserve a chiunque abbia un giardino con alberi da potare.\u00bb',
        '<h4>Dopo due settimane il dolore alla schiena \u00e8 quasi sparito.</h4>\n            <p>\u00abAvevo il materasso troppo rigido da anni e mi svegliavo sempre indolenzita. Con il topper il cambiamento si \u00e8 sentito gi\u00e0 dopo pochi giorni.\u00bb',
    ),
    # review 2 text only
    (
        '<h4>Qualit\u00e0 eccellente, massiccia e ben costruita.</h4>\n            <p>\u00abLa uso regolarmente per tagliare la legna da ardere e non ha mai avuto un problema. Fa esattamente quello che promette.\u00bb',
        '<h4>Qualit\u00e0 ottima, si sente subito la differenza.</h4>\n            <p>\u00abLo uso ogni notte da un mese, il tessuto \u00e8 morbido e la fodera si lava facilmente. Fa esattamente quello che promette.\u00bb',
    ),
    # review 3 text only
    (
        '<h4>L\'ho presa per mio marito, ed \u00e8 entusiasta.</h4>\n            <p>\u00abApprezza soprattutto il fatto di raggiungere i rami alti senza scala. Rende il lavoro in giardino molto pi\u00f9 pratico e sicuro.\u00bb',
        '<h4>L\'ho preso per il divano letto degli ospiti, ora sembra un vero letto.</h4>\n            <p>\u00abNon pensavo facesse cos\u00ec tanta differenza su un divano letto. Ora i miei ospiti dormono comodi come a casa loro.\u00bb',
    ),
    # kit
    (
        '<h2>Kit completo TreeMax\u2122, pronto da caricare e usare</h2>',
        '<h2>Kit completo Topper, pronto da stendere e usare</h2>',
    ),
    (
        '<li>Motosega elettrica 2 in 1 TreeMax\u2122 \u2014 impugnatura + asta telescopica 5 m</li>\n          <li>2\u00d7 Batteria 48V 8000mAh \u2014 massima autonomia senza cavo</li>\n          <li>1\u00d7 Caricabatteria rapido \u2014 pronta in circa 45 minuti</li>\n          <li>2\u00d7 Catene di ricambio \u2014 sempre pronto a tagliare</li>\n          <li>1\u00d7 Serbatoio olio + tecnologia AutoChain X\u2122 \u2014 lubrificazione automatica</li>\n          <li>1\u00d7 Kit di regolazione + valigetta da trasporto rigida</li>\n          <li>Garanzia ufficiale di 2 anni</li>',
        '<li>1\u00d7 Topper ortopedico in memory foam 3 cm con gel termoregolante</li>\n          <li>1\u00d7 Fodera sfoderabile e lavabile in lavatrice</li>\n          <li>4\u00d7 Bande elastiche di fissaggio</li>\n          <li>Disponibile in 3 misure: 140x200 \u00b7 160x200 \u00b7 180x200</li>\n          <li>Garanzia ufficiale di [N] anni</li>',
    ),
    # FAQ block replace
    (
        '<div class="faq-item"><button class="faq-q"><span>Devo pagare in anticipo?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>No. Paghi in contanti direttamente al corriere quando TreeMax\u2122 \u00e8 gi\u00e0 a casa tua. Tieni pronti 49\u20ac.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Serve la benzina o va tenuta sotto carica sempre?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>No benzina, nessun cavo fisso. Funziona con 2 batterie da 48V incluse nella confezione: quando una finisce, monti l\'altra.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Posso raggiungere i rami alti senza scala?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>S\u00ec. L\'asta telescopica estraibile fino a 5 metri \u00e8 pensata proprio per questo: potatura in altezza senza salire su nulla.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>E se non mi convince?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>Hai 30 giorni per restituirla gratuitamente e ricevere il rimborso completo, senza domande.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Ok, sono convinto. Come la ordino?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>Compila il modulo qui sopra con nome, telefono e indirizzo. Ti chiamiamo entro 24h per confermare, e TreeMax\u2122 arriva a casa tua in 1-2 giorni. Paghi solo alla consegna.</p></div></div>',
        '<div class="faq-item"><button class="faq-q"><span>Devo pagare in anticipo?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>No. Paghi in contanti direttamente al corriere quando il topper \u00e8 gi\u00e0 a casa tua.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Va bene su qualsiasi materasso?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>S\u00ec. Le 4 bande elastiche si adattano alla maggior parte dei materassi standard nelle misure disponibili.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Come si lava?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>La fodera \u00e8 completamente sfoderabile e si lava in lavatrice. Il topper in memory foam non va lavato in acqua, basta arieggiarlo.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>\u00c8 adatto anche a chi ha allergie?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>S\u00ec, la fodera \u00e8 trattata contro acari e batteri, indicata anche per pelli sensibili.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>E se non mi convince?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>Hai 30 giorni per restituirlo gratuitamente e ricevere il rimborso completo, senza domande.</p></div></div>\n    <div class="faq-item"><button class="faq-q"><span>Ok, sono convinto. Come lo ordino?</span><span class="arrow">\u25be</span></button>\n      <div class="faq-a"><p>Compila il modulo qui sopra con nome, telefono, indirizzo e misura scelta. Ti chiamiamo entro 24h per confermare, e il topper arriva a casa tua in 1-2 giorni. Paghi solo alla consegna.</p></div></div>',
    ),
]


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    html = data["content"][0]["elements"][0]["settings"]["html"]

    for old, new in REPLACEMENTS:
        if old not in html:
            raise SystemExit(f"MISSING expected fragment ({len(old)} chars):\n{old[:200]!r}...")
        html = html.replace(old, new, 1)

    html = html.replace('S\u00cc, VOGLIO TREEMAX\u2122 \u2192', 'S\u00cc, VOGLIO IL MIO TOPPER \u2192')
    html = html.replace('Paghi solo quando la ricevi', 'Paghi solo quando lo ricevi')

    data["content"][0]["elements"][0]["settings"]["html"] = html

    # validate round-trip
    out = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    json.loads(out)  # must parse

    JSON_PATH.write_text(out, encoding="utf-8")
    print(f"OK: updated {JSON_PATH}")
    print(f"HTML length: {len(html)} chars")


if __name__ == "__main__":
    main()
