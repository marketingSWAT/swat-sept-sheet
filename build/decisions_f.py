"""Decision 45 — the reviews page, round six.

Crow, 28 September, on the page the home page's reviews band links to:

    "on the customer reviews page, when you click on that from the home page to
    see all reviews, this entire page looks bad, its all just text, its hard to
    really get a good feeling for reviews, so how can we improve this page to
    make it look and feel better"

Counted first, as always (see `mocks_g.py`): a **19,664px** page, one 686px
column of **151 paragraphs**, four photographs that are 246px thumbnails blown
up to 686px and captioned with their filenames, and a hero drawn at 5.3x its
original. And the finding that changes the argument: the page carries **none**
of the 42 current reviews printed directly above the link that opens it. It is
the old archive, and its third paragraph praises Glenn.
"""

import mocks as m
import mocks_g as g
from sheetkit import opt, quote, verdict, dec

ALL = []

NEW = ('New', '28 Sep &middot; reviews page')

ASK = quote(
    ['On the customer reviews page, when you click on that from the home page '
     'to see all reviews, this entire page looks bad, it&rsquo;s all just '
     'text, it&rsquo;s hard to really get a good feeling for reviews. So how '
     'can we improve this page to make it look and feel better.'],
    'Crow, 28 September')

OPS = quote(
    ['I just want it to be the real ones, and I want it to be current &mdash; '
     'rather than however old these are. Like, Glenn hasn&rsquo;t guided for '
     'us for like six years.'],
    'SWAT operations, 16 September meeting &mdash; about these same archive '
    'reviews')

H = 2150

