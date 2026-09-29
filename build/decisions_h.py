"""Decision 67, round eight: picking a date on a tour page.

Numbered 67 because 46-51 and 54-66 belong to the dashboard sheet (55 is drawn,
56-66 are briefed there), and a number said out loud has to mean one thing
across every link.

Two designers drew it. Claude drew B, C and D (mocks_i.py); Codex drew E, F
and G from r8/BRIEF.md, as fragments in r8/codex/mocks/ with their notes in
r8/codex/notes/. Codex's panels are loaded here as it left them: the letter,
name, numbered changes, cost and risk are its own words.

The count first (see mocks_i.py). It moved the argument in two places:

  - The drop-down is the smaller half. Opened, the list is 5,322px: six laptop
    screens of Mondays. And the section is the tenth on the page, 7,200px
    below the "Choose your date" button that points at it.
  - 2027 prices differ by date ($2,199 from May 3 to Oct 11, $1,999 the rest)
    and no row says so. Every option drawn here prints the price on the date.
"""

import json
import os

import mocks as m
import mocks_i as i
from sheetkit import opt, quote, verdict, dec

HERE = os.path.dirname(os.path.abspath(__file__))
CODEX = os.path.join(HERE, '..', 'r8', 'codex')

ALL = []

NEW = ('New', '29 Sep')
H = 1000

Q67 = quote(
    ['Something I want to review is this page for departures when you go to '
     'pick your date for booking a tour. I want you and Codex to mock up a '
     'couple new ideas on how we can show this on the website. I just really '
     'feel like we can make this easier and more clear on actually picking '
     'dates, because also when you get into 2027 you have to click that drop '
     'down to see all the other dates.'],
    'Crow, 29 September, with a screenshot of the Mighty 5 from Las Vegas page')


def codex_opt(letter):
    """One of Codex's panels, from the files it wrote. Missing files raise:
    a sheet that quietly drops a designer's option is worse than no build."""
    frag = open(os.path.join(CODEX, 'mocks', f'{letter}.html')).read()
    note = json.load(open(os.path.join(CODEX, 'notes', f'{letter}.json')))
    # Codex writes attribute selectors with double quotes; inside data-sel="" they
    # would end the attribute and the ring script would throw on the rest.
    rings = ''.join(m.ring(n, sel.replace('"', "'")) for n, sel in note.get('rings', []))
    return opt(note['name'], note['changes'], f'<p>{note["body"]}</p>',
               cost=note.get('cost'), risk=note.get('risk'), by='Codex',
               mockup=m.mock(frag + rings, H, aw=1440))


def codex_pick():
    p = os.path.join(CODEX, 'notes', 'pick.json')
    return json.load(open(p)) if os.path.exists(p) else None


