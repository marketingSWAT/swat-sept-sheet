"""Mockup primitives for round nine: the empty right-hand side.

Crow, 29 September, with a screenshot of the Arches and Canyonlands page on
his desktop: "there is just a lot of wasted white space on the right side when
on my computer ... review all the different tabs to see if this issue pops up
anywhere else".

Drawn at **1920** wide, not the usual 1440. His screenshot is 1,851 CSS px
across, and the gap only gets worse as the window grows: a round about wasted
width that shrinks its drawings to a laptop has argued itself out of its case.

Measured off the **deployed production build** at 1920x1080 and 1440x900 on
29 September 2026 (every sitemap page, 214 of them; harvest in r9/harvest/,
`whitespace.mjs`). The counter walks each page in 20px bands and records how
far the rightmost text, photo or filled box in that band stops short of the
content column's right edge (x=1768 at 1920). A band counts as wasted when
more than 35% of the 1,616px column is blank beside it.

  Destination pages (38)   2,081px of the average 4,821px page (43%) has an
                           empty right side. Words are 680px in a 1,616px
                           column: 936px of nothing beside them. Hawaii runs
                           4,000px like that.
  Departing From (10)      68%. Trips are grouped by length and each group
                           starts a new row, so Bryce's three trips sit one
                           per row, 1,230px of empty beside them.
  Journal (44) + guides (13)  73% / 64%. The words sit left-of-centre in a
                           912px box, 736px of blank to their right.
  Hot Deals                48%. One 798px card, 818px of nothing beside it.
  Tour pages (74)          26%, but the booking panel is sticky and follows
                           the reader down that side, so on screen it is
                           mostly filled. The exception is the packing list
                           on 7 tours (register one).
  Fine                     Home 3%, tour finder 8%, trip-style pages 25% (the
                           words at the bottom, same component as the
                           destinations), map 0%, Build Your Own 8%.
"""

import json
import os

import mocks as m

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, '..', 'r9', 'data.json')))

AW = 1920
NAV = ['Home', 'Destinations', 'Trip Styles', 'Departing From', 'Hot Deals',
       'Build Your Own', 'Journal', 'About', 'Group Travel']


# ------------------------------------------------------------------- chrome
def header(active):
    items = ''.join(f'<span class="{"on" if t == active else ""}">{t}</span>' for t in NAV)
    return ('<div class="w9-hd"><div class="sh">'
            f'<img src="{m.WORDMARK}" alt="">'
            f'<div class="w9-nav">{items}<span class="ph">800-970-5864</span>'
            '<span class="cta">Find a Trip</span></div></div></div>')


def top(active):
    """Page top as it loads: 36px strip, 73px header, 50px deals ticker."""
    return ('<div class="w9-strip">Small groups of 7&ndash;13, departing Las Vegas, '
            'Phoenix and Salt Lake City. <b>See the current deals &rsaquo;</b></div>'
            + header(active) +
            '<div class="w9-tick"><span class="hot">HOT DEALS</span>'
            '<span><b>Canyons of the Escalante</b> October 25 <i>$500 off per person</i> '
            '<code>CANYONS500</code></span>'
            '<span><b>Canyons of the Escalante</b> October 25 <i>$500 off per person</i> '
            '<code>CANYONS500</code></span></div>')


def crumbs(*parts):
    inner = ' <span>/</span> '.join(parts[:-1]) + f' <span>/</span> <b>{parts[-1]}</b>'
    return f'<div class="w9-crumbs">{inner}</div>'


def footer():
    cols = ''.join(f'<div><b>{h}</b>{"<br>".join(xs)}</div>' for h, xs in [
        ('Trip styles', ['Backpacking', 'Guided small group', 'Day tour', 'Self-drive']),
        ('Plan', ['Find a trip', 'Departing from', 'The trip map', 'Guides &amp; resources']),
        ('Company', ['About us', 'The Archive', 'Reviews', 'Contact'])])
    return (f'<div class="w9-foot"><div class="sh"><div><img src="{m.WORDMARK}" alt=""><br><br>'
            f'800-970-5864</div>{cols}</div></div>')


