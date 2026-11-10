from pathlib import Path

from playwright.sync_api import sync_playwright
import json
import sys

url = sys.argv[1] if len(sys.argv) > 1 else "https://shoptrendcrest.com/es/granvia-3047/"
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1440, "height": 900})
    page.goto(url, wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(9000)
    data = page.evaluate(
        """() => {
      const f = document.querySelector('.tm-order-form');
      if (!f) return { err: 'no form' };
      const fields = ['name', 'tel', 'street-address'];
      const out = {};
      fields.forEach((n) => {
        const el = f.querySelector('input[name="' + n + '"]');
        const lab = el ? f.querySelector('label[for="' + el.id + '"]') : null;
        out[n] = {
          placeholder: el ? el.placeholder : '',
          value: el ? el.value : '',
          label: lab ? lab.textContent.trim() : '',
        };
      });
      return out;
    }"""
    )
    out = Path(__file__).with_name("_tmp_ph_result.json")
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    b.close()
