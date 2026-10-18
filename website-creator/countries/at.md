# Country: Austria

The skill uses this file when the site targets Austria. Phases point to the section they need; read only that section.

Everything legal here is a starting point based on official sources, not legal advice. Facts as of October 2026.

## Language and address

- The site is in German. The notes on German pages in [../writing-rules.md](../writing-rules.md) apply; Austria uses ß like Germany.
- Use Austrian terms where the audience expects them: "Jänner" instead of "Januar", the official trade names (Tischler, Fleischer, Rauchfangkehrer, Spengler in place of the German Schreiner, Metzger, Schornsteinfeger, Klempner), "Firmenbuch" instead of "Handelsregister", "UID-Nr." instead of "USt-IdNr.".
- Prices are written with the euro sign first and a decimal comma: "€ 105,-", "€ 2.900,--".
- Whether the audience is addressed with Sie or du is the user's decision in phase 1.

## Domain and name check

Used in phase 1 for a new name.

- **Domain:** there is no RDAP for `.at`. Use whois: `whois -h whois.nic.at <name>.at`. `% nothing found` means free; a line starting with `domain:` means taken. Where `whois` isn't installed: `(echo <name>.at; sleep 3) | nc whois.nic.at 43`.
- **Trademarks:** the user searches see.ip, the register of the Austrian Patent Office: https://seeip.patentamt.at/markesuche. It covers Austrian, EU and international marks. For more detail on EU marks use EUIPO eSearch plus, for international marks WIPO Madrid Monitor. A free domain says nothing about trademark rights.
- **Paid checks by the Patent Office**, if the user wants certainty: similarity search (from € 105) or "PreCheck Marke" (€ 210, with a legal assessment).
- **Company names:** Firmenbuch query via https://justizonline.gv.at/jop/web/firmenbuchabfrage, the WKO directory at https://firmen.wko.at/

## Search data

Used in phase 2 and phase 8.

- DataForSEO: `location_code 2040`, `language_code de`.
- Without DataForSEO: Google search in a private window, ideally with google.at.

## Privacy law and consent

Used in phase 5 (fonts, third-party content) and phase 7 (cookies, form services).

