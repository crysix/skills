"""Builds the upload folder dist/ and dist.zip with exactly the files that go live.

Run in the project folder:  python3 deploy/build.py

The FILES list is maintained by hand on purpose: that way research, drafts,
the tweak panel and other working files never land on the server.
Add new files (images, subpages) here.

Cache busting: in the copied HTML files, every link to a local CSS or JS file
gets a version from the file's content (assets/css/site.css?v=3f2a9c1b04), so
browsers load the new file right after an update even though the host lets
them cache CSS and JS for a long time. The source files stay unchanged.

Mail addresses: in the copied HTML files, the addresses in PUBLIC_MAILS are
hidden from bots that read the source. A small script restores text and mailto
links in the browser, so visitors notice nothing. Without JavaScript the address
stays readable and links lead to MAIL_FALLBACK. The source files keep the normal
address. At the end the script lists every address still in plain text in dist/.
"""
import base64
import hashlib
import os
import re
import shutil
import zipfile
from html import unescape

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

# The site's own mail addresses, team members included
PUBLIC_MAILS = ["contact@DOMAIN.TLD"]

# Where mailto links lead without JavaScript. This page has to show the address (name from the country file)
MAIL_FALLBACK = "/impressum.html"

# Hidden in browsers, it only splits the address in the source. Text browsers show it, so use the site's language.
MAIL_DECOY = " (without this note) "

# Restores what protect_mail() hid. Inline, so it travels with the page and runs before deferred scripts.
MAIL_DECODER = (
    '<script>document.querySelectorAll("[data-mail-key]").forEach(function(e){'
    'var m=atob(e.dataset.mailKey).split("").reverse().join("");'
    'if("A"===e.tagName)e.href="mailto:"+m;'
    'else if("FORM"===e.tagName)e.dataset.mailto=m;'
    "else{var p=e.parentNode;e.replaceWith(m);p.normalize();return}"
    'e.removeAttribute("data-mail-key")});</script>'
)

# href="..." or src="..." pointing to a .css or .js file, without a query string yet
ASSET_LINK = re.compile(r"""(?P<attr>(?:href|src)=["'])(?P<url>[^"'?#]+\.(?:css|js))(?P<end>["'])""")

MAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")

# Look like addresses, but aren't: file names such as logo@2x.png, and sample addresses
NOT_MAIL = (
    ".avif", ".css", ".gif", ".ico", ".jpeg", ".jpg", ".js", ".json", ".map", ".mjs", ".mp4", ".pdf", ".png",
    ".svg", ".ttf", ".webm", ".webp", ".woff", ".woff2",
    ".tld", ".example", ".invalid", ".test", "example.com", "example.org", "example.net",
)


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


def mail_key(value):
    """Reversed and Base64: no address pattern left in the source, one line to undo in the browser."""
    return base64.b64encode(value[::-1].encode()).decode()


def protect_mail(html):
    """Hide the addresses in PUBLIC_MAILS from anything that reads the source. Returns the page and the number of hits."""
    count = 0
    for mail in PUBLIC_MAILS:
        local, domain = mail.split("@")
        quoted = re.escape(mail)
        # The guards leave longer addresses alone: sales.info@domain.tld, info@domain.tld.au
        plain = re.compile(rf"(?<![\w.%+-]){quoted}(?!\.?[\w-])")
        count += len(plain.findall(html))

        def swap(text, value):
            return plain.sub(lambda _: value, text)

        # Scripts, including JSON-LD: a JSON escape, so parsers such as Google's still read the address
        html = re.sub(r"<script\b[^>]*>.*?</script>", lambda m: swap(m.group(0), f"{local}\\u0040{domain}"), html, flags=re.I | re.S)
        # Links keep their subject line. The decoder sets the real href.
        html = re.sub(
            rf"""\bhref=(["'])mailto:{quoted}(\?[^"']*)?\1""",
            lambda m: f"href={m[1]}{MAIL_FALLBACK}{m[1]} data-mail-key={m[1]}{mail_key(mail + unescape(m[2] or ''))}{m[1]}",
            html,
            flags=re.I,
        )
        # The form's fallback address (form.js reads data-mailto when the form is sent)
        html = re.sub(rf"""\bdata-mailto=(["']){quoted}\1""", lambda m: f"data-mail-key={m[1]}{mail_key(mail)}{m[1]}", html)
        # Visible text. With tags stripped it reads "contact (without this note) @domain.tld", which is no address.
        text = f'<span data-mail-key="{mail_key(mail)}">{local}<span style="display:none">{MAIL_DECOY}</span>&#64;{domain}</span>'
        html = re.sub(rf">[^<>]*{plain.pattern}[^<>]*<", lambda m: swap(m.group(0), text), html)
        # Whatever is left sits in an attribute, which can hold neither markup nor a script: an entity is all that fits
        html = swap(html, f"{local}&#64;{domain}")

    if "data-mail-key" in html:
        end = html.lower().rfind("</body>")
        if end != -1:
            html = html[:end] + MAIL_DECODER + html[end:]
    return html, count


def plain_mails(rels):
    """Addresses still readable in the uploaded text files, each with the files it is in."""
    found = {}
    for rel in rels:
        if not rel.endswith((".html", ".txt", ".xml", ".json", ".js")) or "/vendor/" in rel:
            continue
        with open(os.path.join(DIST, rel), encoding="utf-8", errors="replace") as f:
            # Sample values in form fields don't count
            source = re.sub(r"""\bplaceholder=(["']).*?\1""", "", f.read())
        for mail in MAIL_PATTERN.findall(source):
            if not mail.lower().endswith(NOT_MAIL):
                found.setdefault(mail.lower(), set()).add(rel)
    return found


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
hidden = 0
for rel in files:
    src = os.path.join(ROOT, rel)
    dst = os.path.join(DIST, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if rel.endswith(".html"):
        with open(src, encoding="utf-8") as f:
            html, count = bust_cache(f.read(), rel, versions)
        html, mails = protect_mail(html)
        with open(dst, "w", encoding="utf-8", newline="") as f:
            f.write(html)
        busted += count
        hidden += mails
    else:
        shutil.copy2(src, dst)

zpath = os.path.join(ROOT, "dist.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for rel in files:
        z.write(os.path.join(DIST, rel), rel)

size = sum(os.path.getsize(os.path.join(DIST, r)) for r in files)
print(f"{len(files)} files, {size / 1024:.0f} KB, {busted} CSS/JS links versioned, {hidden} mail addresses hidden, created dist/ and dist.zip")

left = plain_mails(files)
if left:
    print("\nMail addresses still in plain text in dist/, bots can read them:")
    for mail, rels in sorted(left.items()):
        print(f"  {mail}: {', '.join(sorted(rels))}")
    print("Add the site's own to PUBLIC_MAILS. Addresses of others, such as an authority, may stay.")
