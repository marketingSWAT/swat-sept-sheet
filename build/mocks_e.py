"""Mockup primitives for round four — decision 41, redrawn.

Crow, on 16 September, looking at decision 41's option B on this sheet:

    "Look how the review box looks when it loads — it then extends down,
    there's a shit little white space below the photo and that just looks like
    shit. But it kind of gave me another idea: instead of putting it on the
    right-hand side, maybe you use that white space to just put the different
    reviews below … let's go with my first idea of having them kind of below
    the hero image. You could have up to three, I believe. So kind of building
    off option B, but just move it down to where that blank white space is
    right now."

So every panel here is drawn at **1440**, not 1200 — his window, and the width
the white space exists at. Re-measured on the deployed staging build on
16 September 2026, at 1440x900, on
`/tours/1-day-great-salt-lake-and-antelope-island-tour/` — the same tour
decision 41 draws, so the panels can be read against each other:

  Chrome         promo strip, header and back bar to y=159, breadcrumbs 76px,
                 hero row from **y=255**.
  Hero row       `grid lg:grid-cols-[1.7fr_1fr]`, 1,321 wide inside a 1,321px
                 shell. The gallery is **812x380** at x=52. The title column is
                 **478px** at x=896 and holds four things — a badge row, the
                 h1, the subtitle and a 184px price panel — and ends at
                 **y=600** against a gallery bottom of **y=635**. **That 35px
                 of slack is all the room the column has before it starts
                 leaving paper under the photograph.**
  Under it       the fact strip, the description 772x122 at y=701, the section
                 nav, then the body.
  Reviews band   913px wide at **y=1,539**, 281px tall — the shipped decision
                 26C, a full screen below the gallery.
  The screen     the sticky header is 73px and the window is 900, so 827px of
                 page is visible and the first screen ends at **y=900** — 265px
                 below the bottom of the photograph.
  The page       9,517px tall.

Option B put a review block under the price panel, which runs the 478px column
down past the gallery's bottom edge and leaves the white paper under the
photograph that he is objecting to. E, F and G all put the cards **in** it.
"""

import mocks as m
import mocks_c as c
import mocks_d as d


# --------------------------------------------------------------- the geometry
#: The live hero row at 1440, to the pixel. 812 + 30 + 478 = 1,320, which is
#: what `.mock.aw1440 .m-shell` gives (1440 less 60px of padding a side).
GAL_W, GAL_H = 812, 380
COL_W = 478
GAP = 30
SHELL = GAL_W + GAP + COL_W

#: The content column on the body of the page — the reviews band as shipped is
#: 913px, not the full shell, because the booking rail takes the rest.
BODY_W = 913

TITLE = 'Great Salt Lake and Antelope Island'
SUB = '1-Day Tour'

#: Placeholder, and it says so on the card. `data/tour-reviews.json` is still
#: empty, so every one of these drawings renders NOTHING on all 93 tours until
#: operations sends picks with a tour name against each.
REVIEWS = [
    ('Placeholder review &mdash; this is where a real guest review will sit '
     'once operations has picked them out, tour by tour. It is about the '
     'length one card holds before Read the full review takes over.',
     'Example', 'Sample data'),
    ('Placeholder review &mdash; the second of three. A card holds roughly '
     'forty words at this width, which is two or three sentences of a real '
     'review rather than the whole thing.',
     'Example', 'Sample data'),
    ('Placeholder review &mdash; the third. A trip with nine reviews against '
     'it shows three here and keeps the rest behind the link.',
     'Example', 'Sample data'),
]


def stars():
    return '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'


def head(big=False):
    """The score line. `big` is the h2 the band uses; small is the strip's."""
    cls = 'm-revhead' + ('' if big else ' tight')
    return (f'<div class="{cls}"><b>What guests said</b>{stars()}'
            '<span class="sc">4.9</span>'
            '<span class="n">from 38 reviews</span></div>')


def card(i=0, w=None, more=True):
    q, who, when = REVIEWS[i % len(REVIEWS)]
    style = f'style="width:{w}px"' if w else ''
    mo = '<span class="more">Read the full review</span>' if more else ''
    return (f'<div class="m-revcard" {style}>{stars()}'
            f'<p>&ldquo;{q}&rdquo;</p>'
            f'<span class="who">{who} &middot; {when}</span>{mo}</div>')


def strip(track=GAL_W, n=3, gap=16, drift=False, note=None, big=False):
    """`n` cards across a `track`-wide slot.

    The card width is arithmetic, not a guess: it is what decides whether a
    card holds a sentence or a fragment, and it is the whole argument between
    E (three across 812) and G (three across 1,320).
    """
    w = (track - gap * (n - 1)) // n
    cards = ''.join(card(i, w) for i in range(n))
    if drift:
        # One more card, half off the right edge, so the track never looks
        # finished — the drawn version of "slightly rotating to the right".
        cards += card(n, w)
        inner = (f'<div class="m-revdrift" style="width:{track}px">'
                 f'<div class="track" style="gap:{gap}px">{cards}</div></div>')
    else:
        inner = (f'<div class="m-revrow" style="width:{track}px;gap:{gap}px">'
                 f'{cards}</div>')
    foot = ''
    if note:
        foot = ('<div class="m-revfoot"><i class="on"></i><i></i><i></i>'
                f'<span>{note}</span></div>')
    return (f'<div class="m-revstrip" style="width:{track}px">'
            f'{head(big)}{inner}{foot}</div>')


def whitespace():
    """The thing being complained about, drawn rather than described.

    A hatched box filling the paper option B leaves under the photograph when
    the review block runs the title column past the gallery's bottom edge. Its
    height is not typed in: it stretches to the bottom of the column beside it,
    so it is always exactly the gap the option creates rather than a number
    that goes stale the moment a card grows a line.
    """
    return ('<div class="m-white"><span>white paper</span></div>')


