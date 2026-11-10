#!/usr/bin/env python3
"""One-off generator: RO FLAMORA landing from trimex shell + ArcForce/FLAMORA copy."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V = "20261009"
IMG = f"/assets/img/products/flamora"

trimex = (ROOT / "ro/trimex-2637/index.html").read_text(encoding="utf-8")

pairs = [
    ("trimex-2637", "flamora"),
    ("TRIMEX™", "FLAMORA™"),
    ("TRIMEX", "FLAMORA"),
    ("/assets/img/products/trimex/", f"{IMG}/"),
    ("019fd3ba-5142-7ab3-b965-8163a326c7f9", "019c7158-9ae4-737e-8d04-502baa35da6c"),
    ("2637", "2699"),
    ("2664", "2732"),
    ("lynkdu9dee6imynkym5wtses9339q95h", "rk3me12plkw5ubpcoxb9nrx4utnc862q"),
    ("7611c6c16811da011ffa39878e1d1e1e90c70d50", "c037650f677ec829c3e24537d0b14ae2102b89e2"),
    ("20260926", V),
    ("PRICE: 399", "PRICE: 597"),
    ("OFFER_NAME: 'TRIMEX RO #2637'", "OFFER_NAME: 'FLAMORA RO #2699'"),
    ("LP_ID: 'ro-2637'", "LP_ID: 'ro-2699'"),
]
for a, b in pairs:
    trimex = trimex.replace(a, b)

# --- head ---
trimex = trimex.replace(
    "<title>FLAMORA™ — Motocoasă cu acumulator fără benzină | -50% azi</title>",
    "<title>FLAMORA™ — Aparat de Sudură Profesional 8 în 1 Fără Butelie</title>",
)
trimex = trimex.replace(
    'content="Motocoasă FLAMORA™ cu motor 2880 W, 2 baterii de 60 W incluse și doar 2 kg. Fără benzină, fum sau cabluri. Plată la livrare."',
    'content="FLAMORA™: aparat de sudură profesional 8 în 1 fără butelie. Sudură laser, MIG fără gaz, TIG și electrod la priză 220V. -70% azi, plată la livrare."',
)
trimex = trimex.replace(
    'content="FLAMORA™ — Motocoasă cu acumulator fără benzină | -50% azi"',
    'content="FLAMORA™ — Aparat de Sudură Profesional 8 în 1 | -70% azi"',
)
trimex = trimex.replace(
    'content="Motocoasă FLAMORA™ cu motor 2880 W, 2 baterii de 60 W incluse și doar 2 kg. Fără benzină, fum sau cabluri. Plată la livrare."',
    'content="FLAMORA™: sudură 8 în 1 la priză 220V. -70% azi, plată la livrare."',
)

body_start = '<div class="topbar">'
body_end = '<footer class="site-footer">'
start = trimex.index(body_start)
end = trimex.index(body_end)
new_body = f'''{body_start}🔥 DOAR ASTĂZI: -70% + PLATA LA LIVRARE 🔥</div>

<div class="rating-strip wrap">
  <div class="stars">★★★★★</div>
  <div class="rating-text"><strong>4,8/5</strong> — Peste <strong>8.700</strong> de recenzii verificate</div>
</div>

<section class="hero wrap">
  <div class="hero-copy">
    <span class="gift-strip">🛡️ Garanție 2 ani + Livrare în 24-48h</span>
    <h1 class="h1-mobile-only">Aparat de Sudură Profesional 8 în 1 <span class="hl">⚡ Sudează Automat</span> Orice Material</h1>
    <h1 class="h1-desktop-only">Aparat de Sudură Profesional 8 în 1 ⚡ <span class="hl">Sudează Automat</span> Orice Material</h1>
    <p class="lead">Peste 8.700 de persoane și-au înlocuit deja vechile aparate de sudură: un singur dispozitiv compact pentru sudură laser, MIG fără gaz, TIG și cu electrod. <strong>Funcționează la priza normală de 220V</strong> și sudează aluminiu, fontă, oțel, fier și inox — chiar și sub apă.</p>
    <div class="hero-image hero-image-mobile-only">
      <img decoding="async" src="{IMG}/hero.webp?v={V}" alt="FLAMORA aparat de sudură profesional 8 în 1" loading="eager" fetchpriority="high">
    </div>
    <div class="price-block"><span class="was">1 990 lei</span><span class="now">597 lei</span><span class="pct">-70%</span></div>
    <a href="#order-form" class="cta-btn">DA, VREAU FLAMORA™ →</a>
    <p class="form-note">🔒 Fără avans · Fără card · Plătești doar la livrare</p>
  </div>
  <div class="hero-image hero-image-desktop-only">
    <img decoding="async" src="{IMG}/hero.webp?v={V}" alt="FLAMORA aparat de sudură profesional 8 în 1" loading="eager" fetchpriority="high">
  </div>
</section>

<div class="wrap">
  <div class="feature-row">
    <div class="feature-item"><div class="ico">🚚</div><h4>Livrare în 24-48h</h4><p>Expediere rapidă în toată România</p></div>
    <div class="feature-item"><div class="ico">💳</div><h4>Plata la livrare</h4><p>Plătești doar când primești</p></div>
    <div class="feature-item"><div class="ico">🛡️</div><h4>Garanție 2 ani</h4><p>Acoperire oficială inclusă</p></div>
    <div class="feature-item"><div class="ico">↩️</div><h4>Retur în 30 de zile</h4><p>Rambursare simplă și gratuită</p></div>
  </div>
</div>

<section class="order-section" id="order-form">
  <div class="wrap">
    <div class="urgency-strip">
      <div class="countdown-row">
        <div class="countdown-label">⏰ Oferta de -70% expiră în</div>
        <div class="countdown-timer" id="countdownTimer">
          <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">Ore</div></div><div class="sep">:</div>
          <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">Min</div></div><div class="sep">:</div>
          <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">Sec</div></div>
        </div>
      </div>
      <div class="stock-row">
        <div class="stock-label"><span class="left">Disponibilitate</span><span class="right">Ultimele bucăți în stoc</span></div>
        <div class="stock-bar"><div class="stock-bar-fill"></div></div>
      </div>
      <div class="live-row">
        <span class="dot"></span>
        <span id="liveCount" data-live="<strong>{{n}} de persoane</strong> se uită la FLAMORA™ acum"><strong>38 de persoane</strong> se uită la FLAMORA™ acum</span>
      </div>
    </div>

    <div class="order-card">
      <h2>Finalizează comanda</h2>
      <p>Completează formularul de mai jos, echipa noastră te va contacta pentru a confirma toate detaliile.</p>
      <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Nume și prenume*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Andrei Popescu" required><br>
        <label for="tel">Număr de telefon*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+40 712 345 678" required><br>
        <label for="street-address">Adresa de livrare*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Strada Mihai Eminescu 15, Ap. 8, București" required><br>
        <input name="uid" type="hidden" value="019c7158-9ae4-737e-8d04-502baa35da6c">
        <input name="offer" type="hidden" value="2699">
        <input name="lp" type="hidden" value="2732">
        <input name="subid" id="subid" type="hidden" value="">
        <input name="tmfp" id="tmfp" type="hidden" value="">
        <input name="thankyoupage" type="hidden" value="https://gadgetshifthub.com/ro/flamora/thank-you.html">
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/rk3me12plkw5ubpcoxb9nrx4utnc862q">
        <input name="_key" type="hidden" value="c037650f677ec829c3e24537d0b14ae2102b89e2">
        <button type="submit" class="cta-btn">CONFIRMĂ COMANDA</button>
        <p class="form-note">🔒 Fără avans · Fără card · Plătești doar la livrare</p>
      </form>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{IMG}/desc-1.webp?v={V}" alt="Aparat de sudură 8 în 1 cu funcții multiple" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">01 — Un singur dispozitiv pentru orice lucrare</div>
      <h3>8 funcții într-un singur dispozitiv compact</h3>
      <div class="tag-row"><span class="tag">Sudură laser</span><span class="tag">MIG fără gaz</span><span class="tag">TIG și electrod</span></div>
      <p>Sudură laser, MIG fără gaz, TIG, cu electrod, în puncte și chiar tăiere: totul într-un singur dispozitiv compact. Include și o funcție de curățare laser care elimină rugina, vopseaua și oxidarea de pe suprafețele metalice și piesele mecanice.</p>
      <p class="italic">Gata cu dulapurile pline de echipamente diferite: un singur dispozitiv pentru orice tip de lucrare.</p>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{IMG}/desc-2.webp?v={V}" alt="Sistem de control automat priză 220V" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">02 — Control automat, fără instalare industrială</div>
      <h3>Sistemul detectează materialul și reglează totul singur</h3>
      <div class="tag-row"><span class="tag">Priză standard 220V</span><span class="tag">Reglare automată</span><span class="tag">Potrivit pentru începători</span></div>
      <p>Sistemul electronic recunoaște tipul de prelucrare și reglează automat puterea, curentul și viteza de avans a sârmei, evitând greșelile chiar și pentru cei fără experiență. Nu este nevoie de curent industrial sau de o instalație trifazată: este suficientă priza normală de 220V, acasă, în garaj sau în atelier.</p>
      <p class="italic">Îl bagi în priză și începi imediat să lucrezi.</p>
    </div>
  </div>
</section>

<section class="why-block wrap">
  <div class="why-grid">
    <div class="why-img"><img decoding="async" src="{IMG}/desc-3.webp?v={V}" alt="Sudură pe aluminiu oțel și inox chiar și sub apă" loading="lazy"></div>
    <div>
      <div class="num-eyebrow">03 — Sudează orice material, chiar și sub apă</div>
      <h3>Aluminiu, fontă, oțel, fier, inox — fără limite</h3>
      <div class="tag-row"><span class="tag">Materiale dificile</span><span class="tag">Utilizare și sub apă</span><span class="tag">Protecție la suprasarcină</span></div>
      <p>Conceput pentru a lucra chiar și în condiții extreme, unde aparatele de sudură tradiționale nu reușesc să funcționeze: inclusiv sub apă. Sistemele integrate de protecție la suprasarcină și supraîncălzire garantează o utilizare sigură la fiecare lucrare.</p>
      <p class="italic">Kitul include clești, cabluri și toate accesoriile: gata de utilizare fără costuri suplimentare.</p>
      <a href="#order-form" class="cta-btn cta-inline">DA, VREAU FLAMORA™ →</a>
    </div>
  </div>
</section>

<section class="compare wrap">
  <div class="section-label">Comparație directă</div>
  <h2>Aparat de sudură tradițional vs FLAMORA™</h2>
  <div class="compare-table-wrap" role="region" aria-label="Comparație aparat de sudură tradițional și FLAMORA" tabindex="0">
    <table>
      <tr><th></th><th>Tradițional</th><th class="highlight">FLAMORA™</th></tr>
      <tr><td>Tip de sudură</td><td>Doar un tip</td><td class="win">8 în 1: laser, MIG, TIG, electrod, în puncte</td></tr>
      <tr><td>Tăiere și curățare</td><td>Nu sunt incluse</td><td class="win">Tăiere și curățare laser incluse</td></tr>
      <tr><td>Reglare</td><td>Manuală și complexă</td><td class="win">Automată și inteligentă</td></tr>
      <tr><td>Ușurință în utilizare</td><td>Dificil pentru începători</td><td class="win">Ușor chiar și fără experiență</td></tr>
      <tr><td>Materiale dificile</td><td>Performanțe limitate</td><td class="win">Aluminiu, fontă, inox fără probleme</td></tr>
      <tr><td>Alimentare</td><td>Deseori necesită 380V industrial</td><td class="win">Priză standard 220V</td></tr>
    </table>
  </div>
</section>

<section class="testimonials">
  <div class="wrap">
    <div class="section-heading"><h2>Peste 8.700 de clienți mulțumiți. Descoperă de ce aleg FLAMORA™.</h2></div>
    <div class="t-grid">
      <div class="testimonial">
        <img class="t-photo" src="{IMG}/review-1.webp?v={V}" alt="FLAMORA utilizat pe o piesă de aluminiu" loading="lazy" decoding="async">
        <div class="t-body"><div class="stars">★★★★★</div><h4>Puternic și ușor de folosit chiar și pentru începători.</h4><p>«Foarte puternic și ușor de utilizat. Am sudat aluminiu și inox fără probleme, deși nu am multă experiență.»</p>
          <div class="author-row"><img class="avatar" src="{IMG}/reviewer-1.webp?v={V}" alt="Andrei P." loading="lazy" decoding="async"><div class="author">Andrei P. — București, Client verificat</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img class="t-photo" src="{IMG}/review-2.webp?v={V}" alt="FLAMORA conectat la o priză standard în garaj" loading="lazy" decoding="async">
        <div class="t-body"><div class="stars">★★★★★</div><h4>Gata de utilizare, nicio instalare industrială.</h4><p>«Funcționează perfect la priza normală de 220V și este gata de utilizare imediat. Ideal pentru garaj și mici lucrări pe acasă.»</p>
          <div class="author-row"><img class="avatar" src="{IMG}/reviewer-2.webp?v={V}" alt="Mihai I." loading="lazy" decoding="async"><div class="author">Mihai I. — Cluj-Napoca, Client verificat</div></div>
        </div>
      </div>
      <div class="testimonial">
        <img class="t-photo" src="{IMG}/review-3.webp?v={V}" alt="Curățare laser pe o piesă ruginită" loading="lazy" decoding="async">
        <div class="t-body"><div class="stars">★★★★★</div><h4>Curățarea laser este incredibilă.</h4><p>«Funcția de curățare laser este surprinzătoare. Rugina a dispărut în foarte scurt timp de pe piesele vechi.»</p>
          <div class="author-row"><img class="avatar" src="{IMG}/reviewer-3.webp?v={V}" alt="Florin D." loading="lazy" decoding="async"><div class="author">Florin D. — Timișoara, Client verificat</div></div>
        </div>
      </div>
    </div>
    <a href="#order-form" class="cta-btn cta-inline">DA, VREAU FLAMORA™ →</a>
  </div>
</section>

<section class="kit-section wrap">
  <div class="section-heading"><span class="eyebrow">În pachet</span><h2>Kit complet FLAMORA™, gata de utilizare</h2></div>
  <div class="kit-box">
    <img src="{IMG}/hero.webp?v={V}" alt="Kit complet FLAMORA" loading="lazy" decoding="async">
    <div class="kit-content">
      <div class="price-block" style="margin-bottom:16px;"><span class="was">1 990 lei</span><span class="now">597 lei</span><span class="pct">-70%</span></div>
      <ul>
        <li>Aparat de sudură 8 în 1 — laser, MIG fără gaz, TIG, electrod, în puncte și tăiere</li>
        <li>Clești și cabluri complete — niciun accesoriu de cumpărat separat</li>
        <li>Sistem de control automat — detectează materialul și reglează singur puterea</li>
        <li>Funcție de curățare laser — îndepărtează rugina și oxidarea</li>
        <li>Potrivit și pentru prelucrări sub apă</li>
        <li>Protecție integrată la suprasarcină și supraîncălzire</li>
        <li>Garanție oficială de 2 ani</li>
      </ul>
      <a href="#order-form" class="cta-btn">DA, VREAU FLAMORA™ →</a>
    </div>
  </div>
</section>

<section class="faq wrap">
  <div class="section-heading"><h2>Întrebări frecvente</h2></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>Când ajunge?</span><span class="arrow">▾</span></button><div class="faq-a"><p>Livrarea are loc în 24-48 de ore lucrătoare. Te vom contacta în câteva ore pentru a confirma comanda și detaliile de livrare.</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>Pot plăti la livrare?</span><span class="arrow">▾</span></button><div class="faq-a"><p>Da, plătești numerar direct curierului când primești coletul. Pregătește suma de 597 lei.</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>Este nevoie de curent industrial la 380V?</span><span class="arrow">▾</span></button><div class="faq-a"><p>Nu, funcționează la priza normală de 220V: îl bagi în priză și începi imediat să lucrezi, acasă, în garaj sau în atelier.</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>Îl pot folosi chiar dacă nu am experiență în sudură?</span><span class="arrow">▾</span></button><div class="faq-a"><p>Da, sistemul de control automat detectează materialul și reglează singur puterea, curentul și viteza sârmei, evitând greșelile chiar și pentru începători.</p></div></div>
  <div class="faq-item"><button class="faq-q" type="button"><span>Și dacă nu sunt mulțumit?</span><span class="arrow">▾</span></button><div class="faq-a"><p>Ai la dispoziție 30 de zile pentru a-l returna gratuit și a primi rambursarea completă, fără întrebări.</p></div></div>
</section>

'''

trimex = trimex[:start] + new_body + trimex[end:]

# og:image
trimex = trimex.replace(
    f"https://gadgetshifthub.com/assets/img/products/flamora/hero.webp?v={V}",
    f"https://gadgetshifthub.com{IMG}/hero.webp?v={V}",
)

out_dir = ROOT / "ro/flamora"
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "index.html").write_text(trimex, encoding="utf-8")

# thank-you
ty = (ROOT / "ro/trimex-2637/thank-you.html").read_text(encoding="utf-8")
for a, b in [
    ("trimex-2637", "flamora"),
    ("TRIMEX™", "FLAMORA™"),
    ("TRIMEX", "FLAMORA"),
    ("2637", "2699"),
    ("PRICE: 399", "PRICE: 597"),
    ("trackPurchase(399", "trackPurchase(597"),
]:
    ty = ty.replace(a, b)
(out_dir / "thank-you.html").write_text(ty, encoding="utf-8")
print("OK", out_dir)
