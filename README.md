# Xiyu Ke — Academic website

A personal robotics research website, built with Jekyll and hosted on GitHub Pages. The short homepage contains an introduction with a portrait, three large project demos, a compact publication section, and personal interests. It pairs Comic Sans MS with a warm cream background, muted green accents, and a light/dark theme.

## Preview locally

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open `http://127.0.0.1:4000`. Restart the server after changing `_config.yml`. If upgrading an older checkout gives a Liquid `tainted?` error on a recent Ruby version, run `bundle install` with this updated Gemfile. The Gemfile uses Jekyll 3.10 and Liquid 4.0.4, matching the GitHub Pages versions, with only the plugins this site uses. This avoids unused CommonMark extensions that do not support Ruby 4. CSV, BigDecimal, Logger, and Base64 are explicit dependencies for newer Ruby versions.

To check the production output:

```sh
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

## Edit the content

| Content | Source |
| --- | --- |
| Homepage introduction and section order | `_pages/about.md` |
| Portrait path and alt text | `_data/profile.yml` |
| Shared project descriptions, contributions, demo paths | `_data/projects.yml` |
| Publication titles, author order, status | `_data/publications.yml` |
| Degrees and dates | `_data/education.yml` |
| Technical skills | `_data/skills.yml` |
| Email and site URL | `_config.yml` |
| Navigation | `_data/navigation.yml` |
| Downloadable CV | `CV/Academic_CV.pdf` |
| Colors, fonts, responsive layouts | `assets/css/notebook.css` |

The homepage uses each project's short `home_summary`; the research index, project pages, and CV retain the full project data. Each project page lives in `_portfolio/` and selects its data with `project_id`. Manuscript titles deliberately differ from project display titles where the CV uses different wording. Keep submitted manuscripts marked **Submitted** until their status actually changes. Paper/code links should only be added when real public URLs are available. The homepage shows accepted papers and a collapsed “Under review” list for submitted manuscripts. Both groups include the complete author lists in their original order, with Xiyu Ke in bold. Full venue details remain on the publications page and in the CV. There is no separate education section or GitHub link on the homepage.

The original sample pages and collections remain in the source tree for reference but are excluded in `_config.yml`, along with sample attachments, scripts, and template demo content. They do not appear in the generated site or feed.

## Add your portrait

Place your photo at `images/xiyu-ke.jpg`, or change `photo` in `_data/profile.yml` to an existing image path. Rebuild Jekyll after adding the file. The introduction reserves a portrait-shaped space and shows a neutral placeholder until the file exists. Use a photo with some room around your face: the desktop frame crops to a 9:11 aspect ratio. Adjust `.portrait img` in `assets/css/notebook.css` if the crop needs a different position.

## Add the three demos

Place browser-compatible MP4 videos at:

- `assets/videos/clear.mp4`
- `assets/videos/organizeit.mp4`
- `assets/videos/micromvp.mp4`

Rebuild or restart Jekyll after adding new video files. Their presence is detected at build time: an existing file displays a native video player; an absent file displays a neutral placeholder labeled “Demo coming soon” on the homepage. There is no fake play button. The player has controls, inline playback, metadata-only preload, and no autoplay. Homepage media descriptions are available to assistive technology without adding another visible paragraph. Detailed project pages also show a video download link.

Use H.264 MP4 videos with no audio track. Keep clips reasonably short and compressed. A possible conversion command is:

```sh
ffmpeg -i input.mov -c:v libx264 -crf 24 -preset medium -pix_fmt yuv420p -an -movflags +faststart assets/videos/clear.mp4
```

For an optional poster, place a JPG/PNG in `images/` and set the project's `poster` field to its root-relative path, such as `/images/clear-poster.jpg`. Only existing poster files are used. Update `demo_description` to describe the supplied clip accurately. If a demo contains essential speech, provide captions when preparing the video.

For an existing H.264/AAC MP4 that stalls before playback, move its playback index to the beginning without re-encoding: `ffmpeg -i input.mp4 -map 0 -c copy -movflags +faststart output.mp4`. Use a separate output file and preserve the original. The local development plugin `_plugins/local_video_ranges.rb` also corrects WEBrick's `If-Range` handling for MP4 seeking; restart `jekyll serve` after adding or changing this plugin. It is not needed on GitHub Pages.

## Design and publishing

The site uses a narrow layout, a warm cream background, deep gray-green text, and muted green accents. The homepage uses Comic Sans MS for the name, headings, biography, project descriptions, and hobby labels. Small metadata and contact links use Inter. When Comic Sans MS is not installed on the visitor's device, the locally served Comic Neue font provides a similar handwriting style. Microsoft font files are not bundled. Inter and Comic Neue are served locally, with their licenses in `assets/fonts/notebook/`; no runtime font requests go to external services. Each demo spans the full content width, with a short heading above it and a brief explanation below. Posters are real frames extracted from the supplied videos (CLEAR at 4 seconds, OrganizeIt at 3 seconds, microMVP at 8 seconds). All three videos have no audio tracks. The portrait has a light frame. Dark mode uses a matching charcoal-green palette. All three demos have been supplied; the personal photo is still a placeholder.

Visitors can switch themes; the preference is saved when browser storage is available. The site follows the system theme by default and honors reduced-motion preferences. Main content and navigation work without JavaScript.

Existing public URLs `/`, `/portfolio/`, `/publications/`, and `/cv/` are preserved. The new project pages are `/research/clear/`, `/research/organizeit/`, and `/research/micromvp/`. The CV is served unchanged at `/CV/Academic_CV.pdf`.

This update does not deploy automatically from the local workspace. Publishing uses the repository's configured GitHub Pages workflow after changes are committed and pushed. The local redesign introduces no server or external application service.

Original theme: Academic Pages / Minimal Mistakes (MIT; see `LICENSE`).
