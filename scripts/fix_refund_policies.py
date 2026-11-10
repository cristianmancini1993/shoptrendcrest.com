#!/usr/bin/env python3
"""Regenerate corrupted refund-policy pages from clean smartdockshop-based content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPANY = "Northstar Digital Growth LLC"
EMAIL = "info@homeshopspot.com"
ADDRESS = "32 N Gould St., Sheridan, WY 82801, Statele Unite"

GTAG = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405442415117529');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405442415117529&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"""

LOCALES = {
    "en": {
        "lang": "en",
        "geo": "en",
        "cookie": "We use technical and third-party cookies.",
        "cookie_accept": "Accept",
        "cookie_learn": "Learn more",
        "title": "Refund & Return Policy",
        "description": "30-day satisfaction guarantee. How to return a product and get a full refund.",
        "nav_home": "Home",
        "h1": "Refund & Return Policy",
        "updated": "Last updated: 2026",
        "intro": "Your satisfaction is our priority. You have <strong>30 days</strong> to return a product if you are not satisfied, with a full refund of the amount paid.",
        "s1_title": "1. Right of withdrawal",
        "s1": f"Pursuant to the EU Consumer Rights Directive (2011/83/EU) and Italian Legislative Decree 206/2005, the Consumer has 14 days from receipt to withdraw from the contract. <strong>{COMPANY} voluntarily extends this period to 30 days.</strong>",
        "s2_title": "2. How to request a refund",
        "s2_intro": f'To start the return process, contact us <strong>within 30 days of delivery</strong> by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. Please include:',
        "s2_items": [
            "Order number (you'll find it in the confirmation)",
            "Product to return",
            "Reason for return (optional but helpful for improving our service)",
            "IBAN for the refund",
        ],
        "s2_outro": "We will send you the detailed return instructions within 24 hours.",
        "s3_title": "3. Product condition",
        "s3_intro": "The product must be returned:",
        "s3_items": [
            "in its original packaging",
            "complete with all accessories (batteries, charger, manual, etc.)",
            "in undamaged condition",
        ],
        "s3_outro": 'Normal signs of inspection are accepted: the right of withdrawal allows you to "examine" the item as you would in a physical store.',
        "s4_title": "4. Return shipping costs",
        "s4_intro": f"The return shipping cost is <strong>borne by the customer</strong>, except in the following cases where {COMPANY} also covers the return shipping costs:",
        "s4_items": [
            "Defective product upon receipt",
            "Product not matching the order (shipping error)",
            "Product damaged during transport",
        ],
        "s5_title": "5. Refund timeline",
        "s5": "The refund is issued <strong>within 14 days</strong> of receiving the returned product, by bank transfer to the IBAN provided by the customer. The refund covers the full amount paid, excluding any return shipping costs borne by the customer.",
        "s6_title": "6. Defective product",
        "s6_intro": "In case of a defective or non-conforming product, you have the right — at your choice — to:",
        "s6_items": [
            "<strong>Free replacement</strong> with an identical working product",
            "<strong>Full refund</strong> of the amount paid",
        ],
        "s6_outro": "The <strong>legal warranty of conformity</strong> covers the products for <strong>24 months</strong> from delivery, as set out in Articles 128-135 of the Italian Consumer Code.",
        "s7_title": "7. Items not eligible for return",
        "s7": "By law, certain products are not covered by the right of withdrawal (e.g. personalized items, sealed for hygiene reasons once opened, software/digital content unsealed). These cases do not apply to most of our products, but they will be flagged explicitly in the product page if relevant.",
        "s8_title": "8. Simplified procedure",
        "s8_items": [
            f'Email <a href="mailto:{EMAIL}">{EMAIL}</a> within 30 days',
            "Receive return instructions",
            "Send the product to our warehouse",
            "We receive the package and verify its condition",
            "We process the refund within 14 days",
        ],
        "s9_title": "9. Contact for refunds and returns",
        "s9": f'For any information about refunds and returns: <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Information",
        "footer_contact": "Contact",
        "footer_links": [
            ("About us", "about-us.html"),
            ("Contact us", "contact-us.html"),
            ("Privacy Policy", "privacy-policy.html"),
            ("Terms & Conditions", "terms-conditions.html"),
            ("Cookie Policy", "cookie-policy.html"),
            ("Shipping Policy", "shipping-policy.html"),
            ("Refund Policy", "refund-policy.html"),
        ],
        "compact_meta": False,
    },
    "de": {
        "lang": "de",
        "geo": "de",
        "cookie": "Wir verwenden technisch notwendige Cookies und Cookies von Drittanbietern.",
        "cookie_accept": "Akzeptieren",
        "cookie_learn": "Mehr erfahren",
        "title": "Rückerstattungsrichtlinie",
        "description": "30 Tage Zufriedenheitsgarantie. So geben Sie ein Produkt zurück und erhalten eine vollständige Rückerstattung.",
        "nav_home": "Startseite",
        "h1": "Rückerstattungs- und Rückgabebedingungen",
        "updated": "Letzte Aktualisierung: 2026",
        "intro": "Ihre Zufriedenheit ist unsere Priorität. Sie haben <strong>30 Tage</strong> Zeit, ein Produkt zurückzusenden, wenn Sie nicht zufrieden sind, und erhalten den vollen Betrag zurückerstattet.",
        "s1_title": "1. Widerrufsrecht",
        "s1": f"Gemäß der EU-Verbraucherrechtsrichtlinie (2011/83/EU) und dem italienischen Gesetzesdekret 206/2005 hat der Verbraucher ab Erhalt 14 Tage Zeit, um vom Vertrag zurückzutreten. <strong>{COMPANY} verlängert diese Frist freiwillig auf 30 Tage.</strong>",
        "s2_title": "2. So beantragen Sie eine Rückerstattung",
        "s2_intro": f'Um den Rückgabeprozess zu starten, kontaktieren Sie uns <strong>innerhalb von 30 Tagen nach der Lieferung</strong>, indem Sie an <a href="mailto:{EMAIL}">{EMAIL}</a> schreiben. Bitte beifügen:',
        "s2_items": [
            "Bestellnummer (Sie finden diese in der Bestätigung)",
            "Produkt zur Rückgabe",
            "Grund der Rücksendung (optional, aber hilfreich zur Verbesserung unseres Service)",
            "IBAN für die Rückerstattung",
        ],
        "s2_outro": "Wir senden Ihnen innerhalb von 24 Stunden die detaillierten Rücksendeanweisungen.",
        "s3_title": "3. Produktzustand",
        "s3_intro": "Das Produkt muss zurückgegeben werden:",
        "s3_items": [
            "in der Originalverpackung",
            "komplett mit allem Zubehör (Akkus, Ladegerät, Bedienungsanleitung, etc.)",
            "in unbeschädigtem Zustand",
        ],
        "s3_outro": "Normale Prüfspuren werden akzeptiert: Das Widerrufsrecht ermöglicht es Ihnen, den Artikel wie in einem Ladengeschäft zu „prüfen“.",
        "s4_title": "4. Kosten für die Rücksendung",
        "s4_intro": f"Die Kosten für die Rücksendung trägt <strong>der Kunde</strong>, außer in den folgenden Fällen, in denen {COMPANY} auch die Kosten für die Rücksendung übernimmt:",
        "s4_items": [
            "Defektes Produkt bei Erhalt",
            "Produkt entspricht nicht der Bestellung (Versandfehler)",
            "Produkt beim Transport beschädigt",
        ],
        "s5_title": "5. Zeitplan für die Rückerstattung",
        "s5": "Die Rückerstattung erfolgt <strong>innerhalb von 14 Tagen</strong> nach Erhalt des zurückgegebenen Produkts per Banküberweisung auf die vom Kunden angegebene IBAN. Die Rückerstattung umfasst den gesamten gezahlten Betrag, abzüglich etwaiger vom Kunden zu tragender Rücksendekosten.",
        "s6_title": "6. Defektes Produkt",
        "s6_intro": "Im Falle eines fehlerhaften oder nicht konformen Produkts haben Sie nach Ihrer Wahl das Recht:",
        "s6_items": [
            "<strong>Kostenloser Ersatz</strong> durch ein identisch funktionierendes Produkt",
            "<strong>Volle Rückerstattung</strong> des gezahlten Betrags",
        ],
        "s6_outro": "Die <strong>gesetzliche Konformitätsgarantie</strong> gilt für die Produkte für <strong>24 Monate</strong> ab Lieferung, wie in den Artikeln 128-135 des italienischen Verbraucherschutzgesetzes festgelegt.",
        "s7_title": "7. Artikel, die nicht zur Rückgabe berechtigt sind",
        "s7": "Bestimmte Produkte unterliegen gesetzlich nicht dem Widerrufsrecht (z. B. personalisierte Artikel, die nach dem Öffnen aus Hygienegründen versiegelt sind, Software/digitale Inhalte entsiegelt). Diese Fälle treffen auf die meisten unserer Produkte nicht zu, werden jedoch gegebenenfalls auf der Produktseite explizit gekennzeichnet.",
        "s8_title": "8. Vereinfachtes Verfahren",
        "s8_items": [
            f'Senden Sie innerhalb von 30 Tagen eine E-Mail an <a href="mailto:{EMAIL}">{EMAIL}</a>',
            "Erhalten Sie Rücksendeanweisungen",
            "Senden Sie das Produkt an unser Lager",
            "Wir nehmen das Paket entgegen und prüfen den Zustand",
            "Wir bearbeiten die Rückerstattung innerhalb von 14 Tagen",
        ],
        "s9_title": "9. Kontakt für Rückerstattungen und Rücksendungen",
        "s9": f'Für alle Informationen zu Rückerstattungen und Rücksendungen: <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Information",
        "footer_contact": "Kontakt",
        "footer_links": [
            ("Über uns", "about-us.html"),
            ("Kontaktieren Sie uns", "contact-us.html"),
            ("Datenschutzrichtlinie", "privacy-policy.html"),
            ("Allgemeine Geschäftsbedingungen", "terms-conditions.html"),
            ("Cookie-Richtlinie", "cookie-policy.html"),
            ("Versandbedingungen", "shipping-policy.html"),
            ("Rückerstattungsrichtlinie", "refund-policy.html"),
        ],
    },
    "es": {
        "lang": "es",
        "geo": "es",
        "cookie": "Usamos cookies técnicas y de terceros.",
        "cookie_accept": "Aceptar",
        "cookie_learn": "Más información",
        "title": "Política de reembolso",
        "description": "Garantía de satisfacción de 30 días. Cómo devolver un producto y obtener un reembolso completo.",
        "nav_home": "Inicio",
        "h1": "Política de reembolso y devolución",
        "updated": "Última actualización: 2026",
        "intro": "Su satisfacción es nuestra prioridad. Tiene <strong>30 días</strong> para devolver un producto si no está satisfecho, con la devolución íntegra del importe pagado.",
        "s1_title": "1. Derecho de desistimiento",
        "s1": f"De conformidad con la Directiva de la UE sobre derechos del consumidor (2011/83/UE) y el Decreto Legislativo italiano 206/2005, el Consumidor tiene 14 días desde la recepción para rescindir el contrato. <strong>{COMPANY} amplía voluntariamente este plazo a 30 días.</strong>",
        "s2_title": "2. Cómo solicitar un reembolso",
        "s2_intro": f'Para iniciar el proceso de devolución, contáctenos <strong>dentro de los 30 días posteriores a la entrega</strong> escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Por favor incluya:',
        "s2_items": [
            "Número de pedido (lo encontrará en la confirmación)",
            "Producto a devolver",
            "Motivo de la devolución (opcional pero útil para mejorar nuestro servicio)",
            "IBAN para el reembolso",
        ],
        "s2_outro": "Le enviaremos las instrucciones detalladas de devolución dentro de las 24 horas.",
        "s3_title": "3. Estado del producto",
        "s3_intro": "El producto deberá ser devuelto:",
        "s3_items": [
            "en su embalaje original",
            "completo con todos los accesorios (baterías, cargador, manual, etc.)",
            "en condiciones intactas",
        ],
        "s3_outro": 'Se aceptan las señales normales de inspección: el derecho de desistimiento le permite "examinar" el artículo como lo haría en una tienda física.',
        "s4_title": "4. Gastos de envío de devolución",
        "s4_intro": f"El costo de envío de devolución corre <strong>a cargo del cliente</strong>, excepto en los siguientes casos donde {COMPANY} también cubre los costos de envío de devolución:",
        "s4_items": [
            "Producto defectuoso al recibirlo",
            "Producto que no coincide con el pedido (error de envío)",
            "Producto dañado durante el transporte",
        ],
        "s5_title": "5. Cronograma de reembolso",
        "s5": "El reembolso se realiza <strong>dentro de los 14 días</strong> siguientes a la recepción del producto devuelto, mediante transferencia bancaria al IBAN facilitado por el cliente. El reembolso cubre el importe total pagado, excluyendo los gastos de envío de devolución a cargo del cliente.",
        "s6_title": "6. Producto defectuoso",
        "s6_intro": "En caso de un producto defectuoso o no conforme, usted tiene derecho, a su elección, a:",
        "s6_items": [
            "<strong>Reemplazo gratuito</strong> con un producto idéntico que funcione",
            "<strong>Reembolso total</strong> del importe pagado",
        ],
        "s6_outro": "La <strong>garantía legal de conformidad</strong> cubre los productos durante <strong>24 meses</strong> desde la entrega, según lo establecido en los artículos 128-135 del Código del Consumo italiano.",
        "s7_title": "7. Artículos no elegibles para devolución",
        "s7": "Por ley, ciertos productos no están cubiertos por el derecho de desistimiento (por ejemplo, artículos personalizados, sellados por razones de higiene una vez abiertos, software/contenido digital sin sellar). Estos casos no se aplican a la mayoría de nuestros productos, pero se marcarán explícitamente en la página del producto, si corresponde.",
        "s8_title": "8. Procedimiento simplificado",
        "s8_items": [
            f'Envíe un correo electrónico a <a href="mailto:{EMAIL}">{EMAIL}</a> dentro de los 30 días',
            "Reciba instrucciones de devolución",
            "Envíe el producto a nuestro almacén",
            "Recibimos el paquete y verificamos su estado",
            "Procesamos el reembolso en un plazo de 14 días",
        ],
        "s9_title": "9. Contacto para reembolsos y devoluciones",
        "s9": f'Para cualquier información sobre reembolsos y devoluciones: <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Información",
        "footer_contact": "Contacto",
        "footer_links": [
            ("Sobre nosotros", "about-us.html"),
            ("Contáctenos", "contact-us.html"),
            ("política de privacidad", "privacy-policy.html"),
            ("Términos y condiciones", "terms-conditions.html"),
            ("Política de cookies", "cookie-policy.html"),
            ("Política de envío", "shipping-policy.html"),
            ("Política de reembolso", "refund-policy.html"),
        ],
    },
    "fr": {
        "lang": "fr",
        "geo": "fr",
        "cookie": "Nous utilisons des cookies techniques et des cookies tiers.",
        "cookie_accept": "Accepter",
        "cookie_learn": "En savoir plus",
        "title": "Politique de remboursement",
        "description": "Garantie satisfaction 30 jours. Comment retourner un produit et obtenir un remboursement complet.",
        "nav_home": "Accueil",
        "h1": "Politique de remboursement et de retour",
        "updated": "Dernière mise à jour : 2026",
        "intro": "Votre satisfaction est notre priorité. Vous disposez d'un délai de <strong>30 jours</strong> pour retourner un produit si vous n'êtes pas satisfait, avec un remboursement intégral du montant payé.",
        "s1_title": "1. Droit de rétractation",
        "s1": f"Conformément à la directive européenne sur les droits des consommateurs (2011/83/UE) et au décret législatif italien 206/2005, le consommateur dispose d'un délai de 14 jours à compter de la réception pour résilier le contrat. <strong>{COMPANY} étend volontairement ce délai à 30 jours.</strong>",
        "s2_title": "2. Comment demander un remboursement",
        "s2_intro": f'Pour démarrer le processus de retour, contactez-nous <strong>dans les 30 jours suivant la livraison</strong> en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>. Veuillez inclure :',
        "s2_items": [
            "Numéro de commande (vous le trouverez dans la confirmation)",
            "Produit à retourner",
            "Raison du retour (facultatif mais utile pour améliorer notre service)",
            "IBAN pour le remboursement",
        ],
        "s2_outro": "Nous vous enverrons les instructions de retour détaillées dans les 24 heures.",
        "s3_title": "3. État du produit",
        "s3_intro": "Le produit doit être retourné :",
        "s3_items": [
            "dans son emballage d'origine",
            "complet avec tous les accessoires (batteries, chargeur, manuel, etc.)",
            "en bon état",
        ],
        "s3_outro": "Les signes normaux de contrôle sont acceptés : le droit de rétractation vous permet d'« examiner » l'article comme vous le feriez dans un magasin physique.",
        "s4_title": "4. Frais de retour",
        "s4_intro": f"Les frais de retour sont <strong>à la charge du client</strong>, sauf dans les cas suivants où {COMPANY} prend également en charge les frais de retour :",
        "s4_items": [
            "Produit défectueux à la réception",
            "Produit ne correspondant pas à la commande (erreur d'expédition)",
            "Produit endommagé pendant le transport",
        ],
        "s5_title": "5. Délai de remboursement",
        "s5": "Le remboursement est effectué <strong>dans les 14 jours</strong> suivant la réception du produit retourné, par virement bancaire sur l'IBAN fourni par le client. Le remboursement couvre la totalité du montant payé, hors éventuels frais de retour supportés par le client.",
        "s6_title": "6. Produit défectueux",
        "s6_intro": "En cas de produit défectueux ou non conforme, vous avez le droit — à votre choix — de :",
        "s6_items": [
            "<strong>Remplacement gratuit</strong> par un produit fonctionnel identique",
            "<strong>Remboursement intégral</strong> du montant payé",
        ],
        "s6_outro": "La <strong>garantie légale de conformité</strong> couvre les produits pendant <strong>24 mois</strong> à compter de la livraison, comme prévu aux articles 128-135 du Code de la consommation italien.",
        "s7_title": "7. Articles non éligibles au retour",
        "s7": "Selon la loi, certains produits ne sont pas couverts par le droit de rétractation (ex : articles personnalisés, scellés pour des raisons d'hygiène une fois ouverts, logiciels/contenus numériques descellés). Ces cas ne s'appliquent pas à la plupart de nos produits, mais ils seront signalés explicitement sur la page produit le cas échéant.",
        "s8_title": "8. Procédure simplifiée",
        "s8_items": [
            f'Envoyez un e-mail à <a href="mailto:{EMAIL}">{EMAIL}</a> dans les 30 jours',
            "Recevez les instructions de retour",
            "Envoyez le produit à notre entrepôt",
            "Nous recevons le colis et vérifions son état",
            "Nous traitons le remboursement dans les 14 jours",
        ],
        "s9_title": "9. Contact pour les remboursements et les retours",
        "s9": f'Pour toute information sur les remboursements et retours : <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Information",
        "footer_contact": "Contact",
        "footer_links": [
            ("À propos de nous", "about-us.html"),
            ("Contactez-nous", "contact-us.html"),
            ("politique de confidentialité", "privacy-policy.html"),
            ("Conditions générales", "terms-conditions.html"),
            ("Politique en matière de cookies", "cookie-policy.html"),
            ("Politique d'expédition", "shipping-policy.html"),
            ("Politique de remboursement", "refund-policy.html"),
        ],
    },
    "bg": {
        "lang": "bg",
        "geo": "bg",
        "cookie": "Използваме технически бисквитки и бисквитки на трети страни.",
        "cookie_accept": "Приемам",
        "cookie_learn": "Научете повече",
        "title": "Политика за възстановяване на средства",
        "description": "30-дневна гаранция за удовлетворение. Как да върнете продукт и да получите пълно възстановяване на сумата.",
        "nav_home": "Начало",
        "h1": "Политика за възстановяване и връщане",
        "updated": "Последна актуализация: 2026 г.",
        "intro": "Вашето удовлетворение е наш приоритет. Имате <strong>30 дни</strong> да върнете продукт, ако не сте доволни, с пълно възстановяване на платената сума.",
        "s1_title": "1. Право на отказ",
        "s1": f"Съгласно Директивата за правата на потребителите на ЕС (2011/83/ЕС) и италианския законодателен декрет 206/2005, потребителят разполага с 14 дни от получаването, за да се откаже от договора. <strong>{COMPANY} доброволно удължава този период до 30 дни.</strong>",
        "s2_title": "2. Как да поискате възстановяване на сумата",
        "s2_intro": f'За да започнете процеса на връщане, свържете се с нас <strong>в рамките на 30 дни от доставката</strong>, като пишете на <a href="mailto:{EMAIL}">{EMAIL}</a>. Моля, включете:',
        "s2_items": [
            "Номер на поръчката (ще го намерите в потвърждението)",
            "Продукт за връщане",
            "Причина за връщане (по избор, но полезна за подобряване на нашата услуга)",
            "IBAN за възстановяване",
        ],
        "s2_outro": "Ще ви изпратим подробните инструкции за връщане в рамките на 24 часа.",
        "s3_title": "3. Състояние на продукта",
        "s3_intro": "Продуктът трябва да бъде върнат:",
        "s3_items": [
            "в оригиналната си опаковка",
            "в комплект с всички аксесоари (батерии, зарядно, ръководство и др.)",
            "в неувредено състояние",
        ],
        "s3_outro": "Приемат се нормални признаци на проверка: правото на отказ ви позволява да „разгледате“ артикула, както бихте направили във физически магазин.",
        "s4_title": "4. Разходи за обратна доставка",
        "s4_intro": f"Разходите за обратна доставка се поемат <strong>от клиента</strong>, освен в следните случаи, когато {COMPANY} също покрива разходите за обратна доставка:",
        "s4_items": [
            "Дефектен продукт при получаване",
            "Продуктът не отговаря на поръчката (грешка при доставка)",
            "Продуктът е повреден по време на транспортиране",
        ],
        "s5_title": "5. Срокове за възстановяване",
        "s5": "Възстановяването на сумата се извършва <strong>до 14 дни</strong> от получаване на върнатия продукт, по банков път на предоставения от клиента IBAN. Възстановяването покрива пълната платена сума, с изключение на разходите за връщане, поети от клиента.",
        "s6_title": "6. Дефектен продукт",
        "s6_intro": "В случай на дефектен или несъответстващ продукт, вие имате право — по ваш избор — да:",
        "s6_items": [
            "<strong>Безплатна замяна</strong> с идентичен работещ продукт",
            "<strong>Пълно възстановяване</strong> на платената сума",
        ],
        "s6_outro": "Правната <strong>гаранция за съответствие</strong> покрива продуктите за <strong>24 месеца</strong> от доставката, както е посочено в членове 128-135 от Италианския кодекс на потребителите.",
        "s7_title": "7. Артикули, които не отговарят на условията за връщане",
        "s7": "По закон някои продукти не са обхванати от правото на отказ (напр. персонализирани артикули, запечатани от хигиенни съображения след отваряне, софтуер/дигитално съдържание без печат). Тези случаи не се отнасят за повечето от нашите продукти, но ще бъдат изрично отбелязани на страницата на продукта, ако е уместно.",
        "s8_title": "8. Опростена процедура",
        "s8_items": [
            f'Изпратете имейл на <a href="mailto:{EMAIL}">{EMAIL}</a> в рамките на 30 дни',
            "Получаване на инструкции за връщане",
            "Изпратете продукта до нашия склад",
            "Получаваме пакета и проверяваме състоянието му",
            "Обработваме възстановяването в рамките на 14 дни",
        ],
        "s9_title": "9. Свържете се за възстановяване и връщане",
        "s9": f'За всякаква информация относно възстановявания и връщания: <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Информация",
        "footer_contact": "Контакт",
        "footer_links": [
            ("За нас", "about-us.html"),
            ("Свържете се с нас", "contact-us.html"),
            ("Политика за поверителност", "privacy-policy.html"),
            ("Правила и условия", "terms-conditions.html"),
            ("Политика за бисквитки", "cookie-policy.html"),
            ("Политика за доставка", "shipping-policy.html"),
            ("Политика за възстановяване на средства", "refund-policy.html"),
        ],
    },
    "lv": {
        "lang": "lv",
        "geo": "lv",
        "cookie": "Mēs izmantojam tehniskās un trešo pušu sīkdatnes.",
        "cookie_accept": "Pieņemt",
        "cookie_learn": "Uzzināt vairāk",
        "title": "Atmaksas politika",
        "description": "30 dienu apmierinātības garantija. Kā atgriezt preci un saņemt pilnu naudas atmaksu.",
        "nav_home": "Sākums",
        "h1": "Atmaksas un atgriešanas politika",
        "updated": "Pēdējo reizi atjaunināts: 2026",
        "intro": "Jūsu apmierinātība ir mūsu prioritāte. Jums ir <strong>30 dienas</strong>, lai atgrieztu preci, ja neesat apmierināts, ar pilnu samaksātās summas atmaksu.",
        "s1_title": "1. Atteikuma tiesības",
        "s1": f"Saskaņā ar ES Patērētāju tiesību direktīvu (2011/83/ES) un Itālijas Likumdošanas dekrētu 206/2005 patērētājam ir 14 dienas pēc saņemšanas, lai atkāptos no līguma. <strong>{COMPANY} brīvprātīgi pagarina šo periodu līdz 30 dienām.</strong>",
        "s2_title": "2. Kā pieprasīt atmaksu",
        "s2_intro": f'Lai sāktu atgriešanas procesu, sazinieties ar mums <strong>30 dienu laikā pēc piegādes</strong>, rakstot uz <a href="mailto:{EMAIL}">{EMAIL}</a>. Lūdzu, iekļaujiet:',
        "s2_items": [
            "Pasūtījuma numurs (to atradīsit apstiprinājumā)",
            "Prece, kas jāatgriež",
            "Atgriešanas iemesls (nav obligāti, bet noder mūsu pakalpojuma uzlabošanai)",
            "IBAN par naudas atmaksu",
        ],
        "s2_outro": "Mēs nosūtīsim jums detalizētus atgriešanas norādījumus 24 stundu laikā.",
        "s3_title": "3. Produkta stāvoklis",
        "s3_intro": "Prece ir jāatgriež:",
        "s3_items": [
            "tās oriģinālajā iepakojumā",
            "komplektā ar visiem piederumiem (akumulatoriem, lādētāju, rokasgrāmatu utt.)",
            "nebojātā stāvoklī",
        ],
        "s3_outro": "Tiek pieņemtas parastās apskates pazīmes: atteikuma tiesības ļauj \"pārbaudīt\" preci tā, kā to darītu fiziskajā veikalā.",
        "s4_title": "4. Atgriešanas piegādes izmaksas",
        "s4_intro": f"Atgriešanas piegādes izmaksas sedz <strong>klients</strong>, izņemot šādus gadījumus, kad {COMPANY} sedz arī atgriešanas piegādes izmaksas:",
        "s4_items": [
            "Prece saņemšanas brīdī bojāta",
            "Prece neatbilst pasūtījumam (piegādes kļūda)",
            "Produkts bojāts transportēšanas laikā",
        ],
        "s5_title": "5. Atmaksas laika skala",
        "s5": "Naudas atmaksa tiek izsniegta <strong>14 dienu laikā</strong> no atgrieztās preces saņemšanas, ar bankas pārskaitījumu uz klienta norādīto IBAN. Atmaksa sedz visu samaksāto summu, izņemot atgriešanas piegādes izmaksas, ko sedz klients.",
        "s6_title": "6. Bojāta prece",
        "s6_intro": "Bojāta vai neatbilstoša produkta gadījumā jums ir tiesības pēc jūsu izvēles:",
        "s6_items": [
            "<strong>Bezmaksas nomaiņa</strong> pret identisku darba produktu",
            "<strong>Pilna samaksātās summas atmaksa</strong>",
        ],
        "s6_outro": "Juridiskā <strong>atbilstības garantija</strong> attiecas uz produktiem <strong>24 mēnešus</strong> no piegādes, kā noteikts Itālijas Patērētāju kodeksa 128.-135. pantā.",
        "s7_title": "7. Preces, kuras nevar atgriezt",
        "s7": "Saskaņā ar likumu uz noteiktiem produktiem neattiecas atteikuma tiesības (piemēram, personalizētas preces, kas pēc atvēršanas aizzīmogotas higiēnas apsvērumu dēļ, programmatūra/digitālais saturs ir atvērts). Šie gadījumi neattiecas uz lielāko daļu mūsu produktu, taču, ja nepieciešams, tie tiks skaidri atzīmēti produkta lapā.",
        "s8_title": "8. Vienkāršota procedūra",
        "s8_items": [
            f'Nosūtiet e-pastu uz <a href="mailto:{EMAIL}">{EMAIL}</a> 30 dienu laikā',
            "Saņemiet atgriešanas norādījumus",
            "Nosūtiet preci uz mūsu noliktavu",
            "Saņemam paku un pārbaudām tās stāvokli",
            "Apstrādājam atmaksu 14 dienu laikā",
        ],
        "s9_title": "9. Kontakti par atmaksu un atgriešanu",
        "s9": f'Lai iegūtu jebkādu informāciju par atmaksu un atgriešanu: <a href="mailto:{EMAIL}">{EMAIL}</a>',
        "footer_info": "Informācija",
        "footer_contact": "Sazināties",
        "footer_links": [
            ("Par mums", "about-us.html"),
            ("Sazinieties ar mums", "contact-us.html"),
            ("Privātuma politika", "privacy-policy.html"),
            ("Noteikumi un nosacījumi", "terms-conditions.html"),
            ("Sīkdatņu politika", "cookie-policy.html"),
            ("Piegādes politika", "shipping-policy.html"),
            ("Atmaksas politika", "refund-policy.html"),
        ],
    },
}