- **Cookie rule:** § 165 Abs. 3 TKG 2021. Storing or reading information on the visitor's device needs active consent based on clear information, unless it is strictly necessary for a service the visitor explicitly requested. Breaches can be fined up to € 50,000.
- **GDPR and DSG:** the GDPR applies, supplemented by the Austrian DSG. Supervisor: the Datenschutzbehörde (DSB), https://dsb.gv.at/
- **Consent requirements** (DSB FAQ "Datenschutz & Cookies", https://dsb.gv.at/faqs/datenschutz-cookies):
  - Consent comes before any non-necessary cookie is set; no pre-ticked boxes.
  - Refusing takes no more clicks than accepting and isn't hidden on a second layer; the refuse button is not less visible.
  - Withdrawing consent is as easy as giving it.
  - The first layer of the banner names the controller, the purposes, consent as the legal basis, the right to withdraw at any time and how, and links to the privacy policy.
  - No banner is needed if the site sets no non-necessary cookies. Session, cart, login and storing the consent choice (without a unique ID) count as necessary.
- **Fonts:** in summer 2022 thousands of warning letters over Google Fonts demanded € 190 each. The DSB rejected one such complaint as abusive (21 February 2023, GZ 2023-0.137.735), and Vienna courts have found the mass letters abusive, not yet final. There is no official ruling that Google Fonts as such is lawful. WKO recommends hosting fonts locally; do that.
- **Services outside the EU** (form services, automation tools, hosting): a data processing agreement (Art. 28 GDPR) and a legal basis for the transfer, for example the EU-US Data Privacy Framework or standard contractual clauses. Name every service in the privacy policy.

## Legal pages

Used in phase 5 (pages in the site's style) and phase 7 (content). Austria has several overlapping duties; they can all go on one page.

- **E-Commerce-Gesetz (§ 5 ECG)**, for every commercial website, including pure presentation sites: name or company name, geographic address, contact details including email, Firmenbuch number and court if registered, the supervisory authority if the activity is supervised, for regulated trades and professions the chamber or association, the professional title and the state that conferred it plus a reference to the professional rules, and the UID number if there is one. Prices must be marked as gross or net and say whether shipping is included (§ 5 Abs. 2 ECG).
- **Disclosure (Offenlegung, § 25 MedienG)**, for every website, private or commercial. A small site that only presents the owner states the name or company name, the business purpose if any, and the residence or seat (§ 25 Abs. 5). Sites that can influence public opinion (blogs, news, opinion content) need the full disclosure with ownership and the editorial line ("Blattlinie").
- **Firmenbuch entries (§ 14 UGB):** registered businesses (e.U., OG, KG, GmbH, AG) also state the legal form, seat, Firmenbuch number and court.
- **Trade businesses not in the Firmenbuch (§ 63 GewO):** name and the location of the trade licence. Service providers with mandatory professional liability insurance also give the insurance details (§ 22 DLG).
- **Help:** WKO guide "Das korrekte Website-Impressum" with samples per legal form: https://www.wko.at/oe/internetrecht/das-korrekte-website-impressum.pdf. WKO members can fill in the ECG fields of their entry on firmen.wko.at and link to it, but the details must still appear on the site itself.
- **Privacy policy:** a separate page under Art. 13 GDPR; putting it only into the imprint is not enough.
- **File names:** `impressum.html` (imprint and disclosure combined) and `datenschutz.html`.
- On a redesign, remove the link to the EU online dispute resolution platform; the platform was shut down in July 2025.

## Selling online

Used in phase 7, step 2, as soon as contracts are concluded through the site. The FAGG calls withdrawal "Rücktritt"; the button text is still "Vertrag widerrufen".

- **Terms and conditions (AGB):** not required by law. Unusual, disadvantageous clauses only apply if specifically pointed out (§ 864a ABGB); clauses that grossly disadvantage the other party are void (§ 879 Abs. 3 ABGB); § 6 KSchG lists clauses that never bind consumers, and unclear clauses are invalid. Provide the terms so the customer can store and reproduce them (§ 11 ECG). Draft from the statutory texts, never from other people's terms.
- **When selling to consumers:**
  - information before the contract (§ 4 Abs. 1 FAGG), among others phone number and email, the total price including taxes and delivery, the withdrawal conditions with the model form, where the withdrawal function is, and the statutory warranty with the harmonized notice. The model withdrawal instructions in Annex I of the FAGG cover the withdrawal part.
  - 14 days' withdrawal without reasons (§ 11 FAGG); missing withdrawal information extends the period by 12 months (§ 12 FAGG)
  - withdrawal function for contracts concluded through the site, since 1 October 2026 (§ 13a FAGG): a button labeled "Vertrag widerrufen", then a step where the consumer enters their name, the contract and the channel for the confirmation, and a button labeled "Widerruf bestätigen". Then an acknowledgement goes out right away on a durable medium (email) with the content, date and time. Available for the whole withdrawal period, prominent and easy to reach. A site that only collects inquiries doesn't need it.
  - order button labeled only "zahlungspflichtig bestellen" or something equally clear (§ 8 Abs. 2 FAGG); otherwise the consumer isn't bound. Show the key details right before it, and delivery restrictions and payment methods at the start of the order process.
  - explain the technical steps, how input errors are corrected and whether the contract text is stored (§ 9 ECG); confirm the order electronically without delay (§ 10 ECG)
  - prices (Price Labeling Act, PrAG): gross prices in euro including VAT and all levies; a net price only with the gross price next to it; reductions show the lowest price of the previous 30 days (§ 9a PrAG); unit prices for goods sold by weight, volume, length or area
  - dispute resolution (§ 19 AStG): if the business has committed to an ADR body, name it with its web address on the site and in the terms. In any dispute it can't settle, it refers the consumer to the competent body, for online purchases usually the Internet Ombudsstelle (https://www.ombudsstelle.at/).
  - accessibility under the Accessibility Act (BaFG, since 28 June 2025) for online shops and other e-commerce services for consumers; micro-enterprises providing services (fewer than 10 employees and at most € 2 million turnover or balance sheet total) are exempt (§ 6 BaFG)

## Professional help

Who checks legal drafts before use: the regional WKO chamber (legal advice for members), a lawyer (free first consultation "Erste Anwaltliche Auskunft" of the bar associations: https://www.oerak.at/buergerservice/servicecorner/erste-anwaltliche-auskunft/), or a notary (also a free first consultation). The DSB gives no individual legal assessments.

## Official sources

- Rechtsinformationssystem (RIS), single paragraphs via `https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=<number>&Paragraf=<paragraph>`: TKG 2021 (20011678), ECG (20001703), MedienG (10000719), UGB (10001702), GewO (10007517), FAGG (20008847), PrAG (10007216), KSchG (10002462), ABGB (10001622), AStG (20009242), BaFG (20012316), DSG (10001597, add `&Artikel=2`)
- Withdrawal function: Verbraucherrechts-Änderungsgesetz 2026, BGBl. I Nr. 59/2026: https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_59/BGBLA_2026_I_59.html
- DSB FAQ on cookies: https://dsb.gv.at/faqs/datenschutz-cookies
- Business service portal, legal duties for websites: https://www.usp.gv.at/themen/betrieb-und-umwelt/laufender-betrieb/weitere-informationen-laufender-betrieb/e-commerce-kompetenz/anleitungen-um-das-geschaeft-online-zu-bringen/rechtliche-pflichten-fuer-websites.html
- WKO imprint guide: https://www.wko.at/oe/internetrecht/das-korrekte-website-impressum.pdf
- Austrian Patent Office, own trademark search: https://www.patentamt.at/recherche/marken/selbstrecherche
