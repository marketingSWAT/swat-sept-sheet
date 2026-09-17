"""Decisions 30-39 — round two of the 16 September notes.

These come from Crow's walkthrough of the staging build after round one of the
sheet (decisions 20-29) shipped. Six are about the Build Your Own page, which
he asked for first and by name; the other four are the home page's activity
level, the top of a tour page, the qualifying panel, and the film slot beside
SWAT's own paragraph.

Every "Now" panel is the deployed staging build measured at a 1200px viewport
on 16 September 2026 — see the header of `mocks_c.py` for the full harvest.
"""

import mocks as m
import mocks_c as c
from sheetkit import opt, quote, verdict, dec

ALL = []

NEW = ('New', '16 Sep &middot; round 2')

# The six places the pill buttons wrap on /custom-tours/, measured. Quoted in
# three decisions, so it lives here rather than being retyped.
RAGGED = '695, 763, 280, 611, 443, 544, 694, 497'


# =====================================================================
# 30 — the block above the builder
# =====================================================================
#
# Authored at 1200: the argument is how far down the page the form starts, so
# the drawing has to be the page, not the form.

def _page(meanmode, herostrip=False, tail='', mapmode='sel'):
    return (m.header(active='Build Your Own') +
            c.hero(strip=herostrip) +
            m.crumbs('Home', 'Build your own') +
            c.meaning(meanmode) +
            '<div class="m-band sand" style="margin-top:34px">'
            '<div class="m-shell">' + c.buildhead() +
            c.question(0, 'pill', mapmode=mapmode) +
            c.question(1, 'pill') + '</div></div>' + tail)


ALL.append(dec(
    30,
    'The wall of words above the builder',
    [('/custom-tours/', ''), ('Crow', 'who'), ('2 hours', ''),
     ('570px of page', 'big')],
    [quote(['It says what a custom trip means here — your places, your dates, '
            'your group, your pace. I think we can just remove that, and then '
            'just move up the start here to build your trip.'],
           'Crow, 16 September')],
    [
        opt('Keep it, as now',
            ['A heading, <b>two paragraphs</b> and <b>four cards</b> sit '
             'between the hero and the form.',
             'The block is <b>570px tall</b>, so &ldquo;Start here to build '
             'your trip&rdquo; begins at <b>y=1,344</b> — past the first '
             'screen on a laptop.',
             'It is also the page&rsquo;s only prose: about 200 words, which '
             'is what a crawler and the chatbot read this page as.',
             'Nothing on it is clickable except the phone number.'],
            '<p>Measured on staging: hero, breadcrumbs, then 570px of '
            'explanation before the thing the page is for. Somebody who '
            'clicked <b>Build Your Own</b> has already decided they want '
            'something custom — the explanation is answering a question they '
            'stopped asking one click ago.</p>',
            cost='&mdash;', risk='The form starts below the fold',
            cls='now',
            mockup=m.mock(_page('full', tail=m.ruler(300, 1044,
                                                     'form starts y=1,344')),
                          1560)),
        opt('Cut it, form first',
            ['The heading, both paragraphs and the four cards are '
             '<b>deleted</b>.',
             'The builder heading moves from <b>y=1,344 to about y=700</b> — '
             'first screen, every laptop.',
             'The page loses about <b>200 words</b>; what is left is a hero '
             'line and a form.',
             'Two hours of work, and nothing else on the site changes.'],
            '<p>Literally what was asked for, and the fastest of the four. '
            'The cost is that <code>/custom-tours/</code> becomes a page with '
            'almost no readable text on it — and it is the page Lance named '
            'as the competitive advantage nobody can find.</p>'
            '<p>That matters for one specific reason: the SEO pass measured '
            '<i>rendered</i> words, not source, and a form is not words. This '
            'page would drop to the thinnest on the site.</p>',
            cost='2 hours', risk='The page has almost nothing left to read',
            mockup=m.mock(_page('none'), 1140)),
        opt('One line up, the four promises below',
            ['The two paragraphs become <b>one sentence</b> under the hero, '
             'with a link.',
             'The builder heading lands around <b>y=760</b>.',
             'The four cards — places, dates, group, pace — move <b>below the '
             'form</b>, where they answer &ldquo;what happens now?&rdquo; '
             'instead of delaying the start.',
             'Nothing is thrown away: the words still exist on the page for a '
             'crawler and for the chatbot.'],
            '<p>The instruction is met — the form is the first thing you see '
            '— without turning the page into a bare form. The four cards do '
            'more work underneath it anyway: they are reassurance while '
            'somebody decides whether to press Send, which is where '
            'reassurance belongs.</p>',
            cost='Half a day', risk='One more section below the form',
            cls='rec',
            mockup=m.mock(_page('line', tail=(
                '<div class="m-shell" style="padding-top:30px">'
                + c.meaning('full').replace(
                    'What a custom trip means here',
                    'What happens after you send this')
                + '</div>')), 1720)),
        opt('The four promises become the hero',
            ['The four cards collapse into a <b>thin strip across the bottom '
             'of the hero photograph</b>.',
             'Costs <b>zero extra height</b> — it sits on the picture that is '
             'already there.',
             'The two paragraphs go entirely.',
             'Builder heading lands around <b>y=700</b>, same as cutting it.'],
            '<p>The tightest of the four and the best-looking. The risk is '
            'real though: four cells of white text on a photograph is where '
            'copy goes to be skipped, and it is the one place on this page '
            'SWAT gets to say what custom actually means.</p>',
            cost='Half a day', risk='Text on a photo is text nobody reads',
            mockup=m.mock(_page('none', herostrip=True), 1180)),
    ],
    verdict([
        'Go with <b>C</b>. It does the thing you asked — the form is the '
        'first thing on the page — and it keeps SWAT&rsquo;s own explanation '
        'alive underneath, where it reads as reassurance rather than as a '
        'delay.',
        'If you would rather just be rid of it, <b>B</b> is two hours and I '
        'will do it today. The one thing I would say before you pick it: this '
        'page is the only page on the site that says SWAT builds trips to '
        'order, and after B it says that in one hero sentence and nothing '
        'else.',
        '<b>D</b> is the prettiest and I would still not pick it — four cells '
        'of small white text on a photograph is the classic place for copy to '
        'die.',
    ]),
    since=NEW))


# =====================================================================
# 31 — naming the states on the map
# =====================================================================
#
# Authored at 900: the whole argument is whether a two-letter code survives at
# the size the map actually renders, so the map has to be near its real width.