def ul(items):
    lines = ["<ul>"] + [f"<li>{item}</li>" for item in items] + ["</ul>"]
    return "\n".join(lines)


def ol(items):
    lines = ['<ol style="list-style:decimal;padding-left:1.25rem">'] + [f"<li>{item}</li>" for item in items] + ["</ol>"]
    return "\n".join(lines)


def render_body(loc):
    return f"""<main class="policy-page">
<div class="container container--narrow policy-page__inner">
<h1>{loc["h1"]}</h1>
<p class="policy-page__updated">{loc["updated"]}</p>
<p>{loc["intro"]}</p>
<h2>{loc["s1_title"]}</h2>
<p>{loc["s1"]}</p>
<h2>{loc["s2_title"]}</h2>
<p>{loc["s2_intro"]}</p>
{ul(loc["s2_items"])}
<p>{loc["s2_outro"]}</p>
<h2>{loc["s3_title"]}</h2>
<p>{loc["s3_intro"]}</p>
{ul(loc["s3_items"])}
<p>{loc["s3_outro"]}</p>
<h2>{loc["s4_title"]}</h2>
<p>{loc["s4_intro"]}</p>
{ul(loc["s4_items"])}
<h2>{loc["s5_title"]}</h2>
<p>{loc["s5"]}</p>
<h2>{loc["s6_title"]}</h2>
<p>{loc["s6_intro"]}</p>
{ul(loc["s6_items"])}
<p>{loc["s6_outro"]}</p>
<h2>{loc["s7_title"]}</h2>
<p>{loc["s7"]}</p>
<h2>{loc["s8_title"]}</h2>
{ol(loc["s8_items"])}
<h2>{loc["s9_title"]}</h2>
<p>{loc["s9"]}</p>
</div>
</main>"""


