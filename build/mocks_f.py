"""Mockup primitives for round five — the checkout, decisions 42 to 44.

Crow, 23 September, on the booking walk-through an hour after it went to
production: *"for the check out on the tours, I am still not sure I am loving
how it looks and feels right now."*

Everything here is measured off the **deployed production build** at
**1440x900** on 23 September 2026, at
`swat-website-storefront.vercel.app/book/mighty-5-utah-from-las-vegas/`
(gate 6666). 1440 rather than the sheet's usual 1200 because the complaint is
about how the page feels in his window, and because the emptiness the numbers
below describe only exists at that width.

  Chrome        promo strip 36px, sticky header 73px, so page chrome ends at
                y=109. `main` opens at **y=159**.
  The head      eyebrow at y=207, h1 48px at y=233, a 77px paragraph at y=293,
                then the departures line and the tour-page link.
  The flow      one grid at **y=461**, 1,248 wide: an **880px** question
                column and a **320px** summary rail, gap 48.
                Its total height is **556px**.
  At rest       question 1 open (372px: 90px of explanation, twelve 44px month
                chips in one row, then four 49px date rows two across), and
                questions 2, 3 and 4 folded to 60px bars at y=834, 895, 956.
  Answered      picking Mon 11 Jan folds question 1 to **76px** carrying
                "Mon, Jan 11 – Fri, Jan 15" and a Change link, and opens
                question 2 at y=539.
  The rail      at rest it holds four lines — the tour name, Departs "Pick a
                date", Travelling "Two of us", and a sentence saying the rate
                will appear. Answered it carries the two dates, the party, a
                $1,999 per-person figure, "$3,998 for 2 travellers", "10 SEATS
                LEFT" and the published-price comparison.
  The footer    **736px**, y=1,161 to y=1,897.
  The page      **1,897px**.
  Photographs   **zero** inside `main`. The six images on the page are the
                wordmark and the payment/accreditation marks in the footer.

The two numbers the round hangs off: the booking flow is **556px of a 1,897px
page**, and the **footer is 736px** — the single tallest thing on a page whose
only job is to take a booking.

Photography comes from `mocks.PHOTOS`. The Mighty 5 runs Zion, Canyonlands,
Arches, Capitol Reef and Bryce, so the trip panel draws those and nothing else
— borrowing a Yellowstone frame onto a Utah trip is the thing
`swat-hike-tiles-borrowed-pools` exists to stop.
"""

import mocks as m

# --------------------------------------------------------------- the numbers
HEADER = 73          # sticky header at 1440
STRIP = 36           # positioning strip above it
WINDOW = 900         # Crow's window
SHELL = 1248         # max-w-[78rem], the booking container
COLQ = 880           # question column
COLR = 320           # summary rail
GAP = 48

FLOW_H = 556         # the whole grid, at rest
FOOTER_H = 736
PAGE_H = 1897

TRIP = 'Mighty 5 Utah Tour From Las Vegas'
LEDE = ('5 days from Las Vegas. Every date, price, hotel and seat count below '
        'comes live out of the reservation system SWAT is moving onto, and '
        'nothing here can make a booking: it stops at the card.')
META = ('52 departures through December 2027, all of them 2027. The rest of '
        'this year keeps booking where it does today.')

#: The four January departures the page actually renders, verbatim.
JAN = [('Mon, Jan 4', 'Fri, Jan 8', '$1,999', 8),
       ('Mon, Jan 11', 'Fri, Jan 15', '$1,999', 10),
       ('Mon, Jan 18', 'Fri, Jan 22', '$1,999', 10),
       ('Mon, Jan 25', 'Fri, Jan 29', '$1,999', 10)]

