"""Round thirteen, decisions 80-81: how long a tour page is on a phone.

Crow, 29 September, after the phone QA pass measured every tour page at
390x844: "Can you show me this on a design sheet so I can see what it would
look like". The proposal it answers is in the phone-QA note: a typical tour
page is about 21 phone screens and a third of that is Day by day.

These drawings are NOT markup. Each panel is the live production page at
390x844, with the option applied to the real page in the browser and then
photographed (r13/harvest/proto.js + shoot.mjs). The page length question is
a question about SWAT's real words and photos, so the real page is the only
honest drawing of it. Every panel is the same three phone screens tall,
starting at the same heading, so how far down the page each one gets IS the
comparison.
"""

import glob
import json
import os
import statistics

import mocks as m
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New', '29 Sep')
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'r13', 'data')
SLUG = 'arizona-adventure'
VH = 844
WIN = VH * 3

AZ = json.load(open(os.path.join(DATA, SLUG + '.json')))


def win(kind, v, rings):
    """A three-screen window of the real page, with a hotspot for each ring.

    The hotspots are the measured boxes of real elements on the prototyped
    page, so a ring is drawn round what the page actually rendered."""
    boxes = AZ[v]['win'][kind]
    hs = ''
    for n, (key, _) in enumerate(rings, 1):
        b = boxes[key]
        top = b['y']
        h = min(b['h'], WIN - top - 6)
        hs += (f'<span class="r13-hs" id="r13-{kind}-{v}-{n}" style="left:{b["x"]}px;'
               f'top:{top}px;width:{min(b["w"], 350)}px;height:{h}px"></span>')
    lines = ''.join(f'<span class="r13-fold" style="top:{VH * k}px"><b>{k} screen'
                    f'{"s" if k > 1 else ""} of scrolling</b></span>' for k in (1, 2))
    html = (f'<div class="r13-win"><img src="img/r13/{SLUG}-{kind}-{v}.jpg" alt="">'
            f'{hs}{lines}</div>')
    r = ''.join(m.ring(n, f'#r13-{kind}-{v}-{n}') for n, _ in enumerate(rings, 1))
    return m.mock(html + r, WIN, aw=390)


def screens(px):
    return px / VH


def fmt(px):
    s = screens(px)
    return f'{s:.0f}' if abs(s - round(s)) < 0.25 else f'{s:.1f}'


# ------------------------------------------------------------ the numbers
def combo(d, days, lower):
    """Page height with one days option and one lower-page option. The two
    touch separate parts of the page, so their savings add."""
    now = d['now']['H']
    return now - (now - d[days]['H']) - (now - d[lower]['H'])


COMBOS = [
    ('As it ships', 'now', 'now', ''),
    ('80 B only', 'fold', 'now', ''),
    ('80 C only', 'short', 'now', ''),
    ('80 B + 81 B', 'fold', 'lists', ''),
    ('80 B + 81 C', 'fold', 'photos', 'rec'),
]


def sweep():
    rows = []
    for f in sorted(glob.glob(os.path.join(DATA, 'sweep', '*.json'))):
        d = json.load(open(f))
        if all(d.get(v, {}).get('H') for v in ('now', 'fold', 'short', 'lists', 'photos')):
            rows.append(d)
    return rows


SWEEP = sweep()


def median(days, lower):
    return statistics.median(combo(d, days, lower) for d in SWEEP)


def worst(days, lower):
    return max(combo(d, days, lower) for d in SWEEP)


def count_over(days, lower, n):
    return sum(1 for d in SWEEP if screens(combo(d, days, lower)) >= n)


R66 = next((d for d in SWEEP if d['slug'] == 'route-66-eastbound'), None)


def segs(days, lower):
    """Arizona Adventure cut into the parts of the page, for the bar chart."""
    a, b = AZ[days], AZ[lower]
    y = lambda d, k: d['boxes'][k]['y']
    top = a['itY']
    day = y(a, 'rfy') - a['itY']
    det = y(b, 'gallery') - y(b, 'rfy')
    pho = y(b, 'dep') - y(b, 'gallery')
    book = (y(b, 'protection') + b['boxes']['protection']['h']) - y(b, 'dep')
    rest = combo(AZ, days, lower) - top - day - det - pho - book
    return [('top', top), ('days', day), ('det', det), ('pho', pho), ('book', book),
            ('bot', rest)]


SEG_NAMES = [('top', 'Photo, price, reviews, overview, seasons'), ('days', 'Day by day'),
             ('det', 'Right for you + tour details'), ('pho', 'The two photo sections'),
             ('book', 'Dates, prices, trip protection'), ('bot', 'Similar tours, map, footer')]


