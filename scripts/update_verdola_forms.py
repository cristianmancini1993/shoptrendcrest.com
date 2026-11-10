# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

FORMS = {
    "de/verdola-326": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Vollständiger Name*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Vollständiger Name" required><br>
        <label for="tel">Telefonnummer*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefonnummer" required><br>
        <label for="street-address">Adresse*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Adresse" required><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="326" />
        <input name="lp" type="hidden" value="326" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/de/verdola-326/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="8b0ecf6ade23f7961c725903cc3d36dbec28f5ad" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">✓ BESTELLUNG BESTÄTIGEN — 79,90 €</button>
        </div>
        <p class="form-note">🔒 Keine Anzahlung · Keine Karte · Zahlen Sie erst bei Lieferung</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "pl/verdola-155": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Imię i nazwisko:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Imię i nazwisko:" required><br>
        <label for="tel">Telefon (najlepiej komórkowy):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (najlepiej komórkowy):" required><br>
        <label for="street-address">Pełny adres:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Pełny adres:" required><br>
        <label for="postal-code">Kod Pocztowy:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Kod Pocztowy:" ><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="155" />
        <input name="lp" type="hidden" value="155" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/pl/verdola-155/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="b23f619da75edd82809a2b0d50d9b4afe52235bc" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">Kup Teraz i Zapłać Przy Odbiorze!</button>
        </div>
        <p class="form-note">🔒 Bez zaliczki · Bez karty · Płacisz dopiero przy odbiorze</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "sk/verdola-154": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Meno a priezvisko:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Meno a priezvisko:" required><br>
        <label for="tel">Telefón (najlepšie mobilný):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefón (najlepšie mobilný):" required><br>
        <label for="street-address">Úplná adresa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Úplná adresa:" required><br>
        <label for="postal-code">PSČ:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="PSČ:" ><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="154" />
        <input name="lp" type="hidden" value="154" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/sk/verdola-154/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="548fe66d30c32e9728530e063fac77f30f6c2bff" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">Kúpte Teraz A Plaťte Pri Dobierke!</button>
        </div>
        <p class="form-note">🔒 Bez zálohy · Bez karty · Platíte až pri doručení</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "hu/verdola-153": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Név És Vezetéknév:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Név És Vezetéknév:" required><br>
        <label for="tel">Telefon (Lehetőleg Mobil)*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (Lehetőleg Mobil)" required><br>
        <label for="street-address">Teljes Cím:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Teljes Cím:" required><br>
        <label for="postal-code">Irányítószám</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Irányítószám" ><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="153" />
        <input name="lp" type="hidden" value="153" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/hu/verdola-153/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="66ed9c1a48573295def72305d421abf37f731ccb" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">Vásároljon Most, És Fizessen Kézbesítéskor</button>
        </div>
        <p class="form-note">🔒 Nincs előleg · Nincs kártya · Fizetés átvételkor</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    # CZ: use Czech labels (user paste had Polish labels for offer 152)
    "cz/verdola-152": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Jméno A Příjmení:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jméno A Příjmení:" required><br>
        <label for="tel">Telefon (Nejlépe Mobilní):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (Nejlépe Mobilní):" required><br>
        <label for="street-address">Úplná Adresa:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Úplná Adresa:" required><br>
        <label for="postal-code">PSČ:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="PSČ:" ><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="152" />
        <input name="lp" type="hidden" value="152" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/cz/verdola-152/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="babb4064cdaa35cb7514d433db5bcd7d149195d2" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">Kupte Nyní A Plaťte Při Doručení</button>
        </div>
        <p class="form-note">🔒 Bez zálohy · Bez karty · Platíte až při doručení</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
    "ro/verdola-151": """      <form class="tm-order-form order-form" action="https://offers.unbreakable-offers.com/forms/html/" method="post">
        <label for="name">Nume si Prenume:*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Nume si Prenume:" required><br>
        <label for="tel">Telefon (de preferință mobil):*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="Telefon (de preferință mobil):" required><br>
        <label for="street-address">Adresa completă:*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Adresa completă:" required><br>
        <label for="postal-code">Cod poștal:</label>
        <input id="postal-code" type="text" name="postal-code" autocomplete="postal-code" placeholder="Cod poștal:" ><br>
        <input name="uid" type="hidden" value="01a06cc3-a876-7de8-8a76-5d9f60d10a31" />
        <input name="offer" type="hidden" value="151" />
        <input name="lp" type="hidden" value="151" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/ro/verdola-151/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/34w4sa8bxn4pwdhe4xjr7r51qposkvqo"/>
        <input name="_key" type="hidden" value="dee81748be8799e5e4cb0c04525496e251fa4a30" />
        <div style="margin-top: 10px; text-align: center">
          <button name="submit" type="submit">Cumpărați Acum Și Plătiți La Livrare!</button>
        </div>
        <p class="form-note">🔒 Fără avans · Fără card · Plătești doar la livrare</p>
        <script src="https://offers.unbreakable-offers.com/forms/html/js-v2/" async></script>
      </form>""",
}


def main() -> None:
    for rel, new_form in FORMS.items():
        path = ROOT / rel / "landing.html"
        html = path.read_text(encoding="utf-8")
        html = html.replace('<script src="/assets/js/form-handler.js" defer></script>\n', "")
        html = html.replace('<script src="/assets/js/form-handler.js" defer></script>', "")
        m = re.search(r'      <form class="tm-order-form.*?</form>', html, re.S)
        if not m:
            raise SystemExit(f"form not found in {path}")
        html = html[: m.start()] + new_form + html[m.end() :]
        path.write_text(html, encoding="utf-8")
        print("updated", path)


if __name__ == "__main__":
    main()
