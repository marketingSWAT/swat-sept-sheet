"""Mockup primitives for round twelve: Jason's three questions, decisions 75-79.

Jason Murray, "Website Final round review" thread, 29 September 2026, 2:20 PM:
"Clarity > Connection > Conversion. They go in order, but also you can't miss
one of them."

Drawn at **1440** wide, a laptop, because that is the screen a reviewer who
is not on a big monitor reads the site on. Every current-build panel was read
off the **deployed production build** `swat-website-storefront.vercel.app` at
1440x900 on 29 September 2026 (harvest in r11/harvest/, `page.mjs`,
`crawl.mjs`, `styles.mjs`).

  Home        hero 558px at y=159 (Double Arch), pill "74 guided tours · 10
              departure cities", H1 "Welcome To Southwest Adventure Tours"
              54px, the Destination Management Company paragraph 4 lines;
              search bar y=653; map band from y=823, its heading "We're
              nationwide, not just the Southwest" at y=872, on the fold.
              SWAT's own "Our specialty is small group experiences" paragraph
              is at y=4,905, five screens down.
  Trip styles 9 photo cards 435x272, 3 across, name + trip count only.
              "Special event · 0 trips". Day tour lists three 6-8 day trips.
  Tours       74 crawled. 23 carry Book buttons, 21 "Ask about a date", 29
              "Ask a question" with "Request a quote" at y~1,390. 6 headline
              a 2026 price with no 2026 date left; 5 headline a price lower
              than every date on the page. River cruises: $250, $280, $550
              "from / person".
  Guides      10 names on About; of the reviews on the site, Sonsari is
              named in 5, Kendra 3, Robin 2, Steve Griffin 1, Ann 1. Sonsari,
              Kendra and Steve have no page of their own.
"""

import mocks as m
import mocks_j as j

AW = 1440
SUPA = 'https://pyxnpjvtdlucaqqhhvin.supabase.co/storage/v1/object/public/media/derived/'


def ph(path, w=640):
    """A real photograph off the storefront's own storage."""
    return f'{SUPA}w{w}/photos/{path}'


HERO = ph('windows_section_arches_05063611-79a7-4808-8a5b-183dfdb4dd13.avif', 1600)
MAPBAND = 'img/r12-mapband.webp'  # copied off production; the storefront serves it behind the passcode

GUIDES = {
    'ann': ph('AnnEvans_e013343d-eb52-4bca-ba05-082654d77653.avif'),
    'phil': ph('phil_douglas_71842697-f115-494c-a6af-8d7aa2f90b33.avif'),
    'dennis': ph('Dennis_13892f9a-95b9-4878-b3d8-ddb1e7dcf2d4.avif'),
    'robin': ph('robin_luse_zion_f345414b-616f-4491-a5f1-ca4f725a2bf5.avif'),
    'kirk': ph('kirt_douglass_b6e98676-0e7b-402e-8381-4abd3ba27cd5.avif'),
}


def win(body, h=900):
    """One 1440x900 window: what a laptop shows before any scrolling."""
    return f'<div class="w9 w11 w11-win" style="height:{h}px">{body}</div>'


def page(body):
    return f'<div class="w9 w11">{body}</div>'


# ------------------------------------------------------------------ 75 home
def hero(pill, h1, lede, extra=''):
    return (f'<div class="w11-hero"><img src="{HERO}" alt="">'
            f'<div class="sh"><div class="w11-hero-in">'
            f'<span class="w11-pill">{pill}</span>'
            f'<h1>{h1}</h1><p class="lede">{lede}</p>{extra}</div></div></div>'
            '<div class="sh w11-find-wrap"><div class="w11-find">'
            '<label>Where<span>Anywhere in the Southwest</span></label>'
            '<label>Leaving from<span>Any departure city</span></label>'
            '<label>How long<span>Any length</span></label>'
            '<b class="go">Search 74 tours</b></div>'
            '<div class="w11-pop">Popular: <span>Day tours</span><span>Easy pace</span>'
            '<span>Backpacking</span><span>Private &amp; custom</span><span>Current deals</span></div></div>')


