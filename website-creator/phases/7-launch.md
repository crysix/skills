# Phase 7: Launch

Goal: The site is online, findable for Google and AI search engines, legally sound, and the form arrives.

## 1. SEO and GEO technicals

| File or spot | Content | Template |
|---|---|---|
| `<title>`, `<meta name="description">` | from `copy.md`, main term first | |
| `<link rel="canonical">` | the one correct address of the page | |
| Open Graph and Twitter tags | title, description, preview image | |
| preview image | 1200 × 630 pixels, in the site's style, for LinkedIn, WhatsApp and the like | [../templates/og-image.html](../templates/og-image.html) |
| structured data | in the page head since phase 5, now check with the real domain | |
| `robots.txt` | all search engines and AI crawlers explicitly allowed, pointer to the sitemap | [../templates/robots.txt](../templates/robots.txt) |
| `llms.txt` | short profile in fact sentences that AI assistants read directly | [../templates/llms.txt](../templates/llms.txt) |
| `sitemap.xml` | all pages | [../templates/sitemap.xml](../templates/sitemap.xml) |

The preview image is made like this: copy the template into the `tweak/` folder, adapt the texts, photograph it with Playwright at 1200 × 630 as a PNG, put it at `assets/img/og-image.png`.

Run **Lighthouse** (mobile): `npx lighthouse@13 http://localhost:8000 --form-factor=mobile --output=html --output-path=lighthouse.html`. Goal: above 90 in all four categories.

## 2. Check cookies and terms

Before the legal pages and before the upload, clarify whether the site needs cookie consent or terms and conditions. If it needs them, then from the first visitor on, not only after launch. Flow, legal basis and implementation are in [7-cookies-terms.md](7-cookies-terms.md).

In short: measure the local site, search the code, ask the user what is still to come. Without tracking, without embedded third-party content and without sales, nothing is needed, and one sentence in the status file is enough. The result goes into the privacy policy.

## 3. Legal pages

Which pages are mandatory, what goes into them and which generators help is in the country file, section "Legal pages" (Germany: legal notice and privacy policy). What matters is that they fit the real site:
- With a generator, enter exactly the services the site really uses.
- Remove services that are no longer used (old embeds, analytics tools, appointment booking, chatbots).
- Describe how the form is sent (where the data goes, for example to n8n on the own server).
- Briefly mention local fonts and the absence of cookies.
- Apply the notes in the country file on outdated content, especially on a redesign.

Tell the user clearly: this doesn't replace legal advice. When the site changes, regenerate the texts.

## 4. Connect the form

The form script [../templates/form.js](../templates/form.js) sends the inquiry as JSON to the address in `data-endpoint`. Where to is the user's decision; the hosting file (section "At a glance", row "Form") says what the host supports. Ask with a recommendation:

| Route | Good for | Cost | Effort |
|---|---|---|---|
| **Own PHP script** [../templates/inquiry.php](../templates/inquiry.php) | web space with PHP (milkycode, other web space, Hostinger). No third-party service, data stays with the own host. | none | low |
| **Form service** (Formspree, Web3Forms) | hosts without PHP (Netlify, Vercel, Cloudflare, GitHub Pages, own server without PHP) | free up to a monthly limit | very low |
| **Netlify Forms** | sites hosted on Netlify | free up to a monthly limit | very low |
| **Webhook in n8n, Make or Zapier** | processing inquiries further: email, CRM, spreadsheet, Slack | depends on the service | medium |
| **`mailto:` only** (leave `data-endpoint` empty) | interim solution | none | none |

Recommendation with web space: the PHP script. Anyone already using n8n or Make: webhook.

### Own PHP script

