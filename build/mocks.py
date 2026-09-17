"""
Mockup primitives for the decision sheet.

Every mockup is real HTML at a real 1200px width, painted with the storefront's
own tokens (globals.css) and its own photography, then scaled into whatever
column it lands in. Nothing here is a grey box: the point of the sheet is that
Crow can judge a layout, and a wireframe of rectangles cannot be judged against
a build that has photographs in it.

**Everything in this file is read off the deployed storefront, not remembered.**
The nav items are `NAV_ITEMS` from `PrimaryNav.tsx`. The six cards under
"Bookable now" are the six the production home page actually renders, with their
own photographs, durations, group sizes and prices. The ticker carries the eight
live deals with their real promo codes. Column counts, card widths and gaps are
the measured `grid-template-columns` and bounding boxes at a 1200px viewport —
3-across at 350px for trip cards, 4-across at 263px for photo tiles. The sheet
was drawing everything 4-across at 252px, which is not a width the site has.

Sources, re-harvested 2026-09-16 off the DEPLOYED STAGING build at a 1200px
viewport, after round one of the 16 September notes shipped:
  home    https://swat-website-storefront-git-staging-swat2.vercel.app/
  tour    .../tours/mighty-5-utah-from-las-vegas/
  styles  .../trips/
  builder .../review/build/
Everything below is measured, not remembered. At 1200px the trip shelf is
3-across at 350.2px with 515px-tall cards; the tour page runs a 672x380 gallery
against a 395px title column, a 1185px fact strip at y=659, a sticky subnav at
y=847, the navy change notice at y=961 and a 360px booking rail beside it.
Re-derive before the next round: the featured eight and the live deals rotate.

`SUPA` renders at an explicit width AND height on purpose — the Supabase render
endpoint returns the ORIGINAL height when only `width` is sent, so a width-only
URL silently ships a stretched photo that object-fit then hides.
"""

SUPA = ("https://pyxnpjvtdlucaqqhhvin.supabase.co/storage/v1/render/image/public/"
        "media/photos/")

# The real wordmark, served ungated from the storefront's own asset directory.
# A text logo was standing in for it and read as a different brand.
WORDMARK = ("https://swat-website-storefront.vercel.app/brand/"
            "southwestadventures_logo_white.svg")

