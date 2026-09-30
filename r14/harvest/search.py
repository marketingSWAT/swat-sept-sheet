"""Decision 83: every-day searches against today's matcher and a smarter one.

TODAY = src/lib/trips.ts listTrips: the whole typed phrase, lower-cased, as one
substring of name + positioning + style + departs_from + parks + destinations.
SMART = option B: each word on its own, small spelling slips forgiven, a short
list of everyday words, and the tour's own overview and itinerary searched too
(ranked below a hit in the name or a park)."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, '..', 'data')
CAT = json.load(open(os.path.join(D, 'catalogue.json')))
COUNTS = json.load(open(os.path.join(D, 'counts.json')))

QUERIES = ['zion', 'zion bryce', 'bryce canyon', 'grand canyon', 'yellowstone winter', 'yosemitee',
           'half dome', 'arches from salt lake', 'slc', 'vegas', 'moab', 'sedona', 'hiking',
           'backpacking', 'snowmobile', 'river cruise', 'alaska', 'northern lights', 'mighty five',
           'route 66', 'balloon', 'dinosaurs', 'monument valley', 'hawaii', 'christmas markets',
           'october', 'one day', 'day trip from las vegas', 'national parks', 'family']

def today_text(t):
    return ' '.join([t['name'], t.get('positioning') or '', t['style'], t.get('departs_from') or '',
                     *t['parks'], *t['destinations']]).lower()

def today(q):
    n = q.strip().lower()
    return [t for t in CAT if n in today_text(t)]

STOP = {'from', 'to', 'in', 'the', 'tour', 'tours', 'trip', 'trips', 'a', 'of', 'and', 'for', 'with', 'near'}
SYN = {'slc': 'salt lake', 'vegas': 'las vegas', 'lv': 'las vegas', 'five': '5', 'hiking': 'hik',
       'hike': 'hik', 'hikes': 'hik', 'cruises': 'cruise', 'dinosaurs': 'dinosaur', 'markets': 'market',
       'one': '1', 'backpack': 'backpack'}
MONTH_SEASON = {'march': 'Spring', 'april': 'Spring', 'may': 'Spring', 'june': 'Summer', 'july': 'Summer',
                'august': 'Summer', 'september': 'Autumn', 'october': 'Autumn', 'november': 'Autumn',
                'december': 'Winter', 'january': 'Winter', 'february': 'Winter'}

def norm(s):
    return re.sub(r'[^a-z0-9 ]+', ' ', (s or '').lower().replace('&', ' and '))

def fields(t):
    head = norm(' '.join([t['name'], *t['parks'], *t['destinations'], t.get('departs_from') or '', t['style']]))
    body = norm(' '.join([t.get('positioning') or '', t.get('overview') or '', t.get('highlights_raw') or '',
                          t.get('itinerary_raw') or '']))
    return head, body

F = {t['slug']: fields(t) for t in CAT}
VOCAB = set(w for h, b in F.values() for w in (h + ' ' + b).split())

def lev(a, b):
    if abs(len(a) - len(b)) > 2: return 9
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]

def fix(w):
    if w in VOCAB or len(w) < 5 or any(v.startswith(w) for v in VOCAB): return w
    best = min(VOCAB, key=lambda v: lev(w, v))
    return best if lev(w, best) <= (1 if len(w) < 8 else 2) else w

def smart(q):
    """Returns (trips ranked, what it understood). A month word becomes the
    When filter, which the page already has; 'one day'/'day trip' become the
    day-or-less filter."""
    s = norm(q)
    extra = None
    for m, season in MONTH_SEASON.items():
        if re.search(r'\b' + m + r'\b', s):
            extra = ('season', season); s = re.sub(r'\b' + m + r'\b', ' ', s)
    if re.search(r'\b(1 day|one day|day trip|day tour)\b', s):
        extra = ('day', True); s = re.sub(r'\b(1 day|one day|day trip|day tour)\b', ' ', s)
    words = [SYN.get(w, w) for w in s.split() if w not in STOP]
    words = [fix(w) for w in ' '.join(words).split()]
    out = []
    for t in CAT:
        head, body = F[t['slug']]
        name = norm(t['name'])
        score = 0
        ok = True
        for w in words:
            nw = re.search(r'\b' + re.escape(w), name)
            hw = re.search(r'\b' + re.escape(w), head)
            bw = re.search(r'\b' + re.escape(w), body)
            if not (hw or bw): ok = False; break
            score += 4 if nw else 3 if hw else 1
        if len(words) > 1 and ' '.join(words) in head: score += 5
        if not ok: continue
        if extra and extra[0] == 'day':
            dd = float(t.get('duration_days') or 0)
            if not (t['style'] == 'Day tour' or (0 < dd <= 1)): continue
        out.append((score, t))
    out.sort(key=lambda x: -x[0])
    trips = [t for _, t in out]
    n = len(trips)
    if extra and extra[0] == 'season' and not words:
        n = COUNTS['When'][extra[1]]
    return trips, n, words, extra

rows = []
for q in QUERIES:
    a = today(q)
    b, bn, words, extra = smart(q)
    rows.append({'q': q, 'today': len(a), 'smart': bn, 'first': b[0]['name'] if b else None,
                 'firstSlug': b[0]['slug'] if b else None, 'words': words, 'extra': extra})
    print(f'{q:26} today {len(a):3}  B {bn:3}  {words} {extra}  -> {b[0]["name"] if b else "-"}')
print('zero today', sum(r['today'] == 0 for r in rows), 'zero B', sum(r['smart'] == 0 for r in rows))
json.dump(rows, open(os.path.join(D, 'search.json'), 'w'), indent=1)
