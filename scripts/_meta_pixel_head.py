"""Shared Meta Pixel snippets for HTML generators."""

PIXEL_ID = "1405442415117529"

# For str.format() templates: literal braces are doubled.
META_PIXEL_HEAD = f"""<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

# Doubled braces for str.format() page templates in generators.
META_PIXEL_HEAD_ESCAPED = META_PIXEL_HEAD.replace("{", "{{").replace("}", "}}")


def meta_purchase_script(cpa: float, currency: str = "EUR") -> str:
    value = f"{cpa:.2f}" if abs(cpa - round(cpa)) > 1e-9 else f"{int(round(cpa)):.2f}"
    return f"""
<script>
fbq('track', 'Purchase', {{
value: {value},
currency: '{currency}'
}});
</script>"""
