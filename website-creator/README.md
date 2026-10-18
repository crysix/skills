# 🌐 website-creator

A skill for AI agents like Claude Code or Codex that walks you step by step through building a complete website: name and logo, research with real search data, copy, design direction, build, review, launch, and measuring afterwards on Google and in ChatGPT. It also works if you don't have a name or logo yet.

---

## At a glance

| | |
|---|---|
| **Runs in** | Claude Code, Codex and other agents that load skills |
| **Output** | a static HTML/CSS/JS site, online at milkycode webhosting (default) or the host of your choice |
| **Phases** | nine, each with a sign-off before the next one starts |
| **Design** | [impeccable](https://github.com/pbakaus/impeccable) plugin, against the generic AI look |
| **Animation** | [GSAP](https://gsap.com) with ScrollTrigger and SplitText, self-hosted |
| **Research** | DataForSEO (optional, about $1 per project) |
| **Country** | Germany by default, Austria and Switzerland included (legal pages, cookie law, selling online); for other countries the skill researches a profile from official sources |

---

## Installation

### Let Claude install it (easiest)

Give Claude Code the link to this skill and ask it to install it:

**For all projects**
```
Install the skill from https://github.com/crysix/skills/tree/main/website-creator globally so it is available in every project.
```

**For this project only**
```
Install the skill from https://github.com/crysix/skills/tree/main/website-creator in this project.
```

Claude downloads the folder and puts it in the right place: `~/.claude/skills/website-creator/` for all projects, `.claude/skills/website-creator/` for one project. If the skill doesn't show up right away, restart the agent once.

### Install manually

```bash
git clone https://github.com/crysix/skills.git ~/skills

# all projects
mkdir -p ~/.claude/skills && cp -r ~/skills/website-creator ~/.claude/skills/

# this project only (run inside the project)
mkdir -p .claude/skills && cp -r ~/skills/website-creator .claude/skills/
```

Use `ln -s` instead of `cp -r` to pick up updates with `git pull`.

- **Codex:** copy the folder to `~/.codex/skills/` instead.

---

## Usage

In Claude Code, type in an empty project folder:

```
/website-creator start
```

In other agents, just write: "Start the website-creator skill."

### Continuing later

The skill saves its progress in `WEBSITE-STATUS.md` in your project. If you continue a few days later, open a new chat in the project folder and say "Continue with the website-creator skill"; in Claude Code, `/website-creator continue` works too.

Other arguments: `/website-creator status` shows where the project stands, `/website-creator phase 3` jumps to a specific phase (the skill first checks that its inputs exist).

---

## Requirements

- an AI agent like Claude Code or Codex
- **impeccable**, a free design plugin. The skill sets it up with you at the start.
- **Python with Playwright** (recommended) for screenshots, brand extraction and check runs. Also set up at the start; on macOS and Linux in a virtual environment, because the system Python there usually refuses `pip install`.
- **DataForSEO** account for the research (optional), set up in phase 2. New accounts get $1 of trial credit, often enough for one project. If you like, sign up through my [affiliate link](https://dataforseo.com/?aff=f743f28f-d5b8-4e34-a66d-5c99089b7ca7), at no extra cost to you.
- **Web hosting** for the launch, set up in phase 7. The default is milkycode webhosting on Plesk, where the agent can deploy through the Plesk MCP. Other web space, Hostinger, Netlify, Vercel, Cloudflare, GitHub Pages or an own server work too; each has its own file in [hosting/](hosting/).

---

## How it works

### On every call

1. **Read the status file.** The skill first reads `WEBSITE-STATUS.md` in your project and picks up where it left off. Without one, it starts with phase 0.
2. **Load only what's needed.** Only the current phase file is loaded. Extra files (DataForSEO setup, cookies and terms), the chosen hosting file and sections of the country file come in only when a phase needs them.
3. **Work through the phase.** The skill asks only where a decision is yours, bundled into one message with a recommendation. Everything else it does itself.
4. **Wrap up.** It shows what was produced, updates the status file and asks whether to continue. After phases 1, 2, 3, 4 and 6 you sign off; without your OK, the next phase doesn't start.

### Rules that always apply

- **Nothing invented.** No made-up quotes, numbers, awards, prices or promises like "reply within 24 hours". Missing facts become open questions.
- **The brand is measured, not guessed.** Colors and fonts come from your live site, logo or brand files.
- **No generic AI look.** Design work goes through impeccable: several directions, a random draw against the obvious choice, and an independent reviewer at the end.
- **Copy without an AI ring.** [writing-rules.md](writing-rules.md) takes out buzzwords, dashes, groups of three and the other usual tells.
- **Credentials never in project files.** You enter API keys and tokens yourself, in your agent's personal configuration.
- **Nothing goes live without your OK.** Deployment, DNS changes and real test submissions only after you confirm.
- **Nothing gets deleted.** Old drafts move to `archive/`.
- **Bounded checks.** Build, check once, fix everything in one batch, at most a second pass.

### Country module

Everything that depends on the country lives in [countries/](countries/): domain and trademark check, search location codes, cookie law, legal pages, rules for selling online and official sources.

| File | Country |
|---|---|
| `de.md` | Germany, the default |
| `at.md` | Austria |
| `ch.md` | Switzerland |
| `other.md` | any other country: the agent builds a profile from official sources, with source and date for every fact |

The skill assumes Germany unless your existing site, your address or the conversation says otherwise, and says so in one line so you can correct it.

### Hosting module

Everything that depends on the host lives in [hosting/](hosting/), one file per option, each with the same sections: at a glance (cost, data location, form route, configuration, agent access), set up, configuration, deploy, updates, privacy, sources.

| File | Host |
|---|---|
| `milkycode.md` | milkycode webhosting on Plesk, the default; the agent can deploy through the Plesk MCP |
| `webspace.md` | other web space: IONOS, STRATO, ALL-INKL.COM, netcup, Hetzner, World4You, Hostpoint, cyon, Infomaniak |
| `hostinger.md` | Hostinger, with the Hostinger MCP |
| `netlify.md` | Netlify, with built-in forms |
| `vercel.md` | Vercel (business sites need Pro) |
| `cloudflare.md` | Cloudflare Workers |
| `github-pages.md` | GitHub Pages |
| `own-server.md` | an own server with Caddy or nginx |

The matching configuration templates are in [templates/hosting/](templates/hosting/). `build.py` versions every link to CSS and JS, so the hosts can let browsers cache them for a year and visitors still see changes right away.

### The nine phases

| Phase | Name | Result | Sign-off |
|---|---|---|---|
| 0 | Setup | core tools work, project folder, status file | |
| 1 | Foundation | real brand colors and fonts, or a new name and logo, `PRODUCT.md` | ✋ |
| 2 | Research | design references, keyword and GEO map, competitor analysis | ✋ |
| 3 | Copy | `copy.md` with every text on the page | ✋ |
| 4 | Design direction | one chosen, distinct visual world as a direction contract | ✋ |
| 5 | Build | finished site running locally, with structured data | |
| 6 | Review and polish | independent sign-off, tweak panel, `DESIGN.md` | ✋ |
| 7 | Launch | SEO and GEO technicals, cookie and terms check, legal pages, form, site online | |
| 8 | After launch | Search Console, aligned profiles, visibility measured again | |

Copy comes before design, so the layout is built for real content instead of placeholders. Research comes before copy, because keywords and competitors decide what goes into the headings.

### Phase by phase

**0 · Setup**
- Four questions in one message: existing site or brand, the site's goal, hosting, DataForSEO yes or no.
- Creates the project folders and the status file.
- Sets up impeccable and Python with Playwright (on macOS and Linux in a virtual environment) and records the working Python command.

**1 · Foundation**
- Existing brand: `extract_brand.py` measures colors and fonts on your live site.
- New brand: 8 to 12 name proposals with a domain check. You check the trademark registers yourself (DPMA, see.ip, Swissreg, depending on the country).
- Logo if needed: 6 to 9 SVG concepts, then 5 variants of the chosen one, then polish with a separate favicon.
- `/impeccable init` writes `PRODUCT.md`. The key question: who is the site for, and what should it achieve?

**2 · Research**
- Design references: your favorite sites plus design systems from refero.design. You pick one or two; notes record what's adopted and what isn't.
- Keywords and GEO: five DataForSEO queries for under $1 in total (search volume, Google results, ChatGPT answers, terms of the top pages). The result is a keyword map with a term for every spot on the page. Without DataForSEO, there is a manual route.
- Competitors: the real top 3 on Google are read completely and evaluated (common ground, gaps, structure), plus a table of how five to six competitors win visitors over.

**3 · Copy**
- `copy.md` holds every text: meta, sections, buttons, form, confirmation.
- Fact sentences that AI search engines can quote, plus a list of open questions.
- Every text is checked against the writing rules. Expect two to three rounds.

**4 · Design direction**
- impeccable derives several directions from your audience's world, draws against the obvious choice and builds a selection page.
- You pick one; it becomes the direction contract the build and review are measured against.

**5 · Build**
- Static HTML, CSS and a little JavaScript: self-hosted fonts, CSS variables, the form (via `mailto:` until phase 7), structured data, favicons.
- The first draft already has depth: sections set apart by color, processes as graphics, no empty sections.
- Animation with GSAP, self-hosted: headings build up with SplitText (still readable for screen readers), fade-ins and processes run with ScrollTrigger. Everything respects reduced motion, and the content stays visible without JavaScript.

**6 · Review and polish**
- `check_site.py`: screenshots on desktop and phone, console errors, horizontal scrolling, missing alt texts, heading order.
- `impeccable detect` for the typical AI patterns, then an independent reviewer without the chat history: ship, fix, rebuild or recapture.
- You review the site and set the final spacing yourself in the tweak panel (`?tweak`).
- `DESIGN.md` records the design system for later subpages and presentations.

**7 · Launch**
- SEO and GEO files: title, canonical, Open Graph, preview image, robots.txt, llms.txt, sitemap. Goal: Lighthouse above 90.
- Cookie and terms check by the country file. For an inquiry-only site, that's usually one sentence.
- Legal pages that fit the real site.
- Form target of your choice: own PHP script, form service, Netlify Forms or a webhook. You send the test inquiry.
- `build.py` packs only the files that go live and versions the CSS and JS links; the host configuration sets caching and security headers and blocks working files.
- Online only after your OK, by the route in the hosting file (MCP, CLI, SFTP or zip upload), followed by a live check.

**8 · After launch**
- Google Search Console and Bing Webmaster Tools.
- The fact sentences go onto all your profiles (LinkedIn, Google Business Profile, directories).
- After three to four weeks, the phase 2 measurements are repeated: rankings, ChatGPT answers, inquiries and where they came from.

---

## Costs

The skill itself costs nothing. DataForSEO is pay as you go: the research for one project is about $1. Hosting costs whatever the chosen host charges; the hosting files list the plans. Form services and consent tools are free up to their limits.

---

## File structure

```
website-creator/
├── SKILL.md              Process, rules and tools for the agent
├── README.md             This file
├── writing-rules.md      Rules for copy without an AI ring
├── countries/            de.md (Germany, default), at.md (Austria), ch.md (Switzerland),
│                         other.md (profile for any other country)
├── phases/               One file per phase, loaded only when that phase is up,
│                         plus setup files for DataForSEO, cookies and terms
├── hosting/              one file per host, same sections each: milkycode.md (default),
│                         webspace.md, hostinger.md, netlify.md, vercel.md, cloudflare.md,
│                         github-pages.md, own-server.md
├── templates/            Status file, robots.txt, llms.txt, sitemap.xml, hosting/ (.htaccess,
│                         _headers, _redirects, vercel.json, wrangler.jsonc, nginx.conf, Caddyfile),
│                         structured data, build script, form script, PHP form receiver,
│                         notification email, preview image, tweak panel
└── tools/
    ├── extract_brand.py  Measures colors and fonts of a live site
    └── check_site.py     Batched check run with screenshots
```

---

## Author

Christian Hinz ([@crysix](https://github.com/crysix))
