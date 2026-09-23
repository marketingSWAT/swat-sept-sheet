"""Decisions 42 to 44 — the checkout, round five.

Crow, 23 September, an hour after the booking walk-through went to the
production link so the SWAT sales team could walk it:

    "for the check out on the tours, I am still not sure I am loving how it
    looks and feels right now. Could you make me up a couple re designs on how
    we can change this and make it look and feel better"

There is no second sentence naming what is wrong, so the round starts by
counting. Measured on the deployed production build at 1440x900 on
23 September (see `mocks_f.py` for the full harvest), three numbers describe
the page better than any adjective:

  the booking flow is **556px** of a **1,897px** page,
  the footer under it is **736px** — the tallest thing on the page,
  and `main` contains **zero photographs**.

So the page is mostly site furniture wrapped round a form, on a site whose
every other page leads with a photograph. That is what "doesn't feel right"
measures out to, and the three decisions below are the three places it can be
fixed: the shell (42), the one question that fills the screen (43), and what
the customer can see of the trip they are buying while they buy it (44).
"""

import mocks as m
import mocks_f as f
from sheetkit import opt, quote, verdict, dec

ALL = []

NEW = ('New', '23 Sep &middot; checkout')

ASK = quote(
    ['For the check out on the tours, I am still not sure I am loving how it '
     'looks and feels right now. Could you make me up a couple re designs on '
     'how we can change this and make it look and feel better.'],
    'Crow, 23 September, after it went to the production link')

EARLIER = quote(
    ['Is there a better way to go through this check out so it&rsquo;s not so '
     'many pages I have to scroll to select what I want.'],
    'Crow, 22 September &mdash; the change that produced the page being '
    'looked at now')


