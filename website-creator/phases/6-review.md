# Phase 6: Review and polish

Goal: The site has been signed off by an independent reviewer, the user has set the final spacing themselves, and the design system is recorded.

## 1. One batched check run

`python tools/check_site.py http://localhost:8000` (script in the skill folder). In one run it does:
- screenshots on desktop (1440 pixels) and phone (390 pixels), each of the first screen and the full page,
- console errors and failed files,
- a check for horizontal scrolling,
- a list of all images without alt text and of all headings in order.

Look at all screenshots, collect all errors, **fix them in one pass**, then a second run as a check. Don't take new screenshots after every small fix.

## 2. Automatic check

Run `impeccable detect` once. Fix real errors. Hits that are a deliberate decision of the direction (for example a specific font) get a reason and are allowed for exactly that file, not switched off globally.

## 3. Independent sign-off

In Claude Code, start the `impeccable-finish-reviewer` agent. It checks against the direction contract without knowing the conversation and gives a verdict: ship, fix, rebuild or recapture. On "fix", implement all points in one pass, take new screenshots and give them to the same reviewer for sign-off.

In other agents, for example Codex, start a fresh subagent, or, if the agent has no subagents, a new session without history. It only gets `PRODUCT.md`, the direction contract and the screenshots, with the task of delivering an ordered list of the material flaws.

Why this matters: whoever built the site no longer sees their own habits. A fresh reviewer finds, for example, that the services ended up as three identical columns after all, that the accent color is in every heading, or that the proof only comes below the first screen.

## 4. Sign-off by the user

Only now show the site: local address plus desktop and phone screenshots. Collect change requests and implement them in a batch. For copy changes, update `copy.md` too.

## 5. Fine-tuning with the tweak panel

Describing spacing and positions in chat ("move the wave down a bit") takes many rounds. Better: the user moves them themselves.

1. The adjustable values have been CSS variables since phase 5.
2. Copy the panel from [../templates/tweak/](../templates/tweak/) into the project folder `tweak/`. At the top of `tweak.js`, adapt the area (`SCOPE`) and the list of sliders to the site.
3. Include it in `main.js` so it only loads with `?tweak` in the address:
   ```js
   if (/[?&]tweak\b/.test(location.search)) {
     var t = document.createElement("script"); t.src = "tweak/tweak.js"; document.head.appendChild(t);
   }
   ```
4. Start: `python tweak/server.py`, then open `http://localhost:8765/?tweak` and give the user the address.
5. "Save" writes the values to `assets/css/tweaks.css`. Afterwards, move the values into `site.css` permanently and empty `tweaks.css`.
6. The `tweak/` folder is never uploaded.

## 6. Record the design system

After sign-off:
- Record the origin of every shipped image file (`impeccable embed-prompt`), move unused files to the archive, then start the `impeccable-documenter` agent. It writes `DESIGN.md` from the finished site, not from intentions.

`DESIGN.md` is later the basis for subpages, presentations and proposals in the same style.

## Done when

- [ ] Check run without errors (console, horizontal scrolling, images).
- [ ] Independent sign-off with the verdict "ship".
- [ ] The user has signed off on the site.
- [ ] Panel values moved in permanently.
- [ ] `DESIGN.md` exists.

Next: [Phase 7: Launch](7-launch.md).
