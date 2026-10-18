# 📢 discord-news

A Claude skill that automatically summarizes articles and news and posts them to a configured Discord channel — via browser automation, with your confirmation before sending.

---

## What does this skill do?

Share a link with Claude. The skill fetches the article, extracts the key information, and composes a structured Discord message with a title, summary, bullet points, and source link. Claude shows you the finished message in the input field — and only posts it after your explicit "yes".

**Example output in Discord:**

```
🤖 **OpenAI and Microsoft — A New Phase** 🤝

The partnership has been fundamentally restructured. Here's what's changing.

• Microsoft remains the primary cloud partner
• OpenAI can now use other cloud providers as well
• New license structure runs until 2032, but is no longer exclusive
• Both sides retain access to jointly developed models

🔗 https://openai.com/index/next-phase
```

---

## Requirements

- **Claude** (claude.ai or Claude Code) with the **Claude in Chrome** extension enabled
- Chrome browser with Discord open in a tab (Discord Web)
- You must be logged into Discord

---

## Installation

### 1. Install the skill

**Let Claude install it (easiest).** Give Claude Code the link to this skill and ask it to install it. You can pass your channel details in the same message, then Claude fills in the configuration as well:

**For all projects**
```
Install the skill from https://github.com/crysix/skills/tree/main/discord-news globally so it is available in every project. Configure it for https://discord.com/channels/SERVER_ID/CHANNEL_ID (server "my-server", channel "#news", posts in English).
```

**For this project only**
```
Install the skill from https://github.com/crysix/skills/tree/main/discord-news in this project. Configure it for https://discord.com/channels/SERVER_ID/CHANNEL_ID (server "my-server", channel "#news", posts in English).
```

Claude downloads the folder and puts it in the right place: `~/.claude/skills/discord-news/` for all projects, `.claude/skills/discord-news/` for one project.

**Install manually:**

```bash
git clone https://github.com/crysix/skills.git ~/skills

# all projects
mkdir -p ~/.claude/skills && cp -r ~/skills/discord-news ~/.claude/skills/

# this project only (run inside the project)
mkdir -p .claude/skills && cp -r ~/skills/discord-news .claude/skills/
```

- **Codex:** copy the folder to `~/.codex/skills/` instead.
- **claude.ai:** configure `SKILL.md` first (step 2), then zip the `discord-news` folder and upload it in the Skills settings.

### 2. Configure the skill

If you didn't pass your channel details when installing, edit the installed `SKILL.md` and replace the placeholders under the **Configuration** section with your own values:

| Placeholder | Replace with | Example |
|---|---|---|
| `YOUR_SERVER_NAME` | Your Discord server name | `milkycode` |
| `YOUR_CHANNEL_NAME` | Target channel name | `#news` |
| `YOUR_SERVER_ID` | Server ID from the channel URL | `123456789012345678` |
| `YOUR_CHANNEL_ID` | Channel ID from the channel URL | `987654321098765432` |
| `YOUR_POST_LANGUAGE` | Language the posts are written in | `English` |

**How to find your Server ID and Channel ID:**

1. Open Discord → right-click the channel → **Copy Link**
2. The link looks like: `https://discord.com/channels/SERVER_ID/CHANNEL_ID`
3. Copy both numbers into the corresponding fields in `SKILL.md`

> **Tip:** Enable Developer Mode in Discord (Settings → Advanced → Developer Mode) to right-click and copy IDs directly.

---

## Usage

Share a link with Claude and use any of these triggers:

```
https://example.com/article   →   post this to DC
https://example.com/article   →   make a discord news post
https://example.com/article   →   share this on Discord
https://example.com/article   →   DC post
```

Or more explicitly:

```
Post this article to the Discord channel: https://example.com/article
```

A link on its own, without asking to post it, does **not** trigger the skill.

Claude will then automatically:

1. **Fetch the article** — extract title, key takeaways, and important facts
2. **Open Discord** — navigate to the configured channel
3. **Type the message** — formatted with emoji, bold title, and bullet points
4. **Show a screenshot** — so you can review the message before it's sent
5. **Wait for your OK** — only posts after you confirm with "yes"
6. **Confirm** — takes a final screenshot of the sent message

---

## Message Format

```
[Emoji] **Article Title** [optional emoji]

Short summary in 1–2 sentences.

• Key point one
• Key point two
• Key point three
[up to 6 bullet points]

🔗 https://original-url.com
```

The whole message stays under Discord's limit of 2,000 characters.

**Emoji is chosen automatically based on topic:**

| Emoji | Topic |
|---|---|
| 🔴 | Breaking news / important alert |
| 🤖 | AI / tech |
| 💼 | Business / economy |
| 🔒 | Security / privacy |
| 🚀 | Startups / launches |
| 🌍 | Politics / society |
| 💡 | Innovation / science |

---

## FAQ

**The skill opens Discord but can't find the message input field.**
Make sure the Discord tab is open and visible in Chrome. Reloading the Discord tab usually helps.

**I'm not logged into Discord.**
Claude will wait and let you know. Just log in and the workflow continues automatically.

**The article can't be fetched (paywall, etc.).**
Claude will ask if you want to paste the content manually. Just copy the article text into the chat and Claude will work with that.

**I want to post to a different channel.**
Open `SKILL.md` and update the channel URL and names under the **Configuration** section.

---

## Safety

Claude will **never** post without your explicit confirmation. You always see a screenshot of the prepared message first and are asked whether it should be sent.

---

## Author

Christian Hinz ([@crysix](https://github.com/crysix))
