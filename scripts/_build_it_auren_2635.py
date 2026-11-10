#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build IT AUREN #2635 landing from devicegridbay embera template (rephrased copy)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts/_tmp_embera_source.html"
OUT_DIR = ROOT / "it/italy"
BASE = "https://gadgetshifthub.com/it/italy"

FORM_UID = "019fd3ba-5142-7ab3-b965-8163a326c7f9"
FORM_WEBHOOK = "https://hook.eu2.make.com/lynkdu9dee6imynkym5wtses9339q95h"
FORM_KEY = "a8f3f892387f175bf6e35938d46afdb47069fd18"
TY = f"{BASE}/thank-you.html"

FOOTER = """<footer class="site-footer"><div class="container">
<div class="site-footer__top"><p class="site-footer__powered">gadgetshifthub.com — Gestito da <strong>Netmart LLC</strong></p></div><div class="site-footer__grid">
<div>
<a aria-label="gadgetshifthub.com home" class="site-logo" href="/"><span class="site-logo__text"><span class="site-logo__text-primary">gadgetshifthub</span><span class="site-logo__text-accent">.com</span></span></a>
<p class="site-footer__blurb">Soluzioni per la casa, spedizione veloce e pagamento in contrassegno.</p>
</div>
<div>
<h4 class="site-footer__heading">Informazioni</h4>
<ul class="site-footer__list">
<li><a href="/it/about-us.html">Chi siamo</a></li>
<li><a href="/it/contact-us.html">Contattaci</a></li>
<li><a href="/it/privacy-policy.html">Informativa sulla privacy</a></li>
<li><a href="/it/terms-conditions.html">Termini e condizioni</a></li>
<li><a href="/it/cookie-policy.html">Politica sui cookie</a></li>
<li><a href="/it/shipping-policy.html">Politica di spedizione</a></li>
<li><a href="/it/refund-policy.html">Politica di reso</a></li>
</ul>
</div>
<div>
<h4 class="site-footer__heading">Contatti</h4>
<ul class="site-footer__list">
<li><a href="mailto:info@gadgetshifthub.com">info@gadgetshifthub.com</a></li>
</ul>
</div>
</div>
<div class="site-footer__entity"><p class="site-footer__entity-name"><strong>Netmart LLC</strong></p><p class="site-footer__entity-address">County of Sussex 16192 Coastal Hwy<br/>Lewes, DE 19958-3608, Stati Uniti</p></div><div class="site-footer__bottom">© <span data-year="">2026</span> gadgetshifthub.com — Gestito da <strong>Netmart LLC</strong></div>
</div></footer>"""