PHOTOS = {
    # --- the six trips the home page actually features
    'antelope':  'Antelope_Island_Bison_on_Antelope_Island_State_Park_Utah_9_10_SG1191_Full_646d79ca-8b70-4ae8-a19e-33bd97670913.jpg',
    'bonneville': 'diego_AM53LSIBnRo_unsplash_a5705af3-f19e-41fc-b73c-f1e0f7848088.jpg',
    'darksky':   'antelope_isle_dark_sky_8388d7cf-336f-4d30-b3f8-4c881929c960.jpg',
    'parkcity':  'Utah_olympic_park_ski_jumping_stands_629349a9-125b-465f-8ea9-b5eebe703905.jpg',
    'kanarra':   'waterfall_20f4719e-b6a9-4b65-9d11-1929d91c909c.jpg',
    'ama':       'AmaLilia_SunDeck_Pool_PhotogNER_Wings_75_edit_c67dc4d4-8052-4ef4-900f-460b996bcc24.jpg',

    # --- the four doors, in page order
    'door_place':  'Bryce_Canyon_thors_hammer_26bf9126-1c47-46ae-aaeb-209aaa150bcf.jpg',
    'door_start':  'Airport_SLCIA_4266_93956393-7e58-4932-b575-51d00146d739.jpg',
    'door_travel': 'Zion_Checkerboard_Mesa_Group_Photo_ded30d2e-ad40-4010-ae62-e4b176a7a62a.jpg',
    'door_dates':  'Canyonlands_NP_Mesa_Arch_Sunrise_f3640be2-06e8-4df8-9095-a0599a10d97d.jpg',

    # --- "The parks we guide", in page order
    'arches':    'Mighty_5_SLC_Arches_Delicate_Arch_2_f8a9ac42-afeb-416c-bc29-885e0e53857a.jpg',
    'badlands':  'BadlandsNP2_7eb69b03-83aa-43bf-9e53-67cb683d916b.jpg',
    'bryce':     'IMG_8063_f2cad211-4fb0-4852-aa64-7c54bcc98b58.jpg',
    'yosemite':  'Yosemite_Sequoia_Half_Dome_1__fe6e4aa2-9294-4fed-864d-ac96cfcb93f6.jpg',
    'capitol':   '152_5234_2200px_02d3b5ab-acaa-472a-a19c-9b589b7adfea.jpg',
    'colorado':  'matt_koffel_3LawUms86Y_unsplash_f19af6d2-1670-4b34-8862-dc3ece0f0d0c.jpg',
    'denali':    'DSCN6186_e9931339-9ac8-447b-b711-75dd5374c070.jpg',
    'arizona':   'Sedona_Grand_anyoun_3_Day_1_46238139-153b-4bf1-b356-bb58a009d70c.jpg',

    # --- the home hero, and the tour page
    'hero':      'windows_section_arches_05063611-79a7-4808-8a5b-183dfdb4dd13.jpg',
    'zion':      'ZionTowersVirgin_8a7ab233-398c-49f0-bbc6-f70554bb9c2d.jpg',
    'zion2':     '01e3_fdfe0d96-cfab-485e-bf50-6af13c9107ee.jpg',
    'hoodoo':    'Salt_Lake_City_Zion_Bryce_Canyon_1_Day_12_21a7ecd9-2bce-4c63-b5de-c90c7e9d9b19.jpg',
    'mesa':      'Canyonlands_NP_Mesa_Arch_Sunrise_f3640be2-06e8-4df8-9095-a0599a10d97d.jpg',

    # --- elsewhere on the site
    'templesq':  'Temple_Square_83c9d848-ff03-4ca6-b224-8a5a8c0f2763.jpg',
    'vegas':     'LasVegas_49960e88-ff68-4020-bdbd-7249506bf07f.jpg',
    'moab':      'Moab_3b6e6bc1-861f-41e7-870d-8cdabae11380.png',
    'northrim':  'IMG_7900_5254b53d-5ce7-4b94-936f-3b183e4be7e4.jpg',
    'prismatic': 'jeromey_balderrama_0pmsaCGi_z0_unsplash_31e43278-5305-4210-b997-f63d32741c9a.jpg',
    'glacier':   'GlacierNP1_2200px_48b0e1b4-d29a-4ca7-942d-53ee2534bf48.jpg',
    'oregon':    'Oregon_South_Newport_63759ef7-6fdd-4762-aa77-bfda314c4f75.jpg',
    'mesaverde': 'Balcony_House_Mesa_Verde_National_Park_c432b9af-9da6-4627-9fa9-8b89b5b00481.jpg',

    # --- round three, 2026-09-02: read off the deployed STAGING build
    'm5slc':       'Bryce_Canyon_Great_Basin_Zion_National_Parks_3_4536d187-7910-4432-8ca6-5dddf785ade7.jpg',
    'stgeorge':    'Dinosaur_museum__f99d5357-2887-43fa-a382-50a64355a1bc.jpg',
    'escalante':   'CalfCreekFalls_Michael_Kunde_Photo_0201_27bcbe60-8012-48a3-94f7-7a317b4b8f2d.jpg',
    'grandcircle': 'Grand_Circle_Experience_1_b34d81e7-7f65-43ea-bdd9-509d34545a86.jpg',
    'ancients':    'Trail_of_the_Ancients_Header_1__4ef83398-a2e4-4912-9ef3-fcf15bafc962.png',
    'oregoncoast': 'dan_meyers_0H_Cc4o7JP0_unsplash_cd84ae00-3403-47bb-b90c-c025752e543c.jpg',
    'srim':        'Dawn_on_the_S_rim__4cd55a6b-50b5-416a-974e-d51b825465f8.jpg',
    'snowbird':    'IMG_7994_0b2a2167-7265-4fbc-8bb3-14acc08c4986.jpg',
    'zion3':       'Zion_Bryce_Canyon_1_Day_From_Las_Vegas_2_6c78cd85-f840-433b-9126-8a3a136e14b8.jpg',
    'rainier':     'Mount_Rainier_from_Indian_Henry_4380440b-846d-4215-8bf4-c314b9065dec.jpg',
    'rushmore':    'mt_rushmore_orig_60b85af2-020d-405f-95ee-0fe052ec072d.jpg',
    'mormon':      'nauvoo_illinois_mormon_temple_5c7eee49-ec78-4265-9572-b65c583f7869.jpg',
    'teton':       'Grand_Teton_Schwabaucher_Landing_1463fccb-d19a-446b-b2dd-bee4df310fc2.jpg',
    'auroras':     'Northern_Lights_1_b3dddbe0-b89d-4cda-b1fc-a666bc2cea1b.jpg',
    'snowmobile':  'Lion_Group_Winter_e69b083e-9042-4e27-8cfc-6e0f7ea5383f.jpg',
    'ystwinter':   'Yellowstone_3_f73108fa-a6e0-4c87-a8ce-558a8c675761.jpg',
}


