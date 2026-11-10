#!/usr/bin/env python3
"""Clone shoproomdock.com IT Driovo landing → homeshopspot.com/it/luno (LUNO™)."""

import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ai_image_notice import ai_image_notice_html

ROOT = Path(__file__).resolve().parents[1]
SRC = "https://shoproomdock.com"
SRC_SLUG = "driovo"
GEO = "it"
SLUG = "luno"
OUT = ROOT / GEO / SLUG

META_PIXEL = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="homeshopspot.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">Prodotti utili per la vita quotidiana, consegna in 24–48 ore e pagamento alla consegna.</p>
{ai_image_notice_html("it")}
      </div>
      <div>
        <h4 class="site-footer__heading">Informazioni</h4>
        <ul class="site-footer__list">
          <li><a href="/it/about-us.html">Chi siamo</a></li>
          <li><a href="/it/contact-us.html">Contatti</a></li>
          <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/it/terms-conditions.html">Termini e condizioni</a></li>
          <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>
          <li><a href="/it/shipping-policy.html">Spedizione</a></li>
          <li><a href="/it/refund-policy.html">Resi e rimborsi</a></li>
        </ul>
      </div>
      <div>
        <h4 class="site-footer__heading">Contatti</h4>
        <ul class="site-footer__list">
          <li><strong>Northstar Digital Growth LLC</strong></li>
          <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
          <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — Tutti i diritti riservati.
      <a href="/">homeshopspot.com</a>
    </div>
  </div>
</footer>"""

TY_FOOTER = f"""<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div>
      <a href="/" class="site-logo">
        <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span>
      </a>
{ai_image_notice_html("it")}
    </div>
    <div>
      <h4 class="site-footer__heading">Informazioni</h4>
      <ul class="site-footer__list">
        <li><a href="/it/about-us.html">Chi siamo</a></li>
        <li><a href="/it/contact-us.html">Contattaci</a></li>
        <li><a href="/it/privacy-policy.html">Privacy Policy</a></li>
        <li><a href="/it/terms-conditions.html">Termini e Condizioni</a></li>
        <li><a href="/it/cookie-policy.html">Cookie Policy</a></li>
        <li><a href="/it/shipping-policy.html">Politica di spedizione</a></li>
        <li><a href="/it/refund-policy.html">Politica di reso</a></li>
      </ul>
    </div>
    <div>
      <h4 class="site-footer__heading">Contatti</h4>
      <ul class="site-footer__list">
        <li><strong>Northstar Digital Growth LLC</strong></li>
        <li>32 N Gould St., Sheridan, WY 82801, Statele Unite</li>
        <li><a href="mailto:info@homeshopspot.com">info@homeshopspot.com</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>Northstar Digital Growth LLC</strong> — Tutti i diritti riservati. <a href="/">homeshopspot.com</a></div>
