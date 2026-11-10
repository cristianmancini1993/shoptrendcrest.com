#!/usr/bin/env python3
"""One-off patch: granvia IT noreva LP copy + paths."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "it" / "granvia" / "index.html"
text = path.read_text(encoding="utf-8")

text = text.replace("/assets/img/products/cendora/", "/assets/img/products/granvia/")
text = text.replace("https://shoptrendcrest.com/it/cendora/", "https://shoptrendcrest.com/it/granvia/")
text = text.replace("it/cendora/thank-you.html", "it/granvia/thank-you.html")
text = text.replace("PRODUCT_SLUG: 'cendora'", "PRODUCT_SLUG: 'granvia'")
text = text.replace("LP_ID: 'it-cendora-v1'", "LP_ID: 'it-granvia-v1'")

replacements = [
    (
        "<title>Granvia PRO 2200™ — Tritacarne elettrico 2200 W con 3 dischi</title>",
        "<title>Granvia™ — Tritacarne elettrico 2600 W con 3 dischi</title>",
    ),
    (
        'content="Tritacarne elettrico Granvia PRO 2200™ da 2200 W con 3 dischi in acciaio, imbottigliatrice per salsicce e funzione reverse. Hamburger e salumi fatti in casa. Pagamento alla consegna in Italia."',
        'content="Tritacarne elettrico Granvia™ da 2600 W: fino a 5 kg di carne, 3 dischi in acciaio, accessorio insaccatore e funzione reverse. Pagamento alla consegna in Italia."',
    ),
    (
        'content="Granvia PRO 2200™ — Tritacarne elettrico professionale per casa"',
        'content="Granvia™ — Tritacarne elettrico professionale per casa"',
    ),
    (
        'content="Carne tritata fresca, hamburger, polpette e salsicce con motore 2200 W, 3 dischi e imbottigliatrice inclusa."',
        'content="Carne tritata fresca, hamburger, polpette e salsicce con motore 2600 W, 3 dischi e accessorio insaccatore incluso."',
    ),
    (
        "hanno già scelto Granvia PRO 2200™</div>",
        "hanno già scelto Granvia™</div>",
    ),
    (
        "🎁 IN OMAGGIO: IMBOTTIGLIATRICE + 3 DISCHI IN ACCIAIO</span>",
        "🎁 IN OMAGGIO: ACCESSORIO INSACCATORE + 3 DISCHI IN ACCIAIO</span>",
    ),
    (
        '<h1 class="h1-mobile-only"><span class="hl">4 kg di carne in 60 secondi.</span> 2200 W che non si fermano mai. Il vecchio tritacarne può andare in pensione.</h1>',
        '<h1 class="h1-mobile-only"><span class="hl">Fino a 5 kg di carne.</span> 2600 W che non si fermano mai. Il vecchio tritacarne può andare in pensione.</h1>',
    ),
    (
        '<h1 class="h1-desktop-only">4 KG DI CARNE IN 60 SECONDI. <span class="hl">2200 W</span> CHE NON SI FERMANO MAI. IL TUO VECCHIO TRITACARNE PUÒ ANDARE IN PENSIONE.</h1>',
        '<h1 class="h1-desktop-only">FINO A 5 KG DI CARNE. <span class="hl">2600 W</span> CHE NON SI FERMANO MAI. IL TUO VECCHIO TRITACARNE PUÒ ANDARE IN PENSIONE.</h1>',
    ),
    (
        '<p class="lead">Un solo apparecchio 4 in 1 per hamburger, salsicce, salse, verdure e formaggio. Niente inceppi grazie alla funzione reverse, niente surriscaldamento grazie alla protezione automatica, niente ruggine grazie all\'acciaio inox. Lavora tu meno, lavora lui di più.</p>',
        "<p class=\"lead\">Quattro funzioni in un solo apparecchio: macinatura della carne, insaccatura salsicce, grattugiatura verdure e preparazione kibbe. Niente inceppi grazie alla funzione reverse, niente surriscaldamento grazie alla protezione automatica, niente ruggine grazie all'acciaio inox. Meno fatica per te, più lavoro per lui.</p>",
    ),
    (
        'alt="Tritacarne elettrico Granvia PRO 2200™ con accessori"',
        'alt="Tritacarne elettrico Granvia™ con accessori"',
    ),
    (
        "<h4>Motore 2200 W</h4><p>Tritatura rapida con poco sforzo</p>",
        "<h4>Motore 2600 W</h4><p>Fino a 5 kg di carne per sessione</p>",
    ),
    (
        "<h4>3 dischi in acciaio</h4><p>Fine, medio e grosso</p>",
        "<h4>3 dischi in acciaio</h4><p>Tritatura fine, media e grossa</p>",
    ),
    (
        "stanno guardando Granvia PRO 2200™ in questo momento",
        "stanno guardando Granvia™ in questo momento",
    ),
    (
        'alt="Granvia PRO 2200™: carne tritata fresca"',
        'alt="Granvia™: carne tritata fresca"',
    ),
    (
        '<span class="tag">2200 W</span>',
        '<span class="tag">2600 W</span>',
    ),
    (
        "Il motore da 2200 W lavora in fretta.",
        "Il motore da 2600 W affronta anche grandi quantità di carne.",
    ),
    (
        'alt="Imbottigliatrice Granvia™ per salsicce casalinghe"',
        'alt="Accessorio insaccatore Granvia™ per salsicce casalinghe"',
    ),
    (
        '<span class="tag">Imbottigliatrice</span><span class="tag">3 dischi</span><span class="tag">Spezie tue</span>',
        '<span class="tag">Accessorio insaccatore</span><span class="tag">3 dischi</span><span class="tag">Spezie a tua scelta</span>',
    ),
    (
        "<p>L'accessorio imbottigliatore trasforma la carne tritata in salsicce casalinghe. Con i 3 dischi intercambiabili (fine, medio e grosso) ottieni la consistenza giusta per ogni ricetta.</p>",
        "<p>L'accessorio insaccatore trasforma la carne tritata in salsicce casalinghe. Con i 3 dischi intercambiabili ottieni tritatura fine, media e grossa per ogni ricetta.</p>",
    ),
    (
        'alt="Granvia PRO 2200™: facile da pulire"',
        'alt="Granvia™: facile da pulire"',
    ),
    (
        '<span class="tag">Reverse</span><span class="tag">Spintore</span><span class="tag">Spazzolino</span>',
        '<span class="tag">Funzione reverse</span><span class="tag">Pressino</span><span class="tag">Spazzolino</span>',
    ),
    (
        "<p>Tramoggia e spintore per lavorare con le mani lontane dal meccanismo. Se la carne si blocca, la funzione reverse libera il meccanismo. I pezzi si smontano e si puliscono con lo spazzolino incluso.</p>",
        "<p>Tramoggia e pressino per lavorare con le mani lontane dal meccanismo. Se la carne si blocca, la funzione reverse libera il meccanismo. I pezzi si smontano e si puliscono con lo spazzolino incluso.</p>",
    ),
    (
        "<h2>Tritacarne base o Granvia PRO 2200™? Ecco la differenza</h2>",
        "<h2>Tritacarne base o Granvia™? Ecco la differenza</h2>",
    ),
    (
        'aria-label="Confronto tra tritacarne base e Granvia PRO 2200"',
        'aria-label="Confronto tra tritacarne base e Granvia"',
    ),
    (
        '<td class="win">Motore da 2200 W</td>',
        '<td class="win">Motore da 2600 W · fino a 5 kg</td>',
    ),
    (
        "<td>Senza imbottigliatore</td><td class=\"win\">Imbottigliatrice inclusa</td>",
        "<td>Senza accessorio insaccatore</td><td class=\"win\">Accessorio insaccatore incluso</td>",
    ),
    (
        "<h2>Dopo Granvia PRO 2200™, tornare indietro è difficile</h2>",
        "<h2>Dopo Granvia™, tornare indietro è difficile</h2>",
    ),
    (
        "alt=\"Paola prepara salsicce casalinghe con l'imbottigliatore Granvia\"",
        "alt=\"Paola prepara salsicce casalinghe con l'accessorio insaccatore Granvia\"",
    ),
    (
        "anche quando preparo una quantità grande. Per questo prezzo sono molto soddisfatta.»</p>",
        "anche quando lavoro grandi quantità di carne. Per questo prezzo sono molto soddisfatta.»</p>",
    ),
    (
        "<h2>Granvia PRO 2200™ — kit completo, pronto all'uso</h2>",
        "<h2>Granvia™ — kit completo, pronto all'uso</h2>",
    ),
    (
        'alt="Contenuto completo tritacarne Granvia PRO 2200™"',
        'alt="Contenuto completo tritacarne Granvia™"',
    ),
    (
        """      <ul>
        <li>Tritacarne elettrico con motore da 2200 W</li>
        <li>Tre dischi in acciaio — tritatura fine, media e grossa</li>
        <li>Accessorio imbottigliatore per salsicce</li>
        <li>Funzione reverse, tramoggia e spintore</li>
        <li>Kit con tramoggia, spintore e spazzolino di pulizia</li>
        <li>Libretto istruzioni e garanzia produttore</li>
      </ul>""",
        """      <ul>
        <li>Tritacarne elettrico Granvia™ con motore da 2600 W (fino a 5 kg di carne)</li>
        <li>Tre dischi in acciaio — tritatura fine, media e grossa</li>
        <li>Accessorio insaccatore per salsicce</li>
        <li>Tramoggia, pressino e spazzolino di pulizia</li>
        <li>Manuale di istruzioni e garanzia del produttore</li>
      </ul>""",
    ),
    (
        "<div class=\"faq-a\"><p>Alla consegna paghi questo prezzo in contanti al corriere.</p></div>",
        "<div class=\"faq-a\"><p>Paghi 89 € in contanti al corriere alla consegna.</p></div>",
    ),
    (
        "<div class=\"faq-a\"><p>Sì. L'imbottigliatrice inclusa ti permette di preparare salsicce con carne e spezie a tua scelta.</p></div>",
        "<div class=\"faq-a\"><p>Sì. L'accessorio insaccatore incluso ti permette di preparare salsicce con carne e spezie a tua scelta.</p></div>",
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"Missing expected fragment:\n{old[:120]}...")
    text = text.replace(old, new)

for bad in ("PRO 2200", "2200 W", "2200™", "60 secondi", "imbottigli", "IMBOTTIGLI", "Spintore", "spintore", "Lavora tu meno"):
    if bad.lower() in text.lower() and bad != "imbottigli":  # careful
        pass
# verify no leftover PRO 2200 / 2200
import re
if re.search(r"PRO 2200|2200\s*W|60 secondi|imbottigli|IMBOTTIGLI|Spintore|spintore|Lavora tu meno", text, re.I):
    raise SystemExit("Leftover terms in granvia index")

path.write_text(text, encoding="utf-8", newline="\n")
print("patched", path)
