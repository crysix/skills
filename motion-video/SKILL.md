---
name: motion-video
description: Produce short videos with rich JavaScript motion graphics, integrated AI-generated cutout images, an ElevenLabs voiceover and sound design, delivered as a finished MP4. Use this whenever the user wants an explainer video, ad or promo spot, product video, teaser, social clip or any similar animated video, even if they only say "make a video about X".
---

# Motion Video

## Goal
The result is a finished MP4 that does exactly what the user wants it for: explain something clearly, sell a product, or draw attention to something. At every moment, the animation shows what the voice is saying.

## What makes a good result
- It is motion graphics on every level. Typography, interface elements, diagrams and transitions are animated, and the background keeps moving too. A video made of still images with text on top is not enough.
- AI images are building blocks of the graphics: cutout objects and characters in one consistent style that get animated and combined. They are never a slideshow of full-frame pictures.
- Every scene has its own visual idea. The same illustration does not keep coming back.
- Animations land exactly on the spoken word. That only works with word timestamps taken from the finished recording.
- The script is written to be spoken: complete, natural sentences, no staccato.
- An explainer opens with the question it answers, so viewers know right away what it is about.
- An ad hooks viewers in the first seconds, shows the benefit instead of a feature list, and ends with a clear call to action.
- Text and logos are never drawn by the image model. Text is set in code, and logos are the original files.
- Sound design sits on the accents. Loudness is platform-ready, around -14 to -16 LUFS integrated.

## How a run unfolds
1. Settle the route (see below).
2. Clarify what only the user can decide, including the voice.
3. Present the approval package: the voiceover script, the concept (look and the idea of each scene), the list of AI images and a cost estimate. Iterate on feedback until the user approves. Nothing that costs money runs before that.
4. Build: generate the voice as one recording, take word timestamps from it, generate the images as cutouts, and build the animation in code against those timestamps.
5. Review your own output (see "Before you deliver") and fix what is wrong.
6. Deliver the MP4, report the actual costs and update `preferences.md`. Suggest starting a fresh conversation (or `/clear`) for the next video, so nothing from this one carries over.

## First: the route
The route determines what renders the video and where images, word timestamps and sounds come from. There are four:
1. **Higgsfield Katana**: renders in Higgsfield's cloud sandbox. Images, Whisper and the sound library come from there. Requires a Higgsfield plan with MCP access.
2. **HyperFrames local**, images via kie.ai
3. **HyperFrames local**, images via fal.ai
4. **HyperFrames local**, images via the Higgsfield API

Before anything else, read `preferences.md` in the same folder as this skill.
- If it names a route, use it without asking and say in one sentence which one you are using. Switch only if the user asks for it, or if the route does not work right now, for example because the connector is missing or the API key is not set. Then sort it out with the user.
- If the file does not exist or names no route, the route is your very first question, before anything else. Say what is currently connected and which keys are set. If Higgsfield is not connected, Katana is off the table.

Check whether a key is set without ever printing its value, for example `[ -n "$KIE_API_KEY" ] && echo set || echo missing`.

At the end of a run, write the route that was actually used to `preferences.md`. Store only the route, the names of the environment variables that hold the API keys and, if the user provided one, the path to a local sound library. Never store a key itself. Do not store format, length, voice or anything else; ask for those again on every video. The exception is when the user asks you to remember specific preferences, such as brand colors, fonts or the logo path. Then add those as well.

```markdown
# motion-video preferences
route: 2 (HyperFrames local, images via kie.ai)
image_api_key_env: KIE_API_KEY
elevenlabs_api_key_env: ELEVENLABS_API_KEY
sound_library: ~/sounds/pixabay
```

## What the user decides
Then clarify what you cannot derive from the request, in one compact message rather than question by question:
- purpose and target audience
- length, format (for example 16:9, 9:16 or 1:1) and language. Length is not limited by the tooling: everything is code, so five minutes works too.
- brand guidelines (colors, fonts, logo)
- the user's own images, such as product photos or a logo. An ad shows the real product, never an invented one. A product link is enough to take photos and logo from.
- the voice: suggest three to four fitting voices, each with a direct link to its free preview (the `preview_url` from the ElevenLabs voice list), and let the user choose. Generate paid samples with the real script only if the user wants that, for example to compare two favorites directly.

Everything else is your call: look, scenes, image motifs, animations, pacing and sound. Base those decisions on purpose and audience.

## Images
On every route, images come from GPT Image 2.5 in the Flare variant with `background: transparent`. This applies to new motifs and to images the user provides alike: the original goes in as a reference, and the same motif comes out as a cutout. Recurring characters stay consistent through a reference image.
- Settle on one style description for the whole video and reuse it in every prompt, so all assets match.
- Generate only what the concept needs. The image list in the approval package is the budget.
- Keep text, labels and logos out of the prompts. If a product cutout comes back with a distorted logo or label, place the original logo over it in code.

## Voice
The voice comes from ElevenLabs with the v4 engine (`eleven_v4`), through the ElevenLabs connector if one is connected, otherwise through the API with the key from an environment variable. One continuous recording of the whole script sounds more natural than separate sentences. Send plain text only, without stage directions in square brackets, otherwise they may be spoken aloud.

If a long script exceeds the per-request limit, split it at paragraph boundaries, keep continuity between the parts (request stitching, where the model supports it) and listen for audible seams.

Word timestamps come from the finished recording: on Katana from Whisper in the sandbox, locally from the ElevenLabs timestamp alignment or by transcribing the recording (Whisper or ElevenLabs Speech to Text).

## Route 1: Higgsfield Katana
Katana renders in a cloud sandbox. Whisper for word timestamps and a royalty-free sound library are included, and nothing except the images costs credits.

Pitfalls:
- Base64 via `sandbox_exec` is rejected, and a single command may be at most 16,000 characters long. Files get into the sandbox like this: `media_upload`, upload locally via `curl` PUT, `media_confirm`, then fetch the file inside the sandbox by its URL.
- The compositor outputs audio too quietly (around -23 LUFS). Measure loudness after rendering and normalize.
- The sandbox occasionally hangs (rate limit or "server not responding"). Wait briefly, then retry.

## Routes 2 to 4: HyperFrames local
HyperFrames is an open-source framework by HeyGen that renders HTML pages with JavaScript animation to video. It needs Node and ffmpeg on the machine. For project setup and the render command, follow the HyperFrames documentation (or its agent skills, if installed) instead of guessing the CLI.

The user sets the image provider's API key as an environment variable themselves. Never ask them to paste a key into the chat, and never print one.

There is no built-in sound library locally. If the user has royalty-free sounds, for example from Pixabay, use those. Otherwise synthesize the sounds yourself and tell the user up front that they will sound somewhat artificial.

## Before you deliver
Check your own output before handing it over, and fix whatever fails:
- Render stills at the key moment of each scene and look at them: nothing cut off or overlapping, all text legible, cutouts without white or black boxes or halos, one consistent style.
- Check sync: every animation beat sits on its word.
- Check the audio: nothing clipped at the end, no spoken stage directions.
- Measure integrated loudness (for example with ffmpeg `loudnorm`) and normalize to -14 to -16 LUFS, with true peak at or below -1 dBTP.

## Costs
Give an estimate before starting and the actual costs at the end. Get image prices beforehand from the provider's cost check or price list. Voice cost follows from the script's character count. Only the images and the voice cost money; motion graphics, rendering and sound are free.