# --------------------------------------------------------------- live content

#: The catalogue counts the home page prints in its own eyebrow. Production
#: serves 74 of the 93 harvested tours; the sheet said 93 and 12, which is the
#: draft catalogue, not the live one.
TOURS_LIVE = 74
CITIES_LIVE = 10

#: The eight trips under "Bookable now in November", in the order the deployed
#: staging build renders them, with the activity level each card actually
#: prints. Three say "on request", one says Strenuous, the rest Easy — which is
#: the spread decision 20 has to survive. Round one of the 16 September notes
#: moved this shelf from six cards to eight and put a 60-day floor under it, so
#: in mid-September it is November's departures.
FEATURED = [
    ('zion', 'Small group', '5 days', 'Mighty 5 Utah Tour From Las Vegas',
     'Las Vegas &rarr; Zion National Park',
     'Zion National Park, Bryce Canyon National Park, Arches National Park',
     'Easy', 'Small group, 7&ndash;13', '$1,999'),
    ('auroras', 'Small group', '6 days',
     'Alaska&rsquo;s Northern Lights Adventure Tour', None,
     'Denali National Park, Alaska', 'Easy', 'Small group, 7&ndash;13', '$3,429'),
    ('m5slc', 'Small group', '8 days', 'Mighty 5 Utah From Salt Lake City',
     'Salt Lake City &rarr; Zion National Park',
     'Zion National Park, Bryce Canyon National Park, Arches National Park',
     'Strenuous', 'Small group, 7&ndash;13', '$3,499'),
    ('antelope', 'Day tour', '1 day', 'Great Salt Lake and Antelope Island',
     None, 'Utah', 'on request', 'Small group, up to 14', '$110'),
    ('bonneville', 'Day tour', 'Half day', 'Bonneville Salt Flats Adventure',
     None, 'Multiple parks', 'on request', 'Small group, up to 14', '$110'),
    ('darksky', 'Day tour', 'Duration on request',
     'Salt Lake Antelope Island Dark Sky Experience', None, 'Multiple parks',
     'on request', 'Small group, up to 14', '$110'),
    ('parkcity', 'Winter', '1 day', 'Park City &amp; Olympic Heritage Excursion',
     'Salt Lake City &rarr; Utah', 'Utah', 'on request',
     'Small group, 7&ndash;13', '$129'),
    ('kanarra', 'Day tour', 'Half day', 'Kanarra Falls',
     'St George &rarr; Zion National Park', 'Zion National Park, Utah',
     'Moderate', 'Small group, up to 14', '$225'),
]

#: The four doors under "Start where you are", verbatim.
DOORS = [
    ('door_place', 'I know the place', 'Zion, Yellowstone, Yosemite and 21 more parks.'),
    ('door_start', 'I know where I&rsquo;m starting', 'Everything that leaves from your city.'),
    ('door_travel', 'I know how I want to travel', 'Backpacking, day tours, self-drive, private.'),
    ('door_dates', 'I know my dates', 'Filter the whole catalogue by month.'),
]

#: "The parks we guide", in page order, with the photographs the site uses.
PARKS = [
    ('arches', 'Arches and Canyonlands National Parks'),
    ('badlands', 'Badlands National Park'),
    ('bryce', 'Bryce Canyon National Park'),
    ('yosemite', 'California'),
    ('capitol', 'Capitol Reef National Park'),
    ('colorado', 'Colorado National Parks'),
    ('denali', 'Denali National Park'),
    ('arizona', 'Explore Arizona'),
]

#: The live Hot Deals, with the promo codes the ticker actually prints.
DEALS = [
    ('Grand Canyon &amp; Arizona Adventure', 'September 20', '$600 off per person', 'AZ600'),
    ('Black Hills of South Dakota', 'September 21', '$400 off per person', 'BLACK400'),
    ('Black Hills of South Dakota', 'September 28', '$400 off per person', 'BLACK400'),
    ('Canyons of the Escalante', 'October 25', '$500 off per person', 'CANYONS500'),
]

#: The tour page every tour mockup is drawn from.
TOUR = {
    'title': 'Mighty 5 Utah Tour From Las Vegas',
    'badges': ['Guided small group', 'Easy', 'Zion National Park'],
    'intro': ('One of our most popular tours, Southwest Adventure Tours will show '
              'you Utah&rsquo;s Mighty 5 national parks in 5 days. Those parks are '
              'Arches, Bryce Canyon, Canyonlands, Capitol Reef, and Zion.'),
    'facts': [('Duration', '5 days'), ('Activity level', 'Easy'),
              ('Group size', 'Small group, 7&ndash;13'), ('Departs from', 'Las Vegas'),
              ('Next departure', 'Sep 7, 2026'), ('From', '$1,999')],
    'subnav': ['Overview', 'Tour highlights', 'Day by day', 'Tour details',
               'Gallery', 'More photos', 'Reserve a place', 'Departures',
               'Pricing', 'Trip protection'],
    'price': '$1,999',
    'photo': 'zion',
}


