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
    [('Home page, first screen', ''), ('Lance', 'who'), ('1&ndash;2 days', ''),
     ('redrawn', 'big')],
    [Q53, quote(['53 I still don&rsquo;t like, so mock some more ideas and '
                 'designs for this.'],
                'Crow, 28 September, on B, C and D &mdash; which is why they '
                'are retired below')],
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

        opt('Point at a place',
            ['The headline becomes a question: <b>&ldquo;Where do you want to '
             'go?&rdquo;</b>, with one line under it.',
             'Across the bottom of the photo, <b>six photographs of '
             'places</b>, each with how many trips go there: Utah 28, Arizona '
             '12, California 11, Wyoming and Yellowstone 8, Alaska 2, and day '
             'tours from Salt Lake City 12. One tap opens the tour finder with '
             'that place already picked.',
             'A seventh, orange tile: <b>All 74 tours</b>. That and the menu '
             'button are the only orange on the screen, and both say <b>Find '
             'your tour</b>.',
             'The search bar, the five quick-filter buttons and the floating '
             '&ldquo;Search trips&rdquo; button come off the first screen. The '
             'search bar lives on the tour finder, one tap away.'],
            '<p>The call to action is a picture, not a form. Nobody has to '
            'know what a &ldquo;departure city&rdquo; is or open a dropdown; '
            'they see Yellowstone and tap it. It is the same idea as '
            '&ldquo;I know the place&rdquo; further down the page, moved up '
            'to where everyone sees it.</p>'
            '<p>It shows six places out of sixteen. Anyone after Oregon or '
            'South Dakota goes through <b>All 74 tours</b>, which is why that '
            'tile is the orange one.</p>',
            cost='1 day', risk='Ten smaller destinations are a tap away',
            cls='rec',
            mockup=m.mock(h.screen2('places') + m.ring(1, '.q-top h1')
                          + m.ring(2, '.q-places .q-pt:nth-child(4)')
                          + m.ring(3, '.q-pt.all'), H53, aw=1440)),

        opt('Photo on the right, questions on the left',
            ['The first screen splits in two. On the left, on white: the new '
             'headline, one line, then <b>today&rsquo;s three search '
             'questions stacked</b> in a card, with one orange <b>Find your '
             'tour</b> button under them and the phone number under that.',
             'On the right, the photograph, the full height of the hero '
             '(<b>840px wide</b> instead of the whole screen).',
             'Quick-filter buttons and the floating button come off the first '
             'screen.'],
            '<p>The shape most booking sites use. It reads top to bottom like '
            'a form, so there is no question what to do: answer, then press '
            'the orange button.</p>'
            '<p>It is the only option here that makes the photo smaller. It '
            'keeps its height but loses about <b>40% of its width</b>, which '
            'goes against keeping the big photo that you and Jason chose.</p>',
            cost='1 day', risk='Photo loses 40% of its width',
            mockup=m.mock(h.screen2('split') + m.ring(1, '.q-stack')
                          + m.ring(2, '.q-ph'), H53, aw=1440)),

        opt('The next three departures, on the photo',
            ['The new headline, one line, and one orange <b>Find your '
             'tour</b> button, with &ldquo;or call&rdquo; beside it.',
             'On the right of the photo, a white card: <b>Next departures '
             'with seats</b>. Three real trips with their dates and prices: '
             'Mighty 5 from Salt Lake City on 29 November, Mighty 5 from Las '
             'Vegas on 30 November, Alaska&rsquo;s Northern Lights on 14 '
             'December.',
             'The search bar, quick-filter buttons and floating button come '
             'off the first screen.'],
            '<p>Two ways in: browse everything, or grab a trip that is '
            'leaving soon. The card shows people on the first screen that '
            'these are real trips with real dates, which nothing else up there '
            'does.</p>'
            '<p>It respects the two-month rule, so the soonest date it can '
            'ever show is about two months away. And it changes every week on '
            'its own, which is good for repeat visitors but means nobody '
            'chooses what is advertised there.</p>',
            cost='1 day', risk='Two things to do, not one',
            mockup=m.mock(h.screen2('soon') + m.ring(1, '.l-big')
                          + m.ring(2, '.q-soon'), H53, aw=1440)),

        opt('One box in the middle, and nothing else orange',
            ['Everything centred. The new headline, then <b>one wide search '
             'box</b> where you type anything: a park, a city, &ldquo;3 '
             'days&rdquo;. One orange <b>Find your tour</b> button inside '
             'it.',
             'Under it, five plain-text shortcuts (Zion, Grand Canyon, '
             'Yellowstone, Leaving from Las Vegas, Day tours) and the phone '
             'number.',
             'The menu button turns from orange to an outline, so the search '
             'button is the <b>only orange thing on the screen</b>.',
             'The three dropdowns, the quick-filter buttons and the floating '
             'button come off the first screen.'],
            '<p>The strictest answer to Lance&rsquo;s question: one thing to '
            'do, and it is obvious. It is how Google and Airbnb open.</p>'
            '<p>It is also the most work. Today&rsquo;s finder is three '
            'dropdowns; a box you can type anything into needs a search that '
            'understands &ldquo;Zion&rdquo; as a park and &ldquo;Las '
            'Vegas&rdquo; as a starting city. And an empty box asks people to '
            'already have an idea, which is what the shortcuts under it are '
            'for.</p>',
            cost='2 days', risk='Needs a proper type-anything search',
            mockup=m.mock(h.screen2('onebox') + m.ring(1, '.q-box')
                          + m.ring(2, '.l-hdcta'), H53, aw=1440)),
    ],
    verdict([
        '<b>E.</b> Point at a place. It is the most different from what you '
        'turned down, and it is the one that fits how people shop for trips '
        'like these: they know where they want to go before they know a tour '
        'name, a city or a length. A photo of Yellowstone with &ldquo;8 '
        'trips&rdquo; on it needs no explaining.',
        'Why I moved off C: B, C and D were really one design with different '
        'words on it. Same dark photo, same white headline top left, '
        'something orange underneath. These four each change the shape of the '
        'screen instead.',
        'If you want the single clearest answer to Lance&rsquo;s question, '
        'it is <b>H</b>: one box, one orange button. It costs a day more, '
        'because the search has to understand what people type.',
        'In every one of them the menu button and the main button say the '
        'same words, <b>Find your tour</b>, and the floating &ldquo;Search '
        'trips&rdquo; button stays hidden until you scroll past the photo. '
        'The headline wording is still my draft for Lance or Jason to approve. '
        'None of them makes the photo shorter, and only F makes it narrower.',
    ]),
    since=('Redrawn', '28 Sep &middot; round two'), cols=2))
