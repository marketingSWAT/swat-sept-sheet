"""Mockup primitives for round two of the 16 September notes — decisions 30-39.

Everything here is drawn from the deployed staging build measured at a 1200px
viewport on 16 September 2026, after round one of the 16 September decisions
(20-29) shipped. The numbers quoted in the decision prose are the ones this
file draws:

  /custom-tours/     4,936px tall. "What a custom trip means here" is 570px and
                     puts "Start here to build your trip" at y=1,344. 40 pill
                     buttons, radius 999px, 44px tall, 57-163px wide, in 8
                     wrapped rows with 8 different right edges — 695, 763, 280,
                     611, 443, 544, 694, 497 — inside a 739px column. The map
                     renders 737x384 from a 960x500 viewBox and carries no
                     label until a state is selected, and then the full name.

  /                  Home shelf: 4 of the 8 cards print "Activity level on
                     request". "Start where you are" is 540px with four 263x197
                     photographs; answering the first question leaves the
                     section with ZERO images and 15 pills in 3 rows whose
                     right edges are 1137, 414 and 94. SWAT's own paragraph
                     ("With Southwest Adventure Tours") is 359px of full-width
                     prose at y=4,580.

  /tours/1-day-great-salt-lake-and-antelope-island-tour/
                     9,697px tall. Gallery 672x380 at y=255; title column 395px
                     at x=747; the h1 is 34px and 75px tall; the price panel is
                     184px and ends at y=601 against a gallery bottom of y=635,
                     so there are 34px of slack in that column today. "Is this
                     trip right for you?" is 267px at y=1,185. The reviews band
                     is 326px at y=1,764 and every word in it is placeholder.
"""

import mocks as m
import usmap as _usmap


# --------------------------------------------------------------- the map
#: The eight north-eastern states that cannot hold a two-letter label inside
#: their own outline at this scale. Standard cartography: label them in the
#: margin with a leader line rather than letting the code sit on a neighbour.
LEADERS = ['VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD']

#: Where each leader label parks, in viewBox units. The viewBox is
#: "85 4 830 580", so x=884 is inside the canvas with room for two characters.
LEADER_X = 884
LEADER_Y = {'VT': 60, 'NH': 84, 'MA': 108, 'RI': 132, 'CT': 156,
            'NJ': 180, 'DE': 204, 'MD': 228}


def nationmap(selected=(), lit=(), labels='sel', h=360, cls=''):
    """The national map, with the three labelling schemes decision 31 argues.

    `labels`:
      'sel'   — what ships today: nothing until a state is picked, and then
                its full name, centred in white.
      'all'   — every state's two-letter code, with the eight crowded
                north-eastern ones led out to the margin.
      'ours'  — only the states the catalogue already sells, plus anything
                picked. Fewer labels; says "we don't go there" by omission.
    """
    uses = []
    for ab in sorted(_usmap.PATHS):
        c = 'sel' if ab in selected else ('lit' if ab in lit else '')
        uses.append(f'<use href="#s-{ab}" class="{c}"/>')

    text = ''
    if labels == 'sel':
        # Full names, only on the chosen states — the live behaviour.
        text = ''.join(
            f'<text class="mlab full{" on" if ab in selected else ""}" '
            f'x="{x}" y="{y}">{_FULL.get(ab, ab)}</text>'
            for ab, (x, y) in _usmap.ANCHORS.items()
            if ab in selected and _usmap.ANCHORS.get(ab))
    else:
        show = (sorted(_usmap.PATHS) if labels == 'all'
                else [a for a in sorted(_usmap.PATHS)
                      if a in m.BUILDER_STATES or a in selected])
        bits = []
        for ab in show:
            at = _usmap.ANCHORS.get(ab)
            if not at:
                continue
            on = ' on' if ab in selected else ''
            if ab in LEADERS:
                ly = LEADER_Y[ab]
                bits.append(
                    f'<line class="mlead{on}" x1="{at[0]}" y1="{at[1]}" '
                    f'x2="{LEADER_X - 6}" y2="{ly - 4}"/>'
                    f'<text class="mlab{on}" x="{LEADER_X}" y="{ly}" '
                    f'text-anchor="start">{ab}</text>')
            else:
                bits.append(f'<text class="mlab{on}" x="{at[0]}" y="{at[1]}">'
                            f'{ab}</text>')
        text = ''.join(bits)

    return (f'<div class="m-map {cls}" style="height:{h}px">'
            f'<svg viewBox="{_usmap.VIEW}" preserveAspectRatio="xMidYMid meet">'
            f'{"".join(uses)}{text}</svg></div>')


