"""Decisions 20-24 — activity level, seasons, and the state picker.

Each "Now" panel is the deployed staging build measured at 1200px on
16 September 2026. Authored widths differ per decision on purpose: decision 20
is an argument about a 20px row inside a 350px card, so shrinking it into a
1200px canvas would have argued itself out of its own case.
"""

import mocks as m
from sheetkit import opt, quote, verdict, dec

ALL = []


# =====================================================================
# 20 — the activity mark on a card
# =====================================================================
#
# Authored at 620px: one card at its real 350px beside the pop-up. The thing
# being judged is a single spec row, and a row of three cards scaled into a
# sheet column renders it at four pixels tall.

def _one(trip, mark_kind):
    photo, style, dur, title, route, place, act, group, price = trip
    if mark_kind is None:
        mark = f'<span class="s">Activity level {act}</span>'
    else:
        mark = f'<span class="s">{m.meter(act, mark_kind)}</span>'
    return (f'<div class="m-card" style="width:350px">'
            f'<div class="m-card-ph" style="height:219px">'
            f'{m.img(photo, 700, 438)}'
            f'<span class="m-badge">{style}</span>'
            f'<span class="m-dur">{dur}</span></div>'
            f'<div class="m-card-b"><div class="m-card-t">{title}</div>'
            f'<div class="m-card-r">{route or "&nbsp;"}</div>'
            f'<div class="m-card-s"><span class="s">{place}</span>'
            f'{mark}<span class="s">{group}</span></div>'
            f'<div class="m-card-p"><b>{price}</b><span>from / person</span></div>'
            f'<div class="m-card-go"><span>View tour</span>'
            f'<span>Check dates</span></div></div></div>')


def _card(mark_kind=None, hover=False, ring=''):
    """Two cards off the live November shelf, side by side.

    The pair is the argument: the Mighty 5 from Las Vegas is Easy and the same
    trip from Salt Lake City is Strenuous, and on the shelf today those two
    look identical. One card on its own cannot show that."""
    cards = _one(m.FEATURED[0], mark_kind) + _one(m.FEATURED[2], mark_kind)
    hv = ''
    if hover:
        hv = ('<div class="m-hover" style="left:398px;top:300px">'
              '<b>Easy</b><p>Short walks on made paths and boardwalks, under a '
              'mile at a time, with the vehicle never far away. Fine with a '
              'walking stick; <b>not suitable for a wheelchair or a walker</b>.'
              '</p><a>What the levels mean &rsaquo;</a></div>')
    return (f'<div class="m-cardpair" style="padding:26px 0 26px 26px;'
            f'position:relative;background:#fff;display:flex;gap:24px;'
            f'align-items:flex-start">'
            f'{cards}{hv}{ring}</div>')


