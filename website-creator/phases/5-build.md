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
assets/fonts/              fonts, self-hosted
assets/img/                logo, favicon, photos, preview image
```

Principles:
- **Self-host fonts** (woff2, for example from the `@fontsource-variable` packages on npm). No Google Fonts link: it passes visitors' IP addresses to Google, which in the EU is a data protection problem (country file, section "Privacy law and consent"), and it costs load time.
- **No third-party scripts** without a reason. No cookie banner needed if nothing tracks.
- **Colors, spacing and font sizes as CSS variables** on `:root`. Values the user will later want to move themselves (spacing in the opening, sizes, positions) get variables of their own. The tweak panel in phase 6 needs that.
- **Images** as WebP with a JPG fallback, with `width` and `height`; photos below the first screen with `loading="lazy"`.
- **Use motion deliberately** (see below) and make it switchable off with `prefers-reduced-motion`.
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
- **Motion with a purpose.** Fade-ins while scrolling, numbers that count up, a process that builds itself, hover states on everything clickable. Calm and fast.

This doesn't replace the direction from phase 4; it carries it through consistently: everything in its colors, materials and forms, and impeccable's rules still apply.

Before moving on to phase 6, look at every section once in a screenshot, on desktop and phone: does it look empty, flat or dry? Then fix it now, not when the user says so.

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
- [ ] The site runs locally on desktop and phone width.

No separate sign-off by the user here. It comes after the review in phase 6, so they don't have to judge a half-finished site.

Next: [Phase 6: Review and polish](6-review.md).
