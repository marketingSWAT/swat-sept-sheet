# Answers

Two rounds live on one link. Letters never recycle, and a letter is bound to an
option *name* for the life of the sheet — `build/letters.json` is the ledger and
a collision is a build failure, not a warning.

---

## Round one — decisions 20–29, answered 16 September

**Crow answered the whole sheet at once:** *"Okay let's go ahead and do all of
your recommended picks and build that out and push it to staging so I can look
at it on the staging environment."*

So every decision went to the option marked **MY PICK**:

| # | Decision | Letter | Option | Where it stands now |
|---|---|---|---|---|
| 20 | How hard this trip is, on the card | **C** | The mark, and a pop-up | Shipped. Reopened by decision **35** — the empty "on request" state |
| 21 | Where a tour page explains the level | **C** | A panel under the fact strip | Shipped. Reopened by decision **37** — it takes too much space |
| 22 | Showing a trip in the season you would travel it | **C** | A season band under the facts | Shipped, signed off |
| 23 | Filtering the catalogue by when you can travel | **C** | One bar, four questions | Shipped, signed off |
| 24 | Picking where you want to go | **C** | Map and chips together | Shipped. *"I love the interactive map, I think that looks great."* Refined by 31–33 |
| 25 | The industry / trade audience | **B** | One tab, three doors | Shipped. *"The partner pages looks good."* |
| 26 | Where the reviews for a trip go | **C** | Rating in the rail, reviews in a band | Shipped. Reopened by decision **36** — wrong place on the page |
| 27 | Where the films go | **C** | Highlights up top, Monica below | Shipped. *"The slot for a video looks good."* Extended by decision **39** |
| 28 | Catching a trip builder somebody walks away from | **D** | The prompt, with a way to save it | Shipped, signed off |
| 29 | The strip above the hot deals ticker | **B** | The campaign takes the strip | Shipped. *"I like the bars, that looks good."* |

All ten are folded on the sheet with their letters printed on the front, so the
link carries the record.

### Shipped deviations from round one

Named here because a silent deviation is how a sheet stops being trusted. All
three were in the hand-over at the time and none has been overruled.

- **Decision 20 — the mark has four segments, not three.** The sheet drew
  three. The published scale is four levels and a three-step mark cannot
  separate Challenging from Strenuous, which is the one boundary where being
  wrong has a consequence. The argument for three — that three of anything
  horizontal cannot be read as a score out of five — still holds at four.
- **Decision 26 — the reviews band sits *after* the Overview, not under the
  fact strip.** Three separate decisions asked for that same slot. 21's
  qualifying panel kept it, because it is the safety question and it is what the
  cards and the rail anchor to. 26C's actual requirement was "before the
  itinerary rather than after the price", and the Overview is not the itinerary.
- **Decision 27 — the film tile renders nothing rather than an empty frame.**
  There is still no cut, so the slot is behind a flag.

---

## Round two — decisions 30–39, answered 16 September

Answered decision by decision in one voice note the same evening. Nine of the
ten went to the recommendation; **36 was sent back** and is redrawn on the
sheet rather than folded.

| # | Decision | Letter | Option | Where it stands |
|---|---|---|---|---|
| 30 | The wall of words above the builder | **C** | One line up, the four promises below | Built, staging |
| 31 | Naming the states on the map | **B** | Every state, two letters | Built, staging |
| 32 | The buttons, and the ragged right edge | **C** | An even grid | Built, staging |
| 33 | The shape of the Build Your Own page | **B** | The map goes wide, the questions go under it | Built, staging |
| 34 | What the page does while you answer it | **C** | The map answers with the place | Built, staging — C only |
| 35 | "Activity level on request" on a card | **A** | Empty track, as now | *"maybe just leave it as is"* — nothing built |
| 36 | The title, the price panel, and a review bar | — | **sent back** | Redrawn as E–H; C was never built |
| 37 | Where "Is this trip right for you?" goes | **C** | One line up top, the panel down low | Built, staging |
| 38 | Start where you are, after the first tap | **C** | The answers are photographs too | Built, staging |
| 39 | The highlights film, beside SWAT's own words | **B** | Copy left, film right | Built, staging, behind the film flag |

### What 36 was sent back for

> *"I don't think you understood what I was asking… I want to make those
> reviews like squares, so you can at least read some of the review — and
> there's like three side by side that's slowly rotating, versus this weird
> rectangle bar you have. I like how you have the review number, that looks
> great."*

Four new options, **E–H**; A keeps its letter as the Now panel and **B, C and D
are retired** — those letters are spent. The measurement that decides it: the
title column is 395px, so three squares in it are 120px each. Three cards only
fit under the gallery (672px, E) or across both columns (1,100px, F and G).

### Shipped deviations from round two

Named here because a silent deviation is how a sheet stops being trusted.

- **38C also keeps the door you chose**, as a photo card beside the question.
  That is option **B** of the same decision, built alongside C. C only puts
  photographs behind the *destination* axis; on the other three doors the band
  still emptied itself, which is the thing that was objected to. B was priced
  at a day on the sheet and the sheet said it was worth having anyway.
- **31B stands its labels down below `sm`.** At 390px the map renders 203px
  tall and an 18-unit code is about 7px — fifty of them is a haze. A *selected*
  state is still named at every width, which is the behaviour Crow said he
  liked.
- **33B is measured, and it did not shorten the page.** The builder band is
  1,877px against 1,523px as it shipped: the map went from 737px wide to
  1,112px and the country is 1.92:1, so it is 579px tall. The page height comes
  off decision 30 — the form now starts at y=740 against y=1,344 — and nowhere
  else. The sheet predicted +70px on the band; the real number is +354px.
- **37C's line is 44px on a graded trip and about 89px on one with no level**,
  where the sentence is longer. Against 267px either way.

### What is already decided inside this round, without a letter

- **The interactive map stays.** *"I love the interactive map, I think that
  looks great."* Nothing in 31–33 takes it away; two of the three make it
  bigger.
- **The nav wrapping onto two lines at 1200px** is a defect, not a choice.
  Fixing on sight.
- **The floating "Search trips" pill** standing down on pages that own the
  bottom-right corner — same.

### The one place this round argues with SWAT

Decision **37**. Crow wants "Is this trip right for you?" removed or moved much
lower; SWAT operations asked for it, high up, because *"we have people who will
book a hiking trip when they use a walker."* The sheet recommends C — one line
high, the full panel low — and says plainly that B (remove it) is available and
that Jason or operations should be copied if it ships.