def chart():
    full = AZ['now']['H']
    rows = ''
    for label, dv, lv, cls in COMBOS:
        h = combo(AZ, dv, lv)
        bar = ''.join(f'<i class="s-{k}" style="width:{100 * px / full:.2f}%"></i>'
                      for k, px in segs(dv, lv))
        rows += (f'<div class="r13-row {cls}"><span class="r13-lab">{label}</span>'
                 f'<span class="r13-bar" style="--sc:{100 * VH / full:.3f}%">{bar}</span>'
                 f'<span class="r13-n">{fmt(h)} screens</span></div>')
    key = ''.join(f'<span><i class="s-{k}"></i>{n}</span>' for k, n in SEG_NAMES)

    table = ''
    if SWEEP:
        tr = ''
        for label, dv, lv, cls in COMBOS:
            r66 = fmt(combo(R66, dv, lv)) if R66 else '&ndash;'
            tr += (f'<tr class="{cls}"><td>{label}</td><td>{fmt(median(dv, lv))}</td>'
                   f'<td>{count_over(dv, lv, 25)}</td><td>{fmt(worst(dv, lv))}</td>'
                   f'<td>{r66}</td></tr>')
        table = (f'<table class="tbl r13-tbl"><tr><th>Choice</th><th>A typical tour</th>'
                 f'<th>Tours 25+ screens long</th><th>The longest tour</th>'
                 f'<th>Route 66 Eastbound</th></tr>{tr}</table>'
                 f'<p class="r13-note">All {len(SWEEP)} live tour pages, each measured on a '
                 f'phone with every option applied to the real page. &ldquo;A typical '
                 f'tour&rdquo; is the middle one.</p>')
    return (f'<div class="r13-chart"><div class="r13-ct">How long the whole page is, '
            f'Arizona Adventure, one tick per phone screen</div>{rows}'
            f'<div class="r13-key">{key}</div>{table}</div>')


# ------------------------------------------------------------ decision 80
az_now, az_fold, az_short = AZ['now'], AZ['fold'], AZ['short']
it_now = az_now['boxes']['rfy']['y'] - az_now['itY']
it_fold = az_fold['boxes']['rfy']['y'] - az_fold['itY']
it_short = az_short['boxes']['rfy']['y'] - az_short['itY']

ALL.append(dec(
    80, 'On a phone, the days take a third of every tour page',
    [('74 tour pages, phone only', ''), ('Crow', 'who'), ('&frac12; day', ''),
     (f'Day by day: {fmt(it_now)} screens here', 'big')],
    [quote(['Can you show me this on a design sheet so I can see what it would look like'],
           'Crow, 29 September, on the phone check of every tour page')],
    [
        opt('As it ships',
            ['A strip of <b>the whole trip at a glance</b>, then every day open.',
             'Each day is a <b>full-width photo slideshow</b> first.',
             'Then <b>every word SWAT wrote for that day</b>, open. Day 2 alone is more than a '
             'screen.'],
            f'<p>Arizona Adventure, eight days. Day by day runs <b>{fmt(it_now)} phone '
            f'screens</b> on its own, before you reach &ldquo;Is this trip right for '
            f'you?&rdquo;. Three screens in, you are still on day 3.</p>',
            cls='now',
            mockup=win('days', 'now', [('glance', 0), ('fig1', 0), ('day2', 0)])),

        opt('Fold the days',
            ['Each day becomes <b>one row</b>: its own photo, the day, where you sleep, the '
             'title. Tap it and it opens, exactly as it is today.',
             'All eight days fit on <b>one screen</b>, so the rows are the trip at a glance '
             'and the separate strip goes.',
             'You reach <b>&ldquo;Is this trip right for you?&rdquo;</b> in about a screen '
             'and a half instead of ten.'],
            f'<p>Day by day goes from {fmt(it_now)} screens to <b>{fmt(it_fold)}</b>. Nothing '
            f'is deleted: every word and photo is one tap away, and Google still reads all of '
            f'it. Phones only &mdash; a laptop keeps the days open.</p>',
            cost='&frac12; day for all 74 tours',
            risk='Someone who wants to read the whole itinerary taps eight times. An '
                 '&ldquo;Open every day&rdquo; link above the rows fixes that.',
            cls='rec',
            mockup=win('days', 'fold', [('row1', 0), ('rowLast', 0), ('rfy', 0)])),

        opt('Shorter days, still open',
            ['The slideshow becomes <b>a small photo beside the title</b>.',
             'Each day shows its <b>first four lines</b>, fading out.',
             '<b>&ldquo;Read all of Day 1&rdquo;</b> opens the rest.'],
            f'<p>Keeps every day visible while you scroll. Day by day goes from {fmt(it_now)} '
            f'screens to <b>{fmt(it_short)}</b>, so it saves about two thirds of what B '
            f'saves. On a twelve-day trip that is still four screens of days.</p>',
            cost='&frac12; day for all 74 tours',
            risk='Four lines cut most days off mid-sentence, and the big photos '
                 'become thumbnails.',
            mockup=win('days', 'short', [('top1', 0), ('clamp1', 0), ('more1', 0)])),
    ],
    verdict([
        '<b>B.</b> The days are the longest thing on every tour page, and on a phone '
        'nobody reads eight days back to back. They look for the one day they are curious '
        'about. Folded rows show the whole trip on one screen, with a photo on every row, '
        'and the part of the page that sells the trip (who it is for, what is included, '
        'the dates, the price) moves up by eight screens here.',
        f'Across all {len(SWEEP)} tour pages, a typical one goes from '
        f'<b>{fmt(median("now", "now"))} phone screens to {fmt(median("fold", "now"))}</b>, and '
        f'the {count_over("now", "now", 25)} tours that run past 25 screens today all come in '
        f'under it. Route 66 Eastbound, the longest, goes from {fmt(combo(R66, "now", "now"))} '
        f'to {fmt(combo(R66, "fold", "now"))}.',
        'C is the one to pick if you would rather every day stay visible as people scroll, '
        'but it only gets two thirds of the way, and it chops SWAT&rsquo;s writing off '
        'mid-sentence.',
    ]),
    since=NEW, cols=3))


