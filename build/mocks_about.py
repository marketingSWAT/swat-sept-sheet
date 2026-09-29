"""Decision 74: the whole About page, drawn three ways at 1920.

Everything here is harvested off production on 29 September
(r-about/harvest/): the page's own sentences, its own photographs, the ten
profile bios. Nothing is invented. Every one-line fact on a person card was
checked against that person's profile page (guides.json).

The Now panel is a real full-page screenshot of production above the footer
(site/img/about-now-*.jpg), not a redrawing: the complaint is about the page
as a whole, and a redrawing of a 7,091px page would be a second opinion.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = open(os.path.join(HERE, '..', 'r-about', 'frag', 'chrome.html')).read()

SUPA = ('https://pyxnpjvtdlucaqqhhvin.supabase.co/storage/v1/object/public/'
        'media/derived/')
FILM = 'https://i.ytimg.com/vi/y6-BldlQHlI/maxresdefault.jpg'

P = {
    'canyonlands': 'photos/Canyonlands_Group_456d26f8-8539-46c5-b94f-8a2a610ab7a0.avif',
    'imperial': 'photos/Group_Imperial_Point_780d7e22-85cf-444c-8d40-704bb37971cd.avif',
    'team': 'photos/Team_Photo_33c0786b-81b8-441b-bb34-bfc1e42dd91b.avif',
    'zion': 'photos/Zion_Checkerboard_Mesa_Group_Photo_ded30d2e-ad40-4010-ae62-e4b176a7a62a.avif',
    'alaska': 'photos/Alaska_Group_Exit_Glacier_2200_3357dba1-5e0b-4cab-95fc-97bfc2554f79.avif',
    'arches': 'photos/Arches_NP_Balanced_Rock_Group_91c0d0ee-f60b-4204-af2f-1bacbbe06bc3.avif',
    'hikers': 'photos/IMG_9164_fa936444-36c7-4eeb-afc3-e5b41d130ad4.avif',
    'yosemite': 'photos/Yosemite_Group_Photo_f7b06687-bf64-4bcc-9084-451c41ddf4c8.avif',
    'van': 'photos/Van2021b2200px_42eebb97-0251-44d1-aee2-8c62e17c425f.avif',
    'atta': 'photos/logo_web_ATTA_39bcd1f6-54e7-4df4-9e45-f453613292c3.avif',
    'aba': 'photos/logo_web_AmericanBusAssociation_06ab7452-b0d3-4749-9579-2277de4c073e.avif',
    'iatan': 'photos/logo_web_iatan_a047767a-ec45-4a4b-afb7-a31cd0196ca1.avif',
    'nta': 'photos/logo_web_NTA_09244ba7-9d9d-4ad9-99b5-2e644c0ec974.avif',
}

CAPS = {
    'zion': 'Zion, Checkerboard Mesa', 'alaska': 'Alaska, Exit Glacier',
    'arches': 'Arches, Balanced Rock', 'hikers': 'On the trail',
    'yosemite': 'Yosemite', 'van': 'Zion, with the van',
}


def src(key, w=1200):
    return f'{SUPA}w{w}/{P[key]}'


def im(key, w=1200, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<img{c} src="{src(key, w)}" alt="">'


#: The ten people, in the page's own order. `role` is what they do (three of
#: the ten do not guide). `fact` is lifted from their own profile page.
PEOPLE = [
    dict(slug='ann-evans', name='Ann Evans', first='Ann', role='Guide',
         img='photos/AnnEvans_e013343d-eb52-4bca-ba05-082654d77653.avif',
         fact='25 years with Utah&rsquo;s Department of Natural Resources, most of '
              'them as a State Parks ranger and naturalist. An EMT for 12 years.',
         short='25 years a Utah State Parks ranger and naturalist',
         more='I raised my family recreating in Utah&rsquo;s national parks and love '
              'the opportunity to share them with the guests of Southwest Adventure '
              'Tours.',
         quote='I guarantee you&rsquo;ll leave a changed person!'),
    dict(slug='chris-vander-wilt', name='Chris Vander Wilt', first='Chris', role='Guide',
         img='photos/chris_vander_wilt_opt_516db26a-0e54-4f5f-9a61-e653a6e4af77.avif',
         fact='President of the Utah Tour Guide Association. Guiding custom tours '
              'across the West since 2011.',
         short='President of the Utah Tour Guide Association'),
    dict(slug='dennis-bailey', name='Dennis Bailey', first='Dennis', role='Guide',
         img='photos/Dennis_13892f9a-95b9-4878-b3d8-ddb1e7dcf2d4.avif',
         fact='Grew up in Moab with Arches and Canyonlands as his backyard. A '
              'professional land surveyor.',
         short='Grew up in Moab, with Arches as his backyard',
         quote='Go along for a ride, share in the past, go back in time.'),
    dict(slug='kirk-douglass', name='Kirk Douglass', first='Kirk', role='Guide',
         img='photos/kirt_douglass_b6e98676-0e7b-402e-8381-4abd3ba27cd5.avif',
         fact='A peak bagger: Mount Whitney, Mount Elbert, Wheeler Peak and the '
              'Grand Teton.',
         short='Has climbed Mount Whitney and the Grand Teton'),
    dict(slug='phil-douglass', name='Phil Douglass', first='Phil', role='Guide',
         img='photos/phil_douglas_71842697-f115-494c-a6af-8d7aa2f90b33.avif',
         fact='32 years with the Utah Division of Wildlife Resources, known as '
              '&ldquo;Utah&rsquo;s Wildlife Ambassador.&rdquo; Kirk&rsquo;s '
              'younger brother, and a cowboy poet.',
         short='&ldquo;Utah&rsquo;s Wildlife Ambassador,&rdquo; 32 years in wildlife',
         quote='Gifts from nature and music are companions for life!'),
    dict(slug='robin-luse', name='Robin Luse', first='Robin', role='Guide',
         img='photos/robin_luse_zion_f345414b-616f-4491-a5f1-ca4f725a2bf5.avif',
         fact='Left a career in radio in 1999 to guide. Based in Albuquerque, with '
              'us since 2014.',
         short='Left radio in 1999 to guide the Southwest'),
    dict(slug='shybree-richens', name='Shybree Richens', first='Shybree', role='Guide',
         img='photos/Shybree_Richins_298399eb-cac6-4cdb-b034-9ee14ce5225b.avif',
         fact='Grew up in St. George, near Zion. She loves photography, so you will '
              'get a good picture.',
         short='Grew up near Zion, and takes a good picture', pos='18% 50%'),
    dict(slug='jason-murray', name='Jason Murray', first='Jason', role='Owner',
         img='photos/Jason_Murray_5e542e87-9bdb-499c-bf8f-291242bc308a.avif',
         fact='A Utah native. One of his favorite trips: Havasupai Falls and the '
              'Colorado River in the Grand Canyon.',
         short='Utah native. A favorite trip: Havasupai Falls'),
    dict(slug='julie-burton-ray', name='Julie Burton-Ray', first='Julie',
         role='Operations Manager',
         img='photos/Julie_Burton_Ray_Photo_5afb99f1-0974-41d7-a51a-4611d5718bac.avif',
         fact='In the tour business since 1983, when she started as a Salt Lake City '
              'tour guide.',
         short='In the tour business since 1983'),
    dict(slug='shawn-horman', name='Shawn Horman', first='Shawn', role='Tour design',
         img='photos/Shawn_3_a2aff3c6-efe0-42e3-9393-434aad5496c9.avif',
         fact='30 years designing custom tours, for groups of a few people to a few '
              'hundred.',
         short='30 years designing custom tours'),
]
GUIDES = [p for p in PEOPLE if p['role'] == 'Guide']
OFFICE = [p for p in PEOPLE if p['role'] != 'Guide']


def face(p, w=640):
    st = f' style="object-position:{p["pos"]}"' if p.get('pos') else ''
    return f'<img src="{SUPA}w{w}/{p["img"]}" alt=""{st}>'


# ------------------------------------------------------------ SWAT's own words
HERO_LINE = ('Southwest Adventure Tours provides local, experienced guides who work '
             'hard to provide travelers with the best experience in the Southwest.')
INTRO = ('At Southwest Adventure Tours it would be our pleasure to tour with you! We '
         'are travel enthusiasts and we would love nothing more than to '
         '&ldquo;Explore, Experience, Enrich&rdquo; with each and every one of our '
         'guests. When you are on one of our tours, adventure awaits!')
FILM_LINE = ('To see one of our tour guide professionals in action on one of our '
             'tours, watch this video. It shows what the folks at Southwest '
             'Adventure Tours are all about.')
MISSION = ('Southwest Adventure Tours&rsquo; highest mission is to provide our guests '
           'the opportunity to build lasting memories through creating exceptional '
           'experiences that will touch their heart, mind, and soul.')
GROUPS = ('Groups of seven to thirteen, and a guide who has been there before. Every '
          'photograph here is one of ours, on one of our trips.')
TEAM = ('We are so fortunate to have a diverse and talented team who provide endless '
        'possibilities for your next adventure!')
ORIGIN = ('Southwest Adventure Tours was created by a combination of our deep love for '
          'experiencing all the wonders that surround us and a passion for sharing '
          'these wonders with others.')
CAREERS = ('Love to travel and want to share it with others? You may be a great fit '
           'for the growing SWAT team.')
VERIFY = 'Membership in each of these is verifiable independently of anything said on this site.'


# ------------------------------------------------------------------ shared bits
def page(body):
    return f'<div class="w9">{CHROME}{body}</div>'


def crumbs():
    return '<div class="sh ab-crumbs">Home <span>/</span> <b>About</b></div>'


def film(cls=''):
    return (f'<div class="ab-film {cls}"><img src="{FILM}" alt="">'
            '<span class="ab-play"><i></i></span>'
            '<span class="ab-film-cap">Watch: Southwest Adventure Tours'
            ' <em>8 min</em></span></div>')


def btns(extra=''):
    return ('<div class="ab-btns"><span class="ab-btn">Find a Trip</span>'
            '<span class="ab-btn ghost">Call 800-970-5864</span>' + extra + '</div>')


def logos(cls=''):
    return (f'<div class="ab-logos {cls}">' +
            ''.join(f'<img src="{src(k, 384)}" alt="">' for k in ('atta', 'aba', 'iatan', 'nta'))
            + '</div>')


def google():
    return ('<div class="ab-g"><b>4.8</b><span class="ab-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            '<span>from 255 Google reviews</span></div>')


def closer(title='Ready to see it for yourself?', careers=True):
    c = ('<p class="ab-work">Want to guide with us? <u>Careers and how we work &rsaquo;</u></p>'
         if careers else '')
    return (f'<section class="ab-close"><div class="sh"><div class="in">'
            f'<h2>{title}</h2>'
            '<p>Small groups of 7&ndash;13, departing Las Vegas, Phoenix and Salt '
            'Lake City.</p>'
            f'{btns()}</div>{c}</div></section>')


def card(p, cls='', quote=False, more=False):
    q = (f'<p class="ab-q">&ldquo;{p["quote"]}&rdquo;</p>'
         if quote and p.get('quote') else '')
    if more and p.get('more'):
        q = f'<p>{p["more"]}</p>' + q
    return (f'<a class="ab-card {cls}"><div class="ph">{face(p)}</div>'
            f'<div class="tx"><span class="rl">{p["role"]}</span>'
            f'<h4>{p["name"]}</h4><p>{p["fact"]}</p>{q}'
            f'<span class="lk">Read {p["first"]}&rsquo;s story &rsaquo;</span></div></a>')


# ============================================================ A: as it is now
def now():
    return ('<div class="ab-now"><img class="d" src="img/about-now-1920.jpg" alt="">'
            '<img class="p" src="img/about-now-390.jpg" alt=""></div>')


# ============================================================ B: side by side
def opt_story():
    rows = (
        # 1. The opening: words beside the photograph, not under it.
        '<section class="ab-open"><div class="sh ab-split">'
        '<div class="tx"><span class="ab-kick">About us</span>'
        '<h1>Local guides who have been there before</h1>'
        f'<p class="lead">{HERO_LINE}</p><p>{INTRO}</p>{btns()}</div>'
        f'<div class="ph">{im("canyonlands", 2048)}</div></div></section>'

        # 2. The film, beside the words that promise it.
        '<section class="ab-row"><div class="sh ab-split flip">'
        f'<div class="ph">{film()}</div>'
        '<div class="tx"><span class="ab-kick">See a trip</span>'
        '<h2>Watch a guide at work</h2>'
        f'<p>{FILM_LINE}</p>'
        f'<h3>Our mission</h3><p>{MISSION}</p></div></div></section>'

        # 3. The groups, words beside a mosaic.
        '<section class="ab-row sand"><div class="sh ab-split">'
        '<div class="tx"><span class="ab-kick">Explore, Experience, Enrich</span>'
        '<h2>Small groups, real trips</h2>'
        f'<p>{GROUPS}</p>{google()}</div>'
        '<div class="ab-mos">' +
        ''.join(f'<figure>{im(k, 640)}<figcaption>{CAPS[k]}</figcaption></figure>'
                for k in ('zion', 'arches', 'alaska', 'yosemite')) +
        '</div></div></section>'

        # 4. The people, with words on every card.
        '<section class="ab-row"><div class="sh">'
        '<div class="ab-peoplehd"><div><span class="ab-kick">Our team</span>'
        '<h2>The people who guide your trip</h2></div>'
        f'<p>{TEAM}</p></div>'
        '<div class="ab-g4">' + ''.join(card(p, quote=True) for p in GUIDES) +
        '<div class="ab-office cell"><span class="ab-kick">Behind the trips</span>' +
        ''.join(f'<a class="ab-mini">{face(p, 384)}<span><b>{p["name"]}</b>'
                f'{p["role"]}. {p["short"]}.</span></a>' for p in OFFICE) +
        '</div></div></div></section>'

        # 5. Proof, one row.
        '<section class="ab-row tight"><div class="sh ab-proof">'
        '<div><span class="ab-kick">Accredited by</span>'
        f'<p>{VERIFY}</p></div>{logos()}</div></section>'
    )
    return page(crumbs() + rows + closer())


# ======================================================== C: people come first
def opt_people():
    body = (
        # 1. The first screen is the guides.
        '<section class="ab-pf"><div class="sh">'
        '<div class="ab-pfhd"><div><span class="ab-kick">About us</span>'
        '<h1>Meet the people you will travel with</h1></div>'
        f'<div><p>{HERO_LINE}</p>{btns()}</div></div>'
        '<div class="ab-g7">' + ''.join(card(p, 'big' if i < 3 else '', quote=i == 0, more=i == 0)
                                          for i, p in enumerate(GUIDES)) +
        '</div></div></section>'

        # 2. The company, compact, around the film.
        '<section class="ab-row sand"><div class="sh ab-co">'
        '<div class="tx"><span class="ab-kick">Who we are</span>'
        '<h2>A Utah company that loves to share the West</h2>'
        f'<p>{ORIGIN}</p><p>{INTRO}</p>'
        f'<blockquote>{MISSION}</blockquote></div>'
        f'<div class="fl">{film()}'
        '<div class="ab-office stack"><span class="ab-kick">Running the trips</span>' +
        ''.join(f'<a class="ab-mini">{face(p, 384)}<span><b>{p["name"]}</b>'
                f'{p["role"]}. {p["short"]}.</span></a>' for p in OFFICE) +
        '</div></div></div></section>'

        # 3. Their photos, one strip.
        '<section class="ab-row tight"><div class="sh">'
        f'<div class="ab-striphd"><h2>On the road with our groups</h2><p>{GROUPS}</p></div>'
        '<div class="ab-strip6">' +
        ''.join(f'<figure>{im(k, 640)}<figcaption>{CAPS[k]}</figcaption></figure>'
                for k in ('zion', 'alaska', 'arches', 'hikers', 'yosemite', 'van')) +
        '</div>'
        f'<div class="ab-proof line">{google()}<span class="ab-kick">Accredited by</span>'
        f'{logos()}</div></div></section>'

        # 4. Careers, with the handbook folded shut.
        '<section class="ab-row tight"><div class="sh ab-careers">'
        '<div><h3>Work with us</h3>'
        f'<p>{CAREERS} <u>See current openings &rsaquo;</u></p></div>'
        '<div class="ab-fold"><span>How we work: our three steps of service, '
        'service values and employee promise</span><b>+</b></div></div></section>'
    )
    return page(crumbs() + body + closer('Travel with one of them', careers=False))


# ==================================================== D: one screen, then done
def opt_first():
    body = (
        # 1. Everything that matters in the first 920px.
        '<section class="ab-one"><div class="sh ab-onegrid">'
        '<div class="tx"><span class="ab-kick">About us</span>'
        '<h1>Southwest Adventure Tours</h1>'
        f'<p class="lead">{HERO_LINE}</p><p>{INTRO}</p>'
        f'{btns()}{film("small")}</div>'
        '<div class="ab-quad">'
        f'<figure class="a">{im("canyonlands", 1200)}</figure>'
        f'<figure class="b">{im("imperial", 1200)}</figure>'
        f'<figure class="c">{im("zion", 640)}</figure>'
        f'<figure class="d">{im("alaska", 640)}</figure>'
        '</div></div></section>'

        # 2. Four plain proof points.
        '<section class="ab-facts"><div class="sh ab-f4">'
        '<div><b>7&ndash;13</b><span>people in a group, and a guide who has been there before</span></div>'
        '<div><b>Local</b><span>guides who live in the Southwest: a park ranger, a '
        'land surveyor, 32 years in wildlife</span></div>'
        f'<div>{google()}</div>'
        f'<div><span class="ab-kick">Accredited by</span>{logos("sm")}</div>'
        '</div></section>'

        # 3. The ten, in one band.
        '<section class="ab-row"><div class="sh">'
        '<div class="ab-peoplehd"><div><span class="ab-kick">Our team</span>'
        '<h2>Who you will travel with</h2></div>'
        f'<p>{TEAM} Tap a face to read their story.</p></div>'
        '<div class="ab-row10">' +
        ''.join(f'<a class="ab-f">{face(p, 384)}<b>{p["name"]}</b>'
                f'<span class="rl">{p["role"]}</span><span>{p["short"]}</span></a>'
                for p in GUIDES + OFFICE) +
        '</div></div></section>'

        # 4. The mission beside the team photo, as the last word.
        '<section class="ab-row sand"><div class="sh ab-split">'
        f'<div class="ph">{im("team", 1200, "team")}</div>'
        '<div class="tx"><span class="ab-kick">Our mission</span>'
        f'<blockquote>{MISSION}</blockquote>'
        '<p class="ab-motto">Explore, Experience, Enrich</p></div></div></section>'
    )
    return page(crumbs() + body + closer())
