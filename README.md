# skills

My personal collection of skills for AI agents like Claude Code and Codex. Nothing fancy, just the stuff I use in my daily work.

## Skills

| Skill | What it does |
|---|---|
| [brainstorm](brainstorm/) | Runs a structured brainstorming session with proven ideation techniques |
| [discord-news](discord-news/) | Summarizes an article and posts it to a Discord channel via Claude in Chrome, after you confirm |
| [grill-me](grill-me/) | Grills you about a plan or design, one question at a time, until every decision is settled |
| [kleinanzeigen-listing](kleinanzeigen-listing/) | Turns a photo into a ready-to-paste Kleinanzeigen.de listing with a price suggestion |
| [motion-video](motion-video/) | Builds short explainer or ad videos with motion graphics, AI cutout images, voiceover and sound |

Every folder has a `SKILL.md`, and most also have a `README.md` with the details.

## Usage

Copy (or symlink) a skill folder to wherever your agent loads skills from:

- Claude Code, all projects: `~/.claude/skills/<skill>/`
- Claude Code, one project: `.claude/skills/<skill>/`
- Codex: `~/.codex/skills/<skill>/`

```bash
git clone https://github.com/crysix/skills.git
ln -s "$PWD/skills/motion-video" ~/.claude/skills/motion-video
```

Or just drag a `SKILL.md` into a Claude Code chat and ask Claude to install it.

## License

MIT, see [LICENSE](LICENSE).