def mapband(title, sub):
    return (f'<div class="sh"><div class="w11-map"><img src="{MAPBAND}" alt="">'
            f'<div class="t"><h2>{title}</h2><p>{sub}</p></div></div></div>')


def home_now():
    return win(j.top('Home') + hero(
        '74 guided tours &middot; 10 departure cities',
        'Welcome To Southwest Adventure Tours',
        'As a Destination Management Company and Tour Operator, we provide tours '
        'for individuals and groups through the Great American Southwest. We focus '
        'on conducting sightseeing, photography, and adventure tours.')
        + mapband('We&rsquo;re nationwide, not just the Southwest',
                  '19 states, 69 routes, 120 places. One live map.'))


def home_own_words():
    return win(j.top('Home') + hero(
        'Small groups of 7&ndash;13',
        'With Southwest Adventure Tours, adventure awaits',
        'Our specialty is small group experiences &mdash; usually between 7 and 13 '
        'passengers. We offer multi-day tours and day tours from Las Vegas, Phoenix, '
        'Salt Lake City, and other local areas adjacent to the national parks.')
        + mapband('From the Southwest, out to 19 states',
                  '69 routes, 120 places. One live map.'))


def faces(keys):
    return ('<span class="w11-faces">' + ''.join(
        f'<img src="{GUIDES[k]}" alt="">' for k in keys) + '</span>')


def home_offer():
    proof = ('<ul class="w11-proof">'
             '<li><b>7 to 13 guests</b> on a small-group trip</li>'
             '<li><b>Guides who live here</b>: a former Utah state park ranger, '
             'a Moab native, &ldquo;Utah&rsquo;s Wildlife Ambassador&rdquo;</li>'
             '<li><b>Day trips and multi-day tours</b> from Las Vegas, Phoenix and '
             'Salt Lake City</li></ul>')
    return win(j.top('Home') + hero(
        '74 guided tours &middot; 10 departure cities',
        'Small-group tours of the national parks',
        '', faces(['ann', 'dennis', 'phil']) + proof)
        + mapband('Utah-based. Trips in 19 states.',
                  '69 routes, 120 places. One live map.'))


def home_slot():
    return win(j.top('Home') + hero(
        '74 guided tours &middot; 10 departure cities',
        '<span class="w11-slot">Jason&rsquo;s one sentence: what SWAT is, and who it is for</span>',
        '<span class="w11-slot sm">One line on why SWAT and not the next operator, in his words</span>',
        faces(['ann', 'dennis', 'phil']))
        + mapband('Utah-based. Trips in 19 states.',
                  '69 routes, 120 places. One live map.'))


# ---------------------------------------------------------- 76 trip styles
STYLE_PH = {
    'backpacking': ph('Zion_Checkerboard_Mesa_Group_Photo_ded30d2e-ad40-4010-ae62-e4b176a7a62a.avif'),
    'guided': ph('Canyonlands_Group_456d26f8-8539-46c5-b94f-8a2a610ab7a0.avif'),
    'day': ph('Zion_Bryce_Canyon_1_Day_From_Las_Vegas_5_9ccf4659-8118-4973-824e-4b61728dc0fd.avif'),
    'self': ph('ArizonaPinkJeep_0873e72b-ff52-49c9-9a80-3b4ada8ec70b.avif'),
    'private': ph('Capital_Reef_NP_Group_Shot_fe347266-db6e-484b-994d-36fb56f3883c.avif'),
    'large': ph('Alaska_Group_Exit_Glacier_2200_3357dba1-5e0b-4cab-95fc-97bfc2554f79.avif'),
    'rail': ph('AmaDahlia_Exterior_NileRiver_PhotogMS_Wings_8188_Edit_f464dba1-2d1c-4825-bd1e-8a4c8555a086.avif'),
    'winter': ph('Jackson_Yellowstone_Snowmobile_Adventure_Snowcoach_Snowmobiling_9ce8a3eb-bf00-45b2-a36d-a9ab32731e15.avif'),
    'event': ph('balloonfest_4_36b1c3a9-a93e-41af-be17-1f0beb36be29.avif'),
}

