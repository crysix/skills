# Phase 5: Build

Goal: The complete site runs locally, with all copy from `copy.md`, the chosen direction and structured data.

## Technology

Recommendation for service and personal sites: **static HTML, CSS and a little JavaScript, without a build step.** Reasons: loads fast, runs on any web space, no updates, no security holes from plugins, easy to change.

Folder structure:
```
index.html
impressum.html             legal pages; which ones and their file names come from
datenschutz.html           the country file (Germany: legal notice, privacy policy)
assets/css/site.css
assets/css/tweaks.css      empty, for the tweak panel in phase 6
assets/js/main.js
assets/js/vendor/          GSAP, self-hosted (see "Animation with GSAP")
assets/fonts/              fonts, self-hosted
assets/img/                logo, favicon, photos, preview image
```

Principles:
- **Self-host fonts** (woff2, for example from the `@fontsource-variable` packages on npm). No Google Fonts link: it passes visitors' IP addresses to Google, which in the EU is a data protection problem (country file, section "Privacy law and consent"), and it costs load time.
- **No third-party scripts** without a reason. No cookie banner needed if nothing tracks.
- **Colors, spacing and font sizes as CSS variables** on `:root`. Values the user will later want to move themselves (spacing in the opening, sizes, positions) get variables of their own. The tweak panel in phase 6 needs that.
- **Images** as WebP with a JPG fallback, with `width` and `height`; photos below the first screen with `loading="lazy"`.
- **Animate with GSAP** (see "Animation with GSAP" below), deliberately, and switchable off with `prefers-reduced-motion`.
- **Think mobile first.** Most visitors come via their phone. 16 pixels of side margin, no horizontal scrolling.

## Order

1. Build with impeccable. Before every change, it loads its quality rules (`craft-floor.md` in the plugin) itself.
2. Scaffold and variables (colors, fonts, spacing).
3. First screen, until it's right. It decides the impression.
4. Remaining sections in the order of `copy.md`.
5. Form with in-browser validation, error messages, confirmation. Template: [../templates/form.js](../templates/form.js). The target (webhook or form service) is set in phase 7; until then, the form opens the email program.
6. The legal pages the country file requires, in the site's style (content follows in phase 7).
7. **Structured data** in the page head as JSON-LD: `Person` and/or `Organization` or `ProfessionalService`, plus `FAQPage` if there are questions. Template: [../templates/structured-data.json](../templates/structured-data.json). Only facts from `PRODUCT.md` and `copy.md`.
8. Favicon set: `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` (180 pixels), `favicon-512.png`.

View locally: `python3 -m http.server 8000` in the project folder, then `http://localhost:8000`.

## Build with depth from the start

First drafts almost always turn out too white, too flat and too uniform: every section on the same light surface, processes as three identical boxes, lists as plain text, some sections look empty. The user then has to push a whole round of "more depth, more accents, more life". So the first draft already follows these rules, always within the chosen direction:

- **Separate sections by color.** Not everything on white. Several sections get a surface of their own from the palette (dark, brand color, tinted ground), so scrolling creates a rhythm of light and colored sections.
- **Depth instead of flat boxes.** Layers that overlap or reach over a section edge, surfaces at different heights, large numbers or shapes in the background, cropped images.
- **Set accents.** One element per section that stands out: a key figure, a key sentence, the most important step, the most important benefit. Aim the accent color at it, not everywhere.
- **Processes as graphics.** A three-step process is not a grid of three identical cards but a route, a path or a timeline with a visible connection between the steps and large numbers, ideally with an element that fills while scrolling.
- **No empty sections.** A section with little text gets a form that carries it: a graphic or image next to it, a statement set large, a full-width layout. If it still looks empty, merge it with another one.
- **Motion with a purpose.** Headings that build up, fade-ins while scrolling, numbers that count up, a process that builds itself, hover states on everything clickable. Calm and fast.

This doesn't replace the direction from phase 4; it carries it through consistently: everything in its colors, materials and forms, and impeccable's rules still apply.

Before moving on to phase 6, look at every section once in a screenshot, on desktop and phone: does it look empty, flat or dry? Then fix it now, not when the user says so.

## Animation with GSAP

All animation runs on [GSAP](https://gsap.com), including the plugins ScrollTrigger and SplitText (free, also for commercial sites, under the GSAP Standard License). CSS stays for simple hover and focus states.

**Self-host it.** No CDN link: like Google Fonts, it would pass visitors' IP addresses to a third party. Download the three files once into the project (version 3.15.0 as of October 2026; check the current one with `npm view gsap version`):
```
curl --create-dirs -o assets/js/vendor/gsap.min.js https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
curl --create-dirs -o assets/js/vendor/ScrollTrigger.min.js https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js
curl --create-dirs -o assets/js/vendor/SplitText.min.js https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js
```
On Windows, write `curl.exe` instead of `curl` (in Windows PowerShell, `curl` is an alias for a different command). Include them with `defer` before `main.js`, register the plugins once with `gsap.registerPlugin(ScrollTrigger, SplitText)` and add the files to `deploy/build.py`. Other GSAP plugins (for example DrawSVG for lines, MorphSVG for the logo) only when the direction needs them.

**Headings.** Split them with SplitText into lines or words and let them build up, for example line by line from below with `mask: "lines"`. The H1 on load, the other headings when they scroll into view.
- Use `autoSplit: true` and create the animation in `onSplit` (return it from there). SplitText then splits again after the self-hosted fonts have loaded and when the width changes; otherwise the line breaks are wrong.
- Screen readers keep reading the whole heading: SplitText's default `aria: "auto"` puts the full text into an `aria-label`. Don't switch it off.
- One or two text effects for the whole site, used consistently and matching the direction. Not a different trick for every heading.

**While scrolling.** ScrollTrigger for fade-ins, numbers that count up and a process line that fills while scrolling (`scrub`). Pin sections only where the story needs it. Fade-ins play once (`once: true`), so they don't run backwards when scrolling up.

**Rules that keep it fast and accessible:**
- Wrap all animations in `gsap.matchMedia()` with `(prefers-reduced-motion: no-preference)`. With reduced motion, the content simply appears.
- The content stays visible if JavaScript fails: set start states with GSAP (`gsap.from`, `autoAlpha`), never hide content in CSS.
- Animate only `transform` and `opacity` (GSAP's `x`, `y`, `scale`, `rotation`, `autoAlpha`), never width, height, margins or `top`. Lighthouse has to stay above 90 in phase 7.
- Every animation ends in its final state, so the full-page screenshots in phase 6 show the finished page.
- impeccable's motion rules still apply: calm, short, with a purpose.

## What matters while building

- Small labels above headings ("OUR SERVICES") are banned. They are one of the strongest AI signals.
- Contrast is measured, not estimated. Light accent colors on white are often too weak for text. Then text gets a darker tone of the same color.
- A button meant to sit over an edge gets cut off by `overflow: hidden`. Better work with `clip-path` or without an overflow lock.
- Where two surfaces meet, a thin line appears on some screens. An overlap of two pixels (`margin-bottom: -2px`) fixes it.

## Done when

- [ ] All sections from `copy.md` are built, no placeholders.
- [ ] The form validates input and shows a confirmation.
- [ ] Structured data in the page head.
- [ ] Several sections set apart by color, processes as graphics, no section looks empty or dry.
- [ ] Animations run on self-hosted GSAP, headings included, respect reduced motion, and the content is visible without JavaScript.
- [ ] The site runs locally on desktop and phone width.

No separate sign-off by the user here. It comes after the review in phase 6, so they don't have to judge a half-finished site.

Next: [Phase 6: Review and polish](6-review.md).
