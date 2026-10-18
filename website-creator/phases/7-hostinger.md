# Phase 7, step 6: Deploy with the Hostinger MCP

Load this file only if the site goes to Hostinger and the user has given the explicit OK to go online. Afterwards, continue with step 7 in [7-launch.md](7-launch.md).

If the hosting MCP isn't connected yet (check with `/mcp`), set it up now. Create an API token in the Hostinger panel under Account, API. The user enters the token themselves in the terminal, not in the chat:
- Claude Code: `claude mcp add hostinger -s user -e APITOKEN=<token> -- npx -y hostinger-api-mcp`, on Windows `-- cmd /c npx -y hostinger-api-mcp`. Add it globally (`-s user`): an MCP added only for one project is sometimes not loaded on Windows, because VS Code opens the path with a lowercase drive letter.
- Codex: `codex mcp add hostinger --env APITOKEN=<token> -- npx -y hostinger-api-mcp`
- Then restart the agent, reopen the same chat and continue.

1. If the domain is in a different Hostinger account than the hosting, move the domain to the main account first. Otherwise Hostinger demands a TXT ownership verification.
2. Create the website: `hosting_websites_create` (domain, hosting order). Then query `hosting_websites_list-setups` until the status is "completed". That takes a few minutes. Don't repeat the write command.
3. `python3 deploy/build.py`, copy the zip with a timestamp (`site_YYYYMMDD_HHMMSS.zip`), then `hosting_deploy-static-website` with the domain and the absolute path to the zip.
4. Check DNS (`dns_records_list`). With Hostinger domains, `@` (ALIAS) and `www` (CNAME) point to the Hostinger CDN; then nothing needs to change. Don't touch mail records (MX) and subdomains.
5. **Clear the cache:** `hosting_cache_clear-website`. Otherwise the CDN still serves the old site.