#: The nine cards in live order, with what each one's trips actually are
#: (lengths and lowest per-person prices off the cards on each style page).
STYLES = [
    ('backpacking', 'Backpacking', 7, '4&ndash;6 days on the trail', 'Up to 8 people, permits and a guide', 'from $1,895'),
    ('guided', 'Guided small group', 30, '2&ndash;13 days', '7&ndash;13 people, we drive, hotels &amp; lodges', 'from $1,849'),
    ('day', 'Day tour', 12, 'Half a day to a day', 'Out and back the same day', 'from $110'),
    ('self', 'Self-drive', 6, '5&ndash;10 days', 'Your car, our route and bookings', 'quoted'),
    ('private', 'Private &amp; custom', 4, '5&ndash;8 days', 'Your dates, your group only', 'quoted'),
    ('large', 'Large group', 3, '8&ndash;10 days', '20 or more of you, by coach', 'quoted'),
    ('rail', 'Rail &amp; cruise', 9, '7&ndash;12 days', 'The train or the ship is part of it', 'from $3,649'),
    ('winter', 'Winter', 3, '1&ndash;7 days', 'Snowcoach and snowmobile', 'from $129'),
    ('event', 'Special event', 0, '', '', ''),
]


def styles_top():
    return (j.top('Trip Styles') +
            f'<div class="w11-shero"><img src="{STYLE_PH["backpacking"]}" alt="">'
            '<div class="sh"><span class="w11-pill">Trip styles</span>'
            '<h1>How you want to travel</h1>'
            '<p class="lede">The same parks, nine different ways of being in them. '
            'Pick the one that matches how you like to move.</p></div></div>'
            + '<div class="sh">' + j.crumbs('Home', 'Trip styles') + '</div>')


def stylecard(k, name, n, *_):
    return (f'<div class="w11-sc"><img src="{STYLE_PH[k]}" alt="">'
            f'<div class="t"><p>{name}</p><span>{n} trips</span><b>Open</b></div></div>')


def styles_now():
    cards = ''.join(stylecard(*s) for s in STYLES)
    return page(styles_top() + f'<div class="sh"><div class="w11-sgrid">{cards}</div></div>')


def stylecard_lines(k, name, n, how, who, price):
    return (f'<div class="w11-sc2"><img src="{STYLE_PH[k]}" alt="">'
            f'<div class="b"><p class="n">{name} <span>{n} trips</span></p>'
            f'<p class="how">{how}</p><p class="who">{who}</p>'
            f'<p class="pr">{price}</p></div></div>')


def styles_lines():
    cards = ''.join(stylecard_lines(*s) for s in STYLES if s[2])
    return page(styles_top().replace('nine different ways', 'eight different ways')
                + f'<div class="sh"><div class="w11-sgrid">{cards}</div></div>')


#: Five doors on Jason's own splits: day vs multi-day, guided vs on your own,
#: public vs private. Winter and rail & cruise become ways to narrow a door.
DOORS = [
    ('day', 'A day out', 'Half a day to a full day, out and back. The easiest way '
     'to add a park to a trip you already have.', 'from $110 a person'),
    ('guided', 'A guided trip of several days', '2 to 13 days with 7 to 13 other guests. '
     'We drive, book the hotels and lodges, and pay the park fees.', 'from $1,849 a person'),
    ('backpacking', 'Nights on the trail', '4 to 6 days carrying a pack, up to 8 people, '
     'with the permits and a guide.', 'from $1,895 a person'),
    ('self', 'Drive it yourself', '5 to 10 days in your own car, on our route, '
     'with every night booked.', 'priced for your party'),
    ('private', 'Just your group', 'Your dates and your people, from a family to a '
     'coach of 40. Built around you.', 'priced for your group'),
]


