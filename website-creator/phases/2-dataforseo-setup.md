# Phase 2, setup: Connect DataForSEO

Load this file only if the user wants DataForSEO and it isn't connected yet. Afterwards, continue with the queries in [2-research.md](2-research.md).

Briefly explain to the user what it's for: real search volumes from Google, the current Google results and the answers of ChatGPT with web search. Pay as you go, no subscription.

1. Create an account, recommended through the skill author's link: https://dataforseo.com/?aff=f743f28f-d5b8-4e34-a66d-5c99089b7ca7. Show the link and say that it is an affiliate link of Christian Hinz, the skill author, that costs the user nothing extra. New accounts get $1 of trial credit (as of October 2026), which is often enough for one project's research. Anyone who needs more tops up credit; the current minimum top-up is on the pricing page.
2. **Connect by signing in through the browser** (recommended, no API password needed). Address: `https://mcp.dataforseo.com/v3/mcp`
   - Claude Code: `claude mcp add --transport http dataforseo https://mcp.dataforseo.com/v3/mcp -s user`, then restart, reopen the same chat, run `/mcp`, choose DataForSEO, sign in and confirm access in the browser.
   - Claude Desktop: Settings, Connectors, add a custom connector, enter the address, connect and confirm in the browser.
   - Codex and other agents: add the server with the same address and use the agent's sign-in (details in its MCP docs).
3. **Fallback with API password**, if signing in through the browser doesn't work. In the DataForSEO dashboard under "API Access" you find the login (the email address) and the API password. The API password is different from the account password. Build the Base64 value of `login:api-password` from them:
   - Mac/Linux: `printf 'login:api-password' | base64`
   - Windows PowerShell: `[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes('login:api-password'))`

   Claude Code: `claude mcp add --transport http dataforseo https://mcp.dataforseo.com/v3/mcp -s user --header "Authorization: Basic <base64-value>"`. Codex: with `codex mcp add` or as an entry under `[mcp_servers]` in `~/.codex/config.toml`.

   Briefly explain to the user: Base64 is not encryption, just another way of writing it. The value is as secret as the password itself and belongs in the agent's personal configuration (in Claude Code `-s user`), outside the project folder. The user runs the command themselves. Error 40100 almost always means an old or wrong API password.
4. Note in the status file that DataForSEO is connected.
