# CENDORA multi-geo campaign

## Adrice forms

All 13 offers have buyer-confirmed `lp` / `_key` in `scripts/_cendora_form_ui.py` and live forms in `scripts/cendora_network_forms.py`.

Webhook: `https://hook.eu2.make.com/jjsjp6cl5zj8fq7pehjniq4edokmpbvx`

Visible fields: **name → tel → street-address** (3 only). City/postal belong in the address line.

**Live lead submission** has not been end-to-end tested from this repo (no test orders). Active submit buttons post to Adrice when `lp`, `_key`, and `offer` are present. Cendora landings do **not** use the generic thank-you fallback if the network form is misconfigured (`body.cendora-lp`).

## 12-piece kit (campaign copy)

Campaign landings list **12 cookware pieces** as separate lines (pots, glass lids, deep pan, deep-pan glass lid, two fry pans, steamer, steamer lid). Hero copy uses “glass lids” (`con coperchi in vetro`). The **3,5 L brasiera / deep pan glass lid** is included so the count matches 12 physical pieces (3×(pot+lid) + pan + pan lid + 2 skillets + steamer + steamer lid). Canonical showcase `it/cendora/index.html` still uses the shorter bullet list.

## Source (unchanged canonical IT showcase)

- `it/cendora/index.html`
- `it/cendora/thank-you.html`

## Regenerate

```bash
cd scripts && python3 cendora_load_locales.py && python3 gen_cendora_geos.py
```