_FULL = {'UT': 'Utah', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado',
         'NV': 'Nevada', 'WY': 'Wyoming', 'OR': 'Oregon', 'SD': 'South Dakota',
         'AK': 'Alaska', 'HI': 'Hawaii', 'NM': 'New Mexico', 'TX': 'Texas',
         'MT': 'Montana', 'WA': 'Washington'}


# ------------------------------------------------------- the five questions
#: Verbatim off the deployed builder, in order, with the live option lists.
QUESTIONS = [
    ('Where would you like to go?', 'pick as many as you like',
     ['Utah', 'Arizona', 'California', 'Colorado', 'Nevada', 'Wyoming',
      'Oregon', 'South Dakota', 'Alaska', 'Hawaii', 'New Mexico', 'Texas',
      'Montana', 'Washington', 'Canada', 'Somewhere else']),
    ('How long do you have?', None,
     ['Half day', '1 day', '2-3 days', '4-6 days', '7-10 days', '11+ days']),
    ('How many of you?', None,
     ['Just the two of us', '3&ndash;6', '7&ndash;13', '14 or more']),
    ('Roughly when?', None,
     ['Spring', 'Summer', 'Autumn', 'Winter', 'Not decided yet']),
    ('How do you like to travel?', None,
     ['Backpacking', 'Guided small group', 'Day tour', 'Self-drive',
      'Private &amp; custom', 'Large group', 'Rail &amp; cruise', 'Winter',
      'Special event']),
]

#: How many columns each question's grid takes when the answers are laid out
#: evenly. Sixteen places want four; six durations want three.
GRIDCOLS = [4, 3, 4, 5, 3]


def answers(i, style, on=()):
    """One question's answers, drawn in the style decision 32 is arguing.

    `style`:
      'pill'   — 999px radius, content-width, wrapped. What ships.
      'square' — same layout, 4px radius. The cheapest change.
      'grid'   — every answer the same width in a fixed column count.
      'row'    — 'grid', with the question's label in a fixed left gutter.
    """
    _, _, opts = QUESTIONS[i]
    cls = {'pill': 'm-chip', 'square': 'm-chip sq'}.get(style, 'm-cell')
    if style in ('pill', 'square'):
        inner = ''.join(
            f'<span class="{cls}{" on" if o in on else ""}">{o}</span>'
            for o in opts)
        return f'<div class="m-chips">{inner}</div>'
    inner = ''.join(
        f'<span class="m-cell{" on" if o in on else ""}">'
        f'<i class="m-tick"></i>{o}</span>' for o in opts)
    return (f'<div class="m-cells" style="grid-template-columns:'
            f'repeat({GRIDCOLS[i]},minmax(0,1fr))">{inner}</div>')


def question(i, style, on=(), n=None, mapmode=None, selected=()):
    """A numbered question with its answers, in the current form's shape."""
    title, hint, _ = QUESTIONS[i]
    h = f'<em>{hint}</em>' if hint else ''
    mp = ''
    if mapmode:
        mp = nationmap(selected=selected, labels=mapmode, h=384)
    body = mp + answers(i, style, on)
    if style == 'row':
        return (f'<div class="m-qrow"><div class="m-qlab">'
                f'<b>{n or i + 1}.</b><span>{title}</span>{h}</div>'
                f'<div class="m-qans">{body}</div></div>')
    return (f'<div class="m-q"><div class="m-qh"><b>{n or i + 1}.</b>'
            f'<span>{title}</span>{h}</div>{body}</div>')


def notesq(n=6, style='pill'):
    title = 'Anything else we should know?'
    box = ('<div class="m-ta">Mobility, a birthday, somewhere you have always '
           'wanted to see, a date that is fixed.</div>')
    if style == 'row':
        return (f'<div class="m-qrow"><div class="m-qlab"><b>{n}.</b>'
                f'<span>{title}</span></div><div class="m-qans">{box}</div></div>')
    return (f'<div class="m-q"><div class="m-qh"><b>{n}.</b>'
            f'<span>{title}</span></div>{box}</div>')


