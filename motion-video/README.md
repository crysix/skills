# 🎬 motion-video

A skill that lets Claude Code (or Codex and other agents that load skills) produce short explainer videos and ad spots on its own. The motion graphics are built in code, characters and objects are added as AI-generated cutout images, and an ElevenLabs voiceover plus sound design complete the video. The result is a finished MP4.

Developed and maintained by **milkycode GmbH**: [https://www.milkycode.com](https://www.milkycode.com)

---

## At a glance

| | |
|---|---|
| **Runs in** | Claude Code, Codex and other agents that load skills |
| **Output** | MP4 with voiceover and sound |
| **Images** | GPT Image 2.5 (Flare), transparent cutouts |
| **Voice** | ElevenLabs v4 (`eleven_v4`) |
| **Rendering** | Higgsfield Katana (cloud) or HyperFrames (local) |

---

## What does this skill do?

You give Claude the topic and the constraints. Claude decides the look, scenes, image motifs, animations, pacing and sound itself, based on the video's purpose and audience.

The skill prescribes very little about *how* Claude builds the video. It mostly describes what a good result looks like and sets the frame. That is intentional: current models such as Opus 5.5 do better when they know the goal and the constraints than when they are given every step.

**What a good result looks like, according to the skill:**
- Everything moves: typography, interface elements, diagrams, transitions and the background. Still images with text on top are not enough.
- AI images are cutout building blocks in one consistent style, animated and combined, not a slideshow of full-frame pictures.
- Every scene has its own visual idea. The same illustration does not keep coming back.
- Every animation is timed to the spoken word, using word timestamps from the finished recording.
- The script is written to be spoken, in complete, natural sentences.
- An explainer opens with the question it answers.
- An ad hooks viewers in the first seconds, shows the benefit and ends with a clear call to action.
- Text and logos are never drawn by the image model. Text is set in code, and logos come from the original files.
- Sounds sit on the accents, and loudness is platform-ready (about -14 to -16 LUFS).

---

## Requirements

- **An agent that loads skills:** Claude Code (CLI, desktop app or IDE extension), Codex or similar.
- **An [ElevenLabs](https://elevenlabs.io) account** for the voice, reachable through an ElevenLabs connector or an API key in an environment variable (for example `ELEVENLABS_API_KEY`).
- **One of the four routes** below. Route 1 needs a Higgsfield plan with MCP access. Routes 2 to 4 need Node.js and ffmpeg on your machine, plus an API key from the image provider.

---

## The four routes

On the first run you choose how the video is produced. The route determines what renders the video and where images, word timestamps and sounds come from.

| # | Route | Rendering | Images | Word timestamps | Sounds |
|---|---|---|---|---|---|
| 1 | **Higgsfield Katana** | Higgsfield cloud sandbox | Higgsfield | Whisper in the sandbox | built-in library (300+ royalty-free sounds) |
| 2 | **HyperFrames + kie.ai** | local | [kie.ai](https://kie.ai) | ElevenLabs alignment or Whisper | your own files, or synthesized |
| 3 | **HyperFrames + fal.ai** | local | [fal.ai](https://fal.ai) | ElevenLabs alignment or Whisper | your own files, or synthesized |
| 4 | **HyperFrames + Higgsfield API** | local | [Higgsfield](https://higgsfield.ai) API | ElevenLabs alignment or Whisper | your own files, or synthesized |

### Route 1: Higgsfield Katana (cloud)

Claude renders the video in a Higgsfield cloud sandbox, so there is nothing to install. Whisper for the word timestamps and a library of royalty-free sounds are included. Only the images cost Higgsfield credits.

**You need** a Higgsfield plan with MCP access and the Higgsfield connector in your agent:

- **Claude Code CLI:**
  ```bash
  claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp
  ```
  Then run `/mcp` in Claude Code and sign in with your Higgsfield account once.
- **Claude desktop app / claude.ai:** Settings → Connectors → *Add custom connector*, name it `Higgsfield`, enter `https://mcp.higgsfield.ai/mcp`, click *Connect* and sign in.

### Routes 2 to 4: HyperFrames (local)

[HyperFrames](https://github.com/heygen-com/hyperframes) is an open-source framework by HeyGen that renders HTML pages with JavaScript animation to video ([docs](https://hyperframes.heygen.com)). The three local routes differ only in where the images come from.

**You need:**
1. **Node.js and ffmpeg** on your machine (see the HyperFrames docs for the minimum Node version).
2. **API keys as environment variables.** You set these yourself, for example in `~/.zshrc` or `~/.bashrc`. They never go into the chat:
   ```bash
   export ELEVENLABS_API_KEY="..."   # voice
   export KIE_API_KEY="..."          # route 2, or
   export FAL_KEY="..."              # route 3, or
   export HIGGSFIELD_API_KEY="..."   # route 4 (use whatever the provider requires)
   ```
   The variable names are up to you. Claude asks for the names on the first run and only stores those names, never the values.
3. **Optional: a sound library.** Without one, Claude synthesizes the sounds itself, and they sound somewhat artificial. Results are better with royalty-free sounds, for example from [Pixabay](https://pixabay.com/sound-effects/). Put them in a folder and give Claude the path.

---

## Installation

The skill consists of a single file, `SKILL.md`.

### Option A: let Claude install it (recommended)

Open Claude Code, drag `SKILL.md` into the chat and send one of these prompts with it:

**For all projects**
```
Install the skill from the attached SKILL.md globally so it is available in every project.
```

**For this project only**
```
Install the skill from the attached SKILL.md in this project.
```

### Option B: install it manually

**Claude Code, all projects:**
```bash
mkdir -p ~/.claude/skills/motion-video
cp SKILL.md ~/.claude/skills/motion-video/
```

**Claude Code, one project:**
```bash
mkdir -p .claude/skills/motion-video
cp SKILL.md .claude/skills/motion-video/
```

**Other agents:** put the `motion-video` folder wherever your agent loads skills from, for example `~/.codex/skills/` for Codex (check the agent's documentation for the current path).

---

## Usage

Type `/motion-video` followed by what kind of video you need, or simply ask for a video in plain language. The skill also triggers on requests like "make an explainer video about …".

```
/motion-video Make an explainer video about how GPS works, using the example of how my phone knows where I am right now.
```

The video can be in any language; the skill asks which one you want.

### First run

On the first run, Claude asks which route to use and tells you what is currently connected and which keys are set. After the run, it writes your choice to `preferences.md` next to `SKILL.md` and uses it from then on without asking:

```markdown
# motion-video preferences
route: 2 (HyperFrames local, images via kie.ai)
image_api_key_env: KIE_API_KEY
elevenlabs_api_key_env: ELEVENLABS_API_KEY
sound_library: ~/sounds/pixabay
```

To switch routes, just tell Claude, or edit or delete `preferences.md`.

---

## How a video is made

1. **Settle the route.** Taken from `preferences.md`, or asked on the first run.
2. **Clarify the frame.** Purpose and audience, length, format and language, brand guidelines and your own images such as product photos or a logo. Length is free because everything is built in code; five minutes works too.
3. **Choose a voice.** Claude suggests three to four ElevenLabs voices, each with a link to its free preview. You pick one.
4. **Approve the script.** You get the voiceover script, the concept, the list of AI images and a cost estimate, and you give feedback until everything fits. **Nothing that costs money runs before you approve.**
5. **Build and check.** Claude generates the voice in one take, takes the timestamp of every word from it, has the images generated as cutouts and builds the animation in code. Then it renders stills of each scene, checks them along with sync and loudness, and fixes problems.
6. **Finished MP4.** You get the video as an MP4, and Claude reports the actual costs.

---

## What's in SKILL.md

| Section | Content |
|---|---|
| `name`, `description` | When the skill applies: explainer videos, ads, product videos, teasers and similar animated clips |
| Goal | A finished MP4 that achieves the user's purpose, with the animation always showing what the voice says |
| What makes a good result | The quality criteria listed above |
| How a run unfolds | The order of steps, with script approval before anything costs money |
| First: the route | The four routes and how `preferences.md` is read and written (route and variable names only, never keys) |
| What the user decides | Purpose, audience, length, format, language, branding, own images and voice |
| Images | GPT Image 2.5 Flare with a transparent background, one style for all assets, no text or logos from the model |
| Voice | ElevenLabs v4, one continuous recording, no bracketed stage directions, where word timestamps come from |
| Route 1 / Routes 2 to 4 | Route-specific pitfalls, for example Katana's quiet audio output (about -23 LUFS), which gets measured and normalized |
| Before you deliver | Self-review of stills, sync, audio and loudness |
| Costs | Estimate up front, actual costs at the end |

---

## Costs

Only **images** (Higgsfield credits or the image provider's prices) and the **voice** (ElevenLabs, based on the script's character count) cost money. Motion graphics, rendering and sound are free. Claude gives an estimate before anything paid runs and reports the actual costs at the end.

---

## Tips

- **A new chat for every video.** A finished video can fill more than half of the context window. If you build the next video in the same chat, Claude carries parts of the old one over, even if you don't want that. Start a new chat for each video, or clear the old one with `/clear`.
- **Use a strong model with high effort.** Opus 5.5 with effort set to at least *high* works well, or *extra high* for elaborate motion graphics. Claude then takes more time over each scene.
- **Set up your brand once.** Give Claude your colors, fonts and logo with the first video and ask it to remember them. They are then added to `preferences.md` and used for later videos. Without that request, the skill only remembers the route.
- **Show the real product.** For an ad, a product link or a few photos are enough. Claude cuts out the product and places logos from the original files instead of letting the image model draw them.

---

## Security

- API keys live only in environment variables. Claude never asks you to paste a key into the chat and never prints one.
- `preferences.md` stores the route and the *names* of the environment variables, never their values. It is listed in `.gitignore` because it is user-specific.
- Nothing that costs money runs before you approve the script, the image list and the cost estimate.

---

## File structure

```
motion-video/
├── SKILL.md         Skill instructions for the agent
├── README.md        This file
├── .gitignore       Keeps preferences.md out of the repo
└── preferences.md   Created on the first run (route, variable names, optional brand settings)
```

---

## Maintainer

Developed and maintained by **milkycode GmbH**: [https://www.milkycode.com](https://www.milkycode.com)