def _mapdemo(labels, selected=('UT', 'AZ'), note=None):
    n = f'<p class="m-sub" style="margin-top:14px">{note}</p>' if note else ''
    return ('<div class="m-shell" style="padding-top:20px">'
            '<div class="m-qh"><b>1.</b><span>Where would you like to go?</span>'
            '<em>pick as many as you like</em></div>'
            + c.nationmap(selected=selected, labels=labels, h=470)
            + c.answers(0, 'pill', on=('Utah', 'Arizona')) + n + '</div>')


ALL.append(dec(
    31,
    'Naming the states on the map',
    [('/custom-tours/, step 1', ''), ('Crow', 'who'), ('Half a day', ''),
     ('50 labels', '')],
    [quote(['For the map that we show — to have like the state abbreviation on '
            'the map, so you can clearly see, okay, that&rsquo;s Utah. Kind of '
            'like what it looks like when you select it.'],
           'Crow, 16 September')],
    [
        opt('Nothing until you pick, as now',
            ['An unselected map carries <b>no labels at all</b> — 50 grey '
             'shapes.',
             'Selecting a state fills it rust and prints its <b>full '
             'name</b> in white, centred.',
             'So the only way to find out what a shape is, is to click it.',
             'The chip row underneath is the only readable list of places.'],
            '<p>This is the behaviour you described liking — the white name on '
            'the filled state. The gap is everything before that: somebody '
            'looking for Montana has to know where Montana is, or hunt the '
            'chip row.</p>',
            cost='&mdash;', risk='Unreadable until clicked', cls='now',
            mockup=m.mock(_mapdemo('sel'), 860, aw=760)),
        opt('Every state, two letters',
            ['All <b>50 states</b> carry their two-letter code at rest.',
             'The eight crowded north-eastern ones — VT, NH, MA, RI, CT, NJ, '
             'DE, MD — are <b>led out to the margin</b> on a hairline, because '
             'a code will not fit inside them at this size.',
             'A selected state keeps the rust fill and its code goes '
             '<b>white</b>, so the answer still reads the way it does today.',
             'Labels are drawn white-haloed, so they stay legible over the '
             'state borders.'],
            '<p>The full names cannot be the resting state — &ldquo;South '
            'Dakota&rdquo; across South Dakota is wider than South Dakota. Two '
            'letters is what fits, and it is what every US map does for the '
            'same reason.</p>'
            '<p>The leader lines are not decoration: without them RI and CT '
            'print on top of Massachusetts and the map looks broken.</p>',
            cost='Half a day', risk='Fifty labels is busier than fifty shapes',
            cls='rec',
            mockup=m.mock(_mapdemo('all'), 860, aw=760)),
        opt('Only the states we sell',
            ['The <b>14 states in the catalogue</b> carry a code. The other 36 '
             'stay blank.',
             'Much quieter — a third of the labels.',
             'Every state is still clickable, exactly as now.',
             'But a blank state reads as &ldquo;we don&rsquo;t go '
             'there&rdquo;, which is the opposite of what the room decided in '
             'September.'],
            '<p>Cleaner, and it quietly undoes decision 24. The reason every '
            'state is clickable is [ops]&rsquo;s own line — <i>&ldquo;you can '
            'add every state, because we do custom tours across the '
            'country&rdquo;</i> — and a labelled Utah beside an unlabelled '
            'Vermont says the opposite of that.</p>'
            '<p>Worth drawing because it is genuinely tidier. I would still '
            'not ship it.</p>',
            cost='Half a day', risk='Silently says we do not go there',
            mockup=m.mock(_mapdemo('ours'), 860, aw=760)),
    ],
    verdict([
        '<b>B</b>. It is the thing you asked for and the leader lines are the '
        'only part that needs saying out loud — without them the north-east '
        'is a pile-up.',
        'One thing I will not do without you saying so: the codes are '
        '<b>abbreviations, not names</b>. At the width this map renders — '
        '737px for the whole country — &ldquo;South Dakota&rdquo; is wider '
        'than the state. If you want full names, the map has to get roughly '
        'twice as tall, which is decision 33.',
    ]),
    since=NEW, cols=2))


# =====================================================================
# 32 — the buttons themselves
# =====================================================================
#
# Authored at 800: this is an argument about a 44px control inside a 739px
# column. Scaled into a 1200 canvas the buttons render at half size and the
# ragged edge — the actual complaint — stops being visible.

def _form(style, on=None):
    on = on or {0: ('Utah', 'Arizona'), 1: ('4-6 days',),
                2: ('3&ndash;6',), 3: ('Autumn',)}
    if style == 'row':
        qs = ''.join(c.question(i, 'row', on=on.get(i, ()), n=i + 1)
                     for i in range(5)) + c.notesq(6, 'row')
    else:
        qs = ''.join(c.question(i, style, on=on.get(i, ()), n=i + 1)
                     for i in range(5)) + c.notesq(6, style)
    return f'<div class="m-shell" style="padding-top:22px">{qs}</div>'