# ------------------------------------------------------------ the summary
def sofar(rows=None, cta='Send this to a planner', extra=''):
    rows = rows or [('Where', '&mdash;'), ('Length', '&mdash;'),
                    ('Group', '&mdash;'), ('When', '&mdash;'),
                    ('How you travel', '&mdash;')]
    inner = ''.join(f'<div class="m-sf-r"><span>{k}</span><b>{v}</b></div>'
                    for k, v in rows)
    return ('<aside class="m-sofar"><span class="l">YOUR TRIP SO FAR</span>'
            f'{inner}{extra}'
            '<div class="m-field"><span class="l">YOUR NAME</span>'
            '<div class="m-inp"></div></div>'
            '<div class="m-field"><span class="l">EMAIL</span>'
            '<div class="m-inp"></div></div>'
            f'<div class="m-cta wide">{cta}</div>'
            '<p class="m-fine">Answer as much or as little as you like. '
            'Nothing is booked here. A guide replies within one working '
            'day.</p></aside>')


# -------------------------------------------------- the page above the form
MEAN_P1 = ('Most of what we run is a scheduled small-group departure of seven '
           'to thirteen people. A custom trip is the same operation pointed at '
           'your group instead: the same guides, the same vehicles, the same '
           'permits and lodging relationships, on dates you choose.')
MEAN_P2 = ('It is the part of the business a visitor almost never discovers, '
           'because it has never had a page. If the catalogue does not have '
           'the trip you want, that is not the end of the conversation &mdash; '
           'it is usually the start of one.')

PROMISES = [
    ('Your places', 'Any combination of the parks and monuments we already '
                    'guide, in the order that suits you.'),
    ('Your dates', 'Not tied to a published departure window.'),
    ('Your group', 'Families, friends, photography groups, clubs and '
                   'corporate travel.'),
    ('Your pace', 'From lodge-based sightseeing through to backpacking, or a '
                  'mix across the same trip.'),
]


def hero(short=True, intro=None, strip=False):
    """The page hero. 'short' is the real height class on /custom-tours/."""
    intro = intro or ('We design private and custom itineraries across the '
                      'national parks of the American West &mdash; your '
                      'places, your dates, your pace.')
    st = ''
    if strip:
        cells = ''.join(f'<span><b>{t}</b>{d}</span>' for t, d in PROMISES)
        st = f'<div class="m-herostrip">{cells}</div>'
    return ('<div class="m-phero"><img src="' + _HEROSRC + '" alt="">'
            '<div class="m-phero-tx"><span class="k">BUILD YOUR OWN</span>'
            '<h1>A trip built around you</h1>'
            f'<p>{intro}</p></div>{st}</div>')


_HEROSRC = (m.SUPA + m.PHOTOS['zion2'] + '?width=2400&height=620&resize=cover&quality=68')


def meaning(mode='full'):
    """The block Crow asked to remove, in the four shapes decision 30 draws."""
    if mode == 'none':
        return ''
    if mode == 'line':
        return ('<div class="m-shell"><p class="m-meanline">A custom trip is '
                'the same operation pointed at your group: the same guides, '
                'vehicles, permits and lodging, on dates you choose. '
                '<a>What that means &rsaquo;</a></p></div>')
    cards = ''.join(f'<div class="m-promise"><b>{t}</b><p>{d}</p></div>'
                    for t, d in PROMISES)
    return ('<div class="m-shell"><div class="m-mean">'
            '<h2 class="m-h2">What a custom trip means here</h2>'
            f'<p>{MEAN_P1}</p><p>{MEAN_P2}</p>'
            f'<div class="m-promises">{cards}</div>'
            '<p class="m-callus">Prefer to talk it through? '
            '<a>800-970-5864</a></p>'
            '</div></div>')


def buildhead(sub=True):
    s = ('<p class="m-sub">Tap through what you have in mind. Nothing is booked '
         'here &mdash; a guide reads it and comes back with a real itinerary '
         'and a real price.</p>') if sub else ''
    return f'<h2 class="m-h2">Start here to build your trip</h2>{s}'


