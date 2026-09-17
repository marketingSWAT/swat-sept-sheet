#!/usr/bin/env python3
"""
Builds site/index.html — the decision sheet for the 16 September 2026 review
of the SWAT storefront with Matt, Lance and SWAT's operations side.

Round one of those notes is already built and on staging: the route star, the
half-speed ticker, the nationwide map band, the 60-day floor, eight cards, towns
instead of hotels, the change notice, the per-date deal badge, the About film
slot and /review/build/. This sheet is everything from the same meeting that
cannot be built without someone choosing a shape first.

Numbering continues from the August sheet, which is answered in full, so
"twenty-three goes to B" can only mean one thing.

Every quote is verbatim from the transcript. Every "Now" panel is the shape the
deployed staging build actually renders, measured at a 1200px viewport on
16 September — see mocks.py for what was harvested and when.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import mocks as M                 # noqa: E402
from sheetkit import ANSWERS      # noqa: E402
import decisions_a as A           # noqa: E402
import decisions_b as B           # noqa: E402
import decisions_c as C           # noqa: E402

OUT = os.path.join(HERE, '..', 'site', 'index.html')


# ------------------------------------------------------------------ the page
RAIL = [
    (30, 'The words above the builder'),
    (31, 'State names on the map'),
    (32, 'The buttons'),
    (33, 'The shape of the page'),
    (34, 'What the page does back'),
    (35, '&ldquo;Activity level on request&rdquo;'),
    (36, 'Title, price, review bar'),
    (37, 'Is this trip right for you?'),
    (38, 'Start where you are'),
    (39, 'The film slot'),
]

ROUND1 = [
    (20, 'Activity level on a card'),
    (21, 'The activity section'),
    (22, 'Seasons on a tour page'),
    (23, 'Where the season filter lives'),
    (24, 'The state picker'),
    (25, 'Industry professionals'),
    (26, 'Reviews on a tour page'),
    (27, 'Video, and where it sits'),
    (28, 'Unfinished forms'),
    (29, 'The strip above the ticker'),
]


def rail_html():
    def rows(group):
        return ''.join(
            f'<a href="#d{n}" class="{"done" if n in ANSWERS else ""}">'
            f'<b>{n}</b>{t}</a>' for n, t in group)
    return (
        '<nav class="rail">'
        '<div class="rt">This round &mdash; 30 to 39</div>'
        f'{rows(RAIL)}'
        '<div class="rt">Answered &mdash; built and on staging</div>'
        f'{rows(ROUND1)}'
        '<div class="rt">After the decisions</div>'
        '<a href="#r1">Doing without asking</a>'
        '<a href="#r2">Waiting on SWAT</a>'
        '<a href="#r3">Said, but not built</a>'
        '<a href="#r4">Build order</a>'
        '<a href="#r5">How this was measured</a>'
        '</nav>')


MAST = """
<header class="mast">
  <div class="kick">Southwest Adventure Tours &middot; storefront rebuild</div>
  <h1>The staging walkthrough, drawn</h1>
  <p>Ten more shapes to pick, numbered <b>30 to 39</b>, from your walk through
  the staging build. Six of them are the <b>Build Your Own</b> page, which you
  asked for first; the rest are the home page&rsquo;s activity level, the top of
  a tour page, the qualifying panel, and the film slot. Each shows what the site
  does <b>today</b> beside two to four alternatives drawn at full size. Click any
  drawing to enlarge it, and pull the others in beside it from the chip row.</p>
  <p style="margin-top:12px"><b>Answer with letters.</b> &ldquo;Thirty-two goes
  to C, thirty-seven stays as it is.&rdquo; A voice note is fine &mdash; every
  option has a letter printed on it, and the letters never move.</p>
  <div class="who"><span>Crow</span><span>Walkthrough of staging</span>
  <span>16 Sep 2026</span><span>Round one, 20&ndash;29, is answered and folded
  below</span></div>
