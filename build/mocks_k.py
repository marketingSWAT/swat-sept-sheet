"""Mockup primitives for round ten: decision 73, dates by season.

Crow, 29 September, relaying Matt: use "by season" to pick dates in the
Departures section.

Measured off the **deployed production build** at **1440x900** and **390** on
29 September 2026, `swat-website-storefront.vercel.app/tours/
mighty-5-utah-from-las-vegas/` (gate 6666). Harvest in
`r8/harvest/season-now-*`.

  Departures  decision 67D as it shipped: 928px column at x=52, y=8,781, the
              TENTH section. Two tabs, "2026 · 13 dates" 147x52 and
              "2027 · 52 dates" 149x52. Opens on 2026 (first year with an
              unsold date): 537px, three month cards 223px wide in a 4-track
              grid, 12px gap. 2027 tab: 1,140px, twelve cards, 3 rows.
              Rows 52px: "Mon 5" 15/700, price 12.5 under it (2027 only), a
              rust "Book" pill or a grey "SOLD OUT" + outline "Waitlist".
  Season band "This trip by season" is the FOURTH section, y=1,990, 405px
              (1,094px on a phone): four 220px cards, each with the months, a
              rust heading, one line and "22 autumn departures ›". That link
              goes to #departures and lands on the 2026 tab whatever season
              you tapped. The band is 6,791px above the dates it counts.
  Seasons     meteorological (lib/content/seasons.ts): Dec-Feb winter. For
              this trip, from today: Autumn 22 (9 in Oct-Nov 2026, 13 in
              Sep-Nov 2027), Winter 16 (Dec 2026, Jan-Feb 2027, Dec 2027),
              Spring 14, Summer 13. Prices move INSIDE seasons: Spring is
              $1,999 until May, Autumn 2027 is $2,199 until Oct 11.
"""

import mocks_i as i

MONTH = i.MONTH
MON = i.MON
DATES = i.DATES

#: DESERT_NOTES from src/lib/content/seasons.ts, verbatim — this trip names
#: only desert places, so these are the lines the live band prints.
NOTES = {
    'Spring': ('Warm days, cold mornings',
               'Comfortable walking weather and the desert in flower. Mornings '
               'near freezing at Bryce, and the high country can still be under '
               'snow into May.'),
    'Summer': ('Hot, and we mean it',
               'Over 100&deg;F in the canyons through July and August, with '
               'afternoon thunderstorms. Early starts, long lunches, and '
               'everything worth seeing done before noon.'),
    'Autumn': ('The best month to come',
               'Thirty degrees cooler than July, thinner crowds and low light on '
               'red rock. If your dates are flexible, this is the one to pick.'),
    'Winter': ('Empty, and often snowed',
               'Bryce and the high plateaus under snow, the canyons quiet and '
               'clear. Short days, cold nights, and some roads closed.'),
}
BY_MONTH = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer',
            'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
SPAN = {'Spring': 'Mar &ndash; May', 'Summer': 'Jun &ndash; Aug',
        'Autumn': 'Sep &ndash; Nov', 'Winter': 'Dec &ndash; Feb'}


def season_of(d):
    return BY_MONTH[d.month - 1]


def season_year(d):
    """'2026' for an autumn, '2026&ndash;27' for the winter that starts in Dec 2026."""
    s = season_of(d)
    if s != 'Winter':
        return str(d.year)
    start = d.year if d.month == 12 else d.year - 1
    return f'{start}&ndash;{str(start + 1)[2:]}'


def runs():
    """[(season, season-year, [departures])] in date order: six runs for this
    trip, Autumn 2026 through Winter 2027-28."""
    out = []
    for x in DATES:
        key = (season_of(x['d']), season_year(x['d']))
        if not out or out[-1][:2] != key:
            out.append((key[0], key[1], []))
        out[-1][2].append(x)
    return out


def by_season():
    """Season -> departures across both years, in date order."""
    out = {}
    for x in DATES:
        out.setdefault(season_of(x['d']), []).append(x)
    return out


def from_price(xs):
    ps = [x['price'] for x in xs if x['price']]
    return f'${min(ps):,}' if ps else '$1,999'


def is_open(x):
    return not x['sold']


