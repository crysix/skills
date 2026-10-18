# Country: Switzerland

The skill uses this file when the site targets Switzerland. Phases point to the section they need; read only that section.

Everything legal here is a starting point based on official sources, not legal advice. Facts as of October 2026.

## Language and address

- Ask which languages the site needs: German, French and/or Italian (the federal official languages). About 61 % of the population name German or Swiss German as a main language, 23 % French, 8 % Italian. No law requires a private website to be multilingual.
- Swiss Standard German **never uses ß**; it's always "ss" (Strasse, Grösse). Copy taken over from Germany or Austria must be adapted. This overrides the ß note in [../writing-rules.md](../writing-rules.md).
- Quotation marks are guillemets: «so», nested ‹so›, without inner spaces in German.
- Amounts: "CHF 23.50" or "Fr. 23.50", round amounts "Fr. 20.–"; digit groups with a non-breaking space.
- Whether the audience is addressed with Sie or du is the user's decision in phase 1.

## Domain and name check

Used in phase 1 for a new name.

- **Definitive domain check:** `whois -h whois.nic.ch -p 4343 <name>.ch`. The reply starts with `1` ("can be registered") or `0` ("can not be registered", with a reason).
- **RDAP:** `https://rdap.nic.ch/domain/<name>.ch`. 404 usually means free, 200 means registered. SWITCH doesn't guarantee that a 404 name can be registered, so confirm with the check above.
- **Trademarks:** the user searches Swissreg, the register of the Swiss Federal Institute of Intellectual Property (IGE): https://www.swissreg.ch/database-client/search/query/trademarks. It covers Swiss marks and international registrations with effect in Switzerland. **EU trademarks don't cover Switzerland.** The IGE doesn't check new marks against earlier ones; owners of earlier marks have to oppose, so the own search matters.
- **Company names:** a registered company name must differ clearly from all others in Switzerland (Art. 951 OR). Check it on Zefix: https://www.zefix.admin.ch

## Search data

Used in phase 2 and phase 8.

- DataForSEO: `location_code 2756`, `language_code` `de`, `fr` or `it`, one query set per language version. DataForSEO Labs offers no English for Switzerland.
- Without DataForSEO: Google search in a private window, ideally with google.ch.

## Privacy law and consent

Used in phase 5 (fonts, third-party content) and phase 7 (cookies, form services).

- **Data protection act:** the revised DSG, in force since 1 September 2023. Supervisor: the Federal Data Protection and Information Commissioner (EDÖB), https://www.edoeb.admin.ch
- **Cookie rule: information and opt-out, not consent** (Art. 45c FMG). Users must be told about cookies and similar technologies, their purpose, and how to refuse them, in principle before the cookies are activated. Prior express consent is only needed for sensitive data, high-risk profiling or processing visitors wouldn't expect. Strictly necessary cookies (cart, login, language, the saved choice itself) are fine. So the consent table in [../phases/7-cookies-terms.md](../phases/7-cookies-terms.md), which follows EU law, does not apply as such: analytics and pixels need at least clear information and an easy opt-out.
- **EDÖB cookie guidelines** (version 1.1 of 6 October 2025): refusing must not be harder than accepting, no dark patterns, two-click solutions for social plugins, tracking pixels and third-party embeds. The site operator shares responsibility for embedded third parties.
- **If the site also targets visitors in the EU** (euro prices, delivery to the EU, EU customers mentioned), the GDPR can apply as well (Art. 3(2) GDPR), possibly with a duty to name an EU representative (Art. 27 GDPR). Then build consent the EU way; that also satisfies the Swiss rule.
- **Fonts:** the EDÖB has no statement on Google Fonts. Self-host fonts anyway: it avoids sending visitors' data to Google and covers EU visitors.
- **Privacy policy** (Art. 19 DSG, Art. 13 DSV): at least the identity and contact details of the controller, the purpose, the recipients or categories of recipients, and for transfers abroad the country and the safeguard used. It must be easy to find. Intentionally failing to inform can be fined up to CHF 250,000 (Art. 60 DSG).
- **Services abroad** (form services, automation tools, hosting): allowed to countries on the Federal Council's list in Annex 1 DSV (all EU and EEA states, the UK and a few others). The USA only for companies certified under the Swiss-US Data Privacy Framework (since 15 September 2024, check on dataprivacyframework.gov); otherwise standard contractual clauses recognized by the EDÖB. Name each service and its country in the privacy policy.
- **Newsletter:** mass advertising by email needs prior consent, a correct sender and an easy, free way to unsubscribe (Art. 3 Abs. 1 lit. o UWG).

## Legal pages