</header>
"""

LEDE = """
<div class="lede">
  <h2>What you already signed off, and therefore is not here</h2>
  <p>All ten decisions from the first sheet are built and live on staging, and
  your walkthrough confirmed seven of them outright: <b>the partner pages</b>,
  <b>hot deals</b>, <b>the images</b>, <b>the itinerary</b>, <b>the video
  slot</b>, <b>the archives, by-state and destination pages</b>, and <b>the
  bars on the home page</b>. Those are folded at the bottom of the rail with
  their letters recorded, and I am not reopening them.</p>
  <p>Three came back: <b>the activity mark</b> where a trip has no level
  (decision <a href="#d35">35</a>), <b>where the reviews sit</b> on a tour page
  (<a href="#d36">36</a>), and <b>&ldquo;Is this trip right for you?&rdquo;</b>
  (<a href="#d37">37</a>). Each of those is drawn again here rather than argued
  about, and the original decision links through to its replacement.</p>
  <p>One thing said out loud that needs no decision: <i>&ldquo;I love the
  interactive map, I think that looks great.&rdquo;</i> Decisions 31 to 33 make
  it bigger and readable. None of them takes it away.</p>
</div>
"""


def sec(kicker, title, para=None):
    p = f'<p>{para}</p>' if para else ''
    return f'<div class="sec"><div class="st">{kicker}</div><h2>{title}</h2>{p}</div>'


def register(anchor, kicker, title, intro, body):
    return (f'<section id="{anchor}">{sec(kicker, title, intro)}'
            f'<div class="d"><div class="d-body">{body}</div></div></section>')


R1 = register(
    'r1', 'Register one', 'Doing without asking',
    'Either you dictated it, or you praised it and it now needs protecting '
    'through the rework. No decision needed &mdash; listed so it is visible.',
    '<table class="tbl"><tr><th>What</th><th>Why</th><th>State</th></tr>'
    '<tr><td><b>The nav wraps onto two lines</b></td>'
    '<td>Nine items at 1200px. It is visible in every mockup on this page, '
    'because the mockups draw the real header. &ldquo;For Partners&rdquo; from '
    'decision 25 made it worse</td><td>Queued. It is a defect, not a choice, '
    'so it does not need a letter</td></tr>'
    '<tr><td><b>The floating &ldquo;Search trips&rdquo; pill sits on top of '
    'the builder</b></td><td>On /custom-tours/ it lands in the bottom-right '
    'corner, next to the form&rsquo;s own Send button. Two competing actions, '
    'one of them irrelevant on that page</td><td>Queued. Standing it down below '
    '<code>lg</code> on the pages that own that corner</td></tr>'
    '<tr><td><b>Keep the interactive map</b></td>'
    '<td>&ldquo;I love the interactive map, I think that looks great&rdquo;'
    '</td><td>Protected. Decisions 31-33 only ever make it bigger</td></tr>'
    '<tr><td><b>Keep the partner pages, hot deals, archives, by-state and '
    'destination pages as they are</b></td><td>&ldquo;looks good&rdquo; on '
    'each, unprompted</td><td>Frozen. Nothing in this round touches them'
    '</td></tr>'
    '<tr><td><b>Delete &ldquo;Email me the day-by-day&rdquo;</b></td>'
    '<td>Carried over and still live: travel agents copy the itineraries, so '
    'only booked guests should get them</td><td>Half a day, no design needed'
    '</td></tr>'
    '</table>')

R2 = register(
    'r2', 'Register two', 'Waiting on SWAT',
    'What I need, from whom, and what each piece blocks. Two of these decide '
    'whether decisions in this round can ever be more than a frame.',
    '<table class="tbl">'
    '<tr><th>Who</th><th>What</th><th>Blocks</th></tr>'
    '<tr><td class="n">Operations</td><td><b>Activity levels for the 42 trips '
    'that have none</b> &mdash; four options each, an afternoon for somebody '
    'who knows the trips. Plus sign-off on the four guidance paragraphs</td>'
    '<td>Decision <a href="#d35">35</a>. Until they exist, half the home shelf '
    'says &ldquo;on request&rdquo; and C is a workaround</td></tr>'
    '<tr><td class="n">Matt</td><td><b>Reviews picked per tour</b>, and '
    '<b>the highlights film</b></td>'
    '<td>Decisions <a href="#d36">36</a> and <a href="#d39">39</a>. Both are '
    'built as frames that render nothing until the content lands &mdash; every '
    'word in the review band today is placeholder, and there is no film '
    'anywhere on the site</td></tr>'
    '<tr><td class="n">Marketing</td><td><b>Fifteen state photographs</b>, or '
    'a yes to picking them from the library and verifying each one</td>'
    '<td>Decision <a href="#d38">38</a>, option C</td></tr>'
    '<tr><td class="n">Sean, via ops</td><td>Industry-professionals copy and '
    'five more large-group itineraries</td>'
    '<td>Decision 25 shipped as a shell; the words are still missing</td></tr>'
    '<tr><td class="n">Ashley</td><td>The forward deals calendar</td>'
    '<td>Decision 29 shipped. The strip cannot pre-schedule anything without '
    'dates</td></tr>'
    '<tr><td class="n">Operations</td><td>This year&rsquo;s CUA once approved, '
    'and an owner for re-reading it annually</td>'
    '<td>Decision <a href="#d37">37</a>. Whatever we do with the panel, a '
    'trail named on the site has to be on the permit</td></tr>'
    '</table>')

R3 = register(
    'r3', 'Register three', 'Said, but not built',
    'Things that read on the staging build as though they are finished, and '
    'are not. This is the register that keeps me honest.',
    '<ul class="ul">'
    '<li><b>Every review on the site is placeholder.</b> The band on a tour '
    'page renders sample text and labels itself as sample. There are zero real '
    'reviews in the record. Decision <a href="#d36">36</a> builds a working '
    'bar; it will be full of example text until Matt sends picks per '
    'tour.</li>'
    '<li><b>There is no film.</b> Not for the home page, not for About, not '
    'for any tour. Decision <a href="#d39">39</a> and decision 27 are both '
    'slots behind a flag that render <i>nothing</i> rather than an empty '
    'frame.</li>'
    '<li><b>Half the catalogue has no activity level.</b> 42 of 74 published '
    'trips. That is not a display bug and no option in decision '
    '<a href="#d35">35</a> except D actually fixes it.</li>'
    '<li><b>&ldquo;Slowly moves to the right&rdquo; is motion, and motion has '
    'rules.</b> The review bar will stop on hover and on focus, and will not '
    'animate at all for anyone whose device asks for reduced motion. This '
    'audience skews older and a crawling line of text is the kind of thing '
    'that gets resented.</li>'
    '<li><b>No A/B test can settle any of this.</b> There is no experiment '
    'framework on the build and not enough traffic to run one. Every '
    'recommendation on this page is a judgement, not a measurement &mdash; the '
    'measurements here are all of the <i>current</i> build, not of which '
    'option wins.</li>'
    '<li><b>Nothing automated reaches the visitor.</b> Leads reach SWAT by '
    'email and that is verified. A person who fills in Build Your Own gets no '
    'confirmation of any kind.</li>'
    '</ul>')

R4 = register(
    'r4', 'Register four', 'What I would build first',
    'Assuming you answer with letters and nothing else changes.',
    '<ul class="ul">'
    '<li><b>Same day, needing nothing from anyone:</b> the nav wrap, the '
    'floating pill on the builder page, decision <a href="#d30">30</a> '
    '(whichever letter) and decision <a href="#d35">35</a>. All four are '
    'hours.</li>'
    '<li><b>This week:</b> decision <a href="#d32">32</a> &mdash; the buttons. '
    'It is one control used in three places, so it fixes the builder, the home '
    'band and the filter bar at once, and decision <a href="#d38">38</a> and '
    'decision <a href="#d33">33</a> both assume it has landed.</li>'
    '<li><b>Then the Build Your Own rebuild:</b> decisions '
    '<a href="#d31">31</a>, <a href="#d33">33</a> and <a href="#d34">34</a> '
    'are one piece of work, not three. Roughly a week together, against '
    'two-and-a-half weeks if they are done separately.</li>'
    '<li><b>Then the tour page:</b> <a href="#d36">36</a> and '
    '<a href="#d37">37</a>, a day and a half between them, and they touch the '
    'same two files.</li>'
    '<li><b>Last, because they wait on somebody else:</b> '
    '<a href="#d38">38</a>&rsquo;s fifteen photographs and '
    '<a href="#d39">39</a>&rsquo;s film slot. The slot itself is half a day '
    'and can ship empty today.</li>'
    '</ul>')

R5 = register(
    'r5', 'Register five', 'How this was measured',
    'So the next round re-derives instead of trusting this page.',
    '<ul class="ul">'
    '<li><b>Every &ldquo;Now&rdquo; panel is the deployed staging build</b>, '
    'read at a 1200px viewport on 16 September 2026 &mdash; after round one of '
    'these notes shipped, so it is the build you walked through, not the one '
    'the first sheet drew.</li>'
    '<li><b>/custom-tours/ is 4,936px tall.</b> &ldquo;What a custom trip '
    'means here&rdquo; is 570px and puts the builder heading at y=1,344. The '
    'form holds <b>40 pill buttons</b>, 999px radius, 44px tall, 57&ndash;163px '
    'wide, wrapping into <b>8 rows with 8 different right edges</b> &mdash; '
    '695, 763, 280, 611, 443, 544, 694 and 497 &mdash; inside a 739px '
    'column.</li>'
    '<li><b>The home page.</b> 4 of the 8 cards on the shelf print '
    '&ldquo;Activity level on request&rdquo;; sitewide it is 42 of 74. '
    '&ldquo;Start where you are&rdquo; is 540px with four 263&times;197 '
    'photographs, and answering its first question leaves the section with '
    '<b>zero images</b> and 15 pills in 3 rows ending at 1137, 414 and 94. '
    'SWAT&rsquo;s own paragraph is 359px of full-width prose at y=4,580.</li>'
    '<li><b>The tour page</b> (Great Salt Lake and Antelope Island) is 9,697px. '
    'Gallery 672&times;380 at y=255; title column 395px at x=747; the h1 is '
    '34px and 75px tall; the price panel is 184px and ends 34px short of the '
    'gallery&rsquo;s bottom edge. &ldquo;Is this trip right for you?&rdquo; is '
    '267px at y=1,185; the reviews band is 326px at y=1,764.</li>'
    '<li><b>These rotate &mdash; re-derive them.</b> The eight featured trips '
    '(under the 60-day floor, so they change monthly), the live deals and '
    'their promo codes, and the departure dates.</li>'
    '<li><b>The map is real.</b> State outlines projected from us-atlas '
    'through an Albers equal-area conic, Alaska and Hawaii as the usual '
    'insets. The label positions in decision 31 are that projection&rsquo;s '
    'own anchors.</li>'
    '<li><b>Phone view is derived, not photographed.</b> The same markup '
    're-laid at 390px through the storefront&rsquo;s own breakpoints, then '
    'measured.</li>'
    '</ul>')


SCRIPT = r"""<script>
/* ------------------------------------------------------------------ scaling
   Each mockup is authored at a real width — 1200px for most, wider where the
   thing under argument needs the room — and scaled into whatever column it
   lands in. The factor is measured in JS rather than expressed in CSS:
   calc() cannot divide a length by a length to get a scale factor in every
   engine, and getting it wrong renders a 1200px page inside a 380px box with
   no error anywhere. */