# ------------------------------------------------------------ decision 81
az_lists, az_photos = AZ['lists'], AZ['photos']
lower = lambda d: (d['boxes']['protection']['y'] + d['boxes']['protection']['h']) - d['boxes']['details']['y']

ALL.append(dec(
    81, 'Below the days: the lists and the photo sections',
    [('74 tour pages, phone only', ''), ('Crow', 'who'), ('&frac12; day', ''),
     (f'Details to protection: {fmt(lower(az_now))} screens', 'big')],
    [],
    [
        opt('As it ships',
            ['<b>&ldquo;In the price&rdquo;</b> lists all 13 things, then &ldquo;Not in the '
             'price&rdquo; lists all 7, both open.',
             'Two photo sections back to back, <b>Gallery</b> and <b>More from Grand '
             'Canyon</b>, each a grid of big and small photos.'],
            f'<p>From Tour details down to the end of Trip protection is <b>{fmt(lower(az_now))} '
            f'phone screens</b>. Three screens in, you are still in the first photo grid. '
            f'Trip protection has its own five boxes of questions and answers further down.</p>',
            cls='now',
            mockup=win('lower', 'now', [('inPrice', 0), ('gal1', 0)])),

        opt('Shorter lists',
            ['<b>&ldquo;In the price&rdquo;</b> shows the first five, then <b>&ldquo;Show '
             'all 13 things included&rdquo;</b>.',
             '<b>&ldquo;Not in the price&rdquo;</b> is one row. Tap to open.',
             '<b>Arrival and departure, physical requirements and park permits</b> are one '
             'row each. Trip protection keeps its opening paragraph and folds its five '
             'questions into one row.'],
            f'<p>Tour details to protection goes from {fmt(lower(az_now))} screens to '
            f'<b>{fmt(lower(az_lists))}</b>. The photos stay exactly as they are.</p>',
            cost='&frac12; day',
            risk='&ldquo;Physical requirements&rdquo; is folded, but &ldquo;Is this trip '
                 'right for you?&rdquo; just above it still says how hard the trip is.',
            mockup=win('lower', 'lists', [('detMore', 0), ('notPrice', 0), ('lines', 0)])),

        opt('B, plus photo rows',
            ['Everything in B.',
             '<b>Gallery</b> becomes one row of big photos you swipe sideways.',
             '<b>More from Grand Canyon</b> does the same.'],
            f'<p>Tour details to protection goes to <b>{fmt(lower(az_photos))} '
            f'screens</b>. Every photo is still there at the same size as the small ones '
            f'today; you swipe for them instead of scrolling past them.</p>',
            cost='&frac12; day, plus an hour for the photo rows',
            risk='A swipe row hides most of its photos until you swipe. The first one and '
                 'the edge of the next are what you see.',
            cls='rec',
            mockup=win('lower', 'photos', [('lines', 0), ('gal1', 0), ('mp1', 0)])),
    ],
    verdict([
        '<b>C.</b> The two photo grids are the same idea twice in a row, a screen and a '
        'half of it, right before the dates and prices. One swipe row each keeps every '
        'photo and puts the dates a screen and a half closer. If you would rather keep '
        'the photo grids as they are, B is the safe half of this.',
        '<b>Together, 80 B and 81 C take Arizona Adventure from '
        f'{fmt(AZ["now"]["H"])} phone screens to {fmt(combo(AZ, "fold", "photos"))}.</b> '
        'The chart below shows every combination, and the table under it every tour.',
    ]) + chart(),
    since=NEW, cols=3))
