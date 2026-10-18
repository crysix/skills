"""Builds the upload folder dist/ and dist.zip with exactly the files that go live.

Run in the project folder:  python deploy/build.py

The FILES list is maintained by hand on purpose: that way research, drafts,
the tweak panel and other working files never land on the server.
Add new files (images, subpages) here.
"""
import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

FILES = [
    "index.html", "impressum.html", "datenschutz.html",
    "robots.txt", "sitemap.xml", "llms.txt", ".htaccess",
    "assets/css/site.css", "assets/css/tweaks.css", "assets/js/main.js",
    # Fonts, for example:
    # "assets/fonts/font-latin-wght-normal.woff2",
    "assets/img/logo.svg", "assets/img/favicon.svg",
    "assets/img/favicon-32.png", "assets/img/favicon-512.png", "assets/img/apple-touch-icon.png",
    "assets/img/og-image.png",
]

missing = [rel for rel in FILES if not os.path.exists(os.path.join(ROOT, rel))]
if missing:
    raise SystemExit("Missing in the project:\n  " + "\n  ".join(missing))

if os.path.exists(DIST):
    shutil.rmtree(DIST)
for rel in FILES:
    src = os.path.join(ROOT, rel)
    dst = os.path.join(DIST, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

zpath = os.path.join(ROOT, "dist.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for rel in FILES:
        z.write(os.path.join(DIST, rel), rel)

size = sum(os.path.getsize(os.path.join(DIST, r)) for r in FILES)
print(f"{len(FILES)} files, {size / 1024:.0f} KB, created dist/ and dist.zip")