ALL.append(dec(
    20,
    'How hard is this trip, on the card',
    [('Home shelf, every listing page', ''), ('Matt &amp; the sales team', 'who'),
     ('Half a day', ''), ('Safety, not decoration', 'big')],
    [quote(['one of the things that we run into a problem up with is we have '
            'people who will book a hiking trip when they use a walker, or '
            'they&rsquo;ll book a Yellowstone but they&rsquo;re in a '
            'wheelchair.',
            'maybe little boot icons or something like that that represent our '
            'activity level.'], 'SWAT operations'),
     quote(['I don&rsquo;t think boots is the right one.',
            'and I don&rsquo;t want something showing it three stars, because '
            'people think it will be a rating &mdash; like how good the tour '
            'is.'], 'Matt, and [ops] agreeing')],
    [
        opt('Words only, as now',
            ['The card prints <b>Activity level Easy</b> as the middle of three '
             'grey spec lines, in the same weight as the group size.',
             'These two trips are on the same shelf today. One is <b>Easy</b> '
             'and one is <b>Strenuous</b>, and nothing about them looks '
             'different.',
             'Three of the eight cards say <b>on request</b>, which reads as no '
             'answer at all.',
             'Nothing to hover, nowhere to go.'],
            '<p>It is accurate and it is invisible. On the live shelf the '
            'activity line sits between &ldquo;Zion National Park, Bryce '
            'Canyon&hellip;&rdquo; and &ldquo;Small group, 7&ndash;13&rdquo; at '
            '13px grey &mdash; the eye goes to the photograph, the title and '
            'the price, in that order.</p>'
            '<p>Three of the eight trips on the shelf today say <b>on '
            'request</b>, which tells a customer with a walker nothing at all.</p>',
            cost='&mdash;', risk='The booking it is meant to prevent still happens',
            cls='now',
            mockup=m.mock(_card(None, ring=m.ring(1, '.m-card-s')),
                          560, aw=760)),
        opt('A three-step mark',
            ['Three segments beside the word, filling left to right, '
             '<b>green &rarr; amber &rarr; rust</b>.',
             'Reads at a glance without reading: a scan of the shelf now sorts '
             'itself into easy and hard.',
             '<b>on request</b> shows an empty track rather than a filled one, '
             'so a missing level looks missing.',
             'Not boots, not stars: three of anything horizontal cannot be '
             'mistaken for a score out of five.'],
            '<p>The cheapest thing that answers the complaint. It goes on the '
            'card, the search results and the related row in one change, '
            'because all three render the same component.</p>'
            '<p>What it does not do is explain itself. A visitor who reads two '
            'filled segments still does not know whether their mother can '
            'manage it.</p>',
            cost='Half a day', risk='Still needs words somewhere',
            mockup=m.mock(_card('bars', ring=m.ring(1, '.m-meter')),
                          560, aw=760)),
        opt('The mark, and a pop-up',
            ['Same three-step mark.',
             'Hovering or tapping it opens <b>a short panel in plain '
             'English</b> &mdash; distance, ground, and who it is not suitable '
             'for.',
             'The panel&rsquo;s last line is a link through to the full '
             'explanation on the tour page (decision 21).',
             'On a phone it is a tap, not a hover, and it opens in place.'],
            '<p>This is [ops]&rsquo;s own sentence built literally: <i>&ldquo;a '
            'little call-out where they mouse over it and it says, this tour '
            'includes some level ground or uneven ground walking, so a walker '
            'would not be appropriate.&rdquo;</i></p>'
            '<p>The words are SWAT&rsquo;s, and they matter more than the '
            'graphic. Three sentences per level, written once, used on every '
            'card in the catalogue.</p>',
            cost='1 day + 3 short paragraphs from SWAT',
            risk='Wrong words here are a promise, so ops has to write them',
            cls='rec',
            mockup=m.mock(_card('bars', hover=True,
                                ring=m.ring(1, '.m-hover')), 560, aw=760)),
        opt('A terrain slope',
            ['The mark is a rising slope rather than segments &mdash; flat for '
             'easy, steep for strenuous.',
             'Same colours, same pop-up behaviour as the option beside it.',
             'One glyph instead of three, so it takes less width on a phone.'],
            '<p>Prettier, and more literal &mdash; it looks like the thing it '
            'describes. The risk is that a slope reads as elevation gain '
            'specifically, which is not what the level means: a flat six-mile '
            'walk in 104&deg;F is strenuous and this drawing would call it '
            'easy.</p>',
            cost='Half a day', risk='Reads as elevation, which is not the rating',
            mockup=m.mock(_card('slope', ring=m.ring(1, '.m-slope')),
                          560, aw=760)),
    ],
    verdict([
        'Take <b>C</b>. The graphic is the smaller half of this: the room '
        'talked itself from boots to stars to nothing in about ninety seconds, '
        'and what survived was the sentence &mdash; <i>&ldquo;a walker would '
        'not be appropriate&rdquo;</i>. That is a words problem with a small '
        'picture attached, not the other way round.',
        'Three segments because they cannot be counted as a score; a pop-up '
        'because it is where the useful sentence fits; and a link out of the '
        'pop-up because the full answer belongs on the tour page, which is '
        'decision 21.',
        '<b>What I need from SWAT:</b> three short paragraphs, one per level, '
        'saying distance, ground and who should not book it. I can draft them '
        'off the itineraries, but ops has to own the wording &mdash; this is '
        'the one thing on the sheet where being wrong has a consequence '
        'beyond looking bad.',
    ]),
    since=('New', '16 Sep'), cols=2))


# =====================================================================
# 21 — where the explanation lives on the tour page
# =====================================================================