# ------------------------------------------------------------------ products
def card(c):
    deal = f'<span class="dl">&#128293; {c["deal"]}</span>' if c.get('deal') else ''
    unit = f'<span>{c["unit"]}</span>' if c['unit'] else ''
    cp = '<em>Custom-priced</em>' if c['custom'] else ''
    rt = f'<div class="rt">{c["route"]}</div>' if c['route'] else ''
    return (f'<article class="w9-card"><div class="ph"><img src="{c["img"]}" alt="">'
            f'<span class="st">{c["style"]}</span><span class="du">{c["dur"]}</span>{deal}</div>'
            f'<div class="bd"><div class="tt">{c["title"]}</div>{rt}'
            f'<ul><li>{c["places"]}</li><li>{c["activity"]}</li><li>{c["group"]}</li></ul>'
            f'<div class="pr"><b>{c["price"]}</b>{unit}{cp}</div>'
            f'<div class="go"><span>View tour</span><span>{c["action"]}</span></div></div></article>')


def grid(cards, cls=''):
    return f'<div class="w9-grid {cls}">{"".join(card(c) for c in cards)}</div>'


def tile(t, kick=None):
    k = f'<span class="k">{kick}</span>' if kick else ''
    return f'<a class="w9-tile"><img src="{t["img"]}" alt=""><p>{k}{t["title"]}</p></a>'


def words(paras, extra=''):
    return f'<div class="w9-words">{"".join(f"<p>{p}</p>" for p in paras)}{extra}</div>'


# ======================================================== 68 · the opening
A = D['arches']
ARCHES = 'Arches and Canyonlands National Parks'


def dest_window(body):
    """Crow's screenshot: scrolled past the hero, sticky header, 60px of the
    photograph still showing, then the trail, the search bar and the words."""
    return ('<div class="w9 w9-win">' + header('Destinations') +
            f'<div class="w9-sliver"><img src="{A["hero"]}" alt=""></div>'
            '<div class="sh">' + crumbs('Home', 'Destinations', ARCHES) +
            '<div class="w9-find">'
            '<label>Where<span>Arches National Park</span></label>'
            '<label>When<span>Any time of year</span></label>'
            '<label>How long<span>Any length</span></label>'
            '<label>How you travel<span>Any style</span></label>'
            '<span class="go">Show 11 trips</span></div>' + body + '</div></div>')


HIKES = f'<h2>Hikes in Arches</h2><p>{A["hikes_p"]}</p>'


def trips_sec(n=11):
    return (f'<section class="w9-sec"><h2 class="w9-h2">Trips that go here</h2>'
            f'{grid(A["cards"][:n])}</section>')


def dest_now():
    return dest_window(f'<section class="w9-intro">{words(A["prose"], HIKES)}</section>'
                       + trips_sec(8))


def panel():
    chips = ''.join(f'<span>{c}</span>' for c in A['departing'])
    return ('<aside class="w9-panel"><div class="ph">'
            f'<img src="{A["gallery"][3]}" alt=""></div><div class="in">'
            '<div class="n">11 trips go here</div>'
            '<div class="big">From $1,190<small>per person</small></div>'
            '<span class="btn">Show the 11 trips</span>'
            f'<div class="row"><div class="lab">Departing from</div><div class="w9-chips">{chips}</div></div>'
            '<div class="row"><div class="lab">Plan your walking</div>'
            f'<div class="lnk"><img src="{A["hikes_card"]["img"]}" alt="">Hikes in Arches National Park</div></div>'
            '</div></aside>')


def dest_panel():
    return dest_window('<section class="w9-intro"><div class="w9-two">'
                       f'{words(A["prose"], HIKES)}{panel()}</div></section>' + trips_sec(8))


def mosaic():
    g = A['gallery']
    return ('<div class="w9-mosaic">'
            f'<img class="lead" src="{g[0]}" alt=""><img class="sm" src="{g[3]}" alt="">'
            f'<img class="sm" src="{g[5]}" alt=""></div>')


def dest_photos():
    return dest_window('<section class="w9-intro pair">'
                       f'{words(A["prose"], HIKES)}{mosaic()}</section>' + trips_sec(8))


def dest_trips_first():
    return dest_window('<section class="w9-sec" style="border:0;padding-top:40px">'
                       f'<h2 class="w9-h2">Trips that go here</h2>{grid(A["cards"])}</section>'
                       '<section class="w9-sec w9-intro pair">'
                       f'{words(A["prose"], HIKES)}{mosaic()}</section>')