def render_footer(geo, loc):
    links = "\n".join(
        f'<li><a href="/{geo}/{path}">{label}</a></li>' for label, path in loc["footer_links"]
    )
    return f"""<footer class="site-footer"><div class="container">
<div class="site-footer__grid">
<div><a class="site-logo" href="/"><span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span></a></div>
<div><h4 class="site-footer__heading">{loc["footer_info"]}</h4><ul class="site-footer__list">
{links}
</ul></div>
<div><h4 class="site-footer__heading">{loc["footer_contact"]}</h4><ul class="site-footer__list">
<li>{COMPANY}</li>
<li>{ADDRESS}</li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul></div>
</div>
<div class="site-footer__bottom">© <span data-year="">2026</span> <strong>{COMPANY}</strong> — All rights reserved. <a href="/">homeshopspot.com</a></div>
</div></footer>"""


def render_page(geo, loc):
    compact = loc.get("compact_meta", True)
    if compact:
        meta_block = f"""<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{loc["title"]} | homeshopspot.com</title>
<meta content="{loc["description"]}" name="description"/>
<meta content="{EMAIL}" name="contact"/>"""
    else:
        meta_block = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{loc["title"]} | homeshopspot.com</title>
<meta name="description" content="{loc["description"]}">
<meta name="contact" content="{EMAIL}">"""

    if compact:
        assets = """<link href="/favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&amp;display=swap" rel="stylesheet"/>
