# Country: any other country

Use this file when the site targets a country that has no file of its own in this folder. You build a country profile for the project with the same sections as [de.md](de.md), from official sources.

## How to build the profile

1. Create `research/country.md` in the project with the section headings of `de.md`. Note in the status file: "Country: <name>, profile research/country.md".
2. Research a section the first time a phase needs it, not all at once. The phases name the section they need.
3. Use official sources: the country's law portal, data protection authority, trademark office, domain registry, consumer protection agency. Law firm articles and generators only help you find the official text; they are never the only source.
4. Note the source URL and the date you checked it for every fact.
5. Before a legal section is used, show it to the user and say clearly: researched by an AI from official sources, not legal advice, have it checked locally.
6. If you can't find or verify something, write that into the profile instead of guessing.

## What to find out per section

- **Language and address:** the site's language. If the country has several official languages (for example Switzerland or Belgium), ask which ones. [../writing-rules.md](../writing-rules.md) applies in every language.
- **Domain and name check:** the country-code domain and its registry's lookup (RDAP or whois). The national trademark office's register; for EU countries also the EUIPO; for international plans the WIPO Global Brand Database.
- **Search data:** for DataForSEO, the `location_name` (for example "Austria") or the `location_code` from `keywords_data/google_ads/locations`, plus the `language_code`.
- **Privacy law and consent:** in the EU and EEA, the GDPR applies everywhere, and the cookie rule comes from the ePrivacy Directive as implemented in national law. Find the national provision and the data protection authority's guidance on consent. Outside the EU: the national privacy law, whether cookies and tracking need consent, and the rules for data transfers abroad. Check whether self-hosting fonts and two-click embeds are needed there as well; they never hurt.
- **Legal pages:** whether a legal notice (imprint) is required and what goes into it, what the privacy policy must contain, the usual file names in the site's language, reputable generators if any.
- **Selling online:** consumer information duties, right of withdrawal or cancellation, price display, rules for the order button, accessibility. In the EU, the European Accessibility Act applies to many online shops and services in every member state since 28 June 2025.
- **Professional help:** who checks legal texts locally (lawyers, chambers of commerce, legal-text services).
- **Official sources:** list with URLs and check dates.

## Reusing a profile

If the user builds sites for this country more often, offer to add the finished profile to the skill as `countries/<code>.md` (for example `at.md` for Austria), so later projects start from it. Only with the user's OK, because it changes the skill itself. Re-check facts in a stored profile that are more than a year old.
