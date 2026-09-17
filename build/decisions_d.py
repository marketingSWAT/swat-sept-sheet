"""Decisions 40 and 41 — round three of the 16 September notes.

Both come from Crow's walkthrough of the *built* round-two work on the evening
of 16 September. Everything else in that walkthrough he passed: "looks fine,
looks good, looks good", "go to please notes great", "the film slot looks good
… yeah that's sick". These are the two he stopped on.

40 reopens decision 33, which is answered and shipped: B gave the map the full
width and the map is now too tall to see the answers under it on his own
screen. 41 replaces decision 36, which never got a letter — none of E, F, G or
H put the cards where he has now said twice that he wants them.

Every "Now" panel is the deployed staging build measured at **1440x900** on
16 September 2026 — see the header of `mocks_d.py` for the harvest.
"""

import mocks as m
import mocks_c as c
import mocks_d as d
import mocks_e as e
from sheetkit import opt, quote, verdict, dec

ALL = []

NEW = ('New', '16 Sep &middot; round 3')


# =====================================================================
# 40 — the map, and how much of the question fits on a screen
# =====================================================================
#
# Authored at 1440, not 1200. The complaint is about what fits in Crow's
# window, so the canvas has to be that window: 73px of sticky header, the
# question scrolled to sit under it, and a dashed line where the screen stops.