(function () {
  var PHONE = 390;

  function base(w) {
    if (w.classList.contains('phone')) return PHONE;
    return parseFloat(w.style.getPropertyValue('--aw')) || 1200;
  }

  function fit(w, cap) {
    var b = base(w);
    var s = (cap ? Math.min(w.clientWidth, b) : w.clientWidth) / b;
    if (s > 0) w.style.setProperty('--s', s);
    rings(w);
  }

  /* A ring names an ELEMENT. It is positioned from that element's own box
     after layout, so a row that grows by a line does not leave it behind, and
     a selector that matches nothing hides rather than pointing somewhere
     wrong — a ring 20px out is worse than no ring. */
  function rings(w) {
    var m = w.querySelector('.mock');
    if (!m) return;
    var s = parseFloat(w.style.getPropertyValue('--s')) || 1;
    m.querySelectorAll('.ring').forEach(function (r) {
      var el = m.querySelector(r.dataset.sel);
      if (!el || w.classList.contains('phone')) {
        r.removeAttribute('data-on'); return;
      }
      var a = el.getBoundingClientRect(), b = m.getBoundingClientRect();
      if (!a.width && !a.height) { r.removeAttribute('data-on'); return; }
      r.style.left = ((a.left - b.left) / s - 5) + 'px';
      r.style.top = ((a.top - b.top) / s - 5) + 'px';
      r.style.width = (a.width / s + 10) + 'px';
      r.style.height = (a.height / s + 10) + 'px';
      r.setAttribute('data-on', '1');
    });
  }

  function setPhone(w, on, cap) {
    w.classList.toggle('phone', on);
    if (on) {
      var m = w.querySelector('.mock'), prev = m.style.height;
      m.style.height = 'auto';
      w.style.setProperty('--ph', Math.ceil(m.scrollHeight));
      m.style.height = prev;
    }
    fit(w, cap);
  }

  /* A typed canvas height drifts the moment a mockup gains a row: too small
     clips the drawing, too large leaves white paper that reads as a gap.
     Neither throws. So the declared number is a hint and the real one is
     measured. */
  function height(w) {
    var m = w.querySelector('.mock'), prev = m.style.height;
    m.style.height = 'auto';
    var nat = Math.ceil(m.scrollHeight);
    m.style.height = prev;
    if (nat > 0) w.style.setProperty('--mh', nat);
  }

  /* Then every panel in a decision gets the TALLEST canvas in that decision.
     Unequal boxes read as a difference in the designs rather than in the
     paper, and that misreading has happened on a live sheet before. */
  function equalise(root) {
    (root || document).querySelectorAll('.d, .zoom-in').forEach(function (d) {
      var ws = [].slice.call(d.querySelectorAll('.mockwrap:not(.phone)'));
      if (ws.length < 2) return;
      var tall = 0;
      ws.forEach(function (w) {
        tall = Math.max(tall, parseFloat(w.style.getPropertyValue('--mh')) || 0);
      });
      ws.forEach(function (w) { w.style.setProperty('--mh', tall); fit(w); });
    });
  }

  var wraps = [].slice.call(document.querySelectorAll('.mockwrap'));
  wraps.forEach(function (w) { height(w); fit(w); });
  equalise();
  window.addEventListener('load', function () {
    wraps.forEach(function (w) {
      if (!w.classList.contains('phone')) height(w);
    });
    equalise();
  });
  if (window.ResizeObserver) {
    var ro = new ResizeObserver(function (es) {
      es.forEach(function (e) { fit(e.target); });
    });
    wraps.forEach(function (w) { ro.observe(w); });
  } else {
    window.addEventListener('resize', function () {
      wraps.forEach(function (w) { fit(w); });
    });
  }

  /* ------------------------------------------------------ mockup toolbars */
  wraps.forEach(function (w) {
    var bar = document.createElement('div');
    bar.className = 'mock-bar';
    bar.innerHTML = '<span class="seg">' +
      '<button type="button" class="on" data-w="desk">Desktop</button>' +
      '<button type="button" data-w="phone">Phone</button></span>';
    w.parentNode.insertBefore(bar, w);
    bar.querySelectorAll('.seg button').forEach(function (b) {
      b.addEventListener('click', function () {
        bar.querySelectorAll('.seg button').forEach(function (o) {
          o.classList.toggle('on', o === b);
        });
        setPhone(w, b.dataset.w === 'phone');
      });
    });
  });

  /* ------------------------------------------------------- the enlarged view
     One overlay, however many panes. Clicking a mockup opens it large; the
     chip row brings its siblings in beside it. Panes are CLONES — moving the
     real node would mean closing the overlay could lose a drawing from the
     sheet. Never more than two columns: four across a 1440px laptop is about
     340px a pane, which is the sheet's own grid and the thing this view
     exists to escape. */
  var MAXPANE = 4;
  var shown = [], phoneAll = false;

  var ov = document.createElement('div');
  ov.className = 'zoom';
  ov.innerHTML =
    '<div class="zoom-bar">' +
      '<span class="t"></span>' +
      '<span class="chips"></span>' +
      '<span class="nav"><button type="button" class="pv">&larr; Prev</button>' +
      '<button type="button" class="nx">Next &rarr;</button></span>' +
      '<span class="seg"><button type="button" class="on" data-w="desk">Desktop</button>' +
      '<button type="button" data-w="phone">Phone</button></span>' +
      '<button class="x" type="button">Close &times;</button>' +
    '</div><div class="zoom-in"></div>';
  document.body.appendChild(ov);
  var slot = ov.querySelector('.zoom-in');
  var title = ov.querySelector('.t');
  var chips = ov.querySelector('.chips');

  function meta(w) {
    var o = w.closest('.opt');
    return {
      letter: (o && o.dataset.letter) || '',
      name: (o && o.dataset.name) || 'Mockup',
      rec: !!(o && o.classList.contains('rec')),
      now: !!(o && o.classList.contains('now')),
      opt: o
    };
  }
  function decTitle(d) {
    if (!d) return '';
    var h = d.querySelector('h3');
    if (!h) return '';
    return h.textContent.replace(/New ·.*$|Redrawn ·.*$/, '').trim();
  }

  function close() {
    ov.classList.remove('on');
    slot.innerHTML = '';
    shown = [];
    document.body.classList.remove('noscroll');
  }
  ov.querySelector('.x').addEventListener('click', close);
  ov.addEventListener('click', function (e) { if (e.target === ov) close(); });

  ov.querySelectorAll('.zoom-bar .seg button').forEach(function (b) {
    b.addEventListener('click', function () {
      ov.querySelectorAll('.zoom-bar .seg button').forEach(function (o) {
        o.classList.toggle('on', o === b);
      });
      phoneAll = b.dataset.w === 'phone';
      draw();
    });
  });

  /* A chip and a pane's Remove button are the same action. Dropping the last
     pane closes rather than leaving an empty stage. */
  function toggle(w) {
    var i = shown.indexOf(w);
    if (i > -1) {
      if (shown.length === 1) { close(); return; }
      shown.splice(i, 1);
    } else {
      if (shown.length === MAXPANE) shown.shift();
      shown.push(w);
    }
    draw();
  }

  function draw() {
    var decs = [];
    shown.forEach(function (w) {
      var d = w.closest('.d');
      if (d && decs.indexOf(d) < 0) decs.push(d);
    });

    chips.innerHTML = '';
    decs.forEach(function (d) {
      var g = document.createElement('span');
      g.className = 'grp';
      if (decs.length > 1) {
        var e = document.createElement('em');
        e.textContent = decTitle(d);
        g.appendChild(e);
      }
      [].slice.call(d.querySelectorAll('.opt .mockwrap')).forEach(function (w) {
        var m = meta(w);
        var b = document.createElement('button');
        b.type = 'button';
        var k = document.createElement('b');
        k.textContent = m.letter;
        b.appendChild(k);
        b.appendChild(document.createTextNode(m.name));
        if (m.rec) {
          var st = document.createElement('span');
          st.className = 'star';
          st.textContent = '★';
          b.appendChild(st);
        }
        if (shown.indexOf(w) > -1) b.className = 'on';
        b.addEventListener('click', function () { toggle(w); });
        g.appendChild(b);
      });
      chips.appendChild(g);
    });

    title.textContent = decs.length === 1 ? decTitle(decs[0])
      : shown.length + ' mockups';

    /* "Now" takes the leftmost slot whatever order the panes were added —
       comparing against the build is the movement this view exists for. Sort a
       copy, so pinning a fifth pane still drops the oldest, not the leftmost. */
    var order = shown.slice().sort(function (a, b) {
      return (meta(a).now ? 0 : 1) - (meta(b).now ? 0 : 1);
    });

    slot.className = 'zoom-in n' + Math.min(order.length, MAXPANE) +
      (phoneAll ? ' ph' : '');
    slot.innerHTML = '';
    order.forEach(function (w) {
      var m = meta(w);
      var pane = document.createElement('div');
      pane.className = 'pane';
      var cap = document.createElement('div');
      cap.className = 'cap';
      var nm = document.createElement('span');
      /* The caption carries the LETTER and the name. Zoomed into one drawing
         on a phone the heading is off screen, and the letter is the thing they
         are about to say out loud. */
      nm.innerHTML = (decs.length > 1 ? decTitle(w.closest('.d')) + ' &mdash; ' : '') +
        '<b>' + m.letter + '</b> &middot; ' + m.name +
        (m.rec ? ' <span class="star">★ MY PICK</span>' : '');
      var rm = document.createElement('button');
      rm.type = 'button';
      rm.className = 'rm';
      rm.textContent = 'Remove ×';
      rm.addEventListener('click', function () { toggle(w); });
      cap.appendChild(nm);
      cap.appendChild(rm);
      var clone = w.cloneNode(true);
      clone.style.cursor = 'default';
      pane.appendChild(cap);
      pane.appendChild(clone);
      /* The panel's own prose rides in under the drawing. Without it the
         reader compares four pictures of one screen with nothing to tell them
         apart, and the sentence that explains the difference is on the sheet
         behind an overlay they cannot scroll. */
      if (m.opt) {
        var body = document.createElement('div');
        body.className = 'pane-body';
        var ch = m.opt.querySelector('.changes');
        var ob = m.opt.querySelector('.opt-b');
        body.innerHTML = (ch ? ch.outerHTML : '') + (ob ? ob.outerHTML : '');
        pane.appendChild(body);
      }
      slot.appendChild(pane);
    });

    /* A clone has no width until it is in the document, so scale on the next
       frame — capped, so one pane never renders past its authored width and a
       390px phone layout is not blown up into a tablet. */
    requestAnimationFrame(function () {
      slot.querySelectorAll('.mockwrap').forEach(function (c) {
        if (phoneAll !== c.classList.contains('phone')) setPhone(c, phoneAll, true);
        else fit(c, true);
      });
      equalise(slot);
    });
  }

  function openZoom(list) {
    shown = list.slice(0, MAXPANE);
    phoneAll = shown[0] ? shown[0].classList.contains('phone') : false;
    ov.querySelectorAll('.zoom-bar .seg button').forEach(function (o) {
      o.classList.toggle('on', (o.dataset.w === 'phone') === phoneAll);
    });
    draw();
    ov.classList.add('on');
    document.body.classList.add('noscroll');
  }

  wraps.forEach(function (w) {
    w.addEventListener('click', function () { openZoom([w]); });
  });

  /* Prev / Next: same panes, next decision, and the sheet underneath moves
     with the stage so closing lands the reader where they got to. A ten
     decision sheet answered by opening and closing ten times loses their
     place every time. */
  function step(dir) {
    var d = shown[0] && shown[0].closest('.d');
    var all = [].slice.call(document.querySelectorAll('.d'));
    var i = all.indexOf(d);
    var next = all[i + dir];
    while (next && !next.querySelector('.opt .mockwrap')) {
      i += dir; next = all[i + dir];
    }
    if (!next) return;
    if (next.classList.contains('done')) next.classList.add('open');
    var ws = [].slice.call(next.querySelectorAll('.opt .mockwrap'));
    if (!ws.length) return;
    shown = ws.slice(0, 2);
    next.scrollIntoView({ block: 'start' });
    draw();
  }
  ov.querySelector('.pv').addEventListener('click', function () { step(-1); });
  ov.querySelector('.nx').addEventListener('click', function () { step(1); });

  document.addEventListener('keydown', function (e) {
    if (!ov.classList.contains('on')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowRight') step(1);
    if (e.key === 'ArrowLeft') step(-1);
  });

  /* An answered decision folds, and reopens on a click, a rail link or
     Prev/Next — never on a scroll. Someone scrolled into a settled decision on
     the last sheet and read it as live. */
  document.querySelectorAll('.d.done .d-show').forEach(function (b) {
    b.addEventListener('click', function () {
      var d = b.closest('.d');
      d.classList.toggle('open');
      if (d.classList.contains('open')) {
        d.querySelectorAll('.mockwrap').forEach(function (w) {
          height(w); fit(w);
        });
        equalise();
      }
    });
  });
  document.querySelectorAll('.rail a[href^="#d"]').forEach(function (a) {
    a.addEventListener('click', function () {
      var d = document.querySelector(a.getAttribute('href'));
      if (d && d.classList.contains('done')) d.classList.add('open');
    });
  });
})();
</script>"""


def build():
    css = open(os.path.join(HERE, 'sheet.css')).read()
    decisions = C.ALL + A.ALL + B.ALL
    body = (MAST + LEDE +
            sec('This round', 'Ten more shapes to pick',
                'Green ring is what ships today. Amber ring is the one I would '
                'build, and it says so in words as well. Decisions 20 to 29 '
                'are answered and folded further down &mdash; open any of them '
                'to see what was picked.') +
            ''.join(decisions) + R1 + R2 + R3 + R4 + R5)

    foot = (
        '<div class="foot">Round two, built 16 September 2026 from '
        'Crow&rsquo;s walkthrough of the staging build. Quotes are verbatim. '
        'Current-build panels were read off '
        '<code>swat-website-storefront-git-staging-swat2.vercel.app</code> at '
        'a 1200px viewport on 16 September, after decisions 20&ndash;29 '
        'shipped &mdash; see register five for every number quoted on this '
        'page. Decisions 20&ndash;29 and their answers are folded below this '
        'round. This page quotes people candidly and is <code>noindex</code>; '
        'the URL is the only thing keeping it private.</div>')

    html = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>SWAT — the staging walkthrough, drawn</title>
<style>{css}</style>
</head><body>
{M.mapdefs()}
<div class="wrap">{rail_html()}<main class="main">{body}{foot}</main></div>
{SCRIPT}
</body></html>"""

    with open(OUT, 'w') as f:
        f.write(html)
    n = html.count('<section class="d')
    print(f'{OUT}: {len(html):,} bytes, {n} decisions, '
          f'{html.count("class=\"opt ")} option panels')


if __name__ == '__main__':
    build()
