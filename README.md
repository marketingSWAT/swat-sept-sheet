# SWAT storefront — the 16 September 2026 review, drawn

Ten decisions pulled out of the 16 September review with Matt Warren, Lance Card
and SWAT's operations side. Each shows the build as it ships today beside two to
four alternatives, so the answer can be a letter said out loud.

Numbering continues from `swat-decision-sheet` (decisions 1–19, answered in
full), so "twenty-three goes to B" can only mean one thing.

- `build/render.py` — the generator. `python3 build/render.py` writes `site/`.
- `build/sheetkit.py` — the letter ledger and the four blocks a decision is
  built from. Separate from `render.py` so the decision files can import it
  without a cycle.
- `build/decisions_a.py` — 20–24: activity level, seasons, the state picker.
- `build/decisions_b.py` — 25–29: the trade page, reviews, video, unfinished
  forms, the campaign strip.
- `build/mocks.py` — mockup primitives, the storefront's own tokens and real
  Supabase photography.
- `build/usmap.py` — every US state outline, projected and baked. Generated
  from us-atlas `states-10m` by `scratchpad/mkmap.py`; do not hand-edit.
- `build/letters.json` — the letter ledger. A letter is bound to an option NAME
  for the life of the sheet; renaming an option issues a new letter.
- `PICKS.md` — the answer log. Answers also go into `ANSWERS` in
  `build/sheetkit.py` so the link itself holds the record.

## Provenance

Every "Now" panel was read off the **deployed staging build** at a 1200px
viewport on 16 September 2026, after round one of these notes shipped:
`swat-website-storefront-git-staging-swat2.vercel.app` (gate 6666).

Measured, not estimated: trip shelf 3-across at 350.2px with 515px cards; tour
page 672×380 gallery against a 395px title column; fact strip at y=659, sticky
subnav at y=847, change notice at y=961, 360px booking rail beside it; tour page
11,468px tall; `/trips/` style tiles 356px, 3-across, Large group = 3 trips.

**Re-derive before the next round:** the eight featured trips (November's, under
the 60-day floor), the four live deals and their promo codes, the 61 departure
dates on the Mighty 5.

## Traps this round cost time on

- **`aspect-ratio:1200/var(--mh)` was hard-coded** in the inherited CSS while
  `mock()` had grown an `aw` argument. Decision 20 is authored at 760px and
  rendered into a 1200-wide box, so every card was clipped at a third of its
  height with no error.
- **An inline `width` on `.mock` beats `.mockwrap.phone .mock{width:390px}`.**
  The phone toggle then renders the desktop canvas inside a 390px box and it
  overflows sideways. The width has to come from `--aw` through CSS.
- **`grid-template-columns:1fr` is not enough on a phone.** A 1fr track floors
  at min-content, and the sideways-scrolling chip row inside it has none — one
  step of the trip builder grew to 1,393px. `minmax(0,1fr)` plus `min-width:0`
  on every grid child.
- **SVG `font-size` is in user units.** Labels at 13 inside an 830-unit viewBox
  scaled into a sheet column render at four pixels.
- **46KB of baked state paths, four times over.** Each map is a row of `<use>`
  references and the geometry is emitted once into a hidden `<defs>`.

Source transcript: `/mnt/c/Users/james/clawd-inbound/swat-meeting-2026-09-16-transcript.txt`
