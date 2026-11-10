/**
 * CENDORA™ — keep Adrice tm-order-form to exactly 3 visible inputs in order:
 * name → tel → street-address (Adrice js-v2 may reorder DOM after load).
 */
(function () {
  var ALLOWED = { name: true, tel: true, 'street-address': true };
  var STRIP_NAMES = ['address-level2', 'postal-code'];
  var FIELD_ORDER = ['name', 'tel', 'street-address'];

  function isVisibleInput(el) {
    if (!el || el.tagName !== 'INPUT') return false;
    if ((el.type || '').toLowerCase() === 'hidden') return false;
    var s = window.getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    return true;
  }

  function removeField(form, name) {
    var input = form.querySelector('input[name="' + name + '"]');
    if (!input || !isVisibleInput(input)) return;
    var label = form.querySelector('label[for="' + name + '"]');
    if (label) label.remove();
    input.remove();
  }

  function collectBlock(form, fieldName) {
    var input = form.querySelector('input[name="' + fieldName + '"]');
    if (!input || !isVisibleInput(input)) return [];
    var label = form.querySelector('label[for="' + input.id + '"]');
    var nodes = [];
    if (label) nodes.push(label);
    nodes.push(input);
    var sib = input.nextSibling;
    if (sib && sib.nodeName === 'BR') nodes.push(sib);
    return nodes;
  }

  function visibleFieldNames(form) {
    return Array.prototype.filter
      .call(form.querySelectorAll('input'), isVisibleInput)
      .map(function (el) {
        return el.getAttribute('name') || '';
      });
  }

  function placeholderFor(form, fieldName) {
    var input = form.querySelector('input[name="' + fieldName + '"]');
    if (input && input.getAttribute('data-cendora-placeholder')) {
      return input.getAttribute('data-cendora-placeholder');
    }
    var cfg = window.SITE_CONFIG && window.SITE_CONFIG.FORM_PLACEHOLDERS;
    if (cfg && cfg[fieldName]) return cfg[fieldName];
    return '';
  }

  function enforcePlaceholders(form) {
    FIELD_ORDER.forEach(function (fieldName) {
      var el = form.querySelector('input[name="' + fieldName + '"]');
      if (!el || !isVisibleInput(el)) return;
      var want = placeholderFor(form, fieldName);
      if (!want) return;
      if (el.placeholder !== want) {
        el.placeholder = want;
      }
    });
  }

  function enforceFieldOrder(form) {
    var have = visibleFieldNames(form);
    if (
      have.length === FIELD_ORDER.length &&
      FIELD_ORDER.every(function (n, i) {
        return have[i] === n;
      })
    ) {
      return;
    }
    var anchor = form.querySelector('input[name="uid"]');
    if (!anchor) return;
    FIELD_ORDER.forEach(function (fieldName) {
      collectBlock(form, fieldName).forEach(function (node) {
        form.insertBefore(node, anchor);
      });
    });
  }

  function enforceThreeFields(form) {
    if (!form || !form.classList.contains('tm-order-form')) return;
    STRIP_NAMES.forEach(function (name) {
      removeField(form, name);
    });
    var visible = Array.prototype.filter.call(
      form.querySelectorAll('input'),
      isVisibleInput
    );
    if (visible.length > 3) {
      visible.forEach(function (el) {
        var n = el.getAttribute('name') || '';
        if (!ALLOWED[n]) {
          var lbl = form.querySelector('label[for="' + el.id + '"]');
          if (lbl) lbl.remove();
          el.remove();
        }
      });
    }
    enforceFieldOrder(form);
    enforcePlaceholders(form);
  }

  function bindForm(form) {
    enforceThreeFields(form);
    if (form.__cendoraFormObs) return;
    form.__cendoraFormObs = true;
    var obs = new MutationObserver(function () {
      enforceThreeFields(form);
    });
    obs.observe(form, { childList: true, subtree: true });
  }

  function run() {
    document.querySelectorAll('form.tm-order-form').forEach(bindForm);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
  [400, 1500, 4000, 8000].forEach(function (ms) {
    setTimeout(run, ms);
  });
})();