def styles_doors():
    doors = ''.join(
        f'<div class="w11-door"><img src="{STYLE_PH[k]}" alt="">'
        f'<div class="b"><p class="n">{t}</p><p class="how">{d}</p>'
        f'<p class="pr">{p} <b>See trips &rsaquo;</b></p></div></div>'
        for k, t, d, p in DOORS)
    also = ('<div class="w11-also">Also: <span>Winter trips</span><span>Rail &amp; cruise</span>'
            '<span>Large groups</span></div>')
    top = styles_top().replace(
        'The same parks, nine different ways of being in them. Pick the one that '
        'matches how you like to move.', 'Five ways to take a trip with us. Pick the one that '
        'sounds like you.')
    return page(top + f'<div class="sh"><div class="w11-doors">{doors}</div>{also}</div>')


def styles_table():
    rows = ''.join(
        f'<tr><td><img src="{STYLE_PH[k]}" alt=""><b>{name}</b></td><td>{how}</td>'
        f'<td>{who}</td><td>{price}</td><td>{n}</td></tr>'
        for k, name, n, how, who, price in STYLES if n)
    return page(styles_top() + '<div class="sh"><table class="w11-stbl"><tr><th>Style</th>'
                '<th>How long</th><th>What it is</th><th>Price</th><th>Trips</th></tr>'
                f'{rows}</table></div>')


# -------------------------------------------------------------- 77 guides
REVIEW_SONSARI = ('We had 8 passengers on our bus mostly in our 70&rsquo;s and she '
                  'took care of all of us!')
REVIEW_KENDRA = ('Our guide, Kendra, truly made this tour shine. She was deeply '
                 'knowledgeable about the geology, history&hellip;')
REVIEW_ROBIN = ('The guide Robin Luse, was not only a walking encyclopedia of '
                'knowledge, but his ability to cheerfully accommodate the needs of a '
                'diverse group of 10 guests was superb.')
REVIEW_ANN = 'I had such a great time visiting the salt flats with tour guide, Ann.'

BIO = {
    'ann': ('Ann Evans', 'I spent the next 25 years working for the Utah Department of '
            'Natural Resources, spending most of those years as a Park Ranger/Naturalist.'),
    'phil': ('Phil Douglass', 'In 1986 he began working with the Utah Division of Wildlife '
             'Resources and retired after 32 years.'),
    'dennis': ('Dennis Bailey', 'I grew up with the Arches and Canyonlands as my backyard.'),
    'robin': ('Robin Luse', 'He moved to Albuquerque, New Mexico, and took his first steps '
              'as a tour guide. He&rsquo;s never looked back.'),
}


def reviews_band():
    """The home page's reviews band as it ships, the section a guides band would sit beside."""
    q = [('Cathy', 'Mighty 5 Utah Tour From Las Vegas',
          'We went on the &ldquo;Mighty Five&rdquo; tour begining October 5th. We had such a '
          'a wonderful experience! Our tour guide, Sonsari was truly the best!'),
         ('Dawn', 'Trail of the Ancients',
          'Wow - what a fabulous trip! The guide Robin Luse, was not only a walking '
          'encyclopedia of knowledge&hellip;'),
         ('Keith', 'Mighty 5 Utah From Salt Lake City',
          'The Mighty Five was on our bucket list. Our guide, Kendra, truly made this '
          'tour shine.')]
    cards = ''.join(f'<div class="w11-rv"><i>&#9733;&#9733;&#9733;&#9733;&#9733;</i>'
                    f'<p>&ldquo;{t}&rdquo;</p><b>{n}</b><span>{tr}</span></div>'
                    for n, tr, t in q)
    return ('<div class="sh w11-sec"><h2 class="w9-h2">What people say when they get home</h2>'
            '<p class="w11-sub">&#9733;&#9733;&#9733;&#9733;&#9733; 4.8 out of 5 on Google, '
            'from 256 reviews of Southwest Adventure Tours</p>'
            f'<div class="w11-rvs">{cards}</div></div>')