# ------------------------------------------------------------------ plumbing

def img(key, w, h, cls='', style=''):
    """A real photograph at an explicit width and height."""
    src = f"{SUPA}{PHOTOS[key]}?width={w}&height={h}&resize=cover&quality=68"
    return (f'<img src="{src}" alt="" loading="lazy" decoding="async" '
            f'class="{cls}" style="{style}">')


def mock(inner, h, label=None, tone='', aw=1200):
    """Scale an `aw`-wide canvas into whatever column it lands in.

    `h` is a hint only — the page measures the natural height on load and
    writes it back, because a typed height that is too small clips the drawing
    and one that is too large leaves a white margin that reads as a gap."""
    cap = f'<div class="mock-cap">{label}</div>' if label else ''
    # NOTE: the width is NOT set inline. `--aw` on the wrapper drives it
    # through CSS, so `.mockwrap.phone .mock{width:390px}` can still win — an
    # inline width here silently renders the phone view at desktop width and
    # the canvas overflows with no error.
    # `aw{aw}` lets a decision author at a width other than 1200 and still get
    # the right shell: decision 40 is drawn at 1440 because the complaint is
    # that the map pushes the answers off a 1440x900 window, and a drawing
    # 240px narrower than the screen being complained about proves nothing.
    return (f'{cap}<div class="mockwrap {tone}" style="--mh:{h};--aw:{aw}">'
            f'<div class="mock aw{aw}">{inner}</div></div>')


def ring(n, selector):
    """A numbered ring that names an ELEMENT rather than coordinates.

    The page measures the element after layout and positions the ring from its
    own box, so a row that grows by a line does not leave the ring behind. A
    selector matching nothing stays hidden rather than pointing at the wrong
    thing — a ring 20px out is worse than no ring at all."""
    return f'<i class="ring" data-n="{n}" data-sel="{selector}"><b>{n}</b></i>'


# ---------------------------------------------------------------- chrome bits

#: `NAV_ITEMS` from src/components/PrimaryNav.tsx, in order. The sheet was
#: drawing "Tours · Destinations · Departing from · Deals · About", which is
#: neither the live nav nor the old site's.
#: Round two: `For Partners` shipped with decision 25 and the mocks were still
#: drawing the eight-item nav. Nine items is also what makes the row wrap at
#: 1200px, which is the defect named in register one — so a mockup missing it
#: was hiding the very thing it is evidence for.
NAV = ['Home', 'Destinations', 'Trip Styles', 'Departing From', 'Hot Deals',
       'Build Your Own', 'Journal', 'About', 'For Partners']

#: The number in the header on the deployed build. The sheet's first round
#: printed the old St George line.
PHONE = '800-970-5864'


def promostrip():
    """The 36px positioning strip above the header. It is not a promotion and
    never goes stale, which is why it sits above the deals ticker."""
    return ('<div class="m-strip"><div class="m-shell">'
            'Small groups of 7&ndash;13, departing Las Vegas, Phoenix and Salt '
            'Lake City. <b>See the current deals &rsaquo;</b>'
            '</div></div>')


def header(active='Home', strip=True):
    """The real chrome: navy-800, sticky, 73px tall at 1440."""
    items = ''.join(
        f'<span class="{"on" if t == active else ""}">{t}</span>' for t in NAV)
    return ((promostrip() if strip else '') +
            '<div class="m-hd"><div class="m-shell">'
            f'<img class="m-logo" src="{WORDMARK}" alt="Southwest Adventure Tours">'
            f'<div class="m-nav">{items}</div>'
            f'<div class="m-phone">{PHONE}</div>'
            '<div class="m-hd-cta">Find a Trip</div>'
            '</div></div>')


def backbar(text='&larr; all tours'):
    """44px, directly under the header — and NOT on the home page. `NO_BACK` in
    BackBar.tsx excludes home, so a home-page mockup that draws one is showing
    a bar that is not there."""
    return f'<div class="m-back"><div class="m-shell">{text}</div></div>'


def crumbs(*parts):
    inner = '<span class="sep">/</span>'.join(f'<span>{p}</span>' for p in parts)
    return f'<div class="m-crumbs"><div class="m-shell">{inner}</div></div>'