# --------------------------------------------------------- builder layouts
def builder(style='pill', mapmode='sel', selected=(), on=None, extra='',
            layout='now'):
    """The whole form, in the arrangement decision 33 is arguing.

    `layout`:
      'now'    — one 739px column of six stacked questions, 320px aside.
      'wide'   — the map full width at the top, the four remaining questions
                 in one aligned block beneath, summary across the foot.
      'sticky' — the map pinned left, the questions in a card on the right.
      'board'  — map left, the four short questions as a 2x2 board right.
    """
    on = on or {}
    q = lambda i, **kw: question(i, style, on=on.get(i, ()), **kw)   # noqa: E731

    if layout == 'now':
        left = (q(0, mapmode=mapmode, selected=selected) + q(1) + q(2) +
                q(3) + q(4) + notesq(6, style))
        return (f'<div class="m-shell"><div class="m-2col" '
                f'style="gap:40px;grid-template-columns:739px 320px">'
                f'<div class="m-2l">{left}</div>{sofar()}</div></div>')

    if layout == 'wide':
        # The four short questions go TWO ACROSS, which is where the height
        # actually comes from: four stacked blocks become two rows. Drawing
        # them stacked would have made the panel taller than the one it claims
        # to shorten, and the number under the drawing would have been a lie.
        pairs = ''.join(
            f'<div class="m-pair">'
            f'{question(a, style, on=on.get(a, ()), n=a + 1)}'
            f'{question(b, style, on=on.get(b, ()), n=b + 1)}</div>'
            for a, b in ((1, 2), (3, 4)))
        return ('<div class="m-shell">'
                '<div class="m-q"><div class="m-qh"><b>1.</b>'
                '<span>Where would you like to go?</span>'
                '<em>pick as many as you like</em></div>'
                + nationmap(selected=selected, labels=mapmode, h=400) +
                answers(0, style, on=on.get(0, ())) + '</div>'
                f'{extra}'
                f'<div class="m-2col" style="gap:40px;'
                f'grid-template-columns:minmax(0,1fr) 320px">'
                f'<div class="m-2l">{pairs}{notesq(6, style)}</div>'
                f'{sofar()}</div>'
                '</div>')

    if layout == 'sticky':
        rest = ''.join(question(i, style, on=on.get(i, ()), n=i + 1)
                       for i in (1, 2, 3, 4)) + notesq(6, style)
        mapcol = ('<div class="m-stickymap">'
                  '<div class="m-qh"><b>1.</b><span>Where would you like to '
                  'go?</span><em>pick as many as you like</em></div>'
                  + nationmap(selected=selected, labels=mapmode, h=330)
                  + answers(0, style, on=on.get(0, ())) + extra +
                  '<div class="m-pinned">Stays on screen while you answer the '
                  'rest</div></div>')
        return ('<div class="m-shell">'
                '<div class="m-2col" style="gap:40px;'
                'grid-template-columns:560px minmax(0,1fr)">'
                f'{mapcol}<div class="m-2l">{rest}{sofar()}</div>'
                '</div></div>')

    # board
    board = ''.join(
        f'<div class="m-bcard">{question(i, "grid", on=on.get(i, ()), n=i + 1)}'
        f'</div>' for i in (1, 2, 3, 4))
    return ('<div class="m-shell">'
            '<div class="m-2col" style="gap:32px;'
            'grid-template-columns:minmax(0,1fr) 320px">'
            '<div class="m-2l">'
            '<div class="m-qh"><b>1.</b><span>Where would you like to go?</span>'
            '<em>pick as many as you like</em></div>'
            + nationmap(selected=selected, labels=mapmode, h=330)
            + answers(0, 'grid', on=on.get(0, ()))
            + f'<div class="m-board">{board}</div>'
            + notesq(6, 'grid') + '</div>'
            + sofar() + '</div></div>')


# ------------------------------------------------- what else the page does
def liveline(n=14, band='4&ndash;6 days'):
    """Decision 34B — the page says what it already knows."""
    return ('<div class="m-live"><b>14 trips already go to Utah.</b> '
            'Three of them are 4&ndash;6 days, from $1,999. '
            '<a>See them &rsaquo;</a></div>')