ALL.append(dec(
    32,
    'The buttons, and the ragged right edge',
    [('/custom-tours/ and the home band', ''), ('Crow', 'who'),
     ('1 day', ''), ('40 buttons, 8 edges', 'big')],
    [quote(['Also for the buttons below — I really just don&rsquo;t like these '
            'circle buttons. It just doesn&rsquo;t look super clean, it kind '
            'of just looks sloppy.',
            'I want you to mock a couple designs for different buttons.'],
           'Crow, 16 September')],
    [
        opt('Pills, as now',
            ['<b>40 buttons</b> across five questions, every one a <b>999px '
             'pill</b>, 44px tall.',
             'Widths run <b>57px to 163px</b> — they are as wide as their own '
             'words, so no two line up.',
             'They wrap into <b>8 rows with 8 different right edges</b>: '
             f'{RAGGED}, inside a 739px column.',
             'One row holds a single button with 640px of white paper beside '
             'it.'],
            '<p>This is the measurement behind &ldquo;sloppy&rdquo;, and it is '
            'not a matter of taste: eight rows end at eight different places '
            'across a <b>483px spread</b>. The eye reads that as debris '
            'rather than as a list.</p>'
            '<p>The pill itself is fine. What is wrong is that a pill is '
            '<i>content-width</i>, so the layout is decided by the length of '
            'the words rather than by the grid.</p>',
            cost='&mdash;', risk='Reads as unfinished', cls='now',
            mockup=m.mock(_form('pill', ) + m.ring(1, '.m-chips'),
                          1180, aw=800)),
        opt('Square the corners',
            ['Same buttons, same layout, <b>4px radius</b> instead of 999px.',
             'Looks less like a tag cloud and more like a form.',
             'Matches the cards, the panels and the inputs, which are all 3-4px '
             'on this build.',
             'The <b>eight ragged rows do not change</b> — the widths are '
             'still set by the words.'],
            '<p>Twenty minutes. It kills the &ldquo;circle&rdquo; half of the '
            'complaint and none of the &ldquo;sloppy&rdquo; half, because the '
            'ragged edge is a width problem, not a corner problem.</p>'
            '<p>Included so the two halves of what you said can be answered '
            'separately if you want.</p>',
            cost='20 minutes', risk='The ragged edge survives',
            mockup=m.mock(_form('square'), 1180, aw=800)),
        opt('An even grid',
            ['Every answer becomes a <b>cell of equal width</b> in a fixed '
             'column count — 4 across for places, 3 for durations, 5 for '
             'seasons.',
             '<b>Eight ragged edges become none.</b> Left and right edges line '
             'up down the whole form.',
             'Each cell carries a <b>checkbox</b>, so &ldquo;pick as many as '
             'you like&rdquo; is visible rather than written.',
             'A selected cell fills pale rust with a tick — clearer at a '
             'glance than a solid rust pill.'],
            '<p>This is the fix for the actual complaint. The grid does the '
            'aligning instead of the words, so the form reads as a form.</p>'
            '<p>The checkbox matters more than it looks. Today nothing about a '
            'pill says you may choose several, and the only thing that does is '
            'a line of 13px grey text beside the question.</p>',
            cost='1 day', risk='Long labels truncate at four columns',
            cls='rec',
            mockup=m.mock(_form('grid') + m.ring(1, '.m-cells'),
                          1140, aw=800)),
        opt('A labelled row per question',
            ['C&rsquo;s grid, plus the question moved into a <b>fixed 150px '
             'left gutter</b>.',
             'The whole form now has <b>one alignment</b> — every question '
             'starts at the same x, every answer block starts at the same x.',
             'Turns six stacked blocks into six rows of a single table.',
             'The answers lose 176px of width, so places go 4-across in a '
             'narrower track.'],
            '<p>The most organised of the four, and the closest thing to the '
            '&ldquo;way more clean&rdquo; you asked for. It reads as a spec '
            'sheet rather than as a questionnaire.</p>'
            '<p>The cost is width and the risk is the phone: below 1024 the '
            'gutter has to stack back on top, so the mobile form is C '
            'anyway.</p>',
            cost='1&frac12; days', risk='Two layouts to maintain',
            mockup=m.mock(_form('row') + m.ring(1, '.m-qlab'), 1060, aw=800)),
    ],
    verdict([
        '<b>C</b>. It is the one that fixes what was actually wrong — eight '
        'rows ending at eight different places — and it fixes it everywhere '
        'the same control is used, which is this form, the home band and the '
        'filter bar, in one change.',
        '<b>D</b> is better looking on a desktop and I would happily build it '
        'on top of C later, because C is the mobile layout of D. Nothing is '
        'wasted by starting at C.',
        'I ruled out a fifth option before drawing it: turning the five '
        'questions into dropdowns. It is the cleanest thing possible and it '
        'hides every answer behind a click, on the one page whose whole '
        'purpose is to show somebody what SWAT will do.',
    ]),
    since=NEW, cols=2))


# =====================================================================
# 33 — the shape of the page
# =====================================================================

