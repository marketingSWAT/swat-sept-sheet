"""The sheet's component layer — the letter ledger and the four blocks
every decision is built from.

It lives apart from render.py so the decision files can import it
without importing the thing that imports them.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, 'letters.json')


# ------------------------------------------------------------- letter ledger
def letters_for(dec_no, names):
    """Bind each option NAME to a letter for the life of the sheet.

    The answers arrive as speech — "twenty-three goes to B" is the whole
    record. A letter that gets recycled for a different drawing silently
    rewrites something the reader already said, and nothing on the page looks
    wrong. So a collision raises rather than warns.
    """
    book = json.loads(open(LEDGER).read()) if os.path.exists(LEDGER) else {}
    issued = book.setdefault(str(dec_no), {})
    out = []
    for name in names:
        hit = next((L for L, n in issued.items() if n == name), None)
        if hit is None:
            free = [L for L in 'ABCDEFGH' if L not in issued]
            if not free:
                raise SystemExit(f'decision {dec_no}: out of letters')
            hit = free[0]
            issued[hit] = name
        out.append(hit)
    with open(LEDGER, 'w') as f:
        f.write(json.dumps(book, indent=2, sort_keys=True))
    return out


def retired(dec_no, live_names):
    """Letters issued earlier whose option has left the table."""
    if not os.path.exists(LEDGER):
        return []
    book = json.loads(open(LEDGER).read())
    return [(L, n) for L, n in sorted(book.get(str(dec_no), {}).items())
            if n not in live_names]


# --------------------------------------------------------------- components
def opt(name, changes, body, cost=None, risk=None, cls='', mockup=''):
    """One column of a decision.

    `changes` is the numbered What-changed list and it LEADS the panel: the
    reader is looking at three drawings of the same screen, so the difference
    has to be named before the argument for it. The letter is filled in by
    `dec()` from the ledger, never by enumerate().
    """
    c = ''
    if cost or risk:
        bits = []
        if cost:
            bits.append(f'<span><b>Build:</b> {cost}</span>')
        if risk:
            bits.append(f'<span><b>Risk:</b> {risk}</span>')
        c = f'<div class="cost">{"".join(bits)}</div>'
    lis = ''.join(f'<li>{x}</li>' for x in changes)
    pick = ('<span class="pick"><span class="star">&#9733;</span> MY PICK</span>'
            if cls == 'rec' else '')
    return (f'<div class="opt {cls}" data-name="{name}">'
            f'<div class="opt-hd"><span class="k">@@K@@</span>'
            f'<span class="n">{name}</span>{pick}</div>'
            f'{mockup}<ul class="changes">{lis}</ul>'
            f'<div class="opt-b">{body}{c}</div></div>')


def quote(lines, who):
    ps = ''.join(f'<p>&ldquo;{l}&rdquo;</p>' for l in lines)
    return f'<div class="q">{ps}<cite>{who}</cite></div>'


def verdict(text, warn=False, title='My recommendation'):
    cls = ' warn' if warn else ''
    body = ''.join(f'<p>{t}</p>' for t in text)
    return f'<div class="verdict{cls}"><div class="vt">{title}</div>{body}</div>'


#: Answers, as they come back. `dec()` folds an answered decision and prints
#: the pick on its front, so the link holds the record rather than a voice note.
#:
#: Round one (20-29) was answered in one sentence on 16 September — "let's go
#: ahead and do all of your recommended picks and build that out and push it to
#: staging" — so every one of them went to the option marked MY PICK. All ten
#: are built and live on staging, and Crow has now walked the built versions:
#: "most of this looks really good". Three of them were reopened by that
#: walkthrough and their replacements are decisions 35, 36 and 37.
ANSWERS = {
    20: ('C', 'all recommended picks &mdash; shipped, then reopened as '
              'decision <a href="#d35">35</a>'),
    21: ('C', 'all recommended picks &mdash; shipped, then reopened as '
              'decision <a href="#d37">37</a>'),
    22: ('C', 'all recommended picks &mdash; shipped and signed off'),
    23: ('C', 'all recommended picks &mdash; shipped and signed off'),
    24: ('C', 'all recommended picks &mdash; shipped. &ldquo;I love the '
              'interactive map, I think that looks great.&rdquo; Refined by '
              'decisions <a href="#d31">31</a>-<a href="#d33">33</a>'),
    25: ('B', 'all recommended picks &mdash; shipped. &ldquo;The partner '
              'pages looks good.&rdquo;'),
    26: ('C', 'all recommended picks &mdash; shipped, then reopened as '
              'decision <a href="#d36">36</a>'),
    27: ('C', 'all recommended picks &mdash; shipped. &ldquo;The slot for a '
              'video looks good.&rdquo; Extended by decision '
              '<a href="#d39">39</a>'),
    28: ('D', 'all recommended picks &mdash; shipped and signed off'),
    29: ('B', 'all recommended picks &mdash; shipped. &ldquo;I like the bars, '
              'that looks good.&rdquo;'),

    # Round two, answered decision by decision on the evening of 16 September.
    # Nine of the ten went to the recommendation; 36 was sent back and is
    # redrawn above rather than folded, which is why it is not in here.
    30: ('C', 'built and on staging &mdash; the form starts at y=740, against '
              'y=1,344'),
    31: ('B', 'built and on staging &mdash; fifty codes, eight led out to the '
              'margin'),
    32: ('C', 'built and on staging &mdash; every question has one right edge '
              'now'),
    33: ('B', 'built and on staging &mdash; the map is 1,112px wide. It did '
              'not shorten the page, as measured. Reopened as decision '
              '<a href="#d40">40</a>: at 1440 the map is 687px tall and the '
              'answers under it fall off the screen'),
    34: ('C', 'built and on staging. <b>C only</b> &mdash; the &ldquo;14 trips '
              'already go to Utah&rdquo; line (B) was not asked for and is not '
              'built'),
    35: ('A', 'left as it is &mdash; &ldquo;maybe just leave it as is, I think '
              'that&rsquo;s fine.&rdquo; The 42 missing levels (D) stay on the '
              'waiting list'),
    37: ('C', 'built and on staging &mdash; a 44px line up top, the panel at '
              'y=3,631. Operations should be told it moved'),
    38: ('C', 'built and on staging &mdash; fifteen photo tiles, and the door '
              'you chose stays'),
    39: ('B', 'built and on staging, behind the film flag &mdash; there is '
              'still no cut'),
}


def dec(no, title, tags, quotes, opts, verd, since=None, cols=None):
    """One decision block.

    `opts` is a list of `opt()` strings in panel order, starting with Now. The
    letters are issued here from the ledger and stamped into each panel, which
    is the only place they are decided.
    """
    names = []
    for o in opts:
        names.append(o.split('data-name="', 1)[1].split('"', 1)[0])
    ls = letters_for(no, names)
    filled = []
    for o, L in zip(opts, ls):
        filled.append(o.replace('@@K@@', L, 1)
                       .replace('class="opt ', f'data-letter="{L}" class="opt ', 1))

    t = ''.join(f'<span class="tag {c}">{x}</span>' for x, c in tags)
    sc = ''
    if since:
        kind, when = since
        cl = ' redraw' if kind != 'New' else ''
        sc = f'<span class="d-since{cl}">{kind} &middot; {when}</span>'

    ans = ANSWERS.get(no)
    lock = done = ''
    if ans:
        done = ' done'
        lock = (f'<div class="d-locked">LOCKED &middot; <b>{ans[0]}</b> '
                f'&mdash; {ans[1]}</div>')

    ret = retired(no, names)
    rets = ''
    if ret:
        rets = ('<div class="retired">Retired: ' + ', '.join(
            f'<b>{L}</b> {n}' for L, n in ret) + ' &mdash; those letters are spent.</div>')

    n = len(filled)
    cols = cols or min(n, 4)
    show = ('<button class="d-show" type="button">Show the options</button>'
            if ans else '')
    return (f'<section class="d{done}" id="d{no}">'
            f'<div class="d-hd"><span class="no">{no}</span>'
            f'<div><h3>{title}{sc}</h3><div class="tags">{t}</div>{lock}{show}</div>'
            f'</div>'
            f'<div class="d-body">{"".join(quotes)}'
            f'<div class="opts c{cols}">{"".join(filled)}</div>{rets}{verd}</div>'
            f'</section>')