# ------------------------------------------------------------------ the page
def gallery():
    thumbs = ''.join(f'<span class="m-th">{m.img(k, 152, 104)}</span>'
                     for k in ['darksky', 'bonneville', 'templesq', 'antelope'])
    return (f'<div class="m-gal">{m.img("antelope", 1624, 760)}'
            f'<div class="m-thumbs">{thumbs}</div></div>')


def pricebox():
    return ('<div class="m-pricebox"><span class="l">FROM</span>'
            '<b>$110</b><span class="s">per person, 2026</span>'
            '<span class="m-cta">Reserve a place</span></div>')


def titlecol(slot=''):
    return ('<div class="m-tt">'
            '<div class="m-badges"><span>Day tour</span></div>'
            f'<h1 class="m-h1">{TITLE}</h1>'
            f'<p class="m-ttsub">{SUB}</p>{pricebox()}{slot}</div>')


def hero(kind='now'):
    """The tour page's first screen, in the five shapes decision 41 now draws.

    'now'    — badge, title, price. The reviews are a full screen further down.
    'one'    — option B: one card at a time under the price panel, and the
               white paper it leaves under the photograph.
    'under'  — option E: three cards in that white paper, under the gallery.
    'drift'  — option F: the same slot, on a track that creeps right.
    'wide'   — option G: the strip spans the whole row, under both columns.

    The left-hand side is ALWAYS one element. Two children in a two-column
    grid puts the second one in the 1fr track and wraps the title column onto
    a second row at the gallery's width — which renders as a plausible-looking
    drawing of a layout that does not exist.
    """
    under = ''
    slot = ''
    tail = ''

    if kind == 'one':
        slot = (f'<div class="m-revslot">{head()}{card(0)}'
                '<div class="m-revfoot"><i class="on"></i><i></i><i></i>'
                '<span>one at a time &middot; 8 seconds &middot; stops on '
                'hover</span></div></div>')
        under = whitespace()
    elif kind == 'under':
        under = strip(GAL_W)
    elif kind == 'drift':
        under = strip(GAL_W, drift=True,
                      note='drifts right &middot; stops on hover &middot; '
                           'stands still at three reviews')
    elif kind == 'wide':
        tail = ('<div class="m-shell" style="padding-top:18px">'
                + strip(SHELL) + '</div>')

    if kind == 'one':
        # B is the one shape where the thing being drawn is *beside* the title
        # column rather than under the row, so the gallery and the hatched box
        # share column one of row one and stretch to the column's full height.
        left = f'<div class="m-galcol">{gallery()}{under}</div>'
        return ('<div class="m-shell">'
                f'<div class="m-tourtop rows one" style="grid-template-columns:'
                f'{GAL_W}px minmax(0,1fr);gap:{GAP}px">'
                f'{left}{titlecol(slot)}</div></div>')

    # The strip is a SIBLING of the gallery and the title column, placed into
    # row two of column one, rather than a child of the gallery's column. Two
    # reasons, and the second is the one that matters: the drawing then stacks
    # gallery -> title -> reviews on a phone, instead of putting three review
    # cards between the photograph and the name of the trip. Nested, there is
    # no order rule that can fix it.
    return ('<div class="m-shell">'
            f'<div class="m-tourtop rows" style="grid-template-columns:'
            f'{GAL_W}px minmax(0,1fr);gap:{GAP}px">'
            f'{gallery()}{titlecol(slot)}{under}</div></div>' + tail)


def below(band=False):
    """Everything under the hero row, in page order, so the depth a decision
    puts the reviews at is drawn rather than claimed."""
    cells = [('Duration:', '1 day'), ('Activity level:', 'Easy'),
             ('Group size:', 'Small group'),
             ('Departs from:', 'Salt Lake City'), ('From:', '$110')]
    fs = ''.join(f'<span class="f"><em>{k}</em> <b>{v}</b></span>'
                 for k, v in cells)
    facts = ('<div class="m-facts"><div class="m-shell">'
             f'<div class="m-factrow">{fs}</div></div></div>')
    tail = ''
    if band:
        # Decision 26C as it ships: the band is 913px, not the whole shell,
        # because the booking rail takes the rest of the row.
        tail = ('<div class="m-shell" style="padding-top:24px">'
                + strip(BODY_W, big=True) + '</div>')

    return (facts
            + m.subnav(['Right for you', 'Overview', 'Reviews', 'Seasons',
                        'Day by day', 'Tour details'], active='Overview')
            + '<div class="m-shell" style="padding-top:20px">'
            + m.notice() + '</div>'
            + '<div class="m-shell" style="padding-top:18px">'
            + c.rfy('line')
            + '<section class="m-sec" style="padding-top:20px">'
              '<h2>Overview</h2><p class="m-p"></p><p class="m-p"></p>'
              '<p class="m-p"></p><p class="m-p"></p></section></div>'
            + tail)


#: The drawn chrome comes to 214px above the gallery where the live page's
#: comes to 255 — the sheet's header, back bar and breadcrumbs are each a few
#: pixels tighter than the real ones. The fold is a claim about what is on
#: screen, so it is moved up by that difference rather than left at 900, which
#: would flatter every option by 41px.
FOLD = 900 - 41


def page(kind='now', band=False, foldline=True):
    """A full drawing: the chrome, the hero, the page under it, and the line
    where a 1440x900 window stops."""
    inner = (m.header(active='Destinations')
             + m.backbar()
             + m.crumbs('Home', 'Trip styles', 'Day tour',
                        'Great Salt Lake and Antelope Island')
             + hero(kind) + below(band))
    return inner + (d.fold(FOLD, 'bottom of a 1440&times;900 window')
                    if foldline else '')
