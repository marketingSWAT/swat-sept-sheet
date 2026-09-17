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

## Round two — decisions 30–39, sent 16 September

Built from Crow's walkthrough of the staging build. **Not yet answered.**

When the letters come back, record them verbatim below and add them to
`ANSWERS` in `build/sheetkit.py`, keyed by decision number, so the sheet itself
folds and carries the record.

Format:

```
## 32 — The buttons, and the ragged right edge
**C** · "thirty-two goes to C, but keep the pills on the home page"
Crow, voice note, <date> · revision: <anything attached to the yes>

**Shipped deviation.** <what the build did differently, why, and what going
back would cost.>
```

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
