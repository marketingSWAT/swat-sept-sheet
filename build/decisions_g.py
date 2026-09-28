"""Decisions 52 and 53, round seven: Lance's two notes of 28 September.

Numbered from 52 because the dashboard sheet (swat-dashboard-sheet) holds
46-51, and a number said out loud has to mean one thing across every link.

Both were counted before they were drawn (see `mocks_h.py`). The count moved
both arguments:

  52 - the day tours are not being kept off the shelf by the 60-day rule.
       Five of today's eight cards ARE day tours, as price-order filler,
       because none of the 15 has a dated departure for any rule to read. And
       the window itself has shrunk to four days (27-30 November), which is
       why only two cards on the row are there on merit.
  53 - the search button is on screen at 1440x900; Gmail's icons covered it
       in Lance's screenshot. The muddiness is 30 things to click and three
       orange buttons with three labels that all open the same finder.
"""

import mocks as m
import mocks_h as h
from sheetkit import opt, quote, verdict, dec

ALL = []

NEW = ('New', '28 Sep &middot; Lance')

Q52 = quote(
    ['Do we need to separate the Day Tours from our other multi-day tours in '
     'the Available to Book Now section? You&rsquo;ve done a great job, James, '
     'filtering tours two months out, but SLC Day Tours can be a 12-24-hour '
     'ramp and shouldn&rsquo;t be restricted to the 2-month-out booking '
     'window.'],
    'Lance Card, General Manager, by email, 28 September')

JASON60 = quote(
    ['We have contracts with hotels 30 days in advance that we have to get '
     'numbers in, so we actually need longer &mdash; we need like 60 days in '
     'advance on this page.'],
    'SWAT operations, 16 September meeting &mdash; where the two-month rule '
    'came from')

H52 = 1900

