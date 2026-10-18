---
name: kleinanzeigen-listing
description: Generates a complete, ready-to-post listing for Kleinanzeigen.de from a photo or a description of an item. Always use this when the user uploads a photo of an item and wants to sell it, or uses phrases like "make a Kleinanzeige", "I want to sell this", "write a listing", "create an ad", "list this on Kleinanzeigen" or "eBay Kleinanzeigen" (or German equivalents such as "mach eine Kleinanzeige", "ich will das verkaufen", "Anzeigentext schreiben", "Anzeige erstellen", "bei Kleinanzeigen einstellen"), even if there is no image. Start right away; do not ask whether the skill should be used.
---

# Kleinanzeigen Listing Generator

Creates professional, honest listings for Kleinanzeigen.de. No marketing speak, no exaggeration: buyers on Kleinanzeigen are skeptical.

**Language:** Talk to the user in their language. The listing itself (title, description and category) is always written in German, because it is posted on Kleinanzeigen.de.

---

## Step 1: Analyze the item

**If there is an image:**
Analyze the item systematically:
- **Brand & model**: recognize logos, prints, type plates
- **Category**: e.g. electronics, furniture, clothing, sports, household
- **Condition**: one of the four levels below
  - Like new (*Sehr gut erhalten*) = barely any signs of use
  - Good (*Gut erhalten*) = normal signs of use, fully functional
  - Poor (*Schlecht erhalten*) = visible defects, but functional
  - Defective (*Defekt*) = not functional or only partly functional
- **Material, color, size** (if recognizable)
- **Notable features**: equipment, extras, special details
- **Visible defects**: scratches, cracks, stains; name them honestly

**If there is no image:**
Ask briefly, in the user's language: "Send me a photo of the item and I'll create the listing. Or just describe what you want to sell."

---

## Step 2: Three follow-up questions in one message

Ask **exactly these three questions** in a single, compact message, in the user's language:

```
To complete the listing, three quick questions:

1. Roughly when did you buy it / how old is the item?
2. What did it cost new (original price)?
3. Are any accessories or the original packaging included?

If you don't know something, no problem, just write "don't know".
```

If the user answers "don't know" or information is missing, continue without it.

---

## Step 3: Calculate the asking price

**With the original price:**
| Condition | Deduction from the original price |
|---|---|
| Like new (*Sehr gut erhalten*) | − 20 % |
| Good (*Gut erhalten*) | − 30 % |
| Poor (*Schlecht erhalten*) | − 50 % |
| Defective (*Defekt*) | − 80 % |

Round to even amounts (e.g. 45 €, not 47.50 €).

**Without the original price:**
Estimate the current retail price from brand, model and category. Point this out clearly: *(original price estimated, since unknown)*

**Note:** The calculated price is a suggestion, given as VB (*Verhandlungsbasis*, negotiable). The user can adjust it.

---

## Step 4: Generate the listing

Output it as a copy-paste block with divider lines. Labels and the price calculation are for the user; everything that goes into the listing is in German:

```
════════════════════════════════════════
KLEINANZEIGE – READY TO POST
════════════════════════════════════════

TITLE (max. 65 characters):
[Item] – [Brand/model] – [short condition]

DESCRIPTION:
[Paragraph 1 – what it is & condition]
Factual description of the item. State the condition honestly, including defects. No superlatives.

[Paragraph 2 – details & reason for selling]
Why it is being sold (optional: "wird nicht mehr gebraucht", "Upgrade" or similar). Included accessories, original packaging.

[Paragraph 3 – handling]
Abholung bevorzugt. Versand möglich gegen Aufpreis (Käufer trägt Versandkosten). Privatverkauf – keine Garantie, keine Rücknahme.

PRICE:
XX € VB
(original price: XX € → minus XX % for condition "[German condition]")

CATEGORY:
[Matching main category on Kleinanzeigen.de]

════════════════════════════════════════
```

---

## Tone & rules

- **Factual and direct**: no adjectives like "traumhaft", "top" or "mega"
- **No "Hallo zusammen"**, no smileys, no exclamation marks
- **Never hide defects**: this protects against bad reviews
- **No stock phrases** like "Nur wegen Umzug" (only selling because of a move) unless it is true
- **Always include the private-sale notice**: legally important
- **Shipping**: if unclear, use the standard wording from paragraph 3

---

## Category reference (Kleinanzeigen.de)

Common main categories (use the German names as they appear on the site):
- Elektronik (electronics) → phones, laptops, TV, audio
- Möbel & Wohnen (furniture & living) → sofas, tables, lamps
- Kleidung & Accessoires (clothing & accessories) → by target group
- Sport & Camping (sports & camping) → bicycles, fitness equipment
- Haushalt (household) → kitchen appliances, household appliances
- Garten & Heimwerken (garden & DIY) → tools, plants
- Spielzeug & Kinderbedarf (toys & children's items) → state the age
- Auto & Zubehör (car & accessories) → car parts, accessories
- Freizeit (leisure) → books, music, collectibles