ALL.append(dec(
    33,
    'The shape of the Build Your Own page',
    [('/custom-tours/', ''), ('Crow', 'who'), ('2-3 days', ''),
     ('4,936px today', 'big')],
    [quote(['Just like an overall different layout for the selections — of '
            'like the states, the how long do you have, how many of you. I '
            'really think we can make this look way more clean and organised.'],
           'Crow, 16 September'),
     quote(['I love the interactive map, I think that looks great.'],
           'Crow, same message')],
    [
        opt('One long column, as now',
            ['Six questions stacked in a <b>739px column</b>, with a 320px '
             '&ldquo;Your trip so far&rdquo; panel beside them.',
             'The map is <b>inside question one</b>, 737&times;384 — one '
             'sixth of the form.',
             'The page is <b>4,936px</b> tall; the last question is at '
             'y=2,589. The builder band itself is <b>1,523px</b>.',
             'The summary panel <b>scrolls away</b> after the second question, '
             'so the thing it was built for is off screen while you answer.'],
            '<p>It works, and it is four screens long. The map — the part you '
            'said you love — is visible for the first of those four and gone '
            'for the rest.</p>',
            cost='&mdash;', risk='The map leaves the screen immediately',
            cls='now',
            mockup=m.mock(m.header(active='Build Your Own') +
                          '<div class="m-band sand"><div class="m-shell">' +
                          c.buildhead() + '</div>' +
                          c.builder(layout='now', mapmode='sel') + '</div>',
                          1760)),
        opt('The map goes wide, the questions go under it',
            ['The map goes from <b>737&times;384 to the full 1,100px</b> — '
             '<b>55% more area</b>, and wide enough that <b>full state '
             'names</b> fit inside the big states.',
             'Questions 2-5 go <b>two across</b> under it, so four stacked '
             'blocks become two rows.',
             'The summary panel sits beside <i>those</i>, where it is on '
             'screen while they are answered rather than scrolled past.',
             '<b>It does not make the page shorter</b> — drawn and measured, '
             'it is about 70px taller than what ships.'],
            '<p>The map is the thing that makes this page worth visiting, so '
            'it gets the width. This is also what unlocks full state names — '
            'decision 31 is limited by width, and this is the width.</p>'
            '<p>I expected this to shorten the page and it does not. Measured '
            'on the drawings: the builder band is 1,287px as it ships and '
            '1,359px here. The bigger map costs back everything the two-across '
            'questions save. The page gets shorter from decision '
            '<a href="#d30">30</a>, not from this one.</p>',
            cost='2 days', risk='Map dominates the phone view',
            cls='rec',
            mockup=m.mock(m.header(active='Build Your Own') +
                          '<div class="m-band sand"><div class="m-shell">' +
                          c.buildhead() + '</div>' +
                          c.builder(layout='wide', style='grid',
                                    mapmode='all',
                                    selected=('UT', 'AZ'),
                                    on={0: ('Utah', 'Arizona')}) + '</div>',
                          1980)),
        opt('The map pins itself to the left',
            ['Map in a <b>560px panel on the left that stays on screen</b> '
             'while you answer everything else.',
             'Questions 2-5 and the summary run down the right.',
             'You can see your states light up while you answer how long you '
             'have.',
             'The map is <b>smaller than it is today</b> — 560px against '
             '737px — and at that width a two-letter code is the most it can '
             'carry.'],
            '<p>The most interactive of the three and the only one where the '
            'map is never off screen. It is also the one that makes the map '
            'smaller, which is a real cost on the element you said you '
            'love.</p>'
            '<p>Sticky panels also fight with the site&rsquo;s own sticky '
            'header and the floating Search trips pill, and this page owns the '
            'bottom-right corner on a phone.</p>',
            cost='2&frac12; days', risk='A smaller map, and three sticky things',
            mockup=m.mock(m.header(active='Build Your Own') +
                          '<div class="m-band sand"><div class="m-shell">' +
                          c.buildhead() + '</div>' +
                          c.builder(layout='sticky', style='grid',
                                    mapmode='all', selected=('UT', 'AZ'),
                                    on={0: ('Utah', 'Arizona')}) + '</div>',
                          1700)),
        opt('A board of cards',
            ['Map on top, then the four short questions as a <b>2&times;2 '
             'board of cards</b>.',
             'Each question is visibly its own object, which is the tidiest '
             'reading of &ldquo;organised&rdquo;.',
             'The <b>only one of the four that is shorter</b> than what ships '
             '— and only by about 16px, so the page is the same page.',
             'Four bordered boxes is four more borders on a page that '
             'currently has almost none.'],
            '<p>Tidy, and slightly corporate. The build has deliberately very '
            'few boxes on it — the cards, the rail, the price panel — and this '
            'adds four more in one band.</p>',
            cost='2 days', risk='Boxes inside boxes',
            mockup=m.mock(m.header(active='Build Your Own') +
                          '<div class="m-band sand"><div class="m-shell">' +
                          c.buildhead() + '</div>' +
                          c.builder(layout='board', mapmode='all',
                                    selected=('UT', 'AZ'),
                                    on={0: ('Utah', 'Arizona')}) + '</div>',
                          1820)),
    ],
    verdict([
        '<b>B</b>. It gives the map the room, which is the right instinct — it '
        'is the only part of this page anyone would describe out loud.',
        'It also decides decision <a href="#d31">31</a> for you in the good '
        'direction: at 1,100px wide the map carries <b>full state names</b> on '
        'the big states and codes on the small ones, which is closer to '
        '&ldquo;you can clearly see, okay, that&rsquo;s Utah&rdquo; than '
        'abbreviations everywhere.',
        '<b>One correction to something I assumed.</b> I expected the '
        'reorganised layouts to make this page much shorter, and I measured '
        'the drawings rather than trusting that: the builder band is 1,287px '
        'as it ships, 1,359px in B, 1,339px in C and 1,271px in D. None of '
        'these is a height fix. The height comes off this page in decision '
        '<a href="#d30">30</a> — 570px of it — and nowhere else.',
        '<b>C</b> is the one to pick if watching the states light up while you '
        'answer matters more than map size. I would not, on a page where the '
        'map is already the best thing.',
    ]),
    since=NEW))


# =====================================================================
# 34 — what else the page could do
# =====================================================================

def _extra(kind):
    body = {'none': '', 'count': c.liveline(), 'photo': c.mapback(),
            'itin': c.draftitin()}[kind]
    return ('<div class="m-shell" style="padding-top:22px">'
            '<div class="m-qh"><b>1.</b><span>Where would you like to go?</span>'
            '<em>pick as many as you like</em></div>'
            + c.nationmap(selected=('UT',), labels='all', h=330)
            + c.answers(0, 'grid', on=('Utah',))
            + body
            + c.question(1, 'grid', n=2) + '</div>')