Used in phase 5 (pages in the site's style) and phase 7 (content).

- **Imprint:** whoever offers goods, works or services online must give clear and complete details of their identity and contact address, including email (Art. 3 Abs. 1 lit. s UWG). Per the federal SME portal: the company name as in the commercial register, the postal address and the email address; a phone number is recommended; a contact form alone is not enough. Whether this also covers a purely informational site isn't settled, so always publish an imprint.
- **Company name:** if the business is in the commercial register, its name appears in full and unchanged (Art. 954a OR); logos and short names may be used in addition.
- **Privacy policy:** see "Privacy law and consent". The cookie information and the opt-out belong there too.
- **File names** (conventions, not law): German `impressum.html` and `datenschutz.html`, French `mentions-legales.html` and `protection-des-donnees.html`, Italian `note-legali.html` and `protezione-dei-dati.html`.
- **Generators:** use one only if it's written for the revised DSG (in force since 1 September 2023). Enter exactly the services the site really uses.
- No link to an EU dispute resolution platform is needed.
- **Claims in the copy:** statements about climate impact (e.g. "climate neutral") must be backed by objective, verifiable evidence (Art. 3 Abs. 1 lit. x UWG, since 1 January 2025).

## Selling online

Used in phase 7, step 2, as soon as contracts are concluded through the site.

- **No statutory right of withdrawal for online purchases.** A 14-day right exists only for consumer contracts over CHF 100 concluded at the doorstep, at the workplace, in public places, on promotional trips or **by phone** (Art. 40a to 40e OR). Voluntary return policies are allowed.
- **Order process** (Art. 3 Abs. 1 lit. s UWG): explain the technical steps to the contract, let the customer spot and correct input errors before sending the order, confirm the order electronically without delay. Make clear which click concludes the contract.
- **Prices** (Price Indication Ordinance, PBV): goods for consumers show the price actually payable in CHF, including VAT (standard rate 8.1 %) and all non-optional surcharges; shipping costs may be separate but on the same page or one click away. Foreign currencies only in addition to CHF. Measurable goods need a unit price. For services, the CHF price duty only covers the sectors listed in Art. 10 PBV (for example hairdressers, garages, hospitality, fitness, courses, travel). Comparison prices: the old price must have applied immediately before or for at least 30 consecutive days (Art. 16 PBV).
- **Payment:** offer at least one free payment method that is common in Switzerland (SECO practice).
- **Terms and conditions:** standard terms that, contrary to good faith, create a significant and unjustified imbalance to the consumer's detriment are unfair (Art. 8 UWG). Swiss customers must not be blocked or charged more because of their location (Art. 3a UWG).
- **Accessibility:** no duty for private business websites today; the BehiG's internet duty binds authorities only. A revision is pending in parliament.
- **Selling to EU consumers:** if the shop is directed at an EU country, that country's mandatory consumer law applies (Art. 6 Rome I), including the 14-day withdrawal right, the withdrawal function and the European Accessibility Act. Then also apply the "Selling online" section of that country's file ([de.md](de.md), [at.md](at.md)) or build a profile with [other.md](other.md).

## Professional help

Who checks legal drafts before use: a lawyer (search of the Swiss Bar Association: https://www.sav-fsa.ch/de/anwaltssuche, or the cantonal bar associations), the cantonal chamber of commerce (https://www.sihk.ch) or the cantonal business promotion office. Data protection guidance: EDÖB. Price display questions: the cantonal authorities, supervised by SECO.

## Official sources

- Federal law on fedlex: DSG (SR 235.1) https://www.fedlex.admin.ch/eli/cc/2022/491/de, DSV (SR 235.11) https://www.fedlex.admin.ch/eli/cc/2022/568/de, FMG (SR 784.10) https://www.fedlex.admin.ch/eli/cc/1997/2187_2187_2187/de, UWG (SR 241) https://www.fedlex.admin.ch/eli/cc/1988/223_223_223/de, OR (SR 220) https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de, PBV (SR 942.211) https://www.fedlex.admin.ch/eli/cc/1978/2081_2081_2081/de
- EDÖB cookie guidelines: https://www.edoeb.admin.ch/en/guidelines-on-data-processing-using-cookies, fact sheet: https://www.edoeb.admin.ch/de/merkblatt-cookies
- EDÖB on transfers abroad: https://www.edoeb.admin.ch/de/bekanntgabe-von-personendaten-ins-ausland
- SME portal, Swiss and EU law for online businesses: https://www.kmu.admin.ch/de/die-gesetze-der-schweiz-und-der-eu
- SECO information sheet on online trade: https://www.seco.admin.ch/dam/de/sd-web/6SGen1K7YQ7J/PBV-Brosch%C3%BCren-Onlinehandel-mit-Waren-SECO-DE.pdf (2021, still shows the old 7.7 % VAT rate)
- SWITCH domain check: https://www.nic.ch/whois/domaincheck/, RDAP: https://www.nic.ch/whois/rdap/
- Federal Chancellery spelling guide (ss instead of ß): https://www.bk.admin.ch/dam/de/sd-web/GApRW2tzdhqZ/rechtschreibleitfaden-2017.pdf, writing instructions (guillemets, amounts): https://www.bk.admin.ch/dam/de/sd-web/YVHazXZRkqKn/schreibweisungen.pdf