# =====================================================================
# 42 — the shell
# =====================================================================
ALL.append(dec(
    42,
    'What a checkout page looks like',
    [('/book/&hellip;', ''), ('Crow', 'who'), ('1&ndash;3 days', ''),
     ('556px of 1,897', 'big')],
    [ASK, EARLIER],
    [
        opt('The site, with a form inside it',
            ['The booking flow is <b>556px</b> tall on a <b>1,897px</b> page '
             '&mdash; less than a third of it.',
             'The <b>footer under it is 736px</b>: the single tallest thing '
             'on the page.',
             '<b>No photograph anywhere in the page body.</b> The six images '
             'on it are the wordmark and the marks in the footer.',
             'The nine-item nav, the phone number, the Find a Trip button and '
             'the positioning strip sit above a page whose only job is to '
             'take one booking &mdash; <b>about 40 links out of the '
             'checkout</b>.'],
            '<p>This is what went to the production link this afternoon. The '
            'flow itself is the part that works &mdash; one question at a '
            'time, answered questions folded to a line &mdash; and none of '
            'the options below change it.</p>'
            '<p>What is wrong is everything round it. The page reads as a '
            'form that was dropped into the website rather than as the last '
            'step of buying a five-day trip, and the arithmetic says so: less '
            'than a third of the page is the booking.</p>',
            cost='&mdash;', risk='Reads as a form, not a purchase',
            cls='now',
            mockup=m.mock(f.page('now') + m.ring(1, '.b-flow')
                          + m.ring(2, '.b-foot') + m.ring(4, '.m-hd'),
                          1900, aw=1440)),

        opt('A photograph across the top',
            ['A <b>340px band</b> of the trip above the questions, carrying '
             'the name, the length, the from-price and the departure count.',
             'Everything else stays exactly where it is &mdash; same nav, '
             'same footer, same 880px column, same rail.',
             'The first question still starts inside the first screen: '
             '<b>y=499 against a fold at 900</b>.',
             'Page grows by about <b>180px</b>; the footer is still the '
             'tallest thing on it.'],
            '<p>The cheapest of the three, and the one that changes the least. '
            'It answers "it does not look like the rest of the site" and '
            'nothing else &mdash; the nine ways out of the checkout stay, and '
            'so does the 736px footer.</p>'
            '<p>Worth saying plainly: a big photograph at the top of a '
            'checkout is decoration. It is the right decoration, and it is '
            'half a day, but it does not make the page a checkout.</p>',
            cost='&frac12; day', risk='Fixes the look, not the shape',
            mockup=m.mock(f.page('band') + m.ring(1, '.b-band')
                          + m.ring(2, '.b-foot'), 2080, aw=1440)),

        opt('A checkout of its own, one column',
            ['<b>The site header and footer come off.</b> A 64px bar carries '
             'the wordmark, a four-step progress mark and the phone number.',
             'The footer becomes <b>one 52px line</b> instead of 736px.',
             'The questions move to a <b>centred 720px column</b> on a card, '
             'and the summary rail goes &mdash; the running total lives in '
             'the step.',
             'Page falls from <b>1,897px to about 900</b>. The whole booking '
             'is one screen.'],
            '<p>The standard answer, and the one every checkout the customer '
            'has already used looks like. Taking the nav off is not tidiness: '
            'it removes about forty links out of a page somebody is halfway '
            'through paying on.</p>'
            '<p>What it costs is the trip. With the rail gone there is '
            'nothing on the screen but questions, and a customer who cannot '
            'see what they are buying while they buy it is a customer looking '
            'for the back button. That is the reason I do not recommend '
            'it.</p>',
            cost='1&ndash;2 days',
            risk='Nothing on screen says what you are buying',
            mockup=m.mock(f.page('shell') + m.ring(1, '.b-cohd')
                          + m.ring(2, '.b-cofoot') + m.ring(3, '.b-flow'),
                          980, aw=1440)),

        opt('A checkout of its own, with the trip beside it',
            ['Same shell as the option to its left &mdash; <b>no nav, no '
             '736px footer</b>, a progress mark and the phone number.',
             'The 320px rail becomes <b>the trip</b>: a photograph, the two '
             'dates, the per-person rate, the total, the seats, and the five '
             'days underneath with a frame each.',
             'The questions keep the rest of the width on a white card '
             'against a sand page.',
             'Page falls from <b>1,897px to about 1,050</b> &mdash; and every '
             'pixel of it is the booking.'],
            '<p>The shell from option C with the thing option C throws away '
            'put back. The customer sees the trip for the whole four '
            'questions, which is what the rail is for, and the rail stops '
            'being four lines of white paper.</p>'
            '<p>It also does what the photograph option does &mdash; there is '
            'a real picture of Arches on the screen &mdash; without the page '
            'growing. Decision <a href="#d44">44</a> decides what else goes '
            'in that panel.</p>',
            cost='2&ndash;3 days',
            risk='Two layouts of the site chrome to maintain',
            cls='rec',
            mockup=m.mock(f.page('shelltrip') + m.ring(1, '.b-cohd')
                          + m.ring(2, '.b-rail'), 1180, aw=1440)),
    ],
    verdict([
        '<b>D.</b> It is the only one of the three that changes the shape of '
        'the page rather than the surface of it, and it is the only one where '
        'the customer can see the trip and the total at the same time as the '
        'question they are answering.',
        'The reason to take the site chrome off is not neatness. There are '
        'about forty links out of that page today, and SWAT&rsquo;s audience '
        'skews older &mdash; the standing rule on this build is that anything '
        'that looks clickable gets clicked. A nine-item nav across the top of '
        'a half-finished booking is forty invitations to leave it.',
        'If the budget is half a day rather than three, take <b>B</b>. It is '
        'the photograph and nothing else, it is genuinely quick, and it does '
        'not block D later.',
        '<b>What I cannot prove:</b> which of these converts better. There is '
        'no A/B test on this site, no heat map and no analytics on the '
        'booking page yet &mdash; the vitals beacon measures speed, not '
        'behaviour. Everything above is an argument from the numbers on the '
        'page and from how checkouts are built elsewhere, not from '
        'SWAT&rsquo;s own visitors. If that matters, the honest order is: '
        'ship one, put measurement on it, then argue.',
    ]),
    since=NEW))


