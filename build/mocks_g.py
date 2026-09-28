"""Mockup primitives for round six — the reviews page, decision 45.

Crow, 28 September, on the page the home page's "Read all 118 reviews" link
opens: *"this entire page looks bad, its all just text, its hard to really get
a good feeling for reviews."*

Measured off the **deployed production build** at **1440x900** on
28 September 2026, `swat-website-storefront.vercel.app/guides/
testimonials-and-reviews/` (gate 6666):

  Chrome        strip 36px, header 73px, deals ticker 50px; `main` at y=159.
  Hero          1,425x378 — a group photo whose ORIGINAL is **270x202**, so it
                is drawn **5.3x** its real size under a dark tint.
  Column        one **686px** text column at x=252, **18,001px** tall.
  Reviews       **151 paragraphs**, about **5,700 words**, no headings at all.
                The third and fourth paragraphs praise **Glenn** — the guide
                operations said left about six years ago. 62 of the 151 name a
                guide; almost none name a trip.
  Photos        four inline, each **246px** originals drawn at **686px** wide
                (2.8x), captioned with their **filenames**: "van",
                "queens-garden", "group-on-top", "rock-monolith".
  Footer        736px at y=18,928.
  The page      **19,664px** — about 22 screens of a 900px window.

And the one that matters most: **none of the 42 current reviews** Matt picked
by trip — the three printed directly above the link that opens this page —
appear anywhere on it.
"""

import mocks as m

WINDOW = 900
PAGE_NOW = 19664

_ARCHIVE = ("https://pyxnpjvtdlucaqqhhvin.supabase.co/storage/v1/object/public/"
            "media/derived/{w}/photos/{f}")

HERO_NOW = _ARCHIVE.format(w='w1600', f='group_bryce_054248d1-9fc7-437d-95d5-e317f0bec291.avif')
VAN_NOW = _ARCHIVE.format(w='w828', f='van_4b1c7758-69f9-4daa-b80f-93143bd49ef3.avif')

#: The opening of the archive page, verbatim, bullets and all.
ARCHIVE = [
    '&bull; &ldquo;It was an awesome itinerary! Our accommodations were excellent. '
    'The sites we were suggested to visit were spectacular, directions from and '
    'too were clear, and the people we met on our trip were as wonderful as the '
    'sites we were able to see. We did an Alaskan Cruise last year through '
    'another provider. This 10 day self drive with Southwest Adventure Tours tops '
    'last year&rsquo;s experience by a mile! If you don&rsquo;t know who to go '
    'with, let me suggest this 10 out of 10 trip organizer!&rdquo;',
    '&bull; &ldquo;The trip was everything we expected and more! Cannot compliment '
    'our guide Robin Luse enough. He simply made the tour by being friendly, easy '
    'going, and so knowledgeable, plus great music! The van was comfortable and '
    'our accommodations and meals were good. We were, of course, awed by Glacier '
    'as first time visitors but we are convinced that our visit there was such a '
    'success because of Robin and Southwest Adventure Tours. We do hope to travel '
    'with you again.&rdquo;',
    '&ldquo;The trip yesterday was amazing. Glenn was such a great tour guide and '
    'added to the memorable experience and never rushed us at all. I would '
    'recommend him to anyone and would do another trip myself and request him '
    'the next time I come out there. Hopefully for a trip to Moab.&rdquo;',
    '&ldquo;Our driver/guide Glenn has been fantastic all the way for '
    'information/introduction and it has been a long day for him when we are '
    'back @9pm. I didn&rsquo;t know your company before so I normally go for '
    'viator/gray line. But I will definitely recommend your trips to anyone that '
    'I know who is coming to the Wild West.&rdquo;',
    '&ldquo;So nice to have someone take care of me for awhile. Haydee did an '
    'excellent job. I had no worries, she took care of everything. I would love '
    'to go on another adventure with her as my guide.&rdquo;',
    '&ldquo;We have taken many tours and this is by far the best tour guide we '
    'have ever had. Haydee goes out of her way in a very pleasant way to '
    'accommodate everyone, regardless of their physical abilities.&rdquo;',
    '&ldquo;Raveny was outstanding. She kept us on schedule, was accommodating to '
    'individual preferences and arranged hikes to suit our interests. She was '
    'knowledgeable, friendly, helpful.&rdquo;',
    '&ldquo;Sarah was a fantastic guide! She has a great personality and was very '
    'knowledgeable about everything we were seeing. We loved every moment of our '
    'journey and hope to come back and do one of your longer tours.&rdquo;',
    '&ldquo;Dennis was extremely knowledgeable, went out of his way to '
    'accommodate us all. His patience and willingness to go the extra mile '
    'commendable. We were all thankful he was our guide. The best.&rdquo;',
    '&ldquo;Jason couldn&rsquo;t have done anything better. His service and '
    'knowledge was impeccable.&rdquo;',
]

