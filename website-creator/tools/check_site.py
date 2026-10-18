"""Batched check run for a site, local or live.

Usage:  python3 check_site.py http://localhost:8000 [--chrome] [--out site-check] [--review .impeccable/review]

One run does:
- screenshots on desktop (1440) and mobile (390), each of the first screen and the full page
- console errors and failed files
- a check for horizontal scrolling
- images without alt text, headings in order, page title and description

All results land in the --out folder (default: site-check/). Look at everything first,
then fix all errors in one pass, then a second run.

The full-page screenshots are also saved as desktop.png and mobile.png in the --review
folder (default: .impeccable/review/), where impeccable's finish reviewer looks for them.
"""
import os
import sys

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, sync_playwright

DEVICES = [
    ("desktop", {"width": 1440, "height": 900}, False),
    ("mobile", {"width": 390, "height": 844}, True),
]

INFO = r"""
() => ({
  title: document.title,
  description: (document.querySelector('meta[name="description"]') || {}).content || "",
  horizontal: document.documentElement.scrollWidth > window.innerWidth + 1,
  width: document.documentElement.scrollWidth,
  noAlt: [...document.images].filter(i => !i.hasAttribute("alt")).map(i => i.currentSrc || i.src),
  headings: [...document.querySelectorAll("h1, h2, h3")].map(h => h.tagName + "  " + h.textContent.trim().replace(/\s+/g, " ").slice(0, 90)),
  jsonld: document.querySelectorAll('script[type="application/ld+json"]').length
})
"""


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def open_page(page, url):
    """Load the page and wait for the network to go quiet, but not forever.

    Chat widgets, tracking and live connections keep some sites busy, so they never
    reach "networkidle". After a short wait, the loaded page is checked anyway."""
    page.goto(url, wait_until="load", timeout=60000)
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except PlaywrightTimeoutError:
        print("Note: the network did not go quiet within 10 s, continuing with the loaded page.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or sys.argv[1].startswith("--"):
        raise SystemExit(__doc__)
    url = sys.argv[1]
    out = arg("--out", "site-check")
    review = arg("--review", os.path.join(".impeccable", "review"))
    os.makedirs(out, exist_ok=True)
    os.makedirs(review, exist_ok=True)
    problems = []

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome") if "--chrome" in sys.argv else p.chromium.launch()
        for name, viewport, mobile in DEVICES:
            ctx = browser.new_context(viewport=viewport, is_mobile=mobile, has_touch=mobile,
                                      device_scale_factor=2 if mobile else 1)
            page = ctx.new_page()
            console, failed = [], []
            page.on("console", lambda m: console.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: console.append(str(e)))
            page.on("requestfailed", lambda r: failed.append(r.url))
            page.on("response", lambda r: failed.append(f"{r.status} {r.url}") if r.status >= 400 else None)

            open_page(page, url)
            page.wait_for_timeout(600)
            page.screenshot(path=f"{out}/{name}-top.png")
            height = page.evaluate("document.documentElement.scrollHeight")
            for y in range(0, height, 500):
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(100)
            page.wait_for_timeout(800)
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(300)
            page.screenshot(path=f"{out}/{name}-full.png", full_page=True)
            # At CSS pixel size, so the reviewer gets exactly 1440 and 390 wide captures
            page.screenshot(path=os.path.join(review, f"{name}.png"), full_page=True, scale="css")
            info = page.evaluate(INFO)
            ctx.close()

            print(f"\n== {name} ({viewport['width']} px) ==")
            if name == "desktop":
                print(f"Title ({len(info['title'])} characters): {info['title']}")
                print(f"Description ({len(info['description'])} characters): {info['description']}")
                print(f"Structured data: {info['jsonld']} block(s)")
                print("Headings:")
                for h in info["headings"]:
                    print("  " + h)
                if not info["description"]:
                    problems.append("Meta description missing")
                if sum(h.startswith("H1") for h in info["headings"]) != 1:
                    problems.append("Not exactly one H1")
            if info["horizontal"]:
                problems.append(f"{name}: horizontal scrolling (page is {info['width']} px wide)")
            for src in info["noAlt"]:
                problems.append(f"{name}: image without alt: {src}")
            for c in console:
                problems.append(f"{name}: console: {c}")
            for f in sorted(set(failed)):
                problems.append(f"{name}: file failed: {f}")
        browser.close()

    print(f"\nScreenshots in {out}/, review captures in {review}/ (desktop.png, mobile.png)")
    unique = list(dict.fromkeys(problems))
    if unique:
        print(f"\n{len(unique)} problem(s):")
        for pr in unique:
            print("  - " + pr)
    else:
        print("\nNo automatic problems found. Look at the screenshots anyway.")


if __name__ == "__main__":
    main()