ALL.append(dec(
    34,
    'What the page does while you answer it',
    [('/custom-tours/', ''), ('Crow asked for ideas', 'who'),
     ('&frac12;-3 days', ''), ('Open invitation', '')],
    [quote(['If you have any suggestions on how to improve this page overall '
            'so it&rsquo;s visually appealing, it&rsquo;s very interactive, or '
            'anything else we could add that would make it much better — '
            'I&rsquo;m very open to it.'], 'Crow, 16 September')],
    [
        opt('It says nothing back, as now',
            ['Tapping a state fills it rust. Nothing else on the page '
             'responds.',
             'The summary panel lists what you picked, and it scrolls off '
             'after question two.',
             'There is already a matcher running — it finds the closest '
             'published trip — and its answer only appears in that panel.',
             'You find out whether SWAT can do this <b>after</b> you send your '
             'name and email.'],
            '<p>The page is a form that happens to have a map on it. Nothing '
            'you tap teaches you anything about SWAT.</p>',
            cost='&mdash;', risk='No reason to keep answering',
            cls='now',
            mockup=m.mock(_extra('none'), 1020, aw=900)),
        opt('It tells you what it already knows',
            ['Picking a state prints one line: <b>&ldquo;14 trips already go '
             'to Utah. Three of them are 4-6 days, from $1,999.&rdquo;</b>',
             'Real data — the matcher and the counts already exist in the '
             'browser on this page.',
             'Links straight through to those trips, so somebody who would be '
             'happy with a published departure can stop here.',
             'Updates as each answer narrows it.'],
            '<p>The cheapest useful thing on this list and the only one that '
            'can shorten the sale. Some people filling in a custom form would '
            'be perfectly happy with a scheduled departure — they just do not '
            'know one exists.</p>'
            '<p>Everything it needs is already shipped: the flattened '
            'catalogue crosses into the browser for the &ldquo;closest thing '
            'we already run&rdquo; line.</p>',
            cost='Half a day', risk='A low count reads as "we do not do this"',
            mockup=m.mock(_extra('count') + m.ring(1, '.m-live'),
                          1080, aw=900)),
        opt('The map answers with the place',
            ['Picking a state pulls in <b>that state&rsquo;s own '
             'photograph</b> beside the map, with the parks SWAT guides there '
             'named under it.',
             'Dots appear on the map for each of those parks.',
             'The page stops being grey shapes and starts being the country.',
             'Needs a checked photograph per state — 15 of them, not a stock '
             'library.'],
            '<p>This is the &ldquo;visually appealing and interactive&rdquo; '
            'ask, taken literally. It uses two things that already exist: the '
            'photo library, and the park coordinates built for the tour '
            'map.</p>'
            '<p>The one rule attached to it is provenance. A photograph '
            'labelled Utah has to be Utah — the day tours site shipped '
            'Bolivian stock as the Bonneville Salt Flats and it took a '
            'verification script to find it.</p>',
            cost='2 days', risk='Every photo has to be verified as that place',
            cls='rec',
            mockup=m.mock(_extra('photo') + m.ring(1, '.m-mapback'),
                          1160, aw=900)),
        opt('A draft itinerary assembles itself',
            ['As answers land, a <b>day-by-day strip builds itself</b> — Day '
             '1 Las Vegas &rarr; Zion, Day 2 the Narrows, and so on.',
             'Lifted from the closest published trip and relabelled with your '
             'answers.',
             'By far the most impressive thing on the page.',
             'It is also <b>not a real itinerary</b>, and it looks exactly '
             'like one.'],
            '<p>I have drawn it because it is the obvious next idea and '
            'because I want to argue against it in a picture rather than in a '
            'paragraph.</p>'
            '<p>It manufactures a plan SWAT never wrote, on the page whose '
            'entire promise is that a guide writes you a real one. It is the '
            'same failure as a fake price. If a version of this ships it has '
            'to be visibly a <i>published trip</i> being shown to you, which '
            'is option B.</p>',
            cost='3 days', risk='Invents an itinerary SWAT never wrote',
            mockup=m.mock(_extra('itin') + m.ring(1, '.m-draft'),
                          1120, aw=900)),
    ],
    verdict([
        '<b>C</b> for the look, and I would build <b>B</b> alongside it — they '
        'are the same half of the page and B is half a day once C&rsquo;s '
        'panel exists. C is what makes the page feel alive; B is what makes it '
        'earn money.',
        'Say <b>&ldquo;34 goes to C and B&rdquo;</b> if you want both, or just '
        'C.',
        '<b>D</b> is a no from me and I would like that on the record — it '
        'prints a plan nobody at SWAT wrote, on the page that promises a real '
        'one.',
    ]),
    since=NEW))


# =====================================================================
# 35 — "Activity level on request"
# =====================================================================
#
# Authored at 760 for the same reason decision 20 was: the argument is a 20px
# spec row inside a 350px card.

ALL.append(dec(
    35,
    '&ldquo;Activity level on request&rdquo; on a card',
    [('Home shelf and every listing', ''), ('Crow', 'who'),
     ('2 hours, or a data job', ''), ('4 of 8 cards', 'big')],
    [quote(['For the home page, where the activity level on request — I just '
            'think we should figure out how to put something better there. A '
            'lot of them have it and I don&rsquo;t really like it.'],
           'Crow, 16 September')],
    [
        opt('Empty track, as now',
            ['A trip with no published level prints <b>&ldquo;Activity level '
             'on request&rdquo;</b> beside an <b>empty four-segment '
             'mark</b>.',
             '<b>4 of the 8 cards</b> on the home shelf say it today.',
             'Sitewide it is <b>42 of the 74 published trips</b> — more than '
             'half the catalogue.',
             'The empty mark was deliberate in decision 20: a missing level '
             'should look missing rather than look Easy.'],
            '<p>The logic was right and the result is what you are looking at: '
            'half the shelf carrying an empty gauge and a phrase that answers '
            'nothing. It draws the eye precisely because it is blank.</p>',
            cost='&mdash;', risk='Half the shelf says "we do not know"',
            cls='now',
            mockup=m.mock(c.shelfpair('now') + m.ring(1, '.m-meter'),
                          520, aw=760)),
        opt('The row disappears',
            ['Where there is no level, the <b>row is not drawn</b> — the card '
             'shows two spec lines instead of three.',
             'Nothing on the shelf says &ldquo;we do not know&rdquo;.',
             'Two hours of work.',
             'Cards now have <b>different heights</b> in the same row, or a '
             'gap where the row was.'],
            '<p>The obvious fix, and it breaks the one thing the card grid is '
            'built on: every card is the same height so the eye reads down a '
            'column rather than across three different shapes. Leaving the gap '
            'keeps the height and looks like a rendering bug.</p>',
            cost='2 hours', risk='Breaks the shelf baseline',
            mockup=m.mock(c.shelfpair('drop'), 520, aw=760)),
        opt('The slot carries something we do know',
            ['Where the level is missing, the row prints a fact the trip '
             '<b>does</b> publish — where it departs from.',
             'Same three rows, same card height, same baseline across the '
             'shelf.',
             'Nothing empty, nothing invented, and no level implied.',
             'The pop-up still exists on the graded trips.'],
            '<p>This is the honest version. A missing activity level is not '
            'information worth a row, and the departure city is — it is the '
            'second thing people filter on after the place.</p>'
            '<p>It does not fix the underlying problem, which is that 42 trips '
            'have no level. It stops the shelf advertising that fact.</p>',
            cost='Half a day', risk='Papers over a data gap',
            cls='rec',
            mockup=m.mock(c.shelfpair('swap') + m.ring(1, '.m-swap'),
                          520, aw=760)),
        opt('Publish the levels',
            ['SWAT grades the <b>42 trips</b> that have no level.',
             'Every card prints a real mark. The phrase disappears because the '
             'condition disappears.',
             'It is <b>not a code change</b> — it is a spreadsheet and a '
             'sign-off.',
             'Operations already has to read and approve the four guidance '
             'paragraphs before launch, so this rides with work that has to '
             'happen anyway.'],
            '<p>The actual fix, and it is not mine to do. Forty-two levels, '
            'four options each, and somebody at SWAT who knows the trips. It '
            'is an afternoon for the right person.</p>'
            '<p>This is also a safety item rather than a design one: '
            '[ops]&rsquo;s reason for the whole activity feature was people '
            'booking hiking trips while using a walker.</p>',
            cost='SWAT: an afternoon', risk='Blocked on someone at SWAT',
            mockup=m.mock(c.shelfpair('filled'), 520, aw=760)),
    ],
    verdict([
        '<b>C</b> today, <b>D</b> as the thing that actually closes it. They '
        'are not alternatives — C is what the shelf does until D happens, and '
        'if D happens C never fires.',
        'Say <b>&ldquo;35 goes to C&rdquo;</b> and I will ship it this week. '
        'The half of this that matters more is getting the 42 levels out of '
        'somebody at SWAT — it is on the waiting list at the bottom of this '
        'sheet.',
        '<b>B</b> is the one to avoid. Losing a row on half the cards costs '
        'the shared baseline the whole grid is built on.',
    ]),
    since=NEW, cols=2))


