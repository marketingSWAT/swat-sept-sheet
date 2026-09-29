"""Mockup primitives for round eight: decision 67, picking a date.

Crow, 29 September, with a screenshot of the Departures section on the Mighty 5
from Las Vegas page:

  "something I want to review is this page for departures when you go to pick
   your date for booking a tour ... I just really feel like we can make this
   easier and more clear on actually picking dates, because also when you get
   into 2027 you have to click that drop down to see all the other dates"

Measured off the **deployed production build** at **1440x900** and **390**
on 29 September 2026, `swat-website-storefront.vercel.app/tours/
mighty-5-utah-from-las-vegas/` (gate 6666). Harvest in `r8/harvest/`.

  Page       12,936px at 1440. "Departures" is the TENTH section, at y=8,781,
             under the gallery and "More from Zion...". The rail's "Choose your
             date" button is at y=1,535, so the button sends you 7,200px down.
  Section    928px column at x=52, 887px tall as it loads: a 42px sold-out
             line, then October (4 rows) and November 2026 (5 rows) only, then
             a 353x43 pill "Show all 65 dates through December 2027".
  Rows       65px each, date 16px/600, no price on any row, Reserve pill
             87x40 rust, sold out = grey caps + a 108x42 "Join the list".
  Opened     the section grows from 887px to **5,322px**: six 900px screens of
             Mondays, 15 month headings, 65 rows. Page 12,936 -> 17,371.
  Phone      the section starts at y=13,766 (about 16 screens down) and is
             956px closed, 5,360px open.
  Dates      65: 13 in 2026 (7 sold out, all book on AdventureCentral, no
             per-date price published) and 52 in 2027 (Softrip, per-date
             retail from ProductShop 23 Sep: **$1,999** Jan-Apr and from
             Oct 18, **$2,199** May 3 - Oct 11). Not one row shows its price.
"""

import json
import os
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, '..', 'r8', 'harvest', 'm5lv-dates.json')))

AW = 1440
PHONE = '800-970-5864'
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
WD = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def _d(iso):
    y, m, d = (int(x) for x in iso.split('-'))
    return date(y, m, d)


#: Every departure, in order, as the live page lists them.
DATES = [dict(x, d=_d(x['date'])) for x in DATA['dates']]


def months():
    """(year, month) -> [departures], in calendar order."""
    out = {}
    for x in DATES:
        out.setdefault((x['d'].year, x['d'].month), []).append(x)
    return out


def price(x):
    return f'${x["price"]:,}' if x['price'] else None


def md(d):
    return f'{MON[d.month - 1]} {d.day}'


def span(x):
    """'Oct 5 &ndash; 9' or 'Nov 30 &ndash; Dec 4'."""
    end = x['d'] + timedelta(days=4)
    tail = end.day if end.month == x['d'].month else md(end)
    return f'{md(x["d"])} &ndash; {tail}'


# ------------------------------------------------------------------ frame
def rail(next_line='62 more dates below', cta='Choose your date', extra=''):
    """The booking panel as it ships: navy price block, three dates, four
    facts, the orange button, the phone number."""
    return ('<aside class="dp-rail">'
            '<div class="dp-rt"><span class="l">FROM</span><b>$1,999</b>'
            '<span class="s">per person, double occupancy, 2026</span></div>'
            '<div class="dp-rb">'
            '<span class="l">NEXT DEPARTURES</span>'
            '<ul class="dp-rd"><li>Oct 5, 2026</li><li>Oct 12, 2026</li>'
            '<li>Oct 19, 2026</li></ul>'
            f'<span class="dp-rmore">{next_line}</span>'
            '<div class="dp-spec"><span>Activity level</span><b>Easy</b></div>'
            '<div class="dp-spec"><span>Lodging</span><b>Hotels &amp; lodges</b></div>'
            '<div class="dp-spec"><span>Group size</span><b>Small group, 7&ndash;13</b></div>'
            '<div class="dp-spec"><span>Reviews</span><b><i class="st">&#9733;&#9733;'
            '&#9733;&#9733;&#9733;</i> <u>5 reviews</u></b></div>'
            f'<span class="dp-cta">{cta}</span>{extra}'
            f'<p class="dp-rq">Questions? <u>{PHONE}</u></p>'
            '</div></aside>')


