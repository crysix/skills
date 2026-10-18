# 🌐 website-creator

A skill for AI agents like Claude Code or Codex that walks you step by step through building a complete website: name and logo, research with real search data, copy, design direction, build, review, launch, and measuring afterwards on Google and in ChatGPT. It also works if you don't have a name or logo yet.

---

## At a glance

| | |
|---|---|
| **Runs in** | Claude Code, Codex and other agents that load skills |
| **Output** | a static HTML/CSS/JS site, online on your own web space |
| **Phases** | nine, each with a sign-off before the next one starts |
| **Design** | [impeccable](https://github.com/pbakaus/impeccable) plugin, against the generic AI look |
| **Research** | DataForSEO (optional, about $1 per project) |
| **Country** | Germany by default (Impressum, privacy policy, cookie law, terms and conditions); for other countries the skill researches a profile from official sources |

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
- **Web hosting** for the launch, set up in phase 7. A Hostinger MCP makes deployment possible straight from the agent; without it, you upload a zip file.

---

## The nine phases

| Phase | Name | Result |
|---|---|---|
| 0 | Setup | core tools work, project folder, status file |
| 1 | Foundation | real brand colors and fonts, or a new name and logo, `PRODUCT.md` |
| 2 | Research | design references, keyword and GEO map, competitor analysis |
| 3 | Copy | `copy.md` with every text on the page |
| 4 | Design direction | one chosen, distinct visual world as a direction contract |
| 5 | Build | finished site running locally, with structured data |
| 6 | Review and polish | independent sign-off, tweak panel, `DESIGN.md` |
| 7 | Launch | SEO and GEO technicals, cookie and terms check, legal pages, form, site online |
| 8 | After launch | Search Console, aligned profiles, visibility measured again |

Copy comes before design, so the layout is built for real content instead of placeholders. Research comes before copy, because keywords and competitors decide what goes into the headings.

---

## What the skill makes sure of

- **Nothing invented.** No made-up quotes, numbers, awards or promises like "reply within 24 hours". Missing facts become open questions.
- **The brand is measured, not guessed.** Colors and fonts come from your live site, logo or brand files.
- **No generic AI look.** Several design directions from impeccable, a random draw against the obvious choice, and an independent reviewer at the end.
- **Copy without an AI ring.** [writing-rules.md](writing-rules.md) takes out buzzwords, dashes, groups of three and the other usual tells.
- **Credentials never in project files.** You enter API keys and tokens yourself, in your agent's personal configuration.
- **Nothing goes live without your OK.** Deployment, DNS changes and test submissions only after you confirm.

---

## Costs

The skill itself costs nothing. DataForSEO is pay as you go: the research for one project is about $1. Hosting is whatever your web space costs. Form services and consent tools are free up to their limits.

---

## File structure

```
website-creator/
├── SKILL.md              Process, rules and tools for the agent
├── README.md             This file
├── writing-rules.md      Rules for copy without an AI ring
├── countries/            de.md (Germany, default) and other.md (profile for any other country)
├── phases/               One file per phase, loaded only when that phase is up,
│                         plus setup files for DataForSEO, cookies and terms, Hostinger
├── templates/            Status file, robots.txt, llms.txt, sitemap.xml, .htaccess,
│                         structured data, build script, form script, PHP form receiver,
│                         notification email, preview image, tweak panel
└── tools/
    ├── extract_brand.py  Measures colors and fonts of a live site
    └── check_site.py     Batched check run with screenshots
```

---

## Author

Christian Hinz ([@crysix](https://github.com/crysix))