# =====================================================================
# 43 — the date picker
# =====================================================================
ALL.append(dec(
    43,
    'Picking your dates',
    [('Question 1', ''), ('Crow', 'who'), ('1&ndash;2 days', ''),
     ('52 departures', 'big')],
    [ASK],
    [
        opt('Twelve months, then a list',
            ['A row of <b>twelve 44px month chips</b>, eleven of which are '
             '2027 and one of which says "Jan 2027".',
             'The chosen month drops <b>four to five 49px rows, two across</b> '
             '&mdash; "Mon, Jan 4 &ndash; Fri, Jan 8" and the price.',
             'Every row on the tour is the <b>same $1,999</b>, so the price '
             'column repeats the same number down the page and decides '
             'nothing.',
             'The question is <b>372px</b> tall and the whole year is <b>two '
             'clicks deep</b>: pick a month, then pick a date.'],
            '<p>This is what shipped yesterday, and it did fix the thing it '
            'was built to fix &mdash; the first version put all 52 departures '
            'in one grid in front of everything else.</p>'
            '<p>What it does not do is answer the question a customer is '
            'actually asking, which is "when am I free for five days". A list '
            'of Mondays with no shape to it makes them count the days '
            'themselves.</p>',
            cost='&mdash;', risk='No sense of the shape of the year',
            cls='now',
            mockup=m.mock(f.qregion(f.dates_now())
                          + m.ring(1, '.b-chips') + m.ring(2, '.b-drows'),
                          640, aw=980)),

        opt('A calendar, with the five days drawn on it',
            ['A real month grid. The departing Mondays are marked and priced '
             'in the cell.',
             '<b>The five days you would be away are drawn across the week as '
             'a bar</b>, so the trip is a shape on a calendar rather than two '
             'dates in a sentence.',
             'The month chips stay above it, so switching months is the same '
             'one click it is now.',
             'Costs height: the grid is <b>five 96px rows</b>, so the '
             'question goes from 372px to about <b>640px</b>.'],
            '<p>The one that answers "when am I free". Everybody can read a '
            'calendar, and the bar across the week says five days away, back '
            'on the Friday, without the customer doing arithmetic.</p>'
            '<p>Its weakness is real and worth saying: this tour leaves every '
            'Monday, so <b>a 35-cell grid holds four answers</b>. Without the '
            'bar it would be a mostly empty calendar, which is the emptiness '
            'complaint again. With the bar the grid is carrying the trip, not '
            'the gaps.</p>',
            cost='1&ndash;2 days',
            risk='31 cells for 4 answers on a weekly departure',
            cls='rec',
            mockup=m.mock(f.qregion(f.dates_cal())
                          + m.ring(1, '.b-cal') + m.ring(2, '.b-cal-bar'),
                          900, aw=980)),

        opt('One list, months stuck to the top',
            ['No month chips. <b>All 52 departures in one scroll</b>, grouped '
             'under month headings that stick as you pass them.',
             'Each row carries the two dates, the price and the seats left.',
             'The whole year is <b>zero clicks deep</b> &mdash; scrolling is '
             'the only interaction.',
             'The block is capped at about <b>330px</b> and scrolls inside '
             'itself, so the question stays shorter than it is today.'],
            '<p>The least clicking of the three, and the best of them if '
            'somebody is flexible and just wants to see everything. It is '
            'also the closest thing to what the page did before yesterday, '
            'which is the version that produced the complaint &mdash; the '
            'difference is that this one scrolls inside a box instead of '
            'pushing the rest of the page down.</p>'
            '<p>A scroll box inside a page is a known annoyance on a laptop '
            'trackpad, and on a phone it is worse.</p>',
            cost='1 day', risk='A scrolling box inside a scrolling page',
            mockup=m.mock(f.qregion(f.dates_list())
                          + m.ring(1, '.b-list'), 700, aw=980)),

        opt('Fewer rows, more on each',
            ['The chips stay. The dates go from <b>two columns to one</b>, '
             'and each row gets taller.',
             'A row now carries the dates, <b>"5 days, back on a Friday"</b>, '
             'the rate, and how many seats are left.',
             'Departures under about six seats carry a <b>Filling up</b> '
             'flag &mdash; the only thing on the page that separates one '
             'Monday from another.',
             'Each row ends in a <b>Choose</b> button, so the row reads as '
             'something you press.'],
            '<p>The cheap one, and the one that does most for the <i>feel</i> '
            'per hour spent. Right now four identical rows say four identical '
            'things; this makes each one carry a reason to pick it.</p>'
            '<p>It leans on the seat counts, which is the open question with '
            'Jason &mdash; if SWAT does not want "4 left" shown to customers, '
            'this option loses the flag and becomes a taller version of what '
            'ships now.</p>',
            cost='&frac12; day', risk='Depends on showing seat counts',
            mockup=m.mock(f.qregion(f.dates_fat())
                          + m.ring(1, '.b-frows') + m.ring(3, '.b-tag.warm'),
                          760, aw=980)),
    ],
    verdict([
        '<b>B</b> &mdash; the calendar, with the bar. It is the one that '
        'matches the question the customer is answering, and the bar across '
        'the week is what stops it being an empty grid on a tour that only '
        'leaves on Mondays.',
        'Worth pairing with <b>D</b>: the taller rows are half a day and they '
        'are what makes one Monday different from another. A calendar tells '
        'you when; a row with seats on it tells you which. They do not '
        'conflict &mdash; the calendar can drop the same fat row underneath '
        'once a month is chosen.',
        'The seat-count flag in D is still waiting on Jason and Ann. Until '
        'that is settled, build B on its own.',
    ]),
    since=NEW))


