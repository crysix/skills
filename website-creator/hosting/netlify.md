# Hosting: Netlify

Static hosting platform with a global CDN and built-in form handling. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | static hosting platform, US company |
| Good for | static sites without PHP; built-in forms |
| Cost | Free: 300 credits a month; a production deploy costs 15 credits, bandwidth 20 credits per GB. When the credits run out, **all projects of the account are paused** until the next month. For a business site, Personal ($9 a month, 1,000 credits) or Pro (from $20). Prices in USD |
| Data location | USA (all subprocessors), delivery worldwide |
| Form | Netlify Forms (free and unlimited on the credit plans) or a form service; no PHP |
| Configuration | [../templates/hosting/_headers](../templates/hosting/_headers), plus [_redirects](../templates/hosting/_redirects) only for moved pages |
| Agent access | Netlify CLI; official Netlify MCP |

## Set up

1. The user creates the account at netlify.com and chooses the plan.
2. **Connect the agent**, one of:
   - CLI: `npm install -g netlify-cli` (Node 18.14 or later), then the user runs `netlify login` (browser sign-in).
   - MCP: `claude mcp add --transport http netlify https://netlify-mcp.netlify.app/mcp`, then `/mcp` and sign in. Other agents: `npx -y add-mcp https://netlify-mcp.netlify.app/mcp`. It can create projects and deploy.
3. **Domain:** add it to the site. If the apex domain is primary, Netlify redirects www to it automatically. External DNS: apex as ALIAS/ANAME to `apex-loadbalancer.netlify.com` (or A record `75.2.60.5`), www as CNAME to `<site>.netlify.app`. Netlify recommends www as primary with external DNS; either works, as long as canonical, sitemap and the form's allowed origin use the same address. With Netlify DNS instead, copy existing records such as MX first, then switch the nameservers.
4. **HTTPS:** automatic via Let's Encrypt as soon as DNS points to Netlify.

## Configuration

- Copy [../templates/hosting/_headers](../templates/hosting/_headers) into the project folder; in `deploy/build.py`: `HOST_FILES = ["_headers"]`, plus `"_redirects"` if old addresses need redirects.
- **Form with Netlify Forms:** enable form detection in the Netlify UI (Forms), give the `<form>` `data-netlify="true"`, a unique `name` and `method="POST"`, and a honeypot with `netlify-honeypot="bot-field"`. Send it classically without `form.js`, or with `fetch` to `/` as `application/x-www-form-urlencoded` (Netlify docs). Notifications come from formresponses@netlify.com; a field named `email` becomes the reply-to address.

## Deploy

Only after the user's explicit OK.

1. `python3 deploy/build.py`
2. First deploy, creates the site: `netlify deploy --dir=dist --prod --no-build --site-name <name>` (add `--team <team-slug>` if the user has several teams). Later deploys: `netlify deploy --dir=dist --prod --no-build`.
3. Alternative without CLI: drag the `dist/` folder onto the Deploys page of the site (Netlify Drop).

## Updates

- Every deploy invalidates the CDN cache automatically; browsers get new CSS and JS through the versioned links.
- On the credit plans, every production deploy costs credits: collect changes and deploy them together.
- Update flow for the status file: build, `netlify deploy --dir=dist --prod --no-build`, check live.

## Privacy

- The data processing agreement is part of Netlify's terms; nothing to sign. Transfers to the USA rely on the EU-US Data Privacy Framework, with standard contractual clauses as fallback.
- Name Netlify in the privacy policy as host and, if used, for the form (form data is stored at Netlify).

## Sources

- Deploys and CLI: https://docs.netlify.com/deploy/create-deploys/, https://cli.netlify.com/commands/deploy/
- Headers, redirects: https://docs.netlify.com/manage/routing/headers/, https://docs.netlify.com/manage/routing/redirects/overview/
- Domains and DNS: https://docs.netlify.com/manage/domains/manage-domains/manage-multiple-domains/, https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/
- Caching: https://docs.netlify.com/build/caching/caching-overview/
- Forms: https://docs.netlify.com/manage/forms/setup/
- Credits and pricing: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/, https://www.netlify.com/pricing/
- MCP: https://docs.netlify.com/build/build-with-ai/agent-setup-guides/set-up-claude-code-for-netlify/
- Privacy: https://www.netlify.com/gdpr-ccpa/, https://www.netlify.com/privacy/