ALL.append(dec(
    45,
    'What the reviews page looks like',
    [('/guides/testimonials-and-reviews/', ''), ('Crow', 'who'),
     ('&frac12;&ndash;2 days', ''), ('19,664px of text', 'big')],
    [ASK, OPS],
    [
        opt('One long column of text, as now',
            ['The page is <b>19,664px</b> tall &mdash; about <b>22 screens</b> '
             'of your window &mdash; and it is one 686px column of '
             '<b>151 paragraphs</b> with no headings at all.',
             'The photo at the top is a <b>270px</b> original stretched to '
             'full width, which is why it looks smeared. The four photos '
             'further down are the same problem, and their captions are '
             'their <b>file names</b>: &ldquo;van&rdquo;, '
             '&ldquo;group-on-top&rdquo;.',
             'These are the old archive reviews. <b>The third and fourth '
             'praise Glenn</b>, and 62 of the 151 name a guide while almost '
             'none say which trip it was.',
             '<b>None of the 42 current reviews</b> Matt picked by trip '
             '&mdash; the three shown right above the link &mdash; are on '
             'this page at all.'],
            '<p>This is what the &ldquo;Read all 118 reviews&rdquo; link '
            'opens. It is the old site&rsquo;s testimonial page moved across '
            'word for word, which is the reason it exists and the reason it '
            'looks like this.</p>'
            '<p>The last point is the real problem. Someone reads three '
            'current reviews on the home page, clicks to see more, and lands '
            'on a different, older set that opens with a guide who left '
            'years ago.</p>',
            cost='&mdash;', risk='Old reviews, no trips, 22 screens of text',
            cls='now',
            mockup=m.mock(g.page_now() + m.ring(1, '.v-nhero')
                          + m.ring(2, '.v-nfig') + m.ring(3, '.v-nbody p:nth-child(3)'),
                          H, aw=1440)),

        opt('The same reviews, as cards',
            ['A navy band at the top with the <b>4.8 from 255 Google '
             'reviews</b> printed big, and a button to read them on Google.',
             'The 118 archive reviews become <b>cards in three columns</b>, '
             'each clamped at six lines with View more, like the tour pages.',
             'The smeared photos come out.',
             'Page falls from 19,664px to <b>about 8,500</b>.'],
            '<p>The quickest fix for the look. It stops being a wall of text '
            'and starts looking like a reviews page.</p>'
            '<p>It does nothing about what the reviews <i>are</i>. Glenn is '
            'still near the top, none of them say which trip, and the '
            'current reviews from the home page are still missing. It is a '
            'nicer frame round the thing operations asked us not to use.</p>',
            cost='&frac12; day', risk='Still the old reviews',
            mockup=m.mock(g.page_cards() + m.ring(1, '.v-bigscore')
                          + m.ring(2, '.v-masonry'), H, aw=1440)),

        opt('Current reviews, one row per trip',
            ['The same score band, with <b>one standout review</b> beside it '
             'in large type.',
             'A row of <b>trip buttons</b> under it, so someone who only '
             'cares about Alaska can jump straight there.',
             '<b>One row per trip, 13 rows.</b> The trip&rsquo;s own photo '
             'on the left with its name, how many reviews, and a link to the '
             'trip; its reviews as cards on the right.',
             'The old archive stays at the bottom, <b>folded shut</b>, so '
             'nothing that ranks today is lost. Page about <b>6,000px</b>.'],
            '<p>This uses the reviews operations actually wants shown: '
            'current, and each one tied to a trip. Every review sits next to '
            'a picture of the place it is about, which is what makes '
            'a reviews page <i>feel</i> like something rather than read like '
            'a document.</p>'
            '<p>It is also the only one of the three that sells. Every row '
            'ends in a link to the trip it praises, so the page does the job '
            'the home page band starts. All 42 reviews reach a page for the '
            'first time too; on the tour pages only three per trip show.</p>',
            cost='1 day', risk='Only as full as Matt&rsquo;s review docs',
            cls='rec',
            mockup=m.mock(g.page_bytrip() + m.ring(1, '.v-hq')
                          + m.ring(2, '.v-chips') + m.ring(3, '.v-trow')
                          + m.ring(4, '.v-archive'), H, aw=1440)),

        opt('A wall of photos and quotes',
            ['A <b>full-width photograph</b> with one review written across '
             'it in large type, and the Google score under it.',
             'The same trip buttons.',
             'Then a <b>four-column wall</b> that mixes trip photographs '
             'with review cards, like a magazine spread or a Pinterest '
             'board.',
             'Old archive folded at the bottom, as in the option to its left. '
             'Page about <b>5,000px</b>.'],
            '<p>The most striking of the three, and the one that looks most '
            'like a travel brand. It is the strongest first screen.</p>'
            '<p>It is harder to use. Reviews for one trip are scattered down '
            'the wall instead of sitting together, and eight of the 13 trips '
            'have three reviews or fewer, so some trips barely appear. It '
            'also costs twice as long to build.</p>',
            cost='2 days', risk='Harder to find one trip&rsquo;s reviews',
            mockup=m.mock(g.page_wall() + m.ring(1, '.v-whero')
                          + m.ring(2, '.v-wall'), H, aw=1440)),
    ],
    verdict([
        '<b>C.</b> The page does not only look bad, it is showing the wrong '
        'reviews. C fixes both at once: current reviews, grouped by trip, each '
        'next to a photo of the place and a link to book it.',
        'Three things I would do whichever you pick, because they are '
        'mistakes rather than design: take the blurry photos off, stop showing '
        'file names as captions, and make the home page link say how many '
        'reviews are actually on the page it opens.',
        'I would keep the old archive on the page, folded shut, rather than '
        'deleting it. That page ranks on Google today under the old address, '
        'and the words are what it ranks for. Folded, it stays readable to '
        'Google without being the first thing a customer sees.',
        '<b>What it depends on:</b> the page is only as full as Matt&rsquo;s '
        'review docs. Mighty 5 from Las Vegas, the trip SWAT sells most, has '
        'no reviews yet, so it would not get a row until he sends some. The '
        '&ldquo;Read them on Google&rdquo; button needs the link to '
        'SWAT&rsquo;s Google listing.',
    ]),
    since=NEW))
