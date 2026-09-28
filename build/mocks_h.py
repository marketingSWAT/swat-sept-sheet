"""Mockup primitives for round seven: Lance's two notes, decisions 52 and 53.

Lance Card, 28 September, by email to Jason, Crow and Matt:

  1. "Do we need to separate the Day Tours from our other multi-day tours in
     the Available to Book Now section? ... SLC Day Tours can be a 12-24-hour
     ramp and shouldn't be restricted to the 2-month-out booking window."
  2. "I just realized that our CTA is a little muddy. What is our CTA for the
     homepage?"

Measured off the **deployed production build** at **1440x900** on
28 September 2026, `swat-website-storefront.vercel.app/` (gate 6666):

  Chrome     strip 36px, header 73px at y=36, deals ticker 48px; hero at y=159.
  Hero       1,425x558 (y=159-717). Eyebrow "74 guided tours · 10 departure
             cities", h1 "Welcome To Southwest Adventure Tours" 710x113 at
             y=303, then a 575x124 paragraph about being "a Destination
             Management Company and Tour Operator". No button.
  Search     a 1,321x86 white bar at y=653, straddling the photo's bottom
             edge; its orange "Search 74 tours" button is 171x64 at x=1191.
             It IS on screen at 1440x900 and at 1440x760. In Lance's
             screenshot Gmail's download icons sit on top of it.
  Chips      "Popular:" + five 44px pills at y=755.
  Floating   "Tour Questions?" 193x56 at y=748 and an orange "Search trips"
             pill 162x56 at y=820, both over the page at rest.
  Count      **30** clickable things on the first screen. **Three** orange
             buttons with three different labels (Find a Trip, Search 74
             tours, Search trips) and all three open the same tour finder.

  Shelf      "Bookable now in November", section at y=1,121, 1,908px tall.
             Grid 3 x 424px, cards 561px. Line under the heading: "2 trips
             leave in November, soonest first, then the rest of the
             catalogue." Eight cards: the two Mighty 5 trips (dated), then
             Great Salt Lake, Bonneville, Dark Sky, Park City, Kanarra Falls
             and a $250 AmaWaterways Christmas-markets cruise, which are
             catalogue filler in price order with no November date at all.

Two facts from the data, read the same day, that the drawings rest on:

  - The window is "60 days out to the end of that month". On 28 September
    that is **27-30 November, four days**, which is why only two trips
    qualify. 60-120 days out holds **seven** dated multi-day trips.
  - **None of the 15 published day tours has a single dated departure** in
    the calendar, and none has a Softrip booking page (their codes GSLDT,
    BSF, SLCDSE, PCOHE, ARCHESDT are on the missing list). Every day-tour
    page says "Ask about dates" or "Request a quote". The 60-day rule is not
    what keeps them off the shelf: they have no date for any rule to read.
"""

import mocks as m

WINDOW = 900

m.PHOTOS.update({
    'maui': 'Rock_Beach_Hawaii_a3b12e76-897e-4ad6-ad29-9d912182a20b.jpg',
    'gems': 'Gems_Christmas_Brasov_2880x945_29cb1c55-5b4e-451e-9eba-85c34c9e447c.jpg',
})

GROUP = 'Small group, 7&ndash;13'
DAYG = 'Small group, up to 14'

#: Card tuples in `m.tripcard` order:
#: photo, badge, duration, title, route, places, activity, group, price.
M5SLC = ('m5slc', 'Small group', '8 days', 'Mighty 5 Utah From Salt Lake City',
         'Salt Lake City &rarr; Zion National Park',
         'Zion National Park, Bryce Canyon National Park, Arches National Park',
         'Strenuous', GROUP, '$3,499')
M5LV = ('zion', 'Small group', '5 days', 'Mighty 5 Utah Tour From Las Vegas',
        'Las Vegas &rarr; Zion National Park',
        'Zion National Park, Bryce Canyon National Park, Arches National Park',
        'Easy', GROUP, '$1,999')
ANTELOPE = ('antelope', 'Day tour', '1 day', 'Great Salt Lake and Antelope Island',
            None, 'Utah', 'on request', DAYG, '$110')
BONNEVILLE = ('bonneville', 'Day tour', 'Half day', 'Bonneville Salt Flats Adventure',
              None, 'Multiple parks', 'on request', DAYG, '$110')