def mapback():
    """Decision 34C — the map answers back with the place's own photograph."""
    return ('<div class="m-mapback">'
            f'<div class="m-mb-ph">{m.img("arches", 520, 340)}</div>'
            '<div class="m-mb-tx"><b>Utah</b>'
            '<p>Arches, Bryce Canyon, Canyonlands, Capitol Reef, Zion and '
            'Monument Valley &mdash; six of the places we guide.</p>'
            '<span class="m-mb-dots">&bull; &bull; &bull; &bull; &bull; &bull;'
            '</span></div></div>')


def draftitin():
    """Decision 34D — the thing that looks like a quote and is not one."""
    days = [('Day 1', 'Las Vegas &rarr; Zion National Park'),
            ('Day 2', 'Zion &mdash; Narrows and Angels Landing'),
            ('Day 3', 'Bryce Canyon &mdash; sunrise at Sunset Point'),
            ('Day 4', 'Capitol Reef &rarr; Moab')]
    rows = ''.join(f'<div class="m-dd"><b>{d}</b><span>{t}</span></div>'
                   for d, t in days)
    return ('<div class="m-draft"><span class="l">YOUR DRAFT ITINERARY</span>'
            f'{rows}<div class="m-dd more">+ 1 more day</div></div>')


# --------------------------------------------------- activity level on a card
def shelfcard(trip, mode='now', w=350):
    """One live card with the activity row in the four shapes of decision 35."""
    photo, style, dur, title, route, place, act, group, price = trip
    ph = round(w * 10 / 16)
    unknown = act == 'on request'
    if mode == 'now':
        row = f'<span class="s">{m.meter(act, "bars")}</span>'
        rows = [f'<span class="s">{place}</span>', row,
                f'<span class="s">{group}</span>']
    elif mode == 'drop':
        rows = [f'<span class="s">{place}</span>']
        if not unknown:
            rows.append(f'<span class="s">{m.meter(act, "bars")}</span>')
        rows.append(f'<span class="s">{group}</span>')
    elif mode == 'swap':
        rows = [f'<span class="s">{place}</span>']
        if unknown:
            rows.append('<span class="s m-swap">Departs Salt Lake City</span>')
        else:
            rows.append(f'<span class="s">{m.meter(act, "bars")}</span>')
        rows.append(f'<span class="s">{group}</span>')
    else:  # 'filled' — SWAT publishes the level
        level = 'Easy' if unknown else act
        rows = [f'<span class="s">{place}</span>',
                f'<span class="s">{m.meter(level, "bars")}</span>',
                f'<span class="s">{group}</span>']
    return (f'<div class="m-card" style="width:{w}px">'
            f'<div class="m-card-ph" style="height:{ph}px">'
            f'{m.img(photo, w * 2, ph * 2)}'
            f'<span class="m-badge">{style}</span>'
            f'<span class="m-dur">{dur}</span></div>'
            f'<div class="m-card-b"><div class="m-card-t">{title}</div>'
            f'<div class="m-card-r">{route or "&nbsp;"}</div>'
            f'<div class="m-card-s">{"".join(rows)}</div>'
            f'<div class="m-card-p"><b>{price}</b>'
            f'<span>from / person</span></div>'
            f'<div class="m-card-go"><span>View tour</span>'
            f'<span>Check dates</span></div></div></div>')


def shelfpair(mode='now'):
    """Two cards off the live November shelf: one graded, one not.

    Antelope Island says "on request" and Kanarra Falls says Moderate. Half
    the shelf is in the first state, which is the whole argument."""
    a = shelfcard(m.FEATURED[3], mode)
    b = shelfcard(m.FEATURED[7], mode)
    # A class, not an inline style: an inline `display:flex` beats every
    # `.mockwrap.phone` rule, and the pair then overflows a 390px canvas
    # sideways with no error.
    return f'<div class="m-shelfpair">{a}{b}</div>'


# ----------------------------------------------------- the tour page top
TOUR_TITLE = 'Great Salt Lake and Antelope Island'


def revbar(kind='marquee', wide=False):
    q = ('&ldquo;Placeholder review &mdash; this is where a real guest review '
         'will sit once operations has picked them out by tour.&rdquo;')
    if kind == 'chip':
        return ('<a class="m-revchip"><span class="st">&#9733;&#9733;&#9733;'
                '&#9733;&#9733;</span><b>4.9</b>'
                '<span class="n">38 reviews</span></a>')
    cls = 'm-revbar' + (' wide' if wide else '')
    return (f'<div class="{cls}"><span class="st">&#9733;&#9733;&#9733;'
            '&#9733;&#9733;</span><b>4.9</b>'
            '<span class="n">38</span>'
            f'<div class="m-revtrack"><span>{q}</span>'
            f'<span>&ldquo;Placeholder review &mdash; the rating and the count '
            f'come from the same record.&rdquo;</span></div>'
            '<span class="m-revcue">&rsaquo;</span></div>')


