# Hosting: Vercel

Frontend platform with a global CDN. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | frontend platform, US company |
| Good for | teams that already work with Vercel |
| Cost | The free Hobby plan is for non-commercial personal use only; a business site, or one an agency gets paid for, needs Pro: $20 a month per deploying seat, including $20 of usage credit. Prices in USD plus VAT |
| Data location | worldwide CDN; Vercel may transfer data to the USA and elsewhere; no EU-only option for static content |
| Form | nothing built in: form service (Vercel documents Formspree) or webhook; no PHP |
| Configuration | [../templates/hosting/vercel.json](../templates/hosting/vercel.json) |
| Agent access | Vercel CLI; official Vercel MCP (deploys only small inline file sets, so use the CLI) |

## Set up

1. The user creates the account at vercel.com and books Pro.
2. **Connect the agent:**
   - CLI: `npm i -g vercel`, then the user runs `vercel login`.
   - MCP, optional, for projects and domains: `claude mcp add --transport http vercel https://mcp.vercel.com`, then `/mcp` and sign in.
3. **Domain:** in the project under Settings, Domains, add the apex domain and www, and set www to "Redirect to" the apex domain. Vercel recommends www as primary; either works, as long as canonical, sitemap and the form's allowed origin use the same address. DNS: the A record for the apex (usually `76.76.21.21`) and the CNAME for www as shown on the project's domain card.
4. **HTTPS:** automatic via Let's Encrypt; HTTP always redirects to HTTPS.

## Configuration

- Copy [../templates/hosting/vercel.json](../templates/hosting/vercel.json) into the project folder; in `deploy/build.py`: `HOST_FILES = ["vercel.json"]`. It has to sit in the deployed folder, so the build copies it into `dist/`.
- The Vercel project link (`.vercel/`) may land in `dist/`; `build.py` keeps it on rebuilds.
- The project address `<name>.vercel.app` stays reachable next to the own domain; the canonical tag keeps search engines on the own domain.

## Deploy

Only after the user's explicit OK.

1. `python3 deploy/build.py`
2. `vercel deploy dist --prod --yes` in the project folder. The first deploy creates the project (preset "Other", no build command). If the user belongs to several teams, add `--scope <team>`.

## Updates

- Every deployment gets its own CDN cache; browsers get new CSS and JS through the versioned links. If something still looks stale: `vercel cache purge`.
- Update flow for the status file: build, `vercel deploy dist --prod --yes`, check live.

## Privacy

- The data processing agreement covers Pro and Enterprise. Vercel is certified under the EU-US Data Privacy Framework; the agreement itself uses standard contractual clauses. Vercel logs visitors' IP addresses.
- Name Vercel in the privacy policy as host.

## Sources

- CLI and deploy: https://vercel.com/docs/cli/deploy, https://vercel.com/docs/builds/configure-a-build
- vercel.json: https://vercel.com/docs/project-configuration/vercel-json
- Caching: https://vercel.com/docs/caching/cache-control-headers, https://vercel.com/docs/caching/cdn-cache
- Domains: https://vercel.com/docs/domains/working-with-domains/deploying-and-redirecting
- Hobby terms: https://vercel.com/docs/limits/fair-use-guidelines, Pro: https://vercel.com/docs/plans/pro-plan
- MCP: https://vercel.com/docs/agent-resources/vercel-mcp
- Privacy: https://vercel.com/legal/dpa, https://vercel.com/docs/security/compliance
