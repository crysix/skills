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

Ask **these three questions** in a single, compact message, in the user's language. Leave out any question the user has already answered; if all three are answered, skip this step.

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

**Age:** the table assumes a fairly recent item. For items older than 2 years, add a further 10 percentage points of deduction per additional year, at most 30 points (e.g. 4 years old and good condition: − 30 % − 20 % = − 50 %). The total deduction never exceeds 90 %. Electronics lose value fastest; for items that hold their value (e.g. quality furniture, tools, musical instruments, bicycles), deduct less for age and say so. If a successor model exists, mention that the price may need to be lower. If the age is unknown, skip the age deduction.

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
[Brand model] [item] – [short condition] – [optional extra, e.g. "mit Zubehör"]

DESCRIPTION:
[Paragraph 1 – what it is & condition]
Factual description of the item. State the condition honestly, including defects. No superlatives.

[Paragraph 2 – details & reason for selling]
Why it is being sold (optional: "wird nicht mehr gebraucht", "Upgrade" or similar). Included accessories, original packaging.

[Paragraph 3 – handling]
Abholung bevorzugt. Versand möglich gegen Aufpreis (Käufer trägt Versandkosten). Privatverkauf unter Ausschluss jeglicher Gewährleistung, keine Rücknahme.

PRICE:
XX € VB
(original price: XX € → minus XX % for condition "[German condition]"[, minus XX % for age (X years)])

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
- **Always include the private-sale notice**: legally important. It must exclude the statutory warranty (*Gewährleistung*); "keine Garantie" alone is not enough. The exclusion does not cover defects the seller knew about and concealed, which is one more reason to state defects honestly.
- **Title**: brand and model first, because buyers search for them
- **Shipping**: if unclear, use the standard wording from paragraph 3

---

## Category reference (Kleinanzeigen.de)

Give the category as `Main category → Subcategory`, using the exact German names from this list. If no subcategory fits, use the "Weitere …" subcategory of the closest main category. The names are taken from https://www.kleinanzeigen.de/s-kategorien.html (as of October 2026); if the site has changed them, the site wins.

Main categories for selling items, with their subcategories:
- **Elektronik** (electronics): Audio & Hifi · Foto · Haushaltsgeräte · Kommunikation & Funk · Konsolen · Laptops & Notebooks · PCs · PC-Zubehör & Software · Smartphones · Smartphone Zubehör · Tablets & Reader · Telefone & Fax · TV & Video · Videospiele · Wearables · Wearables Zubehör · Weitere Elektronik
- **Haus & Garten** (home & garden): Badezimmer · Büro · Dekoration · Gartenzubehör & Pflanzen · Heimtextilien · Heimwerken · Küche & Esszimmer · Lampen & Licht · Schlafzimmer · Wohnzimmer · Weiteres Haus & Garten
- **Mode & Beauty** (fashion & beauty): Beauty & Gesundheit · Damenbekleidung · Damenschuhe · Herrenbekleidung · Herrenschuhe · Taschen & Accessoires · Uhren & Schmuck · Weiteres Mode & Beauty
- **Familie, Kind & Baby** (family, kids & baby): Baby- & Kinderkleidung · Baby- & Kinderschuhe · Baby-Ausstattung · Babyschalen & Kindersitze · Kinderwagen & Buggys · Kinderzimmermöbel · Spielzeug · Weiteres Familie, Kind & Baby
- **Freizeit, Hobby & Nachbarschaft** (leisure & hobbies): Esoterik & Spirituelles · Essen & Trinken · Handarbeit, Basteln & Kunsthandwerk · Kunst & Antiquitäten · Modellbau · Sammeln · Sport & Camping · Trödel · Weiteres Freizeit, Hobby & Nachbarschaft
- **Musik, Filme & Bücher** (music, films & books): Bücher & Zeitschriften · Büro & Schreibwaren · Comics · Fachbücher, Schule & Studium · Film & DVD · Musik & CDs · Musikinstrumente · Weitere Musik, Filme & Bücher
- **Auto, Rad & Boot** (vehicles): Autos · Autoteile & Reifen · Boote & Bootszubehör · Fahrräder & Zubehör · Motorräder & Motorroller · Motorradteile & Zubehör · Nutzfahrzeuge & Anhänger · Wohnwagen & -mobile · Weiteres Auto, Rad & Boot
- **Haustiere** (pets): Zubehör (for pet supplies)
- **Eintrittskarten & Tickets** (tickets): Bahn & ÖPNV · Comedy & Kabarett · Gutscheine · Kinder · Konzerte · Sport · Theater & Musical · Weitere Eintrittskarten & Tickets
- **Verschenken & Tauschen** (give away & swap): Tauschen · Verleihen · Verschenken (only if the user wants to give the item away or swap it)

Easy to get wrong: furniture goes under **Haus & Garten** by room (e.g. a sofa → Wohnzimmer, a desk → Büro), except children's furniture (**Familie, Kind & Baby → Kinderzimmermöbel**). Kitchen and household appliances go under **Elektronik → Haushaltsgeräte**. Sports and fitness equipment goes under **Freizeit, Hobby & Nachbarschaft → Sport & Camping**, but bicycles go under **Auto, Rad & Boot → Fahrräder & Zubehör**.

The other main categories (Immobilien, Jobs, Dienstleistungen, Unterricht & Kurse, Nachbarschaftshilfe) are not for selling items.
