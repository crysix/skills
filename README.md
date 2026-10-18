# skills

My personal collection of skills for AI agents like Claude Code and Codex. Nothing fancy, just the stuff I use in my daily work.

## Skills

| Skill | What it does |
|---|---|
| [brainstorm](brainstorm/) | Runs a structured brainstorming session with proven ideation techniques |
| [discord-news](discord-news/) | Summarizes an article and posts it to a Discord channel via Claude in Chrome, after you confirm |
| [kleinanzeigen-listing](kleinanzeigen-listing/) | Turns a photo into a ready-to-paste Kleinanzeigen.de listing with a price suggestion |
| [motion-video](motion-video/) | Builds short explainer or ad videos with motion graphics, AI cutout images, voiceover and sound |

Every folder has a `SKILL.md` and a `README.md` with the details.

## Installation

Each skill's README has its own install section. The short version:

**Let Claude do it.** Give Claude Code the link to a skill folder and ask it to install it:

```
Install the skill from https://github.com/crysix/skills/tree/main/motion-video globally so it is available in every project.
```

Say "in this project" instead of "globally" to install it for the current project only.

**Or by hand.** Copy (or symlink) a skill folder to wherever your agent loads skills from:

- Claude Code, all projects: `~/.claude/skills/<skill>/`
- Claude Code, one project: `.claude/skills/<skill>/`
- Codex: `~/.codex/skills/<skill>/`
- claude.ai: zip the skill folder and upload it in the Skills settings

```bash
git clone https://github.com/crysix/skills.git ~/skills
mkdir -p ~/.claude/skills && ln -s ~/skills/motion-video ~/.claude/skills/motion-video
```

## License

MIT, see [LICENSE](LICENSE).