ALL.append(dec(
    52,
    'Day tours on the &ldquo;Bookable now&rdquo; row',
    [('Home page', ''), ('Lance', 'who'), ('&frac12;&ndash;1 day', ''),
     ('5 of 8 cards are filler', 'big')],
    [Q52, JASON60],
    [
        opt('One row for everything, as now',
            ['The row is meant to show trips leaving two months out. On '
             '28 September that window is <b>27 to 30 November, four '
             'days</b>, so only <b>2 of the 8 cards</b> are there because '
             'they leave in it.',
             'The other six are filler, cheapest first: <b>five day tours</b> '
             'and a $250 European Christmas-markets river cruise. None of '
             'them has a November date.',
             '<b>None of the 15 day tours has a single date</b> in the '
             'calendar, and none can be booked online. Every one says '
             '&ldquo;Ask about dates&rdquo; or &ldquo;Request a quote&rdquo;.'],
            '<p>So Lance is right that the row mixes the two, but not quite '
            'for the reason he thinks. The two-month rule isn&rsquo;t keeping '
            'day tours off; they are on it already, as filler, because they '
            'are the cheapest things in the catalogue. What the row never '
            'tells anyone is that a day tour can go tomorrow.</p>'
            '<p>The window also runs &ldquo;two months out to the end of '
            'that month&rdquo;, so near the end of every month it shrinks to '
            'a few days and the row fills up with whatever is cheapest.</p>',
            cost='&mdash;', risk='Row is mostly filler at every month end',
            cls='now',
            mockup=m.mock(h.shelf_now() + m.ring(1, '.l-line')
                          + m.ring(2, '.l-cell:nth-child(3)')
                          + m.ring(3, '.l-cell:nth-child(8)'), H52, aw=1440)),

        opt('Two rows: multi-day, then day tours',
            ['The multi-day row keeps the <b>two-month rule</b>, but looks '
             '<b>two to four months out</b> instead of to the end of one '
             'month. That holds <b>seven trips with real dates</b> today, '
             'from Mighty 5 on November 29 to Hawaii in January.',
             'It shows <b>six</b> of them, in two clean rows. No day tours '
             'and no filler.',
             'Under it, a row of its own: <b>Day tours from Salt Lake '
             'City</b>, four smaller cards, each saying it can go at short '
             'notice, and a link to all 15.'],
            '<p>This answers Lance&rsquo;s question with a yes. Day tours '
            'get their own row and their own rule, and the two-month rule '
            'goes back to doing the one job it was made for: protecting the '
            'hotel contracts on multi-day trips.</p>'
            '<p>The day tour cards are smaller on purpose. They are $110 '
            'trips beside $3,000 ones, and at the same size they read as the '
            'same kind of decision. It costs two of the eight multi-day cards '
            'that were asked for on 16 September.</p>',
            cost='&frac12; day', risk='Six multi-day cards, not eight',
            cls='rec',
            mockup=m.mock(h.shelf_rows() + m.ring(1, '.l-line')
                          + m.ring(2, '.l-dated')
                          + m.ring(3, '.l-dayrow'), H52, aw=1440)),

        opt('One row with two tabs',
            ['The same fixed window and the same six dated multi-day '
             'trips.',
             '<b>Two tabs</b> over the row: &ldquo;Multi-day trips&rdquo; and '
             '&ldquo;Day tours&rdquo;. Multi-day is open when the page '
             'loads; a click swaps the row to day tours.'],
            '<p>The tidiest page, and the row stays the height it is.</p>'
            '<p>The day tours are behind a click, though, and most people '
            'never click a tab they did not come for. The day-tripper Lance '
            'is worried about, someone in Salt Lake this week, has to '
            'notice a small tab to find out we can take them tomorrow.</p>',
            cost='&frac12; day', risk='Day tours hidden until clicked',
            mockup=m.mock(h.shelf_tabs() + m.ring(1, '.l-tabs'), H52, aw=1440)),

        opt('Multi-day row, plus one strip for day tours',
            ['The same fixed window and the same six dated multi-day '
             'trips.',
             'Day tours leave the row entirely. In their place, <b>one '
             'shallow strip</b>: four small photos, &ldquo;In Salt Lake City '
             'for a day?&rdquo;, and a button to the day-tour page.'],
            '<p>The cheapest and the shortest page. The strip is a signpost '
            'rather than a shelf.</p>'
            '<p>It shows no individual day tour, no price and no name, so '
            'someone has to click through before they see anything they can '
            'book. For a product sold on &ldquo;we can go tomorrow&rdquo;, '
            'that is one step more than it needs.</p>',
            cost='2 hours', risk='No day tour named on the home page',
            mockup=m.mock(h.shelf_strip() + m.ring(1, '.l-strip'), H52, aw=1440)),
    ],
    verdict([
        '<b>B.</b> Two rows, each with its own rule. The multi-day row keeps '
        'the two-month floor that protects the hotel contracts, and day tours '
        'get a row that says what is special about them: they can go at short '
        'notice.',
        'Two things I would fix whichever you pick. First, the multi-day row '
        'should look two to four months out rather than to the end of one '
        'month. As it is, near the end of every month the row runs out of '
        'real trips and fills up with the cheapest things in the catalogue, '
        'which today means a European river cruise. Second, the heading '
        'should stop naming a single month.',
        '<b>What I need from Lance before building:</b> the real cutoff for '
        'a day tour. Is it 12 hours or 24? The cards will say whatever he '
        'says. It is worth him knowing that no day tour can be booked on the '
        'website yet. All 15 go through &ldquo;Ask about dates&rdquo;, and '
        'none has a booking page in Softrip. So &ldquo;tomorrow&rdquo; today '
        'means someone at SWAT answering a form or a phone call fast. If '
        'Jason sets the day tours up in Softrip, the row could book them '
        'directly.',
    ]),
    since=NEW))


Q53 = quote(
    ['I just realized that our CTA is a little muddy. What is our CTA for the '
     'homepage?'],
    'Lance Card, General Manager, by email, 28 September')

H53 = 900

