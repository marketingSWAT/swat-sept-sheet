"""Mockup primitives for round three — decisions 40 and 41.

Round three is two things Crow said while walking the *built* round-two work on
the evening of 16 September: the Build Your Own map is too tall to see the
answers under it, and the reviews are still not where he asked for them.

Everything here is measured off the deployed staging build on 16 September
2026, after decisions 30-35 and 37-39 shipped, at **1440x900** — Crow's own
window, and the one the complaints are about.

  /custom-tours/  Question one is **955px tall**: the legend at y=884, the map
                  1,319x687 from a 960x500 viewBox, and sixteen places four
                  across in four 48px rows from y=1,622 to y=1,838. The sticky
                  header is 73px, so a 900px window shows 827px of page.
                  Scroll the question to the top of that and the window ends at
                  y=1,711 — **two of the four rows of places are below it** and
                  the second row is cut in half. The map alone is 72% of the
                  block.

  /tours/1-day-great-salt-lake-and-antelope-island-tour/
                  Gallery 812x380 at y=255. The title column is 478px wide at
                  x=896 and holds four things: one badge ("Day tour"), an h1
                  75px tall, the subtitle "1-Day Tour", and the 184px price
                  panel, which ends at y=601 against a gallery bottom of y=635
                  — **34px of slack**. The description Crow remembers being up
                  there is not: it is 772x122 at **y=701**, under the six-cell
                  fact strip. The reviews band is 281px at **y=1,539**, which
                  is 1,284px below the top of the gallery.

Decision 40 is authored at **1440**, not the sheet's usual 1200. The complaint
is that a 1440x900 window cannot hold the question, so the drawing has to be
that window. Decision 41 stays at 1200, so it can be read against decision 36,
which Crow has already looked at.
"""

import mocks as m
import mocks_c as c


# ----------------------------------------------------------------- the fold
#: Measured on staging: the sticky header is 73px and the window is 900, so
#: 827px of page is on screen under it.
HEADER = 73
WINDOW = 900
USABLE = WINDOW - HEADER


def fold(top=WINDOW, label='bottom of a 1440&times;900 window'):
    """The edge of the screen, drawn across the canvas.

    Everything below the dashes is on the page and not on the screen. It is
    the only honest way to draw "I can't see all the options below" — a height
    in a caption is a number, and this is the thing itself.
    """
    return (f'<div class="m-dim" style="top:{top}px"></div>'
            f'<div class="m-fold" style="top:{top}px"><span>{label}</span></div>')


def scrolled(inner):
    """A canvas that is a *window*: the sticky header, the page scrolled so
    question one sits directly under it, and the fold where the screen ends."""
    return (m.header(active='Build Your Own', strip=False) +
            '<div class="m-band sand" style="padding:18px 0 34px">'
            f'<div class="m-shell">{inner}</div></div>' + fold())


# ------------------------------------------------------------ question one
SEL = ('UT', 'AZ')
ON = ('Utah', 'Arizona')


def qhead(n=1, title='Where would you like to go?', hint=True):
    h = '<em>pick as many as you like</em>' if hint else ''
    return (f'<div class="m-qh"><b>{n}.</b><span>{title}</span>{h}</div>')


def places(cols=4):
    """The sixteen places as the even grid decision 32C shipped."""
    opts = c.QUESTIONS[0][2]
    inner = ''.join(
        f'<span class="m-cell{" on" if o in ON else ""}">'
        f'<i class="m-tick"></i>{o}</span>' for o in opts)
    return (f'<div class="m-cells" style="grid-template-columns:'
            f'repeat({cols},minmax(0,1fr))">{inner}</div>')


