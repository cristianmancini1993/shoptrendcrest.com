#!/usr/bin/env python3
"""Build Dochura Elementor template JSON from TEMPLATE 4 BENEFITS structure."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path("/Users/xinsetto/Desktop/work/Templates/TEMPLATE 4 BENEFITS.json")
OUT = Path("/Users/xinsetto/Desktop/work/Templates/TEMPLATE 4 BENEFITS.json")
HTML_OUT = ROOT / "preview/template-4-benefits/dochura-from-json.html"
LANDING_OUT = ROOT / "it/dochura/landing.html"
THANKYOU_URL = "https://shoptrendcrest.com/it/dochura/thank-you.html"

# CSS block copied 1:1 from original export (unchanged).
CSS = r""":root{
  --color-bg:#ffffff;
  --color-bg-alt:#f7f9fb;
  --color-text:#14181f;
  --color-text-muted:#5b6472;
  --color-accent:#e2231a;
  --color-accent-dark:#b91912;
  --color-highlight:#1e9be0;
  --color-border:#e7eaee;
  --color-border-blue:#a9d8f5;
  --color-blue-bg:#eaf7fe;
  --color-pink-bg:#fdeeee;
  --color-success:#1f9d55;
  --color-star:#f5a623;
  --radius-lg:16px;
  --radius:12px;
  --radius-sm:8px;
  --shadow:0 8px 28px rgba(20,24,31,.07);
  --font: 'Poppins', 'Segoe UI', 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
  --max-width:1120px;
}
*{box-sizing:border-box; margin:0; padding:0; overflow-wrap:break-word;}
html{ overflow-x:hidden; width:100%; }
body{ font-family:var(--font) !important; color:var(--color-text); background:var(--color-bg); line-height:1.55; -webkit-font-smoothing:antialiased; overflow-x:hidden; width:100%; }
img{max-width:100%; display:block;}
.wrap{max-width:var(--max-width); margin:0 auto; padding:0 20px;}
a{color:inherit;}
.topbar{ background:var(--color-text); color:#fff; text-align:center; font-size:13px; font-weight:700; padding:11px 12px; }
.rating-strip{ text-align:center; padding:20px 16px 0; }
.rating-strip .stars{ color:var(--color-star); font-size:18px; letter-spacing:2px; }
.rating-strip .rating-text{ font-size:14px; color:var(--color-text-muted); margin-top:6px; font-weight:600; }
.rating-strip .rating-text strong{ color:var(--color-text); }
.hero{ padding:22px 0 12px; text-align:center; }
.gift-strip{ display:inline-block; background:var(--color-blue-bg); color:var(--color-highlight); font-size:13px; font-weight:700; padding:9px 18px; border-radius:999px; margin-bottom:18px; }
.hero h1{ font-family:var(--font) !important; font-size:27px; font-weight:800 !important; line-height:1.28; margin-bottom:14px; max-width:600px; margin-left:auto; margin-right:auto; }
.hero h1 .hl{ color:var(--color-highlight) !important; font-weight:800 !important; }
.hero h1.h1-desktop-only{ display:none; }
.hero .lead{ font-size:15.5px; color:var(--color-text-muted); max-width:520px; margin:0 auto 22px; }
.hero .lead strong{ color:var(--color-text); font-weight:700; }
.hero-image{ border-radius:var(--radius-lg); overflow:hidden; margin-bottom:22px; }
.hero-image img{ width:100%; height:auto; display:block; }
.hero-image-desktop-only{ display:none; }
.price-block{ margin-bottom:18px; }
.price-block .was{ font-size:16px; color:#a3aab5; text-decoration:line-through; font-weight:600; }
.price-block .now{ font-size:38px; font-weight:800; color:var(--color-accent); margin:0 8px; }
.price-block .pct{ display:inline-block; background:var(--color-accent); color:#fff; font-size:13px; font-weight:800; padding:4px 12px; border-radius:999px; vertical-align:middle; }
.cta-btn{ display:block; width:100%; background:var(--color-accent); color:#fff; border:none; font-family:var(--font); font-size:16px; font-weight:800; padding:17px; border-radius:var(--radius-sm); text-align:center; text-decoration:none; cursor:pointer; }
.cta-btn:active{ background:var(--color-accent-dark); }
.cta-inline{ max-width:420px; margin:22px auto 0; }
.form-note{ font-size:12px; color:var(--color-text-muted); text-align:center; margin-top:10px; }
.feature-row{ display:grid; grid-template-columns:1fr 1fr; gap:16px; padding:28px 0; }
.feature-item{ text-align:center; padding:16px 10px; background:var(--color-bg-alt); border-radius:var(--radius); }
.feature-item .ico{ font-size:26px; margin-bottom:8px; }
.feature-item h4{ font-size:14px; font-weight:700; margin-bottom:4px; }
.feature-item p{ font-size:12.5px; color:var(--color-text-muted); }
.order-section{ padding:32px 0; background:var(--color-bg-alt); }
.order-card{ background:#fff; border-radius:var(--radius-lg); box-shadow:var(--shadow); padding:26px 22px; max-width:480px; margin:0 auto; }
.order-card h2{ font-family:var(--font) !important; font-size:21px; font-weight:800 !important; text-align:center; margin-bottom:8px; }
.order-card > p{ font-size:14px; color:var(--color-text-muted); text-align:center; margin-bottom:20px; }
.urgency-strip{ max-width:480px; margin:0 auto 18px; background:linear-gradient(180deg,#fff,#fff8f7); border:2px solid var(--color-accent); border-radius:var(--radius-lg); padding:22px 20px; box-shadow:0 4px 20px rgba(226,35,26,.12); }
.countdown-row{ text-align:center; margin-bottom:18px; }
.countdown-label{ font-size:12.5px; font-weight:700; text-transform:uppercase; letter-spacing:.6px; color:var(--color-text-muted); margin-bottom:8px; }
.countdown-timer{ display:flex; justify-content:center; gap:8px; }
.countdown-timer .box{ background:var(--color-text); color:#fff; border-radius:8px; padding:8px 4px; min-width:52px; text-align:center; }
.countdown-timer .box .num{ font-size:24px; font-weight:800; font-variant-numeric:tabular-nums; line-height:1; }
.countdown-timer .box .lbl{ font-size:9px; text-transform:uppercase; letter-spacing:.4px; color:#aab0bb; margin-top:2px; }
.countdown-timer .sep{ font-size:24px; font-weight:800; color:var(--color-accent); align-self:center; }
.stock-row{ margin-bottom:16px; }
.stock-row .stock-label{ display:flex; justify-content:space-between; align-items:center; gap:8px; font-size:13.5px; font-weight:700; margin-bottom:8px; flex-wrap:nowrap; }
.stock-row .stock-label .left{ color:var(--color-text); min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.stock-row .stock-label .right{ color:var(--color-accent); font-weight:700; flex:0 0 auto; white-space:nowrap; text-align:right; }
.stock-bar{ height:10px; background:var(--color-border); border-radius:999px; overflow:hidden; }
.stock-bar-fill{ height:100%; width:91%; border-radius:999px; background:linear-gradient(90deg,var(--color-accent-dark),var(--color-accent)); }
.live-row{ display:flex; align-items:center; justify-content:center; gap:8px; font-size:14px; font-weight:600; color:var(--color-text); padding-top:14px; border-top:1px dashed #f0c4c1; }
.live-row .dot{ display:inline-block; width:9px; height:9px; border-radius:50%; background:var(--color-success); animation:pulse 1.5s infinite; flex:0 0 9px; }
.live-row strong{ color:var(--color-accent); font-weight:800; }
@keyframes pulse{ 0%{ box-shadow:0 0 0 0 rgba(31,157,85,.5); } 70%{ box-shadow:0 0 0 7px rgba(31,157,85,0); } 100%{ box-shadow:0 0 0 0 rgba(31,157,85,0); } }
.order-form input{ width:100%; padding:15px 14px; margin-bottom:10px; border:1px solid var(--color-border); border-radius:var(--radius-sm); font-size:15px; font-family:var(--font); background:#fff; }
.order-form input:focus{ outline:none; border-color:var(--color-highlight); }
.order-form br{ display:none; }
.why-block{ padding:32px 0; border-bottom:1px solid var(--color-border); }
.why-grid{ display:grid; grid-template-columns:1fr; gap:20px; align-items:center; }
.why-block .num-eyebrow{ font-size:13.5px; font-weight:700; color:var(--color-accent); text-transform:uppercase; letter-spacing:.5px; margin-bottom:10px; }
.why-block img{ width:100%; border-radius:var(--radius-lg); display:block; }
.why-block h3{ font-family:var(--font) !important; font-size:22px; font-weight:800 !important; margin-bottom:12px; line-height:1.3; }
.why-block .tag-row{ display:flex; flex-wrap:wrap; gap:10px 12px; margin-bottom:16px; }
.why-block .tag{ display:inline-flex; align-items:center; gap:7px; font-size:14px; font-weight:700; color:var(--color-text); background:var(--color-bg-alt); padding:8px 15px; border-radius:999px; white-space:nowrap; flex:0 0 auto; }
.why-block .tag:before{ content:""; width:7px; height:7px; border-radius:50%; background:var(--color-accent); flex:0 0 7px; }
.why-block p{ font-size:16px; color:var(--color-text-muted); }
.why-block p.italic{ font-style:italic; margin-top:10px; }
.why-block .cta-inline{ margin-left:0; }
.compare{ padding:32px 0; }
.compare > .section-label{ font-size:12px; font-weight:700; color:var(--color-accent); text-transform:uppercase; text-align:center; margin-bottom:6px; }
.compare > h2{ font-family:var(--font) !important; font-size:22px; font-weight:800 !important; text-align:center; margin-bottom:20px; }
.compare table{ width:100%; border-collapse:collapse; font-size:14px; max-width:760px; margin:0 auto; }
.compare th{ padding:12px 6px; background:var(--color-bg-alt); font-size:12px; font-weight:700; }
.compare th.highlight{ color:var(--color-accent); }
.compare td{ padding:12px 6px; border-bottom:1px solid var(--color-border); text-align:center; }
.compare td:first-child{ text-align:left; font-weight:700; font-size:12px; }
.compare td.win{ color:var(--color-success); font-weight:700; }
.testimonials{ padding:36px 0; background:var(--color-bg-alt); }
.testimonials > .section-heading{ text-align:center; margin-bottom:26px; }
.testimonials > .section-heading h2{ font-family:var(--font) !important; font-size:22px; font-weight:800 !important; max-width:640px; margin:0 auto; }
.t-grid{ display:grid; grid-template-columns:1fr; gap:24px; }
.testimonial{ border:1px solid var(--color-border); border-radius:var(--radius-lg); overflow:hidden; background:#fff; }
.testimonial .t-photo{ width:100%; aspect-ratio:1/1; object-fit:contain; object-position:center; background:var(--color-bg-alt); display:block; }
.testimonial .t-photo--empty{ border-bottom:1px solid var(--color-border); }
.testimonial .t-body{ padding:18px 20px 20px; }
.testimonial .author-row{ display:flex; align-items:center; gap:10px; margin-top:12px; }
.testimonial .avatar{ flex:0 0 auto; width:36px; height:36px; border-radius:50%; object-fit:cover; border:1px solid var(--color-border); }
.testimonial .stars{ color:var(--color-star); font-size:14px; margin-bottom:6px; }
.testimonial h4{ font-size:17px; font-weight:700; margin-bottom:8px; }
.testimonial p{ font-size:15px; color:var(--color-text-muted); margin-bottom:0; }
.testimonial .author{ font-size:14px; font-weight:700; }
.kit-section{ padding:32px 0; }
.section-heading{ text-align:center; margin-bottom:28px; }
.section-heading .eyebrow{ display:inline-block; font-size:12.5px; font-weight:700; color:var(--color-highlight); text-transform:uppercase; letter-spacing:.8px; margin-bottom:12px; background:var(--color-blue-bg); padding:6px 16px; border-radius:999px; }
.section-heading h2{ font-family:var(--font) !important; font-size:25px; font-weight:800 !important; line-height:1.32; max-width:560px; margin:0 auto; }
.kit-box{ display:grid; grid-template-columns:1fr; gap:0; align-items:start; max-width:900px; margin:0 auto; background:#fff; border:2px solid var(--color-border); border-radius:var(--radius-lg); overflow:hidden; }
.kit-box img{ width:100%; height:auto; display:block; }
.kit-box .kit-content{ padding:26px 22px; text-align:center; }
.kit-box h3{ font-family:var(--font) !important; font-size:19px; font-weight:800 !important; margin-bottom:14px; }
.kit-box ul{ list-style:none; text-align:left; max-width:380px; margin:0 auto 20px; }
.kit-box li{ font-size:14.5px; padding:6px 0; display:flex; gap:8px; }
.kit-box li:before{ content:"✓"; color:var(--color-success); font-weight:800; }
.faq{ padding:12px 0 40px; max-width:720px; margin:0 auto; }
.faq > .section-heading{ margin-bottom:18px; }
.faq-item{ border-bottom:1px solid var(--color-border); }
.faq-q{ width:100%; background:none; border:none; text-align:left; font-size:15px; font-weight:700; padding:16px 0; display:flex; justify-content:space-between; align-items:flex-start; gap:12px; cursor:pointer; color:var(--color-text); font-family:var(--font); }
.faq-q span:first-child{ flex:1; min-width:0; }
.faq-q .arrow{ flex:0 0 auto; margin-top:2px; font-size:13px; color:var(--color-text-muted); transition:transform .2s; }
.faq-item.open .faq-q .arrow{ transform:rotate(180deg); }
.faq-a{ max-height:0; overflow:hidden; transition:max-height .25s ease; font-size:14.5px; color:var(--color-text-muted); }
.faq-item.open .faq-a{ max-height:260px; padding-bottom:16px; }
@media (min-width:960px){
  :root{ --max-width:1120px; }
  .hero{ display:grid; grid-template-columns:1fr 1fr; gap:56px; align-items:center; text-align:left; padding:48px 0; }
  .hero-copy{ order:1; }
  .hero-image{ order:2; margin-bottom:0; }
  .hero-image-mobile-only{ display:none; }
  .hero-image-desktop-only{ display:block; }
  .gift-strip{ margin-left:0; }
  .hero h1{ font-size:38px; margin-left:0; text-align:left; }
  .hero h1.h1-mobile-only{ display:none; }
  .hero h1.h1-desktop-only{ display:block; }
  .hero .lead{ margin-left:0; text-align:left; }
  .price-block{ text-align:left; }
  .feature-row{ grid-template-columns:repeat(4,1fr); }
  .why-grid{ grid-template-columns:1fr 1fr; gap:40px; }
  .why-block:nth-child(even) .why-img{ order:2; }
  .t-grid{ grid-template-columns:repeat(3,1fr); }
  .kit-box{ grid-template-columns:280px 1fr; text-align:left; align-items:stretch; }
  .kit-box img{ height:100%; object-fit:cover; }
  .kit-box .kit-content{ text-align:left; }
  .kit-box ul{ margin-left:0; }
}"""

BODY = r"""
  <div class="topbar">SOLO OGGI: -70% + SPEDIZIONE GRATUITA — PAGAMENTO ALLA CONSEGNA</div>

  <div class="rating-strip wrap">
    <div class="stars">★★★★★</div>
    <div class="rating-text"><strong>4,9/5</strong> — Oltre <strong>9.480</strong> persone in Italia si asciugano i vestiti più velocemente ogni giorno</div>
  </div>

  <!-- ===== HERO ===== -->
  <section class="hero wrap">
    <div class="hero-copy">
      <span class="gift-strip">Risparmi fino al 60% in bolletta + Garanzia 3 anni</span>
      <h1>Asciuga e distende fino a 20 kg di bucato in soli 30 minuti, consumando fino al 60% in meno.</h1>
      <p class="lead"><strong>Dochura</strong> — Ascugatrice portatile pieghevole con camera chiusa e cerniera: appendi i capi dentro, l'elemento riscaldante e la ventola fanno circolare aria calda, l'umidità esce dalle griglie di ventilazione. Timer integrato, spegnimento automatico.</p>

      <div class="hero-image hero-image-mobile-only">
        <img src="/assets/img/products/dochura/hero.webp" alt="Dochura in lavanderia — asciugatrice portatile con camera chiusa" width="560" height="560" loading="eager" fetchpriority="high" decoding="async">
      </div>

      <div class="price-block">
        <span class="was">79€</span>
        <span class="now">34€</span>
        <span class="pct">-70%</span>
      </div>

      <a href="#order-form" class="cta-btn">SÌ, VOGLIO DOCHURA →</a>
      <p class="form-note">🔒 Zero anticipo · Zero carta · Paghi solo quando lo ricevi</p>
    </div>

    <div class="hero-image hero-image-desktop-only">
      <img src="/assets/img/products/dochura/hero.webp" alt="Dochura in lavanderia — asciugatrice portatile con camera chiusa" width="560" height="560" loading="eager" fetchpriority="high" decoding="async">
    </div>
  </section>
  <!-- Img1: Dochura su sfondo bianco, camera chiusa con cerniera, griglie di ventilazione visibili, prodotto compatto -->

  <div class="wrap">
    <div class="feature-row">
      <div class="feature-item"><div class="ico">🚚</div><h4>Spedizione gratuita</h4><p>Consegna in tutta Italia</p></div>
      <div class="feature-item"><div class="ico">💳</div><h4>Paghi alla consegna</h4><p>Nessuna carta richiesta</p></div>
      <div class="feature-item"><div class="ico">🛡️</div><h4>Garanzia 3 anni</h4><p>Copertura completa inclusa</p></div>
      <div class="feature-item"><div class="ico">↩️</div><h4>Reso 30 giorni</h4><p>Rimborso pieno, senza domande</p></div>
    </div>
  </div>

  <!-- ===== ORDER FORM ===== -->
  <section class="order-section" id="order-form">
    <div class="wrap">
      <div class="urgency-strip">
        <div class="countdown-row">
          <div class="countdown-label">⏰ Prezzo -70% bloccato ancora per</div>
          <div class="countdown-timer" id="countdownTimer">
            <div class="box"><div class="num" id="cd-h">00</div><div class="lbl">Ore</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-m">14</div><div class="lbl">Min</div></div>
            <div class="sep">:</div>
            <div class="box"><div class="num" id="cd-s">59</div><div class="lbl">Sec</div></div>
          </div>
        </div>

        <div class="stock-row">
          <div class="stock-label">
            <span class="left">Disponibilità magazzino</span>
            <span class="right">Solo 4 pezzi rimasti</span>
          </div>
          <div class="stock-bar"><div class="stock-bar-fill"></div></div>
        </div>

        <div class="live-row">
          <span class="dot"></span>
          <span id="liveCount" data-live="<strong>{n} persone</strong> stanno guardando Dochura ora"><strong>38 persone</strong> stanno guardando Dochura ora</span>
        </div>
      </div>

      <div class="order-card">
        <h2>Blocca il tuo Dochura a 34€</h2>
        <p>Compila i campi qui sotto. Ti chiamiamo entro 24h per confermare la consegna — nessun addebito prima.</p>
        <form class="tm-order-form order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
          <input type="text" name="name" autocomplete="name" placeholder="Nome e Cognome" required>
          <input type="tel" name="tel" autocomplete="tel" placeholder="Numero di telefono" required>
          <input type="text" name="street-address" autocomplete="street-address" placeholder="Indirizzo di consegna" required>
          <input name="uid" type="hidden" value="INSERISCI_UID" />
          <input name="offer" type="hidden" value="INSERISCI_OFFER_ID" />
          <input name="lp" type="hidden" value="INSERISCI_LP_ID" />
          <input name="subid" id="subid" type="hidden" value="" />
          <input name="tmfp" id="tmfp" type="hidden" value="" />
          <input name="thankyoupage" type="hidden" value="INSERISCI_URL_THANKYOU"/>
          <input name="webhook" type="hidden" value="INSERISCI_URL_WEBHOOK"/>
          <input name="_key" type="hidden" value="INSERISCI_KEY" />
          <button type="submit" class="cta-btn">SÌ, ORDINO DOCHURA</button>
          <p class="form-note">🔒 Zero anticipo · Zero carta · Paghi solo quando lo ricevi</p>
          <script>
            document.addEventListener("DOMContentLoaded", function () {
              var params = new URLSearchParams(window.location.search);
              var campaign = params.get("utm_campaign") || "";
              var subidInput = document.querySelector('input[name="subid"]');
              if (subidInput) { subidInput.value = campaign; }
            });
          </script>
          <script src="https://offers.adricenetwork.com/forms/tmfp/" crossorigin="anonymous" defer></script>
          <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== WHY BLOCKS (4 benefici) ===== -->
  <section class="why-block wrap">
    <div class="why-grid">
      <div class="why-img">
        <video class="dochura-video" src="/assets/video/dochura/funzionamento.mp4" autoplay muted loop playsinline preload="metadata" disablepictureinpicture controlslist="nodownload nofullscreen noremoteplayback"></video>
      </div>
      <!-- Video1: sequenza funzionamento — apertura cerniera, appendere capi, chiusura camera, accensione, aria calda in circolo, vapore che esce dalle griglie, timer che scende -->
      <div>
        <div class="num-eyebrow">01 — Come funziona Dochura: passo dopo passo</div>
        <h3>Camera chiusa, aria calda in circolo, umidità fuori — spegnimento automatico col timer</h3>
        <div class="tag-row"><span class="tag">Camera chiusa</span><span class="tag">Aria calda</span><span class="tag">Timer auto</span></div>
        <p>Apri la cerniera, appendi i capi all'interno e chiudi la camera. L'elemento riscaldante e la ventola fanno girare aria calda in modo uniforme, l'umidità esce dalle pannelli di ventilazione laterali.</p>
        <p class="italic">Imposti il timer e te ne dimentichi: al termine del ciclo Dochura si spegne da sola, senza rischi di capi lasciati troppo a lungo.</p>
      </div>
    </div>
  </section>

  <section class="why-block wrap">
    <div class="why-grid">
      <div class="why-img"><img src="/assets/img/products/dochura/desc-2.webp" alt="Dochura — circolazione aria calda 360° per asciugatura completa" loading="lazy" decoding="async"></div>
      <!-- Img2: confronto visivo capo asciugato solo in superficie vs capo asciugato in profondità con Dochura -->
      <div>
        <div class="num-eyebrow">02 — Non è la lavatrice il problema</div>
        <h3>Asciugatura completa, non solo in superficie — addio odore di umido</h3>
        <div class="tag-row"><span class="tag">Asciugatura profonda</span><span class="tag">Meno odore</span><span class="tag">Più igiene</span></div>
        <p>Stendere i vestiti in casa o sullo stendino spesso li fa sembrare asciutti fuori, ma restano umidi nelle pieghe e nelle cuciture. Con il tempo arrivano l'odore sgradevole e quella sensazione di «non proprio pulito».</p>
        <p class="italic">Dochura fa circolare aria calda dentro la camera chiusa e raggiunge anche le zone più difficili, così i capi sono davvero pronti da indossare o da riporre nell'armadio.</p>
      </div>
    </div>
  </section>

  <section class="why-block wrap">
    <div class="why-grid">
      <div class="why-img"><img src="/assets/img/products/dochura/desc-3.webp" alt="Dochura funziona indipendentemente dal meteo" loading="lazy" decoding="async"></div>
      <!-- Img3: prodotto acceso in bagno o lavanderia con pioggia/finestra sullo sfondo, capi che si asciugano -->
      <div>
        <div class="num-eyebrow">03 — Niente sole, niente balcone</div>
        <h3>Funziona con qualsiasi tempo — pioggia, inverno o umidità estiva</h3>
        <div class="tag-row"><span class="tag">Indipendente dal meteo</span><span class="tag">Circolazione uniforme</span><span class="tag">Sempre disponibile</span></div>
        <p>Non devi più organizzare la giornata in base al sole o al vento. Dochura asciuga quando vuoi tu: la sera, di notte, con il cielo coperto o quando fuori piove da giorni.</p>
        <p class="italic">L'aria calda si muove dentro la camera chiusa in modo costante, così non dipendi dalle condizioni fuori casa e non resti con il bucato fermo per giorni.</p>
      </div>
    </div>
  </section>

  <section class="why-block wrap" style="border-bottom:none;">
    <div class="why-grid">
      <div class="why-img"><img src="/assets/img/products/dochura/desc-4.webp?v=2" alt="Dochura piegata e portatile per viaggi" loading="lazy" decoding="async"></div>
      <!-- Img4: prodotto piegato e riposto in un armadio sottile, oppure in valigia per viaggio -->
      <div>
        <div class="num-eyebrow">04 — Si piega, si ripara, sparisce</div>
        <h3>Compatta per monolocali, viaggi e campeggio — pronta quando serve</h3>
        <div class="tag-row"><span class="tag">Pieghevole</span><span class="tag">Poco ingombro</span><span class="tag">Portatile</span></div>
        <p>Quando hai finito, Dochura si piega e la riponi in un armadio, sotto il letto o in un ripostiglio. Non serve uno stendino che occupa mezzo soggiorno né un balcone sempre pieno di bucato.</p>
        <p class="italic">Ideale per appartamenti piccoli, seconde case, viaggi lunghi o campeggio: porti con te un modo semplice per avere capi asciutti senza dipendere da spazio esterno.</p>
        <a href="#order-form" class="cta-btn cta-inline">SÌ, VOGLIO DOCHURA →</a>
      </div>
    </div>
  </section>

  <!-- ===== COMPARE ===== -->
  <section class="compare wrap">
    <div class="section-label">Confronto diretto</div>
    <h2>Asciugatura tradizionale vs Dochura</h2>
    <table>
      <tr><th></th><th>Senza Dochura</th><th class="highlight">Con Dochura</th></tr>
      <tr><td>Tempo di asciugatura</td><td>Giorni, dipende da meteo e spazio</td><td class="win">Ciclo guidato in camera chiusa, più prevedibile</td></tr>
      <tr><td>Dipendenza dal meteo</td><td>Sole, vento e umidità esterna</td><td class="win">Funziona sempre, anche con pioggia o in inverno</td></tr>
      <tr><td>Odore di umidità</td><td>Capo che sembra asciutto ma resta umido dentro</td><td class="win">Circolazione di aria calda, meno odore di chiuso</td></tr>
      <tr><td>Spazio in casa</td><td>Stendini, balcone, sedie piene di bucato</td><td class="win">Camera chiusa compatta, si piega e si ripone</td></tr>
    </table>
  </section>

  <!-- ===== TESTIMONIALS ===== -->
  <section class="testimonials">
    <div class="wrap">
      <div class="section-heading">
        <h2>Oltre 9.480 persone in Italia hanno scelto Dochura. Ecco cosa dicono.</h2>
      </div>
      <div class="t-grid">
        <div class="testimonial">
          <img class="t-photo" src="/assets/img/reviews/dochura/review-1.webp" alt="Dochura in lavanderia con capi appesi" loading="lazy" decoding="async">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <h4>Finalmente niente più odore di umido nei capi.</h4>
            <p>«Prima sembravano asciutti sullo stendino, ma restavano umidi nelle pieghe. Con Dochura li appendo dentro, imposto il timer e li trovo davvero pronti da mettere nell'armadio.»</p>
            <div class="author-row">
              <img class="avatar" src="/assets/img/reviews/dochura/avatar-1.webp" alt="Roberto G., cliente verificato" width="42" height="42" loading="lazy" decoding="async">
              <div class="author">Roberto G. — Cliente verificato</div>
            </div>
          </div>
        </div>
        <div class="testimonial">
          <img class="t-photo" src="/assets/img/reviews/dochura/review-2.webp" alt="Dochura in monolocale con pioggia fuori" loading="lazy" decoding="async">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <h4>Con la pioggia fuori, a casa il bucato non si ferma più.</h4>
            <p>«Vivo in un monolocale senza balcone: quando pioveva per giorni restavo bloccata con montagne di vestiti umidi. Ora accendo Dochura la sera e al mattino sono asciutti.»</p>
            <div class="author-row">
              <img class="avatar" src="/assets/img/reviews/dochura/avatar-2.webp" alt="Davide M., cliente verificato" width="42" height="42" loading="lazy" decoding="async">
              <div class="author">Davide M. — Cliente verificato</div>
            </div>
          </div>
        </div>
        <div class="testimonial">
          <img class="t-photo" src="/assets/img/reviews/dochura/review-3.webp" alt="Dochura piegata riposta sotto il letto" loading="lazy" decoding="async">
          <div class="t-body">
            <div class="stars">★★★★★</div>
            <h4>Si piega e sparisce — perfetta per un appartamento piccolo.</h4>
            <p>«Non volevo uno stendino che occupa mezzo soggiorno. Dochura la uso, la chiudo e la ripongo sotto il letto. In viaggio me la porto dietro senza problemi.»</p>
            <div class="author-row">
              <img class="avatar" src="/assets/img/reviews/dochura/avatar-3.webp" alt="Marta T., cliente verificata" width="42" height="42" loading="lazy" decoding="async">
              <div class="author">Marta T. — Cliente verificata</div>
            </div>
          </div>
        </div>
      </div>

      <!-- CTA aggiunta 2 — dopo l'ultima recensione -->
      <a href="#order-form" class="cta-btn cta-inline">SÌ, VOGLIO DOCHURA →</a>
    </div>
  </section>

  <!-- ===== KIT BOX ===== -->
  <section class="kit-section wrap">
    <div class="section-heading">
      <span class="eyebrow">Nella confezione</span>
      <h2>Kit completo Dochura, pronto da usare subito</h2>
    </div>
    <div class="kit-box">
      <img src="/assets/img/products/dochura/kit.webp" alt="Dochura in uso in lavanderia" loading="lazy" decoding="async">
      <!-- Img9: Dochura piegata + cavo di alimentazione + grucce o accessori disposti su sfondo bianco -->
      <div class="kit-content">
        <div class="price-block" style="margin-bottom:16px;">
          <span class="was">79€</span>
          <span class="now">34€</span>
          <span class="pct">-70%</span>
        </div>
        <ul>
          <li>1× Dochura — asciugatrice portatile pieghevole con camera chiusa e timer</li>
          <li>1× Cavo di alimentazione</li>
          <li>1× Set di ganci interni per appendere i capi</li>
          <li>1× Borsa o custodia per riporre il prodotto piegato</li>
          <li>Garanzia ufficiale di 3 anni</li>
        </ul>
        <a href="#order-form" class="cta-btn">SÌ, VOGLIO DOCHURA →</a>
      </div>
    </div>
  </section>

  <!-- ===== FAQ ===== -->
  <section class="faq wrap">
    <div class="section-heading">
      <h2>Domande frequenti</h2>
    </div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Quanto ci mette ad arrivare?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>1-2 giorni lavorativi in tutta Italia. Ti chiamiamo entro 24 ore per confermare l'ordine e l'orario di consegna.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Devo pagare in anticipo?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>No. Paghi in contanti direttamente al corriere quando Dochura è già a casa tua. Nessuna carta, nessun addebito prima.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Che tipi di tessuto posso asciugare?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Dochura è adatta a magliette, felpe, intimo, asciugamani, pigiama e capi del quotidiano. Per lana, seta o materiali molto delicati, controlla sempre l'etichetta del capo e usa cicli brevi.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Fa molto rumore?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Il rumore è paragonabile a quello di un ventilatore domestico: puoi usarla in lavanderia, bagno o camera da letto senza disturbare eccessivamente.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Quanto consuma di elettricità?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Dochura è pensata per un uso domestico quotidiano con consumo contenuto. Il timer ti aiuta a evitare cicli più lunghi del necessario.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>E se non mi convince?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Hai 30 giorni per restituirlo gratuitamente e ricevere il rimborso completo, senza domande.</p></div></div>
    <div class="faq-item"><button class="faq-q" type="button"><span>Ok, sono convinto. Come lo ordino?</span><span class="arrow">▾</span></button>
      <div class="faq-a"><p>Compila il modulo qui sopra con nome, telefono e indirizzo. Ti chiamiamo entro 24h per confermare, e Dochura arriva a casa tua in 1-2 giorni. Paghi solo alla consegna.</p></div></div>
  </section>


<script>
  (function(){
    const end = Date.now() + 15*60*1000;
    function tick(){
      const diff = Math.max(0, end - Date.now());
      const h = Math.floor(diff/3600000);
      const m = Math.floor((diff%3600000)/60000);
      const s = Math.floor((diff%60000)/1000);
      document.getElementById('cd-h').textContent = String(h).padStart(2,'0');
      document.getElementById('cd-m').textContent = String(m).padStart(2,'0');
      document.getElementById('cd-s').textContent = String(s).padStart(2,'0');
      if(diff>0) setTimeout(tick,1000);
    }
    tick();
  })();

  (function(){
    let count = 38;
    const el = document.getElementById('liveCount');
    setInterval(()=>{
      count += (Math.random() > 0.5 ? 1 : -1) * Math.ceil(Math.random()*2);
      count = Math.min(46, Math.max(32, count));
      el.innerHTML = `<strong>${count} persone</strong> stanno guardando Dochura ora`;
    }, 2000);
  })();

  document.querySelectorAll('.faq-item').forEach(item=>{
    item.querySelector('.faq-q').addEventListener('click', ()=>{
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
      if(!isOpen) item.classList.add('open');
    });
  });
</script>
"""

LANDING_HEAD = """<!DOCTYPE html>
<html lang="it">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18510622150"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-18510622150');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Dochura — Asciuugatrice portatile pieghevole | Pagamento alla consegna</title>
<meta name="description" content="Dochura: asciugatrice portatile pieghevole con camera chiusa, aria calda e timer. Asciuga i capi in profondità senza dipendere dal meteo. Pagamento alla consegna in tutta Italia.">
<meta name="contact" content="info@shoptrendcrest.com">
<meta name="theme-color" content="#14181f">
<link rel="canonical" href="https://shoptrendcrest.com/it/dochura/landing.html">
<link rel="alternate" hreflang="it" href="https://shoptrendcrest.com/it/dochura/landing.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/glacierair-landing.css">
<style>.cta-inline{max-width:420px;margin:22px auto 0}.t-photo--empty{display:block;width:100%;aspect-ratio:1/1;background:var(--color-bg-alt);border-bottom:1px solid var(--color-border)}.why-img video.dochura-video{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;border-radius:var(--radius-lg);background:#000;pointer-events:none}</style>
<script>
window.SITE_CONFIG = {
  GEO: 'it',
  PRODUCT_SLUG: 'dochura',
  CURRENCY: 'EUR',
  PRICE: 34.00,
  OFFER_NAME: 'Dochura IT',
  LP_ID: 'it-dochura',
  COOKIE_TEXT: 'Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.',
  COOKIE_ACCEPT: 'Accetta',
  COOKIE_LEARN: 'Scopri di più'
};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body>
"""

LANDING_FOOTER = """
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a href="/" class="site-logo" aria-label="shoptrendcrest.com home">
          <span class="site-logo__text"><span class="site-logo__text-primary">shoptrendcrest</span><span class="site-logo__text-accent">.com</span></span>
        </a>
        <p class="site-footer__blurb">Prodotti utili per la vita quotidiana, consegna in 24-48 ore con pagamento alla consegna.</p>
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
          <li><strong>WHATECH MOBILE CO., LIMITED</strong></li>
          <li>Room 505, 5th floor, Beverley Commercial Centre</li>
          <li>87-105 Chatham Road South</li>
          <li>Tsim Sha Tsui</li>
          <li>Kowloon</li>
          <li>Hong Kong</li>
          <li><a href="mailto:info@shoptrendcrest.com">info@shoptrendcrest.com</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      © <span data-year>2026</span> <strong>WHATECH MOBILE CO., LIMITED</strong> — Tutti i diritti riservati.
      <a href="/">shoptrendcrest.com</a>
    </div>
  </div>
</footer>

<script src="/assets/js/glacierair-landing.js" defer></script>
<script>
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
</script>
</body>
</html>
"""


def landing_body() -> str:
    body = BODY.strip()
    marker = "\n\n<script>\n  (function(){\n    const end = Date.now()"
    if marker in body:
        body = body[: body.index(marker)]
    body = body.replace('value="INSERISCI_URL_THANKYOU"', f'value="{THANKYOU_URL}"')
    return body


def build_landing_html() -> str:
    return LANDING_HEAD + landing_body() + LANDING_FOOTER


HTML = f"""<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Dochura — Asciughino portatile pieghevole | Pagamento alla consegna</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{BODY}
</body>
</html>"""


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    data["content"][0]["elements"][0]["settings"]["html"] = HTML
    data["title"] = "TEMPLATE 4 BENEFITS — Dochura"
    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    HTML_OUT.write_text(HTML, encoding="utf-8")
    landing = build_landing_html()
    LANDING_OUT.write_text(landing, encoding="utf-8")
    print(f"Updated {OUT}")
    print(f"Preview HTML: {HTML_OUT}")
    print(f"Landing HTML: {LANDING_OUT}")
    print(f"HTML length: {len(HTML)}")


if __name__ == "__main__":
    main()