DARKSKY = ('darksky', 'Day tour', 'Duration on request',
           'Salt Lake Antelope Island Dark Sky Experience', None,
           'Multiple parks', 'on request', DAYG, '$110')
PARKCITY = ('parkcity', 'Winter', '1 day', 'Park City &amp; Olympic Heritage Excursion',
            'Salt Lake City &rarr; Utah', 'Utah', 'on request', GROUP, '$129')
KANARRA = ('kanarra', 'Day tour', 'Half day', 'Kanarra Falls',
           'St George &rarr; Zion National Park', 'Zion National Park, Utah',
           'Moderate', DAYG, '$225')
GEMS = ('gems', 'Rail &amp; cruise', '12 days',
        'AMA Waterways: Gems of Southeast Europe Christmas Markets', None,
        'International', 'Easy', GROUP, '$250')

#: The seven multi-day trips with a departure 60-120 days out, soonest first
#: (29 Nov - 24 Jan). Six are drawn: two clean rows of three.
AURORA = ('auroras', 'Small group', '6 days',
          'Alaska&rsquo;s Northern Lights Adventure Tour', None,
          'Denali National Park', 'Easy', GROUP, '$3,429')
SNOWMO = ('snowmobile', 'Winter', '6 days',
          'Jackson Hole &amp; Yellowstone Snowmobile Adventure', None,
          'Yellowstone National Park', 'on request', GROUP, '$2,899')
MAUI = ('maui', 'Small group', '10 days', 'Hawai&rsquo;i Maui Big Island Explorer',
        None, 'Hawaii', 'Easy', GROUP, '$7,999')
YSWIN = ('ystwinter', 'Winter', '7 days', 'Yellowstone &amp; Grand Teton Winter Adventure',
         'Salt Lake City &rarr; Yellowstone National Park',
         'Yellowstone National Park, Grand Teton National Park',
         'on request', GROUP, '$3,119')

NOW8 = [M5SLC, M5LV, ANTELOPE, BONNEVILLE, DARKSKY, PARKCITY, KANARRA, GEMS]
DATED6 = [M5SLC, M5LV, AURORA, SNOWMO, MAUI, YSWIN]
#: The day tours already on today's shelf, so nothing new is claimed about them.
DAY4 = [ANTELOPE, BONNEVILLE, DARKSKY, PARKCITY]

CARD_W = 424
GAP = 24


# ------------------------------------------------------------ decision 52

def _grid(trips, cls=''):
    cards = ''.join(f'<div class="l-cell">{m.tripcard(t, w=CARD_W)}</div>'
                    for t in trips)
    return f'<div class="l-grid {cls}">{cards}</div>'


def _head(title, line, more='See every trip &rarr;'):
    return (f'<div class="l-h2row"><div class="m-h2 l-h2">{title}</div>'
            f'<span class="m-more">{more}</span></div>'
            f'<p class="l-line">{line}</p>')


def daycard(t):
    """A day tour, drawn smaller: four across, no spec rows, and the one
    line a day tour actually needs, which is how soon it can go."""
    photo, badge, dur, title, route, place, act, group, price = t
    return ('<div class="l-dcard">'
            f'<div class="l-dph">{m.img(photo, 630, 394)}'
            f'<span class="m-badge">{badge}</span><span class="m-dur">{dur}</span></div>'
            f'<div class="l-db"><b>{title}</b>'
            f'<span>From Salt Lake City &middot; <em>{price}</em> per person</span>'
            '<i>Short notice is fine &middot; ask about tomorrow &rarr;</i>'
            '</div></div>')


def shelf_now():
    return ('<div class="l-sec">'
            + _head('Bookable now in November',
                    '2 trips leave in November, soonest first, then the rest of '
                    'the catalogue.')
            + _grid(NOW8) + '</div>')


def shelf_rows():
    """B: the multi-day row on a window that holds real dates, and a row of
    its own for day tours under it."""
    days = ''.join(daycard(t) for t in DAY4)
    return ('<div class="l-sec">'
            + _head('Bookable now, leaving late November into January',
                    'Seven trips leave between November 29 and January 24, '
                    'soonest first. Real dates, real prices.')
            + _grid(DATED6, 'l-dated')
            + '<div class="l-dayrow">'
            + _head('Day tours from Salt Lake City',
                    'Half-day and one-day trips that can leave at short notice.',
                    'All 15 day tours &rarr;')
            + f'<div class="l-dgrid">{days}</div></div></div>')