def q1(mode='now'):
    """Question one in the four shapes decision 40 draws.

    'now'    — the map full width at 687px, the places four across under it.
    'short'  — the same arrangement, the map capped at 380px.
    'split'  — the map keeps the left, the sixteen places take the right.
    'all'    — the map keeps the left, every question takes the right.
    """
    if mode == 'now':
        return (qhead() + c.nationmap(selected=SEL, labels='sel', h=687)
                + places(4))

    if mode == 'short':
        # 520, not 380. The live map is `w-full h-auto` on a 960x500 viewBox
        # whose ink fills it (906x485 measured), so height cannot be taken off
        # it without taking width too: H=520 means W=998. 520 is the tallest
        # the map can be and still leave the question inside an 827px screen —
        # H + 267px of legend, gap and four rows of places.
        return ('<div class="m-mapcap">' + qhead()
                + c.nationmap(selected=SEL, labels='all', h=520)
                + '</div>' + places(4))

    if mode == 'split':
        return (qhead() +
                '<div class="m-q2" style="grid-template-columns:820px '
                'minmax(0,1fr)">'
                + c.nationmap(selected=SEL, labels='all', h=427)
                + '<div><p class="m-qside">OR PICK FROM THE LIST</p>'
                + places(2) + '</div></div>')

    # 'all' — the map holds the left column on its own and everything else,
    # including the last four questions, runs down the right.
    rest = ''.join(c.question(i, 'grid', n=i + 1) for i in (1, 2, 3, 4))
    left = ('<div>' + qhead() +
            c.nationmap(selected=SEL, labels='all', h=365) +
            '<p class="m-qside" style="margin:11px 0 0">STAYS ON SCREEN WHILE '
            'YOU ANSWER THE REST</p></div>')
    right = ('<div><p class="m-qside">OR PICK FROM THE LIST</p>'
             + places(2) + rest + '</div>')
    return ('<div class="m-q2" style="grid-template-columns:700px '
            f'minmax(0,1fr)">{left}{right}</div>')


# ---------------------------------------------------------- the review slot
#: Placeholder, and it says so. `data/tour-reviews.json` is still empty — Matt
#: owes the picks — so every one of these drawings renders NOTHING at all on a
#: real tour page until it arrives.
REV = ('&ldquo;Placeholder review &mdash; this is where a real guest review '
       'will sit once operations has picked them out by tour. It is long '
       'enough to show what one looks like in this column.&rdquo;')
REV2 = ('&ldquo;Placeholder review &mdash; the next one arrives from the '
        'right every eight seconds, and stops the moment you point at '
        'it.&rdquo;')


def revhead():
    return ('<div class="m-revhead"><b>What guests said</b>'
            '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            '<span class="sc">4.9</span>'
            '<span class="n">from 38 reviews</span></div>')


def revcard(text=REV, more=True):
    mo = '<span class="more">Read the full review</span>' if more else ''
    return ('<div class="m-revone">'
            '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            f'<p>{text}</p>'
            '<span class="who">Example &middot; Sample data</span>'
            f'{mo}</div>')


def revfoot(note='one at a time &middot; 8 seconds &middot; stops on hover'):
    return ('<div class="m-revfoot"><i class="on"></i><i></i><i></i>'
            f'<span>{note}</span></div>')


def revslot(kind='one'):
    """The review block as it sits in the 478px title column."""
    if kind == 'one':
        return (f'<div class="m-revslot">{revhead()}{revcard()}'
                f'{revfoot()}</div>')
    # 'creep' — the same cards on a track that drifts right, so the edge of
    # the next one is always in view and the track never looks finished.
    track = ('<div class="m-revcreep"><div class="track">'
             f'{revcard(REV)}{revcard(REV2)}{revcard(REV)}</div></div>')
    return (f'<div class="m-revslot">{revhead()}{track}'
            + revfoot('drifts right &middot; stops on hover') + '</div>')


# ------------------------------------------------------------ the tour top
#: Verbatim off the deployed page.
TITLE = 'Great Salt Lake and Antelope Island'
SUB = '1-Day Tour'
DESC = ('Experience spectacular views of the Great Salt Lake, step back in '
        'time with a visit to the historic Fielding Garr Ranch, and enjoy '
        'viewing opportunities of free-ranging bison, mule deer, bighorn '
        'sheep, pronghorns, and millions of birds who congregate along the '
        'shores of the Great Salt Lake.')