# =====================================================================
# 36 — the tour page top, and the review bar
# =====================================================================

ALL.append(dec(
    36,
    'The title, the price panel, and a review bar',
    [('Every tour page', ''), ('Crow', 'who'), ('1 day', ''),
     ('34px of slack', 'big')],
    [quote(['You see the photo on the left-hand side, then you have the title '
            'and then the reserve a place. I think we should make the reserve '
            'a place a little bit smaller and the title a little bit smaller, '
            'so then we can fit like a small bar for reviews there that slowly '
            'kind of moves to the right — instead of where it currently is.'],
           'Crow, 16 September, on the Great Salt Lake and Antelope Island '
           'tour')],
    [
        opt('Title, price, and reviews 1,700px down',
            ['Gallery <b>672&times;380</b>. Title column <b>395px</b> beside '
             'it.',
             'The h1 is <b>34px and 75px tall</b> on this trip; the price '
             'panel is <b>184px</b>.',
             'The column ends at <b>y=601</b> against a gallery bottom of '
             '<b>y=635</b> — there are already <b>34px</b> of unused paper '
             'there.',
             'Reviews are a full band at <b>y=1,764</b>, three cards, 326px '
             'tall.'],
            '<p>The band is where decision 26 put it and it is doing a '
            'different job — it is where somebody <i>reads</i> reviews. What '
            'is missing is the thing that makes the price panel believable at '
            'the moment somebody looks at the price.</p>',
            cost='&mdash;', risk='No proof beside the price', cls='now',
            mockup=m.mock(m.header() + m.backbar() +
                          c.tourtop('now') + m.ring(1, '.m-pricebox'),
                          640)),
        opt('A rating chip above the title',
            ['A small <b>&#9733; 4.9 &middot; 38 reviews</b> pill sits between '
             'the badges and the title.',
             'Nothing moves. Nothing shrinks. Two hours.',
             'Links down to the band.',
             'No quote, no movement — a number, not a voice.'],
            '<p>The cheap version, and it puts the score where the decision is '
            'made. What it does not do is what you described: there is no bar '
            'and nothing moves.</p>',
            cost='2 hours', risk='A score is not a review',
            mockup=m.mock(m.header() + m.backbar() +
                          c.tourtop('chip') + m.ring(1, '.m-revchip'), 640)),
        opt('A moving bar under the price panel',
            ['Title drops <b>34px &rarr; 25px</b>; on this trip that is two '
             'lines instead of two taller lines, saving <b>18px</b>.',
             'Price panel tightens from <b>184px to about 150px</b> — same '
             'price, same button, less padding.',
             'A <b>52px review bar</b> takes the freed space and sits '
             '<b>flush with the bottom of the gallery</b>.',
             'Quotes drift right slowly and pause on hover; the score and '
             'count stay fixed at the left.'],
            '<p>This is the shape you described, and it costs the page no '
            'height at all — the 34px already sitting empty plus the 52px '
            'freed by shrinking two things pays for the whole bar.</p>'
            '<p>Two rules I would hold it to. It stops on hover and on focus, '
            'and it respects <i>reduce motion</i> — this audience skews older '
            'and a crawling line of text is the kind of thing that gets read '
            'twice and then resented.</p>',
            cost='1 day', risk='Motion beside the buy button',
            cls='rec',
            mockup=m.mock(m.header() + m.backbar() +
                          c.tourtop('under') + m.ring(1, '.m-revbar'), 640)),
        opt('The bar spans both columns',
            ['Same bar, but the <b>full 1,100px</b> under the gallery and the '
             'price panel together.',
             'Room for a whole sentence rather than a clause.',
             'Reads as a shelf under the first screen, which is a stronger '
             'visual break.',
             'Pushes everything below it down by about <b>68px</b>, on a page '
             'that is already 9,697px.'],
            '<p>Better typography, worse economy. The wide bar is genuinely '
            'nicer to read and it is the only one of these that costs the page '
            'real height — and this page is already the longest on the '
            'site.</p>',
            cost='1 day', risk='68px added to a 9,697px page',
            mockup=m.mock(m.header() + m.backbar() +
                          c.tourtop('wide') + m.ring(1, '.m-revbar'), 720)),
    ],
    verdict([
        '<b>C</b> — it is what you described, and the measurement says it is '
        'free: 34px of that column is already empty, and shrinking the title '
        'and the panel finds the other 52px.',
        'The band at y=1,764 <b>stays</b>. The bar and the band are not the '
        'same thing: the bar is proof beside the price, the band is where '
        'somebody actually reads three reviews. Losing the band to gain the '
        'bar would be a downgrade.',
        'One honest flag: <b>every word in both is placeholder.</b> There are '
        'zero real reviews in the record — the band renders sample text and '
        'says so. Matt owes the picks, per tour, and until they arrive this '
        'ships as a working bar full of example text.',
    ]),
    since=NEW, cols=2))


# =====================================================================
# 37 — "Is this trip right for you?"
# =====================================================================

def _tour(rfymode, low=False):
    blocks = [m.notice()]
    if rfymode == 'line':
        blocks.append(c.rfy('line'))
    elif rfymode in ('full', 'fold'):
        blocks.append(c.rfy(rfymode))
    blocks.append(c.prose('Overview', 3))
    blocks.append(c.prose('The Experience: Beauty, History and Conservation', 3))
    if low:
        blocks.append(c.rfy('full'))
    blocks.append(c.prose('Tour details', 2))
    return (m.header() + m.backbar() + c.tourtop('now') +
            m.factstrip() + m.subnav() + c.tourcol(blocks))