def guides_now():
    return page(reviews_band() +
                '<div class="sh w11-sec"><h2 class="w9-h2">The parks we guide</h2>'
                '<p class="w11-sub">Eight park tiles follow. No guide, and no face, appears '
                'anywhere on the home page.</p></div>')


def gcard(key, quote=None, guest=None):
    name, bio = BIO[key]
    g = (f'<p class="guest">&ldquo;{quote}&rdquo;<span>{guest}</span></p>' if quote else '')
    return (f'<div class="w11-g"><img src="{GUIDES[key]}" alt=""><div class="b">'
            f'<p class="n">{name}</p><p class="bio">&ldquo;{bio}&rdquo;</p>{g}</div></div>')


def gslot(name, quote, guest):
    return (f'<div class="w11-g slot"><div class="ph">Photo from SWAT</div><div class="b">'
            f'<p class="n">{name}</p><p class="bio">Her own two lines, from SWAT</p>'
            f'<p class="guest">&ldquo;{quote}&rdquo;<span>{guest}</span></p></div></div>')


def guides_bios():
    cards = ''.join(gcard(k) for k in ['ann', 'dennis', 'phil', 'robin'])
    return page(reviews_band() +
                '<div class="sh w11-sec"><h2 class="w9-h2">The people who guide your trip</h2>'
                '<p class="w11-sub">In their own words, from their pages on this site.</p>'
                f'<div class="w11-gs">{cards}</div></div>')


def guides_guests():
    cards = (gslot('Sonsari', REVIEW_SONSARI, 'Cathy, Mighty 5 from Las Vegas')
             + gslot('Kendra', REVIEW_KENDRA, 'Keith, Mighty 5 from Salt Lake City')
             + gcard('robin', REVIEW_ROBIN, 'Dawn, Trail of the Ancients')
             + gcard('ann', REVIEW_ANN, 'a guest, Bonneville Salt Flats'))
    return page('<div class="sh w11-sec"><h2 class="w9-h2">The people who guide your trip</h2>'
                '<p class="w11-sub">What guests said about them, and what they say about '
                'themselves.</p>'
                f'<div class="w11-gs">{cards}</div></div>' + reviews_band())


# --------------------------------------------------------------- 78 prices
GLACIER = ph('supplied/glacier-national-park/flathead-river.avif', 828)
AMA = ph('AmaDahlia_Exterior_NileRiver_PhotogMS_Wings_8188_Edit_f464dba1-2d1c-4825-bd1e-8a4c8555a086.avif')


def pricebox(amount, basis, nxt, extra=''):
    return ('<div class="w11-pbox"><p class="k">From</p>'
            f'<p class="amt">{amount}</p><p class="bs">{basis}</p>'
            f'<p class="nx">{nxt}</p>{extra}<b class="btn">Choose your date</b></div>')


def amacard(price, unit, grp):
    return ('<div class="w9-card w11-ama"><div class="ph">'
            f'<img src="{AMA}" alt=""><span class="st">RAIL &amp; CRUISE</span>'
            '<span class="du">12 days</span></div><div class="bd">'
            '<div class="tt">AMA Waterways: Gems of Southeast Europe Christmas Markets</div>'
            '<div class="rt">International</div>'
            f'<ul><li>Easy</li><li>{grp}</li></ul>'
            f'<div class="pr"><b>{price}</b><span>{unit}</span></div>'
            '<div class="go"><span>View tour</span><span>Check dates</span></div></div></div>')


def prices(box, card):
    return (f'<div class="w11-prices"><div class="left">'
            '<p class="lab">Glacier National Park Tour, the booking panel</p>'
            f'<h1>Glacier National Park Tour</h1>{box}</div>'
            f'<div class="right"><p class="lab">A card on the Rail &amp; cruise page</p>{card}</div></div>')


def prices_now():
    return page(prices(pricebox('$3,649', 'per person, double occupancy, 2026',
                                'Next departure Jun 20, 2027'),
                       amacard('$250', 'from / person', 'Small group, 7&ndash;13')))