ALL.append(dec(
    53,
    'What the home page asks you to do',
    [('Home page, first screen', ''), ('Lance', 'who'), ('&frac12; day', ''),
     ('3 orange buttons, 3 labels', 'big')],
    [Q53],
    [
        opt('Welcome line and a search bar, as now',
            ['The words on the photo describe the company: '
             '&ldquo;Welcome To Southwest Adventure Tours&rdquo;, then '
             '&ldquo;As a Destination Management Company and Tour '
             'Operator&hellip;&rdquo;. They do not ask the visitor to do '
             'anything.',
             'The one real action is the search bar across the bottom edge of '
             'the photo. It <b>is on screen</b> on a laptop. In Lance&rsquo;s '
             'screenshot Gmail&rsquo;s download icons sit on top of its '
             'button.',
             '<b>Three orange buttons</b> with three different labels: '
             '&ldquo;Find a Trip&rdquo;, &ldquo;Search 74 tours&rdquo; and '
             '&ldquo;Search trips&rdquo;. All three open the same tour '
             'finder.',
             '<b>30 things to click</b> on the first screen, counting the '
             'menu, the deals and the five quick-filter buttons.'],
            '<p>That is the muddiness Lance is pointing at. The call to '
            'action is there, but it has three names and it sits below a '
            'paragraph that reads like an About page.</p>',
            cost='&mdash;', risk='No clear first step',
            cls='now',
            mockup=m.mock(h.screen('now') + m.ring(1, '.l-htx h1')
                          + m.ring(2, '.l-sgo') + m.ring(3, '.l-hdcta')
                          + m.ring(4, '.l-pill'), H53, aw=1440)),

        opt('One big button on the photo',
            ['The welcome line and company paragraph come off the photo. In '
             'their place: <b>one line that says what SWAT sells</b>, and '
             'one short line under it.',
             'A big orange <b>Find your tour</b> button, with &ldquo;or call '
             '800-970-5864&rdquo; beside it.',
             'The search bar stays where it is.'],
            '<p>The most familiar shape: a headline and a button. It gives '
            'the photo a job.</p>'
            '<p>It also adds a <b>fourth</b> orange button to the screen, a '
            'hand-width above the search bar, and both do the same thing. '
            'Drawing it is what showed me that. I had suggested this in '
            'chat, and I now think it makes the muddiness worse rather than '
            'better.</p>',
            cost='2 hours', risk='Button and search do the same job',
            mockup=m.mock(h.screen('button') + m.ring(1, '.l-htx h1')
                          + m.ring(2, '.l-ctas'), H53, aw=1440)),

        opt('The search bar is the call to action',
            ['The same new headline and line.',
             'The <b>search bar moves up into the photo</b>, right under the '
             'headline, and its button says <b>Find your tour</b>. The '
             'quick-filter buttons sit under it on the photo.',
             '&ldquo;Rather talk it through? Call 800-970-5864&rdquo; under '
             'that, for the people who would rather phone.',
             'The button in the menu bar says <b>Find your tour</b> too, and '
             'the floating &ldquo;Search trips&rdquo; button stays hidden '
             'until the search bar has scrolled off. <b>One name, two orange '
             'buttons</b> instead of three.'],
            '<p>One action, said one way everywhere. The search bar was '
            'already the right call to action: SWAT&rsquo;s tour names are '
            'hard to guess, so letting someone pick a place, a city and a '
            'length is the most useful first step there is. It only needed '
            'to be the thing the photo points at, not something tucked '
            'under its bottom edge.</p>'
            '<p>The photo stays exactly as big as it is now.</p>',
            cost='&frac12; day', risk='Headline wording needs SWAT&rsquo;s OK',
            cls='rec',
            mockup=m.mock(h.screen('search') + m.ring(1, '.l-htx h1')
                          + m.ring(2, '.l-search.up') + m.ring(3, '.l-call')
                          + m.ring(4, '.l-hdcta'), H53, aw=1440)),

        opt('Two buttons: find a tour, or build your own',
            ['The same new headline and line.',
             'Two buttons on the photo: orange <b>Find your tour</b> and an '
             'outlined <b>Build your own trip</b>.',
             'The search bar stays where it is.'],
            '<p>Speaks to both kinds of customer on the first screen: '
            'someone shopping the catalogue, and a group that wants a custom '
            'trip, which is a line of business that is otherwise easy to '
            'miss.</p>'
            '<p>It is two calls to action, not one, which is the opposite of '
            'what Lance asked for. And the search bar is still a third way '
            'in, right under them.</p>',
            cost='2 hours', risk='Two answers to &ldquo;what is our CTA&rdquo;',
            mockup=m.mock(h.screen('two') + m.ring(1, '.l-ctas'), H53, aw=1440)),
    ],
    verdict([
        '<b>C.</b> The answer to Lance&rsquo;s question is &ldquo;Find your '
        'tour&rdquo;, and C makes that the only thing the first screen asks. '
        'The search bar moves up into the photo, takes that name, and every '
        'other orange button on the page uses the same words.',
        'I have changed my mind since my first reply. In chat I suggested a '
        'big button on the photo, which is B. Drawn out, B puts a fourth '
        'orange button a hand-width above a search bar that does the same '
        'thing, and that is the muddiness Lance is complaining about.',
        'The headline and the line under it are my draft wording, built only '
        'from facts already on the site. Lance or Jason should approve or '
        'replace them. The company description (&ldquo;Destination '
        'Management Company&rdquo;) moves further down the page rather than '
        'being deleted.',
        'None of this makes the photo smaller. That was settled when Lance '
        'asked for a shorter hero and you kept it big.',
    ]),
    since=NEW))
