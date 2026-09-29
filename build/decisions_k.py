"""Round ten, decision 73: picking dates by season.

Matt's note, passed on by Crow. The count is in mocks_k.py. The fact that
shaped the options: the tour page already HAS seasons — "This trip by season",
the fourth section — but it sits 6,791px above the dates it counts, and its
"22 autumn departures" link lands on the 2026 tab whatever you tapped. So the
question is less "add seasons" than "let the seasons and the dates meet".

Every option reuses the 67D month card exactly as it ships, so the only thing
that differs between panels is how you reach a month.
"""

import mocks as m
import mocks_k as k
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New option E', '29 Sep')
H = 900

Q = quote(
    ['Matt had some good feedback about the departures section for displaying '
     'tours. He was saying we should try and utilize the by season for these '
     'selection. Could you mock me a couple designs with this idea.'],
    'Crow, 29 September, passing on Matt&rsquo;s note')

Q2 = quote(
    ['C, the only thing I just don&rsquo;t like is potentially saying the best '
     'month to come, so maybe we should just remove that. Maybe you can toggle '
     'on 2026 and 2027 if you want. I just don&rsquo;t want to deter people from '
     'booking in certain months.',
     'Actually D kind of looks pretty good too, because it just feels more '
     'organized, like you&rsquo;re making a better use of space. So maybe somehow '
     'we can combine C and D. I want you to make that as another option I can '
     'look at before we do anything.'],
    'Crow, 29 September, after looking at A to D')


def mk(html, *rings):
    return m.mock(html + ''.join(m.ring(n, s) for n, s in rings), H, aw=1440)


