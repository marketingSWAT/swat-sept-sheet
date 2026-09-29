# Brief: redesign how a customer picks a departure date on a SWAT tour page

You are one of two designers on this. The client is Crow, who runs marketing for Southwest
Adventure Tours (SWAT), a US small-group tour operator. Its customers skew older (60+ is
common) and most traffic is on phones. The site is a Next.js rebuild that has not launched yet.

Crow's ask, verbatim (voice note, 29 Sep 2026), about the **Departures** section of a tour page:

> "I want you and codex to mock up a couple new ideas on how we can show this on the website,
> I just really feel like we can make this easier and more clear on actually picking dates,
> because also when you get into 2027 you have to click that drop down to see all the other
> dates"

His screenshot: `/mnt/c/Users/james/clawd-inbound/1790703907079-820af937.png`.
Today's section, redrawn at the live geometry: `r8/preview/now-desk.png` (1440) and
`r8/preview/now-phone.png` (390). Its markup: `r8/frag/now.html`.

Your drawings go on a **decision sheet**: one page where Crow sees the build as it is today
(letter A) beside every proposed redesign, and answers out loud: "sixty-seven goes to F".
The other designer (Claude) has drawn **B, C, D**. **You draw three more: E, F and G.**

## The facts, measured on the live production page on 29 Sep 2026

Tour: *Mighty 5 Utah Tour From Las Vegas*, 5 days (every departure leaves on a Monday and is
back on the Friday), from $1,999.

- The page is 12,936px tall at 1440. **Departures is the tenth section, at y=8,781**, below
  the gallery. The booking panel's orange **"Choose your date"** button (top of the page, in
  the sticky right-hand panel, at y=1,535) just jumps you ~7,200px down to that section.
- The section loads 887px tall showing **only October and November 2026 (9 dates)**, then a
  pill "Show all 65 dates through December 2027". **All 52 dates in 2027 are behind that
  pill.** Opened, the section grows to **5,322px: six laptop screens of Mondays** in a flat
  list, 65 rows of 65px, 15 month headings.
- On a phone the section starts about **16 screens down** (y=13,766) and opens to 5,360px.
- **No row shows its price.** Yet 2027 prices differ by date: **$1,999** Jan-Apr and from
  Oct 18; **$2,199** from May 3 to Oct 11 (peak). 2026 dates have no per-date price published
  (show nothing, or "from $1,999"; never invent one).
- 13 dates in 2026, **7 of them sold out**. Sold-out rows today say SOLD OUT + "Join the list"
  (which dials the office, 800-970-5864; they keep a waiting list).
- The full data, one object per date: `r8/harvest/m5lv-dates.json`
  (`date`, `sold`, `price` (null for 2026), `via`: `legacy` = 2026, books on the old
  AdventureCentral site in a new page; `softrip` = 2027, opens Softrip's booking pop-up on our
  page on that exact date; `phone` = sold out).

## Hard constraints (earlier decisions and standing rules; do not break these)

1. **Clickable things must look clickable** (clear buttons, outlines, hover states). The
   audience is older. Tiny text links are not enough for the main action.
2. **Tapping a date must lead straight to booking that date** (or to a clear "Book this date"
   confirm). No extra form. The booking itself happens in Softrip's pop-up, not on our page.
3. **No seat counts** ("only 3 left"). Measured load factor is ~5%, so scarcity copy would be
   false. Sold out is the only availability state shown.
4. **Every date stays in the page HTML** (crawlers and find-on-page). Tabs/strips may hide
   dates visually, but the markup for all 65 must exist. No design that needs data fetched.
5. A date can carry a **Hot deal** (a flame badge + "$300 off" + promo code). This tour has
   none today, but the design must have an obvious place for it. You may draw one on a
   single 2027 date labelled as an example.
6. **US English. No em dashes (—) in any copy you write.** Contractions are fine. Plain words:
   a 70-year-old reading it on a phone must understand every label.
