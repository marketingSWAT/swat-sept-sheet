"""Decision 74: the whole About page, redrawn.

Crow's screenshot of the About page, 29 September: the canyon photograph at
full width with a narrow column of words under it. He asked for a full
redesign in a few different shapes. Codex ran out of credits before drawing
anything, so all three alternatives are Claude's.

A is a real full-page screenshot of production above the footer. B-D are
drawn at 1920 with the page's own words and photographs; every fact on a
person card is from that person's own profile page. mocks_about.py has the
detail, about.css the styles.
"""

import mocks as m
import mocks_about as ab
from sheetkit import opt, quote, verdict, dec

ALL = []
NEW = ('New', '29 Sep')
AW = 1920


def mk(html, h, *rings):
    return m.mock(html + ''.join(m.ring(n, s) for n, s in rings), h, aw=AW)


Q = quote(
    ['I think we need to rework the about page, I dont really like how this '
     'photo is so large and text below, can you use codex to run a full '
     'redesign of this entire page and give me a couple designs of different '
     'ways of showing it',
     'Dont use codex then you can take this on'],
    'Crow, 29 September')


ALL.append(dec(
    74, 'The About page',
    [('The About page, top to bottom', ''), ('Crow', 'who'),
     ('about 1 day', ''), ('Today it is about 7 screens tall', 'big')],
    [Q],
    [
        opt('As it is today',
            ['<b>A photo the full width of the screen with a narrow column of words '
             'under it, twice</b>: the canyon view near the top and the staff photo '
             'halfway down.',
             'It says &ldquo;watch the following video&rdquo; and there is no video. '
             'It says to click &ldquo;Our Team&rdquo; and &ldquo;Careers&rdquo; '
             'buttons that do not exist.',
             '<b>Almost two screens of staff handbook</b>: twelve service values, '
             'the employee promise that calls staff &ldquo;our Ladies and '
             'Gentlemen,&rdquo; and the mission statement a second time. Plus a '
             'photo captioned &ldquo;Wynn Hall&rdquo; that nobody can explain.',
             '<b>Ten faces with a name and nothing else.</b> The heading says they '
             'guide the trips, but three of them are the owner, the operations '
             'manager and the tour designer.'],
            '<p>About seven screens tall on your computer and twelve on a phone, '
            'and nothing at the bottom tells a visitor what to do next.</p>',
            cls='now',
            mockup=mk(ab.now(), 7091)),

        opt('The story, side by side',
            ['<b>Words beside the photo, never under it.</b> The opening puts '
             'SWAT&rsquo;s own sentences next to the Canyonlands group photo, with '
             'Find a Trip and the phone number on the first screen.',
             '<b>The company film</b> (8 minutes, 2023, on YouTube and not on the '
             'new site) fills the video the page already promises, beside '
             'the mission statement.',
             'The group photos sit beside the words about small groups and the '
             'Google rating.',
             '<b>Every guide card says something real</b>: Ann&rsquo;s 25 years as a '
             'park ranger, Phil &ldquo;Utah&rsquo;s Wildlife Ambassador,&rdquo; a '
             'line in their own words. Jason, Julie and Shawn are named for what '
             'they do.'],
            '<p>The closest answer to what you said: each part of the story is a '
            'row with a picture on one side and words on the other. Reads top to '
            'bottom like the page today, just without the dead space. The staff '
            'handbook moves to its own Careers page, linked at the bottom.</p>',
            cost='about 1 day, plus half a day for the Careers page',
            risk='The longest of the three, though still about a third shorter '
                 'than today. It needs a Careers page built to hold the handbook.',
            mockup=mk(ab.opt_story(), 4614,
                      (1, '.ab-open .tx h1'), (2, '.ab-row .ab-film'),
                      (3, '.ab-mos'), (4, '.ab-g4 .ab-card:first-child'))),

        opt('The people come first',
            ['<b>The first thing you see is the seven guides</b>, with a real fact '
             'about each one. Ann gets the big card with a line in her own words.',
             'The company story, the film and the three people who run the trips '
             '(Jason, Julie, Shawn) share one band underneath.',
             'All six group photos in one strip, with the Google rating and the four '
             'accreditations under it.',
             'Careers stays on the page. <b>The handbook is folded shut</b> under it, '
             'for job seekers who open it.'],
            '<p>For someone deciding whether to trust a small company with a week of '
            'their life, the question is who will be with them. This page answers '
            'that before anything else, and it is how SWAT is different from a big '
            'coach company: a 25-year park ranger, 32 years in Utah wildlife and a '
            'harmonica.</p>',
            cost='about 1 day',
            risk='The company story comes second, so someone looking for '
                 '&ldquo;who is this company&rdquo; scrolls past the faces first. '
                 'Somebody has to be the big card, and the team may have a view on '
                 'who.',
            cls='rec',
            mockup=mk(ab.opt_people(), 3825,
                      (1, '.ab-g7 .ab-card:first-child'), (2, '.ab-co .ab-film'),
                      (3, '.ab-strip6'), (4, '.ab-fold'))),

        opt('Everything on the first screen',
            ['<b>Words, buttons and the film on the left, four photos on the '
             'right</b>, all on the first screen.',
             'Four plain facts in one band: groups of 7&ndash;13, local guides, 4.8 '
             'from 255 Google reviews, and the four accreditations.',
             '<b>All ten people in two rows</b>, each with their role and one line.',
             'The mission statement gets the last word, beside the staff photo.'],
            '<p>The shortest page: under half of today. Everything a visitor needs '
            'to trust SWAT is on the first screen, and the rest is proof. The '
            'handbook moves to a Careers page, linked at the bottom.</p>',
            cost='about 1 day, plus half a day for the Careers page',
            risk='Each person gets one short line, so it is the least personal of '
                 'the three. It reads more like a summary than a story.',
            mockup=mk(ab.opt_first(), 3397,
                      (1, '.ab-quad'), (2, '.ab-f4'), (3, '.ab-row10'),
                      (4, '.ab-split blockquote'))),
    ],
    verdict([
        '<b>C, the people come first.</b> The guides are the best thing SWAT has '
        'and the page hides them: ten faces with names only, halfway down. C '
        'leads with them, says something true about each one, and still fits the '
        'company story, the film and the proof in about half the length of '
        'today&rsquo;s page. It is also the cheapest, because Careers and the '
        'handbook stay on this page, folded shut, rather than needing a new page.',
        '<b>B if you want the safest change.</b> Same order as today, fixed: '
        'every photo has words beside it, the film fills the empty promise, the '
        'cards say something. Nobody will be surprised by it.',
        '<b>D if length matters most.</b> It is the shortest, but the people get '
        'one line each, which gives away the thing C is built on.',
        '<b>Whichever you pick, these go:</b> the missing video (the film fills '
        'it), the two buttons that do not exist, the second mission statement, '
        'and the &ldquo;Wynn Hall&rdquo; photo. The handbook leaves the '
        'customer&rsquo;s path in all three. Every word on every drawing is '
        'SWAT&rsquo;s own except headings and buttons, and every fact on a card '
        'is from that person&rsquo;s own profile page.',
    ]),
    since=NEW, cols=4))
