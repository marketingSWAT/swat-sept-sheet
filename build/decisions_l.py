"""Round twelve, decisions 75-79: Jason's Clarity > Connection > Conversion.

Jason Murray's email in the "Website Final round review" thread, 29 September
2026, 2:20 PM. It is his general review method, not notes on this site yet.
His examples ("private, custom tours to Morocco", "adventurous women 50+") are
about other businesses, and he said in the same thread that his specific
feedback was still to come. So this round runs his fifteen questions against
the live site first (the scorecard), and draws the five places where the
answer is a layout.

Numbered from 75: 73 is Matt's dates-by-season (another session), 74 is the
About page (another session). The About page is Jason's origin-story question,
so it is pointed at, not drawn twice.
"""

import mocks as m
import mocks_l as l
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New', '29 Sep')
AW = l.AW

WHO = 'Jason Murray, &ldquo;Website Final round review&rdquo;, 29 September'


def mk(html, h, *rings, aw=AW):
    r = ''.join(m.ring(n, s) for n, s in rings)
    # One-screen drawings are a 900px window with overflow hidden. Rings go
    # INSIDE the window so a ringed element below the fold cannot stretch the
    # measured canvas (the round-nine trap).
    if 'w11-win' in html[:60]:
        return m.mock(html[:-len('</div>')] + r + '</div>', h, aw=aw)
    return m.mock(html + r, h, aw=aw)


# ------------------------------------------------------------ the scorecard
def row(q, state, cls, where):
    return f'<tr><td>{q}</td><td>{state}</td><td class="{cls}">{where[0]}</td><td>{where[1]}</td></tr>'


def head(t):
    return f'<tr class="h"><td colspan="4">{t}</td></tr>'


SCORE = (
    '<section id="r11s"><div class="sec"><div class="st">Round twelve &middot; the scorecard</div>'
    '<h2>Jason&rsquo;s fifteen questions, asked of the live site</h2>'
    '<p>Every question from his email, in his order, answered against production on '
    '29 September: the home page, the trip-style pages and all 74 tour pages. '
    '<b>Clear</b> means a stranger gets the answer without looking for it. The last '
    'column says where it is dealt with. Five of the answers are layouts, and those '
    'are decisions 75 to 79 below. The rest are words or facts only SWAT has.</p></div>'
    '<div class="d"><div class="d-body"><table class="tbl sc11">'
    '<tr><th>His question</th><th>What the live site does</th><th>Answer</th><th>Where</th></tr>'
    + head('Clarity')
    + row('What is your core offer?',
          'The home page opens &ldquo;Welcome To Southwest Adventure Tours&rdquo; and calls SWAT '
          '&ldquo;a Destination Management Company and Tour Operator&rdquo; serving &ldquo;the '
          'Great American Southwest&rdquo;. On the same screen the map says &ldquo;We&rsquo;re '
          'nationwide, not just the Southwest&rdquo;.', 'no', ('Not clear', '<a href="#d75">75</a>'))
    + row('Who is it for?',
          'Never said. The guests say it for us: &ldquo;We had 8 passengers on our bus mostly in '
          'our 70&rsquo;s and she took care of all of us!&rdquo;', 'no',
          ('Not said', '<a href="#d75">75</a>, and Jason&rsquo;s sentence'))
    + row('What are my options, and how are they different?',
          'Nine trip styles, each a photo, a name and a count. None says how it differs. Day '
          'tour lists three trips of 6 to 8 days. Special event has 0 trips.', 'half',
          ('Half', '<a href="#d76">76</a>'))
    + row('Why are you different?',
          'The best answer on the site is the guides: a former Utah state park ranger, a Moab '
          'native, &ldquo;Utah&rsquo;s Wildlife Ambassador&rdquo;. It sits on ten separate '
          'About pages. None of it is on the home page.', 'no',
          ('Buried', '<a href="#d75">75</a>, <a href="#d77">77</a>'))
    + row('Is the language understandable?',
          'Tour pages are SWAT&rsquo;s own plain words. Industry words lead the home page '
          '(&ldquo;Destination Management Company&rdquo;), and the menu says &ldquo;Trip '
          'Styles&rdquo; and &ldquo;Departing From&rdquo;.', 'half',
          ('Half', '<a href="#d75">75</a>, <a href="#r11w">words</a>'))
    + head('Connection')
    + row('Emotion, or information?',
          'Tour pages open on three real guest reviews beside the photo, which is the right '
          'balance. The home page and the style pages are nearly all information.', 'half',
          ('Half', '<a href="#d77">77</a>'))
    + row('Does it feel human? Your words, not Claude&rsquo;s',
          'Every word on the 74 tour pages is SWAT&rsquo;s. The headings and short intros on '
          'the home, style and hub pages are mine, and some of them read like it.', 'half',
          ('Half', '<a href="#r11w">Words that are mine</a>'))
    + row('Is the origin story clear? Don&rsquo;t look bigger than you are',
          'The About page is mostly a staff handbook, with no story of how SWAT started. The '
          'home page says &ldquo;nationwide&rdquo;.', 'no',
          ('No', '74 (the About page) and <a href="#d75">75</a>'))
    + row('What is the deeper need, and do we speak to it?',
          'Not spoken to anywhere. Guests name it in their own reviews: &ldquo;on our bucket '
          'list&rdquo;, &ldquo;a once-in-a-lifetime adventure&rdquo;, &ldquo;she took care of all '
          'of us&rdquo;.', 'no', ('No', '<a href="#d77">77</a>, then Jason'))
    + row('Does the website feel like the experience?',
          'Yes. SWAT&rsquo;s own group photos, 15 films from SWAT&rsquo;s own channel, and '
          'real guest reviews on 23 tours.', 'ok', ('Yes', 'Keep it'))
    + head('Conversion')
    + row('Is there an obvious next step, always visible?',
          'Every tour has a button on the first screen, and &ldquo;Search trips&rdquo; follows '
          'you down every page. But the button says one of three different things.', 'ok',
          ('Yes', '<a href="#d79">79</a>'))
    + row('Is booking friction low?',
          '23 tours book in a pop-up on the page. 21 take a date request. 29 say &ldquo;Ask a '
          'question&rdquo;, and their quote form is about 1,390px down the page.', 'half',
          ('Half', '<a href="#d79">79</a>'))
    + row('Does the pricing make sense?',
          '6 tours lead with a 2026 price and have no 2026 date left. 5 lead with a price lower '
          'than any date on the page. Three river cruises show $250 to $550 for 8 to 13 days.',
          'no', ('No', '<a href="#d78">78</a>'))
    + row('Does it answer objections before checkout?',
          '&ldquo;Is this trip right for you?&rdquo; is on every tour. But 23 tours answer '
          '&ldquo;Ask us&rdquo; for how hard the trip is. Mighty 5 from Las Vegas says '
          '&ldquo;Easy&rdquo;, while a guest review on the same page says &ldquo;a walking/hiking '
          'tour with jam packed long days&rdquo;.', 'half',
          ('Half', '<a href="#r11q">Waiting on SWAT</a>'))
    + row('Has someone you&rsquo;re not married to stress-tested it?',
          'No. It has been tested by us, by Lance and by the sales team. All of them already '
          'know the trips.', 'no', ('No', '<a href="#r11o">Build order</a>'))
    + '</table></div></div></section>')