# ------------------------------------------------------ the live month card
def row(x):
    d = x['d']
    if x['sold']:
        sub, act = '<em class="so">SOLD OUT</em>', '<u class="wl">Waitlist</u>'
    else:
        p = i.price(x)
        sub = f'<em>{p}</em>' if p else ''
        act = '<u>Book</u>'
    return (f'<li><span><b>{i.WD[d.weekday()]} {d.day}</b>{sub}</span>{act}</li>')


def mcard(y, m, xs, year=False):
    """One month as DepartureCalendar renders it since 67D: caps month name
    over a rule, a row per date, equal height across the row of cards."""
    yl = f' <i>{y}</i>' if year else ''
    return (f'<div class="k10-mc" data-m="{y}-{m:02d}"><h4>{MONTH[m - 1]}{yl}</h4>'
            f'<ul>{"".join(row(x) for x in xs)}</ul></div>')


def grid(xs, year=False, cols=4):
    ms = {}
    for x in xs:
        ms.setdefault((x['d'].year, x['d'].month), []).append(x)
    cards = ''.join(mcard(y, m, v, year) for (y, m), v in ms.items())
    return f'<div class="k10-grid c{cols}">{cards}</div>'


# ------------------------------------------------------------------ A · now
def now():
    tabs = ('<div class="k10-ytabs"><span class="on"><b>2026</b><em>13 dates</em></span>'
            '<span><b>2027</b><em>52 dates</em></span></div>')
    y26 = [x for x in DATES if x['d'].year == 2026]
    return i.frame(
        i.SOLD_LINE + tabs +
        '<p class="k10-line">2026 dates <b>from $1,999</b>. The rate for the date '
        'you choose is confirmed when you book.</p>' + grid(y26))


# ---------------------------------------------- B · season tabs, not years
def opt_tabs(sel=('Autumn', '2027')):
    tabs = ''
    chosen = None
    for s, sy, xs in runs():
        live = [x for x in xs if is_open(x)]
        on = (s, sy) == sel
        if on:
            chosen = (s, sy, xs)
        n = f'{len(live)} open' if len(live) != len(xs) else f'{len(xs)} dates'
        tabs += (f'<span class="{"on" if on else ""}"><b>{s} <i>{sy}</i></b>'
                 f'<em>{SPAN[s]} &middot; {n}</em></span>')
    s, sy, xs = chosen
    h, line = NOTES[s]
    return i.frame(
        i.SOLD_LINE +
        f'<div class="k10-stabs">{tabs}</div>'
        f'<div class="k10-note"><b>{h}.</b> {line} '
        f'<span class="k10-from">{s} {sy} from <b>{from_price(xs)}</b></span></div>'
        + grid(xs, cols=3))


# ------------------------------------ C · the season cards pick the dates
ORDER = ['Autumn', 'Winter', 'Spring', 'Summer']   # from today, soonest first


def opt_cards(sel='Autumn'):
    bs = by_season()
    cards = ''
    for s in ORDER:
        xs = bs[s]
        live = [x for x in xs if is_open(x)]
        years = sorted({season_year(x['d']) for x in xs})
        yl = ' and '.join(years).replace('&ndash;', '&ndash;')
        h, _ = NOTES[s]
        cards += (f'<div class="k10-sc{" on" if s == sel else ""}" data-s="{s}">'
                  f'<b>{s}</b><em>{SPAN[s]} &middot; {yl}</em>'
                  f'<strong>{h}</strong>'
                  f'<span class="ct">{len(live)} open dates &middot; from '
                  f'{from_price(xs)}</span></div>')
    xs = bs[sel]
    h, line = NOTES[sel]
    groups = ''
    for s, sy, run in runs():
        if s != sel:
            continue
        live = [x for x in run if is_open(x)]
        groups += (f'<div class="k10-yh"><b>{s} {sy}</b><em>{len(live)} of '
                   f'{len(run)} open</em></div>' + grid(run))
    return i.frame(
        '<p class="dp-lead">Pick a season first. The same trip, very different '
        'weeks.</p>'
        f'<div class="k10-scs">{cards}</div>'
        f'<div class="k10-note"><b>{h}.</b> {line}</div>' + groups +
        i.SOLD_LINE.replace('dp-intro', 'dp-foot'))