ALL.append(dec(
    40,
    'The map, and what fits on one screen',
    [('/custom-tours/', ''), ('Crow', 'who'), ('&frac12;&ndash;2 days', ''),
     ('955px question', 'big')],
    [quote(['The map is like slightly too big where I can&rsquo;t see all the '
            'options below. So if we can kind of shrink that a little bit so '
            'you&rsquo;re able to get this in one concise view.',
            'Or potentially maybe we put the selections on the right hand '
            'side, so you have the interactive map and then you have the '
            'options on the right. I think we could utilise space better '
            'doing it this way.'],
           'Crow, 16 September, walking the built page'),
     quote(['I love the interactive map, I think that looks great.'],
           'Crow, earlier the same day &mdash; which is the constraint on '
           'all of this')],
    [
        opt('The map at full width, as now',
            ['The map is <b>1,319&times;687</b> &mdash; <b>72% of the '
             'question</b>, which is 955px tall in total.',
             'The sixteen places sit under it, <b>four across in four 48px '
             'rows</b>, from y=1,622 to y=1,838.',
             'A 900px window shows <b>827px</b> of page under the 73px sticky '
             'header. Scroll the question to the top of that and the screen '
             'ends at y=1,711.',
             '<b>Two of the four rows are below the fold</b> and the second is '
             'cut in half &mdash; so you see <b>eight and a half of the '
             'sixteen places</b> without scrolling again.'],
            '<p>This is decision <a href="#d33">33B</a>, built exactly as '
            'drawn. It did what it promised &mdash; the map went from '
            '737&times;384 to full width and the state names fit &mdash; and '
            'the cost is the thing you are now looking at: the answers went '
            'off the bottom of the screen.</p>',
            cost='&mdash;', risk='Half the places are never seen',
            cls='now',
            mockup=m.mock(d.scrolled(d.q1('now')) + m.ring(1, '.m-map')
                          + m.ring(4, '.m-cells'), 1085, aw=1440)),
        opt('The map gets shorter',
            ['The map is capped at <b>998&times;520</b> instead of '
             '1,319&times;687, and centred. Nothing else moves.',
             '<b>Shorter means narrower.</b> The map is a fixed 960&times;500 '
             'ratio and its outline fills that, so height cannot come off it '
             'without width coming with it &mdash; 520 tall <i>is</i> 998 '
             'wide.',
             '520 is the <b>tallest it can be</b> and still fit: the question '
             'is the map plus 267px of legend, gap and four rows of places, '
             'and the screen is 827.',
             'The places stay <b>four across</b>, in the same place, in the '
             'same order. The question comes to <b>787px</b>, 40px inside the '
             'screen.'],
            '<p>The literal reading of what you said, and by a distance the '
            'cheapest &mdash; it is a max-width on one element.</p>'
            '<p>What it costs: about a quarter of the map&rsquo;s width and a '
            'quarter of its height. It is still <b>83% more map than you had '
            'before decision 33</b> (737&times;384), so it is not a step '
            'backwards &mdash; but the full-bleed map is the thing you said '
            'you loved, and this is the option that keeps its shape and '
            'reduces it.</p>',
            cost='&frac12; day', risk='The map loses a quarter in each direction',
            mockup=m.mock(d.scrolled(d.q1('short')) + m.ring(1, '.m-map')
                          + m.ring(4, '.m-cells'), 800, aw=1440)),
        opt('The map keeps the left, the places take the right',
            ['Question one becomes <b>two columns</b>: the map at '
             '<b>820&times;427</b> on the left, the sixteen places on the '
             'right. Same ratio, a third less width.',
             'The places go <b>two across in a 470px column</b> &mdash; eight '
             'rows, one right edge, every one of them on the screen beside '
             'the map.',
             'The question comes to about <b>500px</b> &mdash; a little over '
             'half what it is today.',
             'Questions 2 to 5 are untouched, two across underneath, exactly '
             'as they are now.'],
            '<p>Your second suggestion, drawn. It is the one that actually '
            'answers the sentence &mdash; the map and every one of the '
            'sixteen places are on the screen together, which is what '
            '&ldquo;one concise view&rdquo; means.</p>'
            '<p>The map keeps its ratio and loses a third of its width, so '
            'at <b>820&times;427</b> it is still <b>24% more map than you had '
            'before decision 33</b> (737&times;384). Two-letter codes are '
            'legible at that size; full state names are not, so this holds '
            'decision <a href="#d31">31</a> at codes everywhere.</p>',
            cost='1 day', risk='Full state names stop fitting',
            cls='rec',
            mockup=m.mock(d.scrolled(d.q1('split')) + m.ring(1, '.m-map')
                          + m.ring(2, '.m-cells'), 660, aw=1440)),
        opt('The map keeps the left, every question takes the right',
            ['The map holds a <b>700px left column on its own</b> and stays '
             'there while you answer; <b>all five questions</b> run down the '
             'right.',
             'You watch your states light up on the map while you answer how '
             'long you have and how many of you there are.',
             'The whole form is <b>one band</b> rather than four screens '
             '&mdash; everything but the last row of question five is on the '
             'first screen.',
             'The map is <b>700&times;365</b> &mdash; smaller in both '
             'directions than today.'],
            '<p>This is decision <a href="#d33">33C</a>, which you did not '
            'pick &mdash; back on the table because the reason for it has '
            'changed. Then it was about interactivity; now it is the only '
            'option that puts the whole form on one screen.</p>'
            '<p>It is also the biggest change of the four and the one that '
            'shrinks the map most. A pinned column fights the site&rsquo;s own '
            'sticky header and the floating Search trips pill, and this page '
            'already owns the bottom-right corner on a phone.</p>',
            cost='2&frac12; days', risk='Smallest map, three sticky things',
            mockup=m.mock(d.scrolled(d.q1('all')) + m.ring(1, '.m-map')
                          + m.ring(2, '.m-q2 > div:last-child'), 1000, aw=1440)),
    ],
    verdict([
        '<b>C</b> &mdash; your own second idea. It is the only one that puts '
        'the map and all sixteen places on the screen at once, and it does it '
        'by taking width off the map rather than height, so the map keeps the '
        'proportion that makes it readable.',
        '<b>B is the safe one</b> and it is half a day. If you want this fixed '
        'this week and left alone, say B &mdash; it is one line in one file '
        'and it cannot break anything.',
        'One thing to know before you answer: <b>C and D both cost you full '
        'state names.</b> At 820px the map carries two-letter codes well and '
        'full names badly. Decision <a href="#d31">31</a> went to B '
        '(&ldquo;every state, two letters&rdquo;) so this is consistent with '
        'what is already built &mdash; but the &ldquo;you can clearly see, '
        'okay, that&rsquo;s Utah&rdquo; version of the map only exists at full '
        'width. A is the only option that keeps it.',
        '<b>These numbers are your window, not a standard one.</b> Measured at '
        '1440&times;900. On a 1920&times;1080 screen the fold falls at '
        'y=1,891 and everything fits today; on a 13&Prime; laptop at 1440'
        '&times;750 you lose three of the four rows. If your screen is bigger '
        'than 900px tall, say so and I will remeasure &mdash; the fix is the '
        'same shape, the urgency is not.',
    ]),
    since=NEW, cols=2))


