"""Round fourteen, decisions 82-83: the Find a trip page's filters and its search box.

Crow, 30 September, with a screenshot of the filter column: "I don't really like
the bubbles, how can we make this look more clear and organized ... For the
search bar function on this page, how can we improve it to be more helpful, for
any new designs send me a decision sheet."

Like round thirteen these panels are NOT markup. Each one is the live
production /find/ page, with the option applied to the real page in the browser
and then photographed (r14/harvest/proto.js + shoot.mjs), so the trips, photos,
header and prices are exactly what ships. The trip counts beside every filter
choice were read off production the same day (r14/data/counts*.json). The
search numbers come from r14/harvest/search.py, which runs thirty everyday
searches through today's matching rule and through option B's.
"""

import json
import os

import mocks as m
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New', '30 Sep')
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'r14', 'data')
SH = json.load(open(os.path.join(DATA, 'shots.json')))
SR = json.load(open(os.path.join(DATA, 'search.json')))
LOOK = json.load(open(os.path.join(DATA, 'look-1440.json')))

LAPTOP = 900       # a 1440x900 laptop screen
PHONE = 844


def win(v, rings, fold, phone_fold=True):
    """The live page with option `v` applied, desktop and phone in one canvas.

    Desktop shows by default. The sheet's Phone button adds `.phone` to the
    wrapper, which swaps to the phone photograph; rings are hidden in phone
    mode by the sheet's own script, so hotspots only need the desktop boxes."""
    d, p = SH[f'{v}-desk'], SH[f'{v}-phone']
    hs = ''
    for n, key in enumerate(rings, 1):
        b = d['S'][key]
        h = min(b['h'], d['H'] - b['y'] - 8)
        hs += (f'<span class="r14-hs" id="r14-{v}-{n}" style="left:{b["x"]}px;top:{b["y"]}px;'
               f'width:{b["w"]}px;height:{h}px"></span>')
    lines = (f'<span class="r14-fold" style="top:{fold}px"><b>Bottom of a laptop screen</b></span>'
             if fold else '')
    plines = (f'<span class="r14-fold" style="top:{PHONE}px"><b>Bottom of the first phone screen</b></span>'
              if phone_fold else '')
    html = (f'<div class="r14-win r14-dk" style="height:{d["H"]}px"><img src="img/r14/{v}-desk.jpg" alt="" '
            f'style="height:{d["H"]}px">{hs}{lines}</div>'
            f'<div class="r14-win r14-ph" style="height:{p["H"]}px"><img src="img/r14/{v}-phone.jpg" alt="" '
            f'style="height:{p["H"]}px">{plines}</div>')
    r = ''.join(m.ring(n, f'#r14-{v}-{n}') for n, _ in enumerate(rings, 1))
    return m.mock(html + r, d['H'], aw=1440)


def px(v, dev='desk'):
    return SH[f'{v}-{dev}']['rail']['h']


# ------------------------------------------------------------- the numbers
A = SH['a-desk']
RAIL_TOP = A['rail']['y']
groups = {g['label']: g['box']['y'] for g in LOOK['groups']}
DEST_BELOW = groups['Destination'] - LAPTOP
WHEN_BELOW = groups['When'] - LAPTOP
ZERO_TODAY = sum(1 for r in SR if r['today'] == 0)
ZERO_B = sum(1 for r in SR if r['smart'] == 0)
ONE_TODAY = sum(1 for r in SR if r['today'] == 1 and r['smart'] > 1)


def screens(h):
    return f'{h / PHONE:.1f}'.replace('.0', '')