# =====================================================================
# 44 — the trip, while you are booking it
# =====================================================================
ALL.append(dec(
    44,
    'What you can see of the trip while you book it',
    [('Question 2 onward', ''), ('Crow', 'who'), ('&frac12;&ndash;1 day', ''),
     ('4 panels, folded', 'big')],
    [ASK],
    [
        opt('Folded away under the questions',
            ['Everything Softrip holds &mdash; the five days, the four '
             'hotels, the six park fees, the stargazing add-on &mdash; is '
             'behind <b>one closed row</b> reading "What the reservation '
             'system holds for this departure".',
             'It appears only <b>after</b> a date is picked, and it sits '
             '<b>below</b> all four questions.',
             'Opened, it is <b>four panels of reading</b> in the middle of a '
             'checkout.',
             'At rest, the only thing on screen naming the trip is the h1 and '
             'one line in the rail.'],
            '<p>This was a deliberate call when it was built &mdash; four '
            'panels of itinerary between a question and a price is worse than '
            'no itinerary. Closed and below is the safe version.</p>'
            '<p>The cost is that a customer answering question three has '
            'nothing on the screen telling them what they are buying except '
            'the tour name, and the tour name is the one thing they already '
            'knew.</p>',
            cost='&mdash;', risk='Nothing on screen but the name',
            cls='now',
            mockup=m.mock(f.region(f.flow(f.dates_now(), f.rail_now(True),
                                          open_step=2) + f.holdsrow())
                          + m.ring(1, '.b-holds') + m.ring(4, '.b-rail'),
                          760, aw=1440)),

        opt('In the panel beside you',
            ['The rail carries a <b>photograph of the trip</b>, then the two '
             'dates, the rate, the total and the seats.',
             'Under the money, <b>the five days with a frame each</b> &mdash; '
             'Zion, Canyonlands, Arches, Capitol Reef, Bryce, in order, from '
             'Softrip&rsquo;s own filed itinerary.',
             'One line under them says the four hotels are named on the '
             'confirmation &mdash; <b>towns, never hotel names</b>, because '
             'hotel contracts change.',
             'The folded row under the questions goes away; the fees and the '
             'add-on move into the review step, where they are money rather '
             'than reading.'],
            '<p>The trip is on the screen for all four questions, in the '
            'place the eye already goes for the price. Five thumbnails of the '
            'five parks is also the shortest possible answer to "what am I '
            'buying" &mdash; faster to read than any paragraph.</p>'
            '<p>This is the panel drawn in decision <a href="#d42">42D</a>. '
            'If 42 goes another way the panel still works, it just sits in '
            'the site chrome instead of a checkout shell.</p>',
            cost='1 day', risk='Depends on decision 42',
            cls='rec',
            mockup=m.mock(f.region(f.flow(f.dates_now(), f.rail_trip(),
                                          open_step=2))
                          + m.ring(1, '.b-rpic') + m.ring(2, '.b-rdays'),
                          900, aw=1440)),

        opt('Open, underneath, as a band',
            ['The folded row opens by default and becomes a <b>band under the '
             'questions</b> &mdash; the five days across, with a photograph '
             'on each.',
             'The rail stays exactly as it is: white, text, the running '
             'total.',
             'Adds roughly <b>300px</b> to the page.',
             'Visible only after a date is picked, as now.'],
            '<p>The version that needs no decision about the rail and no '
            'decision about the shell &mdash; it is one attribute and a row '
            'of photographs.</p>'
            '<p>It puts the itinerary back in the middle of the checkout, '
            'which is the thing that was deliberately avoided when it was '
            'built. It reads well and it is a longer page.</p>',
            cost='&frac12; day', risk='Puts reading back inside the checkout',
            mockup=m.mock(f.region(f.flow(f.dates_now(), f.rail_now(True),
                                          open_step=2)
                                   + f.holdsrow(open_=True))
                          + m.ring(1, '.b-holdsbody') + m.ring(2, '.b-rail'),
                          1000, aw=1440)),
    ],
    verdict([
        '<b>B</b> &mdash; put it in the panel. It costs no page height, it '
        'fills the emptiest thing on the page today, and it means the trip is '
        'in front of the customer for every one of the four questions rather '
        'than for none of them.',
        'It pairs with <b>42D</b>. If you take 42B instead &mdash; the '
        'photograph band with the site chrome kept &mdash; then take <b>C</b> '
        'here rather than B, because the band is already carrying the '
        'photograph and a second one in the rail beside it is one photograph '
        'too many.',
        'The hotels stay as towns on the confirmation and not as names on the '
        'page, which is the standing rule from operations: hotel contracts '
        'change and a named property on a checkout is a promise.',
    ]),
    since=NEW))