# ------------------------------------------------------------------------ 75
ALL.append(dec(
    75, 'The first screen of the home page: what SWAT is, and who it is for',
    [('Home page', ''), ('Jason: Clarity', 'who'), ('&frac12; day, plus his sentence', ''),
     ('Offer said two ways on one screen', 'big')],
    [quote(['what is your core offer? who is it for?',
            'why are you different? (both copy &amp; visual identity showing you stand out '
            'from the crowd)',
            'is the business&rsquo;s origin story clear? &mdash; don&rsquo;t look bigger '
            'than you are.'], WHO)],
    [
        opt('As it ships',
            ['The headline is a <b>welcome</b>, not an offer.',
             'The paragraph under it opens with <b>&ldquo;Destination Management '
             'Company&rdquo;</b>, an industry term.',
             'It says <b>&ldquo;the Great American Southwest&rdquo;</b>, and the map '
             'band on the same screen says <b>&ldquo;We&rsquo;re nationwide, not just the '
             'Southwest&rdquo;</b>.'],
            '<p>Nothing on this screen says who the trips are for, or why SWAT rather than '
            'the next operator. SWAT&rsquo;s own plain description, &ldquo;Our specialty is '
            'small group experiences&rdquo;, is on the same page, <b>4,905px down</b>, five '
            'screens below this one.</p>',
            cls='now',
            mockup=mk(l.home_now(), 900, (1, '.w11-hero h1'), (2, '.w11-hero .lede'),
                      (3, '.w11-map h2'))),

        opt('SWAT&rsquo;s own words, moved up',
            ['The headline is <b>SWAT&rsquo;s own line</b> from lower on the page.',
             'The paragraph is <b>SWAT&rsquo;s own &ldquo;Our specialty is small group '
             'experiences&rdquo;</b>, moved up five screens.',
             'The map band says <b>&ldquo;From the Southwest, out to 19 states&rdquo;</b>, '
             'so the two lines agree.'],
            '<p>Every word is already SWAT&rsquo;s, which answers Jason&rsquo;s &ldquo;not '
            'Claude&rsquo;s&rdquo; point directly. It says what and where. It still does not '
            'say who it is for, or why SWAT.</p>',
            cost='1 hour',
            risk='Low. &ldquo;Adventure awaits&rdquo; is the one line in it that any operator could say.',
            mockup=mk(l.home_own_words(), 900, (1, '.w11-hero h1'), (2, '.w11-hero .lede'),
                      (3, '.w11-map h2'))),

        opt('The offer, then the proof',
            ['The headline <b>names the offer</b>: small-group tours of the national parks.',
             '<b>Three faces</b> of real SWAT guides, from their About pages.',
             '<b>Three proof points</b>, every fact from SWAT&rsquo;s own pages: the group '
             'size, who the guides are, and where trips leave from.',
             'The map band says <b>&ldquo;Utah-based. Trips in 19 states.&rdquo;</b>'],
            '<p>Answers what, why and where on the first screen, the way Jason&rsquo;s '
            'questions ask. It makes the guides the difference, because they are what the '
            'reviews keep praising. The headline is my wording of SWAT&rsquo;s facts, so treat '
            'it as a stand-in until Jason gives D&rsquo;s sentence.</p>',
            cost='&frac12; day',
            risk='&ldquo;Utah-based&rdquo; needs Jason to confirm it is how he wants SWAT '
                 'described. The trips run in 19 states, and the office is in Cedar City.',
            cls='rec',
            mockup=mk(l.home_offer(), 900, (1, '.w11-hero h1'), (2, '.w11-faces'),
                      (3, '.w11-proof'), (4, '.w11-map h2'))),

        opt('C, waiting for Jason&rsquo;s sentence',
            ['<b>C&rsquo;s layout</b>, with the headline left open for <b>Jason&rsquo;s own '
             'sentence</b> about what SWAT is and who it is for.',
             'One line under it on why SWAT, <b>also his</b>.'],
            '<p>This is how C should end up. I can build the layout now, but the two lines '
            'have to come from him. That is what he means by &ldquo;use the words that are '
            'yours&rdquo;.</p>',
            cost='&frac12; day, once he sends the two lines',
            risk='It waits on Jason. Until then, C&rsquo;s wording stands in.',
            mockup=mk(l.home_slot(), 900, (1, '.w11-slot'), (2, '.w11-faces'))),
    ],
    verdict([
        '<b>C now, and D&rsquo;s two lines from Jason when he has them.</b> C fixes '
        'the contradiction (Southwest or nationwide), gets rid of &ldquo;Destination '
        'Management Company&rdquo;, and puts the thing that makes SWAT different, its '
        'guides, on the first screen.',
        'The one question I cannot answer for him is <b>who it is for</b>. The guests '
        'answer it (&ldquo;mostly in our 70&rsquo;s&rdquo;, &ldquo;on our bucket list&rdquo;), '
        'but whether SWAT wants to <i>say</i> that on the home page is his call. Ask him.',
        'B is the safe fallback if you want to change the words and nothing else today.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 76
ALL.append(dec(
    76, 'Trip styles: what are my options, and how are they different?',
    [('Trip styles page, 9 style pages', ''), ('Jason: Clarity', 'who'), ('&frac12;&ndash;1 day', ''),
     ('9 doors, 0 differences', 'big')],
    [quote(['what are my options, and how are they different? [day vs. multi day; private '
            'vs. public, adventure vs. relaxing vs. urban -- categorize &amp; display your '
            'tours in an easy to comprehent fashion]'], WHO)],
    [
        opt('As it ships',
            ['Nine photo cards with <b>a name and a trip count</b>. Nothing says how one '
             'differs from the next.',
             '<b>&ldquo;Special event &middot; 0 trips&rdquo;</b> is a door into an empty room.',
             'The intro line, &ldquo;nine different ways of being in them&rdquo;, is mine.'],
            '<p>Behind the doors the sorting is loose: <b>Day tour</b> lists Lone Star Texas '
            '(8 days), the Balloon Fiesta (6) and the Black Hills (6). <b>Guided small '
            'group</b> lists a 13-day Rhine river cruise and three 1-day Arches trips. '
            'The Self-drive cards say &ldquo;Small group, 7&ndash;13&rdquo;.</p>',
            cls='now',
            mockup=mk(l.styles_now(), 1400, (1, '.w11-sc'), (2, '.w11-sc:last-child'),
                      (3, '.w11-shero .lede'))),

        opt('Say how each one differs',
            ['Each card gets <b>how long, what it is, and a price</b>, read off its own '
             'trips.',
             'The empty Special event door <b>is hidden</b> until it has a trip.',
             'The same nine pages, the same order.'],
            '<p>The cheapest fix. Someone deciding between Guided small group and Private '
            'can now see the difference without opening both.</p>',
            cost='&frac12; day',
            risk='Nine is still a lot of choices, and three of them (Winter, Rail &amp; cruise, '
                 'Special event) are not ways of travelling at all. They are seasons or kinds of transport.',
            mockup=mk(l.styles_lines(), 1400, (1, '.w11-sc2 .how'), (2, '.w11-sc2 .pr'))),

        opt('Five doors, on Jason&rsquo;s own splits',
            ['<b>Five doors</b> that follow his three splits: <b>a day or several days</b>, '
             '<b>guided or on your own</b>, <b>with others or just your group</b>.',
             'Each door says, in one sentence, <b>what you get</b>, and gives a price.',
             'Winter, Rail &amp; cruise and Large groups become <b>smaller links</b> under '
             'the doors.'],
            '<p>Most people can pick from five. It matches the way Jason asked the '
            'question, and it forces the sorting fix: a door called &ldquo;A day out&rdquo; '
            'cannot hold an 8-day Texas trip. The nine style pages stay online at their '
            'addresses, so nothing is lost from Google.</p>',
            cost='1 day, including re-sorting the misfiled trips',
            risk='The door names are mine and need SWAT&rsquo;s okay. The nine style pages '
                 'still exist, so the menu and the footer keep working.',
            cls='rec',
            mockup=mk(l.styles_doors(), 1400, (1, '.w11-doors'), (2, '.w11-door .how'),
                      (3, '.w11-also'))),

        opt('A side-by-side table',
            ['One <b>table</b>: each style as a row, with how long, what it is, a price and the '
             'number of trips.'],
            '<p>The most information in the least space. Good for someone who likes to '
            'compare.</p>',
            cost='&frac12; day',
            risk='It reads like a spec sheet. For SWAT&rsquo;s older, less hurried '
                 'visitors it is the least inviting of the four, and it is the opposite of '
                 'Jason&rsquo;s emotion point.',
            mockup=mk(l.styles_table(), 1400, (1, '.w11-stbl'))),
    ],
    verdict([
        '<b>C, five doors.</b> It answers Jason&rsquo;s &ldquo;how are they different&rdquo; '
        'in his own terms, and it fixes the sorting. Today a Day tour page can hold an '
        '8-day trip, and no layout makes that clear.',
        'If you want the smaller change first, <b>B</b> is half a day and is not wasted: '
        'its one-line descriptions become the door text in C.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 77
ALL.append(dec(
    77, 'Put the guides in front: the people who make SWAT different',
    [('Home page', ''), ('Jason: Connection', 'who'), ('&frac12; day, plus photos from SWAT', ''),
     ('Sonsari: named in 5 reviews, no page of her own', 'big')],
    [quote(['does this feel human? (tell YOUR unique story, use the words that are yours, and '
            'not Claude&rsquo;s or the industry&rsquo;s)',
            'what is the deeper, core emotional need of the customer, and am I speaking to it? '
            '(belonging? rest? the thrill of being alive again?)'], WHO)],
    [
        opt('As it ships',
            ['The home page has the <b>reviews band</b>, and guests name their guides in it.',
             'Then it goes to the parks. <b>No guide&rsquo;s face appears</b> anywhere on the '
             'home page.'],
            '<p>The guides are on the About page and ten pages behind it. The two that guests '
            'praise most by name, <b>Sonsari (named in 5 reviews) and Kendra (3)</b>, have no page '
            'on the site, and neither does Steve Griffin (1). Robin is named in 2 and Ann in 1.</p>',
            cls='now',
            mockup=mk(l.guides_now(), 700, (1, '.w11-rvs'), (2, '.w11-sec:last-child .w11-sub'))),

        opt('The guides, in their own words',
            ['A band: <b>&ldquo;The people who guide your trip&rdquo;</b>.',
             'Four guides with their <b>photo</b> and <b>one sentence each from their own '
             'bio</b>, word for word.',
             'Each card links to the guide&rsquo;s own page.'],
            '<p>Every word is the guide&rsquo;s own. A former park ranger and a man who grew '
            'up with Arches as his backyard say more about why SWAT is different than any '
            'line I could write.</p>',
            cost='&frac12; day',
            risk='It shows the four guides who have pages, not necessarily the four guests '
                 'will meet. Sonsari and Kendra are missing.',
            mockup=mk(l.guides_bios(), 1000, (1, '.w11-gs'), (2, '.w11-g .bio'))),

        opt('The guides, in their guests&rsquo; words',
            ['The same band, <b>led by what guests said</b> about each guide, word for word '
             'from reviews already on the site.',
             '<b>Sonsari and Kendra first</b>, the two guests name most, drawn with an '
             'empty photo frame until SWAT sends a photo and two lines.',
             'Robin and Ann carry <b>both</b> their own sentence and a guest&rsquo;s.',
             'The band sits <b>above</b> the reviews, so the reviews read as proof.'],
            '<p>This is Jason&rsquo;s &ldquo;deeper need&rdquo; answered by the customers '
            'rather than by me: &ldquo;she took care of all of us&rdquo;. It uses nobody&rsquo;s '
            'words but the guides&rsquo; and the guests&rsquo;.</p>',
            cost='&frac12; day, plus a photo and two lines each for Sonsari and Kendra',
            risk='Needs SWAT to send the two missing guides. Until then, B&rsquo;s four '
                 'stand in.',
            cls='rec',
            mockup=mk(l.guides_guests(), 1150, (1, '.w11-g.slot'), (2, '.w11-g .guest'),
                      (3, '.w11-rvs'))),
    ],
    verdict([
        '<b>C.</b> The guides are SWAT&rsquo;s strongest answer to &ldquo;why you&rdquo;, and '
        'the guests have already written the copy. Build B&rsquo;s four now, and C the '
        'day SWAT sends Sonsari&rsquo;s and Kendra&rsquo;s photos.',
        'The same cards can go on each tour page later (&ldquo;who might guide this '
        'trip&rdquo;). That needs SWAT to say which guides lead which trips, so it is on the '
        'waiting list, not here.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 78
ALL.append(dec(
    78, 'Prices that make sense: the price shown is one you can book',
    [('9 tour pages, 3 cruise cards', ''), ('Jason: Conversion', 'who'), ('2&ndash;3 hours', ''),
     ('6 tours lead with a price that has no dates', 'big')],
    [quote(['does the pricing make sense?',
            'does the website answer objections before checkout?'], WHO)],
    [
        opt('As it ships',
            ['Glacier leads with <b>$3,649, &ldquo;2026&rdquo;</b>. There are no 2026 dates '
             'left. Every date on the page is 2027, from <b>$3,899</b>.',
             'A 12-day river cruise card says <b>$250 per person</b> and <b>&ldquo;Small '
             'group, 7&ndash;13&rdquo;</b>, on a ship.'],
            '<p>Across the 74 tours: <b>6</b> lead with a 2026 price and have only 2027 '
            'dates (Black Hills, Glacier, Magnificent Alaska, Colorado, Yellowstone winter, '
            'Yosemite). <b>5</b> lead with a price lower than every date on the page. The '
            'three river cruises show <b>$250, $280 and $550</b>. I don&rsquo;t know what those '
            'numbers are, maybe a deposit or a discount. The single-room price is at the '
            'bottom of the page, about 9,000px down.</p>',
            cls='now',
            mockup=mk(l.prices_now(), 700, (1, '.w11-pbox .amt'), (2, '.w11-pbox .bs'),
                      (3, '.w11-ama .pr'), aw=1100)),

        opt('The price you can book',
            ['The top price is <b>the cheapest date you can actually book</b>, with its '
             'year.',
             '&ldquo;Double occupancy&rdquo; becomes <b>&ldquo;sharing a room&rdquo;</b>.',
             'The cruise cards say <b>&ldquo;Price on request&rdquo;</b> until SWAT says '
             'what $250 means.'],
            '<p>Worked out from the dates each page already lists, so it stays right as '
            'dates sell out or new ones load.</p>',
            cost='2 hours',
            risk='None to speak of. A tour whose cheapest date sells out shows a higher '
                 'price the next day, which is the truth.',
            mockup=mk(l.prices_real(), 700, (1, '.w11-pbox .amt'), (2, '.w11-pbox .bs'),
                      (3, '.w11-ama .pr'), aw=1100)),

        opt('B, plus the price for one',
            ['Everything in B.',
             'Under it: <b>&ldquo;Travelling alone, from $4,349&rdquo;</b> and the price for '
             'three sharing, from the tour&rsquo;s own table.',
             'A <b>&ldquo;What the price includes&rdquo;</b> link to that section.'],
            '<p>Answers the two questions an older traveller asks first, &ldquo;what if '
            'I&rsquo;m on my own?&rdquo; and &ldquo;what&rsquo;s included?&rdquo;, before they '
            'have to ask. Both answers are already on the page, about 9,000px down.</p>',
            cost='3 hours',
            risk='Only on the 35 tours that have a price table. The rest keep B.',
            cls='rec',
            mockup=mk(l.prices_alone(), 800, (1, '.w11-pbox .amt'), (2, '.w11-alone'),
                      (3, '.w11-ama .pr'), aw=1100)),
    ],
    verdict([
        '<b>C.</b> B is a correction: today the site advertises a price nobody can buy on '
        'six tours, and that is the kind of thing that loses trust at checkout. C goes a '
        'step further and answers &ldquo;what if I travel alone&rdquo; up front, which is a '
        'big question for SWAT&rsquo;s guests.',
        'Separately, <b>SWAT needs to tell us what the $250 / $280 / $550 on the river '
        'cruises is</b>. Until then, I&rsquo;d hide it.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------------ 79
ALL.append(dec(
    79, 'The next step on the 29 trips that are priced by quote',
    [('29 tour pages', ''), ('Jason: Conversion', 'who'), ('&frac12; day', ''),
     ('Quote form 1,392px down', 'big')],
    [quote(['is there an obvious next step when people want to book, and it it always visible?',
            'is the booking friction low? Or do I have to hunt and peck for something that '
            'takes me to booking/inquiry?'], WHO)],
    [
        opt('As it ships',
            ['The button says <b>&ldquo;Ask a question&rdquo;</b> on a trip that has a price.',
             'The facts under the photo say <b>&ldquo;Ask us&rdquo;</b>, <b>&ldquo;Several '
             'cities &mdash; ask us&rdquo;</b> and <b>&ldquo;Dates on request&rdquo;</b>.',
             'The <b>&ldquo;Request a quote&rdquo;</b> form is <b>1,392px</b> down the page.'],
            '<p>Zion Park 1-Day Tour, one of the 29 day tours, self-drives, large groups and '
            'cruises in this shape. SWAT&rsquo;s own price note further down the page already '
            'says where it leaves from: <i>&ldquo;From St. George, Zion or Bryce, $999.00 for up '
            'to 4 people all inclusive. Each additional person is $200/person.&rdquo;</i></p>',
            cls='now',
            mockup=mk(l.zion_now(), 700, (1, '.w11-rl .btn'), (2, '.w11-tour .facts'),
                      (3, '.w11-far'))),

        opt('Get a price, right there',
            ['The quote form <b>moves into the booking panel</b>: date, how many people, '
             'where from.',
             'The button says <b>&ldquo;Get my price&rdquo;</b>, what you actually get.',
             'A line under it: we reply within one business day, <b>nothing is charged</b>.'],
            '<p>The same form, sent to the same inbox, 1,392px higher up the page. Nobody has '
            'to scroll down to find how to buy.</p>',
            cost='&frac12; day for all 29',
            risk='The panel is taller, so on a laptop the facts list under it starts lower. '
                 'On a phone it sits under the photo, as the dates do on the bookable tours.',
            mockup=mk(l.zion_quote(False), 700, (1, '.w11-qf'), (2, '.w11-rl .btn'))),

        opt('B, plus the facts SWAT already wrote',
            ['Everything in B.',
             '<b>&ldquo;Several cities &mdash; ask us&rdquo;</b> becomes <b>&ldquo;Leaves St. '
             'George, Zion or Bryce&rdquo;</b>, from SWAT&rsquo;s own price note.',
             '<b>&ldquo;Each extra person $200 &middot; all inclusive&rdquo;</b> goes under '
             'the price.'],
            '<p>Removes two of the three &ldquo;ask us&rdquo; answers using SWAT&rsquo;s own '
            'words, already on the page. &ldquo;Ask us&rdquo; for how hard the trip is stays '
            'until SWAT writes it.</p>',
            cost='&frac12; day, plus about an hour per 10 tours to read the notes',
            risk='Only where SWAT&rsquo;s note actually says it. I would not guess a city for '
                 'any tour.',
            cls='rec',
            mockup=mk(l.zion_quote(True), 700, (1, '.w11-qf'), (2, '.w11-tour .facts .fix'),
                      (3, '.w11-rl .more'))),
    ],
    verdict([
        '<b>C.</b> On these 29 tours the site is asking the customer to &ldquo;hunt and '
        'peck&rdquo;, in Jason&rsquo;s words: the button asks for a question, not a booking, '
        'and three of the six facts say &ldquo;ask us&rdquo;. C makes the next step the thing '
        'they came for, a price, and fills in what SWAT has already written down.',
    ]),
    since=NEW, cols=2))


# ------------------------------------------------------------------ registers
WORDS = (
    '<section id="r11w"><div class="sec"><div class="st">Round twelve &middot; register</div>'
    '<h2>Words that are mine, not SWAT&rsquo;s</h2>'
    '<p>Jason: <i>&ldquo;use the words that are yours, and not Claude&rsquo;s or the '
    'industry&rsquo;s&rdquo;</i>. The tour pages are SWAT&rsquo;s words, re-extracted from the '
    'old site. These lines are mine, written for the hub pages, and they are what he will '
    'notice. Each one is either cut, replaced with a fact, or replaced with SWAT&rsquo;s own '
    'wording. Nothing here changes until you say so.</p></div>'
    '<div class="d"><div class="d-body"><table class="tbl">'
    '<tr><th>Where</th><th>The line today</th><th>Why it reads wrong</th><th>What I&rsquo;d do</th></tr>'
    '<tr><td>Backpacking</td><td>&ldquo;The strongest thing this operator does, and the hardest '
    'to buy anywhere else.&rdquo;</td><td>It talks about SWAT as &ldquo;this operator&rdquo;, like '
    'a reviewer would. Nobody describes their own company like that</td>'
    '<td>Replace with the facts: 4 to 6 days, up to 8 people, permits held</td></tr>'
    '<tr><td>Build Your Own</td><td>&ldquo;It is the part of the business a visitor almost never '
    'discovers, because it has never had a page.&rdquo;</td><td>It tells the customer about our '
    'website project</td><td>Cut</td></tr>'
    '<tr><td>About</td><td>&ldquo;Membership in each of these is verifiable independently of '
    'anything said on this site.&rdquo;</td><td>Defensive and stiff</td><td>Cut (and 74 covers '
    'the rest of the page)</td></tr>'
    '<tr><td>Home</td><td>&ldquo;We&rsquo;re nationwide, not just the Southwest&rdquo;</td>'
    '<td>Contradicts the company name and the headline above it. And it looks bigger than SWAT is</td>'
    '<td><a href="#d75">75</a></td></tr>'
    '<tr><td>Home</td><td>&ldquo;Real dates, real prices.&rdquo;</td><td>Says out loud what should '
    'go without saying, and on 6 tours it isn&rsquo;t true (<a href="#d78">78</a>)</td><td>Cut</td></tr>'
    '<tr><td>Trip styles</td><td>&ldquo;The same parks, nine different ways of being in '
    'them.&rdquo;</td><td>Clever, and it doesn&rsquo;t help anyone choose</td><td><a href="#d76">76</a></td></tr>'
    '<tr><td>Departing From</td><td>&ldquo;You are already somewhere. Start there&hellip;&rdquo;</td>'
    '<td>Clever again. Jason&rsquo;s &ldquo;so clever nobody understands&rdquo;</td>'
    '<td>&ldquo;Every trip that leaves from your city, day trips first.&rdquo;</td></tr>'
    '<tr><td>The Archive</td><td>&ldquo;The strongest photography in our library&rdquo;; '
    '&ldquo;at the size they deserve&rdquo;</td><td>Grading our own photos</td>'
    '<td>&ldquo;Photos from the places our trips go.&rdquo;</td></tr>'
    '<tr><td>Destinations</td><td>&ldquo;Switch between the two ways of looking rather than having '
    'to know.&rdquo;</td><td>Hard to follow</td><td>&ldquo;Look by park, or by state.&rdquo;</td></tr>'
    '</table></div></div></section>')

WAIT = (
    '<section id="r11q"><div class="sec"><div class="st">Round twelve &middot; register</div>'
    '<h2>Waiting on Jason and SWAT</h2>'
    '<p>What only SWAT can supply. Each one unblocks something above. It is better to send '
    'this as one list than to ask in pieces.</p></div>'
    '<div class="d"><div class="d-body"><table class="tbl">'
    '<tr><th>What</th><th>From</th><th>Unblocks</th></tr>'
    '<tr><td><b>Two sentences</b>: what SWAT is and who it is for, then why SWAT and not the '
    'next operator. In his words</td><td>Jason</td><td><a href="#d75">75</a> D</td></tr>'
    '<tr><td><b>Southwest or nationwide?</b> Is SWAT a Southwest company that also runs trips '
    'elsewhere, or a national one?</td><td>Jason</td><td><a href="#d75">75</a>, the map band, '
    'the About page</td></tr>'
    '<tr><td><b>How SWAT started</b>, told by Jason. A 10-minute recorded call would give '
    'real words to use, not mine</td><td>Jason</td><td>74 (the About page)</td></tr>'
    '<tr><td><b>Photos and two lines each for Sonsari, Kendra and Steve Griffin</b>, the guides '
    'guests name most</td><td>SWAT office</td><td><a href="#d77">77</a> C</td></tr>'
    '<tr><td><b>Which guides lead which trips</b>, even roughly</td><td>Ann / SWAT office</td>'
    '<td>Guide cards on tour pages, later</td></tr>'
    '<tr><td><b>How hard each trip is</b>, on the 23 tours that say &ldquo;Ask us&rdquo;. '
    'And a second look at Mighty 5 from Las Vegas, marked &ldquo;Easy&rdquo; while a guest '
    'calls it &ldquo;a walking/hiking tour with jam packed long days&rdquo;</td>'
    '<td>SWAT writes it; Matt owns the graphic</td><td>His &ldquo;answer objections&rdquo; '
    'point</td></tr>'
    '<tr><td><b>What the $250 / $280 / $550 on the three river cruises is</b></td>'
    '<td>SWAT office</td><td><a href="#d78">78</a></td></tr>'
    '<tr><td><b>The 2022 &ldquo;Corona Virus Policy&rdquo; page</b> is still listed first under '
    'Guides &amp; resources. Keep it, update it or retire it?</td><td>SWAT office</td>'
    '<td>Nothing. It just looks out of date</td></tr>'
    '</table></div></div></section>')

SAID = (
    '<section id="r11n"><div class="sec"><div class="st">Round twelve &middot; register</div>'
    '<h2>Said on the site, but not true</h2>'
    '<p>Places where the site tells a customer something that the rest of the site '
    'contradicts. Jason&rsquo;s clarity point at its most basic.</p></div>'
    '<div class="d"><div class="d-body"><table class="tbl">'
    '<tr><th>The claim</th><th>What is actually there</th><th>Fix</th></tr>'
    '<tr><td>&ldquo;Real dates, real prices&rdquo; (home)</td><td>6 tours lead with a 2026 price '
    'and have only 2027 dates</td><td><a href="#d78">78</a></td></tr>'
    '<tr><td>Day tour</td><td>Lists an 8-day and two 6-day trips</td><td><a href="#d76">76</a></td></tr>'
    '<tr><td>Self-drive cards say &ldquo;Small group, 7&ndash;13&rdquo;</td><td>You drive '
    'yourself. There is no group</td><td>Do without asking</td></tr>'
    '<tr><td>River cruises: &ldquo;Small group, 7&ndash;13&rdquo;, &ldquo;priced per '
    'party&rdquo;, &ldquo;the same guides&rdquo;</td><td>They are AmaWaterways ships</td>'
    '<td>Do without asking</td></tr>'
    '<tr><td>&ldquo;Special event&rdquo; is one of nine ways to travel</td><td>0 trips</td>'
    '<td><a href="#d76">76</a></td></tr>'
    '<tr><td>About: &ldquo;watch the following video&rdquo;, &ldquo;click on Our Team '
    'below&rdquo;</td><td>No video, no Our Team button</td><td>74</td></tr>'
    '</table></div></div></section>')

ORDER = (
    '<section id="r11o"><div class="sec"><div class="st">Round twelve &middot; register</div>'
    '<h2>Build order</h2>'
    '<p>Nothing here is built. This is the order I would do it in, once you pick.</p></div>'
    '<div class="d"><div class="d-body"><table class="tbl">'
    '<tr><th>#</th><th>What</th><th>Why first</th></tr>'
    '<tr><td>1</td><td><a href="#d78">78</a> prices, and the two &ldquo;not true&rdquo; fixes '
    'above</td><td>Corrections, not design. A wrong price is the fastest way to lose a '
    '$5,000 booking</td></tr>'
    '<tr><td>2</td><td><a href="#d79">79</a> the next step on quote trips</td><td>29 tours, one '
    'change, directly on the path to a sale</td></tr>'
    '<tr><td>3</td><td><a href="#d75">75</a> the first screen, and the words register</td>'
    '<td>The first thing Jason will look at, once his two sentences arrive</td></tr>'
    '<tr><td>4</td><td><a href="#d76">76</a> and <a href="#d77">77</a></td><td>Bigger, and 77 '
    'waits on photos</td></tr>'
    '<tr><td>5</td><td><b>The outsider test</b>: three or four people in SWAT&rsquo;s real age '
    'range, each asked to find and price one trip (&ldquo;five days in Utah in May, from Las '
    'Vegas&rdquo;) while the heatmap records it. We watch where they stop</td><td>His last '
    'question. Nobody who has tested the site so far is new to it</td></tr>'
    '</table></div></div></section>')

REGISTERS = WORDS + WAIT + SAID + ORDER