def tourtop(kind='now'):
    """The tour page's first screen, in the four shapes of decision 36.

    Measured: gallery 672x380, title column 395 at x=747, h1 34px/75px tall,
    price panel 184px ending 34px short of the gallery's bottom edge."""
    thumbs = ''.join(f'<span class="m-th">{m.img(k, 152, 104)}</span>'
                     for k in ['darksky', 'bonneville', 'templesq', 'antelope'])
    gal = (f'<div class="m-gal">{m.img("antelope", 1344, 760)}'
           f'<div class="m-thumbs">{thumbs}</div></div>')

    small = kind in ('under', 'wide')
    h1cls = ' sm' if small else ''
    pbcls = ' sm' if small else ''
    chip = revbar('chip') if kind == 'chip' else ''
    bar = revbar('marquee') if kind == 'under' else ''
    # The redraw: three square cards, at the two tracks they can sit in.
    rail = revrail() if kind == 'rail' else ''
    under = (f'<div class="m-revunder">{revhead()}{revcards(672)}</div>'
             if kind == 'cards' else '')

    # One grid child, not two: `.m-tourtop` is a two-column grid, so a
    # sibling here takes the title column's slot and pushes the title and the
    # price panel onto a second row.
    if under:
        gal = f'<div class="m-galcol">{gal}{under}</div>'

    right = (
        '<div class="m-tt">'
        '<div class="m-badges"><span>Day tour</span><span>1 day</span>'
        f'<span>Utah</span></div>{chip}'
        f'<h1 class="m-h1{h1cls}">{TOUR_TITLE}</h1>'
        f'<div class="m-pricebox{pbcls}"><span class="l">FROM</span>'
        '<b>$110</b><span class="s">per person, 2026</span>'
        '<span class="m-cta">Reserve a place</span></div>'
        f'{bar}{rail}</div>')

    tail = ''
    if kind == 'wide':
        tail = f'<div class="m-revwrap">{revbar("marquee", wide=True)}</div>'
    elif kind in ('band', 'bandonly'):
        tail = (f'<div class="m-revwrap">{revhead(wide=True)}'
                f'{revcards(1100)}</div>')

    top = (f'<div class="m-shell"><div class="m-tourtop">{gal}{right}</div>'
           + tail + '</div>')
    return top


# --------------------------------------------- "Is this trip right for you?"
def rfy(mode='full'):
    """The qualifying panel, in the shapes decision 37 draws."""
    body = ('<ul class="m-rfy-l">'
            '<li>Short walks on made paths and boardwalks, under a mile at a '
            'time, with the vehicle never far away.</li>'
            '<li>Causeway and lakeshore &mdash; level ground, loose gravel in '
            'places, full sun and no shade.</li>'
            '<li><b>Not suitable for a wheelchair. Call us before you book if '
            'anyone in your party uses a walker.</b></li></ul>'
            '<p class="m-rfy-f">Your guide decides what is walked on the day. '
            'Questions? <a>800-970-5864</a></p>')
    if mode == 'full':
        return ('<section class="m-rfy"><h2>Is this trip right for you?</h2>'
                f'{body}</section>')
    if mode == 'line':
        return ('<div class="m-rfyline">'
                f'{m.meter("Easy", "bars")}'
                '<span>Level ground, under a mile at a time. '
                '<b>Not suitable for a wheelchair.</b></span>'
                '<a>Is this trip right for you? &rsaquo;</a></div>')
    if mode == 'fold':
        return ('<section class="m-rfy fold"><h2>Is this trip right for you?'
                '<i>+</i></h2><p class="m-rfy-one">Level ground, under a mile '
                'at a time. Not suitable for a wheelchair.</p></section>')
    return ''