ALL.append(dec(
    37,
    'Where &ldquo;Is this trip right for you?&rdquo; goes',
    [('Every tour page', ''), ('Crow, against [ops]', 'who'),
     ('Half a day', ''), ('267px', 'big')],
    [quote(['Instead of adding &ldquo;is this trip right for you&rdquo;, I '
            'think that just takes up too much space. I think we should remove '
            'that, or find a better place — more closer to the bottom, which I '
            'think would make more sense.'], 'Crow, 16 September'),
     quote(['One of the things that we run into a problem with is we have '
            'people who will book a hiking trip when they use a walker, or '
            'they&rsquo;ll book a Yellowstone but they&rsquo;re in a '
            'wheelchair.'],
           'SWAT operations, 16 September — the reason it exists')],
    [
        opt('Under the facts, as now',
            ['A bordered panel at <b>y=1,185</b>, <b>267px tall</b>, above the '
             'Overview.',
             'It is the first block of prose on the page.',
             'The card pop-ups and the booking rail both <b>link to it</b>.',
             'It is where decision 21 deliberately put it, over the '
             'alternative of burying it in Tour details.'],
            '<p>267px is a real cost and you are right that it is the first '
            'thing between the facts and SWAT&rsquo;s own description of the '
            'trip. It is also the one block on the page that exists for a '
            'safety reason rather than a selling one.</p>',
            cost='&mdash;', risk='Delays the trip description', cls='now',
            mockup=m.mock(_tour('full') + m.ring(1, '.m-rfy'), 1560)),
        opt('Remove it',
            ['The panel goes. <b>267px back</b> on every tour page.',
             'Overview becomes the first thing under the facts, which is what '
             'the page did before September.',
             'The activity level still appears as a word in the fact strip and '
             'in the booking rail.',
             'The card pop-up keeps its sentence — but its <b>&ldquo;what the '
             'levels mean&rdquo; link has nowhere to go</b>.'],
            '<p>Cleanest page of the four. What it costs is the only place on '
            'the site where the ground, the distance and who a trip is not '
            'suitable for are stated in full.</p>'
            '<p>I will build it if you say so. I want it on the record that it '
            'undoes the thing operations asked for by name, and that the '
            'guidance text they are being asked to sign off would then appear '
            'only in a hover panel.</p>',
            cost='2 hours', risk='Removes the safety answer entirely',
            mockup=m.mock(_tour('none'), 1420)),
        opt('One line up top, the panel down low',
            ['Under the facts it becomes <b>one line</b>: the mark, the '
             'plain-English summary, and a link.',
             'That line is about <b>44px</b> — it gives back <b>223px</b> of '
             'the 267.',
             'The full panel moves <b>below the Overview and the trip '
             'description</b>, around y=3,800.',
             'Every existing link — the cards, the rail — still lands on the '
             'full panel.'],
            '<p>The compromise that does not cost anything real. The sentence '
            'somebody needs before they book — <i>not suitable for a '
            'wheelchair</i> — stays on the first screen of prose. The 267px of '
            'detail moves to where you asked for it.</p>'
            '<p>Somebody deciding whether to bring their mother gets the '
            'answer in one line and can read the rest if they want it.</p>',
            cost='Half a day', risk='Two places to keep in step',
            cls='rec',
            mockup=m.mock(_tour('line', low=True) + m.ring(1, '.m-rfyline') +
                          m.ring(2, '.m-rfy'), 1740)),
        opt('Fold it',
            ['Stays exactly where it is, collapsed to its <b>heading plus one '
             'line</b>, opening on a click.',
             'About <b>96px</b> instead of 267.',
             'One place to maintain, not two.',
             'A closed panel is a panel most people never open.'],
            '<p>Cheapest way to get the height back. The catch is that a fold '
            'makes the important sentence conditional on a click, and this is '
            'the one section on the page where somebody not reading it has a '
            'consequence.</p>',
            cost='3 hours', risk='Nobody opens a fold',
            mockup=m.mock(_tour('fold') + m.ring(1, '.m-rfy'), 1460)),
    ],
    verdict([
        '<b>C</b>. You get the space back — 223 of the 267px — and the one '
        'sentence that stops a wrong booking stays where somebody will see '
        'it.',
        'This is the only decision in the round where you and SWAT operations '
        'want different things, so it is worth being explicit: they asked for '
        'this panel, high up, because of people booking hiking trips while '
        'using a walker. C is me trying to give you both. If you would rather '
        'just have it gone, say <b>37 goes to B</b> and I will build that — '
        'but I would want Jason or [ops] copied when it ships.',
    ], warn=True),
    since=NEW))


# =====================================================================
# 38 — the home band, when the photographs vanish
# =====================================================================

