# Hosting: Hostinger

Web space on LiteSpeed with an official API and MCP for deployment. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | shared web space on LiteSpeed (reads `.htaccess`; on Agency plans `.htaccess` is off by default) |
| Good for | inexpensive web space that the agent can deploy to through the MCP |
| Cost | the plan; SFTP and SSH only from Web Premium, not in Web Single |
| Data location | chosen at order: France, Germany, Lithuania, the Netherlands or the UK (Agency plans: Frankfurt) |
| Form | own PHP script [../templates/inquiry.php](../templates/inquiry.php) (`mail()` at most 10 a minute and 100 a day, sender on the own domain), or a form service or webhook |
| Configuration | [../templates/hosting/.htaccess](../templates/hosting/.htaccess) |
| Agent access | official Hostinger API MCP; SFTP from Web Premium |

## Set up

1. The user books the plan and adds the domain in hPanel. If the domain is in a different Hostinger account than the hosting, move it to the hosting account first; otherwise Hostinger asks for a TXT ownership record.
2. **HTTPS:** the free "Lifetime SSL" certificate installs itself when the domain is added.
3. **Connect the agent:** the user creates an API token in hPanel under Dev tools, API (https://hpanel.hostinger.com/profile/api) and enters it themselves in the terminal, not in the chat:
   - Claude Code, local server (Node 20 or later): `claude mcp add hostinger -s user -e HOSTINGER_API_TOKEN=<token> -- npx -y hostinger-api-mcp`, on Windows `-- cmd /c npx -y hostinger-api-mcp`. Add it globally (`-s user`): an MCP added for one project only is sometimes not loaded on Windows, because VS Code opens the path with a lowercase drive letter.
   - Claude Code, hosted server without a token: `claude mcp add --transport http hostinger https://mcp.hostinger.com -s user`, then `/mcp` and sign in.
   - Codex: `codex mcp add hostinger --env HOSTINGER_API_TOKEN=<token> -- npx -y hostinger-api-mcp`
   - Then restart the agent, reopen the same chat and continue.

## Configuration

- Copy [../templates/hosting/.htaccess](../templates/hosting/.htaccess) into the project folder and replace `DOMAIN.TLD`; `deploy/build.py` already has `HOST_FILES = [".htaccess"]`.
- **Form with `inquiry.php`:** create the sender address on the own domain in hPanel; Hostinger rejects other senders.

## Deploy

Only after the user's explicit OK. Web root: `public_html`.

The MCP has three tools since version 2.0: `search` finds an operation and its parameters, `execute` runs it, `multi-execute` runs several.

1. If the website doesn't exist yet: find the create operation with `search` (`hosting_websites_create`), run it once and check the setup status until it is "completed". That takes a few minutes; don't repeat the write.
2. `python3 deploy/build.py`, copy the zip with a timestamp (`site_YYYYMMDD_HHMMSS.zip`).
3. `execute` the operation `hosting_deploy-static-website` with the parameters `search` shows (domain and the zip). It uploads and extracts the archive.
4. Check the DNS records with the DNS operations: with Hostinger domains, `@` and `www` point to the Hostinger CDN and nothing needs to change. Don't touch mail records (MX) and subdomains.

Without the MCP: upload `dist.zip` in hPanel's File Manager into `public_html` and extract it, or use SFTP as in [webspace.md](webspace.md) (from Web Premium, with the port hPanel shows).

## Updates

- **Clear the cache** after every upload (find the cache operation with `search`, or in hPanel); otherwise the CDN still delivers the old site. Browsers get new CSS and JS through the versioned links.
- Update flow for the status file: build, zip with timestamp, deploy, clear cache, check live.

## Privacy

- The data processing agreement is part of the terms of service, with standard contractual clauses. Name Hostinger in the privacy policy, with the data center location chosen.

## Sources

- MCP server: https://github.com/hostinger/api-mcp-server, https://www.npmjs.com/package/hostinger-api-mcp
- API token: https://www.hostinger.com/support/10840865-what-is-hostinger-api/
- FTP and SSH: https://docs.hostinger.com/websites/ftp-ssh, File Manager: https://docs.hostinger.com/websites/file-manager
- SSL: https://www.hostinger.com/support/1583258-how-to-install-lifetime-ssl-at-hostinger/
- PHP mail limits: https://www.hostinger.com/support/11393648-php-mail-limitation-explained-how-to-improve-email-delivery-with-smtp/
- Server locations: https://www.hostinger.com/support/1583267-where-are-hostinger-servers-located/, DPA: https://www.hostinger.com/legal/dpa
