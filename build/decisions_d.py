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
# 41 — where the reviews go
# =====================================================================
#
# Authored at 1200, so it can be read against decision 36's drawings, which
# Crow has already been through.

ALL.append(dec(
    41,
    'Where the reviews go on a tour page',
    [('a tour page', ''), ('Crow', 'who'), ('1&ndash;2 days', ''),
     ('third time asked', 'big')],
    [quote(['The reviews thing I told you about specifically was not where I '
            'wanted it placed. I told you that when you&rsquo;re looking at '
            'one of the actual tours, you have the hero images that you can '
            'click through, and then on the right hand side you have the '
            'title and the description of what this is &mdash; and then right '
            'below it I wanted to have those reviews.',
            'In these card shaped boxes like you have now, that&rsquo;s '
            'slightly rotating to the right, and if you hover over it it stops '
            'and you can click read more to actually read the whole review. '
            'Because right now it&rsquo;s below the overview.'],
           'Crow, 16 September, walking the built page')],
    [
        opt('A band below the Overview, as now',
            ['Three cards <b>side by side across the 913px content column</b>, '
             'under the Overview.',
             'They sit at <b>y=1,539</b> &mdash; 1,284px below the top of the '
             'gallery, and about two screens down.',
             'The title column beside the gallery holds four things: the '
             'badge, the title, &ldquo;1-Day Tour&rdquo; and the price panel. '
             'It ends at y=601 against a gallery bottom of y=635, so there are '
             '<b>34px of slack</b> in it.',
             'Nothing rotates. Three cards render, and a tour with nine '
             'reviews shows three of them.'],
            '<p>This is decision <a href="#d26">26C</a>, shipped &mdash; and '
            'decision <a href="#d36">36</a> was drawn to move it and never got '
            'an answer, because none of E, F, G or H put it where you meant.</p>'
            '<p>One correction worth having: <b>the description is not in the '
            'right-hand column.</b> It is 772px wide at y=701, under the fact '
            'strip, below the fold of the first screen. So &ldquo;right below '
            'the description&rdquo; is not a slot that exists on the page '
            'today &mdash; option D is the one that creates it.</p>',
            cost='&mdash;', risk='Two screens from the title',
            cls='now',
            mockup=m.mock(d.tourtop('now') + d.belowtop(reviews=True)
                          + m.ring(1, '.m-revcards') + m.ring(3, '.m-tt'),
                          1810)),
        opt('One review at a time, under the price',
            ['A review block goes <b>into the title column, directly under the '
             'price panel</b> &mdash; the score, the count, then one card.',
             'The next review <b>slides in from the right every eight '
             'seconds</b>. Pointing at the card stops it, and it stays '
             'stopped.',
             '<b>Read the full review</b> opens the whole thing; the card '
             'shows about forty words.',
             'The band below the Overview <b>goes</b>. The reviews exist in '
             'one place instead of two.'],
            '<p>The column has 34px of slack in it today, so this grows the '
            'first block by about 190px &mdash; and takes 337px off further '
            'down, which makes the page slightly shorter overall.</p>'
            '<p>One card at a time is what makes a 478px column work: three '
            'across in that width is 150px each, which is a fragment of a '
            'sentence rather than a review.</p>',
            cost='1 day', risk='One review visible instead of three',
            cls='rec',
            mockup=m.mock(d.tourtop('one') + d.belowtop(reviews=False)
                          + m.ring(1, '.m-revslot'), 1560)),
        opt('A rail that drifts right',
            ['The same slot under the price panel, but the cards sit on '
             '<b>one track that creeps to the right continuously</b>.',
             'You always see one card and <b>the edge of the next</b>, so the '
             'track never looks finished.',
             'Hovering stops the drift. <b>Read the full review</b> works the '
             'same way.',
             'The band below the Overview <b>goes</b>.'],
            '<p>The literal reading of &ldquo;slightly rotating to the '
            'right&rdquo;: not a swap, a drift. It signals &ldquo;there are '
            'more of these&rdquo; without a control.</p>'
            '<p>What it costs: something is moving continuously, 30px from '
            'the <b>Reserve a place</b> button, on the most important column '
            'of the page. That is the argument decision 36 already lost once '
            '&mdash; a review crawling past is not a review anyone reads. '
            'Here the cards are full cards rather than a 52px bar, so it is a '
            'much better version of it, but the objection is the same '
            'one.</p>',
            cost='1 day', risk='Constant motion beside the CTA',
            mockup=m.mock(d.tourtop('creep') + d.belowtop(reviews=False)
                          + m.ring(1, '.m-revcreep'), 1560)),
        opt('The description comes up, and the reviews follow it',
            ['The <b>description moves into the title column</b>, under the '
             'title &mdash; which is where you remembered it being.',
             'The reviews go <b>directly under the description</b>, exactly as '
             'described. Same card, same eight seconds, same hover.',
             'The <b>price panel moves out</b>, to a wide bar directly under '
             'the gallery: from, per person, Reserve a place.',
             'The fact strip keeps its five facts and <b>loses the paragraph</b> '
             '&mdash; it is not printed twice.'],
            '<p>The only option that matches the sentence word for word: '
            'title, description, reviews, in that order, in the right-hand '
            'column.</p>'
            '<p>What it costs: the price panel is the most valuable object on '
            'this page and this moves it. Under the gallery it is <b>wider and '
            'still above the fold</b> &mdash; arguably more prominent, not '
            'less &mdash; but it is a change you did not ask for, made to fit '
            'in one you did.</p>',
            cost='2 days', risk='Moves the price panel and the CTA',
            mockup=m.mock(d.tourtop('desc') + d.belowtop(reviews=False, desc=False)
                          + m.ring(1, '.m-ttdesc') + m.ring(2, '.m-revslot')
                          + m.ring(3, '.m-pricebar'), 1600)),
    ],
    verdict([
        '<b>B</b>, unless the description being up there is the point &mdash; '
        'then <b>D</b>.',
        'B puts the cards where you pointed, in the shape you described, with '
        'the rotation and the hover-stop and the read-more, and changes '
        'nothing else on a page you have otherwise signed off. It is the '
        'smallest change that answers the note.',
        '<b>Say D if what you want is the description up there too.</b> I have '
        'drawn it rather than argued about it, because you have described that '
        'column twice now as holding the description and it does not. D is the '
        'only one that makes the page match the sentence &mdash; and the '
        'reason it is not my pick is that it moves the price panel to do it, '
        'which is a bigger decision than the one you asked me to make.',
        '<b>C is not wrong, it is just noisy.</b> Continuous motion beside the '
        'Reserve button is the one thing I would not put there. If you want '
        'the drift, say C and I will build it &mdash; the difference between '
        'B and C is one CSS animation.',
        '<b>None of this renders anything yet.</b> '
        '<code>data/tour-reviews.json</code> is empty and every word in these '
        'drawings is placeholder. The slot stays invisible on all 93 tours '
        'until Matt sends reviews with a tour name against each. That is item '
        'one on the waiting list and it has not moved since the 16th.',
    ]),
    since=NEW, cols=2))