1. Copy `templates/inquiry.php` into the project, fill in `RECIPIENT`, `SENDER` and `DOMAIN`, add the file to `deploy/build.py`.
2. In the form: `data-endpoint="/inquiry.php"`.
3. Create a sender address on the own domain at the host. Otherwise the emails often land in spam, and many hosts reject other senders (rules in the hosting file).
4. The script checks the origin, required fields and email address, evaluates the invisible honeypot field and lets at most five inquiries per IP per hour through.
5. PHP usually doesn't run locally. Testing happens after the upload, with a test inquiry by the user.

### Form service

- **Formspree:** create a form on formspree.io, put the address `https://formspree.io/f/<id>` into `data-endpoint`.
- **Web3Forms:** request an access key by email on web3forms.com. `data-endpoint="https://api.web3forms.com/submit"` and in the form `<input type="hidden" name="access_key" value="<key>">`. The key may sit publicly in the HTML; it only allows sending to the stored address.
- **Netlify Forms:** see [../hosting/netlify.md](../hosting/netlify.md).
- Name the service in the privacy policy. For services abroad, check data processing agreements and data transfers (country file, section "Privacy law and consent").

### Webhook (example n8n)

- Create a webhook node with method POST. Under options, "Allowed Origins (CORS)", enter the own domain exactly as it appears in the browser (with `https://`, without a trailing slash).
- Enter the address of the production webhook into the form's `data-endpoint`.
- Before launch, check the CORS permission without sending data: `curl -i -X OPTIONS <webhook> -H "Origin: https://domain.tld" -H "Access-Control-Request-Method: POST"`. The response must contain `Access-Control-Allow-Origin` with the domain.
- Notification email: copy the template [../templates/inquiry-email.html](../templates/inquiry-email.html) into the email node (HTML), adapt the colors.

For every route: a real test inquiry is sent by the user themselves, or they explicitly give the OK for it.

## 5. Prepare the upload

- **Build script:** copy [../templates/build.py](../templates/build.py) to `deploy/build.py` and adapt the file list. It copies exactly the files that go live to `dist/`, versions the links to CSS and JS (so browsers load changes right away) and packs `dist.zip`. That way working files (research, panel, drafts) never land on the server.
- **Configuration for the host:** the hosting file (section "Configuration") names the template from [../templates/hosting/](../templates/hosting/) and the `HOST_FILES` entry for `build.py`: `.htaccess` for web space and Plesk, `_headers` for Netlify and Cloudflare, `vercel.json` for Vercel, the server configuration for an own server. Together with the host's domain settings, they force HTTPS, redirect `www` to the address without `www` (otherwise the form's allowed origin doesn't match), set caching and security headers and, where the host allows it, block working files. GitHub Pages allows no own headers.

## 6. Go online

**Only after an explicit OK from the user.** Follow the hosting file: section "Set up" if the host isn't connected yet, then section "Deploy".

## 7. Check live

- HTTPS works, `http://` and `www.` redirect to the right address.
- All files return status 200 (`curl -I` on the page, CSS, JS, fonts, images, robots.txt, llms.txt, sitemap.xml).
- Blocked folders and files (`/tweak/`, `.md` files etc.) return 403 or 404, where the host allows blocking.
- Headers arrive: `curl -I` on a CSS file shows a long `Cache-Control` (or `Expires`) and `X-Content-Type-Options` (not on GitHub Pages).
- `python3 tools/check_site.py https://domain.tld` for screenshots and console.
- Measure cookies and requests to third-party domains on the live site once more. The result must match step 2.
- Check structured data with Google's Rich Results Test.
- Check the preview image with the LinkedIn Post Inspector.

For later changes, record the update flow from the hosting file (section "Updates") in the status file.

## Done when

- [ ] SEO files, preview image, Lighthouse above 90.
- [ ] Cookies and terms checked, result in the status file, implemented before the upload if needed.
- [ ] Legal notice and privacy policy fit the real site.
- [ ] Form target set and checked with a test inquiry by the user.
- [ ] Site online, live check passed.
- [ ] Flow for later updates in the status file.

Next: [Phase 8: After launch](8-after-launch.md).
