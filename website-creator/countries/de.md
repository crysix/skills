# Country: Germany (default)

The skill uses this file unless the site targets another country (then see [other.md](other.md)). Phases point to the section they need; read only that section.

Everything legal here is a starting point based on official sources, not legal advice. Facts as of October 2026.

## Language and address

- The site is in German. The notes on German pages in [../writing-rules.md](../writing-rules.md) apply (umlauts and ß, „German quotation marks", Sie or du throughout).
- Whether the audience is addressed with Sie or du is the user's decision in phase 1.

## Domain and name check

Used in phase 1 for a new name.

- Check the `.de` domain through the host's domain search, via `whois` or RDAP: `https://rdap.denic.de/domain/<name>.de` ("not found" usually means free).
- Trademarks: the user checks the favorite themselves in the register of the German Patent and Trade Mark Office (register.dpma.de) and at the EUIPO for EU trademarks. A free domain says nothing about trademark rights.

## Search data

Used in phase 2 and phase 8.

- DataForSEO: `location_code 2276`, `language_code de`.
- Without DataForSEO: Google search in a private window, ideally with google.de.

## Privacy law and consent

Used in phase 5 (fonts, third-party content) and phase 7 (cookies, form services).

- **Cookie rule:** § 25 TDDDG. Storing or reading information on the visitor's device is only allowed with consent, unless it is strictly necessary for the service the visitor requested.
- **GDPR:** applies on top as soon as personal data such as the IP address goes to third parties while loading, even without any cookies.
- **Fonts:** Google Fonts loaded from Google's servers pass the visitor's IP address to Google. The Munich Regional Court found that to be a GDPR violation (LG München I, 20 January 2022, 3 O 17493/20), which was followed by a wave of warning letters. Self-host fonts.
- **Requirements for consent** (guidance of the German Data Protection Conference (DSK) for digital services, as of November 2024):
  - Scripts, pixels and embeds only load after consent, not in the background beforehand.
  - Declining is as easy as accepting; no preselected checkboxes.
  - Purposes and recipients are in the banner or directly reachable from it.
  - Consent can be withdrawn at any time, for example via a link in the footer.
- **Services outside the EU** (form services, automation tools, hosting): a data processing agreement (Art. 28 GDPR) and a legal basis for the transfer, for example the EU-US Data Privacy Framework or standard contractual clauses. Name every service in the privacy policy.

## Legal pages

Used in phase 5 (pages in the site's style) and phase 7 (content).

- **Mandatory for business sites:** a legal notice (Impressum, § 5 DDG) and a privacy policy (Datenschutzerklärung, Art. 13 GDPR). The legal notice must be easy to find and reachable directly, usually through a footer link on every page.
- **File names:** `impressum.html` and `datenschutz.html`.
- **Generators:** for example e-recht24 or Datenschutz-Generator.de. Enter exactly the services the site really uses.
- On a redesign, update old legal pages: references to "§ 5 TMG" point to a law that no longer exists (replaced by the DDG on 14 May 2024), and the link to the EU online dispute resolution platform is obsolete since the platform was shut down (July 2025).

## Selling online

Used in phase 7, step 2, as soon as contracts are concluded through the site.

- **Terms and conditions (AGB)** are not required by law. Their validity follows §§ 305 to 310 BGB. Draft them from the statutory texts and the official templates, never from other people's terms.
- **When selling to consumers**, these obligations matter more than the terms themselves:
  - mandatory information before the order (Art. 246a EGBGB) and prices including VAT (Price Indication Ordinance, PAngV)
  - cancellation policy and model withdrawal form (Annex 1 and 2 to Art. 246a EGBGB)
  - withdrawal function for every consumer contract concluded through the site, since 19 June 2026 (§ 356a BGB): a button labeled "Vertrag widerrufen", then a step where the consumer enters or confirms their name, the contract and the email for the confirmation, and a button labeled "Widerruf bestätigen". Then an acknowledgement of receipt goes out right away on a durable medium (email) with the content, date and time. The function must be reachable from every page during the withdrawal period, stand out from the other footer links and work without a login. The cancellation policy says where to find it. A site that only collects inquiries doesn't need it.
  - order button labeled "zahlungspflichtig bestellen" ("order with obligation to pay") or something equally clear (§ 312j BGB)
  - cancellation button for subscriptions and continuing contracts (§ 312k BGB): "Verträge hier kündigen", then a confirmation page with "jetzt kündigen". Subscriptions need both this and the withdrawal function.
  - notice on consumer dispute resolution (§ 36 VSBG), mandatory for more than ten employees
  - accessibility under the Accessibility Strengthening Act (BFSG, since 28 June 2025); micro-enterprises providing services are exempt

## Professional help

Who checks legal drafts before use: a lawyer, the chamber of commerce (IHK), or a legal-text service with protection against cease-and-desist letters (Abmahnschutz). When selling to consumers, recommend the legal-text service.

## Official sources

- Gesetze im Internet (gesetze-im-internet.de): TDDDG, DDG, BGB, EGBGB, PAngV, VSBG, BFSG
- Withdrawal function: BGBl. 2026 I Nr. 28 (https://www.recht.bund.de/bgbl/1/2026/28/VO.html), current text at https://www.gesetze-im-internet.de/bgb/__356a.html
- German Data Protection Conference, guidance for providers of digital services (November 2024): https://www.bfdi.bund.de/SharedDocs/Downloads/DE/DSK/Orientierungshilfen/OH_Digitale-Dienste.pdf
- DPMA register: https://register.dpma.de
