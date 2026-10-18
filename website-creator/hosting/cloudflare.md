# Hosting: Cloudflare

Static site on Cloudflare Workers with static assets, which Cloudflare recommends for new projects instead of Pages. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | edge platform with a global network, US company |
| Good for | fast worldwide delivery at no cost; the domain has to move to Cloudflare DNS |
| Cost | Workers Free: requests to static assets are free and unlimited, no bandwidth charges. Cloudflare describes its free plan as "for personal or hobby projects that aren't business-critical"; no ban on commercial use was found |
| Data location | worldwide network; EU-only processing only with the Enterprise Data Localization Suite |
| Form | nothing built in: form service or webhook; no PHP |
| Configuration | [../templates/hosting/wrangler.jsonc](../templates/hosting/wrangler.jsonc) in the project folder, [_headers](../templates/hosting/_headers) in `dist/`, [_redirects](../templates/hosting/_redirects) only for moved pages |
| Agent access | Wrangler CLI; Cloudflare API MCP for DNS, domains and redirect rules |

## Set up

1. The user creates the account at cloudflare.com and adds the domain as a zone: switch the nameservers at the registrar to Cloudflare's and check that MX and other existing records came along.
2. **Connect the agent:**
   - Wrangler: the user runs `npx wrangler login` (browser sign-in).
   - MCP, optional, for DNS and rules: `claude mcp add --transport http cloudflare-api https://mcp.cloudflare.com/mcp`, then `/mcp` and sign in. Deploying a folder through it isn't documented; deploy with Wrangler.
3. **Domain:** set it in `wrangler.jsonc` (`routes` with `custom_domain: true`) or in the dashboard under the Worker's Settings, Domains & Routes. Cloudflare creates the DNS record and the certificate.
4. **www to the address without www:** `_redirects` can't do it. Create a Redirect Rule (Rules, Redirect Rules, template "Redirect from WWW to root": `https://www.*` to `https://${1}`, 301, preserve query string), add a proxied DNS record for `www` (for example `A www 192.0.2.1`, proxied) and switch on "Always Use HTTPS".
5. **HTTPS:** Universal SSL, automatic and free.

## Configuration

- Copy [../templates/hosting/wrangler.jsonc](../templates/hosting/wrangler.jsonc) into the project folder and fill in the name and domain. It stays out of `dist/`.
- Copy [../templates/hosting/_headers](../templates/hosting/_headers) into the project folder; in `deploy/build.py`: `HOST_FILES = ["_headers"]`, plus `"_redirects"` for moved pages (always with status 301, Cloudflare's default is 302).
- Don't add Cache Rules on the domain; they can serve stale files after a deploy.

## Deploy

Only after the user's explicit OK.

1. `python3 deploy/build.py`
2. `npx wrangler deploy` in the project folder.

The older Pages route still works with the same `_headers`: `npx wrangler pages deploy dist --project-name=<name>`.

## Updates

- Browsers revalidate HTML by default; CSS and JS come fresh through the versioned links. Whether a new Workers deploy clears the CDN cache isn't documented: check the live site after each deploy and, if it's stale, use Caching, Purge Everything in the dashboard.
- Update flow for the status file: build, `npx wrangler deploy`, check live.

## Privacy

- The data processing agreement is part of the main agreement, self-serve included. Transfers rely on the EU-US Data Privacy Framework, with standard contractual clauses as fallback.
- Name Cloudflare in the privacy policy as host.

## Sources

- Workers static assets: https://developers.cloudflare.com/workers/static-assets/, recommendation over Pages: https://developers.cloudflare.com/pages/
- Headers and redirects: https://developers.cloudflare.com/workers/static-assets/headers/, https://developers.cloudflare.com/workers/static-assets/redirects/
- www redirect: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/
- Custom domains: https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
- Limits and pricing: https://developers.cloudflare.com/workers/platform/limits/, https://www.cloudflare.com/plans/
- MCP: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/
- Privacy: https://www.cloudflare.com/cloudflare-customer-dpa/, https://www.cloudflare.com/privacypolicy/