def frame(left, rail_html=None, rings=''):
    """The section at the live geometry: a 928px column beside the 360px
    sticky rail, 48px apart, 52px in from the edge of a 1440 window. On a
    phone the rail is not beside the dates at all — the page has a sticky
    bottom bar instead — so the phone view draws that bar."""
    r = rail_html if rail_html is not None else rail()
    return (f'<div class="dp-page">{rings}<div class="dp-grid">'
            f'<div class="dp-col"><h2 class="dp-h2">Departures</h2>{left}</div>'
            f'{r}</div>'
            '<div class="dp-pbar"><span>From <b>$1,999</b></span>'
            '<u>Choose your date</u></div></div>')


SOLD_LINE = ('<p class="dp-intro">7 dates on this trip have sold out as of '
             f'Sep 24, 2026. Call us on <u>{PHONE}</u> about a date marked sold '
             'out &mdash; we keep a waiting list, and cancellations do '
             'happen.</p>')


# ------------------------------------------------------------------ A · now
def _row(x):
    right = ('<span class="dp-sold">SOLD OUT</span><span class="dp-join">'
             'Join the list</span>' if x['sold'] else
             '<span class="dp-res">Reserve</span>')
    d = x['d']
    return (f'<li><b>{MON[d.month - 1]} {d.day}, {d.year}</b>'
            f'<span class="dp-rr">{right}</span></li>')


def now():
    ms = months()
    blocks = ''
    for key in [(2026, 10), (2026, 11)]:
        blocks += (f'<div class="dp-mo"><h3>{MONTH[key[1] - 1].upper()} {key[0]}</h3>'
                   f'<ul class="dp-rows">{"".join(_row(x) for x in ms[key])}</ul></div>')
    return frame(
        SOLD_LINE + blocks +
        '<span class="dp-fold">Show all 65 dates <em>through December 2027</em> '
        '<i>&#8964;</i></span>')


# ---------------------------------------------- B · the calendar you approved
def monthstrip(on=(2026, 10), sub='dates'):
    """Fifteen months, both years, one row. The year is printed once where it
    changes, not on every chip."""
    chips = ''
    last_year = None
    for (y, m), xs in months().items():
        if y != last_year:
            chips += f'<span class="dp-yr">{y}</span>'
            last_year = y
        live = [x for x in xs if not x['sold']]
        if sub == 'dates':
            s = f'{len(live)} open' if len(live) != len(xs) else f'{len(xs)} dates'
            if not live:
                s = 'sold out'
        else:
            s = price(xs[0]) or '&nbsp;'
        cls = ' on' if (y, m) == on else ''
        cls += ' gone' if not live else ''
        chips += f'<span class="dp-mc{cls}"><b>{MON[m - 1]}</b><em>{s}</em></span>'
    return f'<div class="dp-strip">{chips}</div>'


