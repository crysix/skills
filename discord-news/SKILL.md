---
name: discord-news
description: Posts news, articles and announcements to a configured Discord channel via browser automation. Use this only when the user explicitly asks to post something on Discord, e.g. "post this to DC", "make a discord news post", "share this on Discord", "post this in the channel", "Discord message", "DC post" (or German equivalents such as "poste das im DC", "mach discord news", "teile das auf Discord"). A link shared without such a request does not trigger this skill. Once asked, start right away; do not ask whether the skill should be used.
---

# Discord News Skill

Posts formatted news messages to the configured Discord channel via browser automation.

## Configuration

- **Server:** YOUR_SERVER_NAME
- **Channel:** YOUR_CHANNEL_NAME
- **Channel URL:** https://discord.com/channels/YOUR_SERVER_ID/YOUR_CHANNEL_ID
- **Post language:** YOUR_POST_LANGUAGE (e.g. English or German)

---

## Workflow

### Step 1: Extract the article

Fetch the content of the shared link with your web fetch tool, or navigate to the URL in the browser. Extract:
- the article's **title**
- the **main message** (2–3 sentences)
- the **key points** (3–6 bullet points)
- the **original URL** (for the link at the end)

### Step 2: Navigate to the Discord channel

Navigate to the channel URL:
```
https://discord.com/channels/YOUR_SERVER_ID/YOUR_CHANNEL_ID
```

Wait until Discord has fully loaded. If a login is required, tell the user and wait.

### Step 3: Find the input field

Use the browser's find tool (`find` in Claude in Chrome) with a natural-language description such as:
- "message input field in the Discord channel"
- "text box for writing a message"

Click the field to focus it.

### Step 4: Type the message

> ⚠️ **CRITICAL: line breaks in Discord**
> Discord sends the message on `Enter`. Line breaks **must use `Shift+Enter`**.
> **Never** put `\n` into a string. Type each line separately and end it with `Shift+Enter`.

Write the message in the configured post language and type it **line by line** in this format:

```
[Emoji] **Bold title** [optional emoji]
[Shift+Enter]
[Shift+Enter]
One or two sentences summarizing the article.
[Shift+Enter]
[Shift+Enter]
• Key point 1
[Shift+Enter]
• Key point 2
[Shift+Enter]
• Key point 3
[Shift+Enter]
[more bullet points if needed]
[Shift+Enter]
[Shift+Enter]
🔗 https://original-url.com/article
```

**Emoji choice** (pick one that fits the topic):
- 🔴 Breaking news / important alert
- 🤖 AI / tech
- 💼 Business / economy
- 🔒 Security / privacy
- 🚀 Startups / launches
- 🌍 Politics / society
- 💡 Innovation / science

**Formatting rules:**
- Title in `**bold**` (two asterisks)
- Bullet points with the `•` character
- At most 6 bullet points; keep them concise
- Summary: 1–2 sentences, no jargon
- Always put the URL at the end as plain text (not a Markdown link)
- The whole message must stay under Discord's limit of 2,000 characters

### Step 5: Screenshot and confirmation

Take a screenshot that shows the finished message in the input field. Show it to the user and ask:

> "The message is ready. Should I send it now?"

**Wait for an explicit yes.** Never send automatically.

### Step 6: Send and confirm

Only after an explicit "yes" / "send" / "go":
1. Press `Enter` to send the message
2. Wait briefly until the message appears
3. Take a final screenshot as confirmation
4. Tell the user: "✅ Posted!"

---

## Format example

```
🤖 **OpenAI and Microsoft — A New Phase** 🤝

The partnership has been fundamentally restructured. Here are the key changes.

• Microsoft remains the primary cloud partner
• OpenAI can now use other cloud providers as well
• New license structure runs until 2032, but is no longer exclusive
• Both sides retain access to jointly developed models

🔗 https://openai.com/index/next-phase
```

---

## Error cases

| Problem | Solution |
|---|---|
| Not logged into Discord | Tell the user and wait until they have logged in |
| Input field not found | Take a screenshot and ask the user for help |
| Article cannot be fetched | Ask the user whether they want to paste the content manually |
| Message over 2,000 characters | Shorten the bullet points, use at most 4 instead of 6 |