def ticker(compact=False, n=6):
    """The Hot Deals bar. Each item is tour · date · saving · promo code —
    the code is on the live bar and the sheet's invented version dropped it."""
    cls = 'm-tick' + (' compact' if compact else '')
    items = ''.join(
        f'<span>🔥 <b>{t}</b> &middot; {d} &middot; {o} &middot; '
        f'<code>{c}</code></span>' for t, d, o, c in DEALS[:n])
    return (f'<div class="{cls}"><div class="m-tick-track">{items}'
            '<span class="all">See all &rarr;</span></div></div>')


# ------------------------------------------------------------------ products

def tripcard(trip, w=350, hover=False, deal=None, compact=False):
    """A real TripCard: 16/10 frame, style badge left, duration badge right, a
    fixed two-line title, a reserved route line, three spec rows, the price and
    two actions. Its height is what makes the shelf tall — that is the point of
    decision 4, so it must not be drawn short."""
    photo, style, dur, title, route, place, activity, group, price = trip
    ph = round(w * 10 / 16)
    d = (f'<span class="m-deal">🔥 {deal}</span>') if deal else ''
    hv = ' hover' if hover else ''
    spec = (f'<span class="s">{place}</span>'
            f'<span class="s">Activity level <b>{activity}</b></span>'
            f'<span class="s">{group}</span>')
    if compact:
        spec = f'<span class="s">{place}</span>'
    return (f'<div class="m-card{hv}" style="width:{w}px">'
            f'<div class="m-card-ph" style="height:{ph}px">{img(photo, w * 2, ph * 2)}'
            f'<span class="m-badge">{style}</span>'
            f'<span class="m-dur">{dur}</span>{d}</div>'
            f'<div class="m-card-b">'
            f'<div class="m-card-t">{title}</div>'
            f'<div class="m-card-r">{route or "&nbsp;"}</div>'
            f'<div class="m-card-s">{spec}</div>'
            f'<div class="m-card-p"><b>{price}</b><span>from / person</span></div>'
            f'<div class="m-card-go"><span>View tour</span><span>Check dates</span></div>'
            f'</div></div>')


def cards(n=3, w=350, gap=24, hover_first=False, deal_on=None, compact=False):
    """The Bookable now shelf. Three across at 1440, not four — measured
    `grid-template-columns` on the deployed page."""
    inner = ''.join(
        tripcard(t, w=w, hover=(hover_first and i == 0),
                 deal=(deal_on if i == 1 else None), compact=compact)
        for i, t in enumerate(FEATURED[:n]))
    return f'<div class="m-row" style="gap:{gap}px">{inner}</div>'


def tile(photo, label, detail=None, w=263, chev=False):
    """A PhotoTile — the doors, the parks, the states, the journal. Four across
    at 1440 for the doors and the parks; three for the rest."""
    s = f'<div class="m-tile-sub">{detail}</div>' if detail else ''
    c = '<span class="m-chev">&rarr;</span>' if chev else ''
    return (f'<div class="m-tile" style="width:{w}px">'
            f'<div class="m-tile-ph">{img(photo, w * 2, 300)}</div>'
            f'<div class="m-tile-l">{label}{c}</div>{s}</div>')


def tilerow(items, w=263, gap=16):
    inner = ''.join(tile(p, l, d, w=w) for p, l, d in items)
    return f'<div class="m-row" style="gap:{gap}px">{inner}</div>'


def doors(w=263):
    return tilerow(DOORS, w=w)


def parkrow(n=4, w=263):
    return tilerow([(p, l, None) for p, l in PARKS[:n]], w=w)


# ------------------------------------------------------------------- sections

def h2(text, more=None, sub=None):
    m = f'<span class="m-more">{more}</span>' if more else ''
    s = f'<div class="m-sub">{sub}</div>' if sub else ''
    return f'<div class="m-h2row"><div class="m-h2">{text}</div>{m}</div>{s}'


def band(inner, cls=''):
    return f'<div class="m-band {cls}"><div class="m-shell">{inner}</div></div>'


def note(text, top=None, left=None):
    """A red call-out pinned onto a mockup to name the problem being shown."""
    pos = f' style="top:{top}px;left:{left}px"' if top is not None else ''
    return f'<div class="m-note"{pos}>{text}</div>'


def flag(text, top=None, left=None):
    """A green call-out naming the thing that changed in an option."""
    pos = f' style="top:{top}px;left:{left}px"' if top is not None else ''
    return f'<div class="m-flag"{pos}>{text}</div>'