def shelf_tabs():
    """C: one shelf, two tabs over it."""
    return ('<div class="l-sec">'
            + _head('Bookable now',
                    'Seven multi-day trips leave between November 29 and '
                    'January 24, soonest first.')
            + '<div class="l-tabs"><span class="on">Multi-day trips '
              '<em>7</em></span><span>Day tours <em>15</em></span></div>'
            + _grid(DATED6, 'l-dated') + '</div>')


def shelf_strip():
    """D: multi-day only, and one shallow strip that sends day-trippers to
    the day-tour page."""
    thumbs = ''.join(f'<span class="l-sth">{m.img(t[0], 240, 160)}</span>'
                     for t in DAY4)
    return ('<div class="l-sec">'
            + _head('Bookable now, leaving late November into January',
                    'Seven trips leave between November 29 and January 24, '
                    'soonest first. Real dates, real prices.')
            + _grid(DATED6, 'l-dated')
            + '<div class="l-strip">'
            f'<div class="l-sthumbs">{thumbs}</div>'
            '<div class="l-stx"><b>In Salt Lake City for a day?</b>'
            '<span>15 half-day and one-day tours, most of them at short '
            'notice.</span></div>'
            '<span class="m-btn">See the day tours</span></div></div>')


# ------------------------------------------------------------ decision 53

EYEBROW = '74 guided tours &middot; 10 departure cities'
H1_NOW = 'Welcome To Southwest Adventure Tours'
P_NOW = ('As a Destination Management Company and Tour Operator, we provide '
         'tours for individuals and groups through the Great American '
         'Southwest. We focus on conducting sightseeing, photography, and '
         'adventure tours.')
#: Draft wording, ours, for SWAT to approve or replace. Facts only from the
#: site itself: the 7-13 group size is on the strip above the header.
H1_NEW = 'Small-group tours of America&rsquo;s national parks'
P_NEW = ('Guided trips of 7 to 13 people, leaving from Las Vegas, Phoenix, '
         'Salt Lake City and seven more cities.')

LIVE_DEALS = [
    ('Black Hills of South Dakota', 'September 28', '$400 off per person', 'BLACK400'),
    ('Canyons of the Escalante', 'October 25', '$500 off per person', 'CANYONS500'),
    ('Black Hills of South Dakota', 'September 28', '$400 off per person', 'BLACK400'),
]


def chrome(cta='Find a Trip'):
    items = ''.join(f'<span>{t}</span>' for t in m.NAV)
    deals = ''.join(
        f'<span>&#128293; <b>{t}</b> {d} <em>{o}</em> <code>{c}</code></span>'
        for t, d, o, c in LIVE_DEALS)
    return ('<div class="v-chrome">' + m.promostrip()
            + '<div class="m-hd"><div class="m-shell">'
            f'<img class="m-logo" src="{m.WORDMARK}" alt="">'
            f'<div class="m-nav">{items}</div>'
            f'<div class="m-phone">{m.PHONE}</div>'
            f'<div class="m-hd-cta l-hdcta">{cta}</div></div></div>'
            '<div class="l-tick"><span class="k">HOT DEALS</span>'
            f'<div class="l-ttrack">{deals}</div><span class="all">SEE ALL</span></div>'
            '</div>')


def search(btn='Search 74 tours', cls=''):
    f = [('WHERE', 'Anywhere in the Southwest'), ('LEAVING FROM', 'Any departure city'),
         ('HOW LONG', 'Any length')]
    cells = ''.join(f'<div class="l-sf"><small>{a}</small><b>{b}</b><i>&#8964;</i></div>'
                    for a, b in f)
    return (f'<div class="l-search {cls}">{cells}'
            f'<span class="l-sgo">{btn}</span></div>')


def chips(cls=''):
    cs = ''.join(f'<span>{c}</span>' for c in
                 ['Day tours', 'Easy pace', 'Backpacking', 'Private &amp; custom',
                  'Current deals'])
    return f'<div class="l-chips {cls}"><em>Popular:</em>{cs}</div>'


