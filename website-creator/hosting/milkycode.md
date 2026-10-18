# Hosting: milkycode webhosting (default)

Web space on Plesk, run by milkycode GmbH, an agency in Cologne. This is the skill's default recommendation. The Plesk parts apply to any other host with Plesk as well. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | managed web space on Plesk (nginx in front of Apache) |
| Good for | every site this skill builds, with support from people who know the setup |
| Cost | on request |
| Data location | ask milkycode, and state it in the privacy policy |
| Form | own PHP script [../templates/inquiry.php](../templates/inquiry.php), or a form service or webhook |
| Configuration | [../templates/hosting/.htaccess](../templates/hosting/.htaccess) |
| Agent access | Plesk MCP through the WebPros Dashboard; SFTP; Plesk Git |

## Set up

1. **Contact milkycode:** project inquiry at https://www.milkycode.com/de/projektanfrage/ or by phone +49 221 6696404-0 (Monday to Friday, 10 to 18). Ask for:
   - a hosting subscription for the domain,
   - SFTP access: SSH access for the subscription's system user set to "/bin/bash (chrooted)",
   - an MCP key for the agent, scoped to this subscription (see step 4),
   - the data location and the data processing agreement (AV-Vertrag).
2. **Domain:** registered through milkycode or kept at the user's registrar, with DNS pointing to the Plesk server.
3. **HTTPS in Plesk:** SSL/TLS Certificates, "SSL It!", free Let's Encrypt certificate including www; it renews 30 days before expiry. Switch on "Redirect from http to https". In the Hosting Settings, set the preferred domain to the address without www (matches the `.htaccess` and the form's allowed origin).
4. **Connect the agent (optional, recommended):** Plesk speaks MCP through the WebPros Dashboard (since Plesk 18.0.80).
   - milkycode adds the server to its WebPros Dashboard and creates an MCP key scoped to the subscription. Each tool can be enabled, read-only or read-write; every tool call is logged.
   - The user adds the key themselves in the terminal, not in the chat. Claude Code: `claude mcp add --transport http webpros-dashboard https://mcp.webpros.com/api/mcp -s user --header "Authorization: Bearer <MCP_KEY>"`. Other agents: the same URL with the key as a Bearer token (see the agent's MCP docs). Then restart the agent and reopen the same chat.
   - Since Plesk 18.0.81, milkycode can instead allow signing in with a WebPros account linked to the Plesk user.
   - There is no public list of the tools. After connecting, look at which tools the connection offers and use read-only ones first.

## Configuration

- Copy [../templates/hosting/.htaccess](../templates/hosting/.htaccess) into the project folder and replace `DOMAIN.TLD`; `deploy/build.py` already has `HOST_FILES = [".htaccess"]`.
- **Web server settings (Apache & nginx Settings):** Plesk's default, "Proxy mode" on and "Serve static files directly by nginx" off, applies the `.htaccess` to all files. With "Serve static files directly by nginx" on, its rules don't reach CSS, JS and images; ask milkycode to leave it off.
- **Form with `inquiry.php`:** the sender address must be on the own domain; the script passes it with `-f`. Switch on DKIM signing in the Mail Settings. If the domain's email is hosted elsewhere (for example Microsoft 365), switch off "Mail service on this domain" in Plesk, otherwise form mails to the own domain are delivered locally and never arrive.

## Deploy

Only after the user's explicit OK. Web root: `httpdocs`.

1. `python3 deploy/build.py`
2. Upload by one of these routes:
   - **MCP:** if the connection offers file tools, upload the contents of `dist/` into `httpdocs` with them. Ask before every write.
   - **SFTP**, dry run first, then without `--dry-run`:
     ```
     lftp -u <user> sftp://<server> -e "mirror -R --delete --verbose --dry-run -X .well-known/ dist/ httpdocs; quit"
     rsync -avz --delete --exclude .well-known/ --dry-run dist/ <user>@<server>:httpdocs/
     ```
     Write `dist/` with and `httpdocs` without a trailing slash in `lftp`, otherwise the upload lands in `httpdocs/dist/`. `--delete` removes everything on the server that isn't in `dist/`; that's why the dry run comes first. On Windows: WinSCP, Commands, Synchronize, direction "Remote", with "Delete files" and "Preview changes".
   - **File Manager:** upload `dist.zip` into `httpdocs`, select it, "Extract Files" with "Replace existing files", then delete the zip.
   - **Git:** Plesk's Git extension deploys a repository into `httpdocs`, automatically through a webhook. Use a repository that holds only the built site, as described for [github-pages.md](github-pages.md) (a repository in `dist/`, which `build.py` keeps).
3. After the first upload, check the headers: `curl -I https://DOMAIN.TLD/assets/css/site.css` must show a long `Cache-Control` or `Expires` and `X-Content-Type-Options`. If they're missing, ask milkycode to set them in the nginx settings of the domain (only the Plesk administrator can).

## Updates

- Plesk adds no CDN by default, so there is no cache to clear; browsers get new CSS and JS through the versioned links.
- Update flow for the status file: build, upload by the same route, check live.

## Privacy

- Name milkycode as host in the privacy policy, with the data location milkycode states, and conclude the data processing agreement.

## Sources

- WebPros Dashboard MCP: https://support.plesk.com/hc/en-us/articles/42823372160919-How-to-connect-cPanel-Plesk-to-MCP-in-WebPros-Dashboard, MCP key: https://support.webpros.com/hc/en-us/articles/42281757876119-How-to-create-WebPros-Dashboard-MCP-key
- Plesk change log (MCP in 18.0.80 and 18.0.81): https://docs.plesk.com/release-notes/obsidian/change-log/
- File Manager: https://docs.plesk.com/en-US/obsidian/customer-guide/websites-and-domains/website-content/uploading-content-with-file-manager.74105/
- SSH and SFTP for website users: https://docs.plesk.com/en-US/obsidian/administrator-guide/website-management/plesk-for-linux-enabling-ssh-access-for-website-users.80034/
- Git: https://docs.plesk.com/en-US/obsidian/customer-guide/git-support/using-remote-git-hosting.75848/
- Apache and nginx: https://docs.plesk.com/en-US/obsidian/customer-guide/websites-and-domains/hosting-settings/web-server-settings/apache-and-nginx-settings.72320/
- SSL It!: https://docs.plesk.com/en-US/obsidian/customer-guide/websites-and-domains/securing-connections-with-ssltls-certificates/securing-connections-with-the-ssl-it%21-extension.65160/
- Hosting settings (preferred domain): https://docs.plesk.com/en-US/obsidian/customer-guide/websites-and-domains/hosting-settings/general-settings/hosting-types.72051/
- PHP mail sender: https://support.plesk.com/hc/en-us/articles/12377673767191, external mail hosting: https://support.plesk.com/hc/en-us/articles/12377846922775
