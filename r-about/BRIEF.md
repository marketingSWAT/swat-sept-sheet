# Brief: redesign the whole About page of the SWAT website

The client is Crow, who runs marketing for Southwest Adventure Tours (SWAT), a US small-group
tour operator based in Utah. Customers skew older (60+ is common); a lot of traffic is on
phones. The site is a Next.js rebuild that launches this week.

Crow's ask (29 Sep 2026), with a screenshot of the About page:

> "I think we need to rework the about page, I dont really like how this photo is so large and
> text below, can you use codex to run a full redesign of this entire page and give me a couple
> designs of different ways of showing it"

His screenshot: `/mnt/c/Users/james/clawd-inbound/1790717036965-2738c032.png` (the Imperial
Point photo, 1,616 x 423, then a narrow 748px column of text under it).

The owner, Jason Murray, emailed a review rubric the same day: **Clarity > Connection >
Conversion.** The parts that bite on this page: "use the words that are yours, and not Claude's
or the industry's", "a clear origin story", "don't look bigger than you are", "the site should
feel like the trip", and "the next step always visible".

Your designs go on a **decision sheet**: Crow sees the page as it is today (letter **A**, a real
screenshot) beside your redesigns, and answers out loud: "seventy-four goes to C".
**You draw three: B, C and D.** Three genuinely different page structures, not three skins.

## The page today (production, 1920 x 1080, 29 Sep 2026)

Full-page screenshot: `r-about/harvest/about-1920-full.png` (lazy images loaded). One screen at
a time: `r-about/harvest/about-1920-screen1.png` ... `screen7.png`. Phone: `about-390.png`.
Every block with its position: `r-about/harvest/about-1920.json` (`blocks`, `mainText`).

Top to bottom, 7,827px tall (about 7 laptop screens, footer included):

1. **Hero** 640px: Canyonlands sign group photo, "About Us", one line: "Southwest Adventure
   Tours provides local, experienced guides who work hard to provide travelers with the best
   experience in the Southwest."
2. **Imperial Point photo** 1,616 x 423, caption, then 748px-wide text: two intro paragraphs
   (the second says "watch the following video" and **there is no video on the page**),
   Mission Statement, two lines telling you to click "Our Team below" and "the Careers option
   below" (**neither button exists**), Affiliations: 4 logos (ATTA, American Bus Association,
   IATAN, National Tour Association) + "Membership in each of these is verifiable independently
   of anything said on this site."
3. **"Explore, Experience, Enrich"** band: "Groups of seven to thirteen, and a guide who has been
   there before. Every photograph below is one of ours, on one of these trips." + 6 group photos
   (531 x 354, 3 across).
4. **Team photo** 1,616 x 464 (staff at a Bristlecone Pine sign), then "Our Team": one paragraph
   that runs straight into Jason's bio ("...Meet the Team Jason Murray - Owner/CEO As a native of
   Utah..."), a broken join from the old site.
5. **"THE PEOPLE WHO GUIDE THE TRIPS"**: 10 portraits, 304 x 405, 5 across, name only. Each links
   to a profile page `/about/<slug>/`. Note: not all ten are guides: Jason is the owner, Julie
   Burton-Ray is Operations Manager, Shawn Horman designs the tours.
6. **Careers + a staff handbook**: Careers paragraph, a bare URL for the job board, the Mission
   Statement printed a second time, the motto, then "Three Steps Of Service", 12 "Service
   Values: I Am Proud To Be Southwest Adventure Tours" ("I understand my role in achieving the Key
   Success Factors..."), and "The Employee Promise" calling staff "our Ladies and Gentlemen".
   This is internal staff material (it reads like a hotel's employee credo), 1,600px of it.
   A lone photo captioned "Wynn Hall" sits beside it with no explanation.

What's wrong, in Crow's words and ours: a huge photo, then a narrow column of text under it,
repeated twice; half the page is an employee handbook; no origin story; the ten people are faces
with names and nothing else; nothing tells a visitor what to do next.

## Content you may use (real, all of it)

- **All text on the page today** (`mainText` in the JSON). Prefer SWAT's own sentences.
- **The ten people**, full bios in `r-about/harvest/guides.json`. Real, specific facts you can
  lift as one-line hooks, e.g. Ann Evans: 25 years with Utah's Department of Natural Resources,
  mostly as a State Parks ranger/naturalist, EMT; Phil Douglass: 32 years with the Utah Division
  of Wildlife Resources, called "Utah's Wildlife Ambassador"; Dennis Bailey: grew up with Arches
  and Canyonlands as his backyard in Moab, a land surveyor; Robin Luse: left radio in 1999 to
  guide, based in Albuquerque, with SWAT since 2014; Chris Vander Wilt: President of the Utah
  Tour Guide Association; Kirk Douglass: a peak bagger, Mount Whitney to the Grand Teton; Shawn
  Horman: 30 years designing custom tours; Julie Burton-Ray: in the tour business since 1983,
  Operations Manager; Shybree Richens: grew up in St. George near Zion, loves photography;
  Jason Murray: Owner/CEO, Utah native, favourite trip Havasupai Falls. **Check every fact
  against guides.json before you print it.**
- **Photos** (all real SWAT photos, already on the site; use these exact URLs, swap `w640` /
  `w1200` / `w2048` for size):
  - every `IMG` in `about-1920.json` `blocks` (hero, Imperial Point, 6 group photos, team photo,
    10 portraits, Wynn Hall, 4 affiliation logos).
- **A company film exists and is unused**: YouTube `y6-BldlQHlI`, titled "Southwest Adventure
  Tours", about 8 minutes, 2023. Thumbnail `https://i.ytimg.com/vi/y6-BldlQHlI/maxresdefault.jpg`.
  It can fill the "watch the following video" promise. Draw it as a thumbnail with a play button.
- **Other facts printed elsewhere on the site** you may reuse: "Small groups of 7-13, departing
  Las Vegas, Phoenix and Salt Lake City"; "4.8 out of 5 from 255 Google reviews" (company-wide,
  must be attributed to Google, never per trip); phone 800-970-5864; the motto
  "Explore, Experience, Enrich".