# ===================================================== 69 · the bottom half
def gallery(kind):
    g = A['gallery']
    if kind == 'now':
        cells = ([f'<div class="f lead"><img src="{g[0]}" alt=""></div>'] +
                 [f'<div class="f"><img src="{x}" alt=""></div>' for x in g[1:]])
        return f'<div class="w9-gal">{"".join(cells)}</div>'
    if kind == 'fill':
        # 7 photos in 4 columns: lead 2x2 + four = two full rows; the last two
        # each take half the row instead of leaving it half empty.
        cells = ([f'<div class="f lead"><img src="{g[0]}" alt=""></div>'] +
                 [f'<div class="f"><img src="{x}" alt=""></div>' for x in g[1:5]] +
                 [f'<div class="f wide"><img src="{x}" alt=""></div>' for x in g[5:7]])
        return f'<div class="w9-gal">{"".join(cells)}</div>'
    cells = ''.join(f'<div class="f"><img src="{x}" alt=""></div>' for x in g[:3])
    return (f'<div class="w9-strip4">{cells}<div class="f"><img src="{g[3]}" alt="">'
            f'<b>See all {len(g)} photos</b></div></div>')


def lower(kind):
    chips = ''.join(f'<span>{c}</span>' for c in A['departing'])
    hike = tile(A['hikes_card'])
    jr = ''.join(tile(j) for j in A['journal'])
    head = (f'<div class="w9 sh" style="padding-bottom:48px">'
            f'<section class="w9-sec" style="padding:40px 0"><p class="w9-kick">Departing from</p>'
            f'<div class="w9-chips">{chips}</div></section>'
            f'<section class="w9-sec"><p class="w9-kick">{ARCHES} in photographs</p>')
    if kind == 'now':
        return (head + gallery('now') + '</section>'
                '<section class="w9-sec hk"><h2 class="w9-h2">Plan your walking</h2>'
                f'<div class="w9-tiles c3">{hike}</div></section>'
                '<section class="w9-sec jr"><h2 class="w9-h2">From the journal</h2>'
                f'<div class="w9-tiles c3">{jr}</div></section></div>' + footer())
    keep = ('<section class="w9-sec"><h2 class="w9-h2">Keep exploring</h2>'
            f'<div class="w9-tiles c3">{tile(A["hikes_card"], "Plan your walking")}'
            + ''.join(tile(j, 'From the journal') for j in A['journal']) + '</div></section>')
    return head + gallery(kind) + '</section>' + keep + '</div>' + footer()


# ================================================== 70 · departing from Bryce
B = D['bryce']


def bryce_top():
    return ('<div class="w9">' + top('Departing From') + '<div class="sh">' +
            crumbs('Home', 'Departing from', 'Bryce') +
            '<h1 class="w9-dh1">Trips leaving Bryce</h1>'
            f'<p class="w9-dlede">{B["intro"][0]}</p><p class="w9-dcount">{B["intro"][1]}</p>')


def bryce_words(cls=''):
    return (f'<section class="w9-sec" style="margin-top:48px"><h2 class="w9-h2">Starting from Bryce</h2>'
            f'<div style="margin-top:20px">{words(B["words"])}</div></section>')


WHERE = ['Grand Canyon National Park Tours', 'Explore Arizona', 'Explore Colorado',
         'Bryce Canyon National Park', 'Arches and Canyonlands National Parks', 'Explore Utah',
         'Zion National Park Tours', 'Monument Valley Navajo Tribal Park']


def bryce_where():
    return ('<section class="w9-sec" style="padding:40px 0 0"><p class="w9-kick">Where these trips go</p>'
            f'<div class="w9-chips">{"".join(f"<span>{w}</span>" for w in WHERE)}</div></section>')


def bryce_now():
    groups = ''.join(f'<div class="w9-grp g{i}"><div class="w9-lab">{g.upper()}</div>{grid([c])}</div>'
                     for i, (g, c) in enumerate(zip(B['groups'], B['cards']), 1))
    return bryce_top() + groups + bryce_words() + bryce_where() + '</div>' + footer() + '</div>'


def bryce_one_row():
    return (bryce_top() + f'<div style="margin-top:40px">{grid(B["cards"])}</div>' +
            bryce_words() + bryce_where() + '</div>' + footer() + '</div>')


def labelled(cards, groups, cols=''):
    cells = ''
    last = None
    for g, c in zip(groups, cards):
        lab = (f'<div class="w9-lab run">{g.upper()}</div>' if g != last
               else '<div class="w9-lab cont">&nbsp;</div>')
        last = g
        cells += f'<div class="w9-cell">{lab}{card(c)}</div>'
    return f'<div class="w9-grid {cols}">{cells}</div>'


def bryce_labels():
    return (bryce_top() + f'<div style="margin-top:40px">{labelled(B["cards"], B["groups"])}</div>' +
            bryce_words() + bryce_where() + '</div>' + footer() + '</div>')


