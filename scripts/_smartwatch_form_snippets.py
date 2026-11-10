# -*- coding: utf-8 -*-
"""Smartwatch order forms (homeshopspot Adrice account)."""

LANDINGS = {
    "586": "hr/smartwatch-586/landing.html",
    "779": "si/smartwatch-779/landing.html",
    "1633": "pt/smartwatch-1633/landing.html",
    "1636": "lt/smartwatch-1636/landing.html",
    "1842": "gr/smartwatch-1842/landing.html",
    "1843": "bg/smartwatch-1843/landing.html",
    "1844": "ro/smartwatch-1844/landing.html",
    "2297": "es/smartwatch-2297/landing.html",
    "2934": "de/smartwatch-2934/landing.html",
    "3141": "pl/smartwatch-3141/landing.html",
    "3143": "cz/smartwatch-3143/landing.html",
    "3834": "lv/smartwatch-3834/landing.html",
}

FORMS = {
    "586": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Ime i prezime*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Ivan Horvat" required><br>
        <label for="tel">Broj telefona*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+385 91 234 5678" required><br>
        <label for="street-address">Adresa za dostavu*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Ilica 45, 10000 Zagreb" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="586" />
        <input name="lp" type="hidden" value="599" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/hr/smartwatch-586/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="9fb0ba6ece6851dbdeccebfc50d22b4c54b4de1d" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">NARUČI NOVENTIS</button>
        </div>
        <p class="form-note">✅ Plaćanje pouzećem · ⚠️ Ograničena zaliha · 🚚 Dostava 24/48 h</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "779": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Ime in priimek*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Janez Novak" required><br>
        <label for="tel">Telefonska številka*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+386 40 123 456" required><br>
        <label for="street-address">Naslov dostave*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Slovenska cesta 12, 1000 Ljubljana" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="779" />
        <input name="lp" type="hidden" value="793" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/si/smartwatch-779/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="2b8c8673491cb39339795be573bc982a4c0f389a" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">NARUČI NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Plačilo ob prevzemu · Brez pologa · Telefonska potrditev</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "1633": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Nome e apelido*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="João Silva" required><br>
        <label for="tel">Telefone de contacto*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+351 912 345 678" required><br>
        <label for="street-address">Morada de entrega*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Rua Augusta 120, 1100-053 Lisboa" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="1633" />
        <input name="lp" type="hidden" value="1653" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/pt/smartwatch-1633/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="dbd22752cadc6a2d3ce9b1b7c75739b1512873c4" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">ENCOMENDAR NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Pagamento na entrega · Sem adiantamento · Confirmação telefónica</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "1636": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Vardas ir pavardė*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jonas Kazlauskas" required><br>
        <label for="tel">Telefono numeris*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+370 612 34567" required><br>
        <label for="street-address">Pristatymo adresas*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Gedimino pr. 10, 01103 Vilnius" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="1636" />
        <input name="lp" type="hidden" value="1656" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/lt/smartwatch-1636/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="f110456f25e1d3063884f731a6a5417d11d756c4" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">UŽSISAKYTI NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Mokėjimas gavus · Be avanso · Telefoninis patvirtinimas</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "1842": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Ονοματεπώνυμο*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Γιώργος Παπαδόπουλος" required><br>
        <label for="tel">Τηλέφωνο*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+30 691 234 5678" required><br>
        <label for="street-address">Διεύθυνση παράδοσης*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Ερμού 45, 105 63 Αθήνα" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="1842" />
        <input name="lp" type="hidden" value="1862" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/gr/smartwatch-1842/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="625bb8f0c8cb3b257c527a16eecf45491712af8e" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">ΠΑΡΑΓΓΕΛΙΑ NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Αντικαταβολή · Χωρίς προκαταβολή · Τηλεφωνική επιβεβαίωση</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "1843": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Име и фамилия*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Иван Петров" required><br>
        <label for="tel">Телефон*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+359 88 123 4567" required><br>
        <label for="street-address">Адрес за доставка*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="ул. Витоша 15, София" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="1843" />
        <input name="lp" type="hidden" value="1863" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/bg/smartwatch-1843/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="4254a321e94884658f80d967b6cf4bc75571af86" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">ПОРЪЧАЙ NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Плащане при доставка · Без аванс · Телефонно потвърждение</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "1844": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Nume complet*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Ion Popescu" required><br>
        <label for="tel">Număr de telefon*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+40 721 234 567" required><br>
        <label for="street-address">Adresă de livrare*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Str. Victoriei 10, București" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="1844" />
        <input name="lp" type="hidden" value="1864" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/ro/smartwatch-1844/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="52bd842ff573b9e3953856765e2489223bc23ed2" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">NARUČI NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Plată la livrare · Fără avans · Confirmare telefonică</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "2297": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Nombre y apellidos*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Carlos García" required><br>
        <label for="tel">Número de teléfono*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+34 612 345 678" required><br>
        <label for="street-address">Dirección de entrega*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Calle Mayor 25, 28013 Madrid" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="2297" />
        <input name="lp" type="hidden" value="2322" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/es/smartwatch-2297/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="4c254887af0d01dd00a59ef9f591995a6930b311" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">HAGA SU PEDIDO</button>
        </div>
        <p class="form-note">🔒 Pago contra reembolso · Sin anticipo · Confirmación telefónica</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "2934": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Vor- und Nachname*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Max Müller" required><br>
        <label for="tel">Telefonnummer*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+49 151 23456789" required><br>
        <label for="street-address">Lieferadresse*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Hauptstraße 12, 10115 Berlin" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="2934" />
        <input name="lp" type="hidden" value="2968" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/de/smartwatch-2934/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="d1c2b314392d370dadd867e72d82312eb120dfdc" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">NOVENTIS BESTELLEN</button>
        </div>
        <p class="form-note">🔒 Zahlung bei Lieferung · Keine Vorauszahlung · Telefonische Bestätigung</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "3141": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Imię i nazwisko*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jan Kowalski" required><br>
        <label for="tel">Numer telefonu*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+48 512 345 678" required><br>
        <label for="street-address">Adres dostawy*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="ul. Marszałkowska 10, 00-590 Warszawa" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="3141" />
        <input name="lp" type="hidden" value="3175" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/pl/smartwatch-3141/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="a17c46696fbf204bb0e96e047adab65275593452" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">ZAMÓW NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Płatność przy odbiorze · Bez zaliczki · Potwierdzenie telefoniczne</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "3143": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Jméno a příjmení*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jan Novák" required><br>
        <label for="tel">Telefonní číslo*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+420 601 123 456" required><br>
        <label for="street-address">Adresa*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Václavské nám. 1, 110 00 Praha" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="3143" />
        <input name="lp" type="hidden" value="3177" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/cz/smartwatch-3143/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="e4b7a95a868df73963bbca845edb8b5f7049ec82" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">OBJEDNAT NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Bez zálohy · Bez karty · Platíte při doručení</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
    "3834": """<form class="tm-order-form" action="https://offers.adricenetwork.com/forms/html/" method="post">
        <label for="name">Vārds un uzvārds*</label>
        <input id="name" type="text" name="name" autocomplete="name" placeholder="Jānis Bērziņš" required><br>
        <label for="tel">Tālrunis*</label>
        <input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="+371 21234567" required><br>
        <label for="street-address">Piegādes adrese*</label>
        <input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="Brīvības iela 10, Rīga" required><br>
        <input name="uid" type="hidden" value="019fd3be-dca9-7be5-9ba1-36a2f751f582" />
        <input name="offer" type="hidden" value="3834" />
        <input name="lp" type="hidden" value="3874" />
        <input name="thankyoupage" type="hidden" value="https://homeshopspot.com/lv/smartwatch-3834/thank-you.html"/>
        <input name="webhook" type="hidden" value="https://hook.eu2.make.com/q0jh5heip824afslcv48k22l478ndv4o" />
        <input name="_key" type="hidden" value="aa1b47610c205b02c57724d6a1de0fdc939c7646" />
        <div style="margin-top: 10px; text-align: center">
            <button name="submit" type="submit">PASŪTĪT NOVENTIS</button>
        </div>
        <p class="form-note">🔒 Bez priekšapmaksas · Bez kartes · Maksājat piegādes brīdī</p>
        <script src="https://offers.adricenetwork.com/forms/html/js-v2/" async></script>
        </form>""",
}