ALL.append(dec(
    73, 'Picking dates by season',
    [('Every tour page with dates', ''), ('Matt, via Crow', 'who'),
     ('&frac12;&ndash;1 day', ''),
     ('The seasons sit 6,800px above the dates', 'big')],
    [Q, Q2],
    [
        opt('Year tabs, as now',
            ['Two tabs, <b>2026</b> and <b>2027</b>. The page opens on 2026: '
             'three months, and 7 of its 13 dates are sold out.',
             'Only 2027 dates show a price. 2026 gets one &ldquo;from '
             '$1,999&rdquo; line.',
             'The page already talks in seasons: <b>&ldquo;This trip by '
             'season&rdquo;</b> is the fourth section, <b>6,800px above</b> '
             'the dates. Its &ldquo;22 autumn departures&rdquo; link drops you '
             'here on the 2026 tab, whichever season you tapped.'],
            '<p>The season words and the dates never meet. Someone who reads '
            '&ldquo;Autumn: the best month to come&rdquo; has to scroll about '
            'seven screens and then work out for themselves which months are '
            'autumn.</p>',
            cls='now',
            mockup=mk(k.now(), (1, '.k10-ytabs'), (2, '.k10-line'),
                      (3, '.k10-mc li:nth-child(4)'))),

        opt('Seasons instead of years',
            ['<b>Six tabs, one per season</b>, in date order: Autumn 2026 '
             'through Winter 2027&ndash;28. Each says its months and how many '
             'dates are open.',
             'Under the tabs, that season&rsquo;s line from the band (&ldquo;the '
             'best month to come&rdquo;) and its lowest price.',
             'The month cards you approved in 67, three across, because a season '
             'is three months.'],
            '<p>The closest thing to what Matt said: the year tabs become season '
            'tabs and nothing else moves. Drawn with Autumn 2027 tapped, which '
            'shows the price dropping from $2,199 to $1,999 in the middle of '
            'October.</p>',
            cost='about &frac12; day',
            risk='Six tabs is a lot on a phone: they become a row you swipe, and '
                 'the later seasons start off screen. Winter runs over New Year, '
                 'so &ldquo;Winter 2026&ndash;27&rdquo; is a label some people '
                 'will read twice.',
            mockup=mk(k.opt_tabs(), (1, '.k10-stabs'), (2, '.k10-note'),
                      (3, '.k10-grid'))),

        opt('The season cards pick the dates',
            ['The four season cards from <b>&ldquo;This trip by season&rdquo; '
             'move down into Departures and become the buttons</b>. Tap one and '
             'its dates appear underneath.',
             'Each card says how many dates are open and the lowest price. The '
             'page opens on the next season with a seat, autumn today.',
             'Both years of a season show together, each under its own heading: '
             'Autumn 2026, then Autumn 2027.',
             'The separate band near the top goes, so the seasons are not said '
             'twice. The page gets about <b>400px shorter on a laptop</b> and '
             '<b>1,100px on a phone</b>.'],
            '<p>Matt&rsquo;s idea taken all the way: the season is how you choose, '
            'and the words that sell a quieter season (Lance&rsquo;s point when '
            'the band was first built, decision 22) sit exactly where the choice '
            'is made.</p>',
            cost='about 1 day',
            risk='The season words leave the top of the page, where they sit next '
                 'to the Overview today. Someone who already knows they want '
                 '&ldquo;the week of May 10&rdquo; has one extra tap.',
            mockup=mk(k.opt_cards(), (1, '.k10-scs'), (2, '.k10-sc.on .ct'),
                      (3, '.k10-yh'))),

        opt('Every season on one screen',
            ['<b>No tabs at all.</b> Four rows, one per season, soonest first, '
             'each with its heading and lowest price.',
             'Every date is a small button with its price. Tap it to book. The '
             '$2,199 weeks print in orange.',
             'Both years of a season share its row, split by a small year '
             'label.'],
            '<p>Nothing to open and nothing hidden: you see which seasons are '
            'filling up and which are wide open in one look.</p>',
            cost='about &frac12;&ndash;1 day',
            risk='All 65 dates at once is a long block, about a laptop screen '
                 'here, and a tour with more dates makes it longer. It is close to '
                 '&ldquo;every date on one screen&rdquo; in 67, which you passed '
                 'over for the year tabs.',
            mockup=mk(k.opt_rows(), (1, ".k10-sr[data-s='Autumn'] .k10-sl"),
                      (2, '.k10-ch.pk'), (3, '.k10-yl:not(:first-child)'))),

        opt('Season cards over every date',
            ['<b>C&rsquo;s four season cards are the buttons</b>, smaller, each '
             'with its months, how many dates are open and the lowest price. '
             'No &ldquo;best month to come&rdquo; or any other ranking.',
             'Under the cards, one plain line about that season and what to '
             'bring. Every season gets the same kind of line, so none reads as '
             'the wrong time to go.',
             '<b>D&rsquo;s rows of date buttons</b> for the season you tapped, one '
             'row per year: Autumn 2026, then Autumn 2027. Every date shows its '
             'price, all in one color. Tap a date to book it.',
             'A small <b>Both years / 2026 / 2027</b> switch on the right, for '
             'someone who already knows the year.'],
            '<p>C and D put together, as you asked: the season boxes do the '
            'choosing, and the dates underneath take the tight rows from D '
            'instead of the tall month boxes. Autumn here is two rows where C '
            'needs two full grids of month boxes.</p>',
            cost='about 1 day',
            risk='The month boxes you approved this morning go away on this '
                 'section and become small date buttons, so Book and Waitlist '
                 'move inside the button. The year switch is only worth having on '
                 'a tour with a lot of dates; on most tours I would hide it.',
            cls='rec',
            mockup=mk(k.opt_mix(), (1, '.k10-sc2.on'), (2, '.k10-even'),
                      (3, '.k10-sr2:nth-child(2) .k10-chs'), (4, '.k10-yt'))),
    ],
    verdict([
        '<b>E, the season cards over every date.</b> It is the mix of C and D '
        'you asked for. The seasons do the choosing, which is Matt&rsquo;s idea, '
        'and the dates sit in D&rsquo;s tight rows, so the section comes out '
        'about 40% shorter than C with every price showing.',
        '<b>No season is ranked.</b> E drops &ldquo;the best month to come&rdquo;, '
        'and the pricier weeks are no longer picked out in orange. Each season '
        'just says what the weather is like and what to bring.',
        '<b>Worth knowing: the live site already ranks seasons.</b> The '
        '&ldquo;This trip by season&rdquo; section near the top of every tour '
        'page says &ldquo;The best month to come&rdquo; for autumn, &ldquo;Hot, '
        'and we mean it&rdquo; for summer and &ldquo;Empty, and often '
        'snowed&rdquo; for winter. On the mountain tours it calls autumn '
        '&ldquo;our own pick of the year&rdquo;. Whichever letter you choose, '
        'I would rewrite those lines the same even way. That is an hour.',
        '<b>C still stands if you want to keep the month boxes</b> you approved '
        'this morning. E trades them for the smaller date buttons.',
        '<b>Two things to know.</b> Seasons are the calendar kind the page '
        'already uses, so December counts as winter and a winter trip can run '
        'over New Year. A tour that only runs in one season skips the cards and '
        'shows its dates straight away.',
    ]),
    since=NEW, cols=2))