def calendar(y, m):
    """One month, Sunday-first, each departure a bar across the five days —
    DepartureMonth.tsx, the calendar built for decision 43B, as it renders
    on /book/ today, plus the one state it never needed there: sold out."""
    first = date(y, m, 1)
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    nxt = date(y + (m == 12), m % 12 + 1, 1)
    deps = {x['d']: x for x in months()[(y, m)]}
    heads = ''.join(f'<i>{w}</i>' for w in
                    ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'])
    weeks = ''
    d = start
    while d < nxt:
        cells = ''
        bar = ''
        for i in range(7):
            day = d + timedelta(days=i)
            faint = ' out' if day.month != m else ''
            wk = ' wk' if i in (0, 6) else ''
            cells += f'<span class="dp-cd{faint}{wk}">{day.day}</span>'
            if day in deps:
                x = deps[day]
                if x['sold']:
                    bar = (f'<span class="dp-bar gone" style="left:calc({i} * 100% / 7 + 6px)">'
                           f'<b>{span(x)}</b><em>Sold out &middot; <u>Join the list</u></em></span>')
                else:
                    tag = price(x) or 'Book'
                    bar = (f'<span class="dp-bar" style="left:calc({i} * 100% / 7 + 6px)">'
                           f'<b>{span(x)}</b><em>{tag}</em></span>')
        weeks += f'<div class="dp-wk">{cells}{bar}</div>'
        d += timedelta(days=7)
    n = len(deps)
    return ('<div class="dp-cal">'
            f'<div class="dp-calhd"><b>{MONTH[m - 1]} {y}</b>'
            f'<em>{n} departures</em><span class="dp-arr">&lsaquo;</span>'
            '<span class="dp-arr">&rsaquo;</span></div>'
            f'<div class="dp-cdh">{heads}</div>{weeks}</div>')


def opt_calendar():
    return frame(
        '<p class="dp-lead">Each bar is one departure, drawn across the five days '
        'you are away. Tap one to book that date.</p>' +
        monthstrip(on=(2027, 5)) + calendar(2027, 5) +
        '<p class="dp-foot">Prices are per person, two sharing a room. A '
        f'date marked sold out has a waiting list: call <u>{PHONE}</u>.</p>')


# --------------------------------------------- C · every date, one screen
def opt_wall(sel='2027-05-03'):
    lines = ''
    last_year = None
    for (y, m), xs in months().items():
        if y != last_year:
            note = ('books on our current system' if y == 2026 else
                    'summer dates $2,199, the rest $1,999')
            lines += f'<div class="dp-wyr"><b>{y}</b><em>{note}</em></div>'
            last_year = y
        chips = ''
        for x in xs:
            d = x['d']
            if x['sold']:
                chips += (f'<span class="dp-dc gone"><b>{d.day}</b>'
                          '<em>Sold out</em></span>')
            else:
                on = ' on' if x['date'] == sel else ''
                p = price(x)
                chips += (f'<span class="dp-dc{on}{" peak" if x["price"] == 2199 else ""}">'
                          f'<b>{d.day}</b><em>{p or "Mon"}</em></span>')
        lines += (f'<div class="dp-wl"><span class="dp-wm">{MON[m - 1]}</span>'
                  f'<div class="dp-wc">{chips}</div></div>')
    x = next(v for v in DATES if v['date'] == sel)
    pick = ('<div class="dp-pick"><div><span class="l">YOUR DATE</span>'
            f'<b>Mon, {span(x)}, {x["d"].year}</b>'
            f'<em>5 days &middot; {price(x)} per person, two sharing</em></div>'
            '<span class="dp-go">Book this date</span></div>')
    return frame(
        '<p class="dp-lead">Every departure, every month. Tap a date, then '
        'book it.</p>'
        f'<div class="dp-wall">{lines}</div>{pick}')


# ------------------------------------------- D · the year, month by month
def opt_year(y=2027):
    ms = months()
    tabs = ''
    for yy in (2026, 2027):
        xs = [x for (a, _), v in ms.items() if a == yy for x in v]
        on = ' on' if yy == y else ''
        tabs += (f'<span class="dp-tab{on}"><b>{yy}</b>'
                 f'<em>{len(xs)} dates</em></span>')
    cards = ''
    for (a, m), xs in ms.items():
        if a != y:
            continue
        rows = ''
        for x in xs:
            rows += (f'<span class="dp-yr-row"><b>Mon {x["d"].day}</b>'
                     f'<em>{price(x) or ""}</em><u>Book</u></span>')
        cards += (f'<div class="dp-ycard"><h4>{MONTH[m - 1]}</h4>{rows}</div>')
    return frame(
        f'<div class="dp-tabs">{tabs}</div>'
        f'<div class="dp-ygrid">{cards}</div>'
        '<p class="dp-foot">Every trip leaves on a Monday and is back on the '
        'Friday. Prices are per person, two sharing a room.</p>')
