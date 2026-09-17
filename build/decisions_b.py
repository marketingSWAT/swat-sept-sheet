"""Decisions 25-29 — the trade page, reviews, video, unfinished forms and the
strip above the ticker.
"""

import mocks as m
from sheetkit import opt, quote, verdict, dec

ALL = []


# =====================================================================
# 25 — the industry / trade audience
# =====================================================================

def _navpage(nav, hero_title, hero_sub, body, rings=''):
    items = ''.join(
        f'<span class="{"on" if t == nav[-1] else ""}">{t}</span>' for t in nav)
    head = (m.promostrip() +
            '<div class="m-hd"><div class="m-shell">'
            f'<img class="m-logo" src="{m.WORDMARK}" alt="Southwest Adventure Tours">'
            f'<div class="m-nav">{items}</div>'
            f'<div class="m-phone">{m.PHONE}</div>'
            '<div class="m-hd-cta">Find a Trip</div></div></div>')
    return ('<div style="background:#fff">' + head +
            '<div style="position:relative;height:210px;overflow:hidden">' +
            m.img('door_travel', 2400, 420) +
            '<div style="position:absolute;inset:0;background:linear-gradient'
            '(90deg,rgba(5,18,31,.86),rgba(5,18,31,.25))"></div>'
            '<div style="position:absolute;inset:0;display:flex;'
            'align-items:center"><div class="m-shell">'
            '<div style="font-size:11px;font-weight:800;letter-spacing:.14em;'
            f'color:#7fa8c8">TRADE</div>'
            f'<div style="font-size:34px;font-weight:800;color:#fff;'
            f'letter-spacing:-.02em;margin-top:6px">{hero_title}</div>'
            f'<p style="margin:8px 0 0;font-size:15.5px;color:#cfe0ee;'
            f'max-width:620px">{hero_sub}</p>'
            '</div></div></div>' + body + rings + '</div>')


def _doors():
    cells = []
    for key, title, line, cta in [
            ('door_travel', 'Groups &amp; associations',
             'Twenty or more, on your dates. Departures built around your '
             'calendar, not ours.', 'What we need to quote'),
            ('vegas', 'Receptive operators',
             'Land services across the West for inbound operators. Nett rates, '
             'allocations, one point of contact.', 'Request nett rates'),
            ('templesq', 'Travel agents',
             'Commission on every booking, agent rates on familiarisation '
             'trips, and a person who answers the phone.', 'Register an agency')]:
        cells.append(
            '<div style="border:1px solid var(--sand300);border-radius:3px;'
            'overflow:hidden;background:#fff">'
            f'<div style="aspect-ratio:16/10;overflow:hidden">'
            f'{m.img(key, 640, 400)}</div>'
            '<div style="padding:14px 16px 18px">'
            f'<div style="font-size:18px;font-weight:800;color:var(--ink900)">'
            f'{title}</div>'
            f'<p style="margin:7px 0 0;font-size:14px;line-height:1.5;'
            f'color:var(--ink500)">{line}</p>'
            f'<div style="margin-top:12px;font-size:13.5px;font-weight:700;'
            f'color:var(--rust600)">{cta} &rsaquo;</div></div></div>')
    return ('<div class="m-shell" style="padding:26px 0 30px">'
            '<div class="m-grid3" style="display:grid;grid-template-columns:repeat(3,1fr);'
            f'gap:20px">{"".join(cells)}</div>'
            '<div style="margin-top:22px;border:1px solid var(--sand300);'
            'border-radius:3px;background:var(--sand100);padding:18px 22px;'
            'display:flex;align-items:center;gap:20px">'
            '<div><div style="font-size:17px;font-weight:800;color:var(--ink900)">'
            'Working on a specific programme?</div>'
            '<p style="margin:5px 0 0;font-size:14px;color:var(--ink500)">'
            'Send the brief and Sean comes back with an itinerary and a nett '
            'price.</p></div>'
            '<div class="m-cta" style="margin:0 0 0 auto;padding:12px 26px">'
            'Talk to the group desk</div></div></div>')


NAV_NOW = ['Home', 'Destinations', 'Trip Styles', 'Departing From', 'Hot Deals',
           'Build Your Own', 'Journal', 'About']
NAV_TAB = ['Home', 'Destinations', 'Trip Styles', 'Departing From', 'Hot Deals',
           'Build Your Own', 'About', 'For Partners']