def _tourpage(panel='', sub_active='Overview', extra_nav=None, rings=''):
    nav = extra_nav or ['Overview', 'Day by day', 'Tour details', 'More photos',
                        'Reserve a place', 'Departures', 'Pricing']
    body = (panel +
            '<h2 class="m-h2" style="margin-top:22px">Overview</h2>'
            '<p style="margin:10px 0 0;font-size:16px;line-height:1.6;'
            'color:var(--ink700)">By joining one of our most popular tours, '
            'Southwest Adventure Tours will guide you through Utah&rsquo;s '
            'five national parks in five days, staying in Springdale, Bryce '
            'and Moab, with a guide who has driven these roads for a '
            'decade.</p>')
    return ('<div style="background:#fff">' + m.subnav(nav, sub_active) +
            m.factstrip() +
            m.twocol(body, m.rail()) + rings + '</div>')


ALL.append(dec(
    21,
    'Where a tour page explains what the level means',
    [('Every tour page', ''), ('[ops], and Matt on the chatbot', 'who'),
     ('1&ndash;2 days + SWAT copy', ''), ('CUA exposure', 'blocked')],
    [quote(['one of the things that we can do is actually just have it be an '
            'anchor link to a section of the tour page that actually goes into '
            'an explanation of what would not be appropriate for that trip.',
            'I&rsquo;m also thinking of our chat bot and its information, and '
            'making sure that it has the information that it needs when it '
            'skims the site.'], 'SWAT operations'),
     quote(['our guides are authorised to make adjustments based off of whether '
            'they feel like a situation is unsafe&hellip; so if we&rsquo;re '
            'listing the hikes that are available at a particular park, then '
            'if that&rsquo;s not on our itinerary we run into a problem.',
            'we need to base all of that information off of our timing '
            'docs.'], 'SWAT operations')],
    [
        opt('One word, twice',
            ['The fact strip says <b>Activity level: Easy</b> and the booking '
             'rail repeats it. That is the whole of it.',
             'There is nothing for the card&rsquo;s pop-up to link to, and '
             'nothing for a chatbot or an AI answer to quote.',
             'The word is identical on a 1-day bison drive and an 8-day '
             'Mighty 5.'],
            '<p>Measured on the live page: the word appears at y=659 in the '
            'fact strip and again at y=1,181 in the rail, and nowhere else in '
            '11,468px of page.</p>',
            cost='&mdash;', risk='Nothing to anchor to, nothing to quote',
            cls='now',
            mockup=m.mock(_tourpage(rings=m.ring(1, '.m-factrow') +
                                    m.ring(2, '.m-r-spec')), 1000)),
        opt('A section under Tour details',
            ['A new <b>Activity level</b> block inside Tour details, beside '
             'what is included and excluded.',
             'The card&rsquo;s pop-up and the rail both anchor straight to it.',
             'One more item in the sticky sub-nav.'],
            '<p>It sits with the other contractual detail, which is tidy and '
            'which is where a reader looking for it would go second.</p>'
            '<p>The cost is depth. Tour details begins at <b>y=4,514</b> on the '
            'live page &mdash; four screens down. Someone deciding whether to '
            'bring their mother has already decided by then.</p>',
            cost='1 day', risk='Four screens below the decision it informs',
            mockup=m.mock(_tourpage(
                sub_active='Tour details',
                extra_nav=['Overview', 'Day by day', 'Tour details',
                           'Activity level', 'More photos', 'Departures'],
                rings=m.ring(1, '.m-subnav span:nth-child(4)')), 1000)),
        opt('A panel under the fact strip',
            ['A short <b>Is this trip right for you?</b> panel directly under '
             'the facts, above the Overview &mdash; the first thing after the '
             'summary.',
             'Names the ground, the longest walk, the altitude and who should '
             'not book, in four lines.',
             'The card pop-up and the rail both anchor here; so does the '
             'chatbot, because it is the first block of prose under the '
             'heading.',
             'Says explicitly that <b>the guide can change the day</b> &mdash; '
             'which is the CUA problem, answered in place rather than by '
             'listing trails.'],
            '<p>Puts the answer where the question is asked. It also happens to '
            'be the shape an AI answer engine lifts cleanly: a heading, a '
            'short list, no navigation around it.</p>'
            '<p>And it lets SWAT stop naming specific trails. The room worked '
            'out on the call that listing hikes creates a promise the CUA may '
            'not permit next season; a panel about <i>ground and distance</i> '
            'does not go out of date when the permit changes.</p>',
            cost='1&ndash;2 days + copy', risk='Pushes the Overview one screen down',
            cls='rec',
            mockup=m.mock(_tourpage(panel=(
                '<div style="border:1px solid var(--sand300);border-left:4px '
                'solid var(--rust600);border-radius:3px;padding:16px 20px 18px;'
                'margin-top:4px">'
                '<div style="font-size:19px;font-weight:800;color:var(--ink900)">'
                'Is this trip right for you?</div>'
                '<div style="margin-top:10px;display:flex;gap:12px;'
                'align-items:center">' + m.meter('Easy', 'bars') +
                '<span style="font-size:13px;color:var(--ink300)">'
                'Level 1 of 3</span></div>'
                '<ul style="margin:12px 0 0;padding-left:18px;font-size:14.5px;'
                'line-height:1.6;color:var(--ink700)">'
                '<li>Made paths and boardwalks. The longest walk on any day is '
                'about a mile, and the vehicle is never far away.</li>'
                '<li>Two viewpoints sit above 8,000ft. Nothing is scrambled, '
                'roped or exposed.</li>'
                '<li><b>Not suitable for a wheelchair or a walker.</b> Fine '
                'with a walking stick, and tell us when you book.</li>'
                '<li>Your guide may change or drop a stop for weather, road '
                'closures or time. What is walked on the day is their call.</li>'
                '</ul></div>'),
                rings=m.ring(1, '.m-2l > div:first-child')), 1000)),
    ],
    verdict([
        'Take <b>C</b> &mdash; and note that it quietly solves the CUA problem '
        'the room ran into ten minutes later.',
        'The trap in <b>B</b> is not the layout, it is that a section of that '
        'kind invites a list of named trails, and [ops] talked the room out of '
        'that on the call: the permit changes yearly, the guide can drop a stop '
        'on the day, and both of those turn a printed trail name into a '
        'complaint. A panel about ground, distance and altitude says the useful '
        'thing without naming anything that can be withdrawn.',
        '<b>Still open, and it is not mine:</b> somebody has to own re-reading '
        'each CUA against the site every season. If nobody does, this panel '
        'goes stale silently &mdash; and a stale safety claim is worse than '
        'none.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 22 — seasons on a tour page
# =====================================================================

ALL.append(dec(
    22,
    'Showing a trip in the season you would travel it',
    [('Tour pages that run year-round', ''), ('[ops] &amp; Lance', 'who'),
     ('1 week + photography', ''), ('Needs 4 photos a tour', 'blocked')],
    [quote(['should we have a season section so people can look at different '
            'imagery for different seasons? I would love it.',
            'we could potentially push more shoulder season trips, if people '
            'saw that it&rsquo;s visible and not as crowded.'],
           'SWAT operations, and Lance'),
     quote(['when somebody books a trip in July it&rsquo;s over 100 degrees, '
            'it&rsquo;s unbearable, versus like a May or October. So it&rsquo;d '
            'be nice to document: hey, just so you know, it&rsquo;s a summer '
            'trip, it&rsquo;s going to be over 100 degrees in some places, so '
            'people are aware.'], 'SWAT operations')],
    [
        opt('One season only',
            ['The gallery is five photographs and they are all from whenever '
             'the camera happened to be out.',
             'Nothing says the same trip runs in February, and nothing warns '
             'that July is over 100&deg;F.',
             'Winter departures are sold by a separate <b>Winter</b> trip '
             'style, which is where the four winter trips live.'],
            '<p>The catalogue already knows which trips run all year &mdash; '
            'the departure calendar has the dates. It is only the page that is '
            'silent about it.</p>'
            '<p>The cost of the silence is the thing Lance actually wants: '
            'July is one of SWAT&rsquo;s slower months <i>because</i> it is '
            'hot, and nothing on the page moves that customer to October.</p>',
            cost='&mdash;', risk='Shoulder season stays unsold',
            cls='now',
            mockup=m.mock(m.tourhero() + m.factstrip(), 700)),
        opt('Season tabs on the gallery',
            ['Four labels over the gallery. Tapping one <b>swaps the '
             'photographs</b> for that season.',
             'Only shown on trips that actually depart in more than one '
             'season.',
             'Nothing else on the page changes.'],
            '<p>The smallest true version: it answers &ldquo;what does this '
            'look like in October&rdquo; and nothing else.</p>'
            '<p>It is also the one that costs the most photography for the '
            'least explanation &mdash; four labelled sets per trip, and a '
            'visitor still has to work out for themselves that October is '
            'thirty degrees cooler.</p>',
            cost='3 days + 4 photo sets per trip',
            risk='Empty tabs on any trip without winter photographs',
            mockup=m.mock(m.tourhero(season_tabs=True) + m.factstrip(), 700)),
        opt('A season band under the facts',
            ['A <b>This trip by season</b> row: four photographs, each with '
             'one line about what that month is actually like.',
             'Names the heat &mdash; <i>over 100&deg;F in the canyons</i> '
             '&mdash; where a customer reads it before booking July.',
             'Each season links to the departures in it, so the band sells the '
             'shoulder month rather than only illustrating it.',
             'A trip that runs in one season prints one cell, not four empty '
             'ones.'],
            '<p>This is the version that does the commercial job. The tabs in '
            'option A change the picture; this changes the decision &mdash; it '
            'is the only place on the page where SWAT gets to say &ldquo;come '
            'in October instead&rdquo; and link to the dates.</p>'
            '<p>It also carries the heat warning [ops] asked for, in the one '
            'place where saying it is useful rather than alarming.</p>',
            cost='1 week + 4 photo sets per trip',
            risk='Photography is the gate, not the code',
            cls='rec',
            mockup=m.mock(m.tourhero() + m.factstrip() +
                          '<div class="m-shell" style="padding-top:24px">'
                          '<div class="m-h2" style="font-size:24px;font-weight:800;'
                          'color:var(--ink900)">This trip by season</div>'
                          '<p style="margin:6px 0 0;font-size:14.5px;'
                          'color:var(--ink500)">The same five days. Four very '
                          'different weeks.</p>' +
                          m.seasonrow('Autumn') + '</div>', 700)),
    ],
    verdict([
        'Take <b>C</b>, and be honest that the photographs are the project.',
        'The code is a week. Four labelled photograph sets for every trip that '
        'runs year-round is the real cost, and nobody in the room counted it '
        '&mdash; I have not either, because the library is not tagged by '
        'season. The first job is to find out how many trips can actually be '
        'illustrated four ways, and it may be that this ships on six tours '
        'rather than sixty.',
        '<b>Where it should not go:</b> the same four photographs on every '
        'Utah trip. If autumn on the Mighty 5 and autumn on the Grand Circle '
        'are the same frame, the band stops being information about a trip and '
        'becomes wallpaper.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 23 — where the season filter lives
# =====================================================================

STYLE_TILES = [
    ('Backpacking', '7 trips'), ('Guided small group', '30 trips'),
    ('Day tour', '12 trips'), ('Self-drive', '6 trips'),
    ('Private &amp; custom', '4 trips'), ('Large group', '3 trips'),
]


def _styletiles():
    cells = ''.join(
        f'<div style="border:1px solid var(--sand300);border-radius:3px;'
        f'padding:16px 18px;display:flex;align-items:baseline;gap:10px">'
        f'<b style="font-size:17px;color:var(--ink900)">{n}</b>'
        f'<span style="font-size:13px;color:var(--ink300)">{c}</span>'
        f'<span style="margin-left:auto;font-size:13px;font-weight:700;'
        f'color:var(--rust600)">Open</span></div>' for n, c in STYLE_TILES)
    return (f'<div class="m-grid3" style="display:grid;grid-template-columns:repeat(3,1fr);'
            f'gap:16px;margin-top:16px">{cells}</div>')


def _tripspage(filter_html='', rings=''):
    return ('<div style="background:#fff">' + m.header('Trip Styles') +
            m.ticker() +
            '<div class="m-shell" style="padding-top:26px;padding-bottom:30px">'
            '<div style="font-size:31px;font-weight:800;color:var(--ink900);'
            'letter-spacing:-.02em">Trip styles</div>'
            '<p style="margin:8px 0 0;font-size:16px;color:var(--ink500);'
            'max-width:740px">Eight ways to travel the same country. Pick the '
            'one that sounds like your kind of week.</p>'
            + filter_html + _styletiles() + '</div>' + rings + '</div>')


_WHEN = ('<div style="margin-top:22px;padding:14px 16px 16px;'
         'background:var(--sand100);border:1px solid var(--sand300);'
         'border-radius:3px">'
         '<div style="font-size:11px;font-weight:800;letter-spacing:.1em;'
         'color:var(--ink300)">WHEN DO YOU WANT TO TRAVEL</div>' +
         m.chips(['Spring', 'Summer', 'Autumn', 'Winter', 'Any time'],
                 on=('Autumn',)) + '</div>')

_BUILDER = ('<div class="m-filterbar" style="margin-top:22px;padding:16px 18px;'
            'background:var(--navy800);border-radius:3px;display:grid;'
            'grid-template-columns:repeat(4,1fr) auto;gap:12px;'
            'align-items:end">' +
            ''.join(
                '<div><div style="font-size:10px;font-weight:800;'
                f'letter-spacing:.1em;color:var(--navy300)">{lab}</div>'
                '<div style="margin-top:6px;background:#fff;border-radius:3px;'
                'padding:10px 12px;font-size:14px;color:'
                f'{"var(--ink900)" if val else "var(--ink300)"}">{val or ph}</div>'
                '</div>'
                for lab, val, ph in [
                    ('WHERE', 'Utah', 'Anywhere'),
                    ('WHEN', 'October', 'Any month'),
                    ('HOW LONG', '', '4&ndash;6 days'),
                    ('HOW YOU TRAVEL', '', 'Any style')]) +
            '<div class="m-cta" style="margin:0;padding:11px 22px">'
            'Show 14 trips</div></div>')


ALL.append(dec(
    23,
    'Filtering the catalogue by when you can travel',
    [('Trip Styles, Destinations, everywhere', ''), ('[ops] &amp; Lance', 'who'),
     ('3 days &ndash; 2 weeks', ''), ('Biggest build on the sheet', 'big')],
    [quote(['well, let&rsquo;s make it difficult for you and let&rsquo;s have '
            'it be everywhere.',
            'if I&rsquo;m going to trip styles and I&rsquo;m looking at these '
            'different guided small group, and I click into that and then '
            'I&rsquo;m able to sort by season or filter by season &mdash; that '
            'would be very handy. But if I&rsquo;m going to destinations, be '
            'able to do it, I love that too.'], 'SWAT operations'),
     quote(['even putting a filter up here as an option, that says how, when '
            'and why or where &mdash; and it just builds it for you.'],
           'SWAT operations, and Lance agreeing')],
    [
        opt('Season is a trip style',
            ['<b>Winter</b> is one of the eight style tiles, holding four '
             'trips. There is no other way to ask about time of year.',
             'A trip that runs all year appears under its style only, so '
             'October is invisible.',
             'Destinations has no time control at all.'],
            '<p>Measured on the live page: eight style tiles, three across, '
            'with counts &mdash; Guided small group 30, Day tour 12, Self-drive '
            '6, Large group 3.</p>'
            '<p>Treating Winter as a style is why the Mighty 5 cannot be found '
            'by someone who can only travel in February, even though it runs '
            'then.</p>',
            cost='&mdash;', risk='The shoulder-season pitch has nowhere to land',
            cls='now',
            mockup=m.mock(_tripspage(
                rings=m.ring(1, '.m-shell > div:last-child > div:nth-child(6)')),
                740)),
        opt('A season row on browse pages',
            ['One chip row &mdash; <b>Spring / Summer / Autumn / Winter</b> '
             '&mdash; above the tiles on Trip Styles and Destinations.',
             'Filters against the real departure dates, so a trip appears in '
             'every season it actually runs.',
             'The choice follows you from one browse page to the next.'],
            '<p>Three days, and it covers the two journeys [ops] described out '
            'loud. It is the smallest thing that is not a fudge.</p>'
            '<p>What it is not is the thing Lance answered &ldquo;yes&rdquo; '
            'to: it filters by one axis at a time, so &ldquo;six days in Utah '
            'in October&rdquo; still takes three clicks in three places.</p>',
            cost='3 days', risk='One axis at a time',
            mockup=m.mock(_tripspage(_WHEN, rings=m.ring(1, '.m-chips')), 740)),
        opt('One bar, four questions',
            ['A single dark bar on every browse page: <b>Where &middot; When '
             '&middot; How long &middot; How you travel</b>.',
             'Any combination narrows the catalogue at once, and the button '
             'says how many trips are left before you press it.',
             'Empty is a valid answer to every question &mdash; it never '
             'demands four answers to give you one.',
             'The same four questions as Build Your Own, so the two surfaces '
             'stop disagreeing about how SWAT thinks a trip is chosen.'],
            '<p>This is the room&rsquo;s own sentence: <i>&ldquo;how, when and '
            'why or where &mdash; and it just builds it for you&rdquo;</i>, '
            'and it is the version Lance said yes to.</p>'
            '<p>It is also the largest thing on this sheet. It needs a real '
            'query layer behind it, URLs that survive a share, and an empty '
            'state that offers a custom trip instead of an apology.</p>',
            cost='2 weeks', risk='Four filters and 93 trips can return nothing',
            cls='rec',
            mockup=m.mock(_tripspage(_BUILDER,
                                     rings=m.ring(1, '.m-filterbar')), 740)),
    ],
    verdict([
        'Take <b>C</b>, but ship <b>B</b> first if the launch date matters '
        'more than the feature.',
        'They are not alternatives so much as two stops on the same road: the '
        'season chips in B are one of the four questions in C, and building B '
        'first throws away nothing. If the site is going live in early '
        'October, B is in and C is the November update.',
        '<b>The part nobody costed:</b> an empty result. Four filters against '
        '93 trips will produce &ldquo;no trips match&rdquo; regularly, and '
        'that screen has to offer to build the trip instead &mdash; which is '
        'the one place Build Your Own belongs in the browse flow.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 24 — the state picker
# =====================================================================

_STATE_CHIPS = ['Alaska', 'Arizona', 'California', 'Canada', 'Colorado',
                'Hawaii', 'Montana', 'Nevada', 'New Mexico', 'Oregon',
                'South Dakota', 'Texas', 'Utah', 'Washington', 'Wyoming']

SEL = ('UT', 'AZ', 'CO')


def _builder(step1_body, rings='', rows=None):
    rows = rows or [('Where', 'Utah, Arizona, Colorado'),
                    ('How long', '7&ndash;10 days'),
                    ('How many', '3&ndash;6'), ('When', 'Autumn')]
    left = (m.step(1, 'Where would you like to go?', 'pick as many as you like',
                   step1_body) +
            m.step(2, 'How long do you have?', '',
                   m.chips(['Half day', '1 day', '2-3 days', '4-6 days',
                            '7-10 days', '11+ days'], on=('7-10 days',))) +
            m.step(3, 'How many of you?', '',
                   m.chips(['Just the two of us', '3&ndash;6', '7&ndash;13',
                            '14 or more'], on=('3&ndash;6',))))
    return ('<div style="background:#fff">'
            '<div class="m-shell" style="padding-top:24px;padding-bottom:28px">'
            '<div style="font-size:31px;font-weight:800;color:var(--ink900);'
            'letter-spacing:-.02em">Build your own trip</div>'
            '<p style="margin:8px 0 18px;font-size:16px;color:var(--ink500);'
            'max-width:760px">Tap through what you have in mind. Nothing is '
            'booked here &mdash; a guide reads it and comes back with a real '
            'itinerary and a real price.</p>'
            '<div class="m-2col" style="display:grid;'
            'grid-template-columns:1fr 320px;gap:40px;align-items:start">'
            f'<div>{left}</div>{m.sofar(rows)}</div></div>' + rings + '</div>')


ALL.append(dec(
    24,
    'Picking where you want to go',
    [('Build Your Own, step one', ''), ('[ops], seconded by Lance', 'who'),
     ('4&ndash;5 days', ''), ('Sales team reviews it Friday', 'new')],
    [quote(['you should just get a picture of the United States where you '
            'could highlight different states.',
            'I agree, this is a cool feature. I like this a lot.'],
           'SWAT operations, and Lance'),
     quote(['you can add every state &mdash; because we do custom tours across '
            'the country. We can even do some custom tours into Canada. '
            'It&rsquo;s a little harder for us, but we can do it.'],
           'SWAT operations')],
    [
        opt('Fifteen chips',
            ['Step one is a wrapped row of fifteen word-chips, alphabetical '
             '&mdash; Alaska through Wyoming, with <b>Canada</b> filed between '
             'California and Colorado.',
             'Nothing conveys where these places are in relation to each other, '
             'or that four of them are neighbours.',
             'The list is the only thing saying SWAT is nationwide; it reads '
             'as fifteen options, not as a country.'],
            '<p>This is what the sales team will open on Friday. It works, and '
            'it is dull &mdash; which matters here, because this page is the '
            'one the room got excited about and the one the map on the home '
            'page has already set an expectation for.</p>'
            '<p>Alphabetical order also buries the thing SWAT wants read: '
            '&ldquo;Canada&rdquo; between California and Colorado looks like a '
            'typo rather than a capability.</p>',
            cost='&mdash;', risk='Reads as a form, next to a home page with a map',
            cls='now',
            mockup=m.mock(_builder(m.chips(_STATE_CHIPS,
                                           on=('Utah', 'Arizona', 'Colorado')),
                                   rings=m.ring(1, '.m-chips')), 900)),
        opt('The map, on its own',
            ['Step one is <b>a map of the United States</b>. Click a state and '
             'it fills.',
             'Every state, not only the fifteen &mdash; because the answer to '
             '&ldquo;can you do Vermont?&rdquo; is yes.',
             '<b>Alaska and Hawaii</b> are inset at the bottom left, the way '
             'every US map does it.',
             'The chips are gone.'],
            '<p>The strongest possible version of the thing they asked for, and '
            'it says &ldquo;nationwide&rdquo; without a word of copy.</p>'
            '<p>Two things it loses. On a phone, Rhode Island is about four '
            'pixels wide &mdash; a map alone is not a usable control at 390px. '
            'And Canada is not on it, so the capability [ops] mentioned in the '
            'same breath disappears.</p>',
            cost='4 days', risk='Unusable on a phone; no room for Canada',
            mockup=m.mock(_builder(
                f'<div style="margin-top:12px">{m.nationmap(SEL, h=340)}</div>',
                rings=m.ring(1, '.m-map')), 900)),
        opt('Map and chips together',
            ['The map <b>and</b> the chip row, wired to each other &mdash; '
             'click the map, the chip lights; tap a chip, the state fills.',
             'The chips are what make it work on a phone, and what make it '
             'work with a keyboard.',
             'The chip row now leads with the states SWAT actually sells and '
             'ends with <b>Canada</b> and <b>Somewhere else</b>, which the map '
             'cannot hold.',
             'Selected states are labelled on the map itself, so the answer is '
             'readable without cross-checking the list.'],
            '<p>The map is the picture; the chips are the control. Keeping both '
            'costs a day over the map alone and removes every reason the map '
            'could not ship.</p>'
            '<p>&ldquo;Somewhere else&rdquo; is the important chip: it is how a '
            'request for Vermont or Banff reaches a planner instead of dying '
            'at a map of fifty states.</p>',
            cost='4&ndash;5 days', risk='Two controls for one answer must stay in step',
            cls='rec',
            mockup=m.mock(_builder(
                f'<div style="margin-top:12px">{m.nationmap(SEL, h=320, labels=True)}</div>'
                + m.chips(['Utah', 'Arizona', 'Nevada', 'Colorado', 'Wyoming',
                           'Montana', 'California', 'Oregon', 'Washington',
                           'New Mexico', 'South Dakota', 'Texas', 'Alaska',
                           'Hawaii', 'Canada', 'Somewhere else'],
                          on=('Utah', 'Arizona', 'Colorado')),
                rings=m.ring(1, '.m-map') + m.ring(2, '.m-chips')), 900)),
    ],
    verdict([
        'Take <b>C</b>. The map is the right answer and the chips are what stop '
        'it being a worse form than the one it replaces.',
        'Two details worth deciding now rather than later. <b>Every state '
        'is clickable</b>, not just the fifteen &mdash; a greyed-out Vermont '
        'says &ldquo;we do not go there&rdquo;, which is the opposite of what '
        'the room said. And <b>Canada and &ldquo;somewhere else&rdquo; live in '
        'the chips</b>, because a US map cannot hold either and both are real '
        'business.',
        '<b>Timing:</b> the sales team sees the current version on Friday. '
        'This does not have to be built before then &mdash; but if the answer '
        'comes back quickly it can be in front of them a week later, which is '
        'a better use of that meeting than asking them to imagine it.',
    ]),
    since=('New', '16 Sep')))