COPY_REPLACEMENTS = [
    (
        "EMBERA™ — Camino elettrico LED 3D, fino a 80 m² | -50 % | Italia",
        "AUREN™ — Camino elettrico LED 3D, fino a 80 m² | -50% | Italia",
    ),
    (
        'content="EMBERA™: camino elettrico con fiamma LED 3D regolabile, calore in pochi minuti fino a 80 m². App, telecomando e pulsanti. Senza installazione. Spedizione 24–48 h lavorative dopo conferma telefonica e pagamento alla consegna a 96 €."',
        'content="AUREN™: caminetto elettrico con effetto fiamma LED 3D, calore rapido fino a 80 m². App, telecomando e comandi sul pannello. Nessuna installazione. Spedizione 24–48 h dopo conferma telefonica e contrassegno a 96 €."',
    ),
    (
        'content="EMBERA™ — Camino elettrico LED 3D | -50 %"',
        'content="AUREN™ — Camino elettrico LED 3D | -50%"',
    ),
    (
        'content="Calore in pochi minuti, atmosfera camino e controllo dal telefono. 96 € in contrassegno."',
        'content="Riscaldamento veloce, effetto camino e gestione da smartphone. 96 € in contrassegno."',
    ),
    (
        "<strong>4,8/5</strong> — Più di <strong>8.700</strong> persone hanno già scelto il camino elettrico per il soggiorno",
        "<strong>4,8/5</strong> — Oltre <strong>8.700</strong> clienti hanno già scelto un camino elettrico per il living",
    ),
    (
        "🎁 OMAGGIO INCLUSO: TELECOMANDO + APP PER GESTIRE IL CAMINO DAL TELEFONO",
        "🎁 INCLUSI: TELECOMANDO + APP PER COMANDARE AUREN™ DALLO SMARTPHONE",
    ),
    (
        '<h1 class="h1-mobile-only"><span class="hl">Il soggiorno accogliente che ti mancava</span> — calore rapido senza caldaia né lavori.</h1>',
        '<h1 class="h1-mobile-only"><span class="hl">Living più caldo e accogliente</span> — calore veloce senza caldaia né cantieri.</h1>',
    ),
    (
        '<h1 class="h1-desktop-only">Atmosfera camino e <span class="hl">calore uniforme in casa</span> — basta una presa elettrica.</h1>',
        '<h1 class="h1-desktop-only">Effetto camino e <span class="hl">calore omogeneo</span> — ti basta una presa a muro.</h1>',
    ),
    (
        "<strong>EMBERA™:</strong> il calore e l'atmosfera di un vero fuoco senza spendere migliaia di euro per una stufa a pellet. Niente installazione e niente combustibile da ricomprare ogni volta: lo togli dalla scatola, lo colleghi alla presa e in un minuto scalda già tutta la zona giorno.",
        "<strong>AUREN™</strong> unisce l'atmosfera di un fuoco autentico al comfort elettrico, senza investire migliaia di euro in pellet o opere murarie. Nessun tecnico, nessun combustibile da rifornire: estrai dal carton, inserisci la spina e in pochi istanti la zona living è più accogliente.",
    ),
    ("<h4>Fino a 80 m²</h4><p>Calore percepibile in minuti, senza lunghe attese</p>", "<h4>Calore fino a 80 m²</h4><p>Sensazione di caldo in pochi minuti, senza attese lunghe</p>"),
    ("<h4>Zero installazione</h4><p>Collega alla presa e inizia subito</p>", "<h4>Plug & play</h4><p>Collega e usa subito, senza tecnico</p>"),
    ("<h4>App · WiFi · telecomando</h4><p>Accendi il calore prima di tornare a casa</p>", "<h4>App · WiFi · telecomando</h4><p>Imposta temperatura e timer da remoto</p>"),
    ("<h4>Protezione termica</h4><p>Spegnimento automatico in caso di surriscaldamento</p>", "<h4>Sicurezza integrata</h4><p>Auto spegnimento anti surriscaldamento</p>"),
    (
        "⏰ Lo sconto del 50 % termina quando finiscono le unità in promozione",
        "⏰ Lo sconto del 50% vale fino a esaurimento scorte promozionali",
    ),
    ("<span class=\"right\">Ultime 3 unità a prezzo promo</span>", "<span class=\"right\">Restano 3 pezzi a prezzo promo</span>"),
    (
        'data-live="<strong>{n} persone</strong> stanno guardando questa offerta ora"',
        'data-live="<strong>{n} persone</strong> stanno valutando questa promo ora"',
    ),
    ("stanno guardando questa offerta ora", "stanno valutando questa promo ora"),
    ("<h2>Completa l'ordine — EMBERA™ a 96 €</h2>", "<h2>Invia la richiesta — AUREN™ a 96 €</h2>"),
    (
        "<p>Inserisci nome, telefono e indirizzo: ti richiamiamo per confermare la spedizione, senza addebiti anticipati.</p>",
        "<p>Compila nome, telefono e indirizzo: ti contattiamo per confermare la consegna, zero pagamenti anticipati.</p>",
    ),
    ("<h3>Calore in pochi minuti, fino a 80 m²</h3>", "<h3>Calore percepibile in pochi minuti, superficie fino a 80 m²</h3>"),
    (
        "I termosifoni possono richiedere <strong>1–2 ore</strong>. <strong>EMBERA™</strong> offre calore tangibile in <strong>pochi minuti</strong> su <strong>fino a 80 m²</strong>, senza perdite nella rete di riscaldamento.",
        "I radiatori spesso impiegano <strong>1–2 ore</strong>. <strong>AUREN™</strong> riscalda in <strong>pochi minuti</strong> su <strong>fino a 80 m²</strong>, senza dispersioni della rete idraulica.",
    ),
    (
        "Dagli appartamenti alle case con riscaldamento insufficiente: un solo dispositivo compatto per più comfort.",
        "Appartamento o casa mal isolata: un unico elemento compatto per più benessere.",
    ),
    ("<h3>Collega e usa — senza installatore</h3>", "<h3>Presa e via — nessun installatore</h3>"),
    (
        "Niente caldaia, tubature o condotto: <strong>tiralo fuori dalla scatola e collegalo</strong>. Posizionalo dove serve e goditi il calore.",
        "Senza caldaia, tubi o canna fumaria: <strong>apri, collega e accendi</strong>. Spostalo dove ti serve.",
    ),
    (
        "Con <strong>EMBERA™</strong> riduci i costi del gas e dell'installazione, con l'atmosfera di un camino in casa.",
        "Con <strong>AUREN™</strong> alleggerisci spese di gas e montaggio, con l'effetto camino in salotto.",
    ),
    ("<h3>Potenza reale, fiamma LED 3D premium</h3>", "<h3>2000 W reali, fiamma LED 3D di fascia alta</h3>"),
    (
        "Fino a <strong>2000 W</strong> per ambienti ampi in sicurezza. <strong>Fiamma LED 3D</strong> regolabile anche senza calore — zero fumo, cenere o legna. Regola temperatura, modalità e timer da app o telecomando.",
        "Potenza fino a <strong>2000 W</strong> per grandi ambienti in sicurezza. <strong>Fiamma LED 3D</strong> anche senza riscaldamento — zero fumo, cenere o scorta di legna. Timer, modalità e temperatura da app o telecomando IR.",
    ),
    (
        "Fiamma e riscaldamento sono indipendenti: atmosfera tutto l'anno.",
        "Effetto fiamma e calore separati: atmosfera camino tutto l'anno.",
    ),
    ("Perché EMBERA™ batte termosifoni e pellet", "Perché AUREN™ ha senso rispetto a caldaia e pellet"),
    ("<h2>Caldaia / termosifoni vs EMBERA™</h2>", "<h2>Centralina e radiatori vs AUREN™</h2>"),
    ("<th class=\"highlight\">EMBERA™</th>", "<th class=\"highlight\">AUREN™</th>"),
    ("<th>Caldaia e termosifoni</th>", "<th>Centralina e radiatori</th>"),
    ('aria-label="Confronto riscaldamento tradizionale e camino elettrico EMBERA"', 'aria-label="Confronto riscaldamento tradizionale e camino elettrico AUREN"'),
    ("<h2>Migliaia di famiglie si affidano a EMBERA™. Ecco cosa dicono:</h2>", "<h2>Decine di famiglie hanno scelto AUREN™. Le loro impressioni:</h2>"),
    ("<h4>Kit completo, nulla manca</h4>", "<h4>Confezione completa, tutto a posto</h4>"),
    (
        "«Ho aperto la scatola e c'era tutto: camino, telecomando e manuale in italiano. In un minuto era pronto; ho pagato solo al corriere, senza anticipi. A 96 € il kit completo è un affare che non mi volevo far scappare.»",
        "«Ho scartato il pacco e dentro c'erano camino, telecomando e istruzioni in italiano. In un minuto era operativo; ho saldato solo al corriere, zero anticipi. A 96 € il set completo è un'occasione che non volevo lasciarmi sfuggire.»",
    ),
    ("<h4>Senza preventivo da migliaia di euro</h4>", "<h4>Niente preventivi a cinque cifre</h4>"),
    (
        "«Il pellet e un camino vero mi sembravano fuori budget. EMBERA scalda tutta la zona giorno a un prezzo onesto; la accendo dall'app prima di tornare dal lavoro. Niente preventivi da migliaia di euro — l'ho presa subito perché conviene.»",
        "«Pellet e camino tradizionale erano fuori budget. AUREN™ riscalda tutta la zona living a un prezzo accessibile; lo accendo dall'app prima di rientrare. Niente preventivi da migliaia di euro — l'ho ordinato subito perché tornava.»",
    ),
    ("<h4>Bolletta del gas più leggera</h4>", "<h4>Meno gas in bolletta</h4>"),
    (
        "«Ho 85 m² e i termosifoni ci mettevano un'eternità — la bolletta del gas pesava troppo. Con l'offerta a 96 € invece di 192 €, EMBERA scalda in pochi minuti e la fiamma è stupenda. Ho pagato al corriere, a casa in due giorni: per me conviene davvero.»",
        "«85 m² e radiatori lentissimi — il gas pesava troppo in bolletta. Con 96 € invece di 192 €, AUREN™ scalda in pochi minuti e l'effetto fiamma è bellissimo. Pagato al corriere, consegnato in due giorni: per me è stata una scelta azzeccata.»",
    ),
    ("<h2>📦 Kit completo EMBERA™ — pronto da accendere</h2>", "<h2>📦 Set completo AUREN™ — accendi al primo utilizzo</h2>"),
    ("<span class=\"eyebrow\">Cosa include l'offerta</span>", "<span class=\"eyebrow\">Nel pacco</span>"),
    ("<strong>1× EMBERA™</strong> camino elettrico 2000 W, classe energetica A+++", "<strong>1× AUREN™</strong> camino elettrico 2000 W, classe energetica A+++"),
    ("Telecomando IR incluso — fiamma e calore dal divano", "Telecomando IR in dotazione — fiamma e calore comodamente dal divano"),
    ("App e WiFi — controllo dallo smartphone", "App con WiFi — comandi dallo smartphone"),
    ("Fiamma LED 3D regolabile — riscaldamento opzionale", "Effetto fiamma LED 3D regolabile — calore attivabile a piacere"),
    ("Protezione termica automatica integrata", "Sistema anti surriscaldamento integrato"),
    (
        "Spedizione gratis 24–48 h lavorative dopo conferma telefonica · Pagamento alla consegna · 30 giorni di garanzia soddisfatti o rimborsati",
        "Spedizione gratuita 24–48 h lavorative dopo conferma telefonica · Contrassegno · 30 giorni soddisfatti o rimborsati",
    ),
    ("<span>Come posso ordinare?</span>", "<span>Come si effettua l'ordine?</span>"),
    ("Compila il modulo con nome, telefono e indirizzo. Ti richiamiamo per confermare la consegna.", "Inserisci i dati nel modulo: ti richiamiamo per fissare la consegna."),
    ("Paghi 96 € al corriere quando ricevi il pacco — comodo e sicuro, senza anticipo.", "Saldare 96 € al corriere alla consegna — pratico e sicuro, senza anticipo."),
    ("<span>Quanti m² scalda EMBERA™?</span>", "<span>Quanti m² copre AUREN™?</span>"),
    ("Sì. Trattiamo i dati secondo l'informativa privacy e li condividiamo solo con il corriere.", "Sì. I dati sono trattati secondo l'informativa privacy del sito e condivisi solo con il corriere."),
]