</div></footer>"""

# Order matters: rephrase before global brand swap.
REPHRASE: list[tuple[str, str]] = [
    (
        "OGGI -50% — PAGHI QUANDO RICEVI IL PACCO",
        "PROMO -50% OGGI — PAGHI SOLO QUANDO ARRIVA IL PACCO",
    ),
    (
        "<strong>4,9/5</strong> — Oltre <strong>9.480</strong> famiglie in Italia gestiscono il bucato in modo più semplice ogni giorno",
        "<strong>4,9/5</strong> — Più di <strong>9.200</strong> famiglie in Italia organizzano il bucato con meno stress ogni giorno",
    ),
    (
        "🎁 Omaggio: grucce premium, sacca portaoggetti e clip multifunzione",
        "🎁 In regalo: grucce rinforzate, sacca organizzatrice e clip multiuso",
    ),
    (
        "Meno attesa sullo stendino: capi asciutti, ordinati e pronti da riporre in 20 minuti",
        "In circa 20 minuti capi asciutti e ordinati: meno tempo allo stendino, più spazio libero in casa",
    ),
    (
        "<strong>Driovo™</strong> — Asciugatrice portatile pieghevole con camera richiudibile: appendi i capi all’interno, resistenza e ventola fanno circolare aria calda mentre l’umidità esce dalle griglie. Timer integrato con arresto automatico al termine del ciclo.",
        "<strong>LUNO™</strong> è un armadio asciugatrice pieghevole con vano richiudibile: appendi il bucato dentro, resistenza e ventola spingono aria calda in circolo mentre il vapore esce dalle griglie laterali. Il timer integrato spegne tutto automaticamente a fine ciclo.",
    ),
    (
        "⏱️</div><h4>Ciclo da 20 minuti</h4><p>Timer programmabile per il bucato quotidiano</p>",
        "⏱️</div><h4>Ciclo rapido da 20 min</h4><p>Programma il timer in base al carico quotidiano</p>",
    ),
    (
        "💳</div><h4>Pagamento alla consegna</h4><p>Nessuna carta richiesta online</p>",
        "💳</div><h4>Contrassegno</h4><p>Nessun pagamento anticipato sul sito</p>",
    ),
    (
        "📦</div><h4>Compatta e pieghevole</h4><p>Si ripone in armadio o sotto il letto</p>",
        "📦</div><h4>Formato compatto</h4><p>Si chiude e si infila in armadio o sotto il letto</p>",
    ),
    (
        "↩️</div><h4>Reso entro 30 giorni</h4><p>Rimborso integrale, senza stress</p>",
        "↩️</div><h4>30 giorni per il reso</h4><p>Rimborso completo, procedura semplice</p>",
    ),
    (
        "⏰ Lo sconto del -50% resta attivo ancora per",
        "⏰ Il -50% di sconto scade tra",
    ),
    (
        "<span class=\"right\">Ultimi 4 pezzi in magazzino</span>",
        "<span class=\"right\">Restano 4 unità in stock</span>",
    ),
    (
        'data-live="<strong>{n} persone</strong> stanno guardando Driovo™ in questo momento"',
        'data-live="<strong>{n} persone</strong> stanno valutando LUNO™ adesso"',
    ),
    (
        "<strong>38 persone</strong> stanno guardando Driovo™ in questo momento",
        "<strong>38 persone</strong> stanno valutando LUNO™ adesso",
    ),
    (
        "<h2>Richiedi Driovo™ oggi a 74€</h2>",
        "<h2>Ordina LUNO™ oggi a 74€</h2>",
    ),
    (
        "Compila il modulo con i tuoi dati. Entro 24 ore un operatore ti richiama per confermare indirizzo e spedizione — senza pagamenti anticipati.",
        "Inserisci i tuoi dati nel modulo: entro 24 ore ti richiamiamo per confermare indirizzo e consegna, senza acconti online.",
    ),
    ("CONFERMO LA RICHIESTA", "INVIA LA RICHIESTA"),
    (
        "01 — Come funziona in casa",
        "01 — Funzionamento in casa",
    ),
    (
        "Camera sigillata, aria calda in circolo e vapore fuori — spegnimento automatico",
        "Vano chiuso, aria calda in movimento e umidità fuori — stop automatico",
    ),
    (
        "<span class=\"tag\">Vano chiuso</span><span class=\"tag\">Flusso caldo</span><span class=\"tag\">Timer</span>",
        "<span class=\"tag\">Camera sigillata</span><span class=\"tag\">Aria calda</span><span class=\"tag\">Timer</span>",
    ),
    (
        "Sblocchi la cerniera, disponi i capi e richiudi il vano. Resistenza e ventola mantengono aria calda in movimento; l’umidità esce lateralmente dalle griglie di ventilazione.",
        "Apri la zip, appendi i capi e richiudi il vano. Resistenza e ventola fanno girare aria calda; l’umidità esce dalle griglie laterali.",
    ),
    (
        "Imposti la durata e ti liberi la mente: a fine ciclo Driovo™ si spegne da sola, senza lasciare il dispositivo acceso troppo a lungo.",
        "Scegli la durata e non pensarci più: a fine programma LUNO™ si spegne da sola, senza rischi di lasciarla accesa a lungo.",
    ),
    (
        "02 — Il problema non è solo la superficie",
        "02 — Non basta che sembri asciutto",
    ),
    (
        "Asciugatura più uniforme — meno effetto “umido nelle pieghe”",
        "Asciugatura più omogenea — meno umidità nascosta nelle pieghe",
    ),
    (
        "<span class=\"tag\">In profondità</span><span class=\"tag\">Meno odori</span><span class=\"tag\">Più freschezza</span>",
        "<span class=\"tag\">A tutto spessore</span><span class=\"tag\">Meno cattivi odori</span><span class=\"tag\">Più freschezza</span>",
    ),
    (
        "Su stendini e sedie il tessuto può sembrare asciutto ma trattenere umidità tra cuciture e pieghe, con odore di chiuso e sensazione di capo non del tutto pronto.",
        "Su stendino o sedia il capo può sembrare pronto in superficie ma restare umido tra cuciture e pieghe, con odore di chiuso e sensazione di “non del tutto asciutto”.",
    ),
    (
        "Nel vano chiuso l’aria calda raggiunge anche le zone più difficili, così il bucato è più facile da indossare o riporre subito dopo il ciclo.",
        "Nel vano sigillato l’aria calda arriva anche dove è più difficile, così indossi o ripieghi il bucato subito dopo il ciclo.",
    ),
    (
        "03 — Pronta in pochi gesti",
        "03 — Si usa in pochi passaggi",
    ),
    (
        "Facile da usare: carichi, accendi e scegli il tempo di asciugatura",
        "Semplice da usare: carichi, accendi e imposti la durata",
    ),
    (
        "<span class=\"tag\">Comandi chiari</span><span class=\"tag\">Nessuna installazione</span><span class=\"tag\">Presa standard</span>",
        "<span class=\"tag\">Pannello intuitivo</span><span class=\"tag\">Zero montaggio</span><span class=\"tag\">Presa domestica</span>",
    ),
    (
        "Con <strong>Driovo™</strong> non servono montaggi o passaggi complicati: sistemi i capi nel vano, la accendi e imposti il timer in base al bucato che hai appena lavato. I comandi sono immediati, pensati per l’uso quotidiano in casa.",
        "Con <strong>LUNO™</strong> niente installazioni: appendi il bucato, accendi e regoli il timer in base al carico. Comandi diretti, pensati per l’uso quotidiano.",
    ),
    (
        "Ti basta una normale presa elettrica per gestire l’asciugatura in autonomia, senza dipendere da balcone, stendino o condizioni fuori porta.",
        "Una presa normale basta per asciugare in autonomia, senza contare su balcone, meteo o stendino sempre occupato.",
    ),
    (
        "04 — Pochi metri quadri? Nessun problema",
        "04 — Poco spazio in casa",
    ),
    (
        "Si ripiega e si ripone — ideale per viaggi e monolocali",
        "Si chiude e si ripone — ottima per monolocali e viaggi",
    ),
    (
        "<span class=\"tag\">Pieghevole</span><span class=\"tag\">Compatto</span><span class=\"tag\">Da viaggio</span>",
        "<span class=\"tag\">Richiudibile</span><span class=\"tag\">Leggera</span><span class=\"tag\">Portatile</span>",
    ),
    (
        "Finito il ciclo la richiudi e la metti in armadio, sotto il letto o in un ripostiglio. Niente stendino fisso in salotto né balcone sempre occupato.",
        "A fine ciclo la richiudi e la riponi in armadio, sotto il letto o in un ripostiglio. Niente stendino fisso in salotto né balcone sempre pieno.",
    ),
    (
        "Utile in monolocali, case vacanza, trasferte o campeggio: hai un modo semplice per asciugare anche senza spazio esterno.",
        "Ideale in monolocali, B&B, trasferte o campeggio: asciughi anche quando non hai spazio fuori casa.",
    ),
    (
        "<h2>Stendino tradizionale o Driovo™: le differenze</h2>",
        "<h2>Stendino classico o LUNO™: cosa cambia</h2>",
    ),
    (
        "<tr><th></th><th>Metodo classico</th><th class=\"highlight\">Con Driovo™</th></tr>",
        "<tr><th></th><th>Asciugatura tradizionale</th><th class=\"highlight\">Con LUNO™</th></tr>",
    ),
    (
        "<td>Spesso giorni, legati a spazio e clima</td><td class=\"win\">Ciclo nel vano chiuso, tempi più prevedibili</td>",
        "<td>Spesso giorni, dipende da spazio e meteo</td><td class=\"win\">Ciclo nel vano, tempi più stabili</td>",
    ),
    (
        "<td>Serve sole, vento e umidità bassa fuori</td><td class=\"win\">Funziona anche con pioggia, freddo o cielo coperto</td>",
        "<td>Serve bel tempo e aria fuori</td><td class=\"win\">Va bene anche con pioggia, freddo o nuvoloso</td>",
    ),
    (
        "<td>Capo “asciutto” ma umido tra le pieghe</td><td class=\"win\">Aria calda in movimento per ridurre l’odore di chiuso</td>",
        "<td>Superficie asciutta, umidità tra le pieghe</td><td class=\"win\">Aria calda in circolo per limitare odori di chiuso</td>",
    ),
    (
        "<td>Stendini, sedie e balcone sempre impegnati</td><td class=\"win\">Vano compatto che si chiude e si ripone</td>",
        "<td>Stendini, sedie e balcone sempre occupati</td><td class=\"win\">Unità compatta che si chiude e si ripone</td>",
    ),
    (
        "<h2>Oltre 9.480 clienti in Italia. Ecco cosa raccontano.</h2>",
        "<h2>Migliaia di clienti in Italia. Ecco le loro esperienze.</h2>",
    ),
    (
        "<h4>Niente più odore di umido tra le pieghe.</h4>",
        "<h4>Via l’odore di umido tra le pieghe.</h4>",
    ),
    (
        "«Prima sembrava tutto pronto sullo stendino, poi aprivo le pieghe e c’era ancora umidità. Ora carico tutto, imposto venti minuti sul timer e posso riporre senza controllare di continuo.»",
        "«Sul stendino sembrava tutto a posto, poi nelle pieghe c’era ancora umidità. Ora carico tutto in LUNO™, venti minuti di timer e ripongo senza controlli continui.»",
    ),
    (
        "<h4>La sera carico il bucato e al mattino è pronto.</h4>",
        "<h4>La sera carico e al mattino è tutto pronto.</h4>",
    ),
    (
        "«In lavanderia non ho spazio per stendere tutto: con la pioggia finivo con asciugamani e magliette appesi alle sedie. Ora la sera appendo tutto lì, imposto venti minuti e vado a dormire tranquilla: al risveglio trovo tutto asciutto e ordinato.»",
        "«In lavanderia non c’è spazio per stendere: con la pioggia finivo con tutto appeso alle sedie. Ora la sera carico LUNO™, imposto venti minuti e dormo serena: al mattino bucato asciutto e ordinato.»",
    ),
    (
        "<h4>Si ripone in un attimo: perfetta con poco spazio.</h4>",
        "<h4>Si ripone subito: perfetta se hai poco spazio.</h4>",
    ),
    (
        "«Ero stufa dello stendino sempre in vista. Uso Driovo™, la richiudo e la infilo sotto il letto. L’ho portata in viaggio senza problemi.»",
        "«Ero stufa dello stendino sempre in mezzo. Uso LUNO™, la chiudo e la metto sotto il letto. L’ho portata in viaggio senza pensieri.»",
    ),
    (
        "<h2>Kit Driovo™ completo, subito utilizzabile</h2>",
        "<h2>Kit LUNO™ completo, pronto all’uso</h2>",
    ),
    (
        "1× Driovo™ — asciugatrice portatile richiudibile con vano chiuso e timer",
        "1× LUNO™ — armadio asciugatrice richiudibile con vano sigillato e timer",
    ),
    (
        "1× Cavo di alimentazione",
        "1× Cavo di alimentazione standard",
    ),
    (
        "1× Custodia per riporla da chiusa",
        "1× Borsa per riporla da chiusa",
    ),
    (
        "Driovo™ — Asciugatrice portatile pieghevole | Pagamento alla consegna",
        "LUNO™ — Armadio asciugatrice pieghevole | Pagamento alla consegna",
    ),
    (
        "Driovo™ è un'asciugatrice portatile richiudibile con camera sigillata, circolazione d'aria calda e timer. Aiuta ad asciugare il bucato in profondità anche senza balcone. Pagamento alla consegna in tutta Italia.",
        "LUNO™ è un armadio asciugatrice pieghevole con vano sigillato, aria calda in circolo e timer. Aiuta ad asciugare il bucato in profondità anche senza balcone. Contrassegno in tutta Italia.",
    ),
    (
        "Driovo™ — Asciugatrice portatile pieghevole | -50% oggi",
        "LUNO™ — Armadio asciugatrice pieghevole | -50% oggi",
    ),
    (
        "Asciuga il bucato in un vano chiuso con aria calda e timer automatico. Ordine con pagamento alla consegna in Italia.",
        "Asciuga il bucato in un vano chiuso con aria calda e spegnimento automatico. Ordine con contrassegno in Italia.",
    ),
    (
        "In genere 1–2 giorni lavorativi in Italia. Prima della spedizione ricevi una chiamata di conferma entro 24 ore.",
        "Di solito 1–2 giorni lavorativi in Italia. Prima della spedizione ti chiamiamo per confermare entro 24 ore.",
    ),
    (
        "No. Paghi il corriere alla consegna. Non servono carte né acconti.",
        "No. Paghi il corriere quando ricevi il pacco. Niente carte né acconti online.",
    ),
    (
        "Magliette, felpe, intimo, asciugamani, pigiami e bucato quotidiano. Per lana, seta o tessuti delicati segui l’etichetta e preferisci cicli brevi.",
        "Magliette, felpe, intimo, asciugamani, pigiami e bucato di tutti i giorni. Per lana, seta o delicati segui l’etichetta e usa cicli brevi.",
    ),
    (
        "Il rumore è paragonabile a una ventola domestica: puoi usarla in bagno, lavanderia o camera senza troppo disturbo.",
        "Il livello sonoro è simile a una ventola: adatta a bagno, lavanderia o camera senza eccessivo disturbo.",
    ),
    (
        "È pensata per cicli domestici controllati. Il timer evita di lasciarla accesa più del necessario.",
        "Progettata per cicli brevi in casa. Il timer limita i consumi evitando di lasciarla accesa troppo a lungo.",
    ),
    (
        "Sì, entro 30 giorni con rimborso completo, senza procedure complicate.",
        "Sì, hai 30 giorni per il reso con rimborso integrale, senza burocrazia.",
    ),
    (
        "Inserisci nome, telefono e indirizzo nel modulo. Ti richiamiamo entro 24 ore per la conferma; Driovo™ arriva in 1–2 giorni lavorativi e paghi alla ricezione.",
        "Compila nome, telefono e indirizzo. Ti richiamiamo entro 24 ore; LUNO™ arriva in 1–2 giorni lavorativi e paghi al corriere.",
    ),
    # Thank-you page
    (
        "Richiesta ricevuta — Conferma telefonica in arrivo | Driovo™",
        "Richiesta registrata — Attendi la chiamata di conferma | LUNO™",
    ),
    (
        "Abbiamo registrato la tua richiesta per Driovo™. Per completare l'ordine rispondi alla chiamata di conferma del nostro operatore.",
        "La tua richiesta per LUNO™ è stata registrata. Per completare l’ordine rispondi alla chiamata del nostro operatore.",
    ),
    (
        "Ottimo — la richiesta per <strong>Driovo™</strong> è in elaborazione. Manca solo <strong>un ultimo passaggio</strong>: confermare i dati al telefono per avviare la spedizione.",
        "Perfetto — la richiesta per <strong>LUNO™</strong> è in lavorazione. Resta solo <strong>un passaggio</strong>: confermare i dati al telefono per spedire l’ordine.",
    ),
]

ALT_REPHRASE = [
    (
        "Driovo™ — set completo: armadio asciugatura aperto, ripiegato e confezione",
        "LUNO™ — set completo: unità aperta, ripiegata e confezione",
    ),
    (
        "Driovo™ — confronto prima e dopo: camicie lisce senza pieghe",
        "LUNO™ — prima e dopo: meno pieghe e capi più uniformi",
    ),
    (
        "Driovo™ — uso semplice: timer e comandi sul pannello digitale",
        "LUNO™ — pannello digitale con timer e comandi intuitivi",
    ),
    (
        "Driovo™ aperta in salotto e ripiegata sul tavolo",
        "LUNO™ in uso in salotto e ripiegata sul tavolo",
    ),
    (
        "Driovo™ in camera da letto con capi appesi",
        "LUNO™ in camera con capi appesi nel vano",
    ),
    (
        "Driovo™ in lavanderia mentre si appende una camicia",
        "LUNO™ in lavanderia con camicia appesa",
    ),
    (
        "Driovo™ appena estratta dalla confezione in bagno",
        "LUNO™ appena tolta dalla confezione in bagno",
    ),
    (
        "Kit completo Driovo™: unità aperta, ripiegata e confezione",
        "Kit LUNO™ completo: unità aperta, chiusa e confezione",
    ),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "homeshopspot-clone/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def strip_gtag(html: str) -> str:
    html = re.sub(
        r"<!-- Google tag \(gtag\.js\) -->.*?</script>\s*<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"<!-- Event snippet for Purchase.*?<script>.*?</script>\s*",
        "",
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def remap_asset_paths(html: str) -> str:
    html = html.replace("/assets/img/products/driovo/", "/assets/img/products/luno/")
    html = html.replace("/assets/img/reviews/driovo/", "/assets/img/reviews/luno/")
    html = html.replace("/assets/video/driovo/", "/assets/video/luno/")
    html = html.replace("driovo-video", "luno-video")
    return html


def download_assets(html: str) -> None:
    paths = sorted(
        set(
            re.findall(
                r"/assets/(?:img|video)/(?:products|reviews)/driovo/[^\"'\\s>]+",
                html,
            )
        )
    )
    paths += sorted(set(re.findall(r"/assets/video/driovo/[^\"'\\s>]+", html)))
    seen: set[str] = set()
    for rel in paths:
        if rel in seen:
            continue
        seen.add(rel)
        rel_clean = rel.split("?")[0]
        luno_rel = rel_clean.replace("/driovo/", "/luno/")
        dest = ROOT / luno_rel.lstrip("/")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            continue
        url = SRC + rel_clean
        print("GET", url)
        try:
            dest.write_bytes(fetch(url))
        except Exception as exc:
            print("WARN", url, exc)


def apply_rephrase(html: str) -> str:
    for old, new in REPHRASE:
        html = html.replace(old, new)
    for old, new in ALT_REPHRASE:
        html = html.replace(old, new)
    html = html.replace("Driovo™", "LUNO™")
    html = html.replace("DRIOVO™", "LUNO™")
    html = html.replace("Driovo", "LUNO")
    html = html.replace("DRIOVO", "LUNO")
    html = html.replace("driovo", "luno")
    return html


def homeshopspotify(html: str) -> str:
    html = html.replace("shoproomdock.com", "homeshopspot.com")
    html = html.replace("info@shoproomdock.com", "info@homeshopspot.com")
    html = html.replace("shoproomdock", "homeshopspot")
    html = html.replace("The Lead Empire L.L.C-FZ", "Northstar Digital Growth LLC")
    html = html.replace(
        "Meydan Grandstand, 6th floor, Meydan Road, Dubai, Emiratos Árabes Unidos",
        "32 N Gould St., Sheridan, WY 82801, Statele Unite",
    )
    ty_url = f"https://homeshopspot.com/{GEO}/{SLUG}/thank-you.html"
    html = re.sub(
        rf'value="https://homeshopspot\.com/{GEO}/{SRC_SLUG}/thank-you\.html"',
        f'value="{ty_url}"',
        html,
    )
    html = html.replace(
        f"https://homeshopspot.com/{GEO}/{SRC_SLUG}/thank-you.html",
        ty_url,
    )
    html = re.sub(
        rf'<link rel="canonical" href="https://homeshopspot\.com/{GEO}/{SLUG}/">',
        f'<link rel="canonical" href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">',
        html,
        count=1,
    )
    html = re.sub(
        rf'<meta property="og:url" content="https://homeshopspot\.com/{GEO}/{SLUG}/">',
        f'<meta property="og:url" content="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">',
        html,
        count=1,
    )
    html = re.sub(
        r"GOOGLE_ADS_CONVERSION_SEND_TO: '[^']*',\s*",
        "",
        html,
        count=1,
    )
    html = re.sub(
        r"  META_PIXEL_ID: '',\s*GOOGLE_TAG_ID: '',\s*GOOGLE_ADS_CONVERSION_ID: '',\s*TY_CONVERSION_LABEL: '',\s*",
        "",
        html,
        count=1,
    )
    html = html.replace(
        "FORM_ENDPOINT: 'https://TODO-network-endpoint.com/api/lead'",
        "FORM_ENDPOINT: 'https://offers.adricenetwork.com/forms/html/'",
    )
    html = html.replace("PRODUCT_SLUG: 'driovo'", f"PRODUCT_SLUG: '{SLUG}'")
    html = html.replace("OFFER_NAME: 'Driovo IT'", "OFFER_NAME: 'LUNO IT'")
    html = html.replace("LP_ID: 'it-driovo-v1'", "LP_ID: 'it-luno-v1'")
    return html


def process_landing(html: str) -> str:
    html = remap_asset_paths(html)
    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = apply_rephrase(html)
    html = homeshopspotify(html)
    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def process_thank_you(html: str) -> str:
    html = remap_asset_paths(html)
    html = strip_gtag(html)
    if "<!-- Meta Pixel Code -->" not in html:
        html = html.replace("<head>", "<head>\n" + META_PIXEL + "\n", 1)
    html = apply_rephrase(html)
    html = homeshopspotify(html)
    html = re.sub(
        r'<a href="/" class="site-logo"[^>]*>.*?</a>',
        '<a href="/" class="site-logo" aria-label="homeshopspot.com home">\n'
        '      <span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span>'
        '<span class="site-logo__text-accent">.com</span></span>\n    </a>',
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"<footer class=\"site-footer\">.*?</footer>",
        TY_FOOTER,
        html,
        count=1,
        flags=re.DOTALL,
    )
    cpa = 13.0
    html = re.sub(r"CONVERSION_VALUE:\s*[0-9.]+", f"CONVERSION_VALUE: {cpa}", html, count=1)
    if "fbq('track', 'Purchase'" not in html:
        html = html + f"""

<script>
fbq('track', 'Purchase', {{
  value: {cpa:.2f},
  currency: 'EUR'
}});
</script>
"""
    return html


def main() -> None:
    landing_raw = fetch(f"{SRC}/{GEO}/{SRC_SLUG}/").decode("utf-8")
    download_assets(landing_raw)
    landing = process_landing(landing_raw)

    ty_raw = fetch(f"{SRC}/{GEO}/{SRC_SLUG}/thank-you.html").decode("utf-8")
    ty = process_thank_you(ty_raw)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "landing.html").write_text(landing, encoding="utf-8", newline="\n")
    (OUT / "thank-you.html").write_text(ty, encoding="utf-8", newline="\n")
    index = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{GEO}/{SLUG}/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{GEO}/{SLUG}/landing.html">
<link rel="canonical" href="https://homeshopspot.com/{GEO}/{SLUG}/landing.html">
</head>
<body>
<p><a href="/{GEO}/{SLUG}/landing.html">LUNO™</a></p>
</body>
</html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
