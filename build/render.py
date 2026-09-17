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

OUT = os.path.join(HERE, '..', 'site', 'index.html')


# ------------------------------------------------------------------ the page
RAIL = [
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
    items = ''.join(
        f'<a href="#d{n}" class="{"done" if n in ANSWERS else ""}">'
        f'<b>{n}</b>{t}</a>' for n, t in RAIL)
    return (
        '<nav class="rail">'
        '<div class="rt">The decisions</div>'
        f'{items}'
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
  <h1>The 16 September review, drawn</h1>
  <p>Ten things from Tuesday&rsquo;s call that cannot be built until somebody
  picks a shape. Each one shows what the site does <b>today</b>, beside two to
  four alternatives drawn at full size. Click any drawing to enlarge it, and
  pull the others in beside it from the chip row.</p>
  <p style="margin-top:12px"><b>Answer with letters.</b> &ldquo;Twenty-three
  goes to B, twenty-six stays as it is.&rdquo; A voice note is fine &mdash;
  every option has a letter printed on it, and the letters never move.</p>
  <div class="who"><span>Matt Warren</span><span>Lance Card</span>
  <span>SWAT operations</span><span>Recorded 16 Sep 2026, 1h09m</span>
  <span>1,103 lines</span></div>
</header>
"""

LEDE = """
<div class="lede">
  <h2>What is already built, and therefore not here</h2>
  <p>Round one of these notes shipped to staging on Tuesday night and is not up
  for discussion: the <b>star on the route start</b>, the <b>ticker at half
  speed</b>, the map band leading with <b>nationwide</b>, the <b>60-day floor</b>
  under the home shelf, <b>eight cards</b>, day rows naming the <b>town rather
  than the hotel</b>, the <b>change notice</b> in navy on every tour page, the
  <b>flame and promo code</b> on a discounted departure, the <b>About film
  slot</b>, and <b>/review/build/</b> for the sales team.</p>
  <p>Two things the room raised that need nothing from anyone: the map&rsquo;s
  size and image are settled &mdash; <i>&ldquo;the size is perfect, I even
  don&rsquo;t mind the image the way that it is&rdquo;</i> &mdash; and the
  numbered stops are <b>not broken</b>. They render when a tour is selected;
  Matt was clicking a place dot.</p>
  <p>What is below is the rest of the meeting: the parts where the answer is a
  layout, not a line of code.</p>
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
    'Dictated in the room, or praised and therefore protected through the '
    'rework. No decision needed &mdash; listed so it is visible.',
    '<table class="tbl"><tr><th>What</th><th>Their words</th><th>State</th></tr>'
    '<tr><td><b>Delete &ldquo;Email me the day-by-day&rdquo;</b> from every '
    'tour page</td><td>&ldquo;that feature itself should probably be '
    'removed&rdquo; &mdash; travel agents copy the itineraries, so only booked '
    'guests get them</td><td>Still live. Half a day, no design needed</td></tr>'
    '<tr><td><b>Keep the long itinerary</b></td><td>&ldquo;is this itinerary '
    'too detailed, do we need to just do bullet points&rdquo; &rarr; '
    '&ldquo;I say we keep it the way that it is&rdquo;</td><td>Settled. '
    'Written for SEO and AEO, and they agreed</td></tr>'
    '<tr><td><b>Never remove the hot deals ticker</b></td>'
    '<td>&ldquo;I don&rsquo;t ever want to lose the hot deals ticker&rdquo;'
    '</td><td>Protected. Decision 29 is the strip <i>above</i> it</td></tr>'
    '<tr><td><b>Fix the hero search line</b></td><td>&mdash;</td>'
    '<td>It still says &ldquo;Anywhere in the Southwest&rdquo;, one screen '
    'above &ldquo;We&rsquo;re nationwide, not just the Southwest&rdquo;. '
    'Changing it on sight</td></tr>'
    '<tr><td><b>Large group grows from 3 itineraries to 8+</b></td>'
    '<td>&ldquo;this one only shows three of them, we should have eight at '
    'least&rdquo;</td><td>Page is built; it needs the five itineraries, not a '
    'layout</td></tr>'
    '</table>')

R2 = register(
    'r2', 'Register two', 'Waiting on SWAT',
    'What I need, from whom, and what each piece blocks. Sending it as one '
    'list beats asking in pieces.',
    '<table class="tbl">'
    '<tr><th>Who</th><th>What</th><th>Blocks</th></tr>'
    '<tr><td class="n">Matt</td><td>The three-minute film; About page copy; '
    'correct imagery and the largest originals; testimonials broken out by '
    'location; reviews picked per tour; a Black Friday icon</td>'
    '<td>Decisions 26 and 27 cannot go live without the reviews and the cut, '
    'though both can be built empty</td></tr>'
    '<tr><td class="n">Sean, via ops</td><td>Industry-professionals copy, five '
    'more large-group itineraries, and the name for that page</td>'
    '<td>Decision 25 &mdash; the shape can be chosen now, the words cannot be '
    'written here</td></tr>'
    '<tr><td class="n">Ashley</td><td>The forward deals calendar</td>'
    '<td>Decision 29 &mdash; campaigns can only be pre-scheduled if the dates '
    'exist</td></tr>'
    '<tr><td class="n">Operations</td><td>This year&rsquo;s CUA once approved, '
    'plus the timing docs &mdash; and an owner for re-reading it every '
    'year</td><td>Decision 21. Any trail named on the site has to be on the '
    'permit: &ldquo;it can change year by year&rdquo;</td></tr>'
    '<tr><td class="n">Softrip</td><td>Their own data. Asked whether the '
    'bookings and tour codes are current, the answer in the room was '
    '&ldquo;No.&rdquo;</td><td>Live booking, and nothing else</td></tr>'
    '<tr><td class="n">Monica &amp; Robin</td><td>Their pass on Build Your '
    'Own</td><td>Nothing &mdash; but decision 24 is the thing they will be '
    'looking at</td></tr>'
    '</table>')

R3 = register(
    'r3', 'Register three', 'Said in the room, but not built',
    'Things described on the call as though they already exist, or that were '
    'agreed to without anyone pricing them. This is the register that keeps me '
    'honest.',
    '<ul class="ul">'
    '<li><b>&ldquo;It&rsquo;s all in the system&rdquo; &mdash; Softrip.</b> '
    'The poll API can return departures, and I have the key. But asked '
    'directly whether every booking and tour code is up to date in Softrip, '
    'the answer was no. Live booking is gated on their data, not on my '
    'integration.</li>'
    '<li><b>Connecting the Google reviews.</b> Google&rsquo;s own API returns '
    'the five most recent reviews for a business and nothing more &mdash; you '
    'cannot pull 300 of them, you cannot filter them by tour, and you cannot '
    'choose which five. Every &ldquo;all our Google reviews on the site&rdquo; '
    'widget is a paid third party. Decision 26 draws what is actually '
    'reachable.</li>'
    '<li><b>Abandoned-form email.</b> Sending &ldquo;you never finished&rdquo; '
    'mail needs the email address captured <i>before</i> the form is '
    'abandoned, which is a change to step one, not a bolt-on. That is half of '
    'decision 28.</li>'
    '<li><b>Reading each CUA and updating the site.</b> Agreed on the call as '
    'though it were free. It is a recurring annual job for a named person, and '
    'if nobody owns it the trail lists go stale silently &mdash; which is '
    'worse than not listing them.</li>'
    '<li><b>&ldquo;Ingest it straight into the CRM.&rdquo;</b> Leads write to '
    'our own database and email out today. The audit found Zoho Forms, Zoho '
    'CRM, Pipedrive and a Satis.fi widget all in use on the old site. Somebody '
    'has to say which one is the CRM.</li>'
    '<li><b>A/B testing which of these wins.</b> Not available. There is no '
    'experiment framework on the build and no traffic to run one on yet, so '
    'every choice on this sheet is a judgement, not a measurement.</li>'
    '</ul>')

R4 = register(
    'r4', 'Register four', 'What I would build first',
    'Lance asked twice for a date. This is the order I would work in, and the '
    'reason the answer is not one number.',
    '<ul class="ul">'
    '<li><b>This week, needing nothing from anyone:</b> delete the itinerary '
    'email, fix the hero search line, the campaign strip (29), the activity '
    'mark on cards (20). All four are days, not weeks.</li>'
    '<li><b>Next, once the letters come back:</b> the activity section (21), '
    'reviews and video wired as empty frames (26, 27), the unfinished-form '
    'catch (28). Empty frames matter: the moment Matt&rsquo;s reviews and cut '
    'land they drop in, rather than starting a build.</li>'
    '<li><b>The two big ones:</b> seasons (22, 23) and the state picker (24). '
    'These are the only items on the sheet measured in weeks rather than days, '
    'and 22 needs four photographs per tour that nobody has counted yet.</li>'
    '<li><b>Industry professionals (25)</b> sits outside that order because it '
    'is blocked on Sean&rsquo;s copy, not on effort. The shell is a day.</li>'
    '<li><b>Launch does not wait for live booking.</b> Softrip&rsquo;s data is '
    'not current, by their own answer, so a launch with enquiry-led booking and '
    'checkout wired afterwards is the only version of &ldquo;live&rdquo; that '
    'has a date on it. That also matches what you told them: a site that keeps '
    'evolving.</li>'
    '</ul>')

R5 = register(
    'r5', 'Register five', 'How this was measured',
    'So the next round re-derives instead of trusting this page.',
    '<ul class="ul">'
    '<li><b>Every &ldquo;Now&rdquo; panel is the deployed staging build</b>, '
    'read at a 1200px viewport on 16 September 2026, after round one of these '
    'notes shipped &mdash; not from source and not from memory.</li>'
    '<li><b>Measured, not estimated:</b> the trip shelf is 3-across at 350.2px '
    'with 515px cards; the tour page runs a 672&times;380 gallery against a '
    '395px title column; the fact strip is at y=659, the sticky subnav at '
    'y=847, the change notice at y=961 and the 360px booking rail beside it. '
    'The tour page is 11,468px tall.</li>'
    '<li><b>These rotate &mdash; re-derive them.</b> The eight featured trips '
    '(November&rsquo;s, under the 60-day floor), the four live deals and their '
    'promo codes, and the 61 departure dates on the Mighty 5.</li>'
    '<li><b>The map is real.</b> State outlines are projected from us-atlas '
    'through an Albers equal-area conic with Alaska and Hawaii as the usual '
    'insets &mdash; not a drawing of a country.</li>'
    '<li><b>Phone view is derived, not photographed.</b> The same markup '
    're-laid at 390px through the storefront&rsquo;s own breakpoints, then '
    'measured. It is an approximation of the phone layout from the build&rsquo;s '
    'rules.</li>'
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
    decisions = A.ALL + B.ALL
    body = (MAST + LEDE +
            sec('The decisions', 'Ten shapes to pick',
                'Green ring is what ships today. Amber ring is the one I would '
                'build, and it says so in words as well.') +
            ''.join(decisions) + R1 + R2 + R3 + R4 + R5)

    foot = (
        '<div class="foot">Built 16 September 2026 from the full 1,103-line '
        'transcript of that day&rsquo;s review. Quotes are verbatim; the '
        '&ldquo;Other Participants&rdquo; track has no speaker labels, so '
        'anything not said by Matt or addressed by name is attributed to '
        '<code>[ops]</code> rather than guessed. Current-build panels were '
        'read off <code>swat-website-storefront-git-staging-swat2.vercel.app</code> '
        'at a 1200px viewport on 16 September, after round one of these notes '
        'shipped. This page quotes people candidly and is <code>noindex</code>; '
        'the URL is the only thing keeping it private.</div>')

    html = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>SWAT — the 16 September review, drawn</title>
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