def floats(pill='Search trips', show_pill=True):
    p = (f'<span class="l-pill">&#9906; {pill}</span>' if show_pill else '')
    return f'<span class="l-chat">&#128488; Tour Questions?</span>{p}'


def mapband():
    return ('<div class="l-mapband"><div class="l-mapin">'
            '<b>We&rsquo;re nationwide, not just the Southwest</b></div></div>')


def fold():
    return (f'<div class="m-fold" style="top:{WINDOW}px">'
            '<span>bottom of a 1440&times;900 window</span></div>')


def hero(kind='now'):
    """The first screen, in the four shapes decision 53 draws.

    The photograph keeps its height in every option: Crow kept the big hero
    when Lance asked for a shorter one, and none of these reopens that.
    """
    img = m.img('hero', 2400, 930)
    if kind == 'now':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NOW}</h1>'
              f'<p class="l-p">{P_NOW}</p>')
        return (f'<div class="l-hero">{img}<div class="l-tint"></div>'
                f'<div class="l-htx">{tx}</div>'
                f'<div class="l-sbar">{search()}</div></div>{chips()}')
    if kind == 'button':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              f'<p class="l-p">{P_NEW}</p>'
              '<div class="l-ctas"><span class="l-big">Find your tour</span>'
              f'<span class="l-call">or call {m.PHONE}</span></div>')
        return (f'<div class="l-hero">{img}<div class="l-tint"></div>'
                f'<div class="l-htx">{tx}</div>'
                f'<div class="l-sbar">{search()}</div></div>{chips()}')
    if kind == 'search':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              f'<p class="l-p">{P_NEW}</p>'
              + search('Find your tour', 'up')
              + chips('onphoto')
              + f'<span class="l-call">Rather talk it through? Call {m.PHONE}</span>')
        return (f'<div class="l-hero">{img}<div class="l-tint"></div>'
                f'<div class="l-htx wide">{tx}</div></div>')
    if kind == 'two':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              f'<p class="l-p">{P_NEW}</p>'
              '<div class="l-ctas"><span class="l-big">Find your tour</span>'
              '<span class="l-big ghost">Build your own trip</span></div>')
        return (f'<div class="l-hero">{img}<div class="l-tint"></div>'
                f'<div class="l-htx">{tx}</div>'
                f'<div class="l-sbar">{search()}</div></div>{chips()}')
    raise ValueError(kind)


def screen(kind='now'):
    cta = 'Find a Trip' if kind in ('now', 'button', 'two') else 'Find your tour'
    pill = kind != 'search'
    return ('<div class="l-screen">' + chrome(cta) + hero(kind) + mapband()
            + floats(show_pill=pill) + fold() + '</div>')


# ------------------------------------------------- decision 53, round two
#
# Crow, 28 September: "53 I still dont like, so mock some more ideas and
# designs for this." B, C and D were all the same picture with different
# words on it: a dark wash, a white headline top-left, and something orange
# under it. So the four below change the SHAPE of the first screen, not the
# copy on it, and each one is a different answer to "what do we ask a
# visitor to do first":
#
#   E  point at a place        (photographs are the call to action)
#   F  answer three questions  (the photo moves right, the form gets a panel)
#   G  pick a real departure   (the next three trips with seats, on the photo)
#   H  type anything           (one box, centred, nothing else orange)
#
# Counts read off production /find/ on 28 September at 1440x900:
# Utah 28, Arizona 12, California 11, Wyoming 8, Alaska 2, day tours 12,
# 74 in the catalogue. Departures read off the tour pages the same day, first
# date on or after the two-month floor (27 November): Mighty 5 from Salt Lake
# City 29 Nov, Mighty 5 from Las Vegas 30 Nov, Alaska's Northern Lights 14 Dec.

H1_PLACE = 'Where do you want to go?'
P_PLACE = ('74 small-group tours from 10 cities. Pick a place and we will show '
           'you every trip that goes there.')

PLACES = [
    ('arches', 'Utah', 28),
    ('arizona', 'Arizona', 12),
    ('yosemite', 'California', 11),
    ('prismatic', 'Wyoming &amp; Yellowstone', 8),
    ('auroras', 'Alaska', 2),
    ('antelope', 'Day tours from Salt Lake City', 12),
]