def tourcol(blocks):
    """The 691px content column with the 360px rail beside it."""
    return ('<div class="m-shell"><div class="m-2col" style="gap:48px;'
            'grid-template-columns:691px 360px">'
            f'<div class="m-2l">{"".join(blocks)}</div>'
            + m.rail(activity_row='Easy', rating=True) + '</div></div>')


def prose(title, n=3, anchor=''):
    ps = ''.join('<p class="m-p"></p>' for _ in range(n))
    return f'<section class="m-sec"><h2>{title}</h2>{ps}</section>'


# --------------------------------------------------- "Start where you are"
DOOR_Q = 'Where do you want to go?'

STATE_TILES = [
    ('arches', 'Utah'), ('arizona', 'Arizona'), ('yosemite', 'California'),
    ('colorado', 'Colorado'), ('vegas', 'Nevada'), ('teton', 'Wyoming'),
    ('oregoncoast', 'Oregon'), ('rushmore', 'South Dakota'),
    ('denali', 'Alaska'), ('glacier', 'Montana'), ('northrim', 'New Mexico'),
    ('rainier', 'Washington'), ('prismatic', 'Hawaii'), ('moab', 'Texas'),
    ('mesaverde', 'Canada'),
]

STATE_CHIPS = ['Alaska', 'Arizona', 'California', 'Canada', 'Colorado',
               'Hawaii', 'Montana', 'Nevada', 'New Mexico', 'Oregon',
               'South Dakota', 'Texas', 'Utah', 'Washington', 'Wyoming']


def starthere(mode='now'):
    """The home band, at the moment the first question is answered.

    Today the four 263x197 photographs are replaced by 15 pills in three rows
    whose right edges are 1137, 414 and 94 — and the section is left with zero
    images in it."""
    rail = ('<ol class="m-rail3">'
            '<li class="done"><i>&#10003;</i>I know the place</li>'
            '<li class="here"><i>2</i>Narrow it down</li>'
            '<li><i>3</i>See what fits</li></ol>')
    foot = ('<div class="m-shfoot"><a>&larr; Back</a>'
            '<a class="u">Or browse all 74 trips</a></div>')

    if mode == 'now':
        chips = ''.join(f'<span class="m-chip">{s}</span>'
                        for s in STATE_CHIPS)
        body = (f'<p class="m-shq">{DOOR_Q}</p>'
                f'<div class="m-chips">{chips}</div>')
    elif mode == 'keep':
        chips = ''.join(f'<span class="m-chip">{s}</span>'
                        for s in STATE_CHIPS)
        body = ('<div class="m-keep">'
                f'<div class="m-keep-ph">{m.img("door_place", 460, 360)}'
                '<span>I know the place</span></div>'
                f'<div class="m-keep-tx"><p class="m-shq">{DOOR_Q}</p>'
                f'<div class="m-chips">{chips}</div></div></div>')
    elif mode == 'tiles':
        tiles = ''.join(
            f'<div class="m-stile">{m.img(k, 380, 300)}<b>{n}</b></div>'
            for k, n in STATE_TILES)
        body = (f'<p class="m-shq">{DOOR_Q}</p>'
                f'<div class="m-stiles">{tiles}</div>')
    else:  # 'under' — all four doors stay, the answers open beneath
        doors = ''.join(
            f'<div class="m-tile{" on" if i == 0 else ""}" style="width:263px">'
            f'<div class="m-tile-ph">{m.img(p, 526, 300)}</div>'
            f'<div class="m-tile-l">{l}</div></div>'
            for i, (p, l, _) in enumerate(m.DOORS))
        chips = ''.join(f'<span class="m-chip">{s}</span>'
                        for s in STATE_CHIPS)
        body = (f'<div class="m-row" style="gap:16px">{doors}</div>'
                f'<div class="m-underq"><p class="m-shq">{DOOR_Q}</p>'
                f'<div class="m-chips">{chips}</div></div>')

    return ('<div class="m-band"><div class="m-shell">'
            + m.h2('Start where you are',
                   sub='Four ways in. Answer one and we will narrow the '
                       'catalogue for you.')
            + rail + f'<div class="m-shbody">{body}</div>{foot}'
            '</div></div>')