def prices_real():
    return page(prices(pricebox('$3,899', 'per person, sharing a room &middot; 2027 dates',
                                'Next departure Jun 20, 2027'),
                       amacard('Price on request', '', 'River cruise ship')))


def prices_alone():
    extra = ('<div class="w11-alone"><p><span>Travelling alone</span><b>from $4,349</b></p>'
             '<p><span>Three sharing</span><b>from $3,699</b></p>'
             '<p class="inc">What the price includes &rsaquo;</p></div>')
    return page(prices(pricebox('$3,899', 'per person, sharing a room &middot; 2027 dates',
                                'Next departure Jun 20, 2027', extra),
                       amacard('Price on request', '', 'River cruise ship')))


# ------------------------------------------------------------ 79 next step
ZION = ph('Zion_Checkerboard_Mesa_Group_Photo_ded30d2e-ad40-4010-ae62-e4b176a7a62a.avif', 828)


def zion_top(rail, strip):
    thumbs = ''.join(f'<i style="background-image:url({ph(p, 384)})"></i>' for p in [
        'zion_narrows_hiking_1c5dbf86-c3b0-4e7d-9d42-83567c077844.avif',
        'zion_park_narrows_8fce93ec-ded1-43ac-977f-b518ab7f13cb.avif',
        'zion_thumb_dd214d08-1ed7-43ab-ae27-5a0d88a7d040.avif',
        'zion_weekping_66eb9c91-034b-4082-8e97-032abe4f57f3.avif'])
    facts = ''.join(f'<span class="{c}">{t}</span>' for t, c in strip)
    # 700 of the 900: the rest of the window is the tour bar and a notice,
    # identical in every option, and white below the drawing read as a gap.
    return win(j.top('Trip Styles') + '<div class="sh">' + j.crumbs('Home', 'Trip styles', 'Day tour', 'Zion Park 1-Day Tour') + '</div>' +
               '<div class="sh"><div class="w11-tour">'
               f'<div class="gal"><img src="{ZION}" alt=""><div class="th">{thumbs}</div>'
               f'<div class="facts">{facts}</div></div>'
               '<div class="side"><div class="bdg"><span class="st">DAY TOUR</span>'
               '<span>ZION NATIONAL PARK</span></div><h1>Zion Park 1-Day Tour</h1>'
               f'{rail}</div></div></div>', h=700)


STRIP_NOW = [('1 day', ''), ('Ask us', 'ask'), ('Small group, up to 14', ''),
             ('Several cities &mdash; ask us', 'ask'), ('Dates on request', 'ask'), ('$999', '')]
STRIP_REAL = [('1 day', ''), ('Ask us', 'ask'), ('Up to 14', ''),
              ('Leaves St. George, Zion or Bryce', 'fix'), ('Dates on request', 'ask'), ('$999 for up to 4', 'fix')]


def zion_now():
    rail = ('<div class="w11-rl"><p class="k">From</p><p class="amt">$999</p>'
            '<p class="bs">total, for up to 4 people</p><b class="btn">Ask a question</b></div>'
            '<p class="w11-far">&ldquo;Request a quote&rdquo; is 1,392px down the page</p>')
    return zion_top(rail, STRIP_NOW)


def zion_quote(real=False):
    extra = ('<p class="more">Each extra person $200 &middot; all inclusive</p>' if real else '')
    rail = ('<div class="w11-rl"><p class="k">From</p><p class="amt">$999</p>'
            f'<p class="bs">total, for up to 4 people</p>{extra}'
            '<div class="w11-qf"><label>Date<span>Pick a day</span></label>'
            '<label>People<span>2</span></label>'
            '<label>Leaving from<span>St. George</span></label></div>'
            '<b class="btn">Get my price</b>'
            '<p class="sm">We reply within one business day. Nothing is charged.</p></div>')
    return zion_top(rail, STRIP_REAL if real else STRIP_NOW)