def ruler(top, height, label):
    """A measured vertical extent drawn on the mockup, so a claim like 'the
    ticker is 2,167px down' is shown rather than asserted."""
    return (f'<div class="m-ruler" style="top:{top}px;height:{height}px">'
            f'<span>{label}</span></div>')


# =====================================================================
#  16 September round — the surfaces these decisions actually touch.
#
#  Geometry is the deployed staging build measured at a 1200px viewport,
#  not an estimate: gallery 672x380, title column 395, fact strip 1185 wide
#  at y=659, sticky subnav at y=847, navy change notice at y=961, booking
#  rail 360 wide beside it. The shell here is 1100 inside a 1200 canvas,
#  which is the same 691 + 48 + 360 split the page renders.
# =====================================================================

import usmap as _usmap   # noqa: E402  (baked national state outlines)


# ------------------------------------------------------------ tour page top

def tourhero(video_tile=False, season_tabs=False, thumbs=4):
    """The top of a tour page: 672x380 gallery with thumbnails inside its
    bottom edge, and the 395px title column beside it."""
    thumb_keys = ['capitol', 'mesa', 'hoodoo', 'zion2'][:thumbs]
    tiles = ''.join(
        f'<span class="m-th">{img(k, 152, 104)}</span>' for k in thumb_keys)
    if video_tile:
        tiles += ('<span class="m-th m-th-vid">' + img('zion3', 152, 104) +
                  '<i>&#9654;</i><em>Tour film</em></span>')
    tabs = ''
    if season_tabs:
        tabs = ('<div class="m-seasontabs">'
                '<span class="on">Summer</span><span>Autumn</span>'
                '<span>Winter</span><span>Spring</span></div>')
    return ('<div class="m-shell"><div class="m-tourtop">'
            '<div class="m-gal">' + img('zion', 1344, 760) +
            f'{tabs}<div class="m-thumbs">{tiles}</div></div>'
            '<div class="m-tt">'
            '<div class="m-badges"><span>Guided small group</span>'
            '<span>Easy</span><span>Zion National Park</span></div>'
            '<h1 class="m-h1">Mighty 5 Utah Tour From Las Vegas</h1>'
            '<div class="m-pricebox"><span class="l">FROM</span>'
            '<b>$1,999</b><span class="s">per person, double occupancy, 2026</span>'
            '<span class="s">Next departure Sep 21, 2026</span>'
            '<span class="m-cta">Check dates</span></div>'
            '</div></div></div>')


def factstrip(activity='Easy', extra=None):
    """The full-bleed strip under the hero: five facts and the positioning
    paragraph. `Activity level` lives here already, as a word."""
    facts = [('Duration:', '5 days'), ('Activity level:', activity),
             ('Group size:', 'Small group, 7&ndash;13'),
             ('Departs from:', 'Las Vegas'), ('From:', '$1,999')]
    fs = ''.join(f'<span class="f"><em>{k}</em> <b>{v}</b></span>'
                 for k, v in facts)
    ex = extra or ''
    return ('<div class="m-facts"><div class="m-shell">'
            f'<div class="m-factrow">{fs}</div>{ex}'
            '<p class="m-lede">One of our most popular tours, Southwest '
            'Adventure Tours will show you Utah&rsquo;s Mighty 5 national parks '
            'in 5 days. Those parks are Arches, Bryce Canyon, Canyonlands, '
            'Capitol Reef, and Zion.</p>'
            '</div></div>')


def subnav(items=None, active='Overview'):
    items = items or ['Overview', 'Day by day', 'Tour details', 'More photos',
                      'Reserve a place', 'Departures', 'Pricing']
    inner = ''.join(f'<span class="{"on" if i == active else ""}">{i}</span>'
                    for i in items)
    return f'<div class="m-subnav"><div class="m-shell">{inner}</div></div>'


def notice():
    """The change notice that shipped in round one of these notes."""
    return ('<div class="m-notice"><span class="l">PLEASE NOTE</span>'
            '<p>Itineraries, timings and included stops can change. Weather, '
            'road and park closures, fire, and your guide&rsquo;s judgement on '
            'the day all take precedence over the printed plan.</p></div>')


# --------------------------------------------------------------- booking rail

