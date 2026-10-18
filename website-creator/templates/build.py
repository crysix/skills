"""Builds the upload folder dist/ and dist.zip with exactly the files that go live.

Run in the project folder:  python3 deploy/build.py

The FILES list is maintained by hand on purpose: that way research, drafts,
the tweak panel and other working files never land on the server.
Add new files (images, subpages) here.

Cache busting: in the copied HTML files, every link to a local CSS or JS file
gets a version from the file's content (assets/css/site.css?v=3f2a9c1b04), so
browsers load the new file right after an update even though the host lets
them cache CSS and JS for a long time. The source files stay unchanged.
"""
import hashlib
import os
import re
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

FILES = [
    # Legal pages: names from the country file (Germany shown)
    "index.html", "impressum.html", "datenschutz.html",
    "robots.txt", "sitemap.xml", "llms.txt",
    "assets/css/site.css", "assets/css/tweaks.css", "assets/js/main.js",
    "assets/js/vendor/gsap.min.js", "assets/js/vendor/ScrollTrigger.min.js", "assets/js/vendor/SplitText.min.js",
    # Fonts, for example:
    # "assets/fonts/font-latin-wght-normal.woff2",
    "assets/img/logo.svg", "assets/img/favicon.svg",
    "assets/img/favicon-32.png", "assets/img/favicon-512.png", "assets/img/apple-touch-icon.png",
    "assets/img/og-image.png",
]

# Configuration files for the host, as named in the hosting file (hosting/<host>.md)
HOST_FILES = [".htaccess"]

# Folders of deploy tools inside dist/ that survive a rebuild
# (.vercel: the Vercel project link, .git: a repository that publishes dist/)
KEEP_IN_DIST = {".vercel", ".git"}

# href="..." or src="..." pointing to a .css or .js file, without a query string yet
ASSET_LINK = re.compile(r"""(?P<attr>(?:href|src)=["'])(?P<url>[^"'?#]+\.(?:css|js))(?P<end>["'])""")


def content_version(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:10]


def bust_cache(html, html_rel, versions):
    """Append ?v=<content hash> to links to local CSS and JS files in the list."""
    base = os.path.dirname(html_rel)
    count = 0

    def replace(m):
        nonlocal count
        url = m.group("url")
        if url.startswith(("http:", "https:", "//")):
            return m.group(0)
        target = url.lstrip("/") if url.startswith("/") else os.path.normpath(os.path.join(base, url)).replace(os.sep, "/")
        if target not in versions:
            return m.group(0)
        count += 1
        return f"{m.group('attr')}{url}?v={versions[target]}{m.group('end')}"

    return ASSET_LINK.sub(replace, html), count


files = FILES + HOST_FILES
missing = [rel for rel in files if not os.path.exists(os.path.join(ROOT, rel))]
if missing:
    raise SystemExit("Missing in the project:\n  " + "\n  ".join(missing))

versions = {rel: content_version(os.path.join(ROOT, rel)) for rel in files if rel.endswith((".css", ".js"))}

if os.path.exists(DIST):
    for name in os.listdir(DIST):
        if name in KEEP_IN_DIST:
            continue
        path = os.path.join(DIST, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
busted = 0
for rel in files:
    src = os.path.join(ROOT, rel)
    dst = os.path.join(DIST, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if rel.endswith(".html"):
        with open(src, encoding="utf-8") as f:
            html, count = bust_cache(f.read(), rel, versions)
        with open(dst, "w", encoding="utf-8", newline="") as f:
            f.write(html)
        busted += count
    else:
        shutil.copy2(src, dst)

zpath = os.path.join(ROOT, "dist.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for rel in files:
        z.write(os.path.join(DIST, rel), rel)

size = sum(os.path.getsize(os.path.join(DIST, r)) for r in files)
print(f"{len(files)} files, {size / 1024:.0f} KB, {busted} CSS/JS links versioned, created dist/ and dist.zip")
