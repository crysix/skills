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

- **Claude.ai** with the **Claude in Chrome** extension enabled
- Chrome browser with Discord open in a tab (Discord Web)
- You must be logged into Discord

---

## Installation

### 1. Download the skill file

Download `discord-news.skill` from this repository.

### 2. Import into Claude

Go to [claude.ai](https://claude.ai) → **Skills** → **Import skill** → select `discord-news.skill`.

### 3. Configure the skill

After importing, open the skill and edit `SKILL.md`. Replace the placeholders under the **Konfiguration** section with your own values:

| Placeholder | Replace with | Example |
|---|---|---|
| `DEIN_SERVER_NAME` | Your Discord server name | `milkycode` |
| `DEIN_CHANNEL_NAME` | Target channel name | `#news` |
| `DEINE_SERVER_ID` | Server ID from the channel URL | `123456789012345678` |
| `DEINE_CHANNEL_ID` | Channel ID from the channel URL | `987654321098765432` |

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
Open `SKILL.md` and update the channel URL and names under the **Konfiguration** section.

---

## Safety

Claude will **never** post without your explicit confirmation. You always see a screenshot of the prepared message first and are asked whether it should be sent.