# ------------------------------------------ D · every season on one screen
def chip(x):
    d = x['d']
    if x['sold']:
        return (f'<span class="k10-ch so"><b>{MON[d.month - 1]} {d.day}</b>'
                '<em>Sold out</em></span>')
    p = i.price(x) or 'Book'
    pk = ' pk' if x['price'] == 2199 else ''
    return f'<span class="k10-ch{pk}"><b>{MON[d.month - 1]} {d.day}</b><em>{p}</em></span>'


def opt_rows():
    rows = ''
    for s in ORDER:
        h, _ = NOTES[s]
        xs = by_season()[s]
        body = ''
        for ss, sy, run in runs():
            if ss != s:
                continue
            body += (f'<span class="k10-yl">{sy}</span>' + ''.join(chip(x) for x in run))
        rows += (f'<div class="k10-sr" data-s="{s}"><div class="k10-sl"><b>{s}</b>'
                 f'<em>{SPAN[s]}</em><strong>{h}</strong>'
                 f'<span>from {from_price(xs)}</span></div>'
                 f'<div class="k10-chs">{body}</div></div>')
    return i.frame(
        '<p class="dp-lead">Every date, by season. Tap a date to book it. Orange '
        'prices are the $2,199 peak weeks.</p>'
        f'<div class="k10-srs">{rows}</div>' +
        i.SOLD_LINE.replace('dp-intro', 'dp-foot'))


# ---------------------------- E · C's season cards over D's rows of dates
#: Crow, 29 Sep, on C: no "best month to come". Every season gets the same
#: plain what-to-expect line and a what-to-pack tip, so no season reads as the
#: wrong one to book. Re-expressed from DESERT_NOTES; nothing ranks a season.
EVEN = {
    'Autumn': 'Cool mornings and warm afternoons. Bring layers.',
    'Winter': 'Crisp, clear days and snow on the high country. Bring a warm coat.',
    'Spring': 'Mild days and the desert in flower. Bring layers for the mornings.',
    'Summer': 'Long, warm days with early starts. Bring a sun hat.',
}


def chip_even(x):
    """D's date button with every price in one color: the $2,199 weeks no
    longer print in orange, which marked them out as the ones to avoid."""
    d = x['d']
    if x['sold']:
        return (f'<span class="k10-ch so"><b>{MON[d.month - 1]} {d.day}</b>'
                '<em>Sold out</em></span>')
    return (f'<span class="k10-ch"><b>{MON[d.month - 1]} {d.day}</b>'
            f'<em>{i.price(x) or "Book"}</em></span>')


def opt_mix(sel='Autumn'):
    bs = by_season()
    cards = ''
    for s in ORDER:
        xs = bs[s]
        live = [x for x in xs if is_open(x)]
        cards += (f'<div class="k10-sc k10-sc2{" on" if s == sel else ""}" data-s="{s}">'
                  f'<b>{s}</b><em>{SPAN[s]}</em>'
                  f'<span class="ct">{len(live)} open &middot; from '
                  f'{from_price(xs)}</span></div>')
    rows = ''
    for s, sy, run in runs():
        if s != sel:
            continue
        live = [x for x in run if is_open(x)]
        fp = from_price(run)
        rows += (f'<div class="k10-sr k10-sr2"><div class="k10-sl"><b>{s} {sy}</b>'
                 f'<em>{len(live)} of {len(run)} open</em>'
                 f'<span>from {fp}</span></div>'
                 f'<div class="k10-chs">{"".join(chip_even(x) for x in run)}</div></div>')
    yt = ('<div class="k10-yt"><span class="on">Both years</span><span>2026</span>'
          '<span>2027</span></div>')
    return i.frame(
        '<div class="k10-hd2"><p class="dp-lead">Pick a season, then tap a date '
        'to book it.</p>' + yt + '</div>'
        f'<div class="k10-scs">{cards}</div>'
        f'<p class="k10-even"><b>{sel}:</b> {EVEN[sel]}</p>'
        f'<div class="k10-srs">{rows}</div>' +
        i.SOLD_LINE.replace('dp-intro', 'dp-foot'))
