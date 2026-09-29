"""Round nine, decisions 68-72: the empty right-hand side on a desktop screen.

Numbered from 68 because 67 is the date picker, and a number said out loud has
to mean one thing across every link. The count is in mocks_j.py; every panel
is drawn at 1920 wide, the screen in Crow's screenshot.
"""

import mocks as m
import mocks_j as j
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New', '29 Sep')
AW = j.AW

Q = quote(
    ['On the destinations page, see my screenshot, there is just a lot of wasted '
     'white space on the right side when on my computer, seems like a waste. How '
     'can we fix this?',
     'I want you to review all the different tabs to see if this issue pops up '
     'anywhere else.'],
    'Crow, 29 September, with a screenshot of the Arches and Canyonlands page')


def mk(html, h, *rings):
    r = ''.join(m.ring(n, s) for n, s in rings)
    # A one-screen drawing is a window with overflow hidden. Its rings go
    # INSIDE it, so a ring on a grid that runs past the fold is clipped with
    # the grid; outside, the ring's box stretched the canvas to 2,186px.
    if html.startswith('<div class="w9 w9-win">'):
        return m.mock(html[:-len('</div>')] + r + '</div>', h, aw=AW)
    return m.mock(html + r, h, aw=AW)


# ------------------------------------------------------------------------ 68
ALL.append(dec(
    68, 'The words at the top of a destination page',
    [('38 destination pages', ''), ('Crow', 'who'), ('&frac12;&ndash;1 day', ''),
     ('936px of blank beside the words', 'big')],
    [Q],
    [
        opt('The words alone, as now',
            ['The words are <b>680px wide</b> in a <b>1,616px</b> page, so '
             '<b>936px beside them is blank</b> on your screen (650px on a laptop).',
             'Nothing to buy is on the first screen. The trips start below the '
             'words, about <b>1,550px down</b> on a typical page.'],
            '<p>Same on all 38 destination pages. It is worst where the words are '
            'longest: on Hawaii the blank side runs <b>4,000px</b>, about four '
            'screens. The same block of words, with the same gap, closes every '
            'trip-style page too.</p>',
            cls='now',
            mockup=mk(j.dest_now(), 1080, (1, '.w9-intro .w9-words'))),

        opt('A trip panel beside the words',
            ['A panel on the right, where the booking panel sits on a tour page: '
             '<b>how many trips go here, the lowest price, and one button</b> to them.',
             'The &ldquo;Departing from&rdquo; towns and the hikes link move up '
             'into it. They are two thin strips near the bottom today.',
             'The words do not change.'],
            '<p>Same shape as a tour page: words on the left, a panel on the right '
            'that follows you down. On Hawaii it follows you down the long '
            'words, so the side is never empty. Every number in it comes from the '
            'trips the page already lists.</p>',
            cost='&frac12; day for all 38 pages; the same panel can close the trip-style pages',
            risk='Small. On a phone the panel sits under the words, one box longer. The four hub pages '
                 '(Utah, Nevada, New Mexico, National Parks) list places, not trips, so they keep the words alone.',
            cls='rec',
            mockup=mk(j.dest_panel(), 1080, (1, '.w9-panel'), (2, '.w9-panel .row'),
                      (3, '.w9-intro .w9-words'))),

        opt('Photos beside the words',
            ['<b>Three photos</b> from the page&rsquo;s own gallery move up beside '
             'the words: one wide, two below it.',
             'The gallery further down keeps the rest.'],
            '<p>Fills the side with the thing people come for, the place itself. '
            'Nothing new to write or maintain.</p>',
            cost='&frac12; day',
            risk='Pretty, but it sells the place, not the trips, which are still '
                 '1,550px down. Two pages (Washington and the National Parks hub) '
                 'have fewer than three photos and would keep the words alone.',
            mockup=mk(j.dest_photos(), 1080, (1, '.w9-mosaic'))),

        opt('Trips first, words underneath',
            ['The <b>trips move up</b> to straight under the search bar, four across.',
             'The words go below the trips, with <b>C&rsquo;s photos</b> beside them.'],
            '<p>The first screen is all trips. That suits people who arrive '
            'knowing where they want to go and want to see what to book.</p>',
            cost='&frac12; day',
            risk='The largest change. The words are the page&rsquo;s search '
                 'copy, and Google still reads them wherever they sit, but a reader '
                 'who wanted the introduction now scrolls past 11 cards to reach it.',
            mockup=mk(j.dest_trips_first(), 1080, (1, '.w9-sec .w9-grid'))),
    ],
    verdict([
        '<b>B, the trip panel.</b> It fills the empty side with the one thing '
        'this page is for: how many trips go to Arches, from what price, and a '
        'button to them, level with the words and not 1,550px down. It is the '
        'same shape you already approved on the tour pages, so the site gets '
        'more consistent, not less. It also absorbs two thin strips from lower '
        'down (decision 69).',
        '<b>D if you think people land here ready to book.</b> It is the bigger '
        'change and I would try B first.',
        'Whatever you pick carries to the <b>words at the bottom of the 9 '
        'trip-style pages</b> (&ldquo;What a rail &amp; cruise trip is&rdquo;), '
        'which is the same block with the same gap.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 69
ALL.append(dec(
    69, 'The bottom half of a destination page',
    [('38 destination pages', ''), ('Found in the review', 'who'), ('2&ndash;3 hours', ''),
     ('3 of 4 rows half empty', 'big')],
    [],
    [
        opt('Half-empty rows, as now',
            ['The photo gallery&rsquo;s last row is <b>two photos and two blank slots</b>.',
             '&ldquo;Plan your walking&rdquo; is <b>one card on a row of three</b>.',
             '&ldquo;From the journal&rdquo; is <b>two cards on a row of three</b>.'],
            '<p>Arches, drawn here. Across the 38 pages: <b>34 galleries</b> end on a '
            'part-empty row, <b>22 of the 26</b> pages with journal stories show one '
            'or two on a row of three, and all <b>6</b> pages with a hikes row show '
            'one card.</p>',
            cls='now',
            mockup=mk(j.lower('now'), 2200, (1, '.w9-gal .f:last-child'),
                      (2, '.hk .w9-tiles'),
                      (3, '.jr .w9-tiles'))),

        opt('Fill every row',
            ['The last two photos <b>each take half the row</b>, so the gallery '
             'ends square. No photo is dropped.',
             'The hike and the journal stories share <b>one row, &ldquo;Keep '
             'exploring&rdquo;</b>, with a small label on each card saying which '
             'is which.'],
            '<p>Same photos, same links, one heading fewer, and no row ends '
            'early. The rule is general: however many photos a page has, the '
            'last row stretches to fill.</p>',
            cost='2&ndash;3 hours',
            risk='A page with a single photo shows it full width. That is correct, just large.',
            cls='rec',
            mockup=mk(j.lower('fill'), 2200, (1, '.w9-gal .wide'), (2, '.w9-tiles'))),

        opt('One strip of photos',
            ['The gallery becomes <b>one row of four</b>, with &ldquo;See all 7 '
             'photos&rdquo; on the last one. It opens the viewer you already have.',
             'The same &ldquo;Keep exploring&rdquo; row as B.'],
            '<p>Much shorter. Arches ends about 600px sooner.</p>',
            cost='2&ndash;3 hours',
            risk='Hides most of the photographs behind a click, on the page whose job is to sell the place.',
            mockup=mk(j.lower('strip'), 2200, (1, '.w9-strip4'), (2, '.w9-tiles'))),
    ],
    verdict([
        '<b>B, fill every row.</b> Nothing is removed. Every row simply ends '
        'at the right-hand edge. C saves more height, but the photographs are '
        'the best thing on a destination page and I would not hide them to '
        'save a scroll.',
    ]),
    since=NEW, cols=3))


# ------------------------------------------------------------------------ 70
ALL.append(dec(
    70, 'Departing From: one trip per row',
    [('10 Departing From pages', ''), ('Found in the review', 'who'), ('2&ndash;3 hours', ''),
     ('3 trips on 3 rows', 'big')],
    [],
    [
        opt('A new row for each length, as now',
            ['Trips are grouped by length, and <b>each group starts a new row</b>. '
             'Bryce has three trips of three different lengths, so it shows '
             '<b>three rows of one card</b>.',
             'The first screen shows <b>one trip</b>. The page is <b>2,300px</b> '
             'before the footer.'],
            '<p>Worst page of the whole review: on average <b>68%</b> of a '
            'Departing From page has an empty right side. Las Vegas has six trips '
            'on three rows of 1, 2 and 3.</p>',
            cls='now',
            mockup=mk(j.bryce_now(), 3000, (1, '.g1 .w9-grid'), (2, '.g2 .w9-grid'))),

        opt('One row, shortest first',
            ['All the trips go in <b>one grid</b>, shortest first, as the page '
             'already promises.',
             'The length headings go. Each card already says <b>4 days, 7 days, '
             '12 days</b> in its corner.'],
            '<p>Bryce fits on one row and the page is about 1,000px shorter.</p>',
            cost='1 hour',
            risk='You lose the headings that let someone skip straight to a week-long trip.',
            mockup=mk(j.bryce_one_row(), 3000, (1, '.w9-grid'))),

        opt('One row, the lengths ride along',
            ['The same single grid as B.',
             'The length heading <b>stays</b>, as a small label above the '
             '<b>first card</b> of each length, so the groups are still easy to see.'],
            '<p>Keeps the idea behind the page (pick by how long you have) and '
            'loses the empty rows. Las Vegas goes from three rows to two.</p>',
            cost='2&ndash;3 hours',
            risk='Small. A long run of one length wraps onto the next row without a heading, which is fine.',
            cls='rec',
            mockup=mk(j.bryce_labels(), 3000, (1, '.w9-lab.run'), (2, '.w9-grid'))),

        opt('The words beside the trips',
            ['&ldquo;Starting from Bryce&rdquo; moves up into a <b>column on the '
             'left</b>, next to the trips.',
             'Trips go three across on the right, with C&rsquo;s length labels.'],
            '<p>Shortest page of the four, and nothing is blank on either side.</p>',
            cost='&frac12; day',
            risk='Puts the reading before the trips on a page people use to pick a trip.',
            mockup=mk(j.bryce_side(), 3000, (1, '.w9-side > div:first-child'))),
    ],
    verdict([
        '<b>C, one row with the lengths riding along.</b> It is B plus the '
        'thing the page was designed around: you can still see where the '
        'week-long trips start. Bryce&rsquo;s three trips land on one screen '
        'instead of three.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 71
ALL.append(dec(
    71, 'Journal stories and trail guides',
    [('44 stories + 13 guides', ''), ('Found in the review', 'who'), ('&frac12; day', ''),
     ('736px blank to the right', 'big')],
    [],
    [
        opt('Left of centre, as now',
            ['The words sit <b>left of centre</b> in a narrow box: 504px from the '
             'left edge, <b>736px of blank</b> on the right.',
             'The two trips the story is about come <b>at the very end</b>, as two '
             'small cards after 9,000px of reading.'],
            '<p>Narrow is right for reading, and nothing here should get wider. '
            'The problem is that the box is off-centre and nothing sits beside '
            'it. Same on all 13 trail guides.</p>',
            cls='now',
            mockup=mk(j.j_now(), 1080, (1, '.w9-art .w9-words'))),

        opt('Centre the words',
            ['The same column, <b>centred</b>, with equal space on both sides.'],
            '<p>Tidier, and how most magazine sites do it. The empty space is '
            'still there, only split in two.</p>',
            cost='1 hour',
            risk='Does not use the space, it just balances it.',
            mockup=mk(j.j_centre(), 1080, (1, '.w9-art .w9-words'))),

        opt('The trips beside the story',
            ['The words move to the left, as on a tour page.',
             'A panel on the right <b>follows you down</b>: the trips this story '
             'is about, with their price and a Check dates link, then '
             '&ldquo;Keep reading&rdquo;.',
             'Nothing is added. Both lists already exist at the bottom of the page.'],
            '<p>A reader six paragraphs into Alaska sees the Alaska trips and '
            'their prices beside the words, rather than after 9,000px.</p>',
            cost='&frac12; day for all 57 pages',
            risk='Small. A story with no linked trip shows only &ldquo;Keep '
                 'reading&rdquo;. On a phone the panel stays at the bottom, as today.',
            cls='rec',
            mockup=mk(j.j_story(), 1080, (1, '.w9-story .w9-words'), (2, '.w9-rail'))),

        opt('Photos go wide',
            ['Centred words as in B, but every photo in the story runs the <b>full '
             'width of the page</b>.'],
            '<p>The magazine look. The blank sides are broken up every few '
            'paragraphs by a big picture.</p>',
            cost='2&ndash;3 hours',
            risk='Photos supplied at blog size will look soft stretched to '
                 '1,920px. I have not checked each one.',
            mockup=mk(j.j_wide(), 1080, (1, '.w9-bleed'))),
    ],
    verdict([
        '<b>C, the trips beside the story.</b> It turns the blank side into '
        'the reason the journal exists: someone reading about Alaska can see '
        'the Alaska trips and what they cost without leaving the story. It '
        'uses the same layout as the tour pages and B on decision 68, so '
        'the three page types match.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 72
ALL.append(dec(
    72, 'The Hot Deals page',
    [('Hot Deals', ''), ('Found in the review', 'who'), ('2&ndash;3 hours', ''),
     ('1 deal, half the page blank', 'big')],
    [],
    [
        opt('One card on the left, as now',
            ['The only live deal is <b>one 798px card</b> on the left.',
             'The right half, <b>818px</b>, is blank.'],
            '<p>Today there is one deal (Canyons of the Escalante, October 25). '
            'The ticker at the top of every page shrinks the same way as deals '
            'expire, because nothing adds new ones.</p>',
            cls='now',
            mockup=mk(j.deals_now(), 1080, (1, '.w9-dealcard'))),

        opt('One wide row per deal',
            ['The deal spans the <b>full width</b>: photo left, details right.',
             'It gains the trip&rsquo;s length, group size and route, already on its tour card.'],
            '<p>With more deals, each one is a row. It works for 1 deal or 12.</p>',
            cost='2 hours',
            risk='With a single deal the page is still short. That is a content problem, not a layout one.',
            mockup=mk(j.deals_wide(), 1080, (1, '.w9-dealcard.wide'))),

        opt('The deal, plus how deals work',
            ['The card stays. Beside it goes <b>&ldquo;How hot deals work&rdquo;</b> '
             'in three lines taken from the page&rsquo;s own heading.',
             'Under that, a <b>newsletter sign-up</b>: the one the newsletter '
             'page already has.'],
            '<p>When there is only one deal, the page still collects an email '
            'from the person who came looking for a bargain.</p>',
            cost='2&ndash;3 hours',
            risk='Only worth it if deals actually go out on the newsletter. That is Matt&rsquo;s call.',
            cls='rec',
            mockup=mk(j.deals_side(), 1080, (1, '.w9-how'), (2, '.w9-sign'))),
    ],
    verdict([
        '<b>C, if the newsletter will carry deals.</b> A deals page with one '
        'deal is where a sign-up earns its place, because the visitor came for '
        'exactly that. <b>If not, B</b>, which is also the right shape once '
        'SWAT sends more deals.',
    ]),
    since=NEW, cols=2))
