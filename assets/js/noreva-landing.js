(function () {
  const end = Date.now() + 15 * 60 * 1000;
  function tick() {
    const diff = Math.max(0, end - Date.now());
    const h = Math.floor(diff / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);
    const hEl = document.getElementById('cd-h');
    const mEl = document.getElementById('cd-m');
    const sEl = document.getElementById('cd-s');
    if (hEl) hEl.textContent = String(h).padStart(2, '0');
    if (mEl) mEl.textContent = String(m).padStart(2, '0');
    if (sEl) sEl.textContent = String(s).padStart(2, '0');
    if (diff > 0) setTimeout(tick, 1000);
  }
  tick();
})();

(function () {
  function pickFromPipeForms(n, pipe) {
    if (!pipe) return '';
    var forms = pipe.split('|');
    if (forms.length < 2) return forms[0] || '';
    var mod100 = n % 100;
    var mod10 = n % 10;
    if (mod10 === 1 && mod100 !== 11) return forms[0];
    if (mod10 === 2 && mod100 !== 12) return forms[1];
    if ((mod10 === 3 || mod10 === 4) && mod100 !== 13 && mod100 !== 14) {
      return forms[2] || forms[forms.length - 1];
    }
    return forms[forms.length - 1];
  }

  let count = 34;
  const el = document.getElementById('liveCount');
  if (!el) return;
  const cfg = window.SITE_CONFIG || {};
  const tpl = cfg.LIVE_TPL || el.getAttribute('data-live') || '<strong>{n} persone</strong> stanno guardando questo set adesso';
  const unitPipe = cfg.LIVE_UNITS || el.getAttribute('data-live-units') || '';
  function render() {
    var out = tpl.replace('{n}', String(count));
    if (out.indexOf('{unit}') !== -1) {
      out = out.replace('{unit}', pickFromPipeForms(count, unitPipe));
    }
    el.innerHTML = out;
  }
  render();
  setInterval(function () {
    count += (Math.random() > 0.5 ? 1 : -1) * Math.ceil(Math.random() * 2);
    count = Math.min(46, Math.max(32, count));
    render();
  }, 2000);
})();

document.querySelectorAll('.faq-item').forEach(function (item) {
  var btn = item.querySelector('.faq-q');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
      openItem.classList.remove('open');
    });
    if (!isOpen) item.classList.add('open');
  });
});

function isPlaceholderFormValue(value) {
  if (!value) return true;
  return value.indexOf('INSERISCI') !== -1;
}

function isNetworkFormReady(form) {
  if (form.classList.contains('order-form--blocked') || form.getAttribute('data-cendora-blocked') === '1') {
    return false;
  }
  var action = form.getAttribute('action') || '';
  if (action.indexOf('offers.adricenetwork.com') === -1) {
    return false;
  }
  var offer = form.querySelector('[name="offer"]');
  var lp = form.querySelector('[name="lp"]');
  var key = form.querySelector('[name="_key"]');
  return offer && lp && key
    && String(offer.value || '').trim() !== ''
    && String(lp.value || '').trim() !== ''
    && String(key.value || '').trim() !== ''
    && !isPlaceholderFormValue(offer.value)
    && !isPlaceholderFormValue(lp.value)
    && !isPlaceholderFormValue(key.value);
}

function wireOrderFormsFromConfig() {
  var cfg = window.SITE_CONFIG || {};
  var fieldMap = {
    uid: cfg.FORM_UID,
    offer: cfg.FORM_OFFER,
    lp: cfg.FORM_LP,
    webhook: cfg.FORM_WEBHOOK,
    _key: cfg.FORM_KEY,
    thankyoupage: cfg.THANKYOU_URL
  };

  document.querySelectorAll('.tm-order-form').forEach(function (form) {
    Object.keys(fieldMap).forEach(function (name) {
      if (!fieldMap[name]) return;
      var input = form.querySelector('[name="' + name + '"]');
      if (input) input.value = fieldMap[name];
    });
  });
}

function redirectToThankYou(form) {
  var tyInput = form.querySelector('[name="thankyoupage"]');
  var tyURL = (tyInput && tyInput.value) || ((window.SITE_CONFIG || {}).THANKYOU_URL) || '/it/valmora/thank-you.html';

  if (window.appendGadgetshifthubTrackingParams && window.getGadgetshifthubTrackingContext) {
    tyURL = window.appendGadgetshifthubTrackingParams(tyURL, window.getGadgetshifthubTrackingContext());
  }

  if (window.markGadgetshifthubCashboltSubmit) {
    window.markGadgetshifthubCashboltSubmit();
  }
  if (window.trackLead) {
    window.trackLead();
  }

  window.location.href = tyURL;
}

function showCendoraFormBlocked(form) {
  var msg = form.querySelector('.form-blocked-msg');
  if (!msg) {
    msg = document.createElement('p');
    msg.className = 'form-blocked-msg';
    msg.setAttribute('role', 'alert');
    msg.style.cssText =
      'color:#b91c1c;text-align:center;margin-top:12px;font-weight:600;line-height:1.45;';
    var btnWrap = form.querySelector('button[type="submit"]');
    if (btnWrap && btnWrap.parentElement) {
      btnWrap.parentElement.insertAdjacentElement('beforebegin', msg);
    } else {
      form.appendChild(msg);
    }
  }
  var cfg = window.SITE_CONFIG || {};
  var fromForm = form.getAttribute('data-cendora-blocked-msg');
  msg.textContent =
    fromForm ||
    cfg.FORM_BLOCKED_MSG ||
    'Online orders for this offer are temporarily unavailable. Email info@shoptrendcrest.com.';
  msg.hidden = false;
}

function wireTypFallbackForms() {
  document.querySelectorAll('.tm-order-form').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      if (isNetworkFormReady(form)) return;

      event.preventDefault();
      event.stopImmediatePropagation();

      if (document.body.classList.contains('cendora-lp')) {
        showCendoraFormBlocked(form);
        return;
      }

      if (!form.checkValidity()) return;

      var submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = (window.SITE_CONFIG || {}).SUBMITTING_LABEL || 'Invio in corso...';
      }

      redirectToThankYou(form);
    }, true);
  });
}

document.addEventListener('DOMContentLoaded', function () {
  wireOrderFormsFromConfig();
  wireTypFallbackForms();

  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
});
