#!/usr/bin/env python3
"""Check the built site's local links, assets, and key content invariants."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
import re
import sys


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.duplicates = []
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.duplicates.append(attrs["id"])
            self.ids.add(attrs["id"])
        for name in ("href", "src", "poster"):
            if attrs.get(name):
                self.links.append(attrs[name])


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
assert root.is_dir(), "Build the site first: bundle exec jekyll build --strict_front_matter"
errors = []
pages = {file: Page(file.read_text()) for file in root.rglob("*.html")}
for file, page in pages.items():
    relative = file.relative_to(root)
    url = "/" + str(relative)
    text = file.read_text()
    redirect = 'http-equiv="refresh"' in text.lower()
    if not redirect and page.h1_count != 1:
        errors.append(f"{relative}: expected one h1, found {page.h1_count}")
    if page.duplicates:
        errors.append(f"{relative}: duplicate ids {page.duplicates}")
    for link in page.links:
        parsed = urlparse(urljoin(url, link))
        if parsed.scheme or parsed.netloc:
            continue
        target = root / unquote(parsed.path).lstrip("/")
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{relative}: missing target {link}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f"{relative}: missing anchor {link}")

for css in root.rglob("*.css"):
    for ref in re.findall(r"url\(['\"]?([^)'\"]+)", css.read_text()):
        if urlparse(ref).scheme or ref.startswith("#"):
            continue
        target = root / ref.lstrip("/") if ref.startswith("/") else css.parent / ref
        if not target.is_file():
            errors.append(f"{css.relative_to(root)}: missing CSS asset {ref}")

expected = ("index.html", "portfolio/index.html", "publications/index.html", "cv/index.html",
            "research/clear/index.html", "research/organizeit/index.html", "research/micromvp/index.html")
for path in expected:
    if not (root / path).is_file():
        errors.append(f"Missing required page: {path}")

publications = (root / "publications/index.html").read_text()
if publications.count('class="publication"') != 5:
    errors.append("Publications page must contain all five CV entries")
if publications.count('status-accepted"') != 1 or publications.count('status-submitted"') != 4:
    errors.append("Expected one accepted paper and four submitted manuscripts")
homepage = (root / "index.html").read_text()
if homepage.count('class="demo-row"') != 3:
    errors.append("Homepage must feature three concise project demos")
if 'href="https://github.com/' in homepage:
    errors.append("Homepage must omit the GitHub profile link")
if homepage.count('class="home-paper"') != 1 or 'class="home-under-review"' not in homepage:
    errors.append("Homepage must distinguish the accepted paper from submitted manuscripts")
for file in list(pages) + [root / "feed.xml", root / "sitemap.xml"]:
    if file.is_file() and re.search(r"GitHub University|paper-title-number|blog-post-[1-4]|portfolio-[12]|ready-to-fork", file.read_text()):
        errors.append(f"{file.relative_to(root)} contains template demo content")
source_cv = Path("CV/Academic_CV.pdf")
if source_cv.read_bytes() != (root / "CV/Academic_CV.pdf").read_bytes():
    errors.append("Published CV differs from the original")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(pages)} HTML pages; local links, anchors, CSS assets, CV, publication statuses, and template cleanup.")