#: Matt's reviews, verbatim (trimmed where a card clamps them anyway), for the
#: trips drawn. Photo keys are the trip's own parks — never a borrowed frame.
TRIPS = [
    ('Mighty 5 Utah from Salt Lake City', 'arches', 6, [
        ('I can not say enough good things about my Mighty 5 tour! Our tour guide '
         'Brandon was wonderful. We had a really mixed level group, Brandon made '
         'sure everyone was able to experience the tour they wanted. He gave '
         'alternatives hikes for people who wanted more and easier ones for those '
         'who wanted less.', 'Mary'),
        ('Great trip! Mighty 5 out of SLC was well organized and exactly what I '
         'was hoping for to see all of Utahs parks. Tour guide Ashley was '
         'knowledgeable, interesting, fun and excellent at managing a multi level '
         'group.', 'N. Tustin'),
        ('We got back last week from our Mighty Five tour out of Salt Lake City. '
         'It was one of the best vacations and tours I have ever taken. I have '
         'been on large tours and now the smaller tour and much prefer the smaller '
         'tour atmosphere.', 'Linda'),
    ]),
    ('Grand Teton &amp; Yellowstone', 'teton', 5, [
        ('My dad and I had an amazing time in the Grand Tetons and Yellowstone '
         'adventure! Michelle was amazing as our guide, the tour was well paced '
         'and amazing. I took a ton of photos, saw amazing sites, saw a ton of '
         'wildlife.', 'Linda'),
        ('I had such a fabulous trip to Tetons and Yellowstone this summer. The '
         'hotels were great and our guide accommodated our requests as to what '
         'level of exercise we wanted. Water and bear spray was supplied as well '
         'as lunch each day.', 'Suzie'),
        ('This tour of Grand Tetons and Yellowstone was my second tour with '
         'Southwest Adventure Tours. Sarah, our guide, was excellent and brought '
         'experience and a wealth of knowledge to our touring experience.', 'Lou'),
    ]),
    ('Alaska&rsquo;s Northern Lights', 'auroras', 5, [
        ('The Northern Lights Tour was fantastic! We did so much in 5 days! Not '
         'only were the lights phenomenal- we went snowmobiling, dog sledding and '
         'ice fishing!', 'Linda'),
        ('Did the Aurora borealis tour in Alaska and it was phenomenal! '
         'Communication good prior to tour. Matthew, our tour guide was '
         'knowledgeable, funny and I can&rsquo;t say enough good about him!',
         'Wendi'),
        ('Our tour was amazing and it was all due to having an awesome guide. '
         'Matthew not only toured us around to our locations, but he had tons of '
         'fun facts about Alaska, stories to tell.', 'Greg'),
    ]),
    ('Black Hills of South Dakota', 'rushmore', 3, [
        ('A fabulous balance of nature, history and wildlife in a comfortable '
         'van. Tom is the best&mdash;personable, knowledgeable, helpful; a great '
         'leader and driver.', None),
        ('We covered a lot of ground on the tour - the itinerary was packed with '
         'incredible sights and memorable spots in the Blackhills/Badlands area. '
         'Tom was professional, energetic, and attentive to each tour member.',
         'Kenny'),
        ('Excellent itinerary. Loved the small group size. Tom C., our guide, '
         'was fun, informative and very adaptable.', None),
    ]),
    ('Glacier National Park', 'glacier', 3, [
        ('Spent 5 days in Montana with Winn as our driver! He&rsquo;s the BEST! '
         'He has great stories, lots of knowledge (but not the kind that is '
         'overbearing) and is super kind.', None),
        ('We had a fabulous time. Our driver, tour guide, Ben, was the best! He '
         'shared lots of good information and history about the sites we were '
         'visiting.', 'Susan'),
        ('I recently did a tour of Glacier National Park and it was an incredible '
         'experience. We saw so much wildlife including black bears.', None),
    ]),
    ('Yosemite, Sequoia &amp; the California Coast', 'yosemite', 4, [
        ('This trip exceeded all my expectations and beyond. The tour guide, Matt '
         'Graber, is outstanding. All the places we toured left me in awe with '
         'their breathtaking beauty.', 'Annette'),
        ('Had a wonderful time with a great group of travelers and an even better '
         'guide, Jeremy! We hit Yosemite, Sequoia, Kings Canyon, Cambria, '
         'Monterey, San Fran.', 'Jane'),
        ('Awesome points of interest, excellent, knowledgeable guide, and meals '
         'were over the top.', None),
    ]),
]