## Hard rules

1. **Invent nothing.** No founding year, no guest counts, no "20 years in business", no awards,
   no quotes nobody said. If a design wants a fact that isn't above, leave the slot out.
2. **Words:** body copy should be SWAT's own sentences (trimmed is fine, fix the broken joins).
   New copy you write is limited to headings, labels, buttons and short one-line connectors.
   US English, **no em dashes (—)**, plain words a 70-year-old understands. Don't write
   marketing fluff ("unforgettable", "curated", "bespoke", "nestled").
3. **The staff handbook** (Three Steps, Service Values, Employee Promise) must not sit in the
   main flow of the customer page. Each design must say where it goes: e.g. into a
   "How we work" block for job seekers, a collapsed section under Careers, or off this page to a
   Careers page. The duplicate Mission Statement goes. "Wynn Hall" goes unless you can explain it
   (you can't; nobody has).
4. **Crow's complaint is the brief**: no full-width photo followed by a narrow column of text
   below it. Words and pictures should work together (side by side, overlapping, woven), and the
   page should be clearly shorter than today's ~7,000px (above the footer). Target
   **3,500 to 5,500px** at 1920.
5. **Always a next step**: "Find a trip" and the phone number should be reachable, and the page
   should end on something to do, not on a list.
6. Real SWAT palette only (tokens on `.mock` in `build/sheet.css` ~line 231): navy
   `--navy800`/`--navy900`, rust/orange `--rust600` (primary actions only), `--rust100`,
   pine `--pine700`/`--pine100`, sand/pale blue `--sand100/200/300`, ink `--ink900/700/500/300`.
   Font Inter. White page. Buttons look like buttons (older audience).
7. The ten people keep a link to their profile page (draw it as a clear "Read Ann's story"
   link or make the whole card clickable).

## Directions worth exploring (pick three, or better ones)

- **The story, told side by side**: alternating rows, a photo beside each block of words (origin,
  what a trip is like, the people, who we're accredited by). Answers Crow most directly.
- **The people are the page**: lead with the faces. "Who you'll travel with" as the first thing,
  each card with a real one-line fact; the company story compact around them.
- **Everything on the first screen**: a split hero (words + film left, photo mosaic right), a
  strip of three plain proof points (small groups of 7-13 / local guides / accredited by 4
  bodies + Google 4.8), then the people and a closing call to action. The shortest page.
- **Magazine / field journal**: a founder's letter from Jason's own bio words, pull quotes from
  guide bios, photos with real captions.

Give each a short plain name (2-5 words, e.g. "The people come first").

## Deliverables (write ONLY inside `r-about/codex/`)

- `r-about/codex/mocks/B.html`, `C.html`, `D.html`: an HTML **fragment** (no `<html>`/`<head>`),
  the **whole page at 1920 wide from the top strip to just above the footer**. Start with the
  site chrome exactly as given in `r-about/frag/chrome.html` (strip, navy header with "About"
  underlined, hot-deals ticker; its CSS lives in `build/r9.css`, classes `w9-*`). Wrap your page
  in `<div class="w9">...</div>` and use `.sh` for the 1,728px shell (content 1,616px wide,
  x=152 to 1768). Do not draw the footer.
- `r-about/codex/css/codex.css`: all your CSS. **Every selector must start with `.mock .cx-`**
  (or `.mockwrap.phone .cx-` for phone rules) so nothing leaks into the sheet. Name classes
  `cx-...`. You may reuse `.w9`, `.sh` and the `w9-` chrome classes as they are, unchanged.
- **Phone**: the sheet's Phone toggle re-lays the SAME fragment at **390px** by adding class
  `phone` to the wrapper. Write `.mockwrap.phone .cx-...` rules so each design works at 390 with
  **zero horizontal overflow** and a sensible order (story before handbook, people as a
  swipeable row or two-up grid, etc.).
- `r-about/codex/notes/B.json` (and C, D), exactly this shape:
  ```json
  {"name": "The people come first",
   "changes": ["one plain sentence per numbered change, 3 or 4 of them"],
   "rings": [[1, ".cx-some-selector"], [2, ".cx-other"]],
   "body": "Two or three plain sentences: what it does for a visitor, and its catch.",
   "handbook": "one sentence: where the staff handbook goes in this design",
   "cost": "about 1 day",
   "risk": "one plain sentence"}
  ```
  `rings` numbers match `changes`; each is a CSS selector matching ONE element in your fragment.
  **Use single quotes inside attribute selectors, never double quotes.** `cost` is build time on
  a Next.js site where the content already exists.
- `r-about/codex/notes/pick.json`: `{"pick": "C", "why": "two sentences"}`.

## Check your work before you finish

Run `node r-about/tools/preview.mjs codex/B codex/C codex/D` from
`/home/james/swat/projects/swat-sept-sheet`. It renders each fragment exactly as the sheet will,
at 1920 and 390, writes `r-about/preview/codex-B-desk.png` etc., and prints height, OVERFLOW
and BROKEN IMG. **Open the PNGs and look at them.** Fix overflow, broken images, clipped text,
anything unfinished. Make sure the three read as three different pages at a glance, and that none
of them is "big photo, narrow text under it" again. Iterate until you'd show them to a client.

Do not edit anything outside `r-about/codex/`. Do not run git. Do not deploy.