def rail(reviews=None, itin_email=True, activity_row='Easy',
         activity_more=False, rating=False):
    """The 360px sticky booking rail, as it ships: price, three dates, three
    spec rows, the CTA, the itinerary email, the phone number.

    `reviews` is a list of (stars, quote, name) drawn under the CTA — decision
    26. `itin_email=False` removes the row the room asked to delete."""
    more = ('<a class="m-r-more">What this means &rsaquo;</a>'
            if activity_more else '')
    rev = ''
    if reviews:
        cards = ''.join(
            f'<div class="m-rev"><span class="st">{"&#9733;" * s}</span>'
            f'<p>{q}</p><cite>{who}</cite></div>' for s, q, who in reviews)
        rev = ('<div class="m-r-rev"><span class="l">WHAT GUESTS SAY</span>'
               f'{cards}<a class="m-r-more">Read all 38 reviews &rsaquo;</a></div>')
    rate = ''
    if rating:
        rate = ('<a class="m-r-rate"><span class="st">&#9733;&#9733;&#9733;'
                '&#9733;&#9733;</span><b>4.9</b>'
                '<span class="n">38 reviews</span></a>')
    em = ('<div class="m-r-dl"><span class="l">DOWNLOAD THE ITINERARY</span>'
          '<span class="b">Email me the day-by-day</span></div>'
          if itin_email else '')
    return ('<aside class="m-rail">'
            '<div class="m-r-top"><span class="l">FROM</span><b>$1,999</b>'
            '<span class="s">per person, double occupancy, 2026</span></div>'
            '<div class="m-r-body">'
            '<span class="l">NEXT DEPARTURES</span>'
            '<ul class="m-r-dates"><li>Sep 21, 2026</li><li>Sep 28, 2026</li>'
            '<li>Oct 5, 2026</li></ul>'
            '<span class="s">61 more dates below</span>'
            f'<div class="m-r-spec"><span>Activity level</span><b>{activity_row}</b>{more}</div>'
            '<div class="m-r-spec"><span>Lodging</span><b>Hotels &amp; lodges</b></div>'
            '<div class="m-r-spec"><span>Group size</span><b>Small group, 7&ndash;13</b></div>'
            '<div class="m-cta wide">Check availability</div>'
            f'{rate}{rev}{em}'
            '<p class="m-r-q">Questions? 800-970-5864</p>'
            '</div></aside>')


def twocol(left, right='', gap=48, lw=692):
    return (f'<div class="m-shell"><div class="m-2col" '
            f'style="gap:{gap}px;grid-template-columns:{lw}px 360px">'
            f'<div class="m-2l">{left}</div>{right}</div></div>')


# ------------------------------------------------------- activity level marks

def meter(level, kind='bars'):
    """The activity graphic under argument in decision 20.

    Boots and stars are both ruled out in the room — boots because nobody reads
    them, stars because "people think it will be a rating, like how good the
    tour is". Everything here is therefore a shape that cannot be mistaken for
    a score: filled segments, a slope, or nothing at all."""
    n = {'on request': 0, 'Easy': 1, 'Moderate': 2, 'Strenuous': 3}[level]
    if kind == 'bars':
        segs = ''.join(f'<i class="{"on" if i < n else ""}"></i>'
                       for i in range(3))
        return (f'<span class="m-meter" data-n="{n}">{segs}'
                f'<em>{level}</em></span>')
    if kind == 'slope':
        return (f'<span class="m-slope" data-n="{n}">'
                f'<svg viewBox="0 0 34 16" width="34" height="16">'
                f'<path d="M1 15 L{[8,17,26,33][n]} {[15,10,6,2][n]} L33 15Z" '
                f'fill="currentColor" opacity=".9"/>'
                f'<path d="M1 15 L33 15" stroke="currentColor" stroke-width="1.4" '
                f'opacity=".35"/></svg><em>{level}</em></span>')
    return f'<span class="m-plain">Activity level {level}</span>'


def hovercard(level='Easy'):
    """The pop-up the room asked for — "a little call out ... where they mouse
    over it it says ... this tour includes some level ground or uneven ground
    walking, so a walker would not be appropriate"."""
    return ('<div class="m-hover"><b>Easy</b>'
            '<p>Short walks on made paths and boardwalks, under a mile at a '
            'time, with the vehicle never far away. Suitable with a walking '
            'stick; not suitable for a wheelchair or a walker.</p>'
            '<a>What the levels mean &rsaquo;</a></div>')


# --------------------------------------------------------- the national map

#: The states the trip builder offers today, read off /review/build/.
BUILDER_STATES = ['AK', 'AZ', 'CA', 'CO', 'HI', 'MT', 'NV', 'NM', 'OR', 'SD',
                  'TX', 'UT', 'WA', 'WY']


