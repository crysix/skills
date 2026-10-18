# Kleinanzeigen Listing Skill for Claude

This skill adds a structured workflow to Claude for generating listings on **Kleinanzeigen.de** (Germany's largest classifieds platform). From a photo or a short description, Claude produces a ready-to-paste listing — factual, honest, and free of marketing fluff.

---

## Installation

### Requirements
- An active **Claude.ai** account (Pro or Team recommended)
- The `SKILL.md` file from this repository

### Step by Step

1. Open [claude.ai](https://claude.ai) in your browser
2. Click your **profile name** in the top-left corner → **Settings**
3. Go to the **Skills** tab
4. Click **"Create skill"** and paste the contents of `SKILL.md` into the editor
5. Save the skill

The skill will be available automatically in all new conversations.

---

## Usage

### With a Photo (recommended)

Upload a photo of the item and say something like:

> "Turn this into a Kleinanzeige."  
> "I want to sell this."  
> "Write me a listing."

Claude will automatically detect the intent and start the workflow.

### Without a Photo

If you don't have a photo, describe the item:

> "I want to sell my old Sony WH-1000XM4 headphones on Kleinanzeigen."

Claude will ask for a photo or work with the description you provide.

### Trigger Phrases

The skill activates automatically on phrases like:
- "Make a Kleinanzeige"
- "I want to sell this"
- "Write a listing"
- "Create an ad"
- "List this on Kleinanzeigen"
- "eBay Kleinanzeigen"

German phrases work as well. Claude talks to you in your language, but the listing itself is always written in German, because it is posted on Kleinanzeigen.de.

---

## How the Workflow Works

### Step 1 — Item Analysis
Claude analyzes the photo or description and identifies brand, model, condition, notable features, and any visible defects.

### Step 2 — Three Follow-up Questions
Claude asks exactly three questions in a single message:
- When was it purchased / how old is it?
- What was the original retail price?
- Is any accessories or original packaging included?

Answering "don't know" for any of them is fine — Claude will continue without that information.

### Step 3 — Price Calculation
A realistic asking price (VB = Verhandlungsbasis / negotiable) is calculated based on condition:

| Condition | Deduction from retail price |
|---|---|
| Like new | − 20 % |
| Good condition | − 30 % |
| Poor condition | − 50 % |
| Defective | − 80 % |

If the retail price is unknown, Claude estimates it and flags it clearly as an estimate.

### Step 4 — Ready-to-Paste Listing
The output is a formatted copy-paste block containing:
- **Title** (max. 65 characters, clear and without clickbait)
- **Description** in three paragraphs (what it is & condition / highlights & reason for selling / shipping & private sale notice)
- **Price** as VB with a visible calculation
- **Category** as `Main category → Subcategory`, using Kleinanzeigen.de's current category names

---

## Example Output

The labels and the price calculation are for you; the listing text is German.

```
════════════════════════════════════════
KLEINANZEIGE – READY TO POST
════════════════════════════════════════

TITLE (max. 65 characters):
Sony WH-1000XM4 Kopfhörer – gut erhalten – mit Zubehör

DESCRIPTION:
Sony WH-1000XM4 Over-Ear-Kopfhörer mit aktiver Geräuschunterdrückung.
Gut erhalten, voll funktionsfähig. Kleine Gebrauchsspuren am Bügel,
keine Risse oder Defekte.

Kabellos, bis zu 30 Stunden Akkulaufzeit. Im Lieferumfang: Original-
Tasche, USB-C-Ladekabel und Klinkenadapter. Wird nicht mehr gebraucht,
da auf Over-Ear-Modell mit Mikrofon gewechselt.

Abholung in Köln bevorzugt. Versand möglich – Versandkosten trägt
der Käufer. Privatverkauf, keine Garantie, keine Rücknahme.

PRICE:
175 € VB
(original price: 250 € → minus 30 % for condition "Gut erhalten")

CATEGORY:
Elektronik → Audio & Hifi

════════════════════════════════════════
```

---

## Design Principles

The skill deliberately uses a plain, factual tone because buyers on Kleinanzeigen.de are skeptical of marketing language:

- No superlatives ("amazing", "top condition", "like new!!!")
- No "Hallo zusammen", no emojis, no exclamation marks
- Defects are mentioned honestly — this prevents disputes and bad reviews
- The private sale disclaimer is always included (legally important in Germany)

---

## FAQ

**Can I adjust the suggested price?**  
Yes. The calculated price is just a starting point. Ask Claude to regenerate the listing with a different price at any time.

**What if Claude doesn't recognize the brand or model?**  
Claude will describe what it can see and may ask you for the model name or any additional details.

**Can I use this for multiple items at once?**  
Best to do one item per conversation — it keeps the workflow focused and the output clean.

**Can I request changes to the listing afterwards?**  
Yes, just continue in the same conversation: "Make the title shorter" or "Add that pickup is also possible in Bonn."

---

## File Structure

```
kleinanzeigen-listing/
├── SKILL.md    — Full skill instructions for Claude
├── Prompt.txt  — The original prompt the skill was created from
└── README.md   — This file
```
