# Hosting: own server

A virtual server (VPS) at a provider such as Hetzner or netcup, with Caddy or nginx. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | own server with root access |
| Good for | people who already run servers; full control |
| Cost | the server, often a few euros a month |
| Data location | the data center chosen at the provider |
| Form | a form service or webhook is simplest. `inquiry.php` needs PHP-FPM and a mail relay on port 587 (Hetzner Cloud blocks ports 25 and 465 by default) |
| Configuration | [../templates/hosting/Caddyfile](../templates/hosting/Caddyfile) (simpler, automatic HTTPS) or [../templates/hosting/nginx.conf](../templates/hosting/nginx.conf) |
| Agent access | SSH and rsync |

Updates of the operating system, the firewall and backups are the operator's job. If nobody looks after that, choose web space instead.

## Set up

1. Server with a current Debian or Ubuntu, SSH login with a key, a user for deployments (here `deploy`) with write access to `/var/www/DOMAIN.TLD`.
2. DNS: A and AAAA records for the domain and for www point to the server; ports 80 and 443 open.
3. **Web server, one of:**
   - **Caddy:** install from Caddy's apt repository (https://caddyserver.com/docs/install), put [../templates/hosting/Caddyfile](../templates/hosting/Caddyfile) at `/etc/caddy/Caddyfile`, replace `DOMAIN.TLD`, then `sudo systemctl reload caddy`. Caddy gets and renews the certificates itself.
   - **nginx with certbot:** start with only the port-80 block of [../templates/hosting/nginx.conf](../templates/hosting/nginx.conf), install certbot (`sudo snap install --classic certbot`, `sudo ln -s /snap/bin/certbot /usr/local/bin/certbot`), get the certificate with `sudo certbot certonly --nginx -d DOMAIN.TLD -d www.DOMAIN.TLD --deploy-hook "systemctl reload nginx"`, then add the two 443 blocks and run `sudo nginx -t && sudo systemctl reload nginx`. Test renewal with `sudo certbot renew --dry-run`. On nginx 1.24 (Ubuntu 24.04), replace `http2 on;` as the template notes.
4. Renewal has to run automatically: Let's Encrypt certificates get shorter, 64 days from February 2027 and 45 days from February 2028.

## Configuration

- The server configuration lives on the server, not in `dist/`. In `deploy/build.py`: `HOST_FILES = []`.
- Both templates force HTTPS, redirect www to the address without www, set security and cache headers and block hidden and working files. In nginx, never add `add_header` inside a `location` block: it drops the security headers there.

## Deploy

Only after the user's explicit OK.

1. `python3 deploy/build.py`
2. Dry run first, then without `--dry-run`:
   ```
   rsync -avz --delete --chmod=D755,F644 --dry-run dist/ deploy@<server>:/var/www/DOMAIN.TLD/
   ```
   `--delete` removes everything in the target that isn't in `dist/`; check the dry run.

## Updates

- No CDN in front, so there is no cache to clear; browsers get new CSS and JS through the versioned links.
- Update flow for the status file: build, rsync, check live.

## Privacy

- Conclude the data processing agreement with the server provider and name it in the privacy policy, with the data center location. The web server's access logs contain IP addresses: say so in the privacy policy, and keep them short (for example by rotating them after a few days).

## Sources

- nginx: https://nginx.org/en/docs/http/ngx_http_headers_module.html, https://nginx.org/en/docs/http/ngx_http_core_module.html
- certbot: https://certbot.eff.org/instructions?ws=nginx&os=snap
- Caddy: https://caddyserver.com/docs/install, https://caddyserver.com/docs/automatic-https, https://caddyserver.com/docs/caddyfile/directives/header
- Certificate lifetimes: https://letsencrypt.org/2025/12/02/from-90-to-45/
- rsync: https://download.samba.org/pub/rsync/rsync.1
- Hetzner Cloud mail ports: https://docs.hetzner.com/cloud/servers/faq/