def build():
    pick = codex_pick()
    return dec(
        67,
        'Picking a date on a tour page',
        [('Every tour page', ''), ('Crow', 'who'), ('&frac12;&ndash;2 days', ''),
         ('52 of 65 dates behind a button', 'big')],
        [Q67],
        [
            opt('The list, as now',
                ['Only <b>October and November 2026</b> show when the page '
                 'loads. All <b>52 dates in 2027</b> are behind the '
                 '&ldquo;Show all 65 dates&rdquo; button.',
                 '<b>No date shows its price.</b> In 2027 summer costs '
                 '<b>$2,199</b> (May 3 to Oct 11) and the rest <b>$1,999</b>, '
                 'and nothing on the list tells you which is which.',
                 'The panel&rsquo;s &ldquo;Choose your date&rdquo; button '
                 'sends you <b>7,200px down the page</b>: Departures is the '
                 'tenth section, under the gallery.'],
                '<p>Opened, the list grows from 887px to <b>5,322px</b>, six '
                'laptop screens of Mondays, one per row. On a phone it starts '
                'about 16 screens down and opens to about 6 phone screens more. '
                '7 of the 13 dates in 2026 are sold out.</p>',
                cls='now',
                mockup=m.mock(i.now() + m.ring(1, '.dp-fold')
                              + m.ring(2, '.dp-rows li')
                              + m.ring(3, '.dp-cta'), H, aw=1440)),

            opt('The calendar you already approved',
                ['Every month of both years sits in <b>one row</b>. 2027 is '
                 'one tap away, not behind a button.',
                 'Each date is a <b>bar across the five days you are away</b>, '
                 'with its own price on it. Tap the bar to book that date.',
                 'The section stays about <b>780px</b> whichever month is '
                 'open. Sold-out dates stay on the calendar, greyed out, with '
                 'the waiting list beside them.'],
                '<p>This is the calendar you picked for the booking page in '
                'decision 43. It is already built and working there, so this '
                'moves it onto the tour page and teaches it the two things it '
                'never needed on that page: 2026 dates that book on the old '
                'system, and sold out.</p>',
                cost='about 1 day, since the calendar exists',
                risk='One month at a time, so you can&rsquo;t see June and '
                     'September side by side. The date counts on the strip '
                     'are the only overview.',
                cls='rec', by='Claude',
                mockup=m.mock(i.opt_calendar() + m.ring(1, '.dp-strip')
                              + m.ring(2, '.dp-bar')
                              + m.ring(3, '.dp-cal'), H, aw=1440)),

            opt('Every date on one screen',
                ['<b>All 65 dates</b> are on the page at once, one line per '
                 'month. Nothing to open, nothing to switch.',
                 'Each 2027 date shows its <b>price</b>. Summer dates print in '
                 'orange at $2,199, so the difference is visible at a glance.',
                 'Sold-out dates stay where they are, crossed out.',
                 'Tapping a date fills a <b>&ldquo;Your date&rdquo; bar</b> '
                 'with the exact days and price. One more tap books it.'],
                '<p>The most direct answer to &ldquo;I have to click the drop '
                'down&rdquo;: there is no drop-down, and the whole of 2027 '
                'fits in about the space the list takes today with only two '
                'months showing.</p>',
                cost='about 1 day',
                risk='Two taps to book instead of one. Tours with more dates '
                     'than this one make a longer block.',
                by='Claude',
                mockup=m.mock(i.opt_wall() + m.ring(1, '.dp-wall')
                              + m.ring(2, '.dp-dc.peak:not(.on)')
                              + m.ring(3, '.dp-dc.gone')
                              + m.ring(4, '.dp-pick'), H, aw=1440)),

            opt('The year, month by month',
                ['Two tabs, <b>2026</b> and <b>2027</b>, replace the '
                 '&ldquo;Show all&rdquo; button.',
                 'The year is laid out as <b>twelve month cards</b>, four '
                 'across, so a whole year fits on one screen.',
                 'Each date is a row with its price and a Book link.'],
                '<p>The smallest change from today: it is still a list of '
                'dates, just cut into months you can see side by side.</p>',
                cost='about &frac12; day',
                risk='The Book links are small for this audience; making them '
                     'proper buttons makes every card taller. The 2026 tab '
                     'holds only 13 dates, 7 of them sold out.',
                by='Claude',
                mockup=m.mock(i.opt_year() + m.ring(1, '.dp-tabs')
                              + m.ring(2, '.dp-ycard')
                              + m.ring(3, '.dp-yr-row'), H, aw=1440)),

        ] + ([] if os.environ.get('R8_NO_CODEX') else
             [codex_opt('E'), codex_opt('F'), codex_opt('G')]),
        verdict([
            '<b>B, the calendar you already approved.</b> It fixes the '
            'drop-down (every month is one tap), it prints the price on every '
            '2027 date, and it is the one option that is mostly built: the '
            'same calendar runs on the booking page you signed off in '
            'decision 43. Most customers are choosing &ldquo;which week can I '
            'be away&rdquo;, and a bar across Monday to Friday answers that '
            'better than a list of Mondays.',
            '<b>C if you want every date visible without a single tap.</b> It '
            'is the plainest answer to your note, and the one to pick if you '
            'think people will scan the whole year before choosing.',
            (f'<b>Codex&rsquo;s own pick of its three is {pick["pick"]}.</b> '
             f'{pick["why"]}' if pick else ''),
            '<b>Of Codex&rsquo;s three, E has the idea worth stealing.</b> It '
            'opens the dates right where the orange &ldquo;Choose your '
            'date&rdquo; button is, instead of dropping you 7,200px down the '
            'page. That works with any of the others: B&rsquo;s calendar '
            'could open from that button too, for about a day more. The faded '
            'text behind E&rsquo;s pop-up is Codex&rsquo;s filler, not copy '
            'from the live page.',
            '<b>Whichever you pick, two things come with it.</b> Every date '
            'shows its price, and sold-out dates keep their waiting-list line. '
            'Seat counts stay off, as before: they would advertise an empty '
            'bus. The hot deal Codex drew in E and F is an example, labelled '
            'as one; this tour has no deal today.',
        ]),
        since=NEW, cols=2)


ALL.append(build())