ALL.append(dec(
    25,
    'A way in for groups, agents and operators',
    [('Main navigation + a new page', ''), ('Sean, via [ops]', 'who'),
     ('1 day + Sean&rsquo;s copy', ''), ('Blocked on words', 'blocked')],
    [quote(['our large group director came up with the idea&hellip; he said we '
            'just need an easy way for industry professionals to find out how '
            'to work with us, for large groups or as receptives.',
            'adding a page to the top, where you have your home, destinations, '
            'trip styles, departing from &mdash; if we were to just add '
            'something like industry professionals up there.'],
           'SWAT operations'),
     quote(['not large group &mdash; Sean wanted it to just be like travel '
            'professionals or industry professionals. But that&rsquo;s really '
            'long. It is really long.',
            'partnerships? No, I think that would come across wrong. White '
            'label, white glove&hellip; we&rsquo;ll get back to you on that.'],
           'Matt and [ops], on the name')],
    [
        opt('A page nobody can find',
            ['<b>/travel-professionals/ already exists</b> &mdash; it came '
             'across in the migration and is live today.',
             'It is <b>not in the navigation</b>, so the only way to it is a '
             'search engine or the footer.',
             'Its copy is the old site&rsquo;s: commission and group rates, '
             'nothing about receptives, nothing about associations, no '
             'onboarding.'],
            '<p>Worth knowing before anything is built: the page is not missing, '
            'it is unreachable and out of date. That changes the job from '
            '&ldquo;make a page&rdquo; to &ldquo;give it a door and write '
            'it&rdquo;.</p>',
            cost='&mdash;', risk='Sean&rsquo;s whole ask goes unanswered',
            cls='now',
            mockup=m.mock(_navpage(
                NAV_NOW, 'Travel professionals',
                'Commission, group rates and custom itineraries for agents and '
                'advisors booking Southwest Adventure Tours.',
                '<div class="m-shell" style="padding:26px 0 40px;max-width:900px">'
                '<p style="font-size:16px;line-height:1.7;color:var(--ink700)">'
                'Southwest Adventure Tours works with travel agents and '
                'advisors across the United States. Commission is paid on '
                'every confirmed booking, and group rates are available for '
                'parties of ten or more.</p>'
                '<div style="margin-top:22px;border:1px solid var(--sand300);'
                'background:var(--sand100);border-radius:3px;padding:20px 24px">'
                '<div style="font-size:15px;font-weight:700;color:var(--ink900)">'
                'Booking on behalf of a client?</div>'
                '<p style="margin:6px 0 0;font-size:15px;color:var(--ink500)">'
                'Call the trade line and we will hold space while the '
                'paperwork catches up.</p>'
                '<div style="margin-top:12px;font-size:20px;font-weight:800;'
                f'color:var(--rust600)">{m.PHONE}</div></div></div>',
                rings=m.ring(1, '.m-nav')), 640)),
        opt('One tab, three doors',
            ['A ninth tab in the main nav &mdash; drawn here as <b>For '
             'Partners</b>, and the word is Sean&rsquo;s to choose.',
             'The page splits into <b>three audiences</b>, because they want '
             'different things: groups want a quote, receptives want nett '
             'rates, agents want to register.',
             'Each door has its own short page and its own form, so the enquiry '
             'arrives already sorted.',
             'One shared panel at the foot for anything that does not fit, '
             'pointing at the group desk.'],
            '<p>Three audiences were named in the room in one breath &mdash; '
            'large groups, receptives, travel agents &mdash; and they do not '
            'share a next step. Sorting them at the door is what makes the '
            'enquiries useful rather than a single inbox of &ldquo;interested '
            'in working together&rdquo;.</p>'
            '<p>It also gives Sean three short briefs to write instead of one '
            'long page, which is the difference between copy arriving and copy '
            'being promised.</p>',
            cost='1 day for the shell, then Sean&rsquo;s copy',
            risk='Three empty doors look worse than one full page',
            cls='rec',
            mockup=m.mock(_navpage(
                NAV_TAB, 'Work with us',
                'Group departures, nett rates for receptive operators, and '
                'commission for agents. One desk, one contact, the whole West.',
                _doors(), rings=m.ring(1, '.m-nav span:last-child') +
                m.ring(2, '.m-shell > div:first-child')), 640)),
        opt('One long page, no new tab',
            ['The existing page is rewritten to cover all three audiences as '
             'sections, one after another.',
             'Reached from the footer and from About &mdash; <b>no ninth nav '
             'tab</b>.',
             'One form at the bottom, with a &ldquo;what are you?&rdquo; '
             'dropdown.'],
            '<p>The honest cheap version. It puts the words on the internet, '
            'which is most of the SEO value, and it costs half a day.</p>'
            '<p>What it does not do is the thing Sean actually asked for: an '
            '<i>easy way to find out how to work with us</i>. A page a '
            'receptive operator has to already know about is not a door. And '
            'the nav is the only thing on the site that is on every page.</p>',
            cost='Half a day + copy',
            risk='Invisible to exactly the people it is for',
            mockup=m.mock(_navpage(
                NAV_NOW, 'Work with us',
                'Group departures, nett rates and commission &mdash; all three, '
                'on one page.',
                '<div class="m-shell" style="padding:24px 0 34px;max-width:900px">'
                + ''.join(
                    '<div style="padding:16px 0;border-top:1px solid var(--sand200)">'
                    f'<div style="font-size:20px;font-weight:800;'
                    f'color:var(--ink900)">{t}</div>'
                    f'<p style="margin:6px 0 0;font-size:15px;line-height:1.6;'
                    f'color:var(--ink500)">{b}</p></div>'
                    for t, b in [
                        ('Groups and associations',
                         'Twenty or more, on your dates. We build the departure '
                         'around your calendar and quote it as one programme.'),
                        ('Receptive operators',
                         'Land services across the West. Nett rates, '
                         'allocations and one point of contact who knows your '
                         'account.'),
                        ('Travel agents',
                         'Commission on every confirmed booking, agent rates on '
                         'familiarisation trips, and a person who answers the '
                         'phone.')]) +
                '<div style="margin-top:20px;border:1px solid var(--sand300);'
                'border-radius:3px;padding:18px 20px;background:var(--sand100)">'
                '<div style="font-size:15px;font-weight:700;color:var(--ink900)">'
                'Tell us what you need</div>'
                '<div class="m-grid2" style="margin-top:10px;display:grid;'
                'grid-template-columns:1fr 1fr;gap:10px">'
                + ''.join(
                    '<div style="background:#fff;border:1px solid var(--sand300);'
                    f'border-radius:3px;padding:10px 12px;font-size:13.5px;'
                    f'color:var(--ink300)">{f}</div>'
                    for f in ['I am a&hellip; &#9662;', 'Company',
                              'Name', 'Email']) +
                '</div></div></div>'), 640)),
    ],
    verdict([
        'Take <b>B</b>, and treat the name as Sean&rsquo;s decision rather than '
        'a blocker. I have drawn <b>For Partners</b> because it fits the header '
        'at two words; &ldquo;Industry Professionals&rdquo; is 24 characters '
        'and would take the nav to two lines at 1200px, which is what the room '
        'was reacting to. <b>Trade</b>, <b>Groups &amp; Trade</b> and '
        '<b>Work With Us</b> all fit as well. Changing the word later costs '
        'nothing; changing the shape does.',
        'The reason for three doors rather than three sections is that the '
        'enquiries are different. A receptive asking for nett rates and a '
        'couple organising a reunion should not arrive in the same inbox with '
        'the same four fields.',
        '<b>This one is genuinely blocked.</b> I can build the shell this week, '
        'but three empty doors are worse than the page that exists now. It '
        'should not go live until Sean&rsquo;s copy lands.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 26 — reviews on the tour page
# =====================================================================

def _tourbody(rail_kw=None, band='', rings=''):
    rail_kw = rail_kw or {}
    body = (band +
            '<h2 style="font-size:24px;font-weight:800;color:var(--ink900);'
            'margin-top:4px">Overview</h2>'
            '<p style="margin:10px 0 0;font-size:16px;line-height:1.6;'
            'color:var(--ink700)">By joining one of our most popular tours, '
            'Southwest Adventure Tours will guide you through Utah&rsquo;s five '
            'national parks in five days, staying in Springdale, Bryce and '
            'Moab, with a guide who has driven these roads for a decade.</p>'
            '<p style="margin:12px 0 0;font-size:16px;line-height:1.6;'
            'color:var(--ink700)">Small groups of seven to thirteen, hotels '
            'rather than tents, and a vehicle that stops where the light '
            'is.</p>')
    return ('<div style="background:#fff">' + m.subnav() + m.factstrip() +
            m.twocol(body, m.rail(**rail_kw)) + rings + '</div>')


def _revband(compact=False):
    cards = ''.join(
        f'<div style="border:1px solid var(--sand300);border-radius:3px;'
        f'background:#fff;padding:15px 17px 17px">'
        f'<div style="color:#d39a2e;font-size:14px;letter-spacing:2px">'
        f'{"&#9733;" * s}</div>'
        f'<p style="margin:7px 0 0;font-size:14.5px;line-height:1.55;'
        f'color:var(--ink700)">{q}</p>'
        f'<div style="margin-top:9px;font-size:12.5px;color:var(--ink300)">'
        f'{who}</div></div>' for s, q, who in m.REVIEWS)
    return ('<div style="margin-top:2px;padding:20px 0 4px">'
            '<div style="display:flex;align-items:baseline;gap:12px">'
            '<div style="font-size:22px;font-weight:800;color:var(--ink900)">'
            'What guests said about this trip</div>'
            '<span style="color:#d39a2e;font-size:14px;letter-spacing:2px">'
            '&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            '<span style="font-size:13.5px;color:var(--ink300)">4.9 from 38 '
            'reviews</span>'
            '<span style="margin-left:auto;font-size:13.5px;font-weight:700;'
            f'color:var(--rust600)">Read all 38 &rsaquo;</span></div>'
            '<div class="m-grid3" style="display:grid;grid-template-columns:repeat(3,1fr);'
            f'gap:16px;margin-top:14px">{cards}</div></div>')


ALL.append(dec(
    26,
    'Where the reviews for a trip go',
    [('Every tour page', ''), ('[ops], seconded by Lance', 'who'),
     ('2&ndash;3 days', ''), ('Blocked on Matt&rsquo;s picks', 'blocked')],
    [quote(['when you are looking at a place, is there a section for reviews '
            'here on the tour page itself that are connected to it? I would '
            'really want that.',
            'on the right-hand side of the screen, under the check dates '
            '&mdash; does that section actually get any bigger, or would it be '
            'reasonable to put like below that just a rotation? And even see '
            'the star rating on it too.'], 'SWAT operations'),
     quote(['I just want it to be the real ones, and I want it to be current '
            '&mdash; rather than however old these are. Like, Glenn hasn&rsquo;t '
            'guided for us for like six years.'], 'SWAT operations')],
    [
        opt('No reviews on the trip',
            ['The tour page carries <b>no review of this tour</b> anywhere in '
             '11,468px.',
             'The home page has a reviews band, but it draws on SWAT&rsquo;s '
             'archived testimonials &mdash; which is where Glenn comes from.',
             'The booking rail runs price, dates, three specs, the CTA and the '
             'itinerary email.'],
            '<p>The archive is the actual problem, not the absence. The '
            'testimonials that came across in the migration are undated and '
            'some name guides who left years ago &mdash; so the fix is new '
            'content first and a place to put it second.</p>',
            cost='&mdash;', risk='The strongest sales material is not on the page',
            cls='now',
            mockup=m.mock(_tourbody(rings=m.ring(1, '.m-r-spec')), 1080)),
        opt('Three, under Check dates',
            ['Three reviews <b>inside the booking rail</b>, directly under the '
             'CTA, rotating.',
             'Star rating on each, name and month under it.',
             'A link out to all of them.'],
            '<p>Literally what was asked for in the room. It also has a '
            'measured problem.</p>'
            '<p>The rail is <b>709px tall today</b> and it is sticky: it '
            'follows you down the page. Three review cards add about 330px. On '
            'a 13&Prime; laptop the usable height under the sticky header is '
            'about 750px, so the rail stops sticking and the <b>Check '
            'availability</b> button scrolls away with the page &mdash; which '
            'costs more bookings than the reviews win.</p>',
            cost='2 days',
            risk='Breaks the sticky rail on a laptop; CTA scrolls off',
            mockup=m.mock(_tourbody(
                rail_kw={'reviews': m.REVIEWS},
                rings=m.ring(1, '.m-r-rev')), 1080)),
        opt('Rating in the rail, reviews in a band',
            ['The rail gains <b>one line</b>: five stars, the score, and the '
             'count &mdash; which is the part that sells, and it costs 24px.',
             'That line links down to a <b>full-width band above the '
             'Overview</b> holding three reviews and the overall rating.',
             'The band is the first thing under the facts, so it is read '
             'before the itinerary rather than after the price.',
             'Rail stays 733px and keeps sticking, so the CTA never leaves the '
             'screen.'],
            '<p>The same three reviews, in the two places they each do a '
            'different job: a score where the money decision is made, and the '
            'words where there is room to read them.</p>'
            '<p>A band also survives Matt sending six reviews for one tour and '
            'none for another &mdash; it simply does not render. Three empty '
            'slots inside the rail would leave a hole in the most important '
            'column on the page.</p>',
            cost='2&ndash;3 days', risk='Two places to keep in step',
            cls='rec',
            mockup=m.mock(_tourbody(
                rail_kw={'reviews': None, 'rating': True},
                band=_revband(),
                rings=m.ring(1, '.m-2l > div:first-child')), 1080)),
    ],
    verdict([
        'Take <b>C</b>. <b>B</b> is what was described, and I would still not '
        'build it: the rail is already 709px and sticky, and three review cards '
        'push the Check availability button off a laptop screen. That is a '
        'measurable cost against an unmeasured benefit.',
        '<b>On connecting it to Google.</b> Worth being straight about this, '
        'because it came up twice. Google&rsquo;s own API returns <b>the five '
        'most recent reviews</b> for a business, full stop &mdash; you cannot '
        'pull three hundred, you cannot filter them by tour, and you cannot '
        'choose which five. Every &ldquo;all our Google reviews on the '
        'site&rdquo; widget is a paid third party syncing them nightly, and '
        'none of them can tell which tour a review is about either.',
        'So the offer [ops] made in the room is the right mechanism: '
        '<i>&ldquo;I could pick them out and just send them to you.&rdquo;</i> '
        'Reviews with a tour name against each one, from anywhere &mdash; '
        'Google, email, the tour documents. I need the text, the first name, '
        'the month and the tour. Everything else follows.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 27 — video
# =====================================================================

def _photosection(video=False):
    tiles = []
    keys = ['zion2', 'hoodoo', 'mesa', 'capitol', 'moab', 'northrim']
    for i, k in enumerate(keys):
        if video and i == 0:
            tiles.append(
                '<div style="position:relative;aspect-ratio:16/10;'
                'border-radius:3px;overflow:hidden;background:#000">'
                + m.img('zion3', 640, 400, style='opacity:.62') +
                '<div style="position:absolute;inset:0;display:grid;'
                'place-items:center"><div style="width:52px;height:52px;'
                'border-radius:50%;background:rgba(255,255,255,.92);'
                'display:grid;place-items:center;color:var(--ink900);'
                'font-size:17px;padding-left:4px">&#9654;</div></div>'
                '<div style="position:absolute;left:10px;bottom:10px;'
                'background:rgba(5,18,31,.82);color:#fff;font-size:11px;'
                'font-weight:800;letter-spacing:.06em;padding:4px 9px;'
                'border-radius:3px">MONICA ON THIS TRIP &middot; 3:04</div>'
                '</div>')
        else:
            tiles.append(
                '<div style="aspect-ratio:16/10;border-radius:3px;'
                f'overflow:hidden;background:var(--sand200)">{m.img(k, 640, 400)}'
                '</div>')
    return ('<div class="m-shell" style="padding:26px 0 30px">'
            '<div style="font-size:24px;font-weight:800;color:var(--ink900)">'
            'More photos and videos</div>'
            '<div class="m-grid3" style="display:grid;grid-template-columns:repeat(3,1fr);'
            f'gap:16px;margin-top:14px">{"".join(tiles)}</div></div>')


ALL.append(dec(
    27,
    'Where the films go',
    [('Tour pages, About, the Archive', ''), ('Matt', 'who'),
     ('2 days', ''), ('Blocked on the cuts', 'blocked')],
    [quote(['so like, have it be a fourth option up here in the hero area '
            '&mdash; a tour highlights video. And then down in the tour '
            'details we have Monica&rsquo;s video. Yeah, or in more photos and '
            'videos.'], 'Matt'),
     quote(['we have embedded our YouTube videos&hellip; some of our highlights '
            'that could push them to our YouTube channel as well.',
            'I can even give you cut-up segments of Monica talking about each '
            'tour.'], 'Matt')],
    [
        opt('No film anywhere on a trip',
            ['The hero gallery is one 672&times;380 photograph with <b>four '
             'thumbnails</b> inside its bottom edge.',
             'More photos and videos is six photographs and no video.',
             'The About page has a film slot built and waiting &mdash; it '
             'renders nothing until a cut arrives.'],
            '<p>The slot on About shipped on Tuesday and is dark. Everything '
            'here is a container problem, not a code problem: the moment there '
            'is a file, there is somewhere to put it.</p>',
            cost='&mdash;', risk='YouTube gets no traffic from the site',
            cls='now',
            mockup=m.mock(m.tourhero() + m.factstrip() + _photosection(), 860)),
        opt('A fifth tile in the hero',
            ['The tour highlights film becomes <b>a tile in the hero '
             'gallery</b>, with a play badge and a label.',
             'Clicking it plays in place, at the top of the page, where the '
             'photographs already are.',
             'A trip with no film shows four thumbnails, exactly as now.'],
            '<p>Matt&rsquo;s first half, built. The hero is the one place on a '
            'tour page where a visitor is already looking at pictures, so a '
            'film there is found rather than scrolled past.</p>'
            '<p>On its own it leaves Monica out &mdash; and her segments are '
            'the ones that are actually about the trip rather than about the '
            'scenery.</p>',
            cost='1 day', risk='Only one film per tour fits up here',
            mockup=m.mock(m.tourhero(video_tile=True) + m.factstrip() +
                          _photosection(),
                          860, tone='')),
        opt('Highlights up top, Monica below',
            ['The highlights film is a <b>tile in the hero</b>, as beside.',
             'Monica&rsquo;s segment for this trip leads <b>More photos and '
             'videos</b>, with her name and the running time on it.',
             'Both play in place. Both carry a <b>Watch on YouTube</b> link '
             'under them, which is the traffic Matt is after.',
             'Anything over five minutes embeds from YouTube rather than '
             'shipping the file, so a long cut costs nothing in page weight.'],
            '<p>Matt&rsquo;s sentence in full: <i>&ldquo;a fourth option up '
            'here in the hero area is a tour highlights video, and then down in '
            'tour details we have Monica&rsquo;s video.&rdquo;</i></p>'
            '<p>The two films are doing different jobs &mdash; one sells the '
            'place, one sells SWAT &mdash; and separating them means a trip '
            'with only one of the two still looks complete.</p>',
            cost='2 days', risk='Needs a cut per tour to look finished',
            cls='rec',
            mockup=m.mock(m.tourhero(video_tile=True) + m.factstrip() +
                          _photosection(video=True), 860)),
    ],
    verdict([
        'Take <b>C</b>. It is Matt&rsquo;s own description, and the two '
        'placements do not compete &mdash; a highlights reel at the top is '
        'scenery, and Monica further down is the company. A tour with only one '
        'of the two still reads as finished.',
        'Two practical notes. <b>Keep the three-minute cut</b> for the About '
        'page rather than the nine &mdash; that was agreed in the room and it '
        'is the right call: a nine-minute film on a page people arrive at with '
        'a question is a film nobody finishes. And <b>anything over five '
        'minutes goes through YouTube</b>, not through our own storage, which '
        'also gets the channel the view.',
        '<b>What I need:</b> the cuts, and a list of which tour each segment '
        'belongs to. Until then all three of these render as photographs, '
        'which is exactly what they do today.',
    ]),
    since=('New', '16 Sep')))


# =====================================================================
# 28 — unfinished forms
# =====================================================================

def _builder_shell(overlay='', step1=None, rings=''):
    s1 = step1 or m.chips(
        ['Alaska', 'Arizona', 'California', 'Canada', 'Colorado', 'Hawaii',
         'Montana', 'Nevada', 'New Mexico', 'Oregon', 'South Dakota', 'Texas',
         'Utah', 'Washington', 'Wyoming'], on=('Utah', 'Arizona'))
    left = (m.step(1, 'Where would you like to go?', 'pick as many as you like',
                   s1) +
            m.step(2, 'How long do you have?', '',
                   m.chips(['Half day', '1 day', '2-3 days', '4-6 days',
                            '7-10 days', '11+ days'], on=('4-6 days',))) +
            m.step(3, 'How many of you?', '',
                   m.chips(['Just the two of us', '3&ndash;6', '7&ndash;13',
                            '14 or more'])))
    return ('<div style="position:relative;background:#fff">'
            '<div class="m-shell" style="padding-top:22px;padding-bottom:26px">'
            '<div style="font-size:29px;font-weight:800;color:var(--ink900);'
            'letter-spacing:-.02em">Build your own trip</div>'
            '<div class="m-2col" style="display:grid;'
            'grid-template-columns:1fr 320px;gap:36px;align-items:start;'
            'margin-top:14px">'
            f'<div>{left}</div>'
            f'{m.sofar([("Where", "Utah, Arizona"), ("How long", "4&ndash;6 days"), ("How many", "&mdash;"), ("When", "&mdash;")])}'
            '</div></div>' + overlay + rings + '</div>')


_PROMPT = (
    '<div style="position:absolute;inset:0;background:rgba(5,18,31,.55)"></div>'
    '<div class="m-leave" style="position:absolute;left:50%;top:76px;'
    'transform:translateX(-50%);width:480px;background:#fff;border-radius:4px;'
    'box-shadow:0 30px 70px rgba(5,18,31,.4);padding:24px 26px 26px">'
    '<div style="font-size:21px;font-weight:800;color:var(--ink900)">'
    'Leaving already? You are halfway there.</div>'
    '<p style="margin:9px 0 0;font-size:15px;line-height:1.55;'
    'color:var(--ink500)">Utah and Arizona, four to six days. Two more '
    'questions and a guide will come back with a real itinerary and a real '
    'price.</p>'
    '<div style="margin-top:16px;display:flex;gap:10px">'
    '<div class="m-cta" style="margin:0;flex:1;padding:12px 0">'
    'Finish &mdash; two questions left</div>'
    '<div style="flex:1;border:1px solid var(--sand300);border-radius:3px;'
    'text-align:center;font-weight:700;font-size:14px;color:var(--ink700);'
    'padding:12px 0">No thanks</div></div></div>')

_PROMPT_SAVE = (
    '<div style="position:absolute;inset:0;background:rgba(5,18,31,.55)"></div>'
    '<div class="m-leave" style="position:absolute;left:50%;top:60px;'
    'transform:translateX(-50%);width:490px;background:#fff;border-radius:4px;'
    'box-shadow:0 30px 70px rgba(5,18,31,.4);padding:24px 26px 26px">'
    '<div style="font-size:21px;font-weight:800;color:var(--ink900)">'
    'Leaving already? You are halfway there.</div>'
    '<p style="margin:9px 0 0;font-size:15px;line-height:1.55;'
    'color:var(--ink500)">Utah and Arizona, four to six days. Finish now, or '
    'we will send you the link and you can pick it up whenever.</p>'
    '<div class="m-cta" style="margin:16px 0 0;padding:12px 0">'
    'Finish &mdash; two questions left</div>'
    '<div style="margin-top:14px;padding-top:14px;'
    'border-top:1px solid var(--sand200)">'
    '<div style="font-size:12.5px;font-weight:700;color:var(--ink500)">'
    'Or send me my trip so far</div>'
    '<div style="margin-top:8px;display:flex;gap:8px">'
    '<div style="flex:1;border:1px solid var(--sand300);border-radius:3px;'
    'padding:11px 12px;font-size:14px;color:var(--ink300)">you@example.com</div>'
    '<div style="background:var(--navy800);color:#fff;border-radius:3px;'
    'font-weight:700;font-size:14px;padding:11px 18px">Send it</div></div>'
    '<p style="margin:8px 0 0;font-size:12px;color:var(--ink300)">One email '
    'with a link back. Nothing else, unless you ask.</p></div></div>')


ALL.append(dec(
    28,
    'Catching a trip builder somebody walks away from',
    [('Build Your Own', ''), ('Matt, and the room', 'who'),
     ('2&ndash;3 days', ''), ('Consent shape matters', 'big')],
    [quote(['another idea, and tell me how much this sucks &mdash; but if '
            'people actually start filling out the forms and they don&rsquo;t '
            'finish them and they leave the page, and we have a &lsquo;hey, you '
            'started this process, are you sure you want to leave without '
            'finishing it&rsquo; pop-up or something?',
            'ah yes, that&rsquo;s it. Now that&rsquo;s it. Yes.'],
           'Matt, and [ops]'),
     quote(['we could also have a thing where before they even start filling '
            'out their tour they put their email in, so if they don&rsquo;t '
            'finish it then we can have it automatically send them emails. '
            'I&rsquo;m not sure if that&rsquo;s a little spammy.'],
           'Crow, in the room')],
    [
        opt('Nothing happens',
            ['Close the tab at step three and <b>every answer is gone</b>. '
             'Nothing is stored, nothing is sent, nobody knows it happened.',
             'The builder collects nothing until the final Send, so a '
             'half-finished trip is not a lead &mdash; it is not anything.',
             'Six steps is a long way to get nothing from.'],
            '<p>Worth saying plainly: we cannot even count how often this '
            'happens today, because there is no measurement on the steps. The '
            'first version of any of these should log where people stop, '
            'whatever else it does.</p>',
            cost='&mdash;', risk='No idea how big the problem is',
            cls='now',
            mockup=m.mock(_builder_shell(rings=m.ring(1, '.m-sofar')), 760)),
        opt('Ask before they go',
            ['Moving to close the tab with two or more answers given triggers '
             '<b>one prompt</b>.',
             'It repeats what they have chosen back to them, and says how many '
             'questions are left.',
             'Once per visit. Never on a phone, where there is no such thing '
             'as leaving intent and it would fire at the wrong moment.',
             'Nothing is captured and nothing is sent.'],
            '<p>Matt&rsquo;s idea, exactly as described, and the room liked it '
            'immediately.</p>'
            '<p>The limit is what it can reach: only the tab that is still '
            'open. Someone who closes the laptop, or who is on a phone, is '
            'still gone &mdash; and phones are most of this traffic.</p>',
            cost='1 day', risk='Desktop only; catches nothing after the tab closes',
            mockup=m.mock(_builder_shell(_PROMPT,
                                         rings=m.ring(1, '.m-leave')), 760)),
        opt('Email first, then chase',
            ['Step one becomes <b>an email address</b>, before any of the '
             'questions.',
             'An unfinished trip triggers a follow-up email a day later.',
             'It is the only option that reaches somebody whose tab is already '
             'closed.'],
            '<p>This is the DoorDash model, and it does work.</p>'
            '<p>It also puts the one piece of friction people hate in front of '
            'the one thing they were enjoying. Crow&rsquo;s own instinct in the '
            'room was right &mdash; <i>&ldquo;I&rsquo;m not sure if that&rsquo;s '
            'a little spammy&rdquo;</i> &mdash; and an address given before any '
            'value has been offered is the weakest consent there is. It also '
            'lowers the number of people who start at all, which is the '
            'opposite of the goal.</p>',
            cost='2 days + an email sequence',
            risk='Friction at step one; consent nobody really gave',
            mockup=m.mock(_builder_shell(step1=(
                '<div style="margin-top:12px;border:1px solid var(--sand300);'
                'background:var(--sand100);border-radius:3px;padding:16px 18px">'
                '<div style="font-size:14px;font-weight:700;color:var(--ink900)">'
                'First, where should we send it?</div>'
                '<div style="margin-top:10px;display:flex;gap:8px">'
                '<div style="flex:1;background:#fff;border:1px solid '
                'var(--sand300);border-radius:3px;padding:11px 12px;'
                'font-size:14px;color:var(--ink300)">you@example.com</div>'
                '<div class="m-cta" style="margin:0;padding:11px 24px">'
                'Start</div></div></div>'),
                rings=m.ring(1, '.m-step:first-child')), 760)),
        opt('The prompt, with a way to save it',
            ['The same leave prompt as <b>B</b> &mdash; nothing asked for up '
             'front, the builder stays free.',
             'Inside the prompt, a second offer: <b>send me my trip so '
             'far</b>, one field.',
             'The address is given <b>at the moment it buys something</b> '
             '&mdash; a link back to a half-built trip &mdash; which is '
             'consent anybody would recognise.',
             'That email is a real lead with the answers attached, so a walked-'
             'away trip still reaches a planner.',
             'Works on a phone too: the same card appears on a back gesture or '
             'after a long pause, where a leave prompt cannot fire.'],
            '<p>It takes the half of <b>C</b> that works &mdash; an address, so '
            'somebody can be reached after the tab shuts &mdash; and moves it '
            'to the moment where asking is fair.</p>'
            '<p>And unlike either of the others it produces something useful '
            'when it succeeds: not a nudge, a lead.</p>',
            cost='2&ndash;3 days', risk='One more thing that can misfire mid-form',
            cls='rec',
            mockup=m.mock(_builder_shell(_PROMPT_SAVE,
                                         rings=m.ring(1, '.m-leave')), 760)),
    ],
    verdict([
        'Take <b>D</b>. It is Matt&rsquo;s prompt with the useful half of the '
        'email idea attached, and it asks for the address at the only moment '
        'when asking is a fair trade.',
        'One thing to build whichever letter comes back: <b>log where people '
        'stop</b>. Right now nobody knows whether this is a problem worth '
        'three days or a problem that happens twice a month, and a week of '
        'step-by-step numbers would tell us.',
        '<b>Not available:</b> testing these against each other. There is no '
        'experiment framework on the build and not enough traffic to run one '
        'yet, so this is a judgement call rather than a measurement &mdash; '
        'which is also why I would not spend more than three days on it.',
    ]),
    since=('New', '16 Sep'), cols=2))


# =====================================================================
# 29 — the strip above the ticker
# =====================================================================

def _homeTop(strip_kind='now', rings=''):
    strip = m.campaign(strip_kind)
    hdr = ('<div class="m-hd"><div class="m-shell">'
           f'<img class="m-logo" src="{m.WORDMARK}" alt="Southwest Adventure Tours">'
           f'<div class="m-nav">' +
           ''.join(f'<span class="{"on" if t == "Home" else ""}">{t}</span>'
                   for t in m.NAV) +
           f'</div><div class="m-phone">{m.PHONE}</div>'
           '<div class="m-hd-cta">Find a Trip</div></div></div>')
    return ('<div style="background:#fff">' + strip + hdr + m.ticker() +
            '<div style="position:relative;height:210px;overflow:hidden">' +
            m.img('hero', 2400, 420) +
            '<div style="position:absolute;inset:0;background:linear-gradient'
            '(90deg,rgba(5,18,31,.72),rgba(5,18,31,.12))"></div>'
            '<div style="position:absolute;inset:0;display:flex;'
            'align-items:center"><div class="m-shell">'
            '<div style="font-size:38px;font-weight:800;color:#fff;'
            'letter-spacing:-.025em;max-width:640px;line-height:1.1">'
            'The national parks of the American West, in small groups</div>'
            '</div></div></div>' + rings + '</div>')


ALL.append(dec(
    29,
    'The strip above the hot deals ticker',
    [('Every page, above the header', ''), ('[ops]', 'who'),
     ('1&ndash;2 days', ''), ('Hidden on phones today', 'big')],
    [quote(['I don&rsquo;t ever want to lose the hot deals ticker. I wanted to '
            'focus on the hot deals. But the bar above that &mdash; so the '
            'small groups of seven to thirteen departing Las Vegas, Phoenix and '
            'Salt Lake City &mdash; oh yeah, you could use that to indicate '
            '&lsquo;hey, Black Friday deals&rsquo; or something on those '
            'lines.'], 'SWAT operations'),
     quote(['Ashley puts these deals together quite a bit in advance, so '
            'we&rsquo;ll get you to do it.'], 'SWAT operations')],
    [
        opt('One fixed sentence',
            ['A 36px strip above the header carrying SWAT&rsquo;s positioning '
             'line and a link to the deals.',
             'It is hard-coded. Changing it for a campaign is a code change and '
             'a deploy, and changing it back is another.',
             '<b>It is hidden below 640px</b> &mdash; a phone never sees it at '
             'all.'],
            '<p>The last point is the one that matters and it is easy to miss '
            'in a desktop screen-share. The strip is <code>hidden sm:block</code> '
            'on the live build, so a Black Friday message put here today would '
            'be invisible to most of the traffic.</p>',
            cost='&mdash;', risk='Invisible on phones; needs a deploy to change',
            cls='now',
            mockup=m.mock(_homeTop('now', rings=m.ring(1, '.m-strip')), 620)),
        opt('The campaign takes the strip',
            ['For a scheduled window the strip becomes <b>the campaign</b>: '
             'icon, name, offer, code, link.',
             'Dated in advance and it switches itself on and off &mdash; '
             'Ashley&rsquo;s calendar goes in once, nobody touches it in '
             'November.',
             'Its own colour, so it does not read as the same furniture as the '
             'ticker underneath.',
             '<b>Shown on phones</b>, unlike the line it replaces.',
             'Outside a campaign window it reverts to the positioning line, '
             'exactly as now.'],
            '<p>A takeover earns attention because it is rare and because it is '
            'obviously not the usual sentence. The positioning line is not lost '
            '&mdash; it is what the strip says for the other eleven months.</p>',
            cost='1&ndash;2 days',
            risk='Two promotional bars stacked during a campaign',
            cls='rec',
            mockup=m.mock(_homeTop('take', rings=m.ring(1, '.m-strip')), 620)),
        opt('Campaign left, positioning right',
            ['The strip splits: campaign on the left, the small-groups line '
             'stays on the right.',
             'Nothing is ever given up &mdash; both messages are on every page '
             'all the time.',
             'Also shown on phones, where it stacks into two lines.'],
            '<p>The cautious version, and the argument for it is real: the '
            'positioning line does a job every day of the year and a takeover '
            'suspends it.</p>'
            '<p>The argument against is that a 36px strip carrying two '
            'unrelated sentences reads as neither. Splitting it makes the '
            'campaign a footnote to a sentence people have already stopped '
            'reading &mdash; and on a phone it becomes two lines of small type '
            'above the header.</p>',
            cost='1&ndash;2 days', risk='Two messages in 36px reads as none',
            mockup=m.mock(_homeTop('split', rings=m.ring(1, '.m-strip')), 620)),
    ],
    verdict([
        'Take <b>B</b>. A campaign either takes the strip or it is not a '
        'campaign, and the positioning line is not lost &mdash; it is what the '
        'strip says for the rest of the year.',
        '<b>Fix the phone case whichever way this goes.</b> The strip is hidden '
        'below 640px on the build today, which means the Black Friday message '
        'the room was picturing would not be seen by most of the people it is '
        'aimed at. That is a bug in this plan rather than a decision, and I '
        'will fix it regardless.',
        '<b>What makes it worth building:</b> Ashley planning deals in advance. '
        'If the dates and codes arrive as a list, campaigns go in once and '
        'switch themselves on. If they arrive the morning of, this is a '
        'scheduling feature nobody uses and a one-line edit would have done.',
    ]),
    since=('New', '16 Sep'), cols=2))