ALL.append(dec(
    38,
    'Start where you are, after the first tap',
    [('Home page', ''), ('Crow', 'who'), ('1-2 days', ''),
     ('4 photos &rarr; 0', 'big')],
    [quote(['For the home page, where the start where you are — again I think '
            'we can make this better. I don&rsquo;t like how the images '
            'disappear and then it asks you the different states. I think the '
            'buttons for the states can be organised better.'],
           'Crow, 16 September')],
    [
        opt('The photos are replaced, as now',
            ['Four <b>263&times;197 photographs</b> are the four ways in.',
             'Tapping one <b>replaces all four</b> — the section is left with '
             '<b>zero images in it</b>.',
             'In their place: <b>15 pills in 3 rows</b>, right edges at '
             '<b>1137, 414 and 94</b> inside a 1,099px column.',
             'The last row holds one state and a Back link, with 1,000px of '
             'paper beside them.'],
            '<p>Both halves of what you said, measured. The band goes from '
            'four photographs to none in one tap, and what arrives instead is '
            'three rows that end a thousand pixels apart.</p>'
            '<p>The photographs were the reason the band worked — it is the '
            'only place on the home page that looks like a choice rather than '
            'a list.</p>',
            cost='&mdash;', risk='The best-looking band empties itself',
            cls='now',
            mockup=m.mock(c.starthere('now') + m.ring(1, '.m-chips'), 700)),
        opt('The door you chose stays',
            ['The chosen door <b>shrinks to a photo card on the left</b> and '
             'the answers sit beside it.',
             'One photograph survives, and it says which question you are '
             'answering.',
             'Cheapest of the three.',
             'The answers are still <b>ragged pills</b> unless decision 32 '
             'lands with it.'],
            '<p>Fixes the disappearing half and leaves the organised half to '
            'decision 32. Worth knowing that C fixes both on its own.</p>',
            cost='1 day', risk='Still a wrapped pill row',
            mockup=m.mock(c.starthere('keep') + m.ring(1, '.m-keep-ph'), 640)),
        opt('The answers are photographs too',
            ['The 15 states become <b>15 small photo tiles, five across</b>.',
             'The band <b>never loses its pictures</b> — it gains eleven.',
             'Three ragged rows become <b>a grid with one right edge</b>.',
             'Every tile needs a photograph that is genuinely of that state.'],
            '<p>Answers both halves of the complaint with one change, and it '
            'makes the home page&rsquo;s best band better rather than less '
            'bad. Somebody who does not know where they want to go is now '
            'looking at fifteen reasons rather than fifteen words.</p>'
            '<p>The condition attached: <b>provenance</b>. A tile labelled '
            'Montana has to be Montana. The day tours site shipped Bolivian '
            'stock as the Bonneville Salt Flats, and the fix was a script that '
            'checks every photo against its claimed place. That script runs on '
            'these fifteen before they ship.</p>',
            cost='2 days', risk='15 photographs to verify, one by one',
            cls='rec',
            mockup=m.mock(c.starthere('tiles') + m.ring(1, '.m-stiles'), 780)),
        opt('All four doors stay, answers open underneath',
            ['Nothing is replaced. The chosen door is <b>outlined</b> and the '
             'answers open below the row.',
             'All four photographs stay on screen the whole way through.',
             'You can change your mind without pressing Back.',
             'The band grows by about <b>180px</b> and the answer is below the '
             'fold on a laptop.'],
            '<p>The most honest reading of &ldquo;do not make the images '
            'disappear&rdquo; — they simply never do. The cost is height, and '
            'on a phone the answers open off screen, which is the exact '
            'problem the band already has a scroll workaround for.</p>',
            cost='1 day', risk='The answer opens below the fold',
            mockup=m.mock(c.starthere('under') + m.ring(1, '.m-underq'), 840)),
    ],
    verdict([
        '<b>C</b>. It is the only one that answers both things you said with a '
        'single change, and it turns the weakest moment in the band into the '
        'strongest.',
        'It carries one condition I will hold to whatever you pick: fifteen '
        'state photographs, each verified as actually being that state before '
        'it ships. That check already exists as a script.',
        'If two days is too much this week, <b>B</b> is one day and gets the '
        'photograph back; the ragged rows are then fixed by decision 32 '
        'anyway.',
    ]),
    since=NEW))


# =====================================================================
# 39 — the film beside SWAT's own paragraph
# =====================================================================

def _home(mode):
    return ('<div class="m-band sand"><div class="m-shell">'
            + m.h2('The parks we guide', more='Every destination &rarr;')
            + m.parkrow(4) + '</div></div>'
            + c.withswat(mode))


ALL.append(dec(
    39,
    'The highlights film, beside SWAT&rsquo;s own words',
    [('Home page', ''), ('Crow', 'who'), ('Half a day', ''),
     ('No film exists yet', 'big')],
    [quote(['Below the parks we guide on the home page, the next section below '
            'is With Southwest Adventure Tours. On the right-hand side, this '
            'is where we wanted to put like a highlights video — so put a '
            'space for a video to go.'], 'Crow, 16 September')],
    [
        opt('Full-width paragraph, as now',
            ['SWAT&rsquo;s own sentence from the archived home page, then one '
             'paragraph, across the full measure.',
             'The section is <b>359px tall</b> at y=4,580.',
             'It is text on white, directly under four photographs.',
             'Nothing on the right. The section is <b>half empty at 1200px</b> '
             'and more so above that.'],
            '<p>The words are SWAT&rsquo;s, recovered from the archive, and '
            'they are not being rewritten. What is wrong with the section is '
            'that a 68-character measure inside a 1,100px shell leaves a third '
            'of the band blank.</p>',
            cost='&mdash;', risk='Half a band of white paper', cls='now',
            mockup=m.mock(_home('now') + m.ring(1, '.m-swatone'), 900)),
        opt('Copy left, film right',
            ['The paragraph keeps the left, a <b>520&times;293 film slot</b> '
             'takes the right.',
             'The copy measure stays inside the 68 characters it is set for.',
             'Section height is <b>unchanged</b> — 293px of film against 300px '
             'of copy.',
             'Until a cut exists it renders a <b>still with a play button</b>, '
             'behind a flag — never an empty box.'],
            '<p>Exactly what was asked for, and the proportions work out '
            'almost exactly: the copy and the film are the same height, so the '
            'band does not grow.</p>'
            '<p>It also matches the slot built for the About page in decision '
            '27, so there is one film component rather than two.</p>',
            cost='Half a day', risk='Needs a film that does not exist yet',
            cls='rec',
            mockup=m.mock(_home('right') + m.ring(1, '.m-film'), 900)),
        opt('Film left, copy right',
            ['Same two columns, swapped.',
             'The film is the first thing the eye lands on after four '
             'photographs.',
             'Same height, same cost.',
             'Pushes the only paragraph about who SWAT is to the right of the '
             'page.'],
            '<p>Stronger visually and weaker structurally. The left edge is '
            'where every other section on this page starts its words, and '
            'putting a picture there breaks the column the whole home page '
            'reads down.</p>',
            cost='Half a day', risk='Breaks the page’s left edge',
            mockup=m.mock(_home('left'), 900)),
        opt('A full-width film band',
            ['The paragraph sits <b>over</b> a wide still, with a large play '
             'button.',
             'The most cinematic thing on the home page.',
             'Band grows to about <b>340px</b>, roughly what it is now.',
             'SWAT&rsquo;s own paragraph becomes white text on a photograph — '
             'and most of it has to be cut to fit.'],
            '<p>It looks the best in a screenshot and it costs the section its '
            'words. That paragraph is one of very few pieces of SWAT&rsquo;s '
            'own writing on the home page, and this reduces it to a '
            'caption.</p>',
            cost='1 day', risk='The paragraph shrinks to a caption',
            mockup=m.mock(_home('band'), 900)),
    ],
    verdict([
        '<b>B</b> — and it is the one you described. The proportions happen to '
        'be right: the film and the paragraph are the same height, so nothing '
        'below moves.',
        'The thing to know is that <b>there is no film</b>. Not on this page, '
        'not on the About page, not for any tour. The slot ships behind a flag '
        'that renders nothing at all until a cut exists, so the home page '
        'never shows an empty frame to a customer.',
        'Matt is the person with the footage and the film background. One cut '
        'unlocks three slots — here, About, and the tour hero from decision '
        '27.',
    ]),
    since=NEW))