def build_index() -> str:
    html = SRC.read_text(encoding="utf-8")

    for old, new in COPY_REPLACEMENTS:
        if old not in html:
            raise SystemExit(f"Missing copy block: {old[:80]!r}...")
        html = html.replace(old, new)

    html = html.replace("devicegridbay.com", "gadgetshifthub.com")
    html = html.replace("embera-2635", "italy")
    html = html.replace(
        "https://gadgetshifthub.com/it/italy/thank-you/",
        TY,
    )
    html = html.replace("info@devicegridbay.com", "info@gadgetshifthub.com")
    html = html.replace("/assets/img/products/embera/", "/assets/img/products/auren/")
    html = html.replace("EMBERA™", "AUREN™")
    html = html.replace("EMBERA", "AUREN")

    html = re.sub(
        r"window\.SITE_CONFIG = \{.*?\};",
        f"""window.SITE_CONFIG = {{
  GEO: 'it',
  PRODUCT_SLUG: 'italy',
  CURRENCY: 'EUR',
  PRICE: 96,
  OFFER_NAME: 'AUREN IT',
  LP_ID: 'it-italy',
  FORM_UID: '{FORM_UID}',
  FORM_OFFER: '2635',
  FORM_LP: '2662',
  FORM_WEBHOOK: '{FORM_WEBHOOK}',
  FORM_KEY: '{FORM_KEY}',
  THANKYOU_URL: '{TY}',
  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',
  COOKIE_ACCEPT: 'Accetta',
  COOKIE_LEARN: 'Scopri di più'
}};""",
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = html.replace(
        'value="https://hook.eu2.make.com/e8xasqjny5rsfr0pefx353ghwia4f7r1"',
        f'value="{FORM_WEBHOOK}"',
    )
    html = html.replace(
        'value="ce52f8fe99398bf301d01f91e1dac239860e02c6"',
        f'value="{FORM_KEY}"',
    )

    if 'name="subid"' not in html:
        html = html.replace(
            '<input name="lp" type="hidden" value="2662">',
            '<input name="lp" type="hidden" value="2662">\n        <input name="subid" type="hidden" value="">\n        <input name="tmfp" type="hidden" value="">',
        )

    if 'forms/html/js-v2/' not in html:
        html = html.replace(
            "</form>",
            '        <script async src="https://offers.adricenetwork.com/forms/html/js-v2/"></script>\n</form>',
            1,
        )

    html = re.sub(r"<footer class=\"site-footer\">.*?</footer>", FOOTER, html, flags=re.DOTALL)

    html = html.replace(
        'content="https://gadgetshifthub.com/assets/img/products/auren/hero.webp?v=1"',
        'content="https://gadgetshifthub.com/assets/img/products/auren/hero.webp?v=20261028"',
    )
    html = html.replace("/assets/img/products/auren/", "/assets/img/products/auren/")
    html = html.replace("hero.webp?v=1", "hero.webp?v=20261028")

    return html


def build_thankyou() -> str:
    ty = (ROOT / "it/flamora/thank-you.html").read_text(encoding="utf-8")
    reps = [
        ("flamora", "italy"),
        ("FLAMORA™", "AUREN™"),
        ("FLAMORA", "AUREN"),
        ("/it/italy/", "/it/italy/"),
    ]
    for a, b in reps:
        ty = ty.replace(a, b)
    ty = ty.replace(
        "https://gadgetshifthub.com/it/italy/thank-you.html",
        TY,
    )
    return ty


def main() -> None:
    if not SRC.is_file():
        raise SystemExit("Run download first or restore scripts/_tmp_embera_source.html")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "index.html").write_text(build_index(), encoding="utf-8")
    (OUT_DIR / "thank-you.html").write_text(build_thankyou(), encoding="utf-8")
    print("Wrote", OUT_DIR / "index.html")
    print("Wrote", OUT_DIR / "thank-you.html")


if __name__ == "__main__":
    main()