MONTHS = ['Jan 2027', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#: The five days Softrip files against the departure, in its own words.
DAYS = [('Day 1', 'Las Vegas to Zion National Park', 'Springdale'),
        ('Day 2', 'Canyonlands National Park and Moab', 'Moab'),
        ('Day 3', 'Arches National Park and Capitol Reef', 'Torrey'),
        ('Day 4', 'Capitol Reef to Bryce Canyon National Park', 'Bryce'),
        ('Day 5', 'Bryce Canyon and Return to Las Vegas', None)]

#: Photo per day, from the trip's own parks. mocks.PHOTOS keys.
DAYPIX = ['zion', 'mesa', 'arches', 'capitol', 'bryce']


# ------------------------------------------------------------------- chrome
def sitehead():
    """The nine-item nav and the positioning strip, as they ship."""
    return m.header(active='Home', strip=True)


def sitefoot():
    """The real footer: four link columns, a legal row, 736px at 1440.

    Drawn because it is evidence. On the deployed page it is the tallest
    element by a wide margin and the decision cannot be judged without it in
    the picture.
    """
    cols = [
        ('TRIP STYLES', ['Backpacking', 'Guided small group', 'Day tour',
                         'Self-drive', 'Private &amp; custom',
                         'Every trip style']),
        ('PLAN', ['Find a trip', 'Departing from', 'The trip map',
                  'Guides &amp; resources', 'Packing list', 'FAQs']),
        ('COMPANY', ['About us', 'The Archive', 'Reviews',
                     'Travel professionals', 'Contact']),
    ]
    blurb = (
        '<div class="b-fcol wide">'
        '<div class="b-fblurb">Guided small-group adventures across the '
        'national parks of the American West.</div>'
        '<div class="b-fcon"><b>800-970-5864</b><br>'
        'info@southwestadventuretours.com</div>'
        '<div class="b-fsoc">'
        + ''.join('<i></i>' for _ in range(6)) +
        '</div>'
        '<div class="b-fadd">382 E 650 S Circle<br>Cedar City, UT 84720</div>'
        '</div>')
    rest = ''.join(
        f'<div class="b-fcol"><h6>{h}</h6>'
        + ''.join(f'<span>{x}</span>' for x in items) + '</div>'
        for h, items in cols)
    acc = ('<div class="b-fcol"><h6>ACCREDITED BY</h6>'
           '<div class="b-facc"><i></i><i></i><i></i></div></div>')
    return ('<div class="b-foot"><div class="m-shell">'
            f'<div class="b-fgrid">{blurb}{rest}{acc}</div>'
            '<div class="b-flegal"><span>&copy; 2026 Southwest Adventure '
            'Tours.</span><span>Privacy &amp; cancellation policy</span>'
            '<span>Trip protection</span>'
            '<em>Guiding the Colorado Plateau and the parks of the American '
            'West.</em></div>'
            '</div></div>')


def checkouthead(step=1):
    """The stripped shell: wordmark, where you are, and the phone number.

    No nav. A checkout that carries a nine-item nav is a checkout with nine
    ways out of it, and SWAT's audience skews older — the rule from the brief
    is that anything that looks clickable gets clicked.
    """
    dots = ''.join(
        f'<i class="{"on" if i <= step else ""}"></i>' for i in range(1, 5))
    return ('<div class="b-cohd"><div class="b-coshell">'
            f'<img class="m-logo" src="{m.WORDMARK}" alt="Southwest Adventure Tours">'
            f'<div class="b-costeps">{dots}<span>Step {step} of 4</span></div>'
            '<div class="b-cophone">Questions? <b>800-970-5864</b></div>'
            '</div></div>')


def checkoutfoot():
    """One line instead of 736px."""
    return ('<div class="b-cofoot"><div class="b-coshell">'
            '<span>&copy; 2026 Southwest Adventure Tours</span>'
            '<span>Privacy &amp; cancellation policy</span>'
            '<span>Secure booking</span></div></div>')


# --------------------------------------------------------------- page head
def pagehead(meta=True):
    """Eyebrow, h1, the 77px lede, the departures line."""
    mrow = ('<div class="b-meta"><span>' + META + '</span>'
            '<a>The tour page &rsaquo;</a></div>') if meta else ''
    return ('<div class="b-head"><div class="b-shell">'
            '<div class="b-eyebrow">Booking walk-through</div>'
            f'<h1 class="b-h1">{TRIP}</h1>'
            f'<p class="b-lede">{LEDE}</p>{mrow}'
            '</div></div>')


def photoband(h=340):
    """A photograph across the top, with the trip on it.

    The height is the one number that matters here: at 340 the questions still
    start inside the first screen (y=499 against a fold at 900).
    """
    return (f'<div class="b-band" style="height:{h}px">'
            + m.img('zion', 1440, h, cls='b-bandimg') +
            '<div class="b-bandtint"></div>'
            '<div class="b-bandtext"><div class="b-shell">'
            '<div class="b-eyebrow light">Booking</div>'
            f'<h1 class="b-h1 light">{TRIP}</h1>'
            '<div class="b-bandfacts"><span>5 days</span><span>Las Vegas '
            'return</span><span>from $1,999 per person</span>'
            '<span>52 departures in 2027</span></div>'
            '</div></div></div>')


# ------------------------------------------------------------------- steps
def stepbar(n, title, answer=None, state='shut'):
    """One question. `state` is open | shut | done."""
    ans = ''
    if state == 'done' and answer:
        ans = (f'<div class="b-sans"><span>{answer}</span>'
               '<a>Change</a></div>')
    cls = f'b-step {state}'
    return (f'<div class="{cls}"><div class="b-shd">'
            f'<i class="b-sno">{n}</i><span>{title}</span>'
            f'<u class="b-schev"></u></div>{ans}</div>')


def datehelp():
    return ('<p class="b-help">Every date is one the reservation system '
            'confirmed it can sell, with a rate against it and seats left on '
            'the bus. Each one shows the day you leave and the day you are '
            'back. This list was checked Sep 22; the price and the seats are '
            're-checked live the moment you pick one.</p>')


def monthchips(on=0):
    inner = ''.join(
        f'<span class="b-chip{" on" if i == on else ""}">{t}</span>'
        for i, t in enumerate(MONTHS))
    return f'<div class="b-chips">{inner}</div>'


# ---------------------------------------------------------- date pickers
def dates_now():
    """Today: twelve month chips, then the month's departures two across."""
    rows = ''.join(
        f'<span class="b-drow"><b>{a} &ndash; {b}</b><em>{p}</em></span>'
        for a, b, p, _ in JAN)
    return (datehelp() + monthchips() +
            f'<div class="b-drows">{rows}</div>')


def dates_cal(span=True):
    """A real January, with the five days of the trip drawn across the week.

    The sparseness argument is the whole point of drawing it: a month grid is
    35 cells and January answers four of them. Running the trip across the
    row as a bar is what stops it reading as an empty calendar — the shaded
    Monday-to-Friday block is the thing being bought.
    """
    # January 2027 starts on a Friday. 31 days, 5 rows of 7.
    start_blank = 5          # Su Mo Tu We Th | Fr
    heads = ''.join(f'<i>{d}</i>' for d in
                    ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'])
    departs = {4: '$1,999', 11: '$1,999', 18: '$1,999', 25: '$1,999'}
    cells = ''.join('<span class="b-cal-e"></span>'
                    for _ in range(start_blank))
    for day in range(1, 32):
        if day in departs:
            bar = ('<u class="b-cal-bar" style="width:%dpx"></u>' % (5 * 96 - 12)
                   if span else '')
            cells += (f'<span class="b-cal-d go">{bar}<b>{day}</b>'
                      f'<em>{departs[day]}</em>'
                      '<u class="b-cal-dot"></u></span>')
        else:
            cells += f'<span class="b-cal-d"><b>{day}</b></span>'
    return (datehelp() + monthchips() +
            '<div class="b-cal">'
            f'<div class="b-cal-hd">{heads}</div>'
            f'<div class="b-cal-g">{cells}</div></div>'
            '<div class="b-cal-key"><span><u class="k go"></u>Departs &mdash; '
            'every Monday</span><span><u class="k bar"></u>The five days you '
            'are away</span></div>')


def dates_list():
    """One scrolling list of all 52, month headings sticky as you go."""
    def block(label, rows):
        inner = ''.join(
            f'<span class="b-lrow"><b>{a} &ndash; {b}</b>'
            f'<em>{p}</em><i>{s} seats</i></span>' for a, b, p, s in rows)
        return (f'<div class="b-lblock"><h6>{label}</h6>{inner}</div>')
    feb = [('Mon, Feb 1', 'Fri, Feb 5', '$1,999', 10),
           ('Mon, Feb 8', 'Fri, Feb 12', '$1,999', 6)]
    return (datehelp() +
            '<div class="b-list">'
            + block('January 2027', JAN)
            + block('February 2027', feb)
            + '<div class="b-lfade"></div></div>'
            '<div class="b-lnote">52 departures, all of 2027, in one scroll '
            '&mdash; the months stay stuck to the top as you pass them.</div>')


def dates_fat():
    """The chips stay; the row carries what a customer actually weighs up."""
    rows = ''
    tags = ['', '<i class="b-tag">Only 10 seats</i>',
            '<i class="b-tag warm">Filling up &mdash; 4 left</i>', '']
    for (a, b, p, s), tag in zip(JAN, tags):
        rows += ('<span class="b-frow">'
                 f'<span class="b-fdate"><b>{a} &ndash; {b}</b>'
                 '<em>5 days, back on a Friday</em></span>'
                 f'<span class="b-fprice"><b>{p}</b><em>per person</em></span>'
                 f'<span class="b-ftag">{tag}</span>'
                 '<u class="b-fgo">Choose</u></span>')
    return (datehelp() + monthchips() + f'<div class="b-frows">{rows}</div>')


# ------------------------------------------------------------------- rails
def rail_now(answered=False):
    """The 320px summary as it ships — white, bordered, text only."""
    if not answered:
        body = ('<dl class="b-rdl"><dt>Departs</dt><dd>Pick a date</dd>'
                '<dt>Travelling</dt><dd>Two of us</dd></dl>'
                '<p class="b-rnote">The live rate appears here as soon as you '
                'pick a date.</p>')
    else:
        body = ('<dl class="b-rdl"><dt>Departs</dt><dd>Mon, Jan 11, 2027</dd>'
                '<dt>Back on</dt><dd>Fri, Jan 15, 2027</dd>'
                '<dt>Travelling</dt><dd>Two of us</dd></dl>'
                '<div class="b-rprice"><b>$1,999</b><em>per person</em></div>'
                '<div class="b-rtot">$3,998 for 2 travellers</div>'
                '<div class="b-rseats">10 SEATS LEFT</div>'
                '<p class="b-rnote">The website advertises this tour from '
                '$1,999 per person. This is the rate that would be '
                'charged.</p>')
    return ('<aside class="b-rail"><div class="b-rhd">Your booking</div>'
            f'<div class="b-rtrip">{TRIP}</div>{body}</aside>')


def rail_trip(days=True, answered=True):
    """The rail becomes the trip: a photograph, the price, then the days."""
    dayrows = ''
    if days:
        rows = ''.join(
            '<span class="b-drday">'
            + m.img(pix, 92, 62, cls='b-drpic') +
            f'<span><b>{d}</b>{t}</span></span>'
            for (d, t, _), pix in zip(DAYS, DAYPIX))
        dayrows = ('<div class="b-rdays"><h6>Your five days</h6>'
                   f'{rows}'
                   '<div class="b-rhot">Four hotels, named on the '
                   'confirmation</div></div>')
    if answered:
        money = ('<div class="b-rprice big"><b>$1,999</b><em>per person</em>'
                 '</div><div class="b-rtot">$3,998 for 2 travellers</div>'
                 '<div class="b-rseats">10 seats left</div>')
        lines = ('<dl class="b-rdl"><dt>Departs</dt><dd>Mon, Jan 11, 2027</dd>'
                 '<dt>Back on</dt><dd>Fri, Jan 15, 2027</dd>'
                 '<dt>Travelling</dt><dd>Two of us</dd></dl>')
    else:
        money = ('<div class="b-rprice big"><b>$1,999</b>'
                 '<em>per person, from</em></div>')
        lines = ('<dl class="b-rdl"><dt>Departs</dt><dd>Pick a date</dd>'
                 '<dt>Travelling</dt><dd>Two of us</dd></dl>')
    return ('<aside class="b-rail trip">'
            '<div class="b-rpic">'
            + m.img('arches', 320, 190, cls='b-rpicimg') +
            f'<span class="b-rpicname">{TRIP}</span></div>'
            f'<div class="b-rbody">{lines}{money}</div>'
            f'{dayrows}</aside>')


def party(on='Two of us'):
    """Question 2 as it ships: four buttons and a Continue."""
    btns = ''.join(
        f'<span class="b-party{" on" if t == on else ""}">{t}</span>'
        for t in ['On my own', 'Two of us', 'Three of us', 'Four of us'])
    return ('<p class="b-help">The per-person rate depends on how many share '
            'a room, so this changes the price itself and not just the total. '
            'Each answer is priced live.</p>'
            f'<div class="b-parties">{btns}</div>'
            '<div class="b-cont">Continue</div>')


def holdsrow(open_=False):
    """The closed disclosure the itinerary lives behind today.

    Drawn because decision 44 is about this row and a Now panel that leaves it
    out is arguing against something that is not on the page.
    """
    body = ''
    if open_:
        rows = ''.join(
            '<span class="b-drday">'
            + m.img(pix, 92, 62, cls='b-drpic')
            + f'<span><b>{d}</b>{t}</span></span>'
            for (d, t, _), pix in zip(DAYS, DAYPIX))
        body = ('<div class="b-holdsbody"><div class="b-holdscol">'
                '<h6>The days</h6>' + rows + '</div>'
                '<div class="b-holdscol"><h6>Where you sleep</h6>'
                '<span>Springdale</span><span>Moab</span><span>Torrey</span>'
                '<span>Bryce</span>'
                '<h6 style="margin-top:14px">Park fees, and one add-on</h6>'
                '<span>Six park entrances, included</span>'
                '<span>Optional stargazing</span></div></div>')
    cls = 'b-holds' + (' open' if open_ else '')
    return (f'<div class="{cls}"><div class="b-holdshd">'
            '<span>What the reservation system holds for this departure</span>'
            '<u></u></div>' + body + '</div>')


def rail_none():
    return ''


# ------------------------------------------------------------ the whole flow
def flow(step1, rail, open_step=1):
    """The four questions beside the rail."""
    if open_step == 1:
        s1 = ('<div class="b-step open"><div class="b-shd">'
              '<i class="b-sno">1</i><span>When you travel</span></div>'
              f'<div class="b-sbody">{step1}</div></div>')
        s2 = stepbar(2, 'Who is coming')
    else:
        s1 = stepbar(1, 'When you travel',
                     'Mon, Jan 11 &ndash; Fri, Jan 15', 'done')
        s2 = ('<div class="b-step open"><div class="b-shd">'
              '<i class="b-sno">2</i><span>Who is coming</span></div>'
              f'<div class="b-sbody">{party()}</div></div>')
    rest = s2 + stepbar(3, 'Your details') + stepbar(4, 'Review and pay')
    railcol = f'<div class="b-railcol">{rail}</div>' if rail else ''
    cls = 'b-flow' + ('' if rail else ' solo')
    return (f'<div class="{cls}"><div class="b-qcol">{s1}{rest}</div>'
            f'{railcol}</div>')


def fold(top=WINDOW, label='bottom of a 1440&times;900 window'):
    """The edge of the screen, and nothing else.

    No dimming wash under it. Every panel in decision 42 is boxed to the
    tallest of them, so a shorter page leaves paper at the bottom of its
    canvas — and a grey wash over that paper reads as more page rather than
    as the end of one. The end marker below says where the page actually
    stops, which is the number being argued about.
    """
    return (f'<div class="m-fold" style="top:{top}px"><span>{label}</span></div>')


def pageend(px):
    """Where the page stops, drawn. Flows after the last band."""
    return (f'<div class="b-end"><span>end of page &middot; {px}</span></div>')


def page(kind='now', step1=None, rail=None, foldline=True):
    """One whole checkout page at 1440.

    kind:
      now      site chrome, no photograph, the 736px footer
      band     site chrome plus a photograph across the top
      shell    its own shell — no nav, no footer, one column
      shelltrip  its own shell, with the trip panel beside the questions
    """
    step1 = dates_now() if step1 is None else step1
    if kind == 'now':
        body = (sitehead() + pagehead() +
                '<div class="b-page">'
                f'<div class="b-shell">{flow(step1, rail if rail is not None else rail_now())}</div>'
                '</div>' + sitefoot())
    elif kind == 'band':
        body = (sitehead() + photoband() +
                '<div class="b-page up">'
                f'<div class="b-shell">{flow(step1, rail if rail is not None else rail_now())}</div>'
                '</div>' + sitefoot())
    elif kind == 'shell':
        body = (checkouthead() +
                '<div class="b-page co solo">'
                '<div class="b-coshell">'
                f'<div class="b-cotitle"><h1>{TRIP}</h1>'
                '<span>5 days from Las Vegas</span></div>'
                f'{flow(step1, None)}</div></div>' + checkoutfoot())
    else:  # shelltrip
        body = (checkouthead() +
                '<div class="b-page co">'
                '<div class="b-coshell">'
                f'<div class="b-cotitle"><h1>{TRIP}</h1>'
                '<span>5 days from Las Vegas &middot; small group of 7&ndash;13</span></div>'
                f'{flow(step1, rail if rail is not None else rail_trip())}'
                '</div></div>' + checkoutfoot())
    ends = {'now': '1,897px', 'band': 'about 2,080px',
            'shell': 'about 900px', 'shelltrip': 'about 1,050px'}
    return body + pageend(ends[kind]) + (fold() if foldline else '')


def qregion(inner):
    """Just question one, at its real 880px, on a 980px canvas.

    Decision 43 is judged on whether a calendar cell is readable, and a 1440
    canvas in a four-column row scales to 0.175 — a 96px cell renders at 17px
    and the decision cannot be seen at all on the sheet. The question column
    is 880px on the deployed page either way, so drawing it at its own width
    changes the scale and not the thing being judged.
    """
    return ('<div class="b-crop"><div class="b-qshell">'
            '<div class="b-step open"><div class="b-shd">'
            '<i class="b-sno">1</i><span>When you travel</span></div>'
            f'<div class="b-sbody">{inner}</div></div>'
            + stepbar(2, 'Who is coming') + stepbar(3, 'Your details')
            + '</div></div>')


def region(inner, head=True):
    """A crop: the question column and rail only, on the page's own paper.

    Decisions 43 and 44 are about one block, and drawing 1,897px of page to
    argue about a 372px question wastes the panel on chrome the reader has
    already judged in decision 42.
    """
    top = ('<div class="b-croptop"><div class="b-shell">'
           '<span class="b-eyebrow">Booking</span>'
           f'<b>{TRIP}</b></div></div>') if head else ''
    return (f'<div class="b-crop">{top}'
            f'<div class="b-shell">{inner}</div></div>')