def gallery():
    thumbs = ''.join(f'<span class="m-th">{m.img(k, 152, 104)}</span>'
                     for k in ['darksky', 'bonneville', 'templesq', 'antelope'])
    return (f'<div class="m-gal">{m.img("antelope", 1344, 760)}'
            f'<div class="m-thumbs">{thumbs}</div></div>')


def pricebox():
    return ('<div class="m-pricebox"><span class="l">FROM</span>'
            '<b>$110</b><span class="s">per person, 2026</span>'
            '<span class="m-cta">Reserve a place</span></div>')


def pricebar():
    return ('<div class="m-pricebar"><div><span class="l">FROM</span>'
            '<b>$110</b></div><span class="s">per person, 2026</span>'
            '<span class="m-cta">Reserve a place</span></div>')


def tourtop(kind='now'):
    """The tour page's first screen in the shapes decision 41 draws.

    'now'   — badge, title, subtitle, price. The reviews are 1,284px further
              down the page.
    'one'   — one review at a time under the price panel.
    'creep' — the same cards on a track that drifts right.
    'desc'  — the description comes up into the column and the reviews follow
              it; the price panel moves under the gallery as a wide bar.
    """
    head = ('<div class="m-badges"><span>Day tour</span></div>'
            f'<h1 class="m-h1">{TITLE}</h1>'
            f'<p class="m-ttsub">{SUB}</p>')

    if kind == 'desc':
        left = f'<div class="m-galcol">{gallery()}{pricebar()}</div>'
        right = (f'<div class="m-tt">{head}'
                 f'<p class="m-ttdesc">{DESC}</p>{revslot("one")}</div>')
        return ('<div class="m-shell">'
                f'<div class="m-tourtop">{left}{right}</div></div>')

    slot = {'one': revslot('one'), 'creep': revslot('creep')}.get(kind, '')
    right = f'<div class="m-tt">{head}{pricebox()}{slot}</div>'
    return ('<div class="m-shell">'
            f'<div class="m-tourtop">{gallery()}{right}</div></div>')


# -------------------------------------------- the page under the first screen
def facts(desc=True):
    """The six-cell fact strip, with or without the description under it.

    `desc=False` is the option that moves the intro paragraph up into the
    title column, so it must not also print here: a drawing that shows the
    same paragraph twice is lying about the option it is drawing.
    """
    cells = [('Duration:', '1 day'), ('Activity level:', 'Easy'),
             ('Group size:', 'Small group'),
             ('Departs from:', 'Salt Lake City'), ('From:', '$110')]
    fs = ''.join(f'<span class="f"><em>{k}</em> <b>{v}</b></span>'
                 for k, v in cells)
    d = f'<p class="m-lede">{DESC}</p>' if desc else ''
    return ('<div class="m-facts"><div class="m-shell">'
            f'<div class="m-factrow">{fs}</div>{d}</div></div>')


def belowtop(reviews=False, desc=True):
    """Everything from the fact strip down to the end of the Overview, in page
    order, so the depth the reviews sit at is the drawing rather than a claim.
    """
    band = ''
    if reviews:
        band = ('<div class="m-shell" style="padding-top:26px">'
                f'{c.revhead(wide=True)}{c.revcards(1100)}</div>')
    return (facts(desc)
            + m.subnav(['Right for you', 'Overview', 'Reviews', 'Seasons',
                        'Day by day', 'Tour details'], active='Overview')
            + '<div class="m-shell" style="padding-top:20px">'
            + m.notice() + '</div>'
            + '<div class="m-shell" style="padding-top:18px">'
            + c.rfy('line')
            + '<section class="m-sec" style="padding-top:20px">'
              '<h2>Overview</h2><p class="m-p"></p><p class="m-p"></p>'
              '<p class="m-p"></p><p class="m-p"></p></section></div>'
            + band)