def bryce_side():
    return (bryce_top() + '<div class="w9-side"><div><h2 class="w9-h2">Starting from Bryce</h2>'
            f'<div style="margin-top:16px">{words(B["words"])}</div></div>'
            f'{labelled(B["cards"], B["groups"], "c3")}</div>' +
            bryce_where() + '</div>' + footer() + '</div>')


# ========================================================= 71 · a journal story
J = D['journal']
JT = 'Exploring the Last Frontier: My Alaskan Adventure'


def j_window(body):
    return ('<div class="w9 w9-win">' + header('Journal') + '<div class="sh">' + body + '</div></div>')


def j_crumbs():
    return crumbs('Home', 'Journal', JT)


def j_fig():
    return (f'<figure class="w9-fig"><img src="{J["img1"]}" alt="">'
            '<figcaption>Morris Thompson Cultural &amp; Visitors Center Fairbanks AK</figcaption></figure>')


def j_now():
    return j_window('<div class="w9-art">' + j_crumbs() + f'<div class="w9-meta">{J["meta"]}</div>'
                    + words(J['paras'][:9]) + '</div>')


def j_centre():
    return j_window('<div class="w9-art centre">' + j_crumbs() + f'<div class="w9-meta">{J["meta"]}</div>'
                    + words(J['paras'][:9]) + '</div>')


def j_rail():
    go = ''.join(f'<div class="w9-mini"><img src="{c["img"]}" alt=""><div><b>{c["title"]}</b>'
                 f'<span>{c["dur"]} &middot; {c["style"].title()}</span>'
                 f'<span><em>{c["price"]}</em> from / person<u>Check dates</u></span></div></div>'
                 for c in J['go'])
    keep = ''.join(f'<div class="w9-keep">{k["title"]}</div>' for k in J['keep'])
    return (f'<aside><div class="w9-rail"><h3>Go there with us</h3>{go}</div>'
            f'<div class="w9-rail"><h3>Keep reading</h3>{keep}</div></aside>')


def j_story():
    return j_window(j_crumbs() + '<div class="w9-story"><div>'
                    f'<div class="w9-meta">{J["meta"]}</div>' + words(J['paras'][:9]) +
                    f'</div>{j_rail()}</div>')


def j_wide():
    return j_window('<div class="w9-art centre">' + j_crumbs() + f'<div class="w9-meta">{J["meta"]}</div>'
                    + words(J['paras'][:5]) + '</div>'
                    f'<div class="w9-bleed"><img src="{J["img1"]}" alt=""></div>'
                    '<div class="w9-art centre">' + words(J['paras'][5:8]) + '</div>')


# =============================================================== 72 · deals
DEAL_LINE = ('<div class="ln"><b>October 25</b><i>$500 off per person</i>'
             '<code>CODE CANYONS500</code></div>')


def deals_window(body):
    return ('<div class="w9 w9-win">' + header('Hot Deals') + '<div class="sh">' +
            crumbs('Home', 'Hot deals') +
            f'<div class="w9-words" style="max-width:748px;margin-top:40px"><p>{D["deals"]["intro"]}</p></div>'
            + body + '</div></div>')


def dealcard(wide=False):
    facts = ('<div class="w9-facts"><span><b>7 days</b></span><span>Small group, 7&ndash;13</span>'
             '<span>Bryce &rarr; Bryce Canyon National Park</span></div>') if wide else ''
    return (f'<div class="w9-dealcard{" wide" if wide else ""}"><div class="ph">'
            f'<img src="{D["deals"]["img"]}" alt=""></div><div class="in">'
            '<h3>Canyons of the Escalante</h3><div class="was">Normally from $3,119 per person</div>'
            f'{facts}{DEAL_LINE}<div class="more">See the itinerary and departures &rarr;</div></div></div>')


def deals_now():
    return deals_window(f'<div style="margin-top:32px">{dealcard()}</div>')


def deals_wide():
    return deals_window(f'<div style="margin-top:32px">{dealcard(True)}</div>')


def deals_side():
    how = ('<div><div class="w9-how"><h3>How hot deals work</h3><ol>'
           '<li>Each deal is one date on one tour.</li>'
           '<li>It carries its own promo code.</li>'
           '<li>When the date goes, so does the deal.</li></ol></div>'
           '<div class="w9-sign"><b>Get the next deal by email</b>'
           'The same sign-up the newsletter page already has.'
           '<div class="f"><span>Your email</span><u>Sign up</u></div></div></div>')
    return deals_window(f'<div class="w9-dealrow">{dealcard()}{how}</div>')
