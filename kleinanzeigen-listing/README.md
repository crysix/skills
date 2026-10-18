# Kleinanzeigen Listing Skill for Claude

This skill adds a structured workflow to Claude for generating listings on **Kleinanzeigen.de** (Germany's largest classifieds platform). From a photo or a short description, Claude produces a ready-to-paste listing — factual, honest, and free of marketing fluff.

---

## Installation

### Let Claude install it (easiest)

Give Claude Code the link to this skill and ask it to install it:

**For all projects**
```
Install the skill from https://github.com/crysix/skills/tree/main/kleinanzeigen-listing globally so it is available in every project.
```

**For this project only**
```
Install the skill from https://github.com/crysix/skills/tree/main/kleinanzeigen-listing in this project.
```

Claude downloads the folder and puts it in the right place: `~/.claude/skills/kleinanzeigen-listing/` for all projects, `.claude/skills/kleinanzeigen-listing/` for one project.

### Install manually

```bash
git clone https://github.com/crysix/skills.git ~/skills

# all projects
mkdir -p ~/.claude/skills && cp -r ~/skills/kleinanzeigen-listing ~/.claude/skills/

# this project only (run inside the project)
mkdir -p .claude/skills && cp -r ~/skills/kleinanzeigen-listing .claude/skills/
```

Use `ln -s` instead of `cp -r` to pick up updates with `git pull`.

- **Codex:** copy the folder to `~/.codex/skills/` instead.
- **claude.ai:** zip the `kleinanzeigen-listing` folder and upload it in the Skills settings.

No configuration needed; the skill is available in all new conversations.

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
Claude asks up to three questions in a single message, leaving out anything you already mentioned:
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

Items older than 2 years get a further 10 percentage points off per additional year (at most 30 points, total at most 90 %). Items that hold their value, like quality furniture, tools, instruments or bikes, get less of an age deduction.

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
der Käufer. Privatverkauf unter Ausschluss jeglicher Gewährleistung,
keine Rücknahme.

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
- The private sale disclaimer is always included and excludes the statutory warranty (*Gewährleistung*), which is what matters legally in Germany; "keine Garantie" alone would not be enough
- Titles start with brand and model, because that is what buyers search for

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
└── README.md   — This file
```