def mapdefs():
    """Every state outline, once, as reusable symbols.

    The baked paths are 46KB. A sheet that draws four maps would carry them
    four times, so each map is a row of `<use>` references and the geometry is
    emitted once into a hidden defs block at the top of the document."""
    paths = ''.join(f'<path id="s-{ab}" d="{d}"/>'
                    for ab, d in sorted(_usmap.PATHS.items()))
    return (f'<svg class="m-mapdefs" aria-hidden="true" width="0" height="0">'
            f'<defs>{paths}</defs></svg>')


def nationmap(selected=(), lit=(), labels=False, h=360, cls=''):
    """A real map of the United States — every state, Alaska and Hawaii inset.

    The room's instruction was "you should just get a picture of the United
    States where you could highlight different states", and the reason is in
    the same breath: "you can add every state because we do custom tours across
    the country". So this is the whole country, not the West."""
    uses = []
    for ab in sorted(_usmap.PATHS):
        c = 'sel' if ab in selected else ('lit' if ab in lit else '')
        uses.append(f'<use href="#s-{ab}" class="{c}"/>')
    text = ''
    if labels:
        text = ''.join(
            f'<text x="{x}" y="{y}">{ab}</text>'
            for ab, (x, y) in _usmap.ANCHORS.items() if ab in selected)
    return (f'<div class="m-map {cls}" style="height:{h}px">'
            f'<svg viewBox="{_usmap.VIEW}" preserveAspectRatio="xMidYMid meet">'
            f'{"".join(uses)}{text}</svg></div>')


# ------------------------------------------------------------- builder pieces

def chips(items, on=(), w=None):
    inner = ''.join(
        f'<span class="m-chip{" on" if i in on else ""}">{i}</span>'
        for i in items)
    return f'<div class="m-chips">{inner}</div>'


def step(n, title, hint, body, done=False):
    return (f'<div class="m-step{" done" if done else ""}">'
            f'<div class="m-step-h"><b>{n}.</b><span>{title}</span>'
            + (f'<em>{hint}</em>' if hint else '') +
            f'</div>{body}</div>')


def sofar(rows, cta='Send to a planner'):
    inner = ''.join(f'<div class="m-sf-r"><span>{k}</span><b>{v}</b></div>'
                    for k, v in rows)
    return ('<aside class="m-sofar"><span class="l">YOUR TRIP SO FAR</span>'
            f'{inner}<div class="m-cta wide">{cta}</div></aside>')


# ---------------------------------------------------------------- misc bits

REVIEWS = [
    (5, 'Our guide knew every turn-off worth taking. Five days and not one '
        'wasted hour.', 'Diane M. &middot; Mighty 5 from Las Vegas'),
    (5, 'Small group, big country. The van was never crowded and the hotels '
        'were a cut above.', 'Robert &amp; Kay P. &middot; August 2026'),
    (4, 'Bryce at sunrise was worth the early start. Bring layers &mdash; '
        'nobody warned us.', 'Steph L. &middot; July 2026'),
]


def seasonrow(active='Summer'):
    """The four-season strip for a tour that runs all year."""
    cells = []
    for name, key, line in [
            ('Spring', 'kanarra', 'Wildflowers, cool mornings, thin crowds.'),
            ('Summer', 'zion', 'Long days. Over 100&deg;F in the canyons.'),
            ('Autumn', 'hoodoo', 'The shoulder month locals book.'),
            ('Winter', 'ystwinter', 'Snow on the hoodoos. Fewer people.')]:
        cells.append(
            f'<div class="m-season{" on" if name == active else ""}">'
            f'<div class="m-season-ph">{img(key, 520, 340)}</div>'
            f'<b>{name}</b><p>{line}</p></div>')
    return f'<div class="m-seasons">{"".join(cells)}</div>'


def campaign(kind='now'):
    """The strip above the ticker — SWAT's positioning line today, and what a
    Black Friday takeover of it would look like."""
    if kind == 'now':
        return promostrip()
    if kind == 'take':
        return ('<div class="m-strip m-strip-camp"><div class="m-shell">'
                '<span class="m-camp-ic">&#127873;</span> '
                '<b>BLACK FRIDAY</b> &middot; $800 off every 2027 departure '
                'booked before 2 December &middot; code <code>BF800</code> '
                '<b class="u">See the deals &rsaquo;</b></div></div>')
    return ('<div class="m-strip m-strip-split"><div class="m-shell">'
            '<span class="camp"><span class="m-camp-ic">&#127873;</span> '
            '<b>BLACK FRIDAY</b> &middot; $800 off 2027 &middot; '
            '<code>BF800</code></span>'
            '<span class="pos">Small groups of 7&ndash;13, departing Las Vegas, '
            'Phoenix and Salt Lake City.</span></div></div>')
