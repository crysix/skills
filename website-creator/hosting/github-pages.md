# Hosting: GitHub Pages

Free static hosting from a GitHub repository. Facts as of October 2026.

## At a glance

| | |
|---|---|
| Type | static hosting from a repository, US company (GitHub, Microsoft) |
| Good for | personal, project and association sites. For business sites a grey area: GitHub Pages "is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site". Never for shops |
| Cost | free with a public repository |
| Data location | USA; GitHub logs visitors' IP addresses |
| Form | no PHP: form service or webhook |
| Configuration | no own HTTP headers possible (no security headers, browser cache fixed at about 10 minutes); `.nojekyll` and `CNAME` |
| Agent access | `git` and the GitHub CLI `gh` |

## Set up

1. The user creates the account at github.com and signs in the CLI: `gh auth login`.
2. **A separate public repository for the built site only**, for example `<user>/<domain>`. Never publish the project folder itself: research, copy, `PRODUCT.md` and the status file would be public.
3. **Domain:** in the repository under Settings, Pages, Custom domain. DNS for the apex: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and AAAA records `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`; for www a CNAME to `<user>.github.io`. GitHub redirects between apex and www automatically. No wildcard DNS records.
4. **Protect the domain:** verify it in the user's or organization's settings (TXT record `_github-pages-challenge-<user>.<domain>`), so nobody else can take it over.
5. **HTTPS:** tick "Enforce HTTPS" in the Pages settings; it can take up to 24 hours to become available. If the domain has CAA records, one must allow `letsencrypt.org`.

## Configuration

- In the project folder: an empty file `.nojekyll` and a file `CNAME` containing only the domain. In `deploy/build.py`: `HOST_FILES = [".nojekyll", "CNAME"]`.
- No `.htaccess`, no `_headers`: GitHub Pages ignores them.

## Deploy

Only after the user's explicit OK.

First deploy:
```
python3 deploy/build.py
cd dist
git init -b main
git add -A
git commit -m "Publish site"
gh repo create <user>/<repo> --public --source=. --push
```
Then in the repository under Settings, Pages: Source "Deploy from a branch", branch `main`, folder `/ (root)`. `build.py` keeps `dist/.git` on rebuilds.

## Updates

- `python3 deploy/build.py`, then in `dist/`: `git add -A`, `git commit -m "Update"`, `git push`.
- Changes can take up to 10 minutes to appear.
- Update flow for the status file: build, commit and push in `dist/`, check live.

## Privacy

- GitHub logs the IP address of every visitor for security purposes. GitHub states compliance with the EU-US Data Privacy Framework; its data processing agreement applies only under a written GitHub customer agreement, not to a normal free account. That's a weak point for business sites.
- Name GitHub in the privacy policy as host.

## Sources

- Publishing source: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Custom domain: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site, verification: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
- HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- Limits and acceptable use: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Privacy: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages, https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