CHIPS = ['All 13 trips', 'Mighty 5 from Salt Lake City', 'Grand Teton &amp; Yellowstone',
         'Northern Lights', 'Glacier', 'Black Hills', 'Yosemite &amp; Sequoia',
         'Winter Yellowstone', 'Grand Circle', 'Trail of the Ancients', 'Oregon Coast',
         'Death Valley', '+2']

STARS = '<span class="v-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'


# ------------------------------------------------------------------- chrome
def chrome():
    return ('<div class="v-chrome">' + m.header(active='', strip=True)
            + m.ticker() + '</div>')


def pageend(txt):
    return (f'<div class="b-end"><span>the page carries on below &middot; '
            f'{txt} in all</span></div>')


def fold(top=WINDOW):
    return (f'<div class="m-fold" style="top:{top}px">'
            '<span>bottom of a 1440&times;900 window</span></div>')


def google_line(light=True):
    c = ' light' if light else ''
    return (f'<div class="v-google{c}">{STARS}'
            '<span><b>4.8</b> out of 5 on Google, from 255 reviews</span></div>')


def card(text, name, trip=None, cls=''):
    by = name or 'A guest'
    t = f'<a class="v-trip">{trip}</a>' if trip else ''
    return (f'<div class="v-card {cls}">{STARS}<p>{text}</p>'
            f'<div class="v-by"><b>{by}</b>{t}</div></div>')


# ------------------------------------------------------------------ the pages
def page_now():
    """What ships: a blown-up thumbnail and 18,001px of one text column."""
    paras = ''.join(f'<p>{t}</p>' for t in ARCHIVE[:4])
    paras2 = ''.join(f'<p>{t}</p>' for t in ARCHIVE[4:])
    return (chrome() +
            '<div class="v-nhero">'
            f'<img src="{HERO_NOW}" alt="">'
            '<div class="v-ntint"></div>'
            '<div class="v-ntext"><span class="v-pill">Guides &amp; resources</span>'
            '<h1>Customer Reviews</h1></div></div>'
            '<div class="v-ncol">'
            '<div class="v-crumbs">Home / Guides &amp; resources / <b>Customer Reviews</b></div>'
            f'<div class="v-nbody">{paras}'
            f'<figure class="v-nfig"><img src="{VAN_NOW}" alt="">'
            '<figcaption>van</figcaption></figure>'
            f'{paras2}</div></div>'
            + pageend('19,664px, about 22 screens,') + fold())


