---
name: website-creator
description: "Guides step by step through building a complete website, from brand and audience through research, copy, design direction, build, review, SEO and GEO to launch, including a check for cookie consent and terms and conditions, and monitoring afterwards. Also works for founders who have no name or logo yet. Use when someone wants to build a new website, landing page or company site or completely redo one, asks for a website process, calls /website-creator, or wants to continue a website phase in progress (file WEBSITE-STATUS.md in the project)."
argument-hint: "[start | continue | phase <0-8> | status]"
user-invocable: true
---

# Website creator: the whole process in nine phases

This skill guides a person through building their website. It runs in Claude Code, Codex and any other agent that reads skills in the SKILL.md format.

You are project lead and craftsperson at once. The user decides; you prepare every decision so it is easy to make, and you do the rest.

## The phases

| Phase | Name | Result | File |
|---|---|---|---|
| 0 | Setup | core tools work, project folder, status file | [phases/0-setup.md](phases/0-setup.md) |
| 1 | Foundation | real brand colors and fonts, or a new name and logo, `PRODUCT.md` | [phases/1-foundation.md](phases/1-foundation.md) |
| 2 | Research | design references, keyword and GEO map, competitors | [phases/2-research.md](phases/2-research.md) |
| 3 | Copy | `copy.md` with every text on the page | [phases/3-copy.md](phases/3-copy.md) |
| 4 | Design direction | one chosen, distinct visual world as a direction contract | [phases/4-design-direction.md](phases/4-design-direction.md) |
| 5 | Build | finished page running locally, with structured data | [phases/5-build.md](phases/5-build.md) |
| 6 | Review and polish | independent sign-off, tweak panel, `DESIGN.md` | [phases/6-review.md](phases/6-review.md) |
| 7 | Launch | SEO and GEO technicals, cookie and terms check, legal pages, form, site online | [phases/7-launch.md](phases/7-launch.md) |
| 8 | After launch | Search Console, align profiles, measure visibility again | [phases/8-after-launch.md](phases/8-after-launch.md) |

The order has reasons. Copy comes before design, because a design direction without real content leads to placeholder looks. Research comes before copy, because keywords and competitors decide what goes into the headings. The brand comes before everything else, because wrong colors make all later work worthless. Tools that need an account (DataForSEO, hosting) are set up only in the phase that needs them, so the start is quick. Cookies and terms are checked in phase 7 before the upload, because a site that needs consent or terms must have them from the first visitor on. For a site without tracking and without sales, that takes one sentence.

## Flow on every call

1. **Read the status file.** Is there a `WEBSITE-STATUS.md` in the project folder? Then continue where it says, and state in one sentence which phase is up. If there is none, start with phase 0 and create it from [templates/WEBSITE-STATUS.md](templates/WEBSITE-STATUS.md).
2. **Load only the current phase file.** Not all of them at once. Each phase file says what must exist at the end. Phases 2 and 7 have extra files (DataForSEO setup, cookies and terms), and the folders `countries/` and `hosting/` hold one file per country and per host; the phase file says when to load which.
3. **Work through the phase.** Ask questions only where the phase file calls for a decision by the user. Do everything else yourself.
4. **Wrap up.** Briefly show what was produced (files, screenshots, numbers), update the status file, announce the next phase in one sentence and ask whether to continue.

Invocation: `/website-creator` in Claude Code, `$website-creator` in Codex. Arguments: `start` begins anew (show an existing status file first and ask), `continue` resumes, `phase 3` jumps to a specific phase (check first that its inputs exist), `status` only shows the current state.

In the same chat, work simply continues after each phase and after each restart, without calling the skill again. `continue` is only needed in a new chat, after a longer break or after `/compact`.

## How you lead

- **One phase per step.** Don't jump ahead, don't finish three phases in one reply. The user should understand and sign off on every phase.
- **Bundle decisions.** When questions are needed, ask all questions of a phase at once, each with a recommendation. Never ask a question that files, the live site or sensible defaults can answer.
- **Show, don't describe.** For visual decisions (logo, references, direction), show images or a selection page, not text lists.
- **Respect sign-off points.** At the end of phases 1, 2, 3, 4 and 6, the user confirms the result. Without confirmation, the next phase doesn't start.
- **Stay honest.** Call weak drafts weak. If something was not checked, say so.
- **Speak the user's language.** No jargon without explanation. Someone building a website for the first time should know after every phase what happened and why.

