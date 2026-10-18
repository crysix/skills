# Phase 1: Foundation

Goal: The real brand is measured (for a new brand: name and logo shape are settled), the logo carries the brand idea, and `PRODUCT.md` describes who the site is for and what it has to achieve.

If there is no brand yet, go straight to section 1b.

## 1. Measure the brand

Never take colors and fonts from notes or estimate them from screenshots. Sources in this order:

1. **Live site:** `python tools/extract_brand.py https://example.com` (script in the skill folder). It loads the page, scrolls all the way through once (otherwise animated sections stay empty) and weights the computed colors by area and frequency. Result: background, text, accents, fonts with weights.
2. **Logo file:** read the colors from the SVG or PNG.
3. **The user's brand files** (style guide, presentations).

Then put a short brand profile into the status file:

| Role | Value |
|---|---|
| Main color | |
| Accent | |
| Light surface | |
| Text | |
| Headings | font, weight |
| Body text | font, weight |
| Traits | what makes the brand recognizable |

## 1b. New brand: the name first

If there is no name yet, it comes before everything else, because the domain, logo, copy and the later description in AI search all depend on it. Don't invent a brand on your own: you propose, the user decides.

1. **Questions in one message:** What does the user offer, and to whom? What should the name stand for? Three adjectives for the brand. Their own name as the brand, or an invented name? Regional or national?
2. **Eight to twelve proposals** as a table: name, meaning in one sentence, how it sounds (can it be spelled over the phone?), whether the domain is free (in Germany the `.de` domain). Check the domain through the host's domain search, via `whois` or RDAP (for `.de`: `https://rdap.denic.de/domain/<name>.de`, "not found" usually means free). Also do a quick search whether someone in the same industry already uses the name.
3. **Trademark law:** The user checks the favorite themselves in the register of the German Patent and Trade Mark Office (register.dpma.de) and at the EUIPO. Say clearly that this is not legal advice and that a free domain says nothing about trademark rights.
4. **Decision** with date into the status file. The user secures the domain themselves, ideally right away with the future host.

A new brand has no colors and fonts yet. Ask for three to five sites the user likes, from any industry, and note them for phase 2. That's where the palette emerges from the references; until then the brand profile in the status file stays open.

## 2. Check the logo

Ask briefly: Does the logo still fit? Does it carry the idea behind the name? If yes, move on. If no, or if a new brand has none yet:

1. **Put the meaning into words.** What is in the name? (For example, "Bridge" stands for connection, "Compass" for orientation.)
2. **Round 1:** six to nine concepts as SVG. Show each on light, on dark, in one color, as a favicon at 32 and 16 pixels and next to the wordmark, all on one HTML preview page. Call weak concepts weak.
3. **Round 2:** the chosen concept in five variants, applying the user's feedback precisely.
4. **Polish:** check proportions next to the wordmark, convert the wordmark into vector paths with opentype.js (with kerning), build a separate simplified favicon.

What makes logos look less generated:
- Waves and ribbons as shapes that start thin and get thicker, instead of lines of even width.
- Shapes in several tones of the same color, so forms look cut rather than flat.
- Favicon as a badge with a background shape; otherwise nothing is left at 16 pixels.
- A logo family instead of one file: logo with wordmark, mark alone, favicon, each in color, negative and single color.

For a new brand, rounds 1 and 2 are done in one color (dark on light, light on dark), because the colors only come in phase 2. Here it's about the shape. The logo family gets colored after the color choice in phase 2.

Storage: `logo/final/` with `preview.html`, drafts in `logo/drafts/`.

## 3. Capture the product context

Run `/impeccable init`. It writes `PRODUCT.md` and only asks what it doesn't know yet.

The most important question of this phase, always ask it: **Who is the site for, and what should it achieve?** This includes where visitors come from and what they already know.

People who already know the user mainly need an easy path to an inquiry. People who find them on Google for the first time first need reasons to trust them. This answer changes the copy, the proof and the structure.

Also clarify:
- Which proof really exists (training, publications, reach, clients with permission)? With links.
- What should explicitly not be on the site (prices, case studies, client names)?
- How is the audience addressed (formal or informal; in German, Sie or du)?

## Sign-off

Show the user the brand profile (for a new brand: name and logo shape), the logo (if revised) and a five-sentence summary of `PRODUCT.md`. Only continue after their confirmation.

## Done when

- [ ] Brand profile measured and in the status file, or for a new brand: name chosen, favorite sites noted.
- [ ] Logo confirmed or new logo family finished.
- [ ] `PRODUCT.md` exists, the visitor question is answered.
- [ ] The user has confirmed.

Next: [Phase 2: Research](2-research.md).
