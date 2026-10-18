# Phase 7, step 2: Check cookies and terms

Goal: Before the upload, it's clear whether the site needs cookie consent or terms and conditions (AGB). If yes, both are implemented together with the user, as a first draft. This happens before launch, because a site that needs consent or terms must have them from the first visitor on.

The legal framework here is German and EU law. For a site that targets another country, check that country's rules instead and tell the user that this section doesn't cover them.

Usually this step is quick. A service site as this skill builds it, i.e. without tracking, without embedded third-party content, with self-hosted fonts and a form posting to the own server, usually needs neither a cookie banner nor terms. Then the result is recorded in one sentence in the status file, and you continue with step 3 in [7-launch.md](7-launch.md).

Tell the user clearly at the start: this is not legal advice. Everything produced here is a first draft based on official sources. Before use, the user checks it themselves or has it checked (lawyer, chamber of commerce (IHK), legal-text service with protection against cease-and-desist letters).

## 1. Inventory

Look yourself first, then ask.

1. **Measure the site.** Load the local site with Playwright (`http://localhost:8000`) without clicking anything and record: cookies set, entries in local storage, all requests to third-party domains (fonts, scripts, images, iframes).
2. **Search the code** for analytics and advertising scripts, embedded videos, maps, appointment booking, chat widgets, payment buttons.
3. **Ask the user** what is still to come: analytics, newsletter, appointment booking, sales or bookings through the site.

## 2. Cookies and consent

The rule is § 25 TDDDG: storing or reading information on the visitor's device is only allowed with consent, unless it is strictly necessary for the service the visitor requested. On top of that comes the GDPR as soon as personal data such as the IP address goes to third parties while loading, even without any cookies.

| On the site | Consent needed? |
|---|---|
| self-hosted fonts, own CSS and JavaScript | no |
| form posting to the own server or webhook | no (but belongs in the privacy policy) |
| storing the consent itself, shopping cart, login | no, technically necessary |
| Google Analytics, advertising pixels (Meta, LinkedIn, Google Ads) | yes |
| embedded YouTube videos, Google Maps, appointment booking, chat widgets | yes, because data goes to the provider while loading |
| cookieless analytics (e.g. Plausible, self-hosted Umami) | disputed; when in doubt, ask for consent or leave it out |

**Avoid first, then ask for consent.** It often works without a banner:
- Search terms and clicks from Google come from Search Console (phase 8); nothing runs on the site for that.
- Where inquiries come from is shown by the "How did you hear about us?" field in the form.
- Videos and maps as a two-click solution: a preview image with a notice; the real content only loads after the click.

**If consent is needed,** it must meet these requirements (guidance of the German Data Protection Conference (DSK) for digital services, as of November 2024):
- Scripts, pixels and embeds only load after consent, not in the background beforehand.
- Declining is as easy as accepting; no preselected checkboxes.
- Purposes and recipients are in the banner or directly reachable from it.
- Consent can be withdrawn at any time, for example via a link in the footer.

Use a ready-made consent service for this instead of building your own banner. Free options (as of October 2026; check the conditions on the provider's site before recommending one):

| Service | Free up to | Note |
|---|---|---|
| [Cookiebot by Usercentrics](https://www.cookiebot.com) | one domain, up to 50 subpages | one language; scripts are marked by hand (attribute `data-cookieconsent`), which you take care of |
| Usercentrics (free plan) | one domain, 1,000 sessions per month | with more visitors, switch to a paid plan |

Setup: the user creates the account and domain at the service; you add the script to the page head, mark every script that needs consent, check with Playwright that none of them loads before consent, and add the service and the categories to the privacy policy.

## 3. Terms and conditions and selling through the site

Terms and conditions (AGB) are not required by law. They become necessary as soon as contracts are concluded through the site: shop, paid bookings, courses, subscriptions, digital products. A pure inquiry site needs none; the conditions are then in the proposal.

When selling to consumers, obligations come on top that matter more than the terms themselves:
- mandatory information before the order (Art. 246a EGBGB) and prices including VAT (Price Indication Ordinance, PAngV)
- cancellation policy and model withdrawal form (Annex 1 and 2 to Art. 246a EGBGB)
- order button labeled "zahlungspflichtig bestellen" ("order with obligation to pay") or something equally clear (§ 312j BGB)
- cancellation button for subscriptions and continuing contracts (§ 312k BGB)
- notice on consumer dispute resolution (§ 36 VSBG), mandatory for more than ten employees
- accessibility under the Accessibility Strengthening Act (BFSG, since 28 June 2025); micro-enterprises providing services are exempt

Also tell the user: for selling, a static site isn't technically enough; that needs a shop or a payment service. That's a project of its own.

**Draft terms:** on request, you write a draft that fits the actual offer, based on the statutory texts (§§ 305 to 310 BGB on the validity of terms and conditions) and the official templates. Don't copy clauses from other people's terms. Mark the draft clearly as a draft and recommend having it checked; when selling to consumers, ideally through a legal-text service with protection against cease-and-desist letters.

## Official sources

- Gesetze im Internet (gesetze-im-internet.de): TDDDG, BGB, EGBGB, PAngV, VSBG, BFSG
- German Data Protection Conference, guidance for providers of digital services (November 2024): https://www.bfdi.bund.de/SharedDocs/Downloads/DE/DSK/Orientierungshilfen/OH_Digitale-Dienste.pdf

## Sign-off

Show the user in a few sentences: what was measured, what is needed and what isn't, what was implemented and what they should still have checked. Then continue with step 3 in [7-launch.md](7-launch.md). The result goes into the privacy policy.

## Done when

- [ ] Inventory done (measurement of the local site and questions to the user).
- [ ] Result in the status file: nothing needed, or what was implemented.
- [ ] If needed: consent built in and checked that nothing loads before it, privacy policy updated.
- [ ] If needed: terms and mandatory information as a draft, with a note to have them checked.