7. Real SWAT palette only (tokens are defined on `.mock` in `build/sheet.css` line ~231):
   navy `#0f1f2e`/`--navy800`, rust/orange `--rust600` (#e4622a, primary actions),
   `--rust100` light rust, pine green `--pine700`, sand/pale blue `--sand100/200/300`,
   ink `--ink900/700/500/300`. Font: Inter. White page.
8. Selected state is **calm** (navy or ink), never orange. Orange is for the action.

## What Claude drew (so yours must be different)

- **B · The calendar you already approved**: a month strip across all 15 months (both years),
  one month shown as a Sunday-first calendar with each departure as a bar across the five
  days, price on the bar. (Crow approved this calendar for a booking page in an earlier round.)
- **C · Every date on one screen**: one line per month, every date a chip with its price, tap
  one and a "Your date / Book this date" bar confirms it. No fold, no tabs.
- **D · The year, month by month**: 2026 / 2027 tabs, twelve month cards in a 4-across grid,
  each date a row with its price and "Book".

Look at them: `r8/preview/{calendar,wall,year}-{desk,phone}.png`.

## Your job: E, F, G

Three **genuinely different** ideas, different from B-D and from each other in structure,
not just styling. Territory worth exploring (pick any three, or better ones):

- **Pick the date where the button already is.** The booking panel's "Choose your date" opens
  a date picker right there (a popover/drawer calendar or list) instead of scrolling 7,200px.
  The Departures section can then be small. (If you do this, draw the panel open over the
  page; on phones it would be a bottom sheet.)
- **Ask first, then show.** "When would you like to go?" with seasons/months as big buttons
  (with price), then only that month's dates as large tappable cards.
- **Price-led timeline.** A horizontal strip of all 65 weeks where you can see at a glance
  which months cost $2,199 vs $1,999 and which are sold out, then pick one.
- **Next few first, the rest by month.** Big cards for the next 3 bookable dates, then a
  compact "any other month" chooser.

For each, give it a short plain name (2-5 words, no jargon, e.g. "Pick it in the panel").

## Deliverables (write ONLY inside `r8/codex/`)

- `r8/codex/mocks/E.html`, `F.html`, `G.html`: an HTML **fragment** (no `<html>`/`<head>`),
  authored for a **1440px wide** canvas, drawing the same region as `r8/frag/now.html`: the
  Departures section in its 928px column beside the 360px booking panel. Start from that
  file's markup: you may reuse its classes (`dp-page`, `dp-grid`, `dp-col`, `dp-h2`,
  `dp-rail` and children, `dp-pbar`) and change anything inside. Target **800-1,100px** tall
  at 1440. Use the real dates from the JSON (hand-write them, it's static HTML). No images
  needed; if you want one, ask yourself if it earns its place.
- `r8/codex/css/codex.css`: all your CSS. **Every selector must start with `.mock .cx-`** (or
  `.mockwrap.phone .cx-` for phone rules), so nothing leaks into the sheet or into Claude's
  drawings. Name your classes `cx-...`.
- **Phone.** The sheet has a Phone toggle that re-lays the SAME fragment at **390px wide** by
  adding class `phone` to the wrapper (`.mockwrap.phone`). Write `.mockwrap.phone .cx-...`
  rules so each design works at 390 with **zero horizontal overflow**. On a phone the booking
  panel is not beside the dates (it's hidden; `.dp-pbar`, a sticky bottom bar "From $1,999 /
  Choose your date", shows instead). If your design is a bottom sheet on phones, draw it.
- `r8/codex/notes/E.json` (and F, G), exactly this shape:
  ```json
  {"name": "Pick it in the panel",
   "changes": ["one plain sentence per numbered change, 3 or 4 of them"],
   "rings": [[1, ".cx-some-selector"], [2, ".cx-other"]],
   "body": "Two or three plain sentences: what it does for the customer, and its catch.",
   "cost": "about 1 day",
   "risk": "one plain sentence"}
  ```
  `rings` numbers match `changes`: each is a CSS selector (inside your fragment, matching ONE
  element) that the sheet circles with that number. `cost` is build time on a Next.js site
  where the data is already on the page.
- `r8/codex/notes/pick.json`: `{"pick": "F", "why": "two sentences"}`, which of YOUR three
  you'd build, and why.

## Check your work before you finish

Run `node r8/tools/preview.mjs codex/E codex/F codex/G` from `/home/james/swat/projects/swat-sept-sheet`.
It renders each fragment exactly as the sheet will, at 1440 and 390, writes PNGs to
`r8/preview/codex-E-desk.png` etc., and prints the height and any OVERFLOW. **Open the PNGs
and look at them.** Fix overflow, clipped text, anything that looks unfinished, and make sure
the three read as three different ideas at a glance. Iterate until you'd show them to a client.

Do not edit anything outside `r8/codex/`. Do not run git. Do not deploy.
