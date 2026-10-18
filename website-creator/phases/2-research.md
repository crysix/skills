# Phase 2: Research

Goal: Three results that carry all later phases. First, design references with a clear statement of what is adopted. Second, a keyword and GEO map. Third, a competitor analysis: why the top pages rank first on Google and how competitors win visitors over.

## A. Design references

Without role models, the agent invents the average of all websites. So references come first.

1. **The user's favorite sites:** ask for three to five addresses, from any industry.
2. **Find matching design systems:** on styles.refero.design, find five systems that fit the brand and the offer.
   - The gallery loads via JavaScript, and a headless browser gets error 403. With visible Chrome through Playwright (`headless=False`, `channel="chrome"`), the site's search works.
   - Go through many search terms (industry, main color, style such as "editorial", "personal", "studio"), filter by color closeness to the brand, compare screenshots, then read the design-system pages of the finalists.
3. **Show an overview:** all candidates side by side as an image (an overview graphic or HTML page); the user picks one or two.
4. **Record**, per chosen reference in `references/notes.md`: what is adopted (typography, layout, use of color, motion, imagery) and what explicitly isn't.

For example: reference A provides the base world (lots of white space, one large image), reference B the opening with a strong color field. The 3D graphic of reference B is explicitly dropped.

5. **New brand only: colors and fonts.** From the chosen references, derive two to three palettes with a font pairing and show them on a preview page (surfaces, text, button, logo in the colors, contrast measured). The user picks. Then color the logo family from phase 1 and fill in the brand profile in the status file.

## B. Keyword and GEO research

GEO means appearing in the answers of ChatGPT, Perplexity and Google's AI Overviews. That depends on different things than a Google ranking, so both are measured.

### Set up DataForSEO (if wanted and not connected yet)

First check whether the DataForSEO MCP is already connected (in Claude Code and Codex with `/mcp`). If not, set it up now. Briefly explain what it's for: real search volumes from Google, the current Google results and the answers of ChatGPT with web search. Pay as you go, no subscription.

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

### With DataForSEO (five queries, under one dollar in total)

1. **Search volume** for 30 to 40 terms the audience might type: service, service plus audience, service plus location, problems, questions. Endpoint `keywords_data/google_ads/search_volume/live`, set country and language to match (Germany: `location_code 2276`, `language_code de`). The MCP's short mode only shows ten results; use the full mode for all results.
2. **Google results** for the two most important terms: `serp/google/organic/live/advanced`. Shows the competitors, the questions from "People also ask" and which sources Google's AI Overview cites.
3. **ChatGPT answers** with web search: `ai_optimization/chat_gpt/llm_responses/live`. Three questions:
   - a question as a customer would ask it ("Who helps mid-sized companies with …?"),
   - a local or specialized question,
   - a direct question about the person or brand ("What do you know about …?").
4. **Terms of the top pages:** for the three best-ranked provider pages from query 2 (see C), the terms they rank for on Google: `dataforseo_labs/google/ranked_keywords/live` with the domain or URL of the page, `limit` 100, sorted by search volume. Shows terms you wouldn't think of yourself. Costs about two cents per page (as of October 2026).
5. Before starting, check the balance once (`appendix/user_data`) and tell the user the expected cost.

### Without DataForSEO

- Google search in a private window for the main terms; note competitors and "People also ask".
- Google autocomplete for term variants.
- Have the user ask ChatGPT and Perplexity the three questions above themselves and copy the answers into the research.
- Compare volume roughly via Google Trends. Note in the map that numbers are missing.
- Read the terms of the top pages from their page titles and headings (see C).

### Result: `research/keywords-geo.md`

1. Table with term, search volume, competition, assessment.
2. Who ranks at the top on Google, what the AI Overview cites.
3. What ChatGPT answers, split into general questions and the question about the brand.
4. **Keyword map:** one term for each spot on the page (page title, meta description, H1, every section, FAQ).
5. GEO measures (fact sentences, the same facts on all profiles, structured data, FAQ with real questions, llms.txt).
6. Topics for later subpages. A single page can't rank for everything.

Two things that almost always apply:
- The main term is usually highly contested. Variants with audience or location are realistic.
- **Always ask about the own brand.** AI search engines describe a person or company from everything they find: old website, LinkedIn, industry directories. If something wrong is there, such as a wrong headcount, they repeat it.

## C. Analyze competitors

Result in `research/competitors.md`, in two parts. Both are the basis for phase 3.

### Top 3 on Google: why they rank first

This is how SEO agencies work: whoever ranks at the very top for their own service without ads is evidently doing a lot right with terms, topics and structure. That gets read and evaluated.

1. **Pick niche terms, not the biggest ones.** For query 2, take the two terms that describe the offer exactly, i.e. service plus audience or service plus location (for example "AI for trade businesses" instead of "AI consulting"), even if they have less search volume. General terms bring up general providers that are no role models for this site. Name the two terms to the user before the query and have them confirmed.
2. **Real competitors only.** From the results, take the three best-ranked pages that offer the same service to the same audience. Ads, directories, portals, comparison sites, publishers' guide articles and Wikipedia don't count; they rank for other reasons. If the top ten don't contain three matching providers, query the next niche term. Briefly show the user the selection before reading the pages.
3. Read each page completely (fetch the page or open it with Playwright) and record:

| Page | Position for which term | Page title | Meta description | H1 | H2 outline | Where the main term appears | Variants and related terms | Topics and questions covered | Text length (words) | FAQ | Structured data |
|---|---|---|---|---|---|---|---|---|---|---|---|

4. Add the terms from query 4 that the three pages rank for. Keep only terms that fit the own offer. Whatever the pages win with other services or topics is dropped.
5. Below that, evaluate:
   - **Common ground:** Which topics, questions and terms do all three have? Google evidently expects them for this search term; the own page needs them too.
   - **Gaps:** What does none of the three answer, even though it shows up in "People also ask", in the ChatGPT answers or in the keyword table? That's where the own page can be better.
   - **Structure:** How many sections, where does the main term sit (title, H1, first H2), roughly how long is the text. That gives the frame for phase 3. More text is not a goal in itself.
   - **New terms** with real search volume that are still missing go into the keyword map.

Important for expectations: the top pages rank not only because of their copy, but also because of links from other sites and the age of their domain. A new site therefore won't stand next to them right away. Topics, terms and outline are adopted, never wording. The goal is to answer the same questions more concretely and better.

### How competitors win visitors over

Five to six pages: the three from above, the providers ChatGPT names, and one provider with a profile similar to the user's. Per page, record:

| Page | H1 | Subline | Buttons | Trust signals | Process | Concrete numbers | FAQ | Tone |
|---|---|---|---|---|---|---|---|---|

Below that, three to five patterns of the strong pages and the mistakes of the weak ones.

## Sign-off

Show the chosen references with adoption notes, the keyword map, what the top 3 have in common, the most important gap and the three most important findings. Clarify strategic questions the research raises (example: local focus yes or no). Only continue after confirmation.

## Done when

- [ ] One or two references chosen, with notes on what to adopt and what to leave out.
- [ ] For a new brand: colors and fonts chosen, logo colored, brand profile filled in.
- [ ] `research/keywords-geo.md` with keyword map.
- [ ] `research/competitors.md` with the analysis of the top 3 (common ground, gaps, structure) and the table of patterns.
- [ ] The user has confirmed.

Next: [Phase 3: Copy](3-copy.md).