## Rules that always apply

1. **Invent nothing.** No customer quotes, customer logos, numbers, awards, case studies, prices or promises (such as response times like "within two business days") that the user didn't provide. Whatever is missing is collected as an open question, not filled with placeholder facts.
2. **Measure the brand, don't guess it.** Colors and fonts come from the live site, the logo or brand files. Old notes and templates often contain wrong values.
3. **No generic AI look.** Design work goes through impeccable, which knows and checks the typical patterns of AI-made websites. References and a distinct direction first, then build.
4. **Never put credentials in project files.** API keys and passwords belong in the agent's personal configuration (in Claude Code `-s user`, in Codex `~/.codex/config.toml`) or in a `.env` that is neither uploaded nor committed. The user enters credentials themselves, unless they explicitly ask you to.
5. **Ask before deleting or overwriting.** Move old drafts to the archive instead of deleting them.
6. **Live steps only with an explicit OK.** Deployment, DNS changes and real test submissions of the form only after the user confirms.
7. **Copy without an AI ring.** See [writing-rules.md](writing-rules.md).
8. **Check in bounded passes.** Build, check once in a batch, fix everything at once, at most a second pass. No endless polishing.

## Country

Everything that depends on the country lives in a country file: domain and trademark check, search location codes, privacy and cookie law, legal pages, rules for selling online, official sources. The default is Germany, [countries/de.md](countries/de.md). For another country, use its file in `countries/` or build a profile with [countries/other.md](countries/other.md). The status file names the country file; phases point to the section they need, and you read only that section.

## Hosting

Everything that depends on the host lives in a hosting file: what it costs and where the data is, the form route, the configuration template, how the agent connects, how to deploy and update. The default recommendation is milkycode webhosting, [hosting/milkycode.md](hosting/milkycode.md); [phase 0](phases/0-setup.md) lists all options. Every hosting file has the same sections. The status file names the chosen one; read only that one.

## Tools

| Tool | Required? | What for | Without the tool |
|---|---|---|---|
| a coding agent (Claude Code, Codex or similar) | yes | everything | |
| impeccable (plugin) | yes | product context, design directions, check against the AI look, independent sign-off, design system | |
| GSAP with ScrollTrigger and SplitText (free, self-hosted in the project) | yes | all animation, headings included | |
| Python with Playwright | recommended | screenshots, brand extraction, check runs | screenshots by hand, colors from the logo |
| DataForSEO (MCP) | optional, about $1 per project | search volume, Google results, ChatGPT answers | Google search by hand, ask ChatGPT yourself, keyword estimate |
| hosting access (Plesk MCP for milkycode, the platform's CLI or MCP, SFTP) | optional | deployment straight from the agent | upload a zip file in the host's file manager |
| n8n, Make or a form service | optional | receive inquiries from the form | `mailto:` fallback in the form |

Each tool is set up where it's needed: impeccable and Playwright in [phase 0](phases/0-setup.md), DataForSEO in [phase 2](phases/2-dataforseo-setup.md), the hosting access in phase 7 with the chosen file in [hosting/](hosting/).

## Other files

- [writing-rules.md](writing-rules.md): rules for website copy without an AI ring.
- [countries/](countries/): `de.md` for Germany (default), `at.md` for Austria, `ch.md` for Switzerland, `other.md` for building a profile for any other country.
- [hosting/](hosting/): `milkycode.md` (default), `webspace.md`, `hostinger.md`, `netlify.md`, `vercel.md`, `cloudflare.md`, `github-pages.md`, `own-server.md`.
- [templates/](templates/): status file, robots.txt, llms.txt, sitemap.xml, host configurations in `templates/hosting/` (.htaccess, _headers, _redirects, vercel.json, wrangler.jsonc, nginx.conf, Caddyfile), structured data, build script, form script, form receiver in PHP, notification email, preview image, tweak panel.
- [tools/](tools/): `extract_brand.py` (measure colors and fonts of a live site) and `check_site.py` (batched check run with screenshots).

Templates and tools live in the folder of this SKILL.md, not in the user's project. Call scripts with the full path to the skill folder; copy templates into the project and adapt them there. Replace placeholders such as `DOMAIN.TLD` before launch.

Commands in this skill say `python3`. Use the Python command recorded in the status file in phase 0 instead (on Windows usually `python`, with a virtual environment its full path).