# ------------------------------------------------------------- decision 82
ALL.append(dec(
    82, 'The filters on Find a trip: bubbles, or something clearer',
    [('Find a trip page', ''), ('Crow + Jason', 'who'), ('&frac12; day', ''),
     ('40 bubbles in 5 groups today', 'big')],
    [quote(['I don&rsquo;t really like the bubbles, how can we make this look more clear and '
            'organized'], 'Crow, 30 September, with a screenshot of the filter column'),
     quote(['you have to scroll through everything to be able to get this side to go down so '
            'that you can see the rest of the states destination wise &hellip; That is more of an '
            'annoying quirk than anything'], 'Jason, 30 September, video three')],
    [
        opt('As it ships',
            ['<b>Forty rounded bubbles</b> in five groups, each bubble as wide as its own word, so '
             'every row ends at a different place.',
             '<b>Where</b> is fourth of five. On a laptop it starts <b>below the bottom of the '
             'screen</b>, so most people never see it without scrolling.',
             '<b>When</b> is last, and says &ldquo;Winter&rdquo; again, which is also a trip '
             'style one group up.'],
            f'<p>No numbers beside anything, so you only find out a choice is empty after you '
            f'click it (&ldquo;Special event&rdquo; has <b>no trips</b>). &ldquo;A day or '
            f'less&rdquo;, &ldquo;Half day&rdquo; and &ldquo;1 day&rdquo; overlap. On a phone '
            f'the open filter is <b>{screens(px("a", "phone"))} screens</b> of bubbles before the '
            f'first trip.</p>',
            cls='now',
            mockup=win('a', ['g1', 'dest', 'when'], LAPTOP)),

        opt('A list with tick boxes',
            ['Every choice is a plain line: <b>a tick box, the name, and how many trips</b> it '
             'will show. Nothing with no trips is listed.',
             '<b>Where</b> comes first, shows the seven biggest, then &ldquo;Show all 16 '
             'places&rdquo;.',
             'Each group <b>opens and closes</b>. Activity level starts closed.'],
            f'<p>Reads like a shopping site, which most people already know how to use. The '
            f'groups follow the same order as the question bar on the rest of the site: where, '
            f'when, how long, how you travel. You can tick <b>more than one</b> in a group, '
            f'Utah and Arizona say. With everything open it is still a little taller than a '
            f'laptop screen, so it keeps its own scroll.</p>',
            cost='&frac12; day',
            risk='It is still a long column; it is tidier, not shorter. Ticking two states '
                 'means the page needs to understand &ldquo;this or that&rdquo;, which is '
                 'most of the half day.',
            mockup=win('b', ['utah', 'more', 'closed'], LAPTOP)),

        opt('One bar across the top',
            ['The side column goes. The five questions sit in <b>one navy bar</b> above the '
             'trips, the same bar people already see on Destinations and Trip Styles.',
             'Each one opens a short list <b>with the trip count</b> beside every choice.',
             'What you picked shows as a tag under the bar, with an &times; to take it off, and '
             '&ldquo;Clear all&rdquo;.'],
            f'<p>The whole filter is <b>one strip</b> instead of a column longer than the '
            f'screen, so there is nothing to scroll and nothing hidden below the screen. The '
            f'trips get the full width: <b>four across instead of three</b>. On a phone the bar '
            f'is always open and takes about a quarter of the first screen, so there is no '
            f'&ldquo;Filter trips&rdquo; button to find.</p>',
            cost='&frac12; day (the bar is already built for the other pages)',
            risk='You have to open a list to see what is in it. Someone who likes to scan '
                 'every choice at once loses that.',
            cls='rec',
            mockup=win('c', ['bar', 'menu', 'tags'], LAPTOP)),

        opt('A different control for each question',
            ['<b>Where</b> is a two-column list of places with counts.',
             '<b>How long</b> is one row of five boxes, a day up to 11 or more days. '
             '<b>When</b> is four season boxes.',
             '<b>How active</b> uses the same four-step mark the trip cards use, so you pick '
             'the picture you will see on the card.'],
            '<p>The shortest of the three column versions and the most '
            '&ldquo;designed&rdquo;. Every choice still shows its count, and the whole thing '
            'is about one laptop screen tall.</p>',
            cost='1 day',
            risk='Five different kinds of control in one column is more to learn than one. '
                 'The row of length boxes is tight on a phone.',
            mockup=win('d', ['ggroup', 'seg', 'lv'], LAPTOP)),
    ],
    verdict([
        '<b>C.</b> You asked for clear and organized, and one bar is the most organized thing '
        'on the page: five questions in a line, in the same place and the same order as on '
        'Destinations and Trip Styles, so the site asks them one way everywhere. It also ends '
        'Jason&rsquo;s complaint outright rather than working around it. There is no side '
        'column left to scroll, and the trips get the width back.',
        '<b>B</b> is the safe choice if you would rather see every option without clicking. '
        'It looks like the filters on most shopping sites and fixes the bubbles, but it stays '
        'a long column.',
        'Whichever you pick, the scrolling problem is being fixed on staging with the rest of '
        'Jason&rsquo;s notes: the column will scroll on its own, so you no longer have to reach '
        'the bottom of the trips to reach the bottom of the filters. The trip counts in these pictures are today&rsquo;s live '
        'numbers with Utah chosen. They will move a little when the category fixes from '
        'Jason&rsquo;s videos go live.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------- decision 83
def srow(r):
    t = r['today']
    b = r['smart']
    cls = ' class="r14-zero"' if t == 0 else ''
    first = r['first'] or '&ndash;'
    return (f'<tr{cls}><td>&ldquo;{r["q"]}&rdquo;</td><td>{t or "<b>nothing</b>"}</td>'
            f'<td>{b}</td><td>{first}</td></tr>')


TABLE = ('<div class="r14-tbl"><div class="r13-ct">Thirty everyday searches, today and with B'
         '</div><table class="tbl"><tr><th>Typed</th><th>Trips today</th><th>Trips with B</th>'
         '<th>The first trip B shows</th></tr>' + ''.join(srow(r) for r in SR) +
         '</table><p class="r13-note">Searches run against the live catalogue of 74 trips on '
         '30 September. &ldquo;october&rdquo; with B means the page switches on the Autumn '
         'filter it already has. &ldquo;family&rdquo; still finds only three loose matches, '
         'because no trip is labelled for families. That is the kind of search D&rsquo;s '
         '&ldquo;Try&rdquo; row is for.</p></div>')

ALL.append(dec(
    83, 'The search box on Find a trip',
    [('Find a trip page', ''), ('Crow', 'who'), ('&frac12; to 1 day', ''),
     (f'{ZERO_TODAY} of 30 everyday searches find nothing', 'big')],
    [quote(['For the search bar function on this page, how can we improve it to be more '
            'helpful'], 'Crow, 30 September')],
    [
        opt('As it ships',
            ['The box only finds trips whose name or places contain <b>exactly what you '
             'typed</b>, as one phrase.',
             '&ldquo;zion bryce&rdquo; finds <b>nothing</b>, because no trip is called '
             '&ldquo;zion bryce&rdquo; word for word. &ldquo;Zion &amp; Bryce&rdquo; is.'],
            f'<p>I ran thirty searches a customer would type. <b>{ZERO_TODAY} find nothing '
            f'at all</b>: &ldquo;zion bryce&rdquo;, &ldquo;yellowstone winter&rdquo;, '
            f'&ldquo;slc&rdquo;, &ldquo;mighty five&rdquo;, &ldquo;october&rdquo;, a typo of '
            f'Yosemite, and three more. Another {ONE_TODAY} find a single trip when there are '
            f'several, &ldquo;hiking&rdquo; and &ldquo;river cruise&rdquo; among them.</p>',
            cls='now',
            mockup=win('sa', ['input', 'empty'], None, False)),

        opt('It understands more',
            ['<b>Each word counts on its own</b>, so &ldquo;zion bryce&rdquo; finds every trip '
             'that goes to both.',
             'Small <b>spelling slips</b> are forgiven, and everyday words work: slc, vegas, '
             'hiking, mighty five, a month.',
             'It also reads each tour&rsquo;s <b>own description and days</b>, but ranks a trip '
             'named for what you typed first.'],
            f'<p>Nothing on the page looks different. Of the same thirty searches, '
            f'<b>{ZERO_B} find nothing</b>, and the {ONE_TODAY} thin ones find the rest. The '
            f'table below shows every search and the first trip it puts on top.</p>',
            cost='&frac12; day',
            risk='Reading the descriptions finds more, and a few of the extra trips only pass '
                 'near the place. The ranking keeps those at the bottom.',
            mockup=win('sb', ['input', 'card1'], None, False)),

        opt('B, plus suggestions as you type',
            ['Everything in B.',
             'As you type, a list drops down: <b>places, trips and kinds of trip</b>, each with '
             'how many trips it has.',
             'Pick one and you go <b>straight there</b>, or press Enter to see all of them.'],
            '<p>This is the version that helps people who do not know what SWAT calls things. '
            'Typing &ldquo;zion&rdquo; shows the park, four Zion trips by name, and '
            '&ldquo;Day tours in Zion&rdquo;, before they have finished typing.</p>',
            cost='1 day',
            risk='A list that covers the page has to behave on a phone keyboard and for '
                 'people who use the keyboard only. That is most of the day.',
            cls='rec',
            mockup=win('sc', ['input', 'ta', 'taf'], None, False)),

        opt('B, plus results as you type and ideas to try',
            ['Everything in B. The <b>Search button goes</b>: the trips below change as you '
             'type.',
             'A row of <b>ready-made searches</b> sits under the box: Zion and Bryce, '
             'Yellowstone in winter, a day from Salt Lake.',
             'When it fixed a spelling slip it <b>says so</b> in a line above the trips.'],
            '<p>Good for someone who has no idea where to start. The &ldquo;Try&rdquo; row is '
            'five links SWAT can change whenever they like, so it can follow the season or a '
            'deal.</p>',
            cost='1 day',
            risk='The trips jump around under your fingers as you type, which some people '
                 'find unsettling. The Try row needs someone to keep it fresh.',
            mockup=win('sd', ['tri', 'und', 'card1'], None, False)),
    ],
    verdict([
        f'<b>C.</b> The part that matters most is B, and C includes it: {ZERO_TODAY} of the '
        f'thirty searches find nothing today and {ZERO_B} do with B. The suggestions are what '
        f'makes the box feel helpful rather than just correct: people see what SWAT has while '
        f'they type, spelled the way SWAT spells it, with how many trips each one has.',
        'If you want to start small, <b>B on its own</b> is half a day and changes nothing '
        'you can see. The ready-made &ldquo;Try&rdquo; row from D can be added to either '
        'later.',
    ]) + TABLE,
    since=NEW, cols=2))