def hero_score(quote=None):
    """Navy band: the Google score, big, and the way to the rest."""
    q = ''
    if quote:
        q = (f'<blockquote class="v-hq">&ldquo;{quote[0]}&rdquo;'
             f'<cite>{quote[1]} &middot; {quote[2]}</cite></blockquote>')
    return ('<div class="v-shero"><div class="v-shell v-shero-in">'
            '<div><div class="v-eyebrow">In their words</div>'
            '<h1>What people say when they get home</h1>'
            '<div class="v-bigscore"><b>4.8</b><div>'
            f'{STARS}<span>out of 5 on Google<br>from 255 reviews</span></div></div>'
            '<div class="v-hbtns"><span class="v-btn">Read them on Google</span>'
            '<span class="v-btn ghost">Find a trip</span></div></div>'
            f'{q}</div></div>')


def page_cards():
    """B: the same archive, drawn as cards in three columns."""
    cards_ = ''.join(card(t.replace('&bull; ', ''), None) for t in (ARCHIVE + ARCHIVE[:8]))
    return (chrome() + hero_score() +
            '<div class="v-shell v-sec">'
            '<div class="v-h2">Every review we have ever published</div>'
            f'<div class="v-masonry">{cards_}</div></div>'
            + pageend('about 8,500px') + fold())


def tripsection(trip, photo, n, reviews):
    cards_ = ''.join(card(t, name) for t, name in reviews)
    more = f'<span class="v-more">{n - 3} more &rarr;</span>' if n > 3 else ''
    return ('<div class="v-trow">'
            '<div class="v-tpic">' + m.img(photo, 380, 300) +
            f'<div class="v-tcap"><b>{trip}</b><span>{n} reviews</span>'
            '<a>See this trip &rarr;</a></div></div>'
            f'<div class="v-tcards">{cards_}{more}</div></div>')


def page_bytrip():
    """C: current reviews, one row per trip, the trip's own photograph beside them."""
    chips = ''.join(f'<span class="{"on" if i == 0 else ""}">{c}</span>'
                    for i, c in enumerate(CHIPS))
    rows = ''.join(tripsection(*t) for t in TRIPS)
    return (chrome() +
            hero_score(('The Northern Lights Tour was fantastic! We did so much '
                        'in 5 days! Not only were the lights phenomenal, we went '
                        'snowmobiling, dog sledding and ice fishing!',
                        'Linda', 'Alaska&rsquo;s Northern Lights')) +
            f'<div class="v-chips"><div class="v-shell">{chips}</div></div>'
            f'<div class="v-shell v-sec">{rows}'
            '<div class="v-archive">Older reviews from our archive &middot; 118 '
            '<span>&#9662;</span></div></div>'
            + pageend('about 6,000px') + fold())


def page_wall():
    """D: a photo hero with one quote on it, then a wall of photos and quotes."""
    chips = ''.join(f'<span class="{"on" if i == 0 else ""}">{c}</span>'
                    for i, c in enumerate(CHIPS))
    tiles = []
    order = [0, 1, 2, 3, 4, 5]
    for i in order:
        trip, photo, n, reviews = TRIPS[i]
        tiles.append('<div class="v-wpic">' + m.img(photo, 320, 400 if i % 2 else 260)
                     + f'<span>{trip}</span></div>')
        for t, name in reviews[:2]:
            tiles.append(card(t, name, trip))
    return (chrome() +
            '<div class="v-whero">' + m.img('teton', 1440, 560) +
            '<div class="v-wtint"></div><div class="v-shell v-wtext">'
            '<blockquote>&ldquo;Sarah was the absolute best guide we could have '
            'imagined. She inspired the entire group to be curious and excited '
            'about the natural world.&rdquo;</blockquote>'
            '<cite>Grand Teton &amp; Yellowstone</cite>'
            + google_line() + '</div></div>'
            f'<div class="v-chips"><div class="v-shell">{chips}</div></div>'
            f'<div class="v-shell v-sec"><div class="v-wall">{"".join(tiles)}</div></div>'
            + pageend('about 5,000px') + fold())