# =====================================================================
# 41 — where the reviews go  (REDRAWN, round four)
# =====================================================================
#
# Crow looked at B on this sheet and did not answer it. What he said instead
# opened a slot none of A-D used: the review block under the price panel runs
# the 478px title column down past the bottom of the gallery, and the paper it
# leaves beside it is the thing he objected to — and then proposed filling.
#
# So C and D come off the table (C was the drift beside the CTA, D moved the
# price panel) and E, F and G go on it, all three of them in that white space.
# A and B keep their drawings so the comparison still works, redrawn at 1440
# with the live hero geometry: an 812px gallery against a 478px column.

ALL.append(dec(
    41,
    'Where the reviews go on a tour page',
    [('a tour page', ''), ('Crow', 'who'), ('1&ndash;2 days', ''),
     ('redrawn', 'big')],
    [quote(['Look how the review box looks when it loads &mdash; it then '
            'extends down, there&rsquo;s a shit little white space below the '
            'photo and that just looks like shit.',
            'But it kind of gave me another idea. Instead of putting it on the '
            'right-hand side, maybe you use that white space to just put the '
            'different reviews below &mdash; I think that could make sense or '
            'look good.',
            'Let&rsquo;s go with my first idea of having them kind of below '
            'the hero image. You could have up to three, I believe. So kind of '
            'building off option B, but just move it down to where that blank '
            'white space is right now.'],
           'Crow, 16 September, on option B of this decision'),
     quote(['If you look at D, the description comes up and the review follows '
            'it &mdash; I kind of like that, but it&rsquo;s not super clean.'],
           'Crow, in the same note &mdash; which is why D is off the table '
           'rather than recommended')],
    [
        opt('A band below the Overview, as now',
            ['Three cards side by side across the <b>913px</b> content column, '
             'under the Overview.',
             'They sit at <b>y=1,539</b>. The first screen ends at y=900, so '
             'they are <b>a full screen and a half below</b> the photograph.',
             'The title column holds a badge, the title, &ldquo;1-Day '
             'Tour&rdquo; and the price panel. It ends at <b>y=600</b> against '
             'a gallery bottom of <b>y=635</b> &mdash; <b>35px of slack</b>.',
             'Nothing rotates. Three render, and a tour with nine reviews '
             'shows three of them.'],
            '<p>Decision <a href="#d26">26C</a>, shipped. Every panel below '
            'removes this band &mdash; the reviews end up in one place, not '
            'two.</p>'
            '<p>The 35px of slack is the whole geometric problem: the column '
            'beside the photograph has <b>no room left in it</b>. Anything '
            'added there runs past the bottom of the picture, which is exactly '
            'what you saw in B.</p>',
            cost='&mdash;', risk='A screen and a half from the title',
            cls='now',
            mockup=m.mock(e.page('now', band=True), 1900, aw=1440)),
        opt('One review at a time, under the price',
            ['A review block goes into the title column, <b>under the price '
             'panel</b> &mdash; score, count, then one card at a time.',
             'The next slides in from the right every eight seconds; pointing '
             'at it stops it.',
             'The column then runs <b>172px past the bottom of the '
             'photograph</b>, which leaves <b>812&times;158 of white paper</b> '
             'beside it. <b>That is the hatched box in the drawing</b>, and it '
             'is stretched to the gap rather than typed in.',
             'The band below the Overview goes.'],
            '<p>This was my recommendation and it is the one you stopped on. '
            'The drawing now shows the cost you spotted rather than hiding it: '
            'a 478px column cannot take a review block without outrunning the '
            'picture beside it.</p>'
            '<p>It is still the option that puts a review <b>highest</b> on '
            'the page &mdash; level with the price, in the eye line of the '
            'Reserve button. Left on the table for that reason alone.</p>',
            cost='1 day', risk='Leaves 158px of paper under the photograph',
            mockup=m.mock(e.page('one') + m.ring(1, '.m-revslot')
                          + m.ring(2, '.m-white'), 1900, aw=1440)),
        opt('Three cards in that white space',
            ['The cards go <b>under the photograph</b>, in the left column: '
             'the score line, then <b>three cards across 812px</b> &mdash; '
             '<b>260px each</b>, 262px of strip in total.',
             'The title column is <b>untouched</b>. Badge, title, subtitle, '
             'price panel &mdash; nothing added, nothing moved.',
             'Each card carries about forty words in six lines, then <b>Read '
             'the full review</b>. Three is the ceiling, as you said.',
             'The first block grows from <b>402px to 710px</b>, and the 281px '
             'band below the Overview <b>goes</b> &mdash; so the page ends up '
             'shorter, not longer.',
             'On a phone the strip drops <b>below the price panel</b>: '
             'photograph, name, price, reviews. A review never comes between '
             'the picture and the name of the trip.'],
            '<p>Your own idea, drawn. It is the only slot on this page where '
            'three cards fit side by side above the fold &mdash; 260px a card '
            'holds two sentences; the 150px the title column could offer holds '
            'a fragment.</p>'
            '<p>It fixes what you objected to by construction: there is no '
            'white space under the photograph, because the reviews are in it. '
            'Measured on the drawing, the strip ends <b>42px past the bottom '
            'edge</b> of a 1440&times;900 window &mdash; so you get the '
            'photograph, the price, the score line and most of all three cards '
            'before you touch the wheel.</p>'
            '<p>Two honest costs. At <b>260px a card is narrower than the '
            '293px</b> the band gives it today, so a review runs further down '
            'the card. And the strip is <b>262px</b> where the paper it fills '
            'is only <b>158</b> &mdash; so this block ends <b>135px lower</b> '
            'than B&rsquo;s, not level with the photograph.</p>',
            cost='1 day', risk='260px a card &mdash; the narrowest of the three',
            cls='rec',
            mockup=m.mock(e.page('under') + m.ring(1, '.m-revstrip')
                          + m.ring(2, '.m-tt'), 1900, aw=1440)),
        opt('The same three, drifting right',
            ['Same slot, same three cards, but on <b>one track that creeps to '
             'the right</b> &mdash; the &ldquo;slightly rotating&rdquo; you '
             'asked for, moved down here.',
             'You always see the <b>edge of a fourth card</b>, so the track '
             'never looks finished and says &ldquo;there are more&rdquo; '
             'without a control.',
             'Hovering stops it. It does not animate at all for anyone whose '
             'device asks for reduced motion.',
             '<b>At exactly three reviews it stands still</b> &mdash; there is '
             'nothing to drift to, so it renders as E until a fourth arrives. '
             'The strip is 288px against E&rsquo;s 262, for the row of '
             'dots.'],
            '<p>E plus an animation, and that is the honest description of it. '
            'If operations only ever sends three per tour, this <i>is</i> E '
            'and the extra day buys nothing.</p>'
            '<p>Where it earns its keep is a trip with nine reviews: a static '
            'row of three says &ldquo;here are three reviews&rdquo;, and a '
            'drifting one says &ldquo;here are the first three of many&rdquo;. '
            'Worth knowing that this audience skews older and a crawling line '
            'of text is the kind of thing that gets resented &mdash; it is a '
            'long way from the Reserve button here, which is what made me '
            'argue against the old C.</p>',
            cost='1&frac12; days', risk='Motion that only pays off above three reviews',
            mockup=m.mock(e.page('drift') + m.ring(1, '.m-revdrift'),
                          1900, aw=1440)),
        opt('A strip across the whole row',
            ['The cards go <b>under both columns</b> instead of only the '
             'photograph &mdash; three across <b>1,320px</b>, <b>429px '
             'each</b>.',
             'The <b>same review prints in four lines instead of six</b>, '
             'because the card is 65% wider. A long one is far less likely to '
             'be cut off at <b>Read the full review</b>.',
             'The hero row keeps its shape exactly: gallery and price panel '
             'end level, as they do today, and the strip is a band under '
             'them.',
             'The strip is <b>222px</b> against E&rsquo;s 262, and the whole '
             'block ends <b>9px inside</b> a 1440&times;900 window where '
             'E&rsquo;s runs 42px past it.'],
            '<p>The tidiest geometry of the three, and the one that scales: it '
            'is the only slot where a long review can be printed rather than '
            'truncated.</p>'
            '<p>What it is not: &ldquo;below the hero image&rdquo;. It is a '
            'band under the <i>whole</i> first block, so it reads as a new '
            'section rather than as part of the picture. It leaves the 35px '
            'under the price panel exactly as it is &mdash; which is fine, '
            'because 35px of paper is not what anybody notices.</p>'
            '<p>Where each option&rsquo;s first block ends, measured on these '
            'drawings, with the screen ending at y=859: <b>A y=594</b> (and a '
            'band at y=1,129), <b>B y=766</b>, <b>G y=850</b>, <b>E y=901</b>, '
            '<b>F y=928</b>.</p>',
            cost='1 day', risk='Reads as a band, not as part of the hero',
            mockup=m.mock(e.page('wide') + m.ring(1, '.m-revstrip'),
                          1900, aw=1440)),
    ],
    verdict([
        '<b>E</b> &mdash; your own idea, and the one that answers the '
        'objection by construction. The cards are in the white space, so there '
        'is none.',
        '<b>The one number worth having before you answer:</b> the paper B '
        'leaves is <b>812&times;158</b> and E&rsquo;s strip is <b>262px</b> '
        'tall. So &ldquo;move it down into the white space&rdquo; does not '
        'come free &mdash; the strip is two-thirds taller than the paper it '
        'fills, and the block ends <b>135px lower</b> than B&rsquo;s rather '
        'than level with the photograph. Every option here still makes the '
        'page shorter overall, because all of them delete the 281px band below '
        'the Overview.',
        '<b>G is the one to say if the reviews turn out to be long.</b> '
        '429px a card against 260 prints the same review in <b>four lines '
        'instead of six</b>, and E&rsquo;s 260px is actually <i>narrower</i> '
        'than the 293px a card gets in the band today. If operations sends '
        'paragraphs rather than lines, E cuts most of every one of them at '
        'Read the full review. That is the whole argument between E and G, and '
        'it turns on content nobody has seen yet.',
        '<b>F only pays off above three reviews.</b> At three it is E with a '
        'stopped animation. Say F if you want the drift built now so it is '
        'there when the picks arrive; say E if you would rather add it later, '
        'because it is half a day either way.',
        '<b>C and D are off the table</b> &mdash; C put continuous motion 30px '
        'from the Reserve button, and you have said D is &ldquo;not super '
        'clean&rdquo;. Their letters are spent and will not be reused.',
        '<b>None of this renders anything yet.</b> '
        '<code>data/tour-reviews.json</code> is empty and every word in these '
        'drawings is placeholder. The slot stays invisible on all 93 tours '
        'until Matt sends reviews with a tour name against each. It has not '
        'moved since the 16th.',
    ]),
    since=('Redrawn', '16 Sep &middot; round 4'), cols=2))