# ------------------------------------------ SWAT's paragraph and the film
SWAT_P = ('Our specialty is small group experiences &mdash; usually between 7 '
          'and 13 passengers. We offer a wide range of multi-day tours and day '
          'tours from <a>Las Vegas</a>, <a>Phoenix</a>, <a>Salt Lake City</a>, '
          'and other local areas adjacent to the <a>national parks</a>. From '
          'lodge &amp; hotel-based tours to camping &amp; backpacking, we can '
          'provide you with unique itineraries and opportunities throughout '
          'the American Southwest.')


def filmslot(w=520, h=293, label='Tour highlights &middot; 2:14'):
    return (f'<div class="m-film" style="width:{w}px;height:{h}px">'
            f'{m.img("grandcircle", w * 2, h * 2)}'
            f'<i class="m-play">&#9654;</i>'
            f'<span class="m-filmlab">{label}</span></div>')


def withswat(mode='now'):
    """SWAT's own paragraph, and where the highlights film goes beside it."""
    head = ('<p class="m-swath">With Southwest Adventure Tours, '
            '<em>ADVENTURE AWAITS!</em></p>')
    copy = f'{head}<p class="m-swatp">{SWAT_P}</p>'
    if mode == 'now':
        inner = f'<div class="m-swatone">{copy}</div>'
    elif mode == 'right':
        inner = (f'<div class="m-swat2"><div>{copy}</div>'
                 f'<div>{filmslot()}</div></div>')
    elif mode == 'left':
        inner = (f'<div class="m-swat2 flip"><div>{filmslot()}</div>'
                 f'<div>{copy}</div></div>')
    else:  # 'band'
        return ('<div class="m-swatband">'
                f'{m.img("grandcircle", 2400, 760)}'
                f'<div class="m-swatband-tx">{head}'
                '<p class="m-swatp">Our specialty is small group experiences '
                '&mdash; usually between 7 and 13 passengers.</p>'
                '<i class="m-play big">&#9654;</i></div></div>')
    return f'<div class="m-shell" style="padding-top:34px">{inner}</div>'

# ---------------------------------------------- decision 36, redrawn
#: Three of them, and the text has to be readable at the size it renders —
#: the whole point of the redraw is that a clause crawling past in a 52px bar
#: is not a review anybody reads.
REVIEWS = [
    ('&ldquo;Placeholder review &mdash; this is where a real guest review will '
     'sit once operations has picked them out by tour. It is long enough to '
     'show what a real one looks like in this box.&rdquo;', 'Example', 'Sample data'),
    ('&ldquo;Placeholder review &mdash; three render at a time and the set '
     'changes every eight seconds, so a trip with nine reviews shows all nine '
     'without anybody scrolling.&rdquo;', 'Example', 'Sample data'),
    ('&ldquo;Placeholder review &mdash; the rating and the count above come '
     'from the same record, so they can never disagree with the cards under '
     'them.&rdquo;', 'Example', 'Sample data'),
]


def revhead(wide=False):
    """The score and the count — the part Crow said already works."""
    cls = 'm-revhead' + (' wide' if wide else '')
    return (f'<div class="{cls}"><b>What guests said</b>'
            '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            '<span class="sc">4.9</span>'
            '<span class="n">from 38 reviews</span></div>')


def revcards(w=672, n=3, dots=True):
    """Three square cards, side by side, rotating.

    `w` is the track they sit in — 672 under the gallery, 1,100 across both
    columns — because the argument is whether a card is wide enough to read a
    sentence in, and that is decided by the track.
    """
    gap = 16
    card = (w - gap * (n - 1)) // n
    cards = ''
    for i in range(n):
        q, who, when = REVIEWS[i % len(REVIEWS)]
        cards += (f'<div class="m-revcard" style="width:{card}px;height:{card}px">'
                  '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
                  f'<p>{q}</p><span class="who">{who} &middot; {when}</span>'
                  '</div>')
    d = ''
    if dots:
        d = ('<div class="m-revdots"><i class="on"></i><i></i><i></i>'
             '<span>rotates every 8 seconds &middot; pauses on hover</span></div>')
    return f'<div class="m-revcards" style="width:{w}px">{cards}{d}</div>'


def revrail():
    """One card at a time, in the 395px column beside the price."""
    q, who, when = REVIEWS[0]
    return ('<div class="m-revrail">'
            '<span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            f'<p>{q}</p><span class="who">{who} &middot; {when}</span>'
            '<div class="m-revdots one"><i class="on"></i><i></i><i></i></div>'
            '</div>')