SOON = [
    ('m5slc', 'Mighty 5 Utah From Salt Lake City', 'Sun 29 Nov', '8 days', '$3,499'),
    ('zion', 'Mighty 5 Utah Tour From Las Vegas', 'Mon 30 Nov', '5 days', '$1,999'),
    ('auroras', 'Alaska&rsquo;s Northern Lights Adventure Tour', 'Mon 14 Dec',
     '6 days', '$3,429'),
]


def _placetiles():
    ts = ''.join(
        f'<div class="q-pt">{m.img(p, 360, 300)}<div class="q-ptx"><b>{n}</b>'
        f'<span>{c} trip{"s" if c != 1 else ""}</span></div></div>'
        for p, n, c in PLACES)
    return (f'<div class="q-places">{ts}'
            '<div class="q-pt all"><b>All 74 tours</b><span>Find your tour '
            '&rarr;</span></div></div>')


def _stack():
    """The three questions of today's search bar, stacked in a panel."""
    f = [('WHERE', 'Anywhere in the Southwest'), ('LEAVING FROM', 'Any departure city'),
         ('HOW LONG', 'Any length')]
    cells = ''.join(f'<div class="q-sf"><small>{a}</small><b>{b}</b><i>&#8964;</i></div>'
                    for a, b in f)
    return (f'<div class="q-stack">{cells}'
            '<span class="q-go">Find your tour</span></div>')


def _soon():
    rows = ''.join(
        f'<div class="q-srow">{m.img(p, 160, 120)}<div><b>{t}</b>'
        f'<span>{d} &middot; {n} &middot; from {pr}</span></div><i>&rarr;</i></div>'
        for p, t, d, n, pr in SOON)
    return ('<div class="q-soon"><div class="q-sh">Next departures with seats'
            '</div>' + rows + '<div class="q-sall">Every date, every trip &rarr;</div></div>')


def hero2(kind):
    img = m.img('hero', 2400, 930)
    if kind == 'places':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_PLACE}</h1>'
              f'<p class="l-p">{P_PLACE}</p>')
        return (f'<div class="l-hero q-tall">{img}<div class="l-tint q-down"></div>'
                f'<div class="l-htx q-top">{tx}</div>{_placetiles()}</div>')
    if kind == 'split':
        tx = (f'<span class="q-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              f'<p>{P_NEW}</p>{_stack()}'
              f'<span class="q-call">Rather talk it through? Call {m.PHONE}</span>')
        return (f'<div class="l-hero q-split"><div class="q-pan">{tx}</div>'
                f'<div class="q-ph">{m.img("hero", 1800, 1116)}</div></div>')
    if kind == 'soon':
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              f'<p class="l-p">{P_NEW}</p>'
              '<div class="l-ctas"><span class="l-big">Find your tour</span>'
              f'<span class="l-call">or call {m.PHONE}</span></div>')
        return (f'<div class="l-hero">{img}<div class="l-tint"></div>'
                f'<div class="l-htx q-narrow">{tx}</div>{_soon()}</div>')
    if kind == 'onebox':
        pops = ' &middot; '.join(['Zion', 'Grand Canyon', 'Yellowstone',
                                  'Leaving from Las Vegas', 'Day tours'])
        tx = (f'<span class="l-eye">{EYEBROW}</span><h1>{H1_NEW}</h1>'
              '<div class="q-box"><span class="q-in">&#9906;&ensp;Try Zion, '
              'Yellowstone, Las Vegas or &ldquo;3 days&rdquo;</span>'
              '<span class="q-go">Find your tour</span></div>'
              f'<div class="q-pop">Popular: {pops}</div>'
              f'<div class="q-pop dim">Rather talk it through? Call {m.PHONE}</div>')
        return (f'<div class="l-hero">{img}<div class="l-tint q-even"></div>'
                f'<div class="q-mid">{tx}</div></div>')
    raise ValueError(kind)


def screen2(kind):
    """The first screen for E-H. None of them keeps the floating
    'Search trips' pill at rest; it comes back once the page has scrolled
    past the hero, so it is not drawn here."""
    head = chrome('Find your tour')
    if kind == 'onebox':
        head = head.replace('m-hd-cta l-hdcta', 'm-hd-cta l-hdcta q-quiet')
    return ('<div class="l-screen">' + head + hero2(kind) + mapband()
            + floats(show_pill=False) + fold() + '</div>')
