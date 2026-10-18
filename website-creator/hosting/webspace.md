# Hosting: classic web space

Web space from a hosting company, uploaded by SFTP or the host's file manager. Covers IONOS, STRATO, ALL-INKL.COM, netcup, Hetzner, World4You, Hostpoint, cyon, Infomaniak and any other host whose web space reads `.htaccess`. For Plesk-based web space (netcup, among others), the Plesk settings in [milkycode.md](milkycode.md) apply. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | shared web space with Apache or LiteSpeed |
| Good for | sites with the PHP form script, data in Germany, Austria or Switzerland |
| Cost | the host's plan; check that the plan includes SFTP (see the table) |
| Data location | depends on the host (table) |
| Form | own PHP script [../templates/inquiry.php](../templates/inquiry.php), or a form service or webhook |
| Configuration | [../templates/hosting/.htaccess](../templates/hosting/.htaccess) |
| Agent access | none of these hosts has a deploy API or MCP: SFTP from the terminal, or the file manager by hand |

| Host | SFTP / SSH | HTTPS | PHP mail | Data location |
|---|---|---|---|---|
| IONOS | SFTP on port 22 (`accessNNN.webspace-data.io`) | own free certificate, activate under Domain & SSL; needs IONOS nameservers | sender must be a domain in the own contract | Europe, Germany page available |
| STRATO | SFTP and SSH on port 22, also in Starter; no zip extraction in the panel | own free certificate, assign under "SSL verwalten" | scripts can't use external mail servers; sender on the own domain | Germany (Berlin, Karlsruhe) |
| ALL-INKL.COM | FTPS in all plans, SFTP and SSH from Premium | Let's Encrypt in the KAS, included from PrivatPlus; needs ALL-INKL DNS | | Germany (Dresden) |
| netcup (web hosting) | SFTP and SSH for the main user | Let's Encrypt in Plesk | 250 mails an hour per mailbox | Nuremberg or Vienna; the "mnz" products are in the USA |
| Hetzner Webhosting | SFTP in all plans, SSH from L on port 222; web root `public_html` | Let's Encrypt in the SSL Manager | sender with `-f`; external SMTP only on port 587 | Germany |
| World4You (AT) | SFTP and SSH in all plans | Let's Encrypt, free | | Linz |
| Hostpoint (CH) | SFTP and SSH in all plans (switch on SSH first); web root `www/<domain>/` | FreeSSL (Let's Encrypt), usually automatic | set the sender in `.user.ini`: `sendmail_path = "/usr/sbin/sendmail -t -f <address>"` | Switzerland |
| cyon (CH) | SFTP and SSH in all plans; web root `public_html` | Let's Encrypt in my.cyon | envelope sender must match the From domain | Basel |
| Infomaniak (CH) | SFTP and SSH in paid plans; the free Starter has only plain FTP and no PHP | Let's Encrypt, install in the Manager | `mail()` is off by default, switch it on per site | Switzerland |

Hostinger has a deploy MCP and its own file: [hostinger.md](hostinger.md).

## Set up

1. The user books the plan (with SFTP, if the agent should upload) and connects the domain to the web space in the host's panel.
2. **HTTPS:** activate the certificate as shown in the table and switch on the redirect to HTTPS if the panel offers one; the `.htaccess` also forces it.
3. **SFTP access:** the user creates or looks up the SFTP login in the panel. Best with an SSH key instead of a password; the user keeps credentials out of the chat (in `~/.netrc`, the SSH config or an environment variable such as `LFTP_PASSWORD` with `lftp --env-password`).

## Configuration

- Copy [../templates/hosting/.htaccess](../templates/hosting/.htaccess) into the project folder and replace `DOMAIN.TLD`; `deploy/build.py` already has `HOST_FILES = [".htaccess"]`.
- **Form with `inquiry.php`:** the sender is an address on the own domain, created at the host; the script passes it with `-f`. Observe the host's rules in the table.

## Deploy

Only after the user's explicit OK.

1. `python3 deploy/build.py`
2. Upload by one of these routes:
   - **SFTP**, dry run first, then without `--dry-run`. `<webroot>` is the folder the domain points to:
     ```
     lftp -u <user> sftp://<host> -e "mirror -R --delete --verbose --dry-run -X .well-known/ dist/ <webroot>; quit"
     rsync -avz --delete --exclude .well-known/ --dry-run dist/ <user>@<host>:<webroot>/
     ```
     `rsync` needs SSH (Hetzner: add `-e 'ssh -p 222'`). In `lftp`, write `dist/` with and the target without a trailing slash, otherwise the upload lands in `<webroot>/dist/`. `--delete` removes everything on the server that isn't in `dist/`: check the dry run, and never point it at the account root. On Windows: WinSCP, Commands, Synchronize, direction "Remote", with "Delete files" and "Preview changes".
   - **File manager:** upload `dist.zip` into the web root and extract it there (where the panel can; STRATO and Hostpoint only via SSH), then delete the zip.

## Updates

- Classic web space has no CDN, so there is no cache to clear; browsers get new CSS and JS through the versioned links.
- Update flow for the status file: build, upload by the same route, check live.

## Privacy

- Every listed host offers a data processing agreement (AV-Vertrag, ADV); with most it's part of the terms, otherwise conclude it in the customer area. Name the host in the privacy policy.

## Sources

- IONOS: https://www.ionos.com/help/hosting/setting-up-and-managing-ftp-access/connection-details-for-ftp/sftp-in-ionos-web-hosting/, https://www.ionos.com/help/hosting/no-sending-of-emails-with-a-different-sender-address/
- STRATO: https://www.strato.de/faq/hosting/so-nutzen-sie-ihren-ssh-sftp-zugang/, https://www.strato.de/faq/domains/wie-kann-ich-mein-kostenfreies-strato-ssl-zertifikat-verwenden/
- ALL-INKL.COM: https://all-inkl.com/en/support/tutorials/kas/ssl-protection/ssl-certificate/how-to-install-a-lets-encrypt-certificate_470.html, https://all-inkl.com/en/about-us/datacenter
- netcup: https://www.netcup.com/en/helpcenter/documentation/web-hosting/interface, https://www.netcup.com/en/about-netcup/server-locations
- Hetzner: https://docs.hetzner.com/managed/administration-on-konsoleh/access-details/ftp-sftp/, https://docs.hetzner.com/managed/administration-on-konsoleh/access-details/ssh/
- World4You: https://faq.world4you.com/en/articles/4708-can-i-access-my-webspace-via-ssh
- Hostpoint: https://support.hostpoint.ch/en/products/webhosting/first-steps/how-do-i-connect-to-my-server-via-ftp-sftp, https://support.hostpoint.ch/en/products/webhosting/frequently-asked-questions/sending-e-mails-through-your-website
- cyon: https://www.cyon.ch/support/a/sftp, https://www.cyon.ch/support/a/kontaktformular-richtig-konfigurieren
- Infomaniak: https://www.infomaniak.com/en/support/faq/446/understanding-web-transfer-protocols, https://www.infomaniak.com/en/support/faq/2150/php-function-mail-send-mail-from-server
- lftp: https://lftp.yar.ru/lftp-man.html, rsync: https://download.samba.org/pub/rsync/rsync.1, WinSCP: https://winscp.net/eng/docs/task_synchronize_full