<link href="/assets/css/variables.css" rel="stylesheet"/>
<link href="/assets/css/reset.css" rel="stylesheet"/>
<link href="/assets/css/components.css" rel="stylesheet"/>
<link href="/assets/css/home.css" rel="stylesheet"/>"""
        script_defer = ' defer=""'
    else:
        assets = """<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<link rel="stylesheet" href="/assets/css/home.css">"""
        script_defer = " defer"

    cookie_json = (
        f"{{ GEO: '{loc['geo']}', COOKIE_TEXT: '{loc['cookie']}', "
        f"COOKIE_ACCEPT: '{loc['cookie_accept']}', COOKIE_LEARN: '{loc['cookie_learn']}' }}"
    )

    return f"""<!DOCTYPE html>

<html lang="{loc["lang"]}">
<head>
{GTAG}
{meta_block}
{assets}
<script>window.SITE_CONFIG = {cookie_json};</script>
<script src="/assets/js/main.js"{script_defer}></script>
</head>
<body>
<header class="site-header"><div class="site-header__inner">
<a class="site-logo" href="/"><span class="site-logo__text"><span class="site-logo__text-primary">homeshopspot</span><span class="site-logo__text-accent">.com</span></span></a>
<nav class="site-header__nav"><a href="/">{loc["nav_home"]}</a></nav>
</div></header>
{render_body(loc)}
{render_footer(geo, loc)}
</body>
</html>
"""


def fix_fr_footers():
    for path in ROOT.glob("fr/*.html"):
        text = path.read_text(encoding="utf-8")
        if "CORA S.R.L." in text:
            path.write_text(text.replace("CORA S.R.L.", COMPANY), encoding="utf-8")
            print(f"Fixed footer in {path.relative_to(ROOT)}")


def main():
    for geo, loc in LOCALES.items():
        out = ROOT / geo / "refund-policy.html"
        out.write_text(render_page(geo, loc), encoding="utf-8", newline="\n")
        print(f"Wrote {out.relative_to(ROOT)}")
    fix_fr_footers()


if __name__ == "__main__":
    main()
